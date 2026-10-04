"""Fail when light-mode code text is the same color as the light page."""

import re
import sys
from pathlib import Path

_EXACT_TEXT_SELECTORS = frozenset({"pre", "code", ".highlight"})
_SKIP_COLOR = frozenset({"inherit", "transparent", "currentcolor"})
_HSL_COMPONENTS = re.compile(
    r"^([+-]?\d+(?:\.\d+)?)\s+([+-]?\d+(?:\.\d+)?)%\s+([+-]?\d+(?:\.\d+)?)%$"
)
_HEX = re.compile(r"^#([0-9a-f]{3}|[0-9a-f]{6})$", re.I)
_RGB = re.compile(
    r"^rgba?\(\s*([+-]?\d+(?:\.\d+)?)(%?)\s*[, ]\s*"
    r"([+-]?\d+(?:\.\d+)?)(%?)\s*[, ]\s*"
    r"([+-]?\d+(?:\.\d+)?)(%?)",
    re.I,
)


def check(pygments_css: str, theme_css: str) -> list[str]:
    background = None
    foreground = None
    theme_text = []
    token_text = []

    def visit_theme(selector: str, body: str) -> None:
        nonlocal background, foreground
        if ".dark" in selector:
            return
        selectors = _selector_list(selector)
        for name, value in _declarations(body):
            raw = _unimportant(value)
            if ":root" in selectors and name in {"--background", "--foreground"}:
                parsed = _hsl_components(raw)
                if parsed is None:
                    continue
                if name == "--background":
                    background = parsed
                else:
                    foreground = parsed
            if name != "color":
                continue
            for sel in selectors:
                if sel in _EXACT_TEXT_SELECTORS:
                    theme_text.append((sel, raw))

    def visit_pygments(selector: str, body: str) -> None:
        if ".dark" in selector:
            return
        for name, value in _declarations(body):
            if name != "color":
                continue
            token_text.append((re.sub(r"\s+", " ", selector).strip(), _unimportant(value)))

    _walk(_without_comments(theme_css), visit_theme)
    _walk(_without_comments(pygments_css), visit_pygments)

    if background is None:
        return ["missing light background"]

    failures = []
    for selector, raw in token_text:
        color = _literal_rgb(raw)
        if color is not None and color == background:
            failures.append(f"{selector} color {raw} matches light background")
    for selector, raw in theme_text:
        color = _theme_rgb(raw, foreground)
        if color is not None and color == background:
            failures.append(f"{selector} color {raw} matches light background")
    if foreground is not None and foreground == background:
        failures.append("light foreground matches light background")
    return failures


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        return 2
    root = Path(argv[0])
    sheets = (root / "_static" / "pygments.css", root / "_static" / "theme.css")
    if not root.is_dir() or any(not path.is_file() for path in sheets):
        return 2
    failures = check(sheets[0].read_text(encoding="utf-8"), sheets[1].read_text(encoding="utf-8"))
    if not failures:
        return 0
    sys.stdout.write("\n".join(failures) + "\n")
    return 1


def _without_comments(css: str) -> str:
    parts = []
    index = 0
    while index < len(css):
        if css.startswith("/*", index):
            end = css.find("*/", index + 2)
            if end == -1:
                break
            index = end + 2
            continue
        parts.append(css[index])
        index += 1
    return "".join(parts)


def _walk(css: str, visit) -> None:
    index = 0
    length = len(css)
    while index < length:
        while index < length and css[index].isspace():
            index += 1
        if index >= length:
            return
        end, opener = _prelude_end(css, index)
        if opener is None:
            return
        prelude = css[index:end]
        if css[opener] == ";":
            index = opener + 1
            continue
        body, index = _block_body(css, opener)
        if prelude.lstrip().startswith("@"):
            if not _dark_media(prelude):
                _walk(body, visit)
            continue
        visit(prelude.strip(), body)


def _prelude_end(css: str, start: int) -> tuple[int, int | None]:
    parens = 0
    for index in range(start, len(css)):
        char = css[index]
        if char == "(":
            parens += 1
        elif char == ")" and parens:
            parens -= 1
        elif parens == 0 and char in "{;":
            return index, index
    return len(css), None


def _block_body(css: str, open_brace: int) -> tuple[str, int]:
    depth = 0
    for index in range(open_brace, len(css)):
        if css[index] == "{":
            depth += 1
        elif css[index] == "}":
            depth -= 1
            if depth == 0:
                return css[open_brace + 1 : index], index + 1
    return css[open_brace + 1 :], len(css)


def _dark_media(prelude: str) -> bool:
    compact = re.sub(r"\s+", "", prelude.lower())
    return compact.startswith("@media") and "prefers-color-scheme:dark" in compact


def _declarations(body: str) -> list[tuple[str, str]]:
    found = []
    for part in _split_semicolons(body):
        if "{" in part or ":" not in part:
            continue
        name, value = part.split(":", 1)
        found.append((name.strip().lower(), value.strip()))
    return found


def _split_semicolons(body: str) -> list[str]:
    parts = []
    chunk = []
    depth = 0
    for char in body:
        if char == "{":
            depth += 1
        elif char == "}":
            depth = max(0, depth - 1)
        if char == ";" and depth == 0:
            parts.append("".join(chunk))
            chunk = []
        else:
            chunk.append(char)
    if "".join(chunk).strip():
        parts.append("".join(chunk))
    return parts


def _selector_list(selector: str) -> list[str]:
    return [re.sub(r"\s+", " ", part).strip() for part in selector.split(",")]


def _unimportant(value: str) -> str:
    return re.sub(r"\s*!important\s*$", "", value.strip(), flags=re.I)


def _hsl_components(value: str) -> tuple[int, int, int] | None:
    match = _HSL_COMPONENTS.fullmatch(value.strip())
    if match is None:
        return None
    hue, saturation, lightness = (float(group) for group in match.groups())
    return _hsl_to_rgb(hue, saturation, lightness)


def _hsl_to_rgb(hue: float, saturation: float, lightness: float) -> tuple[int, int, int]:
    hue = hue % 360
    saturation /= 100.0
    lightness /= 100.0

    def channel(percent: float, peak: float, offset: float) -> float:
        amount = offset
        if amount < 0:
            amount += 1
        if amount > 1:
            amount -= 1
        if amount < 1 / 6:
            return percent + (peak - percent) * 6 * amount
        if amount < 1 / 2:
            return peak
        if amount < 2 / 3:
            return percent + (peak - percent) * (2 / 3 - amount) * 6
        return percent

    if saturation == 0:
        red = green = blue = lightness
    else:
        peak = (
            lightness * (1 + saturation)
            if lightness < 0.5
            else lightness + saturation - lightness * saturation
        )
        percent = 2 * lightness - peak
        turn = hue / 360
        red = channel(percent, peak, turn + 1 / 3)
        green = channel(percent, peak, turn)
        blue = channel(percent, peak, turn - 1 / 3)
    return tuple(int(round(min(1.0, max(0.0, item)) * 255)) for item in (red, green, blue))


def _literal_rgb(value: str) -> tuple[int, int, int] | None:
    compact = re.sub(r"\s+", "", value.lower())
    if compact in _SKIP_COLOR:
        return None
    hex_match = _HEX.fullmatch(compact)
    if hex_match:
        digits = hex_match.group(1)
        if len(digits) == 3:
            digits = "".join(char * 2 for char in digits)
        return tuple(int(digits[index : index + 2], 16) for index in (0, 2, 4))
    rgb_match = _RGB.match(value.strip())
    if rgb_match is None or any(rgb_match.group(index) == "%" for index in (2, 4, 6)):
        return None
    return tuple(
        int(round(min(255.0, max(0.0, float(rgb_match.group(index))))))
        for index in (1, 3, 5)
    )


def _theme_rgb(value: str, foreground: tuple[int, int, int] | None) -> tuple[int, int, int] | None:
    compact = re.sub(r"\s+", "", value.lower())
    if compact in {"var(--foreground)", "hsl(var(--foreground))"}:
        return foreground
    return _literal_rgb(value)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
