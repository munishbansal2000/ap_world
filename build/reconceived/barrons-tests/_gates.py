"""Mechanical gates for build/reconceived/barrons-tests/.
Run: python3 build/reconceived/barrons-tests/_gates.py
Exits nonzero with a report if any gate fails.
"""
import json, os, sys
from collections import Counter

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)))

def load():
    items = []
    for f in sorted(os.listdir(BASE)):
        if f.startswith('test') and f.endswith('.json'):
            items += json.load(open(os.path.join(BASE, f)))
    return items

REQUIRED = ['id','source_id','unit','stimulus','stem','options','key',
            'explanation','option_explanations','skill','reasoning','themes',
            'difficulty','type','stimulus_words','source_stimulus_words']

def main():
    items = load()
    fails = []
    print(f'items: {len(items)}')
    # schema
    for it in items:
        missing = [k for k in REQUIRED if k not in it]
        if missing:
            fails.append(f"{it.get('id')}: missing {missing}")
    # id collisions
    ids = Counter(it['id'] for it in items)
    dupes = [i for i, c in ids.items() if c > 1]
    if dupes: fails.append(f'id collisions: {dupes}')
    # key balance
    keys = Counter(it['key'] for it in items)
    n = len(items)
    for k, c in keys.items():
        if c / n > 0.30:
            fails.append(f'key {k} at {c/n:.1%} (>30%)')
    print('key distribution:', {k: f'{c/n:.1%}' for k, c in sorted(keys.items())})
    # length-tell: fraction of items where the longest option is the key
    lt = 0
    for it in items:
        lens = [len(o) for o in it['options']]
        longest_idx = lens.index(max(lens))
        if 'ABCD'[longest_idx] == it['key']:
            lt += 1
    print(f'length-tell (longest-is-key): {lt/n:.1%}')
    if lt / n > 0.35:
        fails.append(f'length-tell {lt/n:.1%} too high')
    # unit sanity
    units = Counter(it['unit'] for it in items)
    print('units:', dict(sorted(units.items())))
    bad_units = [u for u in units if u not in range(1, 10)]
    if bad_units: fails.append(f'bad units: {bad_units}')
    # options format
    for it in items:
        if len(it['options']) != 4:
            fails.append(f"{it['id']}: {len(it['options'])} options")
    if fails:
        print('\nFAILURES:')
        for f in fails: print(' -', f)
        sys.exit(1)
    print('\nALL GATES GREEN')

if __name__ == '__main__':
    main()
