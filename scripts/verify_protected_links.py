#!/usr/bin/env python3
"""Verify protected lœrn privacy statement links are unchanged.

Hard requirement:
- Links to lœrn privacy/data-security statements must remain untouched.

This script compares the set of protected href targets in the current working
tree against a reference git ref (default: main).

Protected hrefs are defined as:
- href exactly equal to: "loern/privacy.html" (CTA relative link)
- href ending with: "projects/loern/privacy.html" (covers absolute and relative)

Usage:
  python3 scripts/verify_protected_links.py
  python3 scripts/verify_protected_links.py --ref main
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]


HREF_RE = re.compile(r"href\s*=\s*(?:\"([^\"]*)\"|'([^']*)')", re.IGNORECASE)


@dataclass(frozen=True)
class ScanResult:
    hrefs: set[str]


def iter_html_files_in_worktree(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.html"):
        # Ignore anything in .git just in case
        if ".git" in path.parts:
            continue
        yield path


def read_file_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def git_show_text(ref: str, rel_path: str) -> str:
    completed = subprocess.run(
        ["git", "show", f"{ref}:{rel_path}"],
        cwd=str(ROOT),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return completed.stdout.decode("utf-8", errors="replace")


def git_list_html_files(ref: str) -> list[str]:
    # list tracked files at ref
    completed = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", ref],
        cwd=str(ROOT),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    files = []
    for line in completed.stdout.decode("utf-8", errors="replace").splitlines():
        if line.lower().endswith(".html"):
            files.append(line)
    return files


def extract_protected_hrefs(html: str) -> set[str]:
    matches = set()
    for m in HREF_RE.finditer(html):
        href = m.group(1) if m.group(1) is not None else m.group(2)
        if href is None:
            continue
        href = href.strip()
        if not href:
            continue
        if href == "loern/privacy.html" or href.endswith("projects/loern/privacy.html"):
            matches.add(href)
    return matches


def scan_worktree() -> ScanResult:
    hrefs: set[str] = set()
    for path in iter_html_files_in_worktree(ROOT):
        hrefs |= extract_protected_hrefs(read_file_text(path))
    return ScanResult(hrefs=hrefs)


def scan_ref(ref: str) -> ScanResult:
    hrefs: set[str] = set()
    for rel_path in git_list_html_files(ref):
        hrefs |= extract_protected_hrefs(git_show_text(ref, rel_path))
    return ScanResult(hrefs=hrefs)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", default="main", help="Git ref to compare against (default: main)")
    args = parser.parse_args()

    # Ensure we're in a git repo
    subprocess.run(["git", "rev-parse", "--is-inside-work-tree"], cwd=str(ROOT), check=True)

    baseline = scan_ref(args.ref)
    current = scan_worktree()

    removed = sorted(baseline.hrefs - current.hrefs)
    added = sorted(current.hrefs - baseline.hrefs)

    if not removed and not added:
        print(f"OK: protected href targets unchanged vs {args.ref} ({len(current.hrefs)} unique targets)")
        return 0

    print(f"FAIL: protected href targets changed vs {args.ref}")
    if removed:
        print("Removed targets:")
        for href in removed:
            print(f"- {href}")
    if added:
        print("Added targets:")
        for href in added:
            print(f"+ {href}")

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
