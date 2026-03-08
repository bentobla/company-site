#!/usr/bin/env python3
"""Phase 5: small localization QA fixes.

Goals:
- Remove obvious English leaks in non-English locales.
- Keep changes deterministic and safe.

This script intentionally does NOT change any URLs/hrefs (esp. protected lœrn privacy links).

Usage:
  python3 scripts/apply_phase5_localization_fixes.py            # apply changes
  python3 scripts/apply_phase5_localization_fixes.py --check   # report only
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Replacement:
    old: str
    new: str
    label: str


def apply_all(text: str, replacements: list[Replacement]) -> tuple[str, list[str]]:
    changed: list[str] = []
    for repl in replacements:
        if repl.old not in text:
            continue
        text = text.replace(repl.old, repl.new)
        changed.append(repl.label)
    return text, changed


def iter_locale_html(locale: str) -> list[Path]:
    base = ROOT / locale
    if not base.exists():
        return []
    return sorted([p for p in base.rglob("*.html") if p.is_file()])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Only report changes; do not write files")
    args = parser.parse_args()

    skip_link_old = '<a class="skip-link" href="#main">Skip to content</a>'

    skip_link_text: dict[str, str] = {
        "de": "Zum Inhalt springen",
        "fr": "Aller au contenu",
        "es": "Saltar al contenido",
        "it": "Vai al contenuto",
        "nl": "Ga naar inhoud",
        "sv": "Hoppa till innehållet",
    }

    # Exact-string replacements to keep this safe and deterministic.
    file_replacements: dict[str, list[Replacement]] = {
        "de/projects.html": [
            Replacement(
                old="                <p>Offline-first. Kein Konto. Deine Lerndaten bleiben auf deinem Gerät.</p>",
                new="                <p>Offline zuerst. Kein Konto. Deine Lerndaten bleiben auf deinem Gerät.</p>",
                label="de:projects:offline-first-translate",
            )
        ],
        "es/projects.html": [
            Replacement(
                old="                <p>Offline primero. Sin cuenta. Tus datos de aprendizaje se quedan en tu dispositivo.</p>",
                new="                <p>Primero sin conexión. Sin cuenta. Tus datos de aprendizaje se quedan en tu dispositivo.</p>",
                label="es:projects:offline-first-translate",
            )
        ],
        "it/projects.html": [
            Replacement(
                old="                <p>Offline prima di tutto. Nessun account. I tuoi dati di studio restano sul tuo dispositivo.</p>",
                new="                <p>Prima offline. Nessun account. I tuoi dati di studio restano sul tuo dispositivo.</p>",
                label="it:projects:offline-first-translate",
            )
        ],
        "nl/projects.html": [
            Replacement(
                old="                <p>Offline-first. Geen account. Je leerdata blijft op je apparaat.</p>",
                new="                <p>Offline eerst. Geen account. Je leerdata blijft op je apparaat.</p>",
                label="nl:projects:offline-first-translate",
            )
        ],
        "sv/projects.html": [
            Replacement(
                old="                <p>Offline först. Inget konto. Dina studiedata stannar på din enhet.</p>",
                new="                <p>Offline först. Inget konto. Dina studiedata stannar på din enhet.</p>",
                label="sv:projects:offline-first-translate",
            )
        ],
        "nl/about.html": [
            Replacement(
                old="            <p><strong>Product-first:</strong> we bouwen en onderhouden onze eigen applicaties (geen klantwerk).</p>",
                new="            <p><strong>Productgericht:</strong> we bouwen en onderhouden onze eigen applicaties (geen klantwerk).</p>",
                label="nl:about:product-first-translate",
            )
        ],
    }

    any_changed = False

    # 1) Localize skip-link text in non-English locales.
    for locale, localized in skip_link_text.items():
        new_skip = f'<a class="skip-link" href="#main">{localized}</a>'
        for html_path in iter_locale_html(locale):
            rel = html_path.relative_to(ROOT).as_posix()
            original = html_path.read_text(encoding="utf-8")
            updated = original

            if skip_link_old in updated:
                updated = updated.replace(skip_link_old, new_skip)

            # 2) Per-file targeted replacements.
            for repl in file_replacements.get(rel, []):
                if repl.old in updated:
                    updated = updated.replace(repl.old, repl.new)

            if updated == original:
                continue

            any_changed = True
            if args.check:
                print(f"[EDIT] {rel}")
            else:
                html_path.write_text(updated, encoding="utf-8")
                print(f"[EDIT] {rel}")

    if args.check:
        return 0

    if not any_changed:
        print("No changes applied.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
