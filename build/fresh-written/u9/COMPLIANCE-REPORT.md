# Compliance Report — AP World Unit 9 Fresh-Written MCQs

**Reviewer:** clean-context compliance pass (no prior exposure to the items)
**Date:** 2026-10-02
**Files:** `batch-01.json`, `batch-02.json`, `batch-03.json`, `batch-04.json`
**Items reviewed:** 33 (wh-fresh-u9-001 … wh-fresh-u9-033)

Scope: originality/IP, fabrication (quotes/speeches/statistics), fact spot-checks via non-College-Board web sources, MCQ-only format, visual honesty. Keys were not changed. No [UNVERIFIED] flags were added — every flagged issue was repairable in place and repaired. **Nothing is recommended for quarantine.**

## Verdict summary

| Check | Result |
|---|---|
| Items reviewed | 33 |
| Originality/IP issues | 0 |
| Invented quotes found | 1 stimulus (repaired — was not verbatim fabrication, but styled as direct quotes) |
| Factual errors found | 2 (both repaired) |
| Format violations | 0 (all MCQ, 4 options, stems end with ? or :) |
| Visual-honesty failures | 0 after repair |
| Keys changed | 0 |
| [UNVERIFIED] flags added | 0 |
| Quarantine recommendations | 0 |

## Repairs made (3, none affecting keys)

**R1 — u9-004 + u9-005 stimulus mislabeled (data error, repaired).**
Both stimuli described a "Line chart titled 'World merchandise exports as a share of world GDP, 1960-2020'" with values rising ~25% (1960) → ~60% (2008), dipping in 2009, recovering after. Verified against World Bank WDI data: world **trade (exports + imports of goods and services) as % of GDP** was 60.68 in 2008, rose to ~61% before the 2009 crash to 52%, and recovered in 2011 — but world **merchandise exports alone** as % of GDP are roughly half those values. The title mislabeled the series the numbers describe. Repaired title to: 'World trade (exports and imports of goods and services) as a share of world GDP, 1960-2020.' Also corrected the u9-004 explanation ("exports rising" → "trade … rising"; removed "the chart measures merchandise (goods) exports" claim). The "Data: World Bank, 2024" source note was already correct and is unchanged. Key A on both items is unaffected ("the share of national output traded across borders more than doubled" is true of the corrected series: 25% → 60%).

**R2 — u9-023 + u9-024 stimulus date (unverifiable date, repaired to documented anchor).**
Stimulus was "News report, Durban, South Africa, 2001 (paraphrased)". Web verification found the canonical documented anchor: the **July 9, 2000** "Global March for Treatment Access" in Durban during the XIII International AIDS Conference (~5,000 TAC-organized marchers demanding affordable antiretroviral access). No 2001-specific Durban march could be verified. Date repaired to **2000** in both stimuli (same report shared by both items); nothing else in the stimulus changed. Keys (A, D) unaffected.

**R3 — u9-031 invented historian quotes (repaired to paraphrase).**
Stimulus presented Historian A and Historian B in direct quotation marks. These are invented speeches, not sourced quotes. Repaired to paraphrased positions ("Two historians on globalization and democracy (positions paraphrased). Historian A argues that… Historian B counters that…"), `stimulus_words` updated 47 → 55. Key (A) unaffected; explanations reference the content, not the quote marks, and remain valid.

## Fact spot-checks (web-verified, all PASS)

- **WTO established 1995** (u9-005) — consensus, pass.
- **Kyoto Protocol 1997, Paris Agreement 2015** (u9-020/021/022) — pass. CO2 data: 1960 annual mean ≈ 316.9 ppm ("about 315" fine); 2024 ≈ 424 ppm ("about 425" fine); NOAA maintains the record — pass.
- **Shenzhen SEZ designated 26 August 1980** under Deng (u9-027/028) — pass.
- **West Germany–Turkey labor recruitment agreement, 30 Oct 1961** (u9-029/030) — pass.
- **South Africa TRC 1996, democratic elections 1994** (u9-015/016) — pass.
- **9/11: four airliners, WTC + Pentagon, ~3,000 dead; Afghanistan 2001, Iraq 2003** (u9-032) — pass.
- **English ≈ 1.5 billion speakers** by 2020 (u9-033; BBC/Ethnologue/British Council consensus) — pass.
- **EU 27 members, USMCA 3 members, ASEAN 10 members** (u9-017/018/019); **euro introduced 1999** (u9-005) — pass.
- **Tiananmen/Tank Man June 5, 1989; Berlin Wall fall Nov 1989; Tahrir Jan 2011; Gorbachev 1985 → dissolution 1991** — pass.

## Originality / IP

All stimuli, stems, and options read as original textbook-style prose. Every historical "quote" in the batch is explicitly marked **(paraphrased)** — none present invented verbatim speech except R3 above, now repaired. No passage resembles a known textbook, prep book, or web article. No item is a lifted excerpt. PASS.

## Format

Programmatic check: all 33 items `type == "mcq"`, exactly 4 options, every stem ends with `?` or `:`. No SAQ/LEQ structures. PASS.

## Visual honesty

After R1, all `visual_needs_url` stimuli describe real, findable visuals:
- 004/005: World Bank "Trade (% of GDP)" line chart (Our World in Data / World Bank carry it).
- 008/009/010: Singapore container-port photograph (common stock/editorial subject).
- 017/018/019: regional trade-agreement world map (EU/USMCA/ASEAN).
- 020/021/022: NOAA Global Climate Dashboard CO2 + temperature graph (315 ppm 1960 → ~425 ppm 2024 matches the record).
- 027/028: Shenzhen 1980-vs-2020 before/after aerials (widely published comparison images).
The AUDIT-REPORT.md also notes each visual item's stimulus text is self-contained — nothing requires an undescribed visual to answer. PASS.

## Deliberately-false distractors (confirmed as distractors, not item defects)

- u9-005 (B): "the Soviet Union dissolved in 1991, an event that directly created the WTO" — intentionally false, correctly keyed out.
- u9-025 (C): "the reunification of Germany after World War I, when the Treaty of Versailles merged East and West Germany" — intentionally absurd, correctly keyed out.
- u9-007 (D): "China and Cuba held free elections [in 1989]" — intentionally false, correctly keyed out.

## No [UNVERIFIED] flags, no quarantines

Every risk was either verified or repaired. Post-repair re-validation: all four files parse as valid JSON, all 33 items remain MCQ × 4 options, and the keys of the five repaired items (004 A, 005 C, 023 A, 024 D, 031 A) are byte-identical to the values the blind key audit (AUDIT-REPORT.md) validated — so the key audit still holds.
