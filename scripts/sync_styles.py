"""Embed the shared CSS so downloaded pages do not need sibling-file access."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'courses.html', 'placement-test.html', 'registration.html')
PATTERN = re.compile(r'  <style id="academy-styles">.*?</style>', re.DOTALL)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail if embedded styles are stale')
    args = parser.parse_args()
    css = (ROOT / 'assets/styles.css').read_text(encoding='utf-8').rstrip()
    if '</style' in css.lower():
        raise SystemExit('CSS must not contain a closing style tag')
    expected = '  <style id="academy-styles">\n' + css + '\n  </style>'
    stale = []
    for filename in PAGES:
        path = ROOT / filename
        html = path.read_text(encoding='utf-8')
        match = PATTERN.search(html)
        if args.check:
            if not match or match.group() != expected:
                stale.append(filename)
        elif match:
            path.write_text(PATTERN.sub(lambda _: expected, html), encoding='utf-8')
        else:
            old = '  <link rel="stylesheet" href="assets/styles.css">'
            if old not in html:
                raise SystemExit(f'{filename}: stylesheet marker not found')
            path.write_text(html.replace(old, expected), encoding='utf-8')
    if stale:
        raise SystemExit('Run python3 scripts/sync_styles.py to update: ' + ', '.join(stale))
    print('Embedded styles checked.' if args.check else 'Embedded styles updated.')


if __name__ == '__main__':
    main()
