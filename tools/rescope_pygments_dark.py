"""Move dark Pygments rules from the OS media query onto html.dark.

Theme 6 writes the Monokai sheet inside @media (prefers-color-scheme: dark)
and sets .highlight { background-color: transparent }. The page background
follows the html.dark class from the theme toggle. Those two switches
disagree, so a light page can show #F8F8F2 text.
"""

import re
import sys
from pathlib import Path

_DARK_MEDIA = re.compile(
    r"@media\s*\(\s*prefers-color-scheme\s*:\s*dark\s*\)\s*\{",
    re.I,
)


def rescope(css: str) -> str:
    """Return css with each dark-mode media block rewritten as html.dark rules."""
    parts = []
    cursor = 0
    while True:
        match = _DARK_MEDIA.search(css, cursor)
        if match is None:
            parts.append(css[cursor:])
            break
        parts.append(css[cursor:match.start()])
        body, end = _block(css, match.end() - 1)
        parts.append(_prefix_rules(body))
        cursor = end
    return "".join(parts)


def rescope_html_dir(html_dir: Path) -> None:
    """Rewrite build/html/_static/pygments.css in place.

    Missing sheet is an error. A sheet with no dark media block is unchanged.
    """
    path = html_dir / "_static" / "pygments.css"
    if not path.is_file():
        raise FileNotFoundError(path)
    original = path.read_text(encoding="utf-8")
    rewritten = rescope(original)
    if _DARK_MEDIA.search(rewritten):
        raise RuntimeError(f"dark media query remains in {path}")
    path.write_text(rewritten, encoding="utf-8")


def _block(css: str, open_brace: int) -> tuple[str, int]:
    depth = 0
    for index in range(open_brace, len(css)):
        char = css[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return css[open_brace + 1:index], index + 1
    raise ValueError("unclosed dark media query")


def _prefix_rules(body: str) -> str:
    out = []
    cursor = 0
    while cursor < len(body):
        brace = body.find("{", cursor)
        if brace == -1:
            out.append(body[cursor:])
            break
        rule_body, end = _block(body, brace)
        kept = _without_backgrounds(rule_body)
        if kept:
            out.append(_prefix_selector(body[cursor:brace]))
            out.append(" {" + kept + "}\n")
        cursor = end
    return "".join(out)


def _without_backgrounds(body: str) -> str:
    """Drop paint that would cover the theme's transparent code background."""
    kept = []
    for part in body.split(";"):
        if ":" not in part:
            continue
        prop, value = part.split(":", 1)
        if prop.strip().lower() in {"background", "background-color"}:
            continue
        kept.append(f"{prop.strip()}: {value.strip()}")
    if not kept:
        return ""
    return " " + "; ".join(kept) + " "


def _prefix_selector(selector: str) -> str:
    pieces = []
    for part in selector.split(","):
        stripped = part.strip()
        if not stripped:
            continue
        if stripped.startswith("html.dark"):
            pieces.append(stripped)
        else:
            pieces.append(f"html.dark {stripped}")
    joiner = ",\n" if "\n" in selector else ", "
    return joiner.join(pieces)


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: rescope_pygments_dark.py BUILD_HTML", file=sys.stderr)
        return 2
    try:
        rescope_html_dir(Path(argv[0]))
    except FileNotFoundError as exc:
        print(exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
