#!/usr/bin/env python3
"""Derive Quartz page titles from each note's H1.

Quartz v5 takes a page's title from frontmatter and falls back to the filename,
with no config option to prefer the first heading. This runs over the *copied*
content tree at build time so the source vault stays pure Markdown: for any file
without a `title:`, it promotes the leading `# ` heading into frontmatter and
drops that heading from the body (Quartz renders the title as the page heading,
so leaving it would render twice).

Conservative by design - a file is skipped unless it already has no title AND
its first non-blank body line is an H1.
"""

import os
import re
import sys

CONTENT = sys.argv[1]

# Markdown -> plain text, enough for a title string.
SUBS = [
    (re.compile(r"\[\[([^\]|]+)\|([^\]]+)\]\]"), r"\2"),  # [[target|alias]]
    (re.compile(r"\[\[([^\]]+)\]\]"), r"\1"),  # [[target]]
    (re.compile(r"\[([^\]]+)\]\([^)]*\)"), r"\1"),  # [text](url)
    (re.compile(r"\*\*([^*]+)\*\*"), r"\1"),  # bold
    (re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)"), r"\1"),  # italic
    (re.compile(r"`([^`]+)`"), r"\1"),  # code
]


def clean(text):
    for pattern, repl in SUBS:
        text = pattern.sub(repl, text)
    return " ".join(text.split())


def yaml_quote(text):
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def split_frontmatter(lines):
    """Return (frontmatter_lines_including_fences, body_lines)."""
    if lines and lines[0].rstrip() == "---":
        for i in range(1, len(lines)):
            if lines[i].rstrip() == "---":
                return lines[: i + 1], lines[i + 1 :]
    return [], lines


changed = skipped = 0
for root, _, files in os.walk(CONTENT):
    for name in files:
        if not name.endswith(".md"):
            continue
        path = os.path.join(root, name)
        with open(path, encoding="utf-8") as handle:
            lines = handle.read().split("\n")

        front, body = split_frontmatter(lines)
        if any(re.match(r"^title\s*:", line) for line in front):
            skipped += 1
            continue

        first = next((i for i, line in enumerate(body) if line.strip()), None)
        if first is None or not body[first].startswith("# "):
            skipped += 1
            continue

        title = clean(body[first][2:])
        if not title:
            skipped += 1
            continue

        del body[first]
        while first < len(body) and not body[first].strip():
            del body[first]

        entry = f"title: {yaml_quote(title)}"
        front = front[:1] + [entry] + front[1:] if front else ["---", entry, "---", ""]

        with open(path, "w", encoding="utf-8") as handle:
            handle.write("\n".join(front + body))
        changed += 1

print(f"titles injected: {changed}, skipped: {skipped}")
