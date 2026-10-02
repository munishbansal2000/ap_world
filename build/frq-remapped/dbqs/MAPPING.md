# DBQ Remap — Source Mapping (Fall 2026 CED)

All 10 DBQs are re-conceived for the new format: 7 documents each, prompt opens
"Using the documents and your knowledge of world history, ...". Topics below were
used as inspiration only; every document is freshly selected and worded, and no
remapped DBQ retains a source book's document set or prompt design.

File schema maps to the Barron's new-format DBQ pattern (see
`build/format-reference-barrons-tests.md`, format patterns only):
- `documents[].n` → "Document N" header
- `documents[].source_line` → "Source:" line
- `documents[].text_or_description` → excerpt / image description

| File | Topic / Era | Reasoning | Inspiration |
|---|---|---|---|
| dbq-01.json | The Mongols and Eurasian Exchange, c. 1200-1400 (Units 1/2) | comparison | fresh |
| dbq-02.json | The Indian Ocean Trading World, c. 1200-1500 (Units 1/2) | continuity/change | fresh |
| dbq-03.json | Aztec and Inca Methods of Rule, c. 1300-1500 (Unit 1) | comparison | fresh |
| dbq-04.json | The Columbian Exchange, c. 1450-1700 (Unit 4) | causation | loosely inspired by barrons-dbq-t1 (encounters topic) |
| dbq-05.json | Legitimizing the Gunpowder Empires, c. 1500-1700 (Unit 3) | comparison | fresh |
| dbq-06.json | Industrialization and British Workers, c. 1750-1900 (Units 5/6) | continuity/change | fresh |
| dbq-07.json | Decolonization and International Relations, c. 1945-1965 (Unit 8) | continuity/change | inspired by princeton-pt1-dbq (decolonization & diplomacy) |
| dbq-08.json | Women and Industrialization, c. 1750-1900 (Units 5/6) | continuity/change | inspired by princeton-pdf4-dbq (barriers women faced) |
| dbq-09.json | Politics and the Olympic Games, 1896-2000 (Units 7/8/9) | causation | inspired by fivesteps-frq-033 (politics & Olympics) |
| dbq-10.json | Hydroelectric Dams in the Twentieth Century (Unit 9) | causation | inspired by barrons-dbq-t2 (hydroelectric dams) |

Coverage: 3 substantially pre-1450 topics (01, 02, 03); units 1-9 represented;
reasoning processes: comparison x3, causation x3, continuity/change x4.

## Image-license verification notes

All non-text documents carry a `license` field stating what was verified.
Fully verified (PD or CC, license visible on the file page or evident from date):
Mongol_Empire_map.gif (CC BY-SA 3.0), YuanEmperorAlbumGenghisPortrait.jpg (PD),
Wu_bei_zhi_LOC_2004633695-17.tif (PD), Quipu.png (PD), Casta_painting_all.jpg
(PD, 18th c.), Triangle_trade2.png (CC BY-SA 3.0), AbulFazlPresentingAkbarnama.jpg
(PD), Islamic_Gunpowder_Empires.jpg (CC BY-SA 4.0), Powerloom_weaving_in_1835.jpg
(PD), British_Decolonisation_in_Africa.png (PD), United_Nations_Member_States-1945.png
(PD), Blanchisseuses_1865.jpg (PD), Luz_Long_and_Jesse_Owens.png (CC0),
Bundesarchiv_Bild_183-R96374 (CC BY-SA 3.0), Hoover_dam_from_air.jpg (PD),
TVA water-control diagram (PD).

Caveats (flagged in final report):
- Aztec_Empire_ME orthographic svg / Inca_Empire_South_America svg: Commons file
  pages show a free-license template, but the specific license names did not render
  in the text fetch. Treat as unverified-license until confirmed in a browser.
- Three non-text slots use original charts/timelines created for this assessment
  (dbq-02 doc 7, dbq-06 doc 7, dbq-08 doc 7): no external URL, marked
  `"original_work": true`. No copyright concern.
- Could not verify on Commons (not used; listed for the record): a Codex Mendoza
  folio image, a monsoon-winds map, a Chartist-meeting photograph, pit-brow-women
  photographs, and the license of the "Voyages of Zheng He" map.
