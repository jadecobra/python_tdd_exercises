"""Autosectionlabel-aware Sphinx reference validator.

Extracts explicit targets (.. _label:) and section headings across all .rst files
to validate :ref:`target` references without false positives.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_EXPLICIT_TARGET_RE = re.compile(r"^\.\. _`?([^:`]+)`?:\s*$")
_REF_RE = re.compile(r":ref:`([^`]+)`")
_MARKUP_RE = re.compile(r"[`*]")
_HEADING_CHARS = set("=~-*#^\"'`:")


def _clean_target(text: str) -> str:
    cleaned = _MARKUP_RE.sub("", text).strip().lower()
    # Normalize multiple whitespace to single space
    return " ".join(cleaned.split())


def build_target_catalog(source_dir: Path) -> set[str]:
    """Extract explicit targets and section heading slugs across all .rst files."""
    catalog: set[str] = set()

    for rst_path in source_dir.rglob("*.rst"):
        try:
            lines = rst_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue

        for idx, line in enumerate(lines):
            # Check for explicit anchor: .. _label: or .. _`spaced label`:
            stripped = line.strip()
            explicit_match = _EXPLICIT_TARGET_RE.match(stripped)
            if explicit_match:
                catalog.add(_clean_target(explicit_match.group(1)))

            # Check for section heading
            if not stripped or stripped.startswith(".. "):
                continue

            # Heading with underline:
            if idx + 1 < len(lines):
                next_line = lines[idx + 1].strip()
                if (
                    next_line
                    and len(next_line) >= len(stripped)
                    and next_line[0] in _HEADING_CHARS
                    and len(set(next_line)) == 1
                ):
                    catalog.add(_clean_target(stripped))

            # Heading with overline and underline:
            if idx > 0 and idx + 1 < len(lines):
                prev_line = lines[idx - 1].strip()
                next_line = lines[idx + 1].strip()
                if (
                    prev_line
                    and next_line
                    and len(prev_line) >= len(stripped)
                    and len(next_line) >= len(stripped)
                    and prev_line[0] in _HEADING_CHARS
                    and next_line[0] in _HEADING_CHARS
                    and len(set(prev_line)) == 1
                    and len(set(next_line)) == 1
                ):
                    catalog.add(_clean_target(stripped))

    return catalog


def extract_ref_target(raw_content: str) -> str:
    """Extract target identifier from :ref:`raw_content` (handling Title <target>)."""
    trimmed = raw_content.strip()
    if "<" in trimmed and trimmed.endswith(">"):
        return trimmed[trimmed.find("<") + 1 : -1].strip()
    return trimmed


def check_refs(path: Path, catalog: set[str]) -> list[str]:
    """Validate all :ref:`...` in path against the catalog."""
    errors: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    except OSError as err:
        return [f"{path}: failed to read file: {err}"]

    for idx, line in enumerate(lines):
        for match in _REF_RE.finditer(line):
            raw = match.group(1)
            target = extract_ref_target(raw)
            cleaned = _clean_target(target)
            if cleaned not in catalog:
                errors.append(f"{path}:{idx + 1}: broken reference target '{target}'")

    return errors


def validate_file(path: Path, catalog: set[str]) -> list[str]:
    """Validate single file against the target catalog."""
    return check_refs(path, catalog)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate :ref: targets against headings and explicit anchors."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="RST files or directories to validate. Defaults to source/ if omitted.",
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("source"),
        help="Root documentation directory to build catalog from (default: source).",
    )
    args = parser.parse_args(argv)

    source_dir = args.source_dir
    if not source_dir.is_dir():
        print(f"Error: documentation directory '{source_dir}' does not exist.", file=sys.stderr)
        return 1

    catalog = build_target_catalog(source_dir)
    print(f"Loaded {len(catalog)} valid targets from {source_dir}.")

    targets_to_check: list[Path] = []
    if args.paths:
        for p in args.paths:
            if p.is_dir():
                targets_to_check.extend(sorted(p.rglob("*.rst")))
            elif p.is_file():
                targets_to_check.append(p)
            else:
                print(f"Warning: path '{p}' not found.", file=sys.stderr)
    else:
        targets_to_check = sorted(source_dir.rglob("*.rst"))

    all_errors: list[str] = []
    for file_path in targets_to_check:
        errors = check_refs(file_path, catalog)
        all_errors.extend(errors)

    if all_errors:
        print(f"\nFound {len(all_errors)} broken reference(s):", file=sys.stderr)
        for err in all_errors:
            print(f"  {err}", file=sys.stderr)
        return 1

    print(f"All {len(targets_to_check)} file(s) checked: no broken references found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
