#!/usr/bin/env python3
"""Phase 1 implementation: header wrapper + language persistence.

Applies two safe, deterministic improvements across all locale HTML pages:
1) Wraps `.site-header` contents in `<div class="header-content">…</div>`
   - Idempotent: skips files that already have the wrapper.
2) Persists the chosen language into localStorage (`jd_lang`) in the
   language switcher handler.
   - Idempotent: skips if the setItem call already exists.

It intentionally does not modify the root `/index.html` redirect page.

Usage:
  python3 scripts/apply_phase1_header_lang.py --check
  python3 scripts/apply_phase1_header_lang.py --apply
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


HEADER_OPEN = '<header class="site-header">'
HEADER_WRAPPER_OPEN = '<div class="header-content">'
HEADER_CLOSE = "</header>"


LANG_SETITEM_SNIPPET = 'try { localStorage.setItem("jd_lang", lang); } catch (e) {}'


VAR_LANG_RE = re.compile(r"^(?P<indent>[\t ]*)var lang = this\.value;\s*$", re.MULTILINE)


@dataclass
class Change:
    path: Path
    changed: bool
    reasons: list[str]


def is_locale_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    if path.name.startswith("."):
        return False
    # Locale dirs in this repo contain at least index.html
    return (path / "index.html").exists() and (path / "about.html").exists()


def wrap_header_content(html: str) -> tuple[str, bool]:
    if HEADER_OPEN not in html or HEADER_CLOSE not in html:
        return html, False

    # If wrapper already exists inside header, skip.
    header_start = html.find(HEADER_OPEN)
    header_end = html.find(HEADER_CLOSE, header_start)
    if header_end == -1:
        return html, False

    header_block = html[header_start:header_end]
    if HEADER_WRAPPER_OPEN in header_block:
        return html, False

    # Insert wrapper open after header open.
    html = html.replace(HEADER_OPEN, HEADER_OPEN + "\n        " + HEADER_WRAPPER_OPEN, 1)

    # Insert wrapper close before header close (first occurrence after start).
    # We insert with indentation that matches the closing header indentation in existing pages.
    html = html.replace(HEADER_CLOSE, "        </div>\n    " + HEADER_CLOSE, 1)

    return html, True


def add_lang_persistence(html: str) -> tuple[str, bool]:
    if 'localStorage.setItem("jd_lang"' in html:
        return html, False

    m = VAR_LANG_RE.search(html)
    if not m:
        return html, False

    indent = m.group("indent")
    injection = m.group(0) + "\n" + indent + LANG_SETITEM_SNIPPET
    html2 = VAR_LANG_RE.sub(injection, html, count=1)
    return html2, html2 != html


def process_file(path: Path) -> Change:
    original = path.read_text(encoding="utf-8", errors="replace")
    html = original
    reasons: list[str] = []

    html, wrapped = wrap_header_content(html)
    if wrapped:
        reasons.append("header-content wrapper")

    html, persisted = add_lang_persistence(html)
    if persisted:
        reasons.append("jd_lang persistence")

    if html == original:
        return Change(path=path, changed=False, reasons=[])

    path.write_text(html, encoding="utf-8")
    return Change(path=path, changed=True, reasons=reasons)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Report what would change")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk")
    args = parser.parse_args()

    if args.check == args.apply:
        raise SystemExit("Specify exactly one of --check or --apply")

    locale_dirs = [p for p in ROOT.iterdir() if is_locale_dir(p)]
    locale_dirs.sort(key=lambda p: p.name)

    html_files: list[Path] = []
    for loc in locale_dirs:
        html_files.extend(loc.rglob("*.html"))

    # Do not touch root index.html
    html_files = [p for p in html_files if p.name.endswith(".html")]

    changes: list[Change] = []

    if args.check:
        for path in html_files:
            text = path.read_text(encoding="utf-8", errors="replace")
            would_wrap = False
            would_persist = False

            # wrapper check
            if HEADER_OPEN in text:
                hs = text.find(HEADER_OPEN)
                he = text.find(HEADER_CLOSE, hs)
                if he != -1 and HEADER_WRAPPER_OPEN not in text[hs:he]:
                    would_wrap = True

            if 'localStorage.setItem("jd_lang"' not in text and VAR_LANG_RE.search(text):
                would_persist = True

            if would_wrap or would_persist:
                reasons = []
                if would_wrap:
                    reasons.append("header-content wrapper")
                if would_persist:
                    reasons.append("jd_lang persistence")
                changes.append(Change(path=path, changed=True, reasons=reasons))

        if not changes:
            print("CHECK: no changes needed")
            return 0

        print(f"CHECK: {len(changes)} file(s) would change")
        for ch in changes:
            rel = ch.path.relative_to(ROOT)
            print(f"- {rel} :: {', '.join(ch.reasons)}")
        return 0

    # apply
    applied = 0
    for path in html_files:
        ch = process_file(path)
        if ch.changed:
            applied += 1
            changes.append(ch)

    print(f"APPLY: changed {applied} file(s)")
    for ch in changes:
        rel = ch.path.relative_to(ROOT)
        print(f"- {rel} :: {', '.join(ch.reasons)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
