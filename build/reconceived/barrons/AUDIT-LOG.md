# Blind Answer-Key Audit — Barron's reconceived set

- Date: 2026-10-02
- Auditor protocol: strict blind. For each of 160 items read ONLY stimulus/stem/options,
  derived the answer from AP World knowledge, wrote it down, THEN compared with the
  recorded `key`. Keys, explanations, and option_explanations were read only for the
  7 mismatches.
- Result: 160 audited, 153 blind derivations matched the recorded key, 7 mismatches,
  7 repairs, 0 quarantines, 0 auditor-errors (see below).
- Repair policy applied: never flip the key. For each mismatch the correct option was
  ROTATED to the recorded key's position (option texts reordered, embedded letter
  prefixes rewritten, option_explanations remapped to follow their texts). Key letters
  unchanged, so key-position balance is untouched (A/B/C/D = 40/40/40/40 before and
  after). All 7 were re-derived blind AFTER repair — all now match their recorded keys.
- Post-audit corpus check: all 160 items have 4 options with correct positional
  prefixes, option_explanations for A–D, exactly one "Correct" marker per item, and
  that marker agrees with the recorded key. 0 problems.

## Matches (153) — blind derivation = recorded key

- practice-test-1-a-mcq.json (matches): wh-barrons-u9-007(C), -008(B), -009(D), -011(C),
  -012(D), -013(C), -014(B), -015(B)
- practice-test-1-b-mcq.json (matches): wh-barrons-u4-004(B), -005(B), -006(B), -003-010(C),
  -006-014(B), -015(A), -016(C), -017(B), -018(B), -019(C), -020(D), -021(D), -022(A),
  -023(D), -024(C), -025(A), -026(B), -007(C), -008(A)
- practice-test-2-a-mcq.json (matches): wh-barrons-u6-027(C), -028(D), -029(D), -007-003(D),
  -004(A), -005(C), -006(D), -007(D), -008(B), -009(C), -008-004(A), -005(D), -006(A)
- practice-test-2-b-mcq.json (matches): wh-barrons-u2-003(D), -004(B), -005(B), -006-030(C),
  -004-007(B), -006-031(C), -004-008(C), -001-022(C), -023(D), -024(C), -025(C)
- sec1-mcq.json (matches): wh-barrons-u1-001(D), -004(D), -005(A), -007(C), -009(A),
  -010(B), -028(C), -029(C), -030(C), -031(D), -003-007(C), -008(B), -009(D), -004-001(C),
  -002(A), -003(A), -003-001(B), -002(C), -003(C), -004(B), -005(B), -006(A)
- sec2-mcq.json (matches): wh-barrons-u5-004(A), -005(D), -006(B), -008-007(D), -009-016(A),
  -017(B), -018(D), -019(A), -020(A), -004(D), -005(A), -006(A), -007(D), -008(B), -009(D),
  -010(A), -011(A), -012(C), -008-008(C), -009(D), -010(D), -004-011(B), -012(D), -013(C),
  -005-013(C), -014(B), -015(C)
- sec3-mcq.json (matches): wh-barrons-u6-001(B), -002(A), -003(B), -004(D), -005(B), -006(A),
  -007(B), -008(B), -009(D), -010(C), -011(D), -012(B), -013(A), -032(B), -033(A), -034(A),
  -009-001(B), -002(B), -003(B), -004(C), -005(D), -006(A), -008-001(A), -002(D), -003(A)
- sec4-mcq.json (matches): wh-barrons-u1-012(A), -013(C), -014(B), -015(D), -016(C), -017(A),
  -018(C), -019(A), -020(D), -021(B)

## Mismatches (7) — all repaired, none quarantined

Common pattern in all 7: the item was sound (unambiguous stem, single correct answer) and
the recorded explanation/option_explanations already identified the blind-derived answer
as "Correct" — only the `key` field (and hence the correct option's position) disagreed.
Repair: rotated the correct option to the recorded key position (option texts, letter
prefixes, and option_explanations remapped; key letters preserved). Re-derived blind
after repair — all 7 now match.

1. wh-barrons-u9-010 (practice-test-1-a-mcq.json). NOT-supported-by-HIV/AIDS-chart item.
   Blind: B (chart cannot prove the virus originated in Africa). Recorded key: D, with
   explanation and option_explanations marking B "Correct". Repair: correct option moved
   B→D; explanation's letter refs updated ("Conclusions A, B, and C stay within...; D
   leaps beyond it"). Post-repair blind re-derivation: D = recorded key. ✓
2. wh-barrons-u1-002 (sec1-mcq.json). Arab chronicler of Mongol invasions; stem asks how a
   historian of the later-1200s trade revival should treat the passage. Blind: A
   (vivid evidence of conquest-era violence, limited guide to later merchant policy).
   Recorded key: D, explanations mark A "Correct". Repair: correct option moved A→D.
   Post-repair blind re-derivation: D = recorded key. ✓
3. wh-barrons-u2-001 (sec1-mcq.json). Mongol relocation of skilled specialists. Blind: B
   (gathering skilled workers for administration/crafts/weaponry). Recorded key: A,
   explanations mark B "Correct". Repair: correct option moved B→A. Post-repair blind
   re-derivation: A = recorded key. ✓
4. wh-barrons-u1-003 (sec1-mcq.json). Longer-term outcome for former Abbasid lands. Blind: D
   (Ilkhanid conversion to Islam, patronage). Recorded key: C, explanations mark D
   "Correct". Repair: correct option moved D→C. Post-repair blind re-derivation: C =
   recorded key. ✓
5. wh-barrons-u1-006 (sec1-mcq.json). Christine de Pizan's career as professional writer.
   Blind: C (literate court culture and aristocratic patronage — she died ~1430, before
   Gutenberg, so the printing-press option is anachronistic). Recorded key: B,
   explanations mark C "Correct". Repair: correct option moved C→B. Post-repair blind
   re-derivation: B = recorded key. ✓
6. wh-barrons-u1-008 (sec1-mcq.json). De Pizan's controversy. Blind: D (querelle des
   femmes, named verbatim in the stimulus). Recorded key: C, explanations mark D
   "Correct". Repair: correct option moved D→C. Post-repair blind re-derivation: C =
   recorded key. ✓
7. wh-barrons-u1-011 (sec1-mcq.json). Spanish adaptation of the Inca mit'a. Blind: C
   (adapted into forced labor drafts for Potosí silver mines). Recorded key: B,
   explanations mark C "Correct". Repair: correct option moved C→B. Post-repair blind
   re-derivation: B = recorded key. ✓
