"""Assemble 10 AP World practice tests from the merged bank.

Usage: python3 build/tests/assemble_tests.py
Reads: build/bank/mcq-bank.json, build/frq-remapped/saq-sets-*/, build/frq-remapped/dbqs/, build/frq-remapped/leqs/
Writes: build/tests/test-01.json .. test-10.json, build/tests/ANSWER_KEYS.md

Rules (Fall 2026 CED):
- 55 MCQ per test, 550 UNIQUE across tests, zero overlap.
- Unit weights per test: U1/U2/U7/U8/U9 = 5 each (9.1%), U3/U4 = 8 each (14.5%), U5/U6 = 7 each (12.7%).
- Visual items (image_url present) distributed evenly across tests.
- 3 SAQ sets per test (mandated source-type rotation already in the sets).
- 1 DBQ (7 docs), 1 LEQ (single prompt) per test; DBQ topics span 1200-2001, varied; LEQs cover all 3 reasoning processes.
- New-format directions text only.
"""
import json, glob, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
BANK = os.path.join(ROOT, 'build', 'bank', 'mcq-bank.json')

UNIT_QUOTA = {1: 5, 2: 5, 3: 8, 4: 8, 5: 7, 6: 7, 7: 5, 8: 5, 9: 5}  # = 55
assert sum(UNIT_QUOTA.values()) == 55

SAQ_DIRECTIONS = (
    "Answer all three questions. Each question has three parts (a, b, and c). "
    "You have 40 minutes for this section."
)
DBQ_DIRECTIONS = (
    "Question 1 is based on the accompanying documents. The documents have been edited "
    "for the purpose of this exercise. You are advised to spend 15 minutes reading and "
    "planning and 45 minutes writing your answer."
)
LEQ_DIRECTIONS = (
    "Answer the question below. You have 40 minutes."
)
MCQ_DIRECTIONS = (
    "Each of the questions or incomplete statements below is followed by four suggested "
    "answers or completions. Select the one that is best in each case. You have 55 minutes."
)


def load_bank():
    bank = json.load(open(BANK))
    # exclude any items flagged problematic
    ok = [it for it in bank if not it.get('quarantined') and not it.get('flags')]
    print(f"bank: {len(bank)} total, {len(ok)} eligible (excluded {len(bank)-len(ok)} flagged)")
    return ok


def main():
    random.seed(20261002)
    bank = load_bank()
    by_unit = {}
    for u in range(1, 10):
        pool = [it for it in bank if it['unit'] == u]
        random.shuffle(pool)
        by_unit[u] = pool
        need = UNIT_QUOTA[u] * 10
        print(f"U{u}: pool {len(pool)}, need {need} {'OK' if len(pool) >= need else 'SHORT'}")
        if len(pool) < need:
            sys.exit(f"FATAL: unit {u} short")

    # deal 55 per test, zero overlap; force even visual distribution first
    # (54 image items -> 5-6 per test), then fill remaining by unit quota
    tests = [[] for _ in range(10)]
    visuals = [it for it in bank if it.get('image_url')]
    random.shuffle(visuals)
    for i, it in enumerate(visuals):
        tests[i % 10].append(it)
    used_ids = set(it['id'] for t in tests for it in t)
    for t in range(10):
        # count visuals already placed per unit in this test
        placed_by_unit = {}
        for it in tests[t]:
            placed_by_unit[it['unit']] = placed_by_unit.get(it['unit'], 0) + 1
        for u, q in UNIT_QUOTA.items():
            need = q - placed_by_unit.get(u, 0)
            if need <= 0:
                continue
            pool = [it for it in by_unit[u] if it['id'] not in used_ids]
            # prefer visual_reconstructed to boost visual-adjacent coverage
            pool.sort(key=lambda it: (not it.get('visual_reconstructed'), random.random()))
            take = pool[:need]
            assert len(take) == need, f"unit {u} test {t}: short"
            tests[t].extend(take)
            used_ids.update(it['id'] for it in take)
        random.shuffle(tests[t])
        assert len(tests[t]) == 55
    # verify uniqueness
    all_ids = [it['id'] for t in tests for it in t]
    assert len(all_ids) == len(set(all_ids)) == 550, "duplicate MCQ across tests!"
    print("550 unique MCQs dealt, zero overlap")

    # visual distribution report
    for t, mcqs in enumerate(tests):
        nv = sum(1 for it in mcqs if it.get('image_url'))
        print(f"test-{t+1:02d}: {nv} visual items ({nv/55*100:.0f}%)")

    # SAQ sets: 60 available, need 30
    saq_files = sorted(glob.glob(os.path.join(ROOT, 'build/frq-remapped/saq-sets-*/set-*.json')))
    print(f"SAQ sets available: {len(saq_files)}")
    assert len(saq_files) >= 30

    # DBQs: 10 available, need 10
    dbq_files = sorted(glob.glob(os.path.join(ROOT, 'build/frq-remapped/dbqs/dbq-*.json')))
    print(f"DBQs available: {len(dbq_files)}")
    assert len(dbq_files) >= 10

    # LEQs: 20 available, need 10 covering all 3 reasoning processes
    leq_files = sorted(glob.glob(os.path.join(ROOT, 'build/frq-remapped/leqs/leq-*.json')))
    leqs = [json.load(open(f)) for f in leq_files]
    print(f"LEQs available: {len(leq_files)}")
    from collections import Counter
    print('LEQ reasoning:', Counter(l.get('target_reasoning_process') for l in leqs))

    # assign: round-robin SAQs, DBQs in order, LEQs chosen for reasoning coverage
    leq_by_reason = {}
    for l in leqs:
        leq_by_reason.setdefault(l.get('target_reasoning_process'), []).append(l)
    reasons = list(leq_by_reason.keys())
    print('reasoning processes:', reasons)

    chosen_leqs = []
    for t in range(10):
        r = reasons[t % len(reasons)]
        pool = leq_by_reason[r]
        chosen_leqs.append(pool[(t // len(reasons)) % len(pool)])

    out_dir = os.path.join(ROOT, 'build', 'tests')
    os.makedirs(out_dir, exist_ok=True)
    answer_keys = []
    for t in range(10):
        saqs = [json.load(open(f)) for f in saq_files[t*3:(t+1)*3]]
        dbq = json.load(open(dbq_files[t]))
        test = {
            'id': f'ap-world-practice-test-{t+1:02d}',
            'format': 'Fall 2026 CED',
            'section_1a': {
                'directions': MCQ_DIRECTIONS,
                'questions': [
                    {
                        'n': i+1,
                        'id': it['id'],
                        'unit': it['unit'],
                        'stimulus': it.get('stimulus'),
                        'image_url': it.get('image_url'),
                        'stem': it['stem'],
                        'options': it['options'],
                        'skill': it['skill'],
                    } for i, it in enumerate(tests[t])
                ],
            },
            'section_1b': {
                'directions': SAQ_DIRECTIONS,
                'saq_sets': saqs,
            },
            'section_2a': {
                'directions': DBQ_DIRECTIONS,
                'dbq': dbq,
            },
            'section_2b': {
                'directions': LEQ_DIRECTIONS,
                'leq': chosen_leqs[t],
            },
        }
        json.dump(test, open(os.path.join(out_dir, f'test-{t+1:02d}.json'), 'w'),
                  indent=1, ensure_ascii=False)
        answer_keys.append((t+1, tests[t]))
    print(f"wrote 10 test files to {out_dir}")

    # ANSWER_KEYS.md (separate file)
    with open(os.path.join(out_dir, 'ANSWER_KEYS.md'), 'w') as f:
        f.write('# AP World Practice Tests — Answer Keys\n\n')
        f.write('Keys only. Explanations live in build/bank/mcq-bank.json by item id.\n\n')
        for t, mcqs in answer_keys:
            f.write(f'## Test {t:02d}\n\n')
            f.write(''.join(
                f"{i+1}. {it['key']} ({it['id']})\n" for i, it in enumerate(mcqs)))
            f.write('\n')
    print("wrote ANSWER_KEYS.md")


if __name__ == '__main__':
    main()
