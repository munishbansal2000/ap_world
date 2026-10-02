# AP World History: Modern — Content Plan

**Exam:** Thursday, May 6, 2027, 8:00 AM local (Session 1). Fully digital, Bluebook.
**Governing framework:** CED Effective Fall 2026 (verified live 2026-10-02; see `build/phase0-ced-research.md`).
**Repo:** munishbansal2000/ap_world, `main` only.

## Exam blueprint (Fall 2026 CED)

| Section | Format | Time | Weight |
|---|---|---|---|
| I-A: MCQ | 55 questions, stimulus sets of 2–5 | 55 min | 40% |
| I-B: SAQ | 3 required (Q1 secondary text, Q2 primary text, Q3 non-text) | 40 min | 20% |
| II-A: DBQ | 7 documents, topic range **1200–2001** | 60 min (incl. 15-min read) | 25% |
| II-B: LEQ | single prompt, student chooses reasoning | 40 min | 15% |

Total 3h15m. Rubrics: DBQ 7 / LEQ 6 / SAQ 3 each. No SAQ choice, no LEQ choice — old-format structures must not appear even in directions text.

## Framework

9 units (1200–present), 6 themes (ENV, CDI, GOV, ECN, SIO, TEC), 6 skills + 3 reasoning processes (comparison, causation, continuity/change). Unit weights: U1/U2/U7/U8/U9 at 8–10%, U3/U4/U5/U6 at 12–15%.

2025 Chief Reader bleed (old format, directionally valid): explanation SAQ parts (B/C ~0.5/1), DBQ complexity/analysis points. Our difficulty rubric must target these.

## Content targets

- **~900 MCQs** across the bank, unit-weighted to exam weights, stimulus-based
- **~60 SAQ sets** (3 required questions each, mandated source-type rotation)
- **8–10 DBQs** (7 docs each, topics spanning 1200–2001, pre-1900 sources PD-quotable)
- **20 LEQs** (single-prompt format, all 3 reasoning processes)
- **10 full practice tests** (55 MCQ + 3 SAQ + DBQ + LEQ, blueprint-faithful)
- **9 unit reviews** (concise, exam-weighted)
- Annotated exemplar essays at 3 score points for test DBQs/LEQs; rubric maps; full plain-language explanations for every MCQ option (no "trap/distractor" jargon — standing rule)

## Build pipeline (same gates as APUSH)

1. **Reclaim** — extract questions from his 3 books into staged files, tagged by book/unit; duplicates skipped, never merged raw.
2. **Re-conceive** — every item rewritten: new angles, fresh distractor sets, our explanations. No bank item may retain a book's question design. (Standing IP law: facts aren't copyrightable; selection/arrangement/wording must be ours. Zero copyright tolerance.)
3. **Blind key audit** — separate agent pass, never folded into repair; keys balanced, length-tell 0%.
4. **Test assembly** — blueprint quotas per test; visual stimuli ~40%, every image a verified PD/CC URL (the t4 lesson: never ship a described-but-unverified image).
5. **Prod-readiness review** — clean-context reviewers read everything; ship with 0 blockers.

## Standing rules (inherited)

- Work on main, no branches; name the repo on every push report.
- New CED format only. Pre-Fall-2026 books teach the old format — strategy content remapped or quarantined.
- Pre-1900 primary sources are public domain (quotable verbatim — ideal for DBQ docs); post-1929 sources get paraphrase/original treatment.
- "Let's go" = build the whole chain, no clarifying questions. Repair-first when the fix is obvious.
- Student-facing: full plain-language explanations, no sales jargon.

## Status

- [x] Repo scaffolded (`3625d49`→`207566a`)
- [x] Phase 0 CED research (`a020070`)
- [ ] Books ingested (3 books + 3 Princeton test PDFs — in repo, organized)
- [ ] Reclaim pass (RUNNING — extract + re-conceive from all sources)
- [ ] Re-conception pass
- [ ] Bank assembly + blind audit
- [ ] Test assembly (10 tests)
- [ ] Reviews + exemplars + explanations
- [ ] Prod-readiness review
