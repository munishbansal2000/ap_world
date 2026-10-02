# Blind Key Audit Report — AP World top-ups batch-01 + batch-02

**Date:** 2026-10-02 · **Auditor:** clean-context blind audit · **Scope:** 24 fresh-written MCQ items (U1, U4, U6, U8)

**Method:** Each answer was derived from stimulus + stem + options (A–D) alone, *before* reading the recorded `key`. The recorded key was then compared against the blind derivation. Mismatches were to be diagnosed as (a) item broken → repair in place, or (b) auditor error → leave and note. Structural checks: 4 options, A–D keys, option_explanations coverage, no phantom references, no two defensible options.

## Result: 24/24 match — 0 mismatches, 0 repairs, 0 items changed

| # | Item ID | Blind derive | Recorded key | Verdict |
|---|---------|--------------|--------------|---------|
| 1 | wh-fresh-u1-001 | B | B | ✓ MATCH — Song exams are an expansion of an earlier imperial pattern, not an invention |
| 2 | wh-fresh-u1-002 | D | D | ✓ MATCH — Aztec tribute fits the tributary-empire extraction pattern |
| 3 | wh-fresh-u1-003 | A | A | ✓ MATCH — mit'a pairs labor demand with reciprocal redistribution legitimating rule |
| 4 | wh-fresh-u1-004 | C | C | ✓ MATCH — trade + royal patronage spread Islam while older customs persisted |
| 5 | wh-fresh-u4-001 | C | C | ✓ MATCH — Equiano wrote to expose cruelty and build abolition support |
| 6 | wh-fresh-u4-002 | A | A | ✓ MATCH — contiguous overland rule vs overseas maritime-colonial networks |
| 7 | wh-fresh-u4-003 | B | B | ✓ MATCH — smallpox as decisive, unintended factor in the conquest |
| 8 | wh-fresh-u4-004 | D | D | ✓ MATCH — Potosi links coerced Andean labor to a global silver circuit (Europe + China) |
| 9 | wh-fresh-u4-005 | C | C | ✓ MATCH — encomienda = coerced labor + Christianization mission, contested and reformed |
| 10 | wh-fresh-u4-006 | B | B | ✓ MATCH — joint-stock companies blended private capital with state-like powers |
| 11 | wh-fresh-u4-007 | A | A | ✓ MATCH — plantation demand + European demand + African participation + mortality |
| 12 | wh-fresh-u6-001 | D | D | ✓ MATCH — Berlin formalized a European-only partition without African consent |
| 13 | wh-fresh-u6-002 | B | B | ✓ MATCH — Raj railways served extraction and British manufacturers, undercutting local industry |
| 14 | wh-fresh-u6-003 | A | A | ✓ MATCH — defeat → unequal Treaty of Nanjing on British terms |
| 15 | wh-fresh-u6-004 | C | C | ✓ MATCH — Meiji selective modernization; European workers split union-reform vs Marxist-revolution |
| 16 | wh-fresh-u8-001 | A | A | ✓ MATCH — Truman to Congress: fund Greece/Turkey aid to contain Soviet influence |
| 17 | wh-fresh-u8-002 | D | D | ✓ MATCH — decolonization took varied paths, each inspiring further movements |
| 18 | wh-fresh-u8-003 | B | B | ✓ MATCH — 1949 victory extended U.S. containment into Asia (Korea, Vietnam) |
| 19 | wh-fresh-u8-004 | C | C | ✓ MATCH — apartheid entrenched white-minority rule amid continent-wide decolonization |
| 20 | wh-fresh-u8-005 | D | D | ✓ MATCH — Marshall Plan = economic recovery as containment + East-West deepening |
| 21 | wh-fresh-u8-006 | A | A | ✓ MATCH — peasant-based movement adapted to rural China, land reform central |
| 22 | wh-fresh-u8-007 | B | B | ✓ MATCH — Tet was a communist military setback that shattered U.S. public confidence |
| 23 | wh-fresh-u8-008 | C | C | ✓ MATCH — apartheid as legal system preserving white-minority dominance |
| 24 | wh-fresh-u8-009 | D | D | ✓ MATCH — non-alignment = independence from blocs while engaging both sides |

## Structural checks (all passed, script-verified)
- 24 items total, all unique IDs (no duplicates).
- Every item: exactly 4 options lettered A–D; key ∈ {A,B,C,D}; `option_explanations` covers all four letters; the keyed explanation is marked as correct.
- Key distribution: A×6, B×6, C×6, D×6 — perfectly balanced.
- No two options simultaneously defensible on any item; distractors are substantive and cleanly contradicted by the stimulus.
- No phantom references (no stimulus references outside the given text).
- Each item has exactly one defensible answer; the blind derivation never hesitated between the key and a distractor.

## Advisory notes (no changes made — items are correct as-is)
- **Length-tell watch:** on a few items the keyed option is also the longest (e.g. wh-fresh-u4-005 key C, wh-fresh-u8-002 key D). Distractors are strong and the keys are not mechanically the longest on all items, so this is not a pattern violation — just flagging for consistency if a distractor-length hygiene pass is ever run.
- wh-fresh-u4-006 option (C) "The Dutch East India Company was controlled and directed by Asian merchants" is a deliberately odd distractor; it is flatly contradicted by the stimulus and harmless.

## Conclusion
All 24 top-up items pass blind key audit with no mismatches, no repairs needed, and no edits made. No commit, no push (per instructions).
