#!/usr/bin/env python3
"""
Second pass: fix JS pages maps where the SV entry was the last (no trailing comma).

Run from the project root:
  python3 scripts/fix_pages_map_sv.py
"""

import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXISTING_LOCALES = ["de", "en", "fr", "es", "it", "nl", "sv"]

files = []
for locale in EXISTING_LOCALES:
    base = os.path.join(BASE, locale)
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            if fn.endswith(".html"):
                files.append(os.path.join(dirpath, fn))

print(f"Scanning {len(files)} files...")

updated = 0
for fpath in sorted(files):
    with open(fpath, encoding="utf-8") as f:
        content = f.read()

    def fix_sv_no_comma(m):
        sv_val = re.search(r'"sv":\s*"([^"]+)"', m.group(0)).group(1)
        def derive(lc):
            return re.sub(r'/sv(/|")', '/' + lc + r'\1', sv_val)
        pl_t = derive("pl")
        ptbr_t = derive("pt-br")
        ptpt_t = derive("pt-pt")
        return (
            '        "sv": "' + sv_val + '",\n'
            '        "pl": "' + pl_t + '",\n'
            '        "pt-br": "' + ptbr_t + '",\n'
            '        "pt-pt": "' + ptpt_t + '"\n'
            '    };'
        )

    new_content = re.sub(
        r'        "sv":\s*"([^"]+)"\n    \};',
        fix_sv_no_comma,
        content,
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Fixed map: {fpath.replace(BASE + '/', '')}")
        updated += 1

print(f"\n{updated} files fixed.")
