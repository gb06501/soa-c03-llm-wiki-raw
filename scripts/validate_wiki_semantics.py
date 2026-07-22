#!/usr/bin/env python3
"""Validate deterministic metadata and corpus-global service framing."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SKILL_ID = re.compile(r"(?<!\d)(\d+\.\d+\.\d+)(?!\d)")
BATCH_LANGUAGE = re.compile(
    r"\b(?:domain\s+\d+|corpus reconciliation|bootstrap|ingest batch)\b",
    re.IGNORECASE,
)


def numeric_id(value: str) -> tuple[int, ...]:
    return tuple(int(part) for part in value.split("."))


def parse_inline_list(frontmatter: str, field: str, path: Path) -> list[str]:
    match = re.search(rf"^{re.escape(field)}:\s*(\[.*\])$", frontmatter, re.MULTILINE)
    if not match:
        raise ValueError(f"{path}: missing inline {field}")
    try:
        values = ast.literal_eval(match.group(1))
    except (SyntaxError, ValueError) as error:
        raise ValueError(f"{path}: invalid {field}: {error}") from error
    if not isinstance(values, list) or not all(isinstance(item, str) for item in values):
        raise ValueError(f"{path}: {field} must be a list of strings")
    return values


def parse_sources(frontmatter: str, path: Path) -> list[str]:
    match = re.search(r"^sources:\n(?P<items>(?:  - .+\n)+)", frontmatter, re.MULTILINE)
    if not match:
        raise ValueError(f"{path}: missing sources list")
    return [line.removeprefix("  - ").strip() for line in match.group("items").splitlines()]


def source_key(source: str) -> tuple[object, ...]:
    match = re.search(r"/raw/skills/(\d+\.\d+\.\d+)-", source)
    if match:
        return (0, *numeric_id(match.group(1)))
    return (1, source)


def readable_sources(body: str, path: Path) -> list[str]:
    marker = "# Sources\n"
    position = body.rfind(marker)
    if position < 0:
        raise ValueError(f"{path}: missing final # Sources section")
    section = body[position + len(marker) :]
    links = re.findall(r"^- \[[^]]+\]\(([^)]+)\)\s*$", section, re.MULTILINE)
    nonblank = [line for line in section.splitlines() if line.strip()]
    if len(links) != len(nonblank):
        raise ValueError(f"{path}: # Sources must contain only readable source links")
    resolved = []
    for target in links:
        destination = (path.parent / target).resolve()
        try:
            resolved.append(destination.relative_to(ROOT).as_posix())
        except ValueError as error:
            raise ValueError(f"{path}: source link escapes the repository: {target}") from error
    return resolved


def semantic_pages() -> Iterable[tuple[Path, str, str]]:
    for path in sorted(WIKI.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        try:
            frontmatter, body = text[4:].split("---\n", 1)
        except ValueError:
            continue
        if re.search(r"^type:", frontmatter, re.MULTILINE):
            yield path, frontmatter, body


def validate_page(path: Path, frontmatter: str, body: str) -> list[str]:
    errors: list[str] = []
    relative = path.relative_to(ROOT)

    try:
        skill_ids = parse_inline_list(frontmatter, "skill_ids", relative)
        if skill_ids != sorted(set(skill_ids), key=numeric_id):
            errors.append(f"{relative}: skill_ids are not unique and numerically sorted")
    except ValueError as error:
        errors.append(str(error))
        skill_ids = []

    try:
        domain_ids = parse_inline_list(frontmatter, "domain_ids", relative)
        if domain_ids != sorted(set(domain_ids), key=numeric_id):
            errors.append(f"{relative}: domain_ids are not unique and numerically sorted")
    except ValueError as error:
        errors.append(str(error))

    try:
        sources = parse_sources(frontmatter, relative)
        if sources != sorted(set(sources), key=source_key):
            errors.append(f"{relative}: sources are not unique and sorted by skill ID")

        source_skill_ids = []
        for source in sources:
            source_path = ROOT / source.removeprefix("/")
            if not source_path.is_file():
                errors.append(f"{relative}: declared source does not exist: {source}")
            match = re.search(r"/raw/skills/(\d+\.\d+\.\d+)-", source)
            if match:
                source_skill_ids.append(match.group(1))
        if skill_ids and source_skill_ids != skill_ids:
            errors.append(f"{relative}: skill_ids do not match raw skill sources")

        readable = readable_sources(body, path)
        declared = [source.removeprefix("/") for source in sources]
        if readable != declared:
            errors.append(f"{relative}: readable # Sources do not match frontmatter order")
    except ValueError as error:
        errors.append(str(error))

    type_match = re.search(r"^type:\s*(.+)$", frontmatter, re.MULTILINE)
    if type_match and type_match.group(1).strip() == "AWS Service":
        description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        core_match = re.search(
            r"(?ms)^# (?!Sources\n)(?:Core model|[^\n]+)\n\n(?P<core>.*?)(?=\n# |\Z)",
            body,
        )
        primary_text = " ".join(
            part
            for part in (
                description_match.group(1) if description_match else "",
                core_match.group("core") if core_match else "",
            )
            if part
        )
        if not description_match or not core_match:
            errors.append(f"{relative}: AWS Service requires a description and primary content section")
        elif BATCH_LANGUAGE.search(primary_text):
            errors.append(f"{relative}: service identity contains domain or ingestion-batch language")

    return errors


def main() -> int:
    errors: list[str] = []
    count = 0
    for path, frontmatter, body in semantic_pages():
        count += 1
        errors.extend(validate_page(path, frontmatter, body))

    if errors:
        print(f"Semantic validation failed with {len(errors)} error(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated deterministic metadata and service framing for {count} semantic pages.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
