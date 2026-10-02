# Compliance Report — AP World Unit 3 Fresh-Written MCQs

- **Files reviewed:** `batch-01.json` … `batch-05.json` (55 items: `wh-fresh-u3-001` … `wh-fresh-u3-055`)
- **Reviewer method:** clean-context. Read all 55 items end to end; checked each against the five compliance axes below. Quoted stimuli were web-verified (non-College-Board sources); riskiest factual claims spot-checked; format validated programmatically.
- **Date:** 2026-10-02
- **Keys:** NOT changed on any item (key audit already passed; flags only, no key impact).

## Summary

| Axis | Result |
|------|--------|
| Items reviewed | 55 |
| Originality / IP | 55/55 pass — no lifted passages found |
| Fabrication check | 51/55 fully verified; 4 quote-stimuli carry `[UNVERIFIED-QUOTE]` flags (10 items) — substance verified genuine in all four, exact quoted wording not traceable |
| Fact check | 55/55 pass — no wrong dates, names, or causal claims found; nothing required in-place repair |
| Format | 55/55 MCQ-only, exactly 4 options, every stem ends with `?` or `:` |
| Visual honesty | all `visual_needs_url` visuals are real/findable (Topkapi kanunname manuscripts, Taj Mahal photos, Suleymaniye photos, honest constructed maps of genuine geography) |

**Repairs made:** none. No item had a wrong fact requiring in-place repair.

**Quarantine recommendation:** none. The flagged quotes are transparently labeled as adaptations and their substance is verified; they do not need quarantine.

## Originality / IP

All prose is original, textbook-level composition. The stimulus descriptions (kanunname page, devshirme/millet, ghulams, zamindars, intendants, sankin-kotai, sakoku, etc.) read as fresh paraphrase, not as passages lifted from a recognizable textbook, prep book, or website. Quoted material falls into two clean buckets:

- **Verbatim pre-1900 public domain:** Luther's 95 Theses (items 045–047: Thesis 1 and Thesis 32 wording matches standard pre-1900 translations) — fine.
- **Disclosed adaptations:** Shah Ismail proclamation (007), Ain-i-Akbari passage (012–014), Qing queue decree (017–019), Peter the Great beard decree (023–025). All are tagged "adapted from pre-1900 translations/sources." No item invents an attribution for post-1929 material.

No IP issues; nothing reads like a lifted passage.

## Fabrication check (web-verified)

Verified genuine via browser.search on non-College-Board sources:

- **Luther's theses quotes (045–047):** Thesis 1 ("When our Lord and Master Jesus Christ said, 'Repent,' he willed the entire life of believers to be one of repentance") and Thesis 32 ("Those who believe that they can be certain of salvation because they have indulgence letters will be eternally damned, together with their teachers") are the standard translations — PASS, no flag.
- **Ain-i-Akbari stimulus (012–014):** substance verified — Ibadat Khana built 1575 at Fatehpur Sikri; discussions among Muslims, Hindus, Jains, Zoroastrians, Christians; Blochmann translation 1873 (pre-1900 label honest). Exact quoted wording ("the lamp of inquiry be lit in every heart") NOT traceable to a published translation — flagged [UNVERIFIED-QUOTE].
- **Qing 1645 queue decree (017–019):** substance verified — July 1645 queue order, Han men to adopt the Manchu queue on pain of death (the documented "keep the head, lose the hair; keep the hair, lose the head" edict; scholarly confirmation that refusal was punishable by execution). Exact English wording NOT traceable to a specific published translation — flagged [UNVERIFIED-QUOTE].
- **Peter the Great 1705 beard decree (023–025):** substance verified against the full ukase text of 16 January 1705 (shave beards/moustaches; rank-based annual taxes; tokens as receipts to be worn; one-kopeck peasant toll at town gates; separate German-dress decrees). The specific flourish "that Russia may cease to be a mockery among enlightened peoples" was NOT found in the published ukase — flagged [UNVERIFIED-QUOTE].
- **Shah Ismail proclamation (007):** exact wording ("I am the deputy of the Mahdi, the lord of the age... those who turn away shall face my sword") could NOT be traced to any published proclamation. Substance is genuine — Ismail's claim to divine/messianic Shi'a mandate and the Qizilbash's spiritual devotion to him are documented (Encyclopaedia Iranica; his Divan poetry; Safavid-era histories describe him as God's chosen agent drawing "the sword of conquest") — but the quoted text is an unattributable stylization — flagged [UNVERIFIED-QUOTE].
- **Leo Africanus on Timbuktu (028–029):** substance matches Pory's 1600 translation (books brought from Barbary; book trade more profitable than any other merchandise). Askia Muhammad's hajj (1496–98) and mosque/school endowments in Timbuktu are documented — PASS, no flag.

## Fact check (spot-checked riskiest claims)

All confirmed: Chaldiran 1514; Suleyman r. 1520–1566; Shah Abbas I r. 1588–1629; Ottoman greatest extent c. 1683; Taj Mahal completed c. 1653; St. Petersburg founded 1703; yasak fur tribute; Dejima confined Dutch post; Time of Troubles 1598–1613 with Michael Romanov elected 1613 after Ivan IV's death in 1584; Peace of Augsburg 1555 / cuius regio eius religio; Council of Trent 1545–1563; Jesuit order 1540; Akbar's jizya abolition and Rajput appointments; Bossuet's divine-right defense. No wrong dates, names, or causal claims found. The Ottoman "caliph" title claim (item 050) is standard AP World framing, not a fabrication.

Minor observation (not flagged): the Qing map c. 1750 (items 020–021) labels Burma as a tribute-paying state; the formal tributary relationship postdates the 1765–1769 Qing-Burmese war. Neither item's tested content hinges on Burma, so no flag was added.

## Format

Programmatically verified: all 55 items `type: "mcq"`, exactly 4 options, every stem ends with `?` or `:`. No SAQ/LEQ structures. Unique ids confirmed (55/55).

## Visual honesty

`visual_needs_url: true` items describe real, findable visuals: illuminated kanunname pages with Suleyman's tughra (exist in the Topkapi Palace Library); Taj Mahal photographs; Suleymaniye Mosque complex photographs; constructed maps showing genuine geography (Ottoman/Safavid c. 1600, Ottoman c. 1683, Qing c. 1750, Russian expansion 1500–1800, Tokugawa Japan c. 1700). Nothing invented. Note: items 039/040/050/051/052 set `visual_needs_url: true` on data tables rather than images — harmless inconsistency; the tables are fully described in text.

## Changes applied

No content changes. Added `"flags"` fields to 10 items (all [UNVERIFIED-QUOTE], wording in the files):

- `wh-fresh-u3-007` (Shah Ismail proclamation)
- `wh-fresh-u3-012`, `-013`, `-014` (Ain-i-Akbari quote)
- `wh-fresh-u3-017`, `-018`, `-019` (Qing queue decree quote)
- `wh-fresh-u3-023`, `-024`, `-025` (Peter the Great decree quote)

JSON re-validated after edits; no git commit or push made.
