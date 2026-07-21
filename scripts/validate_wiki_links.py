#!/usr/bin/env python3
"""Validate Markdown links across the complete generated wiki."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
INLINE_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)")
REFERENCE_LINK = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
EXTERNAL_SCHEMES = {"http", "https", "mailto", "data"}


def targets(markdown: str):
    for match in INLINE_LINK.finditer(markdown):
        yield match.group(1).strip("<>")
    for match in REFERENCE_LINK.finditer(markdown):
        yield match.group(1).strip("<>")


def main() -> int:
    errors: list[str] = []
    checked = 0
    files = sorted(WIKI.rglob("*.md"))

    for source in files:
        markdown = source.read_text(encoding="utf-8")
        for target in targets(markdown):
            parsed = urlsplit(target)
            if parsed.scheme.lower() in EXTERNAL_SCHEMES:
                continue
            if target.startswith("#"):
                continue

            checked += 1
            if parsed.path.startswith("/"):
                errors.append(
                    f"{source.relative_to(ROOT)}: root-relative link is not GitHub-safe: {target}"
                )
                continue

            destination = (source.parent / unquote(parsed.path)).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                errors.append(
                    f"{source.relative_to(ROOT)}: link escapes repository: {target}"
                )
                continue

            if parsed.path and not destination.exists():
                errors.append(
                    f"{source.relative_to(ROOT)}: missing target {target} -> "
                    f"{destination.relative_to(ROOT)}"
                )

    if errors:
        print("\n".join(errors))
        print(f"FAILED: {len(errors)} invalid links across {len(files)} wiki files.")
        return 1

    print(f"OK: {checked} internal links resolve across {len(files)} wiki files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
