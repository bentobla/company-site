#!/usr/bin/env python3
"""Phase 1 implementation: active nav include + Contact CTA class.

Applies two improvements across all locale HTML pages:
- Include the shared `/site.js` with correct relative path (depth-aware).
- Add `class="nav-cta"` to the Contact link in the header nav.

Idempotent: safe to run multiple times.

Usage:
  python3 scripts/apply_phase1_active_nav_and_cta.py --check
  python3 scripts/apply_phase1_active_nav_and_cta.py --apply
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


def is_locale_dir(path: Path) -> bool:
    return path.is_dir() and (path / "index.html").exists() and (path / "about.html").exists()


def script_src_for(path: Path) -> str:
    # path is like ROOT/<lang>/.../*.html
    rel = path.relative_to(ROOT)
    parts = rel.parts
    # parts[0] is locale
    depth_after_locale = len(parts) - 2  # number of directories between locale and file

    if depth_after_locale == 0:
        return "../site.js"
    if depth_after_locale == 1:
        return "../../site.js"
    if depth_after_locale == 2:
        return "../../../site.js"

    # Should not happen for current structure, but make it robust.
    return "../" * (depth_after_locale + 1) + "site.js"


LANG_SCRIPT_MARKER_RE = re.compile(r"\n\s*<script>\s*\n\s*// Language switcher", re.MULTILINE)


def ensure_site_js_include(html: str, src: str) -> tuple[str, bool]:
    if "site.js" in html:
        return html, False

    m = LANG_SCRIPT_MARKER_RE.search(html)
    if not m:
        return html, False

    insertion = f"\n    <script src=\"{src}\"></script>\n" + m.group(0).lstrip("\n")
    html2 = html[: m.start()] + insertion + html[m.end() :]
    return html2, html2 != html


def ensure_contact_cta(html: str) -> tuple[str, bool]:
    # Only update the header nav link; this is intentionally simple and based on the template.
    # Handle the common href forms used at different directory depths.
    patterns = [
        (r'<a href="contact\.html">', r'<a href="contact.html" class="nav-cta">'),
        (r'<a href="\.\./contact\.html">', r'<a href="../contact.html" class="nav-cta">'),
        (r'<a href="\.\./\.\./contact\.html">', r'<a href="../../contact.html" class="nav-cta">'),
    ]

    if 'class="nav-cta"' in html:
        return html, False

    html2 = html
    changed = False
    for pat, repl in patterns:
        new_html = re.sub(pat, repl, html2, count=1)
        if new_html != html2:
            html2 = new_html
            changed = True
            break

    return html2, changed


def process_file(path: Path) -> Change:
    original = path.read_text(encoding="utf-8", errors="replace")
    html = original
    reasons: list[str] = []

    src = script_src_for(path)
    html, added_script = ensure_site_js_include(html, src)
    if added_script:
        reasons.append("include site.js")

    html, cta = ensure_contact_cta(html)
    if cta:
        reasons.append("contact nav-cta")

    if html == original:
        return Change(path=path, changed=False, reasons=[])

    path.write_text(html, encoding="utf-8")
    return Change(path=path, changed=True, reasons=reasons)


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

    if args.check:
        for path in html_files:
            text = path.read_text(encoding="utf-8", errors="replace")
            would = []
            if "site.js" not in text and LANG_SCRIPT_MARKER_RE.search(text):
                would.append("include site.js")
            if 'class="nav-cta"' not in text and re.search(r'<a href="(\.\./){0,2}contact\.html">', text):
                would.append("contact nav-cta")
            if would:
                changes.append(Change(path=path, changed=True, reasons=would))

        print(f"CHECK: {len(changes)} file(s) would change")
        for ch in changes:
            print(f"- {ch.path.relative_to(ROOT)} :: {', '.join(ch.reasons)}")
        return 0

    applied = 0
    for path in html_files:
        ch = process_file(path)
        if ch.changed:
            applied += 1
            changes.append(ch)

    print(f"APPLY: changed {applied} file(s)")
    for ch in changes:
        print(f"- {ch.path.relative_to(ROOT)} :: {', '.join(ch.reasons)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
