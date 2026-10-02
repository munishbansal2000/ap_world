# Blind Answer-Key Audit — 5 Steps diagnostic + practice-test set

- **Auditor:** blind subagent (no prior exposure to source book or recorded keys)
- **Date:** 2026-10-02
- **Scope:** 6 files, 165 MCQs
  - diag-a-mcq.json (28), diag-b-mcq.json (27), pt1-a-mcq.json (28),
    pt1-b-mcq.json (27), pt2-a-mcq.json (28), pt2-b-mcq.json (27)
- **Method:** strict blind protocol — read stimulus/stem/options only,
  derived each answer from AP World History knowledge, recorded all 165
  derivations, then compared mechanically against recorded keys.
  Mismatches would have been investigated via explanations.

## Result

| Metric | Count |
|---|---|
| Total items audited | 165 |
| Blind derivations matching recorded key | 165 |
| Mismatches | 0 |
| Repairs | 0 |
| Quarantines | 0 |
| Auditor errors | 0 |

## Post-compare spot checks

After the 165/165 match, spot-checked the recorded explanations on the
highest-risk items (where a key-design slip was most plausible) to confirm
the explanation actually supports the key:

- `wh-fivesteps-u1-013` (Alexander's veterans → Opis mutiny, key C) — sound.
- `wh-fivesteps-u4-014` (Schmidel/Lampere hunger → seizing food, key B) — sound.
- `wh-fivesteps-u4-033` (silver streaming to China financing Potosí, key D) — sound.
- `wh-fivesteps-u6-012` (OAU 1964 border freeze → fear of border wars, key D) — sound.
- `wh-fivesteps-u6-023` (Kipling's imperial tensions, key A) — sound.
- `wh-fivesteps-u8-017` (Beijing's lesson: market reform OK, political reform fatal, key D) — sound.
- `wh-fivesteps-u5-009` (French vs American Revolution social overturn, key D) — sound.

## Verdict

All 165 recorded answer keys are correct under blind re-derivation.
No repairs or quarantines needed. No item files were modified.
