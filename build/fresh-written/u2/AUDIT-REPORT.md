# Blind Key Audit Report — AP World Unit 2, Fresh-Written Batches 01–03

**Auditor role:** clean-context key auditor (no prior exposure to these items; derivation from stimulus + stem + historical knowledge only).
**Items audited:** 30 (`wh-fresh-u2-001` … `wh-fresh-u2-030`)
**Date:** 2026-10-02
**Files:** `batch-01.json`, `batch-02.json`, `batch-03.json` in `build/fresh-written/u2/`

## Method note (honesty about blindness)
The keys are stored inline in the same JSON objects as the stimuli, so a perfectly blind read was not possible — the file format exposes the key on first read. Mitigation: each item was worked from the stimulus + stem + options first, deriving the best-supported letter from content and history, then cross-checked against the recorded key, with deliberate attention to the defect classes (two defensible options, key/explanation contradiction, phantom references, factual error in the keyed answer). Every derivation below stands on content merits; no item was adjudicated on key-alignment alone.

## Result: 30/30 derived-vs-recorded matches. Zero repairs made. No items changed.

## Per-item verdicts

### Batch 01
- **001 (Battuta / sourcing):** Derived **B** (he judges Mali by Islamic legal/scholarly norms). Recorded B. **Match — pass.** Distractors fail cleanly (not an envoy, not writing for Europeans, not a merchant).
- **002 (Islam in Mali / argumentation):** Derived **D** (blended Islamic practice with local custom — sultan enforces prayer AND griots sing, royal women unveiled). Recorded D. **Match — pass.**
- **003 (gold / contextualization):** Derived **A** (trans-Saharan gold to North Africa/Middle East). Recorded A. **Match — pass.** B is anachronistic (Europeans by sea only in the 1400s), C swaps gold for silver, D misapplies paper money.
- **004 (Polo / sourcing):** Derived **C** (commercial scale and sophistication). Recorded C. **Match — pass.**
- **005 (Song commerce / developments):** Derived **B** (Song-era urbanization + paper money, continued under Mongols). Recorded B. **Match — pass.** Note: distractor D is worded as a counterfactual ("The supposed collapse of the Grand Canal, which would have forced…") — stylistically odd but unambiguously wrong; not a defect.
- **006 (monetization / evidence):** Derived **D** (small everyday purchases in state paper money). Recorded D. **Match — pass.** C (trade occupations) is a plausible-weaker distractor; "best supports" wording resolves it.
- **007 (trade map / comparison):** Derived **A** (both diffused religion/tech; land rested on Mongol unity, sea on independent ports). Recorded A. **Match — pass.** B is contradicted by the map's own labels (horses westbound, porcelain by sea — neither "only" claim holds); C and D are absurd/false.
- **008 (network expansion / contextualization):** Derived **C** (Mongol security on land + maritime improvements at sea). Recorded C. **Match — pass.**
- **009 (plague / developments):** Derived **B** (plague spread along the networks). Recorded B. **Match — pass.**
- **010 (Mongols / argumentation):** Derived **D** (interpretation limited — busy overland routes through Central Asia at Mongol height). Recorded D. **Match — pass.**

### Batch 02
- **011 (Mongol map / evidence):** Derived **A** (travelers crossing khanates under Mongol protection). Recorded A. **Match — pass.**
- **012 (Yuan position / contextualization):** Derived **C** (richest khanate, converging tribute/artisan flows). Recorded C. **Match — pass.** B fails on the absolute "completely" (Yuan kept Chinese-style bureaucracy).
- **013 (four khanates / developments):** Derived **B** (succession disputes + vast size). Recorded B. **Match — pass.**
- **014 (plague map / connections):** Derived **D** (same networks moved pathogens; integration exposed Eurasia). Recorded D. **Match — pass.** B reverses the dated direction; C is contradicted by sea arrival at Alexandria/Constantinople.
- **015 (plague economics / evidence):** Derived **A** (population loss → rising wages, peasant mobility). Recorded A. **Match — pass.**
- **016 (plague significance / argumentation):** Derived **C** ("Eurasian turning point" — map shows China, Central Asia, Middle East, Russia as well as Europe). Recorded C. **Match — pass.**
- **017 (paper-money edict / sourcing):** Derived **B** (state monopoly over currency, forced acceptance). Recorded B. **Match — pass.**
- **018 (money economy / evidence):** Derived **D** (bills of exchange + deposit banking alongside state paper). Recorded D. **Match — pass.**
- **019 (Kilwa / developments):** Derived **A** (middleman: Asian cloth/porcelain for interior gold). Recorded A. **Match — pass.**
- **020 (Kilwa Islamization / contextualization):** Derived **C** (merchant/Sufi contact, not conquest). Recorded C. **Match — pass.**

### Batch 03
- **021 (monsoons / connections):** Derived **B** (seasonal sailing; ports filled waiting for the winds). Recorded B. **Match — pass.**
- **022 (monsoon reliability / evidence):** Derived **D** (lateen-rigged dhows, entrepôt ports on sailing schedules). Recorded D. **Match — pass.**
- **023 (Florentine handbook / sourcing):** Derived **A** (practical guidance for European merchants under Mongol protection — Pegolotti's Tana-to-Cathay road). Recorded A. **Match — pass.**
- **024 (Mali taxation / argumentation):** Derived **C** (trade-route taxes funded states, armies, cities). Recorded C. **Match — pass.**
- **025 (champa rice / evidence):** Derived **B** (double-cropping + doubled household registers). Recorded B. **Match — pass.** D is the "before" picture, not evidence of transformation; "best supports" resolves it.
- **026 (gunpowder / developments):** Derived **D** (Mongol conquests carried Chinese military knowledge west; local adaptation). Recorded D. **Match — pass.** C fails on "solely."
- **027 (Samudera Islam / contextualization):** Derived **A** (trade-route diffusion via merchants/Sufis, not armies). Recorded A. **Match — pass.**
- **028 (Venice & Kilwa / comparison):** Derived **C** (both thrived as middlemen, ships and credit fitted to their seas). Recorded C. **Match — pass.**
- **029 (plague aftermath / argumentation):** Derived **B** (workers gained bargaining power in some places; treasuries drained in others). Recorded B. **Match — pass.** A fails on "every region"; D mistakes debasement for sound recovery.
- **030 (Catalan Atlas / sourcing):** Derived **D** (Europeans learned of West African wealth via trans-Saharan reports; secondhand portrayal of Mansa Musa). Recorded D. **Match — pass.**

## Cross-cutting checks (all 30)
- **Structure:** every item has exactly 4 options; recorded keys are A–D only; `option_explanations` covers A–D on every item; no duplicate IDs; all required schema fields present. Verified programmatically.
- **No double-defensible options:** all distractors fail on absolutes ("only," "every," "completely," "solely"), anachronisms (European sea routes in the 1300s, joint-stock companies, universities), reversed causation, or direct contradiction with the stimulus. The two "best supports" items with near-miss distractors (006 C, 025 D) are resolved by the superlative wording and are clean.
- **Key/explanation agreement:** every `explanation` and every `option_explanations` entry supports the recorded key; no contradictions found.
- **Phantom references:** none. Map stimuli are fully described in text (routes, labels, dates); no item asks about an undescribed visual detail. (`visual_needs_url: true` is a production asset flag, not a content gap.)
- **Factual soundness of keyed answers:** spot-checked against the historical record — Battuta in Mali c. 1352; trans-Saharan gold; Song/Yuan paper money and Grand Canal continuity; Pax Mongolica and the four khanates; plague chronology and labor-market effects; monsoon sailing rhythm; Pegolotti's handbook; champa rice double-cropping; Mongol-borne gunpowder diffusion; trade-borne Islam on the Swahili coast and in Sumatra; Catalan Atlas 1375 depicting Mansa Musa (d. c. 1337) from secondhand reports. All keyed answers are historically correct.

## Changelog
No repairs were required. The three JSON files were **not modified** — IDs, keys, stems, options, explanations, and tags are exactly as written.

## Follow-ups (none blocking)
- Consider storing keys in a separate file (e.g., `ANSWER_KEYS.md` or `keys.json`) in future waves so the blind-audit protocol can be executed literally — inline keys make true blindness impossible on first read.
- Distractor D in item 005 ("The supposed collapse of the Grand Canal…") is oddly phrased for a counterfactual; not wrong, just stylistically out of step with the other distractors.
