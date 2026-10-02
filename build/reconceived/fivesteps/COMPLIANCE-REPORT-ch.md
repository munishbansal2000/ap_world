# Compliance Report — 5 Steps chapters re-conceived set (clean-context review)

- Reviewer: independent (not involved in drafting). Date: 2026-10-02.
- Scope: `ch07-mcq.json` … `ch25-mcq.json` (19 files, **71 MCQs**), each compared against its `source_id` item in `build/reclaim-staged/fivesteps/ch*.json` (read-only comparison).
- Verdict: **PASS** after repairs (8 IP rewrites, 49 option-length edits). Mechanical gates were FAILED on intake; now GREEN.

## Mechanical gates (required script)

Intake run:
```
n= 71 keys= {'B': 23, 'A': 16, 'D': 16, 'C': 16} pct= {'B': 32.4, 'A': 22.5, 'D': 22.5, 'C': 22.5}
longest_is_key= 45 63.4 %
GATES FAILED
```
Post-repair run:
```
n= 71 keys= {'B': 18, 'A': 17, 'D': 19, 'C': 17} pct= {'B': 25.4, 'A': 23.9, 'D': 26.8, 'C': 23.9}
longest_is_key= 6 8.5 %
GATES GREEN
```
Repairs: key-letter rebalance (B was 32.4%, moved 5 B-keys out / 1 in via the IP rewrites); option-length rebalancing so the key is not the uniquely longest option (63.4% → 8.5%). Key letters were preserved on all length-only edits; all option edits preserve meaning and keep explanations accurate.

## (a) IP check — per-item verdicts

FAIL = same angle AND same distractor set (reworded) as the source item. All 8 failures were rewritten with a new angle, fresh distractors, and own explanation, then re-checked.

| id | src | verdict | note |
|---|---|---|---|
| wh-fivesteps-u1-001 | fivesteps-u1-012 | PASS | different angle (military-fiscal causation vs phrase definition), fresh distractors |
| wh-fivesteps-u1-002 | fivesteps-u1-013 | PASS | different angle (secularism thesis vs chronology ordering) |
| wh-fivesteps-u1-003 | fivesteps-u1-014 | PASS | different angle (printing-press capacity vs secular institutions) |
| wh-fivesteps-u2-001 | fivesteps-u2-005 | PASS | different angle (Crusade financing of Renaissance vs humanism link) |
| wh-fivesteps-u2-002 | fivesteps-u2-006 | PASS | different angle (transmission mechanism vs "first Renaissance" label) |
| wh-fivesteps-u2-003 | fivesteps-u2-007 | PASS | different angle (trade-post→territorial shift vs voyage characterization) |
| wh-fivesteps-u1-004 | fivesteps-u1-015 | PASS | different angle (Inca/Aztec trade comparison, fresh distractors) |
| wh-fivesteps-u1-005 | fivesteps-u1-016 | PASS | different angle (shared Persian/Inca practice vs which people) |
| wh-fivesteps-u1-006 | fivesteps-u1-017 | PASS | different angle (Confucian assumption vs best supporting line) |
| wh-fivesteps-u1-007 | fivesteps-u1-018 | PASS | different angle (political threat beyond economics vs historian's reason) |
| wh-fivesteps-u1-008 | fivesteps-u1-019 | PASS | different angle (tribute as diplomatic ritual vs description) |
| wh-fivesteps-u1-009 | fivesteps-u1-020 | PASS | different angle (gekokujo term vs long-term consequence) |
| wh-fivesteps-u1-010 | fivesteps-u1-021 | PASS | different angle (Song vulnerability mechanism vs fall reason) |
| wh-fivesteps-u3-001 | fivesteps-u3-001 | PASS | different angle (why China demanded silver vs what was shipped) |
| wh-fivesteps-u3-002 | fivesteps-u3-002 | PASS | different angle (who Price Revolution harmed vs impact of exchange) |
| wh-fivesteps-u3-003 | fivesteps-u3-003 | PASS | different angle (Glorious Revolution mechanism vs which nation) |
| wh-fivesteps-u3-004 | fivesteps-u3-004 | PASS | different angle (Akbar policy vs true-of-Mughals) |
| wh-fivesteps-u3-005 | fivesteps-u3-005 | PASS | different angle (Canton/Nagasaki similarity vs comparison) |
| wh-fivesteps-u4-001 | fivesteps-u4-018 | **FAIL → REWRITTEN** | kept source design: identical "most appropriate caption" stem + same four-concept distractor set reworded |
| wh-fivesteps-u4-002 | fivesteps-u4-019 | PASS | different angle (horse/Plains transformation vs benefit) |
| wh-fivesteps-u4-003 | fivesteps-u4-020 | PASS | different angle (potato mechanism vs Europe impact) |
| wh-fivesteps-u4-004 | fivesteps-u4-021 | PASS | different angle (capitalism vs mercantilism vs term definition) |
| wh-fivesteps-u4-005 | fivesteps-u4-022 | PASS | different angle (least integrated region vs trade accuracy) |
| wh-fivesteps-u4-006 | fivesteps-u4-023 | PASS | different angle (sugar/labor demand vs slave-shipment growth) |
| wh-fivesteps-u4-007 | fivesteps-u4-024 | PASS | different angle (what estimate illustrates vs where most ended up) |
| wh-fivesteps-u4-008 | fivesteps-u4-025 | PASS | different angle (Brazil/Haiti syncretism cases vs syncretism example) |
| wh-fivesteps-u4-009 | fivesteps-u4-026 | PASS | different angle (textile deindustrialization vs trade effect) |
| wh-fivesteps-u4-010 | fivesteps-u4-027 | PASS | different angle (Bacon's method vs phrase summary) |
| wh-fivesteps-u4-011 | fivesteps-u4-028 | PASS | different angle (Jupiter moons vs Bacon link) |
| wh-fivesteps-u4-012 | fivesteps-u4-029 | PASS | different angle (legitimacy basis vs resulting government form) |
| wh-fivesteps-u4-013 | fivesteps-u4-030 | PASS | different angle (Deist distinction vs which lacked natural law) |
| wh-fivesteps-u5-001 | fivesteps-u5-005 | PASS | different angle (what 1895 demonstrated vs quote event ID) |
| wh-fivesteps-u5-002 | fivesteps-u5-006 | PASS | different angle (fukoku kyohei meaning vs Meiji motive) |
| wh-fivesteps-u5-003 | fivesteps-u5-007 | PASS | different angle (why subsidize railroads vs critical development) |
| wh-fivesteps-u5-004 | fivesteps-u5-008 | PASS | different angle (invisible-hand meaning vs theory name) |
| wh-fivesteps-u5-005 | fivesteps-u5-009 | PASS | different angle (separate spheres content vs social change) |
| wh-fivesteps-u5-006 | fivesteps-u5-010 | PASS | different angle (why criollos backed independence vs castes involved) |
| wh-fivesteps-u5-007 | fivesteps-u5-011 | PASS | different angle (purity-of-blood origin vs who held control) |
| wh-fivesteps-u6-001 | fivesteps-u6-005 | PASS | different angle (Berlin Act gap vs "blessings" meaning) |
| wh-fivesteps-u6-002 | fivesteps-u6-006 | PASS | different angle (how Livingstone formula served empire vs who fulfills goal) |
| wh-fivesteps-u6-003 | fivesteps-u6-007 | PASS | different angle (irony of sarcastic usage vs phrase meaning) |
| wh-fivesteps-u6-004 | fivesteps-u6-008 | **FAIL → REWRITTEN** | kept source design: identical "caption fits best" stem + same four caption concepts reworded |
| wh-fivesteps-u6-005 | fivesteps-u6-009 | PASS | different angle (investment pattern vs economy truth) |
| wh-fivesteps-u6-006 | fivesteps-u6-010 | PASS | different angle (why Balkan revolts succeeded vs decline factor) |
| wh-fivesteps-u6-007 | fivesteps-u6-011 | PASS | different angle (why sell opium vs what prompted actions) |
| wh-fivesteps-u6-008 | fivesteps-u6-012 | PASS | different angle (treaty ports in practice vs Opium War impact) |
| wh-fivesteps-u6-009 | fivesteps-u6-013 | PASS | different angle (why pattern favored West vs trade characterization) |
| wh-fivesteps-u7-001 | fivesteps-u7-015 | PASS | different angle (invasion's direct result vs sequence position) |
| wh-fivesteps-u7-002 | fivesteps-u7-016 | PASS | different angle (Munich assumption vs policy name) |
| wh-fivesteps-u7-003 | fivesteps-u7-017 | PASS | different angle (how USSR converted presence to domination vs long-term impact) |
| wh-fivesteps-u8-001 | fivesteps-u8-001 | PASS | different angle (what bomb represents vs artist's attitude) |
| wh-fivesteps-u8-002 | fivesteps-u8-002 | PASS | different angle (cartoonist's implication vs artist's purpose) |
| wh-fivesteps-u8-003 | fivesteps-u8-003 | PASS | different angle (immediate human consequence vs ultimate outcome) |
| wh-fivesteps-u8-004 | fivesteps-u8-004 | PASS | different angle (why nationalism fatal vs contributing factor) |
| wh-fivesteps-u8-005 | fivesteps-u8-005 | **FAIL → REWRITTEN** | kept source design: same "immediate consequence of 1991" angle + distractor set mapped 1:1 onto the source's |
| wh-fivesteps-u8-006 | fivesteps-u8-006 | PASS | different angle (why Chernobyl hurt legitimacy vs domestic-factor timeline) |
| wh-fivesteps-u8-007 | fivesteps-u8-007 | **FAIL → REWRITTEN** | kept source design: same "common problem of Japan and Russia" angle with two verbatim distractors retained |
| wh-fivesteps-u9-001 | fivesteps-u9-002 | **FAIL → REWRITTEN** | kept source design: same "which economic philosophy" angle + same generic-ism distractor set |
| wh-fivesteps-u9-002 | fivesteps-u9-003 | PASS | different angle (market-reform cases vs Coyne counter-example) |
| wh-fivesteps-u9-003 | fivesteps-u9-004 | PASS | different angle (policy both support vs org least likely) |
| wh-fivesteps-u9-004 | fivesteps-u9-005 | PASS | different angle (Myanmar laptop meaning vs image theme) |
| wh-fivesteps-u9-005 | fivesteps-u9-006 | PASS | different angle (social concern vs theme) |
| wh-fivesteps-u9-006 | fivesteps-u9-007 | PASS | different angle (what problem modem solved vs which invention) |
| wh-fivesteps-u9-007 | fivesteps-u9-008 | **FAIL → REWRITTEN** | kept source design: same "what phenomenon was UDHR responding to" angle + distractor set largely reworded 1:1 |
| wh-fivesteps-u9-008 | fivesteps-u9-009 | **FAIL → REWRITTEN** | kept source design: same angle + distractor set mapped 1:1 (regional→national, belief, effort, documents) |
| wh-fivesteps-u9-009 | fivesteps-u9-010 | PASS | different angle (UDHR influence on new states vs what it inspired) |
| wh-fivesteps-u9-010 | fivesteps-u9-011 | PASS | different angle (Liberation Theology central claim vs outgrowth of passage) |
| wh-fivesteps-u9-011 | fivesteps-u9-012 | **FAIL → REWRITTEN** | kept source design: same "what did USSR/Japan/US/W.Europe have in common" angle + same distractor set reworded |
| wh-fivesteps-u9-012 | fivesteps-u9-013 | PASS | different angle (legal consequence vs definition) |
| wh-fivesteps-u9-013 | fivesteps-u9-014 | PASS | different angle (remittance meaning vs disproportionate effect) |
| wh-fivesteps-u9-014 | fivesteps-u9-015 | PASS | different angle (why direction reversed vs least common pattern) |

### The 8 IP rewrites (ids kept; new angles; re-verified clean)

1. **wh-fivesteps-u4-001** (ch12, key now D): "Which was the largest demographic consequence of the Columbian Exchange for the Americas?" — epidemic-disease collapse of Native populations. Fresh distractors (European immigration scale, voluntary African migration, crop-driven birthrates).
2. **wh-fivesteps-u6-004** (ch17, key now C): "Why did the Congo Free State produce some of the worst atrocities of the New Imperialism era?" — rubber quotas enforced by terror (Force Publique). Fresh distractors (settlers/farmland, missionary rivalry, drought).
3. **wh-fivesteps-u8-005** (ch21, key now B): "Why did Gorbachev's policies of glasnost and perestroika fail to save the Soviet Union?" — freed criticism + half-measures wrecking the planned economy. Fresh distractors.
4. **wh-fivesteps-u8-007** (ch21, key now D): "Which of the following best contrasts the origins of Japan's 1990s stagnation and Russia's 1990s economic collapse?" — burst asset bubble vs dismantled planning. Fresh distractors.
5. **wh-fivesteps-u9-001** (ch22, key now C): "Which development most directly challenged the Washington Consensus in the late 1990s?" — 1997 East Asian financial crisis. Fresh distractors.
6. **wh-fivesteps-u9-007** (ch24, key now D): "Which statement about the Universal Declaration of Human Rights (1948) is most accurate?" — Eleanor Roosevelt chaired the drafting commission. Fresh distractors.
7. **wh-fivesteps-u9-008** (ch24, key now A): "Roosevelt's phrase 'small places, close to home' referred to which of the following?" — neighborhoods/schools/workplaces of daily life. Fresh distractors.
8. **wh-fivesteps-u9-011** (ch24, key now A): "Postwar Western European welfare states differed from the Soviet model most fundamentally in which way?" — market economies + social protections vs command economy. Fresh distractors.

Resulting key distribution: A 17 / B 18 / C 17 / D 19 (all ≤ 29.6%).

## (b) Format check

- (i) **All 71 items in `reconceived/fivesteps/ch07–ch25-mcq.json` are `type: "mcq"`** — no SAQ/DBQ/LEQ items present. PASS.
- (ii) Spot-check of `build/reclaim-staged/fivesteps/frq.json`: all 40 items (28 saq, 9 leq, 3 dbq) carry `format: "old"` and an `old_format_note` reading "OLD FORMAT: predates Fall 2026 CED (SAQ choice, LEQ 3-choice)." SAQ-with-choice and 3-choice LEQ items are tagged as required. No violations.

## (c) Facts check

All 71 items' historical claims verified against standard scholarship from the reviewer's own knowledge. No wrong claims found; **no key changes** were needed for factual reasons. Notes:

- u4-007 ("more enslaved Africans remained within Africa than were shipped across the Atlantic"): standard published historian estimate (Manning/Lovejoy tradition) — treated as verifiable scholarship, not flagged.
- u9-013 ("over $800 billion a year in remittances" by the 2020s): consistent with World Bank/KNOMAD global remittance totals for the 2020s (~$850B+). Not flagged.
- u9-008 rewrite's 1958 Roosevelt "small places, close to home" speech attribution and u9-007 rewrite's Eleanor Roosevelt drafting-commission chairmanship: verified correct.
- u6-003's "1939 film set in 1885" (Stagecoach) framing: consistent with the source stimulus.

**[UNVERIFIED] flags: none.** No material claim required flagging.

## Files changed

- `build/reconceived/fivesteps/ch12-mcq.json`, `ch17-mcq.json`, `ch21-mcq.json`, `ch22-mcq.json`, `ch24-mcq.json` (IP rewrites)
- `ch07, ch08, ch09, ch10, ch11, ch12, ch13, ch14, ch15, ch17, ch18, ch19, ch20, ch21, ch22, ch23, ch24, ch25-mcq.json` (option-length rebalancing)
- This report: `build/reconceived/fivesteps/COMPLIANCE-REPORT-ch.md`

## Residual notes for parent

- The mechanical gates FAILED on intake (B-key 32.4%, longest-is-key 63.4%); both repaired in this pass — worth confirming the upstream drafting pipeline now emits balanced options natively.
- Two borderline items (u8-007, u9-001) were failed conservatively; the re-conceived set is now clean by the stated bar.
- No git-history concerns introduced; only ch files + report committed.
