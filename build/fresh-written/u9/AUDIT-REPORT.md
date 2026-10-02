# Blind Key Audit Report — AP World Unit 9 Fresh-Written MCQs

**Auditor:** clean-context pass (fresh session, no prior exposure to the items)
**Date:** 2026-10-02
**Files:** `batch-01.json`, `batch-02.json`, `batch-03.json`, `batch-04.json`
**Items audited:** 33 (wh-fresh-u9-001 … wh-fresh-u9-033)

**Caveat on blindness:** the JSON files carry the `key` field inline, so the keys were technically visible in the same file output. The method was honored in substance: for each item I derived the answer from the stimulus + stem + options (plus my own historical knowledge) *before* consulting the recorded key, and I checked explanations/stimulus support only after the derivation. No book, writer notes, or external sources were consulted.

## Summary

| Metric | Result |
|---|---|
| Items audited | 33 |
| Derived matches recorded key | **33 / 33 (100%)** |
| Mismatches | 0 |
| Repairs made | 0 (none needed) |
| Files re-written | None — no edits |

## Per-item verdicts

All items **PASS**. For each item I record my blind derivation (D) and the recorded key (K).

**batch-01**
- 001 (Gorbachev reforms → dissolution): D=C, K=C — PASS. (C) is the only option matching the stimulus; A/B/D are factually contradicted by it.
- 002 (evidence perestroika failed economically): D=B, K=B — PASS. Only (B) is direct economic evidence; A is foreign-policy irrelevant, C/D out of period.
- 003 (best argument about reforms): D=D, K=D — PASS. A/B/C are overclaims or contradicted (China reformed without collapsing/democratizing); D is the stimulus's exact thesis.
- 004 (trade-share chart claim): D=A, K=A — PASS. ~25% → ~60% is more than doubling; B/C/D contradicted by the described trend.
- 005 (post-WWII institutions → trade growth): D=C, K=C — PASS. Only (C) names the tariff-reduction mechanism; B contains two factual errors (USSR dissolution did not create the WTO; tariffs not ended worldwide).
- 006 (1989 Beijing declaration POV): D=B, K=B — PASS. "We seek reform, not the overthrow of the system" is textbook reformist.
- 007 (1989 claim from declaration + Tank Man account): D=A, K=A — PASS. Contrast of force vs. no-force outcomes is the defensible synthesis; B/C/D are contradicted by the account.
- 008 (container ship → connection): D=D, K=D — PASS.
- 009 (best argument about containerization): D=B, K=B — PASS. A/C/D contain absolute/false claims; B is the standard export-led industrialization link.

**batch-02**
- 010 (continuity and change, shipping revolution): D=C, K=C — PASS. A/D factually false; B contradicted by the Singapore stimulus.
- 011 (Green Revolution Punjab → effects): D=A, K=A — PASS. B/C/D contradicted by or unrelated to the report.
- 012 (Green Revolution connection): D=D, K=D — PASS. The report's expensive input package supports exactly (D); A/B/C are false overclaims.
- 013 (Cairo 2011 phones → connection): D=B, K=B — PASS.
- 014 (challenge "social media caused the uprising"): D=C, K=C — PASS. Only (C) supplies pre-existing independent causes; A/B/D are consistent with or support the claim.
- 015 (TRC purpose): D=A, K=A — PASS. Amnesty-for-truth model = public record over mass trials; B/C/D contradicted by the testimony and dates.
- 016 (TRC context): D=D, K=D — PASS.
- 017 (trade blocs driven by): D=B, K=B — PASS. A/C/D contain false absolutes (UN did not order blocs; members still trade externally).

**batch-03**
- 018 (map claim): D=C, K=C — PASS. Blocs on three continents; A/B/D misread the map's scope/details.
- 019 (EU vs USMCA): D=A, K=A — PASS. Shared institutions + euro = deeper integration; B/C/D factually false.
- 020 (Kyoto/Paris context): D=D, K=D — PASS. A/B/C contradicted by the rising CO2 line and historical record.
- 021 (emissions trend → globalization): D=B, K=B — PASS. A/D contradicted by the graph; C reverses agency.
- 022 (best argument about climate agreements): D=C, K=C — PASS. A/B contradicted by the still-rising CO2 line; D reverses causation.
- 023 (AIDS campaigns → effects): D=A, K=A — PASS. B/C/D are false (no cure; no travel ban; UN programs expanded).
- 024 (disease in globalization): D=D, K=D — PASS. A/B/C contradicted by the report and known history.
- 025 (Berlin Wall scene context): D=B, K=B — PASS. Gorbachev's non-intervention is the standard enabling condition; C is historically absurd (Versailles did not "merge East and West Germany").

**batch-04**
- 026 (historian caution): D=C, K=C — PASS. One celebratory night cannot stand in for the painful 1990s transition; A/B are non-issues; D misreads the source.
- 027 (Shenzhen transformation): D=A, K=A — PASS. 1980 SEZ is the canonical cause; B/C/D factually false.
- 028 (Shenzhen connection): D=D, K=D — PASS. State-directed reform + manufacturing relocation; A/B/C invert the evidence.
- 029 (guest workers record → connection): D=B, K=B — PASS.
- 030 (guest-worker context): D=C, K=C — PASS. A (slave trade) is wrong era/type; B/D factually false.
- 031 (evaluate two historians): D=A, K=A — PASS. Mixed evidence is the only defensible evaluation; B/C/D ignore one side's real examples or make false claims.
- 032 (9/11 and globalization): D=D, K=D — PASS. A/B/C contradicted by the nature of the attacks and their aftermath.
- 033 (global culture): D=B, K=B — PASS. Homogenization + hybridization; A/C/D contradicted by the stimulus's own examples.

## Secondary checks (all items)

- **Exactly 4 options, keys A–D only:** yes for all 33 (verified programmatically).
- **Key-letter distribution:** A=8, B=9, C=8, D=8 — balanced; no letter dominates.
- **No two defensible answers:** on every item exactly one option is defensible; the distractors are either factually false, unsupported by the stimulus, or overclaims contradicted by the stimulus itself. No item was borderline.
- **Option explanations support the key:** yes — for each item the "Right" explanation corresponds to the recorded key and each "Wrong" explanation correctly dismisses its distractor. No contradictions found between explanations and keys.
- **Stimulus self-sufficiency:** yes — no phantom references. All chart/map/photograph items carry complete textual descriptions of the visual (line values, shading keys, image contents), so nothing requires an undescribed visual. (`visual_needs_url: true` flags exist on the visual items, but the stimulus text already contains everything needed to answer.)
- **Distractor-length tell:** no systematic "longest option is the key" pattern. Correct answers include short options (001 C, 008 D) and are spread across lengths; several items have keys of average or shorter length than distractors.

## Conclusion

33/33 blind derivations match the recorded keys. Zero mismatches, zero repairs, zero derivation errors. The batch is clean — no edits were made to any file. All four files parse as valid JSON (verified: batch-01 9 items, batch-02 8 items, batch-03 8 items, batch-04 8 items).
