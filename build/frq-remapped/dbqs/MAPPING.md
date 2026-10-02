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
| dbq-04.json | The Columbian Exchange, c. 1450-1750 (Unit 4) | causation | loosely inspired by barrons-dbq-t1 (encounters topic) |
| dbq-05.json | Legitimizing the Gunpowder Empires, c. 1500-1700 (Unit 3) | comparison | fresh |
| dbq-06.json | Industrialization and British Workers, c. 1750-1900 (Units 5/6) | continuity/change | fresh |
| dbq-07.json | Decolonization and International Relations, c. 1945-1965 (Unit 8) | continuity/change | inspired by princeton-pt1-dbq (decolonization & diplomacy) |
| dbq-08.json | Women and Industrialization, c. 1750-1900 (Units 5/6) | continuity/change | inspired by princeton-pdf4-dbq (barriers women faced) |
| dbq-09.json | Politics and the Olympic Games, 1896-2000 (Units 7/8/9) | causation | inspired by fivesteps-frq-033 (politics & Olympics) |
| dbq-10.json | Hydroelectric Dams in the Twentieth Century (Unit 9) | causation | inspired by barrons-dbq-t2 (hydroelectric dams) |

Coverage: 3 substantially pre-1450 topics (01, 02, 03); units 1-9 represented;
reasoning processes: comparison x3, causation x3, continuity/change x4.

## Image-license verification notes

All non-text documents carry `image_url` (direct `upload.wikimedia.org` file URL, per
APUSH convention) plus `source_page` (the Commons/Wikipedia file page for license
inspection). License states below reflect the blind audit of 2026-10-02.

Re-verified during blind audit (file page opened, license confirmed):
Mongol_Empire_map.gif (CC BY-SA 3.0 — note: ANIMATED map of expansion 1206-1294,
description corrected accordingly), YuanEmperorAlbumGenghisPortrait.jpg (PD,
14th-c. album leaf, National Palace Museum Taipei), Quipu.png (PD, 1888 Meyers
Konversationslexikon), AbulFazlPresentingAkbarnama.jpg (PD-art, Govardhan
c. 1603-1605, Chester Beatty Library), Powerloom_weaving_in_1835.jpg (PD, 1835
Baines engraving by T. Allom/J. Tingle),
Bundesarchiv_Bild_183-R96374 (CC BY-SA 3.0, German Federal Archives).

Replaced during blind audit:
- dbq-04 doc 5: the anonymous "Ming official memorial on the Single Whip" had no
  identifiable source — replaced with Antonio de Morga, Sucesos de las Islas
  Filipinas (1609), on Chinese junks at Manila carrying American silver back to
  China. Genuine PD primary source.
- dbq-08 doc 2: the anonymous "mill worker testimony" had no identifiable source —
  replaced with Betty Harris's recorded testimony to the Children's Employment
  Commission (1842), Knowles Pit, Little Bolton. Genuine; pairs with Doc 4's report.
- dbq-09 doc 6: Luz_Long_and_Jesse_Owens.png REMOVED — its CC0 claim was
  uploader-declared on a YouTube-sourced still of unknown provenance (not a press
  photo; no wiki usage). Replaced with a paraphrased text doc: Jesse Owens's own
  recollection of Luz Long's sportsmanship in the 1936 long jump. Zero IP risk.

Carried over from the remap author's verification (not re-opened in blind audit —
text-fetch proxy returned 403 on later file-page requests, so these need a render
check in the app before shipping):
Wu_bei_zhi_LOC_2004633695-17.tif (PD, 1621 — served via the standard 800px
MediaWiki thumbnail .jpg since browsers cannot render TIFF; thumbnail URL
[UNVERIFIED], confirm render), Casta_painting_all.jpg (PD, 18th c.),
Triangle_trade2.png (CC BY-SA 3.0), Islamic_Gunpowder_Empires.jpg (CC BY-SA 4.0),
British_Decolonisation_in_Africa.png (PD, released by author),
United_Nations_Member_States-1945.png (PD), Blanchisseuses_1865.jpg (PD),
Hoover_dam_from_air.jpg (PD, U.S. federal work), TVA water-control diagram (PD,
U.S. federal work; copyright not renewed).

Caveats (flagged in final report):
- Aztec_Empire_ME orthographic svg / Inca_Empire_South_America svg: Commons file
  pages show a free-license template, but the specific license names did not render
  in the text fetch. License fields carry [UNVERIFIED]. The Inca map description
  was trimmed to what the map shows (four suyus); the "road network" claim was
  removed.
- dbq-04 prompt period extended c. 1450-1700 -> c. 1450-1750: the 18th-century
  casta painting postdated the old range.
- Theme codes fixed: MIG/SOC (retired pre-2019 CED codes) -> SIO; "SIO - States
  and Other Institutions of Power" (APUSH label) -> "SIO - Social Interactions and
  Organization"; "ENV - Humans and the Environments" typo -> "ENV - Humans and the
  Environment".
- Three non-text slots use original charts/timelines created for this assessment
  (dbq-02 doc 7, dbq-06 doc 7, dbq-08 doc 7): no external URL, marked
  `"original_work": true`. No copyright concern.
- Could not verify on Commons (not used; listed for the record): a Codex Mendoza
  folio image, a monsoon-winds map, a Chartist-meeting photograph, pit-brow-women
  photographs, and the license of the "Voyages of Zheng He" map.
