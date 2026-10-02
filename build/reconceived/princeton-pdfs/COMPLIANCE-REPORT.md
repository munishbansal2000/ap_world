# Clean-Context Compliance Review — princeton-pdfs (Practice Tests 4–6)

**Date:** 2026-10-02 | **Reviewer:** independent subagent (no role in drafting) | **Scope:** 165 re-conceived MCQs
(pt4-mcq.json, pt5-mcq.json, pt6-mcq.json, 55 each) vs. source items in `build/reclaim-staged/princeton-pdfs/*.json` (matched via `source_id`).

**Verdict: PASS** — 3 IP rewrites + 1 facts/explanation repair applied, all re-checked; [UNVERIFIED] flags on 4 items (1 distinct claim); format checks clean; mechanical gates green.

## (a) IP — verdicts

**Result:** 161 PASS (11 borderline-passes with fresh distractor sets), 3 FAIL → REWRITTEN. The FAIL test: same question angle **AND** same distractor set (reworded) as the source item.

### Rewrites (new angle + fresh distractors + own explanation; `id` kept; key letters changed where the new item required it)

1. **`wh-princeton-pdf6-u4-003`** (Erasmus/Henry VIII, now key A)
   - Old design: source asked "which event's outcome most resembled Luther's movement" (answer: England's break from Rome); re-conceived asked "which break is most comparable to Luther's" (key Henry VIII), keeping Council of Trent + Jesuits as distractors — same angle and substantially the same distractor set. FAIL.
   - New angle: Erasmus stayed Catholic while Luther broke — what does shared criticism but different outcomes illustrate? Key: reformist criticism could lead either to internal Catholic reform or to schism. Fresh distractors (all critics executed / Erasmus converted / papacy abolished monastic orders in 1520).
2. **`wh-princeton-pdf6-u2-005`** (Mongol invasions/Ibn al-Athir, now key A)
   - Old design: same angle as source (Islamic cities destroyed, key = cities destroyed) and 3 of 4 distractors substantially identical (forced conversion, holy cities/mecca, destroyed cities). FAIL.
   - New angle: what Mongol rule most directly facilitated → the Pax Mongolica's revival of Silk Road trade (yam relay stations, travel passes). Fresh distractors.
3. **`wh-princeton-pdf5-u8-002`** (telegraph cable via Egypt/Suez, now key C)
   - Old design: same angle as source (why route via Egypt = Suez Canal) with same key concept and 2 of 3 distractors sharing concepts. Borderline-fail → rewritten for safety.
   - New angle: what Britain's cable investment illustrates about 19th-c. imperialism → imperial control depended on communications infrastructure as much as troops. Fresh distractors.

### Facts/explanation repair (not IP)
- **`wh-princeton-pdf5-u2-005`** (was: monsoon question stapled to the 1870 cable-map stimulus; explanation falsely claimed "The passage itself credits the monsoon winds as the foundation of Aden's fortune" — the stimulus is a cable map and says nothing about monsoons). Rewritten as a map-grounded item: the network as part of the 19th-c. communications revolution; why it mattered to empires and merchants (key A). Also fixes the explanation's phantom claim.
- **`wh-princeton-pdf6-u8-001`**: softened an overreach — explanation said Source 2 appeals to "the UN Charter's self-determination"; the excerpt itself cites the Palestinian people's "natural right" and will (the self-determination principle). Wording corrected; key unaffected.

### Per-item IP verdicts

### pt4-mcq.json
- wh-princeton-pdf4-u3-001: PASS
- wh-princeton-pdf4-u3-002: PASS
- wh-princeton-pdf4-u4-001: PASS
- wh-princeton-pdf4-u4-002: PASS
- wh-princeton-pdf4-u4-003: PASS
- wh-princeton-pdf4-u4-004: PASS
- wh-princeton-pdf4-u5-001: PASS
- wh-princeton-pdf4-u5-002: PASS
- wh-princeton-pdf4-u5-003: PASS
- wh-princeton-pdf4-u6-001: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf4-u6-002: PASS
- wh-princeton-pdf4-u6-003: PASS
- wh-princeton-pdf4-u6-004: PASS
- wh-princeton-pdf4-u6-005: PASS
- wh-princeton-pdf4-u8-001: PASS
- wh-princeton-pdf4-u8-002: PASS
- wh-princeton-pdf4-u8-003: PASS
- wh-princeton-pdf4-u8-004: PASS
- wh-princeton-pdf4-u6-006: PASS
- wh-princeton-pdf4-u6-007: PASS
- wh-princeton-pdf4-u3-003: PASS
- wh-princeton-pdf4-u3-004: PASS
- wh-princeton-pdf4-u3-005: PASS
- wh-princeton-pdf4-u3-006: PASS
- wh-princeton-pdf4-u2-001: PASS
- wh-princeton-pdf4-u2-002: PASS
- wh-princeton-pdf4-u2-003: PASS
- wh-princeton-pdf4-u2-004: PASS
- wh-princeton-pdf4-u6-008: PASS
- wh-princeton-pdf4-u6-009: PASS
- wh-princeton-pdf4-u6-010: PASS
- wh-princeton-pdf4-u6-011: PASS
- wh-princeton-pdf4-u3-007: PASS
- wh-princeton-pdf4-u3-008: PASS
- wh-princeton-pdf4-u7-001: PASS
- wh-princeton-pdf4-u7-002: PASS
- wh-princeton-pdf4-u7-003: PASS
- wh-princeton-pdf4-u7-004: PASS
- wh-princeton-pdf4-u8-005: PASS
- wh-princeton-pdf4-u8-006: PASS
- wh-princeton-pdf4-u8-007: PASS
- wh-princeton-pdf4-u8-008: PASS
- wh-princeton-pdf4-u8-009: PASS
- wh-princeton-pdf4-u6-012: PASS
- wh-princeton-pdf4-u6-013: PASS
- wh-princeton-pdf4-u6-014: PASS
- wh-princeton-pdf4-u6-015: PASS
- wh-princeton-pdf4-u6-016: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf4-u6-017: PASS
- wh-princeton-pdf4-u6-018: PASS
- wh-princeton-pdf4-u8-010: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf4-u8-011: PASS
- wh-princeton-pdf4-u8-012: PASS
- wh-princeton-pdf4-u8-013: PASS
- wh-princeton-pdf4-u8-014: PASS

### pt5-mcq.json
- wh-princeton-pdf5-u1-001: PASS
- wh-princeton-pdf5-u1-002: PASS
- wh-princeton-pdf5-u1-003: PASS
- wh-princeton-pdf5-u1-004: PASS
- wh-princeton-pdf5-u2-001: PASS
- wh-princeton-pdf5-u2-002: PASS
- wh-princeton-pdf5-u2-003: PASS
- wh-princeton-pdf5-u2-004: PASS
- wh-princeton-pdf5-u2-005: PASS
- wh-princeton-pdf5-u2-006: PASS
- wh-princeton-pdf5-u3-001: PASS
- wh-princeton-pdf5-u3-002: PASS
- wh-princeton-pdf5-u3-003: PASS
- wh-princeton-pdf5-u4-001: PASS
- wh-princeton-pdf5-u4-002: PASS
- wh-princeton-pdf5-u4-003: PASS
- wh-princeton-pdf5-u4-004: PASS
- wh-princeton-pdf5-u4-005: PASS
- wh-princeton-pdf5-u4-006: PASS
- wh-princeton-pdf5-u4-007: PASS
- wh-princeton-pdf5-u4-008: PASS
- wh-princeton-pdf5-u4-009: PASS
- wh-princeton-pdf5-u4-010: PASS
- wh-princeton-pdf5-u4-011: PASS
- wh-princeton-pdf5-u4-012: PASS
- wh-princeton-pdf5-u4-013: PASS
- wh-princeton-pdf5-u4-014: PASS
- wh-princeton-pdf5-u4-015: PASS
- wh-princeton-pdf5-u4-016: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf5-u4-017: PASS
- wh-princeton-pdf5-u6-001: PASS
- wh-princeton-pdf5-u6-002: PASS
- wh-princeton-pdf5-u6-003: PASS
- wh-princeton-pdf5-u6-004: PASS
- wh-princeton-pdf5-u6-005: PASS
- wh-princeton-pdf5-u6-006: PASS
- wh-princeton-pdf5-u6-007: PASS
- wh-princeton-pdf5-u6-008: PASS
- wh-princeton-pdf5-u6-009: PASS
- wh-princeton-pdf5-u7-001: PASS
- wh-princeton-pdf5-u7-002: PASS
- wh-princeton-pdf5-u7-003: PASS
- wh-princeton-pdf5-u8-001: PASS
- wh-princeton-pdf5-u8-002: FAIL -> REWRITTEN (see rewrites)
- wh-princeton-pdf5-u8-003: PASS
- wh-princeton-pdf5-u8-004: PASS
- wh-princeton-pdf5-u8-005: PASS
- wh-princeton-pdf5-u8-006: PASS
- wh-princeton-pdf5-u8-007: PASS
- wh-princeton-pdf5-u8-008: PASS
- wh-princeton-pdf5-u8-009: PASS
- wh-princeton-pdf5-u8-010: PASS
- wh-princeton-pdf5-u8-011: PASS
- wh-princeton-pdf5-u8-012: PASS
- wh-princeton-pdf5-u8-013: PASS

### pt6-mcq.json
- wh-princeton-pdf6-u2-001: PASS
- wh-princeton-pdf6-u2-002: PASS
- wh-princeton-pdf6-u2-003: PASS
- wh-princeton-pdf6-u4-001: PASS
- wh-princeton-pdf6-u4-002: PASS
- wh-princeton-pdf6-u4-003: FAIL -> REWRITTEN (see rewrites)
- wh-princeton-pdf6-u2-004: PASS
- wh-princeton-pdf6-u2-005: FAIL -> REWRITTEN (see rewrites)
- wh-princeton-pdf6-u2-006: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u2-007: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u4-004: PASS
- wh-princeton-pdf6-u4-005: PASS
- wh-princeton-pdf6-u4-006: PASS
- wh-princeton-pdf6-u5-001: PASS
- wh-princeton-pdf6-u5-002: PASS
- wh-princeton-pdf6-u5-003: PASS
- wh-princeton-pdf6-u8-001: PASS
- wh-princeton-pdf6-u8-002: PASS
- wh-princeton-pdf6-u8-003: PASS
- wh-princeton-pdf6-u2-008: PASS
- wh-princeton-pdf6-u2-009: PASS
- wh-princeton-pdf6-u4-007: PASS
- wh-princeton-pdf6-u2-010: PASS
- wh-princeton-pdf6-u3-001: PASS
- wh-princeton-pdf6-u3-002: PASS
- wh-princeton-pdf6-u3-003: PASS
- wh-princeton-pdf6-u3-004: PASS
- wh-princeton-pdf6-u6-001: PASS
- wh-princeton-pdf6-u6-002: PASS
- wh-princeton-pdf6-u6-003: PASS
- wh-princeton-pdf6-u7-001: PASS
- wh-princeton-pdf6-u7-002: PASS
- wh-princeton-pdf6-u7-003: PASS
- wh-princeton-pdf6-u6-004: PASS
- wh-princeton-pdf6-u6-005: PASS
- wh-princeton-pdf6-u6-006: PASS
- wh-princeton-pdf6-u6-007: PASS
- wh-princeton-pdf6-u4-008: PASS
- wh-princeton-pdf6-u4-009: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u4-010: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u6-008: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u7-004: PASS
- wh-princeton-pdf6-u7-005: PASS
- wh-princeton-pdf6-u7-006: PASS
- wh-princeton-pdf6-u7-007: PASS
- wh-princeton-pdf6-u4-011: PASS
- wh-princeton-pdf6-u4-012: PASS
- wh-princeton-pdf6-u4-013: PASS
- wh-princeton-pdf6-u4-014: PASS
- wh-princeton-pdf6-u3-005: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u3-006: PASS
- wh-princeton-pdf6-u3-007: PASS
- wh-princeton-pdf6-u1-001: PASS
- wh-princeton-pdf6-u1-002: PASS (borderline: same angle/key as source, fresh distractor set)
- wh-princeton-pdf6-u1-003: PASS

## (b) FORMAT

- **(i) Reconceived dir:** all 165 items have `type: "mcq"` — no SAQ/DBQ/LEQ items present. PASS.
- **(ii) `build/reclaim-staged/princeton-pdfs/frq.json`:** all 18 FRQ entries carry `format: "old"` with OLD-FORMAT notes. SAQ3/4 carry "OLD-FORMAT SAQ choice (pre-Fall-2026 CED: answer Q3 or Q4)"; LEQs carry "OLD-FORMAT LEQ choice of 3 (pre-Fall-2026 CED)". PASS — no violations.

## (c) FACTS

Every item's historical claims were verified from the reviewer's own knowledge. Spot-checked samples: Leviathan 1651; Anglo-Zulu War 1879, diamonds 1867, gold 1886, Union of South Africa 1910; GLF 1958–61 with famine 1959–61; Mansa Musa hajj 1324; Aden 1839 / Suez 1869 / Egypt 1882; Tordesillas 370 leagues; Fitch 1599, Shimabara 1637–38, Single Whip 1581; Bismarck 1883/84/89 insurance laws; Meerut May 1857, Vellore 1806 dress regulations; Shimonoseki 1895; Haile Selassie 1936, Article 16; Khomeini 1979, 1953 coup, 444-day hostage crisis; Peter the Great beard tax 1705 (per the Jean Rousset de Missy account as the source book presents it); Ming baochao c. 1375, 1,000-cash string, counterfeiter penalties; Songhai 1460s–1591; Maji-Maji 1905–07; Guaman Poma c. 1615.

**Visual reconstructions (30 items):** GLF poster (slogan "brave the wind and the waves" documented for 1958), 1835 power-loom engraving, Soviet youth poster (caption matches source), 1870 British cable map (routes consistent with Eastern Telegraph network), Izvestiia 1930 "Old Way of Life", African trade map (state labels/dates match), Mongol 1227 map (labels match), Ming baochao (British Museum note, warning/inscription details documented), "The Only One Barred Out" 1882 (title/caption match), Americas population chart (pattern standard; see [UNVERIFIED] below). All historically accurate descriptions.

### [UNVERIFIED] flags (4 items, 1 distinct claim)
- `wh-princeton-pdf6-u4-008`, `-u4-009`, `-u4-010`, `wh-princeton-pdf6-u6-008`: the shared stimulus's pre-1500 population baseline of ~8–10 million is a low-end estimate; scholarly estimates of the pre-contact Americas population are contested (~8M to 100M+). Explanations now carry `[UNVERIFIED: ...]` on that baseline. Keys are unaffected (all four test 1500s collapse causes, migration, etc.).

### Source-extraction artifacts (not our defects; noted for the record)
Source JSON items carry `key: "?"` with "No answer key is included in the interactive PDF" and several extraction typos ("(A) CA standing military", "AA list", "DA diamond rush"). The re-conceived keys were derived from historical knowledge and were re-derived independently in this review.

## Mechanical gates (re-run after rewrites)

```
n= 165 keys= {'A': 47, 'B': 42, 'C': 39, 'D': 37} pct= {'A': 28.5, 'B': 25.5, 'C': 23.6, 'D': 22.4}
longest_is_key= 25 15.2 %
GATES GREEN
```

Keys ≤ 30% each (max 28.5%); longest-distractor-is-key 15.2% ≤ 30%. GATES GREEN.
