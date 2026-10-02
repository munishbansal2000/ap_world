#!/usr/bin/env python3
"""Merge tagging results (skill_code/topic_code) into finished-layer JSONs.

String-surgery merge: inserts the two fields right after each item's
"id" line, preserving every other byte (formatting, key order, content).
Same ids, no reordering, no content changes.

Run: python3 build/merge_tags.py [--check]
  --check : verify only -- report which ids would be tagged / are missing.
"""
import glob as g
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(REPO, "build")
CHECK = "--check" in sys.argv


def target_files():
    files = [os.path.join(BUILD, "bank", "mcq-bank.json")]
    for pat in [os.path.join(BUILD, "visual-backfill", "**", "*.json"),
                os.path.join(BUILD, "fresh-written", "**", "*.json"),
                os.path.join(BUILD, "reconceived", "**", "*.json")]:
        for f in sorted(g.glob(pat, recursive=True)):
            if "mapping" not in os.path.basename(f).lower():
                files.append(f)
    return files


def load_tags():
    tags = {}
    for f in sorted(g.glob(os.path.join(BUILD, "tagging", "results",
                                        "batch-*-tags.json"))):
        for r in json.load(open(f)):
            iid = r.get("id")
            if not iid:
                continue
            if iid in tags and tags[iid] != (r.get("skill_code"),
                                             r.get("topic_code")):
                print(f"WARN: conflicting tags for {iid}: "
                      f"{tags[iid]} vs {(r.get('skill_code'), r.get('topic_code'))}")
            tags[iid] = (r.get("skill_code"), r.get("topic_code"))
    return tags


def merge_file(path, tags):
    text = open(path).read()
    if '"skill_code"' in text:
        # already merged (or partially) -- only fill gaps
        pass
    out_lines = []
    n_tagged = 0
    lines = text.split("\n")
    # robust approach: parse JSON, find ids lacking skill_code, then
    # surgical-insert only for those ids.
    try:
        d = json.load(open(path))
    except Exception as e:
        print(f"WARN: {path} not parseable ({e}); skipped")
        return 0, 0
    items = d if isinstance(d, list) else d.get("items") or \
        d.get("questions") or []
    need = {}
    for it in items:
        if isinstance(it, dict) and it.get("id") and not it.get("skill_code") \
                and it.get("id") in tags:
            need[it["id"]] = tags[it["id"]]
    if CHECK:
        return 0, len(need)
    # Fast path: "id" on its own line (pretty-printed files). Only used
    # when it tags every needed id; otherwise fall through to inline.
    line_ids = re.findall(r'^[ \t]*"id"\s*:\s*"([^"]+)"\s*,?\s*$', text,
                          re.M)
    n_tagged = 0
    if line_ids:
        out_lines = []
        for line in lines:
            m = re.match(r'^([ \t]*)"id"\s*:\s*"([^"]+)"\s*(,?)\s*$', line)
            if m and m.group(2) in need:
                indent = m.group(1)
                sc, tc = need[m.group(2)]
                if m.group(3):
                    # more keys follow the id line
                    out_lines.append(line)
                    out_lines.append(f'{indent}"skill_code": "{sc}",')
                    out_lines.append(f'{indent}"topic_code": "{tc}",')
                else:
                    # id was the last key: add comma, no trailing comma
                    # on the final inserted line
                    out_lines.append(line + ",")
                    out_lines.append(f'{indent}"skill_code": "{sc}",')
                    out_lines.append(f'{indent}"topic_code": "{tc}"')
                n_tagged += 1
            else:
                out_lines.append(line)
        if n_tagged == len(need):
            open(path, "w").write("\n".join(out_lines))
            return n_tagged, 0
    # Fallback: compact/single-line JSON -- inline insertion after the
    # "id" pair (byte-preserving except the inserted fields).
    n_tagged = 0

    def rep(m):
        nonlocal n_tagged
        iid = m.group(1)
        if iid not in need:
            return m.group(0)
        sc, tc = need[iid]
        n_tagged += 1
        return f'"id": "{iid}", "skill_code": "{sc}", "topic_code": "{tc}"'

    new_text, _ = re.subn(r'"id":\s*"([^"]+)"', rep, text)
    if n_tagged:
        open(path, "w").write(new_text)
    return n_tagged, 0


def main():
    tags = load_tags()
    print(f"tag results loaded: {len(tags)} unique ids")
    total = 0
    for path in target_files():
        n, want = merge_file(path, tags)
        if CHECK:
            total += want
            if want:
                print(f"  {os.path.relpath(path, REPO)}: would tag {want}")
        else:
            total += n
            if n:
                print(f"  {os.path.relpath(path, REPO)}: +{n}")
    print(f"{'would tag' if CHECK else 'tagged'} {total} item occurrences "
          f"across {len(target_files())} files")


if __name__ == "__main__":
    main()
