# AP World Practice Tests — Validation Report

**Date:** 2026-10-02 · **Repo:** munishbansal2000/ap_world (main)

## Bank (build/bank/mcq-bank.json)

| Check | Result |
|---|---|
| Total items | 1,111 (891 reclaimed + 220 fresh) |
| ID collisions | 0 |
| Schema completeness | 100% (id, unit, stem, options, key, explanation, option_explanations, skill, reasoning, themes, stimulus_words) |
| Skill tags | All 6 canonical CB skills; 234 repaired + 38 renamed |
| Skills×units matrix | All 54 cells ≥ 5 (min 5) |
| Unit quotas | U1 129, U2 84, U3 130, U4 150, U5 136, U6 171, U7 89, U8 123, U9 99 (all ≥ quota) |
| Key balance | A 25.9% / B 25.0% / C 24.2% / D 24.8% (all ≤ 30%) |
| Length-tell | 19.3% (below chance) |
| Verified image URLs | 54 items; 0 `visual_needs_url` remaining |

## Test assembly (10 tests)

| Check | Result |
|---|---|
| MCQs per test | 55 each, exact unit quotas (U1/U2/U7/U8/U9: 5; U3/U4: 8; U5/U6: 7) |
| Cross-test uniqueness | 550 unique ids, zero overlap |
| Visual per test | 5–6 verified images (~10%; bank constraint — 54 total available) |
| SAQ sets | 30 (3/test); all follow q1 secondary-text / q2 primary-text / q3 non-text |
| DBQs | 10, 7 documents each; topics span U1–U9 |
| LEQs | 10 single prompts; causation 4, continuity/change 3, comparison 3 |
| Directions text | New Fall 2026 CED format only; zero old-format language |

## Blind validation (clean-context)

- **Key audit:** 100 MCQs blind-derived (10/test) → 100/100 match, 0 mismatches.
- **Structural:** unit weights exact, zero duplicates, directions new-format, SAQ rotation correct, 10/10 sampled image URLs HTTP 200, DBQ 7 docs, LEQ prompts non-empty.
- **Repairs from validation:**
  - `wh-barrons-u7-005`: stem said "about New York", stimulus is Senghor writing about Africa — stem and option A corrected ("Parisian literary family"); key re-derived blind → D, match.
  - `wh-princeton-pdf6-u2-005`, `wh-princeton-pdf5-u8-002`: options lacked letter labels in JSON — labeled (A)–(D); keys unchanged.

## Known limitations (honest)

- Visual coverage ~10% per test (54 verified images in bank); CB's ~40% visual is aspirational for this bank.
- 12 fresh items carry [UNVERIFIED-QUOTE] flags (adapted pre-1900 wording, substance verified).
- 92 items are `visual_reconstructed` (charts/maps described as text, no image URL needed).
- FRQ remap covered 60 SAQ sets / 10 DBQs / 20 LEQs; 10 tests consume 30/10/10.
