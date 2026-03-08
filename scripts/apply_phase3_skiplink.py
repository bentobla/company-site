#!/usr/bin/env python3
"""Phase 3 implementation: skip link + main landmark id.

Adds:
- A skip link right after <body>:
    <a class="skip-link" href="#main">Skip to content</a>
- An id on the main landmark:
    <main id="main" ...>

Idempotent and locale-wide. Does not touch the root /index.html redirect.

Usage:
  python3 scripts/apply_phase3_skiplink.py --check
  python3 scripts/apply_phase3_skiplink.py --apply
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Change:
    path: Path
    changed: bool
    reasons: list[str]


BODY_OPEN_RE = re.compile(r"<body(\s[^>]*)?>", re.IGNORECASE)
MAIN_TAG_RE = re.compile(r"<main\b", re.IGNORECASE)
MAIN_WITH_ID_RE = re.compile(r"<main\b[^>]*\bid\s*=\s*(?:\"main\"|'main')", re.IGNORECASE)


SKIP_LINK_HTML = '    <a class="skip-link" href="#main">Skip to content</a>'


def is_locale_dir(path: Path) -> bool:
    return path.is_dir() and (path / "index.html").exists() and (path / "about.html").exists()


def ensure_skip_link(html: str) -> tuple[str, bool]:
    if "class=\"skip-link\"" in html or "class='skip-link'" in html:
        return html, False

    m = BODY_OPEN_RE.search(html)
    if not m:
        return html, False

    insert_at = m.end()
    # Insert newline + skip link after <body>
    html2 = html[:insert_at] + "\n" + SKIP_LINK_HTML + html[insert_at:]
    return html2, html2 != html


def ensure_main_id(html: str) -> tuple[str, bool]:
    if not MAIN_TAG_RE.search(html):
        return html, False
    if MAIN_WITH_ID_RE.search(html):
        return html, False

    # Add id="main" as the first attribute
    html2 = MAIN_TAG_RE.sub('<main id="main"', html, count=1)
    return html2, html2 != html


def process_file(path: Path, *, apply: bool) -> Change:
    original = path.read_text(encoding="utf-8", errors="replace")
    html = original
    reasons: list[str] = []

    html, changed_skip = ensure_skip_link(html)
    if changed_skip:
        reasons.append("skip-link")

    html, changed_main = ensure_main_id(html)
    if changed_main:
        reasons.append("main id")

    changed = html != original
    if changed and apply:
        path.write_text(html, encoding="utf-8")

    return Change(path=path, changed=changed, reasons=reasons)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    if args.check == args.apply:
        raise SystemExit("Specify exactly one of --check or --apply")

    locale_dirs = sorted([p for p in ROOT.iterdir() if is_locale_dir(p)], key=lambda p: p.name)
    html_files: list[Path] = []
    for loc in locale_dirs:
        html_files.extend(loc.rglob("*.html"))

    changes: list[Change] = []
    for path in html_files:
        ch = process_file(path, apply=args.apply)
        if ch.changed:
            changes.append(ch)

    mode = "CHECK" if args.check else "APPLY"
    print(f"{mode}: changed {len(changes)} file(s)")
    for ch in changes:
        print(f"- {ch.path.relative_to(ROOT)} :: {', '.join(ch.reasons)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
