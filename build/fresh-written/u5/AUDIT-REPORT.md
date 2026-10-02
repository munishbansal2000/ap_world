# Blind Key Audit Report — AP World Unit 5 Fresh-Written MCQs

- **Date:** 2026-10-02 (PDT)
- **Auditor:** clean-context subagent (blind; writers' notes, books, and recorded keys not consulted until after each derivation)
- **Files audited:** `~/workspace/ap_world/build/fresh-written/u5/batch-01.json` through `batch-06.json`
- **Items audited:** 61 (`wh-fresh-u5-001` … `wh-fresh-u5-061`)

## Summary

| Metric | Result |
|---|---|
| Items audited | 61 |
| Blind derivation == recorded key | **61 / 61 (100%)** |
| Derivation-error (my derivation wrong, item left as-is) | 0 |
| Items requiring repair | 1 (minor explanation precision fix, key unchanged) |
| Structural checks (4 options A–D, explanation keys, key explanation affirmative, no distractor explanation says "correct") | 61/61 pass |
| Stimulus adequacy / phantom-reference check | 61/61 pass — every map/engraving/chart stimulus is described in sufficient detail to answer; no undescribed visuals |

## Method

For each item I read only stimulus + stem + options (keys masked via script), derived the answer from my own historical knowledge, then compared against the recorded `key`. On a mismatch I would have diagnosed whether the item was broken (repair in place) or my derivation was wrong (leave it). There were no mismatches, so no repairs to stems, options, or keys were needed.

## Changelog

- `batch-06.json`, item `wh-fresh-u5-053` — **explanation precision fix** (not a key defect): the option-(B) explanation previously read "Wrong. No Americans served as advisors to the National Assembly." That absolute is historically overbroad — Jefferson gave Lafayette informal advice on the 1789 Declaration of the Rights of Man (though not on the 1791 constitution). Rewrote to: "Wrong. Americans held no formal advisory role in writing the 1791 constitution — Jefferson's informal advice to Lafayette concerned the 1789 Declaration of the Rights of Man, not the constitution. The influence shown in the excerpts was ideological: a written, consent-based model adapted to a monarchy." The key (A) and the distractor's defensibility are unchanged — this only removes a false absolute.
- No other items were modified: no key flips, no stem/option/stimulus edits, no tag changes.

## Per-item findings

All 61 items: **PASS** — blind-derived letter matches recorded key; exactly 4 options (A–D); the key's `option_explanations` and top-level `explanation` support the key; stimulus contains what's needed; no second defensible option.

- **001–010** (batch-01): all pass. 001=A, 002=C, 003=B, 004=D, 005=A, 006=C, 007=B, 008=D, 009=A, 010=C. (Note: 005's distractor (C) stacks two anachronisms — Monroe Doctrine issued 1823 + Bolívar writing in exile in 1815 — deliberately; no ambiguity.)
- **011–020** (batch-02): all pass. 011=C, 012=B, 013=D, 014=A, 015=C, 016=B, 017=A, 018=D, 019=C, 020=A. (Note: 019's stimulus is the Louverture engraving; the correct sequence (C) — 1794 abolition decree → 1802 expedition to restore slavery → independence war — is historically accurate.)
- **021–030** (batch-03): all pass. 021=B, 022=D, 023=A, 024=C, 025=B, 026=A, 027=D, 028=C, 029=B, 030=A. (Note: 022's distractor (A) includes the explicit "without exception" qualifier, which correctly kills it given partial early abolitions; 024's key (C) requires outside knowledge that Rousseau's general will shaped France, which is standard curriculum content.)
- **031–040** (batch-04): all pass. 031=A, 032=C, 033=B, 034=D, 035=B, 036=A, 037=D, 038=C, 039=A, 040=B. (Note: 036's "best understood in the context of" phrasing legitimately yields (A) — Britain's industrial-capitalist free-vs-forced-labor debate — over anachronistic distractors.)
- **041–050** (batch-05): all pass. 041=A, 042=C, 043=B, 044=D, 045=A, 046=B, 047=C, 048=D, 049=A, 050=B.
- **051–061** (batch-06): all pass. 051=B, 052=D, 053=A (explanation precision fix noted above; key unchanged), 054=C, 055=B, 056=D, 057=A, 058=C, 059=B, 060=D, 061=A.

## Verdict

The batch is **clean**. No ambiguity, no dual-defensible options, no phantom references, no explanations contradicting keys, and all six files still parse as valid JSON (10+10+10+10+10+11 = 61 items). One minor explanation wording improvement made in `batch-06.json` (`wh-fresh-u5-053`); no commit/push performed per instructions.
