#!/usr/bin/env python3
"""Regenerate the *Eval Guide* — a study guide on how to test and benchmark
open-source / open-weight SLMs and LLMs, with a focus on coding agents and
SWE benchmarks.

This is a sibling to the top-level `regenerate.py` and produces content under
`eval-guide/chapters/` from an in-script manifest. Running:

    python3 eval-guide/regenerate.py

will:
  1. Wipe `eval-guide/chapters/`.
  2. Write one `README.md` per chapter under `NN-slug/`.
  3. Write `eval-guide/README.md` with the curriculum table.

The eval guide is intentionally self-contained — it does not share state with
the main study guide's renderer or glossary. Hand edits to chapter files are
ephemeral; the source of truth is this script + content modules.
"""

from __future__ import annotations

import os
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
README_PATH = os.path.join(ROOT, "README.md")

# Make local imports work when run via `python3 eval-guide/regenerate.py`.
sys.path.insert(0, ROOT)

from _chapter_types import Chapter, Paper, Extra  # noqa: E402,F401
from _content_foundations import FOUNDATIONS_CHAPTERS  # noqa: E402
from _content_models import MODELS_CHAPTERS  # noqa: E402
from _content_general_benchmarks import GENERAL_BENCH_CHAPTERS  # noqa: E402
from _content_coding_benchmarks import CODING_BENCH_CHAPTERS  # noqa: E402
from _content_methodology import METHODOLOGY_CHAPTERS  # noqa: E402


MANIFEST: list[Chapter] = (
    FOUNDATIONS_CHAPTERS
    + MODELS_CHAPTERS
    + GENERAL_BENCH_CHAPTERS
    + CODING_BENCH_CHAPTERS
    + METHODOLOGY_CHAPTERS
)


# --------------------------------------------------------------------------- #
# Renderers
# --------------------------------------------------------------------------- #

def render_chapter_md(ch: Chapter) -> str:
    out: list[str] = []
    out.append("---")
    out.append(f"id: {ch.id}")
    out.append(f"title: {ch.title}")
    out.append(f"part: {ch.part}")
    out.append("---")
    out.append("")
    out.append(f"# {ch.title}")
    out.append("")
    out.append(f"*{ch.part}*")
    out.append("")
    out.append(ch.summary_html.strip())
    out.append("")
    if ch.papers:
        out.append("## Papers and references")
        out.append("")
        for p in ch.papers:
            out.append(f"### {p.title}")
            out.append(f"- **Authors:** {p.authors}")
            out.append(f"- **Year:** {p.year}")
            if p.venue:
                out.append(f"- **Venue:** {p.venue}")
            out.append(f"- **URL:** {p.url}")
            out.append("")
            out.append(p.summary.strip())
            out.append("")
    if ch.extras:
        out.append("## Extras")
        for e in ch.extras:
            out.append(f"- [{e.label}]({e.url})")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def write_chapter(ch: Chapter, total: int) -> None:
    folder = os.path.join(CHAPTERS_DIR, f"{ch.id:02d}-{ch.slug}")
    os.makedirs(folder, exist_ok=True)
    md_path = os.path.join(folder, "README.md")
    with open(md_path, "w") as f:
        f.write(render_chapter_md(ch))
    rel = os.path.relpath(md_path, ROOT)
    print(f"[{ch.id:>2}/{total:>2}] wrote {rel}")


# --------------------------------------------------------------------------- #
# README curriculum block
# --------------------------------------------------------------------------- #

README_TEMPLATE = """# Eval Guide: Testing and Benchmarking Open SLMs and LLMs

A companion study guide to the main airesearch LLM Study Guide, focused on
**how to test and benchmark open-source and open-weight SLMs and LLMs** —
with extra depth on **coding agents** and **software-engineering benchmarks**.

It is organized into **5 sections** and **{n_chapters} chapters total**:

1. **Foundations of evaluation** — what we measure, why it's hard, the
   contamination problem, and the difference between capability and behavior.
2. **The model landscape** — open-source and open-weight families to test
   (Llama, Qwen, DeepSeek, Mistral, Gemma, Phi, SmolLM, plus coding-specific
   models like StarCoder and Code Llama).
3. **General-purpose benchmarks** — MMLU, MMLU-Pro, GPQA, BBH, IFEval, GSM8K,
   MATH, ARC, HellaSwag — what each one actually tests and how to read the
   numbers.
4. **Coding and SWE benchmarks** — HumanEval, MBPP, LiveCodeBench, BigCodeBench,
   SWE-bench (Verified, Lite, Live), CodeContests, MultiPL-E, ClassEval — and
   how to set up a coding-agent harness.
5. **Methodology** — running evals, prompting & few-shot, sampling & temperature,
   reproducibility, statistical significance, leaderboards, contamination
   defense, and a benchmark-shopping checklist.

Every reference is open-access. No paywalls.

## Quick start

The eval guide is regenerated from `regenerate.py`:

```bash
python3 eval-guide/regenerate.py
```

This wipes `eval-guide/chapters/`, recreates each chapter's `README.md`, and
rewrites this file. Per-chapter progress prints to stdout.

To browse: each `eval-guide/chapters/NN-slug/` directory contains a
`README.md` that GitHub renders inline when you click into the folder.

## Curriculum

{curriculum}

## License

Chapter prose: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Linked papers and resources retain their original licenses.
"""


def render_curriculum(manifest: list[Chapter]) -> str:
    parts: dict[str, list[Chapter]] = {}
    order: list[str] = []
    for ch in manifest:
        if ch.part not in parts:
            parts[ch.part] = []
            order.append(ch.part)
        parts[ch.part].append(ch)
    out: list[str] = []
    for part in order:
        out.append(f"### {part}")
        out.append("")
        for ch in parts[part]:
            slug = f"{ch.id:02d}-{ch.slug}"
            out.append(f"{ch.id}. [{ch.title}](chapters/{slug}/)")
        out.append("")
    return "\n".join(out).rstrip()


def write_readme(manifest: list[Chapter]) -> None:
    text = README_TEMPLATE.format(
        n_chapters=len(manifest),
        curriculum=render_curriculum(manifest),
    )
    with open(README_PATH, "w") as f:
        f.write(text)
    print(f"[readme]  wrote {os.path.relpath(README_PATH, ROOT)}")


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #

def reset_chapters_dir() -> None:
    if os.path.isdir(CHAPTERS_DIR):
        shutil.rmtree(CHAPTERS_DIR)
        print(f"[wipe]    removed {os.path.relpath(CHAPTERS_DIR, ROOT)}")
    os.makedirs(CHAPTERS_DIR, exist_ok=True)


def validate_manifest(manifest: list[Chapter]) -> None:
    seen_ids: set[int] = set()
    for ch in manifest:
        if ch.id in seen_ids:
            raise SystemExit(f"duplicate chapter id: {ch.id}")
        seen_ids.add(ch.id)
    expected = list(range(1, len(manifest) + 1))
    actual = [ch.id for ch in manifest]
    if actual != expected:
        raise SystemExit(
            f"chapter ids must be 1..N contiguous; got {actual}, expected {expected}"
        )


def main() -> None:
    print(f"=== eval-guide regenerate.py ({len(MANIFEST)} chapters) ===")
    validate_manifest(MANIFEST)
    reset_chapters_dir()
    total = len(MANIFEST)
    for ch in MANIFEST:
        write_chapter(ch, total)
    write_readme(MANIFEST)
    print(f"=== done: {total} chapters regenerated ===")


if __name__ == "__main__":
    main()
