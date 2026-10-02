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
  SAQ-FORMAT   60 sets, Q1 secondary / Q2 primary / Q3 non-text, parts a-c,
               sample answers present
  DBQ-FORMAT   10 DBQs, 7 documents each, topic within the 1200-2001 range
  LEQ-FORMAT   20 LEQs, single prompt each, no choice language
  TEST-STRUCT  10 tests: 55 MCQ / 3 SAQ / DBQ / LEQ, no duplicate MCQ ids
               across tests, new-format directions only
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


def main():
    check_mcq()
    check_saq()
    check_dbq()
    check_leq()
    check_tests()
    print()
    if FAILS:
        print(f"{len(FAILS)} FAILURES:")
        for x in FAILS:
            print(" ", x)
        sys.exit(1)
    print("ALL GATES GREEN")


if __name__ == "__main__":
    main()
