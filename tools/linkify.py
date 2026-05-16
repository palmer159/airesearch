#!/usr/bin/env python3
"""Inject glossary hyperlinks into the summary section of every chapter.md.

Rules:
  • Only the summary section (everything before the first `## ` heading) is
    modified — Papers/Extras already have authoritative URLs.
  • For each (phrase, url) in glossary.GLOSSARY, the FIRST matching token
    in each chapter's summary is wrapped in an <a> tag.
  • Skip insertion inside <a>…</a>, <pre>…</pre>, <code>…</code>, and
    inside HTML attributes.
  • Idempotent: re-running won't double-wrap, because we explicitly skip
    text inside any <a>.

Run:
    python3 tools/linkify.py
"""

from __future__ import annotations

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from glossary import GLOSSARY  # noqa: E402

CHAPTERS_DIR = os.path.join(ROOT, "chapters")

# Tags whose text content we MUST NOT modify.
SKIP_TAG_RX = re.compile(r"<(a|pre|code)\b[^>]*>.*?</\1>", re.IGNORECASE | re.DOTALL)

FRONTMATTER_RX = re.compile(r"^(---\s*\n.*?\n---\s*\n)(.*)$", re.DOTALL)
PAPERS_HEADING_RX = re.compile(r"\n## ", re.IGNORECASE)


def _split_protected(text: str) -> list[tuple[str, bool]]:
    """Return [(chunk, is_protected), ...] so we only linkify in unprotected parts."""
    parts: list[tuple[str, bool]] = []
    last = 0
    for m in SKIP_TAG_RX.finditer(text):
        if m.start() > last:
            parts.append((text[last:m.start()], False))
        parts.append((m.group(0), True))
        last = m.end()
    if last < len(text):
        parts.append((text[last:], False))
    return parts


def _linkify_unprotected(chunk: str, phrase: str, url: str) -> tuple[str, bool]:
    """Replace the first occurrence of `phrase` in `chunk` with an <a> link.
    Word-boundary semantics: the phrase must not be sandwiched against
    other word characters (so 'CLIP' doesn't match 'CLIPPED').
    Returns (new_chunk, replaced)."""
    pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(phrase) + r"(?![A-Za-z0-9])")
    m = pattern.search(chunk)
    if not m:
        return chunk, False
    matched = m.group(0)
    replacement = f'<a href="{url}" target="_blank" rel="noopener">{matched}</a>'
    return chunk[:m.start()] + replacement + chunk[m.end():], True


def linkify_summary(summary: str) -> tuple[str, list[str]]:
    """Apply every glossary entry once to the summary text.
    Returns the new summary and the list of phrases inserted (for logging)."""
    inserted: list[str] = []
    for phrase, url in GLOSSARY:
        parts = _split_protected(summary)
        # Walk parts, replace in the first unprotected chunk that contains the phrase.
        # If the phrase URL is already present anywhere in the summary, skip
        # (idempotency / glossary URL clash).
        if url in summary:
            continue
        out: list[str] = []
        replaced = False
        for chunk, protected in parts:
            if not replaced and not protected:
                new_chunk, did = _linkify_unprotected(chunk, phrase, url)
                out.append(new_chunk)
                if did:
                    replaced = True
                    inserted.append(phrase)
            else:
                out.append(chunk)
        summary = "".join(out)
    return summary, inserted


def process_file(path: str) -> int:
    with open(path) as f:
        full = f.read()
    m = FRONTMATTER_RX.match(full)
    if not m:
        return 0
    fm, body = m.group(1), m.group(2)

    # Body is summary + (optional) ## sections. Split at the first '## ' line.
    h = PAPERS_HEADING_RX.search(body)
    if h:
        summary, rest = body[: h.start() + 1], body[h.start() + 1 :]
    else:
        summary, rest = body, ""

    new_summary, inserted = linkify_summary(summary)
    if not inserted:
        return 0
    new_full = fm + new_summary + rest
    with open(path, "w") as f:
        f.write(new_full)
    print(f"  + {os.path.basename(os.path.dirname(path))}: {', '.join(inserted)}")
    return len(inserted)


def main() -> None:
    total_files = 0
    total_links = 0
    for name in sorted(os.listdir(CHAPTERS_DIR)):
        d = os.path.join(CHAPTERS_DIR, name)
        if not os.path.isdir(d):
            continue
        md = os.path.join(d, "chapter.md")
        if not os.path.isfile(md):
            continue
        n = process_file(md)
        if n:
            total_files += 1
            total_links += n
    print(f"\nDone: {total_links} links inserted across {total_files} chapters.")


if __name__ == "__main__":
    main()
