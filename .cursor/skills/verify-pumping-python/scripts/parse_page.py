#!/usr/bin/env python3
"""Extract stable handles from a Sphinx HTML snapshot."""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import sys


def text_of(html: str, pattern: str) -> str:
    m = re.search(pattern, html, re.I | re.S)
    if not m:
        return ""
    return " ".join(re.sub(r"<[^>]+>", "", m.group(1)).split())


def h1s(html: str) -> list[str]:
    out = []
    for m in re.finditer(r"<h1[^>]*>(.*?)</h1>", html, re.I | re.S):
        out.append(" ".join(re.sub(r"<[^>]+>", "", m.group(1)).split()))
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("html_path")
    p.add_argument("--url", default="")
    p.add_argument("--meta", default="")
    p.add_argument("--expect-title-substr", default="")
    p.add_argument("--expect-h1-substr", default="")
    p.add_argument("--expect-href", action="append", default=[])
    p.add_argument("--expect-text", action="append", default=[])
    args = p.parse_args()
    raw = pathlib.Path(args.html_path).read_bytes()
    html = raw.decode("utf-8", "replace")
    title = text_of(html, r"<title[^>]*>(.*?)</title>")
    headings = h1s(html)
    sha = hashlib.sha256(raw).hexdigest()
    lines = [
        f"url: {args.url}",
        f"bytes: {len(raw)}",
        f"sha256: {sha}",
        f"title: {title}",
        f"h1: {headings[0] if headings else ''}",
        f"h1_all: {headings}",
    ]
    if args.meta:
        pathlib.Path(args.meta).write_text("\n".join(lines) + "\n")
    print("\n".join(f"  {ln}" for ln in lines))
    problems = []
    if args.expect_title_substr and args.expect_title_substr.lower() not in title.lower():
        problems.append(f"title missing {args.expect_title_substr!r}: {title}")
    if args.expect_h1_substr:
        blob = " | ".join(headings)
        if args.expect_h1_substr.lower() not in blob.lower():
            problems.append(f"h1 missing {args.expect_h1_substr!r}: {blob}")
    for href in args.expect_href:
        if href not in html:
            problems.append(f"missing href {href}")
    for text in args.expect_text:
        if text not in html:
            problems.append(f"missing text {text!r}")
    if problems:
        for item in problems:
            print(f"PARSE FAIL: {item}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
