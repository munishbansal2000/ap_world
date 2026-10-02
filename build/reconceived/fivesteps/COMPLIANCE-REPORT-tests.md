# Clean-Context Compliance Review — 5 Steps tests

**Date:** 2026-10-02
**Reviewer:** independent subagent (not involved in drafting)
**Scope:** 165 re-conceived MCQs in `build/reconceived/fivesteps/`:
diag-a-mcq.json (28), diag-b-mcq.json (27), pt1-a-mcq.json (28), pt1-b-mcq.json (27), pt2-a-mcq.json (28), pt2-b-mcq.json (27)
**Reference (read only for IP comparison, never as drafting material):** `build/reclaim-staged/fivesteps/`

**Method:** Every item was compared against its source item via `source_id` (all 165 ids resolved against 276 source items; 0 missing). FAIL bar = same angle AND same distractor set, reworded. Facts checked against reviewer knowledge; blind key audit (`AUDIT-LOG-tests.md`, 2026-10-02) had already passed all 165 keys — keys were not re-audited here, only IP/format/facts.

---

## (a) IP verdicts

### FAILURES — rewritten (7)

1. `wh-fivesteps-u4-014` (diag-a, key B) ← `fivesteps-u4-001`. Old item asked why the Lampere attack fit Spanish motives (answer: food/provisions); distractors {bring Christianity, extend crown power, gain allies} were reworded, same design. **Rewrote:** new angle = what Lampere pit traps, a 4,000-man army, and a three-day defense show about early conquest warfare (indigenous organized resistance broken by firepower/persistence). Key kept: B.
2. `wh-fivesteps-u2-005` (diag-a, key D) ← `fivesteps-u2-001`. Old item asked how the Songhai king profited (answer: trade/tribute wealth); same 4-concept distractor set reworded. **Rewrote:** new angle = how marriage into merchant families and patronizing scholars/judges converted commercial wealth into royal legitimacy. Key kept: D.
3. `wh-fivesteps-u4-027` (diag-b, key A) ← `fivesteps-u4-011`. Old item asked the destination/use of captives from the Arab slave trade; same 4-concept distractor set reworded. **Rewrote:** new angle = economics of raiding (16 men return with 400 captives → violence pays). Key kept: A.
4. `wh-fivesteps-u4-042` (pt1-a, key A) ← `fivesteps-u4-039`. Old item asked about the pattern of expulsions vs voluntary migration; same 4 concepts reworded. **Rewrote:** new angle = what the destination pattern (Central/Eastern Europe, Ottoman Empire) shows about pragmatic tolerance attracting skilled refugees. Key kept: A.
5. `wh-fivesteps-u5-013` (pt1-a, key C) ← `fivesteps-u5-013`. Old item asked why Toussaint refused Sonthonax (feared blame); same 4-concept distractor set reworded. **Rewrote:** new angle = what political work the dialogue-form report did for Toussaint (discredit rival, advertise loyalty). Key kept: C.
6. `wh-fivesteps-u1-030` (pt1-b, key D) ← `fivesteps-u1-030`. Old item asked why Malian women didn't veil (pre-existing customs); same 4 concepts reworded. **Rewrote:** new angle = what Battuta's combination of praise and condemnation reveals about him as a source (judged Malian Islam against Middle Eastern urban norms). Key kept: D.
7. `wh-fivesteps-u6-022` (pt2-a, key A) ← `fivesteps-u6-022`. Old item asked the meaning of "a better man" (moral worth over rank); same 4-concept distractor set reworded. **Rewrote:** new angle = what the narrator's confession of beating Din does to the tribute (praise becomes guilt; hierarchy inverted). Key kept: A.

All 7 rewrites: new angle, fresh distractors, original explanations; same id; same key letter; re-checked against source — no longer same-angle + same-distractor-set. Facts in all 7 verified against reviewer knowledge.

### PASS — marginal/watchlist items (same source topic, but distractor sets differ enough to clear the conjunctive bar)

- diag-b: u7-004 (bubble metaphor — changed), u7-012 (Soviet stats skepticism — changed), u4-033 (silver to China — changed)
- pt1-a: u4-040 (foot plow — changed), u4-044 (migration consequences — changed)
- pt1-b: u8-008 (US–Soviet relationship — changed), u8-010 (containment — same angle/key, ~50% distractor overlap; judged changed), u5-017 (source utility — changed), u1-032 (Buddhism diffusion — changed), u6-018 (child labor — changed), u1-037 (Fujiwara opposition — changed)
- pt2-a: u1-042 (trade routes transmit ideas — changed), u6-021 (imperial attitudes — changed), u9-015/u9-016/u9-017 (globalization set — changed), u1-044 (Mongol women — changed)
- pt2-b: no marginal items.

### PASS — all remaining 151 items

Each retains no recognizable element of the source item's design: different angle, different distractor construction, or both. All 165 items pass (a) after the 7 rewrites.

---

## (b) FORMAT

(i) **MCQ-only check:** all 165 items in the 6 files carry `type == "mcq"`. No SAQ, DBQ, or LEQ items present. PASS.

(ii) **Staged frq.json spot-check:** `build/reclaim-staged/fivesteps/frq.json` holds 40 items (28 SAQ, 3 DBQ, 9 LEQ). Every item carries `"format": "old"` and an explicit `old_format_note`: "OLD FORMAT: predates Fall 2026 CED (SAQ choice, LEQ 3-choice)." PASS — old-format items are tagged.

**Violations:** none.

---

## (c) FACTS

All historical claims across the 165 items were checked against reviewer knowledge. No factually wrong claims found; no key was affected by a fact correction. One judgment call worth recording: the rewording of several source stimuli into modern paraphrases did not alter any material fact under test. Zero items flagged `[UNVERIFIED]`.

**[UNVERIFIED] flags:** none.

---

## Mechanical gates (script from the task, run verbatim)

```
n= 165 keys= {'D': 43, 'C': 43, 'B': 36, 'A': 43} pct= {'D': 26.1, 'C': 26.1, 'B': 21.8, 'A': 26.1}
longest_is_key= 21 12.7 %
GATES GREEN
```

Key distribution: A 26.1%, B 21.8%, C 26.1%, D 26.1% — all ≤ 30%. Longest-option-is-key: 12.7% — ≤ 30%.

---

## Verdict: PASS

- 165/165 items reviewed against source via source_id (0 unresolved).
- 7 IP failures rewritten (ids above), keys preserved, re-checked.
- 0 `[UNVERIFIED]` flags.
- 0 format violations (all-MCQ files; frq.json old-format tags present).
- Mechanical gates GREEN.

**Honest partition:** source stimuli remain paraphrases of book excerpts (the IP check covered question design — angle and distractor sets — not stimulus wording). The FRQ set was not re-conceived in this batch; it carries old-format tags as staged.
