#!/usr/bin/env python3
"""Localize remote images per Munish's local-only image policy (2026-10-02).

- Downloads every unique image_url from bank + visual-backfill + tests.
- HTTP 200 + image/* required; otherwise the URL is recorded dead and the
  item is flagged (image_url rewritten to the intended local path with
  "image_unavailable": true so the validator gate surfaces it).
- Saves under assets/images/u<unit>/<item_id>.<ext> (dedupe by URL).
- Images with max dimension > 1600px are downscaled (LANCZOS); JPEG
  re-encoded at quality 82. Never upscaled, never cropped. SVG kept raw.
- Rewrites image_url to the repo-relative local path; preserves
  image_license/image_verified; adds image_source_url + image_local_verified.

Run: python3 build/localize_images.py [--rewrite] [--check FILE]
  --rewrite : actually rewrite the content JSON files (default: dry run)
  --check FILE : use a pre-run HEAD-check report (lines: "<code> <ct> :: <url>")
                 to skip known-dead URLs without a GET attempt.
Writes build/image-download-report.json in all modes.
"""
import json
import os
import re
import subprocess
import sys
import urllib.request
from datetime import date
from PIL import Image, ImageFile
# Large but legitimate images exist (208M px seen); raise the limit while
# still keeping a bomb guard at ~4x the observed max. Individual image
# processing errors are caught per-URL so one bad file can't kill the run.
Image.MAX_IMAGE_PIXELS = 800_000_000
ImageFile.LOAD_TRUNCATED_IMAGES = False

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(REPO, "build")
ASSETS = os.path.join(REPO, "assets", "images")
TODAY = date.today().isoformat()

EXT_BY_CT = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
    "image/tiff": ".tif",
    "image/bmp": ".bmp",
}


def iter_content():
    """Yield (item_dict, unit, file_path) for bank + backfill + tests
    + fresh-written + reconceived (every dir the validator's
    finished_items() scans)."""
    bpath = os.path.join(BUILD, "bank", "mcq-bank.json")
    for it in json.load(open(bpath)):
        yield it, it.get("unit"), bpath
    import glob as g
    for f in sorted(g.glob(os.path.join(BUILD, "visual-backfill", "*",
                                        "batch-*.json"))):
        for it in json.load(open(f)):
            yield it, it.get("unit"), f
    for f in sorted(g.glob(os.path.join(BUILD, "tests", "test-*.json"))):
        t = json.load(open(f))
        for q in t.get("section_1a", {}).get("questions", []):
            yield q, q.get("unit"), f
        # DBQ documents live in section_2a
        for doc in t.get("section_2a", {}).get("dbq", {}).get("documents",
                                                              []) or []:
            if isinstance(doc, dict) and doc.get("image_url"):
                doc = dict(doc)
                doc["id"] = f"{t.get('id', 'test')}-dbq-doc{doc.get('n', '?')}"
                yield doc, "dbq", f
    for root in ("fresh-written", "reconceived"):
        rd = os.path.join(BUILD, root)
        if not os.path.isdir(rd):
            continue
        for f in sorted(g.glob(os.path.join(rd, "**", "*.json"),
                                recursive=True)):
            if "mapping" in os.path.basename(f).lower():
                continue
            try:
                d = json.load(open(f))
            except Exception:
                continue
            items = d if isinstance(d, list) else d.get("items") or \
                d.get("questions") or []
            for it in items:
                if isinstance(it, dict) and it.get("stem"):
                    yield it, it.get("unit"), f
    # DBQ documents (frq-remapped/dbqs): finished content, image_url refs
    # must go local too. Synthetic item id "<dbq_id>-doc<n>".
    for f in sorted(g.glob(os.path.join(BUILD, "frq-remapped", "dbqs",
                                        "*.json"))):
        try:
            d = json.load(open(f))
        except Exception:
            continue
        dbq_id = d.get("id", os.path.basename(f).replace(".json", ""))
        for doc in d.get("documents", []) or []:
            if isinstance(doc, dict) and doc.get("image_url"):
                doc = dict(doc)
                doc["id"] = f"{dbq_id}-doc{doc.get('n', '?')}"
                yield doc, "dbq", f


def main():
    rewrite = "--rewrite" in sys.argv
    head_known = {}
    if "--check" in sys.argv:
        cp = sys.argv[sys.argv.index("--check") + 1]
        for line in open(cp):
            line = line.strip()
            if not line or line == "DONE":
                continue
            m = re.match(r"^(\S+)\s+(\S+)\s+::\s+(.*)$", line)
            if m:
                head_known[m.group(3)] = (m.group(1), m.group(2))

    # url -> {item_id, unit, files:set}
    urlmap = {}
    for item, unit, fpath in iter_content():
        u = item.get("image_url")
        if not u or not str(u).startswith("http"):
            continue
        e = urlmap.setdefault(u, {"item_id": item.get("id"), "unit": unit,
                                  "files": set()})
        e["files"].add(fpath)

    print(f"unique remote urls: {len(urlmap)}")
    rp = os.path.join(BUILD, "image-download-report.json")
    report = {"date": TODAY, "downloaded": {}, "dead": {}, "skipped": []}
    # resume: keep progress already written by a previous (crashed) run
    if os.path.isfile(rp):
        try:
            prev = json.load(open(rp))
            for url, rec in prev.get("downloaded", {}).items():
                if os.path.isfile(os.path.join(REPO, rec["local_path"])):
                    report["downloaded"][url] = rec
            report["dead"].update(prev.get("dead", {}))
            print(f"resuming: {len(report['downloaded'])} downloaded, "
                  f"{len(report['dead'])} dead already known")
        except Exception:
            pass
    CT_BY_EXT = {v: k for k, v in EXT_BY_CT.items()}

    def resume_dest(meta):
        """Reuse a file left on disk by a crashed pre-report run (names
        are deterministic: assets/images/<subdir>/<item_id>.<ext>)."""
        unit = meta["unit"]
        sub = unit if isinstance(unit, str) else f"u{unit or 0}"
        d = os.path.join(REPO, "assets", "images", sub)
        base = meta["item_id"]
        if not base or not os.path.isdir(d):
            return None
        hits = sorted(f for f in os.listdir(d)
                      if f.startswith(base + "."))
        if hits:
            return os.path.join("assets", "images", f"u{unit}", hits[0])
        return None

    for url, meta in sorted(urlmap.items()):
        if url in report["downloaded"] or url in report["dead"]:
            # already have it: still refresh the files list so --rewrite
            # covers files discovered after the URL was first downloaded
            rec = report["downloaded"].get(url) or report["dead"].get(url)
            known = set(rec.get("files", []))
            known.update(sorted(meta["files"]))
            rec["files"] = sorted(known)
            report["skipped"].append(url)
            continue
        rdest = resume_dest(meta)
        if rdest:
            full = os.path.join(REPO, rdest)
            ext = "." + rdest.rsplit(".", 1)[-1]
            report["downloaded"][url] = {
                "local_path": rdest, "bytes": os.path.getsize(full),
                "content_type": CT_BY_EXT.get(ext, "unknown"),
                "note": "resumed: already downloaded by earlier partial run",
                **meta, "files": sorted(meta["files"])}
            print(f"RESUME {rdest}")
            json.dump(report, open(rp, "w"), indent=1)
            continue
        hc = head_known.get(url)
        if hc and (hc[0] != "200" or not hc[1].startswith("image/")):
            report["dead"][url] = {"reason": f"HEAD {hc[0]} {hc[1]}",
                                   **meta, "files": sorted(meta["files"])}
            print(f"DEAD (head) {url}")
            continue
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "ap-world-content-bot/1.0 (localization)"})
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status != 200:
                    raise IOError(f"HTTP {r.status}")
                ct = r.headers.get("Content-Type", "").split(";")[0].strip()
                if not ct.startswith("image/"):
                    raise IOError(f"content-type {ct}")
                data = r.read()
            if len(data) > 100 * 1024 * 1024:  # 100MB hard cap per file
                raise IOError(f"too large: {len(data)} bytes")
        except Exception as e:
            report["dead"][url] = {"reason": str(e), **meta,
                                   "files": sorted(meta["files"])}
            print(f"DEAD {url} ({e})")
            json.dump(report, open(rp, "w"), indent=1)  # flush progress
            continue
        ext = EXT_BY_CT.get(ct, ".bin")
        unit = meta["unit"]
        sub = unit if isinstance(unit, str) else f"u{unit or 0}"
        fname = f"{meta['item_id']}{ext}"
        rel = os.path.join("assets", "images", sub, fname)
        dest = os.path.join(REPO, rel)
        try:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            if ct == "image/svg+xml":
                open(dest, "wb").write(data)  # keep raw, never rasterize
                note = "svg kept raw"
            else:
                import io
                im = Image.open(io.BytesIO(data))
                im.load()
                w, h = im.size
                if max(w, h) > 1600:
                    scale = 1600 / max(w, h)
                    im = im.resize((int(w * scale), int(h * scale)),
                                   Image.LANCZOS)
                    note = f"downscaled {w}x{h} -> {im.size[0]}x{im.size[1]}"
                else:
                    note = f"kept as-is {w}x{h}"
                save_kw = {"quality": 82} if ext == ".jpg" else {}
                if ext == ".jpg" and im.mode in ("RGBA", "P"):
                    im = im.convert("RGB")
                im.save(dest, **save_kw)
        except Exception as e:
            report["dead"][url] = {"reason": f"processing failed: {e}",
                                   **meta, "files": sorted(meta["files"])}
            print(f"DEAD {url} (processing: {e})")
            json.dump(report, open(rp, "w"), indent=1)  # flush progress
            continue
        sz = os.path.getsize(dest)
        report["downloaded"][url] = {"local_path": rel, "bytes": sz,
                                     "content_type": ct, "note": note,
                                     **meta, "files": sorted(meta["files"])}
        print(f"OK {rel} ({sz}b) {note}")
        json.dump(report, open(rp, "w"), indent=1)  # flush progress

    # rewrite content files surgically (string replacement: preserves file
    # formatting, keeps the diff to exactly the image_url lines)
    def rewrite_file(fpath, url, new_image_url, extra_fields):
        text = open(fpath).read()
        old = f'"image_url": "{url}"'
        n = text.count(old)
        if n == 0:
            print(f"WARN: {url} not found as image_url in {fpath}")
            return False
        out_lines = []
        for line in text.split("\n"):
            if old in line:
                indent = line[:len(line) - len(line.lstrip())]
                rep = f'{indent}"image_url": "{new_image_url}",'
                for k, v in extra_fields:
                    rep += f'\n{indent}{json.dumps(k)}: {json.dumps(v)},'
                rep = rep.rstrip(",")
                line = line.replace(old, rep, 1)
            out_lines.append(line)
        open(fpath, "w").write("\n".join(out_lines))
        return True

    if rewrite:
        touched = set()
        for url, rec in report["downloaded"].items():
            for fpath in rec["files"]:
                if rewrite_file(
                        fpath, url, rec["local_path"],
                        [("image_source_url", url),
                         ("image_local_verified", TODAY)]):
                    touched.add(fpath)
        for url, rec in report["dead"].items():
            unit = rec.get("unit")
            sub = unit if isinstance(unit, str) else f"u{unit or 0}"
            rel = os.path.join("assets", "images", sub,
                               f"{rec.get('item_id')}.missing")
            for fpath in rec["files"]:
                if rewrite_file(
                        fpath, url, rel,
                        [("image_source_url", url),
                         ("image_local_verified", TODAY),
                         ("image_unavailable", True)]):
                    touched.add(fpath)
        print(f"rewrote {len(touched)} files")

    rp = os.path.join(BUILD, "image-download-report.json")  # (kept for clarity)
    json.dump(report, open(rp, "w"), indent=1)
    print(f"report: {rp}")
    print(f"downloaded {len(report['downloaded'])}, "
          f"dead {len(report['dead'])}")


if __name__ == "__main__":
    main()
