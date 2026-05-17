"""Load chapter Markdown files from ./chapters/ at server startup.

Each chapter file looks like:

    ---
    id: 1
    title: From n-grams to Neural LMs: A Brief History
    part: I. Foundations
    ---

    <body HTML/markdown — passed through verbatim into the page>

    ## Papers

    ### Title of paper
    - **Authors:** ...
    - **Year:** 2017
    - **Venue:** NeurIPS         (optional)
    - **URL:** https://...

    Free-form summary paragraph.

    ### Next paper
    ...

    ## Extras
    - [Label](https://url)
    - [Label2](https://url2)

The parser is deliberately tiny — no third-party Markdown lib — because the body
content is already authored in HTML and we only need structured Papers/Extras.
"""

from __future__ import annotations

import os
import re
from typing import Any

CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), "chapters")

_FRONTMATTER_RX = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    m = _FRONTMATTER_RX.match(text)
    if not m:
        raise ValueError("missing frontmatter")
    fm_block, rest = m.group(1), m.group(2)
    fm: dict[str, Any] = {}
    for line in fm_block.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    if "id" in fm:
        fm["id"] = int(fm["id"])
    return fm, rest


def _split_sections(body: str) -> tuple[str, str, str]:
    """Return (summary, papers_section, extras_section). Each section is
    everything between its `## Heading` line and the next `## ` line (or EOF)."""
    # Find positions of top-level section headings.
    headings = [(m.start(), m.group(1)) for m in re.finditer(r"^## (.+)$", body, re.MULTILINE)]
    if not headings:
        return body.strip(), "", ""
    summary = body[: headings[0][0]].strip()
    papers, extras = "", ""
    for i, (pos, name) in enumerate(headings):
        end = headings[i + 1][0] if i + 1 < len(headings) else len(body)
        chunk = body[pos:end]
        # strip the heading line
        chunk = re.sub(r"^## .+\n?", "", chunk, count=1)
        if name.strip().lower() == "papers":
            papers = chunk
        elif name.strip().lower() == "extras":
            extras = chunk
    return summary, papers, extras


_PAPER_FIELD_RX = re.compile(r"^- \*\*(\w+):\*\*\s*(.+)$", re.MULTILINE)


def _parse_papers(papers_section: str) -> list[dict]:
    if not papers_section.strip():
        return []
    blocks = re.split(r"^### (.+)$", papers_section, flags=re.MULTILINE)
    # split returns: [pre, title1, body1, title2, body2, ...]
    out: list[dict] = []
    for i in range(1, len(blocks), 2):
        title = blocks[i].strip()
        body = blocks[i + 1] if i + 1 < len(blocks) else ""
        fields = {m.group(1).lower(): m.group(2).strip() for m in _PAPER_FIELD_RX.finditer(body)}
        # summary = everything after the field block (lines that don't match the field pattern)
        # Strip the leading bulleted block and any blank lines.
        body_lines = body.splitlines()
        # Drop leading bullet lines + trailing/leading blanks.
        idx = 0
        while idx < len(body_lines) and (body_lines[idx].startswith("- **") or not body_lines[idx].strip()):
            idx += 1
        summary = "\n".join(body_lines[idx:]).strip()
        paper = {
            "title": title,
            "authors": fields.get("authors", ""),
            "year": fields.get("year", ""),
            "url": fields.get("url", ""),
            "summary": summary,
        }
        if "venue" in fields:
            paper["venue"] = fields["venue"]
        out.append(paper)
    return out


_LINK_RX = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)\s*$", re.MULTILINE)


def _parse_extras(extras_section: str) -> list[dict]:
    return [{"label": m.group(1), "url": m.group(2)} for m in _LINK_RX.finditer(extras_section)]


def load_chapter(path: str) -> dict:
    with open(path) as f:
        text = f.read()
    fm, body = _parse_frontmatter(text)
    summary, papers_section, extras_section = _split_sections(body)
    ch = {
        "id": fm["id"],
        "title": fm["title"],
        "part": fm["part"],
        "summary": summary,
        "papers": _parse_papers(papers_section),
        "extras": _parse_extras(extras_section),
        "_path": path,
    }
    return ch


def load_all_chapters(directory: str = CHAPTERS_DIR) -> list[dict]:
    chapters: list[dict] = []
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"chapters directory not found: {directory}")
    for name in sorted(os.listdir(directory)):
        sub = os.path.join(directory, name)
        if not os.path.isdir(sub):
            continue
        md = os.path.join(sub, "README.md")
        if not os.path.isfile(md):
            continue
        chapters.append(load_chapter(md))
    chapters.sort(key=lambda c: c["id"])
    return chapters


if __name__ == "__main__":
    chs = load_all_chapters()
    print(f"loaded {len(chs)} chapters")
    total_papers = sum(len(c["papers"]) for c in chs)
    total_extras = sum(len(c["extras"]) for c in chs)
    print(f"  papers: {total_papers}")
    print(f"  extras: {total_extras}")
    print()
    print("first chapter sample:")
    c = chs[0]
    print(f"  id={c['id']} part={c['part']}")
    print(f"  title={c['title']}")
    print(f"  summary[:120]={c['summary'][:120]!r}")
    print(f"  papers[0]={c['papers'][0]['title']!r} -> {c['papers'][0]['url']}")
