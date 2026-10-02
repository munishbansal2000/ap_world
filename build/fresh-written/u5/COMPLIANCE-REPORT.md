# Compliance Review — AP World Unit 5 Fresh-Written MCQs

- **Date:** 2026-10-02 (PDT)
- **Reviewer:** clean-context subagent
- **Files reviewed:** `~/workspace/ap_world/build/fresh-written/u5/batch-01.json` through `batch-06.json`
- **Items reviewed:** 61 (`wh-fresh-u5-001` … `wh-fresh-u5-061`)
- **Commit/push:** not performed, per instructions

## Verdict

**PASS with repairs.** No items quarantined. No keys changed (key audit already passed 61/61 — all repairs are stimulus/attribution text only, no stem, option, or key edits). No `[UNVERIFIED]` flags were needed: every check below either confirmed the fact/quote or was repaired in place.

## Format check (programmatic)

All 61 items: type `mcq`, exactly 4 options labeled (A)–(D), stems end with `?` or `:`, keys are A/B/C/D. **0 issues.**

## Repairs made (10 items, stimulus text only)

1. **`wh-fresh-u5-004`, `wh-fresh-u5-005`** (batch-01) — The Jamaica Letter stimulus is a loose paraphrase of Bolívar's 1815 letter, not a verbatim translation. Verified the substance against published translations (Bertrand: "neither Indians nor Europeans, but a species midway between the legitimate proprietors of this country and the Spanish usurpers"; "though Americans by birth we derive our rights from Europe, and we have to assert these rights against the rights of the natives, and at the same time we must defend ourselves against the invaders"). Repair: attribution now reads "— Simón Bolívar, Jamaica Letter, 1815 **(paraphrased)**". Key unchanged.
2. **`wh-fresh-u5-008`, `wh-fresh-u5-009`** (batch-01) — The Wollstonecraft "quote" is a paraphrase: the genuine phrases "women in particular, are rendered weak and wretched" and "a false system of education" are real (Vindication, Introduction), but the item's combined sentences are not verbatim. Repair: attribution now reads "— Mary Wollstonecraft, A Vindication of the Rights of Woman, 1792 **(paraphrased from the Introduction)**". Key unchanged.
3. **`wh-fresh-u5-015`, `wh-fresh-u5-016`** (batch-02) — Haitian Constitution (1805) quotes verified genuine against the standard English translation (Art. 12: "No white man of whatever nation he may be, shall put his foot on this territory with the title of master or proprietor, neither shall he in future acquire any property therein."; Art. 14: "The Haytians shall hence forward be known only by the generic appellation of Blacks."). Repair: fixed typo "whiteman" → "white man" to match the genuine text. Key unchanged.
4. **`wh-fresh-u5-019`, `wh-fresh-u5-020`** (batch-02) — Visual-honesty fix. The described engraving did not match the real, findable print: the famous c. 1802 Paris print (Chez Jean; V&A collection) shows Toussaint **mounted on a rearing horse with sword aloft**, captioned "Toussaint Louverture, Chef des Noirs Insurgés de Saint Domingue" — not "seated with his hand resting on his sword." Repair: stimulus description rewritten to match the real image (Chez Jean, Paris, 1802; horseback, sword raised; full caption). Key unchanged; the item's argument (enslaved-born man as French general) is unaffected.
5. **`wh-fresh-u5-035`, `wh-fresh-u5-036`** (batch-04) — **Fabricated-style quote removed.** Stimulus A presented a verbatim quote ("The African slave trade is a crime against humanity. Let Parliament wash its hands of this bloodstained commerce.") attributed to a generic "British abolitionist pamphlet, 1807". Web search found no such pamphlet; "crime against humanity" is anachronistic for 1807 abolitionist rhetoric. This was a composed pastiche presented as a primary source. Repair: replaced with an explicitly labeled summary — "British abolitionist arguments, c. 1807 (summary): abolitionists condemned the African slave trade as morally indefensible and urged Parliament to abolish it outright." Keys unchanged (035=B, 036=A); the items' logic (abolitionist campaigning as evidence) is unaffected. Note the paired stimulus B already self-labels as "paraphrased from rebel statements" and its substance (Baptist War rebels believing the King had granted freedom) is documented — left as-is.

## Quote authenticity (verified genuine, no repair)

- **Declaration of the Rights of Man and of the Citizen (1789), Arts. 1/3/6** (001–003): standard translation, PD. ✓
- **Jamaica Letter, 1815** (004–005): substance genuine; marked paraphrased (see repairs). ✓
- **Wollstonecraft (1792)** (008–009): genuine phrases, paraphrase structure; marked paraphrased (see repairs). ✓
- **de Gouges (1791)** (013–014): verified verbatim — "Woman, wake up; the tocsin of reason is being heard throughout the whole universe; discover your rights"; "Woman is born free and remains equal to man in rights"; Art. VI "all female and male citizens must contribute personally or through their representatives". PD. ✓
- **Haitian Constitution (1805), Arts. 12/14** (015–016): verified verbatim (see repairs for typo). PD. ✓
- **Declaration of Sentiments (1848)** (025–026): verified verbatim ("all men and women are created equal"; "history of repeated injuries and usurpations… establishment of an absolute tyranny over her"). PD. ✓
- **Locke, Second Treatise (1689)** (023–024): §95 genuine. PD. ✓
- **Montesquieu, Spirit of the Laws (1748)** (023–024): Book XI ch. 6 genuine. PD. ✓
- **Rousseau, Social Contract (1762)** (059): "Man is born free, and everywhere he is in chains" + general-will passage genuine. PD. ✓
- **Bismarck "blood and iron" (1862)** (057): genuine quote substance (Eisen und Blut; speeches/majority-votes rendering standard). ✓
- **Bolívar "We have plowed the sea"** (030): genuine, item hedges with "reportedly". ✓
- **Napoleonic Code Art. 213** (043–044): "The husband owes protection to his wife; the wife owes obedience to her husband" — genuine translation. PD. ✓
- **Declaration of Independence** (015–016, 053–054): genuine. PD. ✓
- Items 017, 030, 047, 049, 053(B), 055, 056, 060 use unlabeled summaries or honest "paraphrased"/"in effect"/"reportedly" markers — no false-verbatim claims. ✓

## Fact spot-checks (riskiest claims, non-CB web sources)

All confirmed: White Lotus 1796–1804; Toussaint captured 1802, died in French prison 1803; Haiti 2nd independent nation in the Americas, 1st Black republic; Britain's 1802–03 Leclerc expedition defeated; Watt's separate-condenser patent 1769; Louisiana Purchase $15M (1803); Gran Colombia dissolution by 1830; British 1833 act — apprenticeship to 1838, £20M enslaver compensation, children under 6 freed immediately; Sadler Committee 1832 (children as young as ~8, 12–14-hr days); Gülhane Edict 1839; Baptist War 1831; Naples (1821)/Spain (1823) Congress-System interventions; Congress of Vienna 1814–15; German unification wars 1864–71; Seneca Falls 1848 with abolitionist-network organizers; New Jersey women's suffrage revoked 1807; Monroe Doctrine 1823; Isabey engraving (1819, after 1815 painting) — see below.

## Visual honesty (`visual_needs_url` items)

- **010** — "Congress of Vienna (engraving, 1819, after Jean-Baptiste Isabey)": **real and findable** (etching 1819, after Isabey's 1815 painting; confirmed via Nelson-Atkins/Bridgeman records). Description matches. ✓
- **019/020** — Toussaint engraving: description did not match the real print; **repaired** (see above). ✓
- **031/032** — 1789 Third Estate print ("carrying the clergy and nobility"): **real** (famous 1789 cartoon; Musée Carnavalet copies). Description matches. ✓
- **033/034** — Louis XVI execution engraving: generic-but-real class of contemporary engravings; description plausible. ✓
- **006/007, 011/012, 021/022, 027, 029, 037, 039/040, 041/042, 045/046, 051/052, 061** — descriptive map/timeline/chart/engraving briefs (not claimed as named works); all describe standard, sourceable visual types with accurate data. **Note for the URL-sourcing step:** the 037 bar-chart numbers are approximations ("about 23 million / 4 million / 800,000 / 700,000") and should stay "about" in the caption if a real chart is sourced or one is built.
- **045** note: item text says "Holy Alliance powers discussed helping Spain recover its colonies" — accurate (Troppau Protocol debates, 1820–21). ✓

## Originality / IP

These are fresh-written items, not book-derived. Stimuli are famous PD primary sources (all pre-1900) with standard translations, or original summaries; option sets are original expression. No stimulus reads as lifted from a recognizable textbook/prep book/website. The de Gouges/Wollstonecraft/Locke/Montesquieu translations are widely used standard renderings of PD texts — not copyright-bearing expression. The removed 1807 pamphlet pastiche was the only invented-attribution risk and was repaired.

## [UNVERIFIED] flags added

**None.** Every spot-checked claim was confirmable, and the one unverifiable quote (035/036 stimulus A) was repaired to an explicitly labeled summary rather than flagged.

## Quarantine recommendation

**None.** No item needs removal. The most sensitive historical claim in the bank — 055's "defeated the armies of France, Britain, and Spain" — is supported by standard histories (Britain's 1793–98 expedition withdrawn in defeat; Spain ceded Santo Domingo in 1795; Napoleon's 1802–03 expedition destroyed).

## What changed on disk

- `batch-01.json`: 004, 005, 008, 009 — attribution labels (+ stimulus_words updated: 76, 76, 68, 68)
- `batch-02.json`: 015, 016 — "whiteman" → "white man" (85, 85); 019, 020 — engraving description (57, 57)
- `batch-04.json`: 035, 036 — pamphlet quote → summary (56, 56)
- Keys, stems, options, explanations untouched. All files still parse as valid JSON. No commit/push.
