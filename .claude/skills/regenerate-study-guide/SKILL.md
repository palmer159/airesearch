---
name: regenerate-study-guide
description: |
  Regenerate the airesearch LLM Study Guide from its in-script manifest so the
  on-disk content (chapters/, glossary.py, README.md) matches the latest
  authored version. Use when the user asks to "regenerate the study guide",
  "rebuild chapters", "refresh the LLM study guide", "run regenerate.py", or
  any phrasing that means "produce the latest version of this guide on my
  machine right now". Runs `python3 regenerate.py` in the repo root and prints
  per-chapter progress.
---

# Regenerate Study Guide

Rebuild the entire airesearch LLM Study Guide (math foundations + LLM/SLM
overview + chronological ML/AI history) from `regenerate.py`'s in-script
manifest. The script is the source of truth — it wipes `chapters/`, recreates
all 30 chapter `README.md` files, refreshes `glossary.py`, rewrites the
top-level `README.md`, and runs the inline glossary linkifier.

## When to invoke

Trigger phrases:
- "regenerate the study guide"
- "rebuild the chapters"
- "refresh the LLM study guide"
- "produce the latest version of the guide"
- "run regenerate.py"
- "rerun the guide generator"
- "I just edited a chapter — rebuild"

Do NOT invoke for unrelated requests (e.g. starting the server, editing one
chapter by hand, fixing a typo). Those don't need a full regeneration unless
the user asks for one.

## Prerequisites

- Working directory contains `regenerate.py` at repo root
  (i.e. you are inside a clone of `palmer159/airesearch` or a fork)
- `python3` 3.10+ on PATH
- No third-party Python deps required

If `regenerate.py` is missing, tell the user the skill must be run from inside
the airesearch repo and stop.

## Procedure

1. **Verify location.** From the cwd, confirm `regenerate.py`, `loader.py`,
   `_chapter_types.py`, `_content_math.py`, `_content_overview.py`, and
   `_content_history.py` all exist. If any are missing, abort with a clear
   message.
2. **Run the generator.** Execute:
   ```bash
   python3 regenerate.py
   ```
   The script prints `[NN/30] wrote chapters/NN-slug/README.md` lines as it
   works, plus `[glossary]`, `[readme]`, and `[linkify]` lines. Surface that
   progress to the user — do not suppress it.
3. **Verify the output.** After it returns:
   ```bash
   python3 loader.py
   ```
   should report `loaded 30 chapters` with non-zero papers. If the count is
   wrong, investigate before reporting success.
4. **Optional smoke check (only if user asks).** Start the local server:
   ```bash
   python3 server.py 51829
   ```
   Hit `http://127.0.0.1:51829/health` — should return
   `{"ok": true, "chapters": 30}`. Kill the server when done.
5. **Report.** Tell the user how many chapters were written, that the glossary
   and top-level README were refreshed, and that linkify ran.

## Editing content

The skill is for *running* the generator, not editing content. To change a
chapter, edit `_content_math.py` / `_content_overview.py` /
`_content_history.py` — those modules are the inputs to `regenerate.py`. After
editing, re-invoke this skill to apply the change.

## What this skill does NOT do

- It does not commit or push. Commit decisions are the user's. If the user
  also wants to commit, commit separately following normal git practice.
- It does not check link health or validate citations against the live web.
  That is a separate concern handled by an external citation-verification
  pass.
- It does not modify the server, loader, or linkifier code. Those are
  framework, not content.

## Troubleshooting

- **`ImportError: cannot import name MATH_CHAPTERS`** — the content modules
  must be importable from the repo root. Run from the repo root, not from a
  subdirectory.
- **Loader reports fewer than 30 chapters** — `regenerate.py` partially
  failed. Re-run; if it persists, inspect the section content modules for a
  Python syntax error.
- **`linkify` step fails** — `glossary.py` or a chapter `README.md` is
  malformed. Check the latest changes to `GLOSSARY_PHRASES` in
  `regenerate.py`.
