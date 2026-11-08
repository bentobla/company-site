#!/usr/bin/env python3
"""Refresh content-based versions of shared styles, scripts and brand images.

Run after editing these assets, before committing. Versions change only when the
file content changes; browsers can keep caching unchanged files normally.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = (
    'base.css', 'style.css', 'site.js', 'company_logo.png',
    'pictures/loern-icon.png', 'pictures/sudoku-icon.png',
    'pictures/tower-icon.png',
)


def version(path: str) -> str:
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()[:12]


def replace_url(text: str, path: str) -> str:
    # Match literal relative or absolute URLs ending at a quote/closing paren.
    # Existing version strings are replaced, making repeated runs idempotent.
    pattern = re.escape(path) + r'(?:\?v=[a-f0-9]+)?(?=[\x22\x27)])'
    return re.sub(pattern, lambda _: path + '?v=' + version(path), text)


def main() -> None:
    # Version the imported base first, then hash the resulting outer stylesheet.
    style = ROOT / 'style.css'
    before = style.read_text()
    after = replace_url(before, 'base.css')
    if after != before:
        style.write_text(after)
    changed = 0
    for page in sorted(ROOT.rglob('*.html')):
        if '.git' in page.parts:
            continue
        before = page.read_text()
        after = before
        for asset in ASSETS:
            after = replace_url(after, asset)
        if after != before:
            page.write_text(after)
            changed += 1
    print(f'Refreshed asset URLs on {changed} HTML pages.')


if __name__ == '__main__':
    main()
