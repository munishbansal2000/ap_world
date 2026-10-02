# COMPLIANCE REPORT — Barron's Clean-Context Review

**Reviewer:** independent subagent (not involved in drafting)
**Date:** 2026-10-02
**Scope:** all 160 MCQs in `build/reconceived/barrons/*.json`, each compared against its source item in `build/reclaim-staged/barrons/*.json` (matched via `source_id`).
**mapping.json / AUDIT-LOG.md:** ignored.

## Overall verdict: PASS (after repair)

- Items reviewed: **160** (8 files × unit MCQs + practice-test MCQs; file-level counts match the source set exactly)
- IP failures found and rewritten: **1** — `wh-barrons-u9-006`
- [UNVERIFIED] flags: **0**
- Format violations: **0**
- Mechanical gates: **GREEN** (see output below)

---

## (a) IP check — per-item verdicts

Rule applied: FAIL = same angle (asks the same thing about the topic in the same way) **AND** same distractor set (same wrong answers, reworded). Borderline cases (same angle, fresh distractors) are marked PASS per the conjunctive rule but noted.

### FAIL → rewritten
- `wh-barrons-u9-006` — FAIL. Reworded clone of `barrons-u9-006`: near-verbatim rephrase of the stem ("how the NOW document compares to late-1800s/early-1900s feminist thinking"), identical key in substance ("expansion from basic rights to equality in every sphere"), and one distractor a direct reword of the source's ("rejected the accomplishments... as too inadequate" → "a complete rejection of everything earlier feminists had achieved"). **Rewritten below** with a genuinely new angle; self-checked PASS on (a) and (c).

### PASS (borderline — same substantive answer, fresh distractors / reframed angle; listed for transparency)
- `wh-barrons-u4-008` — same definitional angle on chartered companies; 2 of 3 distractors new
- `wh-barrons-u7-009` — same angle (Soviet education as indoctrination); all-new distractor set
- `wh-barrons-u1-027` — similar angle (crusade-era war + commerce); fresh distractors
- `wh-barrons-u6-004` — same causal explanation (opium sales fixed the trade deficit); fresh distractors
- `wh-barrons-u3-002` — same point (Tokugawa merchants low status despite wealth); reframed comparatively, fresh distractors
- `wh-barrons-u1-021` — same point (Islamic wine poetry vs prohibition = norm-defiance); fresh distractors
- `wh-barrons-u9-013` — same point (McDonald's glocalization); fresh distractors
- `wh-barrons-u1-020` — same point (Qur'an addressed to believers, not a universal audience); fresh distractors
- `wh-barrons-u4-002` — same point (Native agency historiography); fresh distractors
- `wh-barrons-u9-005` — same point (NOW's physical-strength rebuttal); fresh distractors
- `wh-barrons-u3-006` — same point (Mughal Turkic/Persianate character); fresh distractors
- `wh-barrons-u9-023` — same point (energy-consumption disparity); fresh distractors
- `wh-barrons-u6-008` — same point (Japan feared China's fate); fresh distractors

### PASS (clean)
All remaining 146 items: `wh-barrons-u1-001` … (full per-item list in the audit table below). Each was compared stem+options against its source; angles and distractor sets are ours.

**Audit table (160/160):**
| id | IP | id | IP | id | IP |
|----|----|----|----|----|----|
| wh-barrons-u1-001 | PASS | wh-barrons-u1-002 | PASS | wh-barrons-u1-003 | PASS |
| wh-barrons-u1-004 | PASS | wh-barrons-u1-005 | PASS | wh-barrons-u1-006 | PASS |
| wh-barrons-u1-007 | PASS | wh-barrons-u1-008 | PASS | wh-barrons-u1-009 | PASS |
| wh-barrons-u1-010 | PASS | wh-barrons-u1-011 | PASS | wh-barrons-u1-012 | PASS |
| wh-barrons-u1-013 | PASS | wh-barrons-u1-014 | PASS | wh-barrons-u1-015 | PASS |
| wh-barrons-u1-016 | PASS | wh-barrons-u1-017 | PASS | wh-barrons-u1-018 | PASS |
| wh-barrons-u1-019 | PASS | wh-barrons-u1-020 | PASS (borderline) | wh-barrons-u1-021 | PASS (borderline) |
| wh-barrons-u1-022 | PASS | wh-barrons-u1-023 | PASS | wh-barrons-u1-024 | PASS |
| wh-barrons-u1-025 | PASS | wh-barrons-u1-026 | PASS | wh-barrons-u1-027 | PASS (borderline) |
| wh-barrons-u1-028 | PASS | wh-barrons-u1-029 | PASS | wh-barrons-u1-030 | PASS |
| wh-barrons-u1-031 | PASS | wh-barrons-u2-001 | PASS | wh-barrons-u2-002 | PASS |
| wh-barrons-u2-003 | PASS | wh-barrons-u2-004 | PASS | wh-barrons-u2-005 | PASS |
| wh-barrons-u2-006 | PASS | wh-barrons-u2-007 | PASS | wh-barrons-u2-008 | PASS |
| wh-barrons-u2-009 | PASS | wh-barrons-u2-010 | PASS | wh-barrons-u2-011 | PASS |
| wh-barrons-u2-012 | PASS | wh-barrons-u2-013 | PASS | wh-barrons-u2-014 | PASS |
| wh-barrons-u2-015 | PASS | wh-barrons-u3-001 | PASS | wh-barrons-u3-002 | PASS (borderline) |
| wh-barrons-u3-003 | PASS | wh-barrons-u3-004 | PASS | wh-barrons-u3-005 | PASS |
| wh-barrons-u3-006 | PASS (borderline) | wh-barrons-u3-007 | PASS | wh-barrons-u3-008 | PASS |
| wh-barrons-u3-009 | PASS | wh-barrons-u3-010 | PASS | wh-barrons-u3-011 | PASS |
| wh-barrons-u3-012 | PASS | wh-barrons-u3-013 | PASS | wh-barrons-u3-014 | PASS |
| wh-barrons-u3-015 | PASS | wh-barrons-u3-016 | PASS | wh-barrons-u3-017 | PASS |
| wh-barrons-u3-018 | PASS | wh-barrons-u3-019 | PASS | wh-barrons-u3-020 | PASS |
| wh-barrons-u4-001 | PASS | wh-barrons-u4-002 | PASS (borderline) | wh-barrons-u4-003 | PASS |
| wh-barrons-u4-004 | PASS | wh-barrons-u4-005 | PASS | wh-barrons-u4-006 | PASS |
| wh-barrons-u4-007 | PASS | wh-barrons-u4-008 | PASS (borderline) | wh-barrons-u4-009 | PASS |
| wh-barrons-u4-010 | PASS | wh-barrons-u4-011 | PASS | wh-barrons-u4-012 | PASS |
| wh-barrons-u4-013 | PASS | wh-barrons-u4-014 | PASS | wh-barrons-u4-015 | PASS |
| wh-barrons-u4-016 | PASS | wh-barrons-u4-017 | PASS | wh-barrons-u4-018 | PASS |
| wh-barrons-u4-019 | PASS | wh-barrons-u5-001 | PASS | wh-barrons-u5-002 | PASS |
| wh-barrons-u5-003 | PASS | wh-barrons-u5-004 | PASS | wh-barrons-u5-005 | PASS |
| wh-barrons-u5-006 | PASS | wh-barrons-u5-007 | PASS | wh-barrons-u5-008 | PASS |
| wh-barrons-u5-009 | PASS | wh-barrons-u5-010 | PASS | wh-barrons-u5-011 | PASS |
| wh-barrons-u5-012 | PASS | wh-barrons-u5-013 | PASS | wh-barrons-u5-014 | PASS |
| wh-barrons-u5-015 | PASS | wh-barrons-u6-001 | PASS | wh-barrons-u6-002 | PASS |
| wh-barrons-u6-003 | PASS | wh-barrons-u6-004 | PASS (borderline) | wh-barrons-u6-005 | PASS |
| wh-barrons-u6-006 | PASS | wh-barrons-u6-007 | PASS | wh-barrons-u6-008 | PASS (borderline) |
| wh-barrons-u6-009 | PASS | wh-barrons-u6-010 | PASS | wh-barrons-u6-011 | PASS |
| wh-barrons-u6-012 | PASS | wh-barrons-u6-013 | PASS | wh-barrons-u6-014 | PASS |
| wh-barrons-u6-015 | PASS | wh-barrons-u6-016 | PASS | wh-barrons-u6-017 | PASS |
| wh-barrons-u6-018 | PASS | wh-barrons-u6-019 | PASS | wh-barrons-u6-020 | PASS |
| wh-barrons-u6-021 | PASS | wh-barrons-u6-022 | PASS | wh-barrons-u6-023 | PASS |
| wh-barrons-u6-024 | PASS | wh-barrons-u6-025 | PASS | wh-barrons-u6-026 | PASS |
| wh-barrons-u6-027 | PASS | wh-barrons-u6-028 | PASS | wh-barrons-u6-029 | PASS |
| wh-barrons-u6-030 | PASS | wh-barrons-u6-031 | PASS | wh-barrons-u6-032 | PASS |
| wh-barrons-u6-033 | PASS | wh-barrons-u6-034 | PASS | wh-barrons-u6-035 | PASS |
| wh-barrons-u7-001 | PASS | wh-barrons-u7-002 | PASS | wh-barrons-u7-003 | PASS |
| wh-barrons-u7-004 | PASS | wh-barrons-u7-005 | PASS | wh-barrons-u7-006 | PASS |
| wh-barrons-u7-007 | PASS | wh-barrons-u7-008 | PASS | wh-barrons-u7-009 | PASS (borderline) |
| wh-barrons-u7-010 | PASS | wh-barrons-u7-011 | PASS | wh-barrons-u8-001 | PASS |
| wh-barrons-u8-002 | PASS | wh-barrons-u8-003 | PASS | wh-barrons-u8-004 | PASS |
| wh-barrons-u8-005 | PASS | wh-barrons-u8-006 | PASS | wh-barrons-u8-007 | PASS |
| wh-barrons-u8-008 | PASS | wh-barrons-u8-009 | PASS | wh-barrons-u8-010 | PASS |
| wh-barrons-u8-011 | PASS | wh-barrons-u9-001 | PASS | wh-barrons-u9-002 | PASS |
| wh-barrons-u9-003 | PASS | wh-barrons-u9-004 | PASS | wh-barrons-u9-005 | PASS (borderline) |
| wh-barrons-u9-006 | FAIL → rewritten (PASS) | wh-barrons-u9-007 | PASS | wh-barrons-u9-008 | PASS |
| wh-barrons-u9-009 | PASS | wh-barrons-u9-010 | PASS | wh-barrons-u9-011 | PASS |
| wh-barrons-u9-012 | PASS | wh-barrons-u9-013 | PASS (borderline) | wh-barrons-u9-014 | PASS |
| wh-barrons-u9-015 | PASS | wh-barrons-u9-016 | PASS | wh-barrons-u9-017 | PASS |
| wh-barrons-u9-018 | PASS | wh-barrons-u9-019 | PASS | wh-barrons-u9-020 | PASS |
| wh-barrons-u9-021 | PASS | wh-barrons-u9-022 | PASS | wh-barrons-u9-023 | PASS (borderline) |
| wh-barrons-u9-024 | PASS | | | | |

---

## Rewrite: `wh-barrons-u9-006` (id and key letter A kept)

**New angle:** organizational strategy — NOW as a women's "own NAACP" that would picket, sue, and lobby, i.e., second-wave feminism borrowing the civil-rights movement's tactical playbook. The source item asked how the document compares to first-wave feminist thinking; the rewrite asks what the NAACP model reveals about the movement's organizational DNA. Different question, different answer, different distractors.

- **stimulus:** "In 1966, Betty Friedan and other professional women founded the National Organization for Women. The immediate spark was the Equal Employment Opportunity Commission's refusal to enforce the Civil Rights Act's ban on sex discrimination — a provision many officials openly treated as a joke. The founders concluded that women needed their own NAACP: an organization that would picket, sue, and lobby for women's rights.\n\nThe comparison was a program, not a compliment. The NAACP had won school desegregation and voting rights through test-case litigation, mass pressure, and congressional lobbying; NOW's founders believed the same methods could break sex-segregated help-wanted ads, workplace discrimination, and quotas in professional schools. The new feminist movement would be built with tools the civil rights movement had already proved."
- **stem:** "The founders' decision to model NOW on the NAACP — a group that would 'picket, sue, and lobby' — best illustrates which of the following about the early second-wave feminist movement?"
- **options:**
  - (A) It borrowed its organizational tactics from the civil rights movement
  - (B) It rejected legal and political action in favor of cultural separatism
  - (C) It drew its leadership mainly from elected government officials
  - (D) It sought change only through constitutional amendment rather than enforcement of existing laws
- **key:** A
- **explanation:** "NOW was consciously built on the NAACP model: mass pressure, test-case lawsuits, and lobbying. The second wave's organizational DNA came from the Black freedom movement — the founders, many of them veterans of the civil-rights era, took tactics that had desegregated schools and won voting rights and aimed them at sex discrimination."
- **option_explanations:**
  - A: "Correct. The NAACP comparison shows the new movement adopting civil-rights methods for a new cause."
  - B: "Wrong. Picketing, suing, and lobbying are political-legal action — the opposite of withdrawing from politics."
  - C: "Wrong. The founders were writers, union officers, and activists, not elected officeholders."
  - D: "Wrong. NOW's first campaigns targeted enforcement of laws already on the books; the Equal Rights Amendment came later."

**IP self-check (rewrite vs `barrons-u9-006`):** source asked "how does this document compare to earlier feminist thinking?" with key "move beyond basic rights"; rewrite asks what the NAACP model illustrates (organizational tactics), key "borrowed tactics from the civil-rights movement", all distractors new. PASS.

**Facts self-check:** NOW founded 1966 ✓; EEOC's refusal to enforce the 1964 Act's sex-discrimination provision was the founding spark ✓; Friedan's "own NAACP" framing is documented ✓; NAACP's litigation/lobbying record (Brown 1954, VRA 1965) ✓; sex-segregated help-wanted ads and professional-school quotas are period-accurate ✓; ERA (1972) postdates NOW's first campaigns ✓. PASS.

---

## (b) FORMAT findings

- **(b)(i) MCQ-only:** every one of the 160 items in `build/reconceived/barrons/` has `options` + `key`; no SAQ/DBQ/LEQ items present. PASS — no violation.
- **(b)(ii) OLD-FORMAT tags in `build/reclaim-staged/barrons/frq.json` (16 items):** all 8 SAQ-with-choice items (t1/t2 variants) carry "OLD-FORMAT: complete 3 of 4; Q1+Q2 required, then choose Q3 or Q4"; both 3-choice LEQs carry "OLD-FORMAT: LEQ offers 3 choices (new CED = single prompt)"; the 4 standalone section SAQs (s1–s4) correctly lack choice tags (their notes state they are single required SAQs, no choice). PASS — no violation.

---

## (c) FACTS findings

All 160 items' stimuli, stems, options, and explanations were read and checked against AP World History knowledge.

- **Fact errors requiring fixes: 0.** Every load-bearing historical claim verified correct (sample: 1998 US energy consumption 94.6 quadrillion BTU; EEOC/1964 Act spark for NOW; Ambedkar/Mahar/Article 17; Decree 900 and Operation PBSUCCESS 1954; Kyoto 1997 and the US non-ratification; population milestones 1B/2B/4B/6B; tirailleurs sénégalais ~200,000; "cristallisation" of 1959; HBC charter 1670; Leo Africanus/al-Hasan al-Wazzan; Mogul/Tokugawa/Ming details).
- **[UNVERIFIED] flags: 0.** No claim load-bearing to an answer was unverifiable.
- **Minor caveat (not flagged, not load-bearing):** `wh-barrons-u8-010`'s explanation states Western intelligence backing of Nkrumah's 1966 overthrow as established fact; historians debate the extent of CIA involvement. The claim is tangential to the item's key (Nkrumah was abroad during the coup) and the stimulus itself hedges ("many assumed CIA involvement"), so no [UNVERIFIED] tag was applied. Suggested softening in a future pass if desired: "the army — widely suspected of Western intelligence backing — struck while he was in Hanoi."

---

## Mechanical gates output (run verbatim)

```
n= 160 keys= {'C': 40, 'B': 40, 'D': 40, 'A': 40} pct= {'C': 25.0, 'B': 25.0, 'D': 25.0, 'A': 25.0}
longest_is_key= 45 28.1 %
GATES GREEN
```

Full verbatim output:
- `n= 160 keys= {'C': 40, 'B': 40, 'D': 40, 'A': 40} pct= {'C': 25.0, 'B': 25.0, 'D': 25.0, 'A': 25.0}`
- `longest_is_key= 45 28.1 %`
- `GATES GREEN` (all keys ≤30%; longest-is-key 28.1% ≤30%)

---

## Commit

Commit message used: `compliance: clean-context review barrons (160 items, 1 IP rewrite, 0 unverified)`
