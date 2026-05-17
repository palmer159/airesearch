# Implementation Plan — Regenerated LLM Study Guide

**Spec:** `docs/superpowers/specs/2026-05-17-regenerated-study-guide-design.md`
**Branch:** `feature/regenerated-study-guide-2026-05-17`

## Tasks

### T1 — Wire up regenerate.py skeleton (sequential)
- New file `regenerate.py` at repo root.
- Defines a `Chapter` dataclass: `id, slug, part, title, summary_html,
  papers (list of dicts), extras (list of dicts)`.
- Defines a top-level `MANIFEST: list[Chapter]` (initially empty).
- Defines `write_chapter(ch)`, `write_glossary(phrases)`,
  `write_readme(manifest)`, `run_linkify()`, `main()`.
- `main()` prints per-step progress to the terminal:
  `[ N/30] writing chapters/NN-slug/chapter.md`.
- Wipes `chapters/` and `glossary.py` before writing.

### T2 — Author Section 1 (Math), parallel subagent
Three chapters of plain-language math with open-access references only.
Returns Python `Chapter(...)` literals ready to paste into MANIFEST.
Subagent: `general-purpose`.

### T3 — Author Section 2 (LLM/SLM overview), parallel subagent
Three bridge chapters connecting math → LLMs/SLMs.
Subagent: `general-purpose`.

### T4 — Author Section 3 (chronological), parallel subagent
24 chapters in invention order, each focused on one key idea.
Subagent: `general-purpose`. Reuses URLs already verified in commit
`2201335` so we don't have to re-crawl.

### T5 — Assemble MANIFEST, write glossary phrases, run script
Paste the three subagents' outputs into `regenerate.py`. Run it.
Verify chapter count, run `python3 loader.py`, smoke `server.py`.

### T6 — Commit on feature branch with `--no-gpg-sign`
Single commit:
- new `regenerate.py`
- regenerated `chapters/`
- updated `glossary.py`
- updated `README.md`
- new `docs/superpowers/specs/...` and `docs/superpowers/plans/...`

## Order

T1 sequential first.
T2 + T3 + T4 dispatched in parallel as three subagents.
T5 after all three return.
T6 last.

## Subagent prompts

Each subagent will receive: the spec, the chapter loader format
(showing exactly how `chapter.md` is parsed), the citation policy, an
example `Chapter(...)` Python literal, and the list of chapters they own.
The subagent returns ONLY the `Chapter(...)` literals as plain text — no
file writes.
