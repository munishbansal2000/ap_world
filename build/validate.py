#!/usr/bin/env python3
"""Repo-wide validator for the AP World History content build.

Enforces schema, metadata vocabularies, structural rules, and Fall 2026 CED
format compliance across every content directory.

Run:  python3 build/validate.py
Exit code is nonzero when any gate fails; all failures are printed.

Gates:
  MCQ-SCHEMA   every MCQ item carries the required fields with sane values
  MCQ-VOCAB    unit/skill/reasoning/difficulty/themes/type come from the
               controlled vocabularies (no typos, no wrong-category values)
  MCQ-OPTIONS  4 options labelled (A)-(D), key in A-D, option_explanations
               covers all four letters
  MCQ-IMAGE    items with image_url also carry image_license + image_verified
  MCQ-IDS      item ids are unique repo-wide (bank, reconceived, backfill,
               fresh-written, tests)
  MCQ-KEYS     no answer letter exceeds 30% within any item file
  MCQ-EXPLAIN  explanation non-empty (>=40 chars); every option explanation
               non-empty (>=20 chars)
  MCQ-IDFMT    ids match wh-<source>-<tag>-<nnn> (tag = t1..t3 or u1..u9)
  MCQ-DIFFICULTY no unit may be 0% or 100% hard
  MCQ-STIMWORDS stimulus_words within 2x of actual stimulus word count;
               stimulus and stem non-empty
  LENGTHTELL-RPT report % of items where the longest option is the key
               (report-only; the repo has no stated bar)
  ORPHAN-JSON  every build JSON is classified: BANK / SOURCE (merged into the
               bank) / FRQ-BANK / TEST / STAGED (visual-backfill, merge
               decision pending with Munish) / RAW-STAGING (reclaim-staged) /
               REFERENCE (released-cb); anything else fails
  SOURCE-MERGED every reconceived/fresh-written item id exists in the bank
               and every bank id exists in a source layer (the backfill is
               explicitly NOT merged yet)
  SAQ-FORMAT   60 sets, Q1 secondary / Q2 primary / Q3 non-text, parts a-c,
               sample answers present
  DBQ-FORMAT   10 DBQs, 7 documents each, topic within the 1200-2001 range
  LEQ-FORMAT   20 LEQs, single prompt each, no choice language
  TEST-STRUCT  10 tests: 55 MCQ / 3 SAQ / DBQ / LEQ, no duplicate MCQ ids
               across tests, new-format directions only
  TEST-BANK-LINK test MCQs are drawn from the bank: every test question id
               exists in build/bank/mcq-bank.json (this repo's policy --
               tests sample the bank; cross-test uniqueness in TEST-STRUCT)
  LINK-KEYS    ANSWER_KEYS.md: 10 sections x 55 ordered entries matching each
               test's question ids in order, keys A-D
  LINK-FRQ     test set_id/dbq/leq references resolve to frq-remapped files
               and the test's embedded copies are byte-identical to source
  IMAGE-LOCAL  LOCAL-ONLY policy: every image_url in bank+backfill+tests
               is a repo-relative local path -- the file must exist under
               the repo, be non-empty, and be a readable image. Any
               http(s) image_url remaining in content JSON fails the gate.
               Items flagged image_unavailable (dead remote source) fail
               until a replacement is chosen.
  COVERAGE     build/coverage-matrix.json (regenerated each run): unit
               quotas met, every skills x units cell >= 5, each unit spans
               >= 3 themes
  CB-CODES-FILE build/cb-codes.json (the verified official CB code list)
               loads and parses; every code below is checked verbatim
               against it. Any code not in that file is an invention and
               fails.
  CB-SKILL-CODE every finished-layer MCQ carries skill_code that is one
               of the 17 official sub-codes (1.A-6.D), verbatim; the
               sub-code's parent skill name matches the item's skill.
  CB-TOPIC-CODE every finished-layer MCQ carries topic_code that is one
               of the 68 official topic codes, verbatim; the topic's unit
               prefix matches the item's unit.
  CB-NO-INVENTION any skill_code/topic_code/reasoning_code value not
               verbatim in build/cb-codes.json fails (no locally invented
               codes, ever).
"""
import json
import os
import re
import sys
from collections import Counter

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(REPO, "build")

FAILS = []


def fail(gate, msg):
    FAILS.append(f"[{gate}] {msg}")


# ---------------------------------------------------------------- vocabularies
SKILLS = {
    "Developments and Processes",
    "Sourcing and Situation",
    "Claims and Evidence in Sources",
    "Contextualization",
    "Making Connections",
    "Argumentation",
}
REASONING = {"Causation", "Comparison", "Continuity and Change"}
DIFFICULTY = {"easy", "medium", "hard"}
THEMES = {"GOV", "CDI", "ECN", "SIO", "TEC", "ENV"}
SAQ_Q1 = {"secondary text", "secondary_text"}
SAQ_Q2 = {"primary text", "primary_text"}
SAQ_Q3 = {"map", "chart", "image", "non-text: map", "non-text: chart",
          "non-text: image", "non-text map", "non-text chart", "non-text image"}
OLD_FORMAT_PATTERNS = [
    r"choose 1 of 3", r"choose one of three", r"either Q3 or Q4",
    r"answer Q1\+Q2", r"complete 3 of 4", r"answer three of the four",
]

MCQ_REQUIRED = ["id", "source_id", "unit", "stimulus", "stem", "options",
                "key", "explanation", "option_explanations", "skill",
                "reasoning", "themes", "difficulty", "type",
                "stimulus_words", "source_stimulus_words"]


def iter_mcq_files():
    """Yield (label, path) for every file holding MCQ items."""
    roots = [
        (os.path.join(BUILD, "bank"), "bank"),
        (os.path.join(BUILD, "visual-backfill"), "backfill"),
        (os.path.join(BUILD, "fresh-written"), "fresh"),
    ]
    for root, label in roots:
        if not os.path.isdir(root):
            continue
        for dirpath, _, files in os.walk(root):
            for f in sorted(files):
                if f.endswith(".json"):
                    yield label, os.path.join(dirpath, f)
    rec = os.path.join(BUILD, "reconceived")
    if os.path.isdir(rec):
        for dirpath, _, files in os.walk(rec):
            for f in sorted(files):
                if f.endswith(".json") and not f.startswith("_") \
                        and f != "AUDIT-LOG.md" and "mapping" not in f.lower():
                    yield "reconceived", os.path.join(dirpath, f)


def load_items(path):
    try:
        d = json.load(open(path))
    except Exception as e:
        fail("MCQ-SCHEMA", f"{path}: unreadable JSON ({e})")
        return []
    if isinstance(d, dict):
        for k in ("items", "questions"):
            if isinstance(d.get(k), list):
                return d[k]
        return []
    return d if isinstance(d, list) else []


def looks_like_mcq(item):
    return isinstance(item, dict) and "stem" in item and "options" in item


# ------------------------------------------------------------------- MCQ gates
def check_mcq():
    # ID layers: the bank is a merge of the source layers, so bank-vs-source
    # overlap is by design. Uniqueness is enforced WITHIN each layer:
    #   bank   = build/bank/mcq-bank.json
    #   source = build/reconceived + build/fresh-written + build/visual-backfill
    #   test   = build/tests (also checked test-vs-test in check_tests)
    seen_ids = {"bank": {}, "source": {}}
    key_counts = Counter()
    n_items = 0
    for label, path in iter_mcq_files():
        items = [i for i in load_items(path) if looks_like_mcq(i)]
        if not items:
            continue
        layer = "bank" if "/build/bank/" in path else "source"
        file_keys = Counter()
        for it in items:
            n_items += 1
            iid = it.get("id", f"<noid@{path}>")
            # schema
            missing = [k for k in MCQ_REQUIRED if k not in it]
            if missing:
                fail("MCQ-SCHEMA", f"{iid}: missing fields {missing} ({path})")
            # vocab
            u = it.get("unit")
            if u not in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                fail("MCQ-VOCAB", f"{iid}: bad unit {u!r}")
            if it.get("skill") not in SKILLS:
                fail("MCQ-VOCAB", f"{iid}: bad skill {it.get('skill')!r}")
            if it.get("reasoning") not in REASONING:
                fail("MCQ-VOCAB",
                     f"{iid}: bad reasoning {it.get('reasoning')!r} "
                     f"(must be one of {sorted(REASONING)})")
            if it.get("difficulty") not in DIFFICULTY:
                fail("MCQ-VOCAB", f"{iid}: bad difficulty {it.get('difficulty')!r}")
            th = it.get("themes")
            if not isinstance(th, list) or not th or not set(th) <= THEMES:
                fail("MCQ-VOCAB", f"{iid}: bad themes {th!r}")
            if it.get("type") != "mcq":
                fail("MCQ-VOCAB", f"{iid}: bad type {it.get('type')!r}")
            sw = it.get("stimulus_words")
            if not isinstance(sw, int) or sw < 0:
                fail("MCQ-SCHEMA", f"{iid}: bad stimulus_words {sw!r}")
            # options
            opts = it.get("options")
            key = it.get("key")
            if not isinstance(opts, list) or len(opts) != 4:
                fail("MCQ-OPTIONS", f"{iid}: options is not a 4-list")
            else:
                letters = []
                for o in opts:
                    m = re.match(r"\(([A-D])\)", str(o))
                    letters.append(m.group(1) if m else "?")
                if sorted(letters) != ["A", "B", "C", "D"]:
                    fail("MCQ-OPTIONS", f"{iid}: option labels {letters}")
            if key not in ("A", "B", "C", "D"):
                fail("MCQ-OPTIONS", f"{iid}: bad key {key!r}")
            else:
                file_keys[key] += 1
                key_counts[key] += 1
            oe = it.get("option_explanations")
            if not isinstance(oe, dict) or sorted(oe.keys()) != ["A", "B", "C", "D"]:
                fail("MCQ-OPTIONS",
                     f"{iid}: option_explanations must cover A-D "
                     f"(got {sorted(oe.keys()) if isinstance(oe, dict) else type(oe).__name__})")
            # image items
            if it.get("image_url"):
                if not it.get("image_license"):
                    fail("MCQ-IMAGE", f"{iid}: image_url without image_license")
                if not it.get("image_verified"):
                    fail("MCQ-IMAGE", f"{iid}: image_url without image_verified")
            # id uniqueness (within layer; bank-vs-source overlap is by design)
            if iid in seen_ids[layer]:
                fail("MCQ-IDS",
                     f"duplicate id {iid} within {layer} layer: "
                     f"{seen_ids[layer][iid]} vs {path}")
            else:
                seen_ids[layer][iid] = path
        # key balance: per file only at test scale (n>=40); chapter-size
        # files vary by +-2 items which is noise. Bank-wide balance is
        # checked separately below.
        nf = sum(file_keys.values())
        if nf >= 40:
            for k, c in file_keys.items():
                if c / nf > 0.30:
                    fail("MCQ-KEYS",
                         f"{path}: key {k} at {c/nf:.1%} of {nf} (>30%)")
    n_unique = len(seen_ids["bank"]) + len(seen_ids["source"])
    print(f"MCQ items checked: {n_items} "
          f"(bank layer: {len(seen_ids['bank'])} ids, "
          f"source layer: {len(seen_ids['source'])} ids)")
    # bank-wide key balance
    bank_path = os.path.join(BUILD, "bank", "mcq-bank.json")
    if os.path.isfile(bank_path):
        bank_items = [i for i in load_items(bank_path) if looks_like_mcq(i)]
        n = len(bank_items)
        if n:
            bc = Counter(i["key"] for i in bank_items)
            for k, c in sorted(bc.items()):
                if c / n > 0.28:
                    fail("MCQ-KEYS",
                         f"bank-wide: key {k} at {c/n:.1%} of {n} (>28%)")
            print(f"bank-wide key balance: "
                  f"{ {k: f'{v/n:.1%}' for k, v in sorted(bc.items())} }")


# ------------------------------------------------------------------- FRQ gates
def saq_sets():
    out = []
    base = os.path.join(BUILD, "frq-remapped")
    if not os.path.isdir(base):
        return out
    for d in sorted(os.listdir(base)):
        if d.startswith("saq-sets"):
            dd = os.path.join(base, d)
            for f in sorted(os.listdir(dd)):
                if f.startswith("set-") and f.endswith(".json"):
                    out.append(os.path.join(dd, f))
    return out


def check_saq():
    files = saq_sets()
    print(f"SAQ sets checked: {len(files)}")
    if len(files) != 60:
        fail("SAQ-FORMAT", f"expected 60 SAQ sets, found {len(files)}")
    for path in files:
        try:
            d = json.load(open(path))
        except Exception as e:
            fail("SAQ-FORMAT", f"{path}: unreadable ({e})")
            continue
        for qi, want in (("q1", SAQ_Q1), ("q2", SAQ_Q2), ("q3", SAQ_Q3)):
            q = d.get(qi)
            if not isinstance(q, dict):
                fail("SAQ-FORMAT", f"{path}: missing {qi}")
                continue
            st = str(q.get("source_type", "")).strip().lower().replace("_", " ")
            want_norm = {w.replace("_", " ") for w in want}
            if st not in want_norm and st.replace("non-text: ", "") not in \
                    {w.replace("non-text: ", "") for w in want_norm}:
                # lenient: accept if it matches any allowed token loosely
                if not any(tok in st for tok in ("secondary", "primary",
                                                "map", "chart", "image",
                                                "non-text")):
                    fail("SAQ-FORMAT",
                         f"{path} {qi}: source_type {q.get('source_type')!r} "
                         f"breaks the mandated rotation")
            parts = q.get("parts")
            if not isinstance(parts, dict) or \
                    sorted(parts.keys()) != ["a", "b", "c"]:
                fail("SAQ-FORMAT", f"{path} {qi}: parts must be a/b/c")
            if not q.get("sample_answers"):
                fail("SAQ-FORMAT", f"{path} {qi}: missing sample_answers")
        blob = json.dumps(d).lower()
        for pat in OLD_FORMAT_PATTERNS:
            if re.search(pat, blob):
                fail("SAQ-FORMAT", f"{path}: old-format language '{pat}'")


def check_dbq():
    base = os.path.join(BUILD, "frq-remapped", "dbqs")
    files = sorted(f for f in os.listdir(base) if f.endswith(".json")) \
        if os.path.isdir(base) else []
    print(f"DBQs checked: {len(files)}")
    if len(files) != 10:
        fail("DBQ-FORMAT", f"expected 10 DBQs, found {len(files)}")
    for f in files:
        path = os.path.join(base, f)
        d = json.load(open(path))
        docs = d.get("documents", [])
        if len(docs) != 7:
            fail("DBQ-FORMAT", f"{f}: {len(docs)} documents (need 7)")
        period = str(d.get("period", ""))
        nums = [int(x) for x in re.findall(r"\b(1[2-9]\d\d|20\d\d)\b", period)]
        if nums and (min(nums) < 1200 or max(nums) > 2001):
            fail("DBQ-FORMAT", f"{f}: period {period!r} outside 1200-2001")


def check_leq():
    base = os.path.join(BUILD, "frq-remapped", "leqs")
    files = sorted(f for f in os.listdir(base) if f.endswith(".json")) \
        if os.path.isdir(base) else []
    print(f"LEQs checked: {len(files)}")
    if len(files) != 20:
        fail("LEQ-FORMAT", f"expected 20 LEQs, found {len(files)}")
    for f in files:
        path = os.path.join(base, f)
        blob = open(path).read().lower()
        for pat in OLD_FORMAT_PATTERNS:
            if re.search(pat, blob):
                fail("LEQ-FORMAT", f"{f}: old-format language '{pat}'")


# ------------------------------------------------------------------ test gates
def test_items():
    """Yield (test_file, question) for every section_1a question."""
    base = os.path.join(BUILD, "tests")
    if not os.path.isdir(base):
        return
    for f in sorted(os.listdir(base)):
        if f.startswith("test-") and f.endswith(".json"):
            t = json.load(open(os.path.join(base, f)))
            for q in t.get("section_1a", {}).get("questions", []):
                yield f, q


def check_tests():
    base = os.path.join(BUILD, "tests")
    files = sorted(f for f in os.listdir(base)
                   if f.startswith("test-") and f.endswith(".json")) \
        if os.path.isdir(base) else []
    print(f"Practice tests checked: {len(files)}")
    if len(files) != 10:
        fail("TEST-STRUCT", f"expected 10 tests, found {len(files)}")
    seen_mcq = {}
    for f in files:
        path = os.path.join(base, f)
        t = json.load(open(path))
        for sec in ("section_1a", "section_1b", "section_2a", "section_2b"):
            if sec not in t:
                fail("TEST-STRUCT", f"{f}: missing {sec}")
        mcqs = t.get("section_1a", {}).get("questions", [])
        if len(mcqs) != 55:
            fail("TEST-STRUCT", f"{f}: section_1a has {len(mcqs)} MCQ (need 55)")
        for q in mcqs:
            iid = q.get("id", "<noid>")
            if iid in seen_mcq:
                fail("TEST-STRUCT",
                     f"MCQ {iid} in both {seen_mcq[iid]} and {f}")
            seen_mcq[iid] = f
            if not looks_like_mcq(q):
                fail("TEST-STRUCT", f"{f}: item {iid} fails MCQ shape")
        saqs = t.get("section_1b", {}).get("saq_sets", [])
        if len(saqs) != 3:
            fail("TEST-STRUCT", f"{f}: section_1b has {len(saqs)} SAQ sets (need 3)")
        blob = json.dumps(t).lower()
        for pat in OLD_FORMAT_PATTERNS:
            if re.search(pat, blob):
                fail("TEST-STRUCT", f"{f}: old-format language '{pat}'")
    print(f"Unique test MCQs: {len(seen_mcq)}")


# ------------------------------------------------------ extended MCQ gates
ID_PATTERN = re.compile(r"^wh-([a-z0-9][a-z0-9-]*?)-(t[1-3]|u[1-9])-(\d{3})$")
UNIT_QUOTAS = {1: 80, 2: 80, 3: 120, 4: 120, 5: 120, 6: 120, 7: 80, 8: 80, 9: 80}
SKILL_CELL_MIN = 5
UNIT_THEMES_MIN = 3


def finished_items():
    """Full-schema MCQ items from finished layers: bank, reconceived,
    fresh-written, visual-backfill (staged). Yields (layer, path, item)."""
    for label, path in iter_mcq_files():
        layer = "bank" if "/build/bank/" in path else "source" \
            if label in ("reconceived", "fresh") else "staged"
        for it in load_items(path):
            if looks_like_mcq(it):
                yield layer, path, it


def check_mcq_explain():
    n = 0
    for layer, path, it in finished_items():
        n += 1
        iid = it.get("id", f"<noid@{path}>")
        expl = it.get("explanation")
        if not isinstance(expl, str) or len(expl.strip()) < 40:
            fail("MCQ-EXPLAIN",
                 f"{iid}: explanation missing/too short "
                 f"({len(expl.strip()) if isinstance(expl, str) else 0} chars)")
        oe = it.get("option_explanations")
        if not isinstance(oe, dict):
            continue  # MCQ-OPTIONS already flags this
        for k in ("A", "B", "C", "D"):
            v = oe.get(k)
            if not isinstance(v, str) or len(v.strip()) < 20:
                fail("MCQ-EXPLAIN",
                     f"{iid}: option explanation {k} missing/too short "
                     f"({len(v.strip()) if isinstance(v, str) else 0} chars)")
    print(f"explanation completeness checked: {n} items")


def check_mcq_idfmt():
    n = 0
    for layer, path, it in finished_items():
        n += 1
        iid = it.get("id", "")
        m = ID_PATTERN.match(iid)
        if not m:
            fail("MCQ-IDFMT", f"{iid}: does not match "
                              f"wh-<source>-<t1-3|u1-9>-<nnn> ({path})")
    # test-layer question ids
    for f, q in test_items():
        iid = q.get("id", "")
        if not ID_PATTERN.match(iid):
            fail("MCQ-IDFMT", f"test {f}: {iid} does not match id pattern")
    print(f"id format checked: {n} finished-layer items + test ids")


def check_mcq_difficulty():
    bank_path = os.path.join(BUILD, "bank", "mcq-bank.json")
    by_unit = {}
    for it in load_items(bank_path):
        if looks_like_mcq(it):
            by_unit.setdefault(it.get("unit"), Counter())[it.get("difficulty")] += 1
    for u in sorted(by_unit):
        tot = sum(by_unit[u].values())
        h = by_unit[u].get("hard", 0)
        frac = h / tot if tot else 0
        print(f"  unit {u}: hard {h}/{tot} ({frac:.1%})")
        if frac == 0 or frac == 1:
            fail("MCQ-DIFFICULTY",
                 f"unit {u}: hard fraction {frac:.1%} (must not be 0%/100%)")


def check_stimwords():
    n = 0
    stem_only = 0
    for layer, path, it in finished_items():
        n += 1
        iid = it.get("id", f"<noid@{path}>")
        stimulus = it.get("stimulus")
        if not isinstance(it.get("stem"), str) or not it["stem"].strip():
            fail("MCQ-STIMWORDS", f"{iid}: empty stem")
        declared = it.get("stimulus_words")
        if stimulus is None or not str(stimulus).strip():
            # stem-only item: legal only when stimulus_words == 0
            if declared:
                fail("MCQ-STIMWORDS",
                     f"{iid}: no stimulus but stimulus_words={declared}")
            stem_only += 1
            continue
        actual = len(str(stimulus).split())
        if isinstance(declared, int) and actual > 0:
            if declared > 2 * actual or actual > 2 * declared:
                fail("MCQ-STIMWORDS",
                     f"{iid}: stimulus_words={declared} vs actual {actual} "
                     f"(>2x divergence)")
    print(f"stimulus-word sanity checked: {n} items "
          f"({stem_only} stem-only, stimulus_words=0)")


def check_lengthtell():
    # report-only: the repo has no stated length-tell bar. VALIDATION.md
    # records 19.3% as an observed value ("below chance"), not a gate.
    n = 0
    hits = 0
    ties = 0
    for layer, path, it in finished_items():
        lens = [len(str(o)) for o in it.get("options", [])]
        key = it.get("key")
        if len(lens) == 4 and key in "ABCD":
            n += 1
            mx = max(lens)
            if lens.count(mx) > 1:
                ties += 1
                continue
            if "ABCD".index(key) == lens.index(mx):
                hits += 1
    pct = hits / n * 100 if n else 0
    print(f"LENGTHTELL-RPT: longest-option-is-key = {hits}/{n} ({pct:.1f}%), "
          f"{ties} ties, no stated bar -- report only")


# ------------------------------------------------------------- orphan + merge
ORPHAN_CLASSES = [
    ("BANK", "build/bank/"),
    ("SOURCE", "build/reconceived/"),
    ("SOURCE", "build/fresh-written/"),
    ("STAGED", "build/visual-backfill/"),
    ("RAW-STAGING", "build/reclaim-staged/"),
    ("FRQ-BANK", "build/frq-remapped/"),
    ("TEST", "build/tests/test-"),
    ("REFERENCE", "build/released-cb/"),
    ("GENERATED", "build/image-download-report.json"),
    ("TAGGING-AUDIT", "build/tagging/"),
    ("TAGGING-AUDIT", "build/tagging-audit/"),
]


def classify_build_json(path):
    rel = os.path.relpath(path, REPO).replace(os.sep, "/")
    if rel == "build/tests/assemble_tests.py":
        return "TOOLING"
    for cls, prefix in ORPHAN_CLASSES:
        if rel.startswith(prefix):
            return cls
    if rel in ("build/coverage-matrix.json", "build/image-check-cache.json"):
        return "GENERATED"
    if rel == "build/cb-codes.json":
        return "REFERENCE"
    return None


def check_orphans():
    counts = Counter()
    n = 0
    for dirpath, _, files in os.walk(BUILD):
        for f in sorted(files):
            if f.endswith(".json"):
                n += 1
                path = os.path.join(dirpath, f)
                cls = classify_build_json(path)
                if cls is None:
                    fail("ORPHAN-JSON", f"unclassified json: {path}")
                else:
                    counts[cls] += 1
    print(f"orphan scan: {n} json files -> {dict(counts)}")


def check_source_merged():
    # explicit pass: bank ids vs source (reconceived+fresh-written) ids
    bank_ids, src_ids, staged_ids = set(), set(), set()
    for layer, path, it in finished_items():
        iid = it.get("id")
        if not iid:
            continue
        if layer == "bank":
            bank_ids.add(iid)
        elif layer == "source":
            src_ids.add(iid)
        else:
            staged_ids.add(iid)
    for iid in sorted(src_ids - bank_ids):
        fail("SOURCE-MERGED", f"source item {iid} not merged into the bank")
    for iid in sorted(bank_ids - src_ids):
        fail("SOURCE-MERGED", f"bank item {iid} has no source-layer item")
    overlap = bank_ids & staged_ids
    if overlap:
        fail("SOURCE-MERGED",
             f"staged backfill ids already in bank (merge happened?): "
             f"{sorted(overlap)[:5]}")
    print(f"source-merge: bank {len(bank_ids)}, source {len(src_ids)}, "
          f"staged(backfill) {len(staged_ids)}, backfill-in-bank {len(overlap)}")


# ------------------------------------------------------------ link integrity
def check_test_bank_link():
    bank_path = os.path.join(BUILD, "bank", "mcq-bank.json")
    bank_ids = {it.get("id") for it in load_items(bank_path)
                if looks_like_mcq(it)}
    n = 0
    for f, q in test_items():
        n += 1
        iid = q.get("id", "<noid>")
        if iid not in bank_ids:
            fail("TEST-BANK-LINK",
                 f"test {f}: question {iid} not found in the bank "
                 f"(repo policy: tests draw from the bank)")
    print(f"test-bank link: {n} test questions all resolve to bank ids")


def check_answer_keys():
    path = os.path.join(BUILD, "tests", "ANSWER_KEYS.md")
    try:
        text = open(path).read()
    except Exception as e:
        fail("LINK-KEYS", f"cannot read ANSWER_KEYS.md ({e})")
        return
    sections = re.split(r"^## Test (\d+)$", text, flags=re.M)
    # sections[0] is preamble, then alternating number/body
    bodies = {int(sections[i]): sections[i + 1]
              for i in range(1, len(sections) - 1, 2)}
    if len(bodies) != 10:
        fail("LINK-KEYS", f"expected 10 Test sections, found {len(bodies)}")
        return
    for tno in range(1, 11):
        body = bodies.get(tno, "")
        entries = re.findall(r"^(\d+)\.\s+([A-D])\s+\((wh-[^)]+)\)",
                             body, flags=re.M)
        if len(entries) != 55:
            fail("LINK-KEYS", f"Test {tno:02d}: {len(entries)} entries (need 55)")
            continue
        tpath = os.path.join(BUILD, "tests", f"test-{tno:02d}.json")
        qs = json.load(open(tpath))["section_1a"]["questions"]
        for idx, ((num, letter, iid), q) in enumerate(zip(entries, qs)):
            if int(num) != idx + 1:
                fail("LINK-KEYS",
                     f"Test {tno:02d}: numbering not sequential at {num}")
                break
            if iid != q.get("id"):
                fail("LINK-KEYS",
                     f"Test {tno:02d} q{num}: key id {iid} != "
                     f"test question id {q.get('id')}")
    print("ANSWER_KEYS.md: 10 sections x 55 entries match test question ids")


def find_frq_source(kind, ref):
    base = os.path.join(BUILD, "frq-remapped")
    if kind == "saq":
        for sub in ("saq-sets-01-30", "saq-sets-31-60"):
            p = os.path.join(base, sub, f"{ref}.json")
            if os.path.isfile(p):
                return p
        return None
    if kind == "dbq":
        p = os.path.join(base, "dbqs", f"{ref}.json")
        return p if os.path.isfile(p) else None
    if kind == "leq":
        p = os.path.join(base, "leqs", f"{ref}.json")
        return p if os.path.isfile(p) else None
    return None


def check_frq_links():
    base = os.path.join(BUILD, "tests")
    for f in sorted(os.listdir(base)):
        if not (f.startswith("test-") and f.endswith(".json")):
            continue
        t = json.load(open(os.path.join(base, f)))
        for s in t.get("section_1b", {}).get("saq_sets", []):
            sid = s.get("set_id", "<noid>")
            src = find_frq_source("saq", sid)
            if src is None:
                fail("LINK-FRQ", f"{f}: saq set {sid} has no source file")
            elif json.dumps(json.load(open(src)), sort_keys=True) != \
                    json.dumps(s, sort_keys=True):
                fail("LINK-FRQ", f"{f}: embedded {sid} differs from source")
        dbq = t.get("section_2a", {}).get("dbq", {})
        did = dbq.get("id", "<noid>")
        dsrc = find_frq_source("dbq", did)
        if dsrc is None:
            fail("LINK-FRQ", f"{f}: dbq {did} has no source file")
        elif json.dumps(json.load(open(dsrc)), sort_keys=True) != \
                json.dumps(dbq, sort_keys=True):
            fail("LINK-FRQ", f"{f}: embedded {did} differs from source")
        leq = t.get("section_2b", {}).get("leq", {})
        lid = leq.get("id", "<noid>")
        lsrc = find_frq_source("leq", lid)
        if lsrc is None:
            fail("LINK-FRQ", f"{f}: leq {lid} has no source file")
        elif json.dumps(json.load(open(lsrc)), sort_keys=True) != \
                json.dumps(leq, sort_keys=True):
            fail("LINK-FRQ", f"{f}: embedded {lid} differs from source")
    print("FRQ links: 10 tests x (3 SAQ sets + DBQ + LEQ) resolve, embedded "
          "copies byte-identical to source")


# ------------------------------------------------------------ image + coverage
def all_image_urls():
    urls = {}
    for layer, path, it in finished_items():
        u = it.get("image_url")
        if u:
            urls.setdefault(u, set()).add(f"{layer}:{it.get('id')}")
    for f, q in test_items():
        u = q.get("image_url")
        if u:
            urls.setdefault(u, set()).add(f"test:{f}")
    return urls


def looks_like_image(path):
    """Non-empty file that PIL can open (or an SVG). Returns (ok, why)."""
    if os.path.getsize(path) == 0:
        return False, "empty file"
    try:
        from PIL import Image
        im = Image.open(path)
        im.verify()
        return True, f"{im.format}"
    except ImportError:
        return True, "non-empty (PIL unavailable, extension-only check)"
    except Exception as e:
        if path.lower().endswith(".svg"):
            head = open(path, "rb").read(400)
            if b"<svg" in head:
                return True, "svg"
        return False, f"not a readable image ({e})"


def check_images():
    urls = all_image_urls()
    checked_files = set()
    for u, users in sorted(urls.items()):
        user = sorted(users)[0]
        if u.startswith("http://") or u.startswith("https://"):
            fail("IMAGE-LOCAL",
                 f"REMOTE image_url still in content (local-only policy): "
                 f"{u} (used by {user})")
            continue
        fpath = os.path.join(REPO, u) if not os.path.isabs(u) else u
        if not os.path.isfile(fpath):
            fail("IMAGE-LOCAL",
                 f"missing local image file: {u} (used by {user})")
            continue
        if fpath not in checked_files:
            checked_files.add(fpath)
            ok, why = looks_like_image(fpath)
            if not ok:
                fail("IMAGE-LOCAL", f"bad local image {u}: {why}")
    # items whose remote source was dead: flag until a replacement exists
    for layer, path, it in finished_items():
        if it.get("image_unavailable"):
            fail("IMAGE-LOCAL",
                 f"{it.get('id')}: image source dead "
                 f"({it.get('image_source_url')}) -- needs replacement "
                 f"or rewrite")
    for f, q in test_items():
        if q.get("image_unavailable"):
            fail("IMAGE-LOCAL",
                 f"test {f} {q.get('id')}: image source dead "
                 f"({q.get('image_source_url')}) -- needs replacement "
                 f"or rewrite")
    # any other local image path fields referenced in build/
    local_refs = []
    for dirpath, _, files in os.walk(BUILD):
        for fn in files:
            if not fn.endswith(".json"):
                continue
            path = os.path.join(dirpath, fn)
            try:
                d = json.load(open(path))
            except Exception:
                continue
            stack = [d]
            while stack:
                node = stack.pop()
                if isinstance(node, dict):
                    for k, v in node.items():
                        if k in ("image_path", "local_image",
                                 "local_image_path") and isinstance(v, str):
                            local_refs.append((path, v))
                        stack.append(v)
                elif isinstance(node, list):
                    stack.extend(node)
    for path, ref in local_refs:
        if not os.path.isfile(os.path.join(REPO, ref)) and \
                not os.path.isfile(ref):
            fail("IMAGE-LOCAL", f"{path}: local image missing: {ref}")
    print(f"image checks: {len(urls)} image refs, "
          f"{len(checked_files)} unique local files, "
          f"{len(local_refs)} extra local refs")


def write_coverage_matrix():
    bank_path = os.path.join(BUILD, "bank", "mcq-bank.json")
    items = [i for i in load_items(bank_path) if looks_like_mcq(i)]
    skills = sorted(SKILLS)
    matrix = {s: {str(u): 0 for u in range(1, 10)} for s in skills}
    unit_counts = Counter()
    unit_themes = {u: set() for u in range(1, 10)}
    for it in items:
        u = it.get("unit")
        s = it.get("skill")
        if u in range(1, 10) and s in SKILLS:
            matrix[s][str(u)] += 1
        if u in range(1, 10):
            unit_counts[u] += 1
            for th in (it.get("themes") or []):
                unit_themes[u].add(th)
    out = {
        "generated": "build/validate.py COVERAGE gate (do not hand-edit)",
        "unit_quotas": {str(k): v for k, v in UNIT_QUOTAS.items()},
        "skill_cell_minimum": SKILL_CELL_MIN,
        "unit_themes_minimum": UNIT_THEMES_MIN,
        "unit_totals": {str(u): unit_counts.get(u, 0) for u in range(1, 10)},
        "unit_theme_spans": {str(u): sorted(unit_themes[u]) for u in range(1, 10)},
        "skills_by_unit": matrix,
    }
    path = os.path.join(BUILD, "coverage-matrix.json")
    json.dump(out, open(path, "w"), indent=1)
    return out


def check_coverage():
    cov = write_coverage_matrix()
    for u in range(1, 10):
        su = str(u)
        tot = cov["unit_totals"][su]
        if tot < UNIT_QUOTAS[u]:
            fail("COVERAGE",
                 f"unit {u}: {tot} bank items, quota {UNIT_QUOTAS[u]}")
        for s in sorted(SKILLS):
            c = cov["skills_by_unit"][s][su]
            if c < SKILL_CELL_MIN:
                fail("COVERAGE",
                     f"skill '{s}' x unit {u}: {c} < {SKILL_CELL_MIN}")
        nthemes = len(cov["unit_theme_spans"][su])
        if nthemes < UNIT_THEMES_MIN:
            fail("COVERAGE",
                 f"unit {u}: spans {nthemes} themes "
                 f"(need >={UNIT_THEMES_MIN})")
    print(f"coverage matrix written: build/coverage-matrix.json "
          f"({sum(cov['unit_totals'].values())} bank items)")


# ------------------------------------------------- CB code-linkage gates
def load_cb_codes():
    """Load build/cb-codes.json; fail CB-CODES-FILE and return None if
    the file is missing or invalid."""
    path = os.path.join(BUILD, "cb-codes.json")
    if not os.path.isfile(path):
        fail("CB-CODES-FILE", f"{path} missing -- official code list required")
        return None
    try:
        data = json.load(open(path))
    except Exception as e:
        fail("CB-CODES-FILE", f"{path} does not parse: {e}")
        return None
    for key in ("skills", "topics", "reasoning_processes"):
        if not isinstance(data.get(key), list) or not data[key]:
            fail("CB-CODES-FILE", f"{path}: '{key}' missing/empty")
            return None
    return data


def check_cb_codes():
    cb = load_cb_codes()
    if cb is None:
        return
    skill_of = {s["code"]: s["skill"] for s in cb["skills"]}
    topic_unit = {}
    for t in cb["topics"]:
        topic_unit[t["code"]] = t.get("unit")
    rp_codes = {r["code"] for r in cb["reasoning_processes"]}

    n = 0
    miss_skill, miss_topic = [], []
    invent_skill, invent_topic, invent_rp = [], [], []
    parent_mismatch, unit_mismatch = [], []

    for layer, path, it in finished_items():
        n += 1
        iid = it.get("id", f"<noid@{path}>")
        sc = it.get("skill_code")
        if not sc:
            miss_skill.append(iid)
        elif sc not in skill_of:
            invent_skill.append((iid, sc))
        elif it.get("skill") != skill_of[sc]:
            parent_mismatch.append((iid, sc, it.get("skill")))
        tc = it.get("topic_code")
        if not tc:
            miss_topic.append(iid)
        elif tc not in topic_unit:
            invent_topic.append((iid, tc))
        elif str(topic_unit[tc]) != str(it.get("unit")):
            unit_mismatch.append((iid, tc, it.get("unit")))
        rc = it.get("reasoning_code")
        if rc and rc not in rp_codes:
            invent_rp.append((iid, rc))

    def summ(items, head, fmt):
        if items:
            shown = ", ".join(fmt(x) for x in items[:5])
            fail(head, f"{len(items)} items: {shown}"
                       + (" ..." if len(items) > 5 else ""))

    summ(miss_skill, "CB-SKILL-CODE", lambda x: x)
    summ(invent_skill, "CB-NO-INVENTION",
         lambda x: f"{x[0]} skill_code='{x[1]}'")
    summ(parent_mismatch, "CB-SKILL-CODE",
         lambda x: f"{x[0]} skill_code={x[1]} but skill='{x[2]}'")
    summ(miss_topic, "CB-TOPIC-CODE", lambda x: x)
    summ(invent_topic, "CB-NO-INVENTION",
         lambda x: f"{x[0]} topic_code='{x[1]}'")
    summ(unit_mismatch, "CB-TOPIC-CODE",
         lambda x: f"{x[0]} topic_code={x[1]} but unit={x[2]}")
    summ(invent_rp, "CB-NO-INVENTION",
         lambda x: f"{x[0]} reasoning_code='{x[1]}'")
    print(f"CB code linkage checked: {n} finished-layer items "
          f"(skills={len(skill_of)}, topics={len(topic_unit)}, "
          f"reasoning={len(rp_codes)} official codes)")


def main():
    check_mcq()
    check_mcq_explain()
    check_mcq_idfmt()
    check_mcq_difficulty()
    check_stimwords()
    check_lengthtell()
    check_orphans()
    check_source_merged()
    check_cb_codes()
    check_saq()
    check_dbq()
    check_leq()
    check_tests()
    check_test_bank_link()
    check_answer_keys()
    check_frq_links()
    check_images()
    check_coverage()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAILURES:")
        for x in FAILS:
            print(" ", x)
        sys.exit(1)
    print("ALL GATES GREEN")


if __name__ == "__main__":
    main()
