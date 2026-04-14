#!/usr/bin/env python3
"""
Add PL, PT-BR, PT-PT options to lang-switch selects and JS page maps
in all pre-existing locale HTML files (de, en, fr, es, it, nl, sv).

Run from the project root:
  python3 scripts/update_existing_locales.py
"""

import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXISTING_LOCALES = ["de", "en", "fr", "es", "it", "nl", "sv"]

NEW_OPTIONS = (
    '                    <option value="pl">PL</option>\n'
    '                    <option value="pt-br">PT-BR</option>\n'
    '                    <option value="pt-pt">PT-PT</option>'
)

# Gather all HTML files from existing locales
files = []
for locale in EXISTING_LOCALES:
    base = os.path.join(BASE, locale)
    for dirpath, _, filenames in os.walk(base):
        for fn in filenames:
            if fn.endswith(".html"):
                files.append(os.path.join(dirpath, fn))

print(f"Found {len(files)} files to update")

for fpath in sorted(files):
    with open(fpath, encoding="utf-8") as f:
        content = f.read()

    # 1. Add new <option> elements after the SV option in the lang-switch select
    #    The SV option may or may not have "selected".
    new_content = re.sub(
        r'(<option value="sv"[^>]*>SV</option>\n)(\s*</select>)',
        r'\1' + NEW_OPTIONS + '\n' + r'\2',
        content,
    )

    # 2. Add PL/PT-BR/PT-PT entries to the JS pages map
    #    The SV entry looks like:  "sv": "../../sv/...",
    def insert_new_pages(m):
        sv_line = m.group(1)  # e.g.  '        "sv": "../sv/",\n'
        sv_target_m = re.search(r'"sv":\s*"([^"]+)"', sv_line)
        if not sv_target_m:
            return m.group(0)
        sv_target = sv_target_m.group(1)
        # Derive targets for new locales by replacing /sv/ (or trailing /sv")
        def derive(lc):
            t = re.sub(r'/sv(/|")', f'/{lc}\\1', sv_target)
            return t
        pl_t = derive("pl")
        ptbr_t = derive("pt-br")
        ptpt_t = derive("pt-pt")
        return (
            sv_line
            + f'        "pl": "{pl_t}",\n'
            + f'        "pt-br": "{ptbr_t}",\n'
            + f'        "pt-pt": "{ptpt_t}",\n'
        )

    new_content = re.sub(
        r'(        "sv":\s*"[^"]+",\n)',
        insert_new_pages,
        new_content,
    )

    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Updated: {fpath.replace(BASE + '/', '')}")
    else:
        print(f"  NO CHANGE: {fpath.replace(BASE + '/', '')}")

print("\nDone.")
