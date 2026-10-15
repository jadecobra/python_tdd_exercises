"""Mechanical checks for a chapter RST before it is saved.

Fails when a literalinclude path is missing, or when :emphasize-lines: points
outside the shown block. Prints each :lineno-start: and does not judge jumps.
"""

from __future__ import annotations

import sys
from pathlib import Path


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _parse_ranges(spec: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start_s, end_s = part.split("-", 1)
            start = int(start_s)
            end = int(end_s) if end_s.strip() else start
            ranges.append((start, end))
        else:
            n = int(part)
            ranges.append((n, n))
    return ranges


def _shown_line_count(path: Path, lines_opt: str | None) -> int:
    file_lines = path.read_text().splitlines()
    if not lines_opt:
        return len(file_lines)
    count = 0
    for start, end in _parse_ranges(lines_opt):
        if end < start:
            continue
        last = end if end <= len(file_lines) else len(file_lines)
        if start <= len(file_lines):
            count += last - start + 1
    return count


def _directive_body(lines: list[str], start: int, base: int) -> tuple[list[str], int]:
    i = start
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            break
        if _indent(line) <= base or not line.lstrip(" ").startswith(":"):
            break
        i += 1
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    body: list[str] = []
    while i < len(lines):
        line = lines[i]
        if line.strip() == "":
            body.append(line)
            i += 1
            continue
        if _indent(line) <= base:
            break
        body.append(line)
        i += 1
    while body and body[-1].strip() == "":
        body.pop()
    return body, i


def check_rst(path: Path) -> tuple[list[str], list[str]]:
    """Return (errors, lineno-start notes)."""
    text = path.read_text()
    lines = text.splitlines()
    errors: list[str] = []
    notes: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip(" ")
        kind = None
        if stripped.startswith(".. code-block::"):
            kind = "code-block"
        elif stripped.startswith(".. literalinclude::"):
            kind = "literalinclude"
        if kind is None:
            i += 1
            continue
        base = _indent(line)
        argument = stripped.split("::", 1)[1].strip()
        body, nxt = _directive_body(lines, i + 1, base)
        options: dict[str, str] = {}
        j = i + 1
        while j < nxt and j < len(lines) and lines[j].strip() == "":
            j += 1
        while j < len(lines) and lines[j].strip().startswith(":") and _indent(lines[j]) > base:
            opt = lines[j].strip()
            name, _, value = opt[1:].partition(":")
            options[name.strip()] = value.strip()
            j += 1
            if j >= nxt:
                break
        label = argument or kind
        if "lineno-start" in options:
            notes.append(f"{kind} {label} lineno-start {options['lineno-start']}")
        if kind == "literalinclude":
            target = (path.parent / argument).resolve()
            if not argument or not target.is_file():
                errors.append(f"{path}:{i + 1}: missing literalinclude {argument!r}")
                i = nxt
                continue
            shown = _shown_line_count(target, options.get("lines"))
        else:
            shown = len(body)
        if "emphasize-lines" in options:
            spec = options["emphasize-lines"]
            try:
                ranges = _parse_ranges(spec)
            except ValueError:
                errors.append(f"{path}:{i + 1}: bad emphasize-lines {spec!r}")
                i = nxt
                continue
            for start, end in ranges:
                if end < start:
                    errors.append(
                        f"{path}:{i + 1}: reversed emphasize-lines {start}-{end}"
                    )
                    continue
                if start < 1 or end > shown:
                    errors.append(
                        f"{path}:{i + 1}: emphasize-lines {start}-{end} "
                        f"outside 1..{shown}"
                    )
        i = nxt
    return errors, notes


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: check_chapter_rst.py CHAPTER.rst [MORE.rst ...]", file=sys.stderr)
        return 2
    failed = False
    for raw in argv[1:]:
        path = Path(raw)
        errors, notes = check_rst(path)
        print(f"# {path}")
        for note in notes:
            print(note)
        for error in errors:
            print(error)
        if errors:
            failed = True
            print(f"FAIL {path} {len(errors)}")
        else:
            print(f"OK {path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
