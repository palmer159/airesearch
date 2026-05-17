# Regenerated LLM Study Guide — Design

**Date:** 2026-05-17
**Branch:** `feature/regenerated-study-guide-2026-05-17`
**Mandate:** autonomous execution per user request

## Goal

Replace the current 48-chapter study guide with a re-organized 30-chapter
guide that is reproducible from a single Python script (`regenerate.py`).
Every commit on this work must land on a new feature branch and be made
with `--no-gpg-sign`.

## New structure

The guide has three sections, in this order:

### Section 1 — Math for ML (Chapters 1–3)

Plain-language explainers for the math a postgrad CS student needs before
the rest of the book lands. Every cited reference must be open-access and
free of paywalls (arXiv, Wikipedia, lecture notes from public faculty
pages, MIT OCW, 3Blue1Brown, immersivemath.com, OpenIntro Statistics, MML
book, Cover & Thomas mirrors).

1. Linear algebra you actually use (vectors, matrices, dot products,
   eigen-decomposition, SVD, why GPUs care)
2. Calculus & optimization (derivatives, gradients, chain rule,
   gradient descent, convex vs non-convex, AdamW intuition)
3. Probability, statistics & information theory (random variables,
   Bayes, KL divergence, cross-entropy, MLE — the loss-function backbone)

### Section 2 — Broad overview of LLMs / SLMs and their dependence on math (Chapters 4–6)

A short bridge that turns the math into intuition for what an LLM/SLM is.

4. What is a language model? (probability over sequences, perplexity,
   tokens, scaling intuition)
5. The math under the hood (linear algebra → attention; calculus →
   training; probability → next-token sampling)
6. SLMs vs LLMs (why both exist, economics, on-device, when to choose
   which)

### Section 3 — ML/AI in chronological order (Chapters 7–30)

Twenty-four chapters, each a single key idea, ordered by year of
invention. Each chapter focuses on **only the highlight that mattered**,
not an exhaustive survey.

| # | Year | Chapter |
|---|------|---------|
| 7  | 1958 | Perceptron |
| 8  | 1986 | Backpropagation |
| 9  | 1989 | Convolutional networks (LeNet) |
| 10 | 1997 | LSTM (recurrent networks that worked) |
| 11 | 2003 | Neural language models (Bengio NPLM) |
| 12 | 2012 | AlexNet & the deep-learning ignition |
| 13 | 2013 | Word embeddings (word2vec, GloVe) |
| 14 | 2014 | Seq2seq + attention |
| 15 | 2014 | GANs |
| 16 | 2015 | ResNet & batch normalization |
| 17 | 2017 | The Transformer |
| 18 | 2018 | BERT and the encoder era |
| 19 | 2019 | GPT-2 & the decoder-only paradigm |
| 20 | 2020 | GPT-3, scaling laws, in-context learning |
| 21 | 2020 | Diffusion models (DDPM) |
| 22 | 2021 | CLIP & multimodal contrastive learning |
| 23 | 2022 | InstructGPT, RLHF, ChatGPT |
| 24 | 2022 | Chain-of-thought prompting |
| 25 | 2022 | RAG & retrieval-augmented LLMs |
| 26 | 2023 | LLaMA & the open-weight era |
| 27 | 2023 | LoRA / QLoRA & parameter-efficient fine-tuning |
| 28 | 2024 | Mixture-of-Experts at scale (Mixtral, DeepSeek-V3) |
| 29 | 2024 | Phi & the SLM thesis ("textbooks are all you need") |
| 30 | 2024–25 | Inference-time reasoning (o1, DeepSeek-R1) |

## Architecture

Already in repo: `server.py`, `loader.py`, `glossary.py`,
`tools/linkify.py`, `chapters/NN-slug/chapter.md`. The renderer/loader
contract does not change.

What this work changes:

- **Adds** `regenerate.py` at repo root — a single script that:
  1. Removes `chapters/` entirely.
  2. Iterates over an in-script `MANIFEST` (a Python list of typed
     dicts, one per chapter).
  3. Writes `chapters/NN-slug/chapter.md` for each entry using the
     existing frontmatter + body + Papers + Extras format.
  4. Rewrites `glossary.py` so the linkifier targets are aligned to the
     new content.
  5. Rewrites the curriculum table in `README.md`.
  6. Runs `tools/linkify.py` to inject inline glossary links.
  7. Prints a per-task progress line to stdout (e.g.
     `[ 7/30] writing chapters/07-perceptron/chapter.md` and a final
     summary).
- **Replaces** `chapters/*` content (curated by the script's manifest).
- **Updates** `README.md`'s curriculum section.

## Citation policy

Every URL in the manifest must be open-access. Hard-blocked domains:
`ieeexplore.ieee.org` paywalls, `link.springer.com` paywalls,
`sciencedirect.com` paywalls, `nature.com` non-OA. Allowed: arXiv,
`*.edu` faculty pages, `cdn.openai.com`, `www-cdn.anthropic.com`,
`transformer-circuits.pub`, JMLR, OpenReview, ACL anthology, GitHub,
Wikipedia, `3blue1brown.com`, `immersivemath.com`, OpenIntro,
`mml-book.com`, MIT OCW, Stanford CS229/CS231n/CS224n notes.

Citations are not re-verified by HTTP fetch in this round — the URLs in
the manifest are picked from sources we already verified in the prior
guide (cf. commit `2201335`) plus a small set of textbook/lecture-note
URLs for the new math chapters. The script does not perform link
checking; that remains a separate concern.

## Out of scope

- Fancy diagrams beyond what already renders.
- New server features.
- Re-running the citation-verification crawler.
- Touching `glossary.py`'s linkifier engine; only the phrase table.

## Risks & mitigations

| Risk | Mitigation |
|---|---|
| Math chapter prose drifts into formula-heavy academic style | Authoring instruction explicitly says "plain-language", and uses 3B1B / MML book / immersivemath as reference style. |
| Re-running script destroys hand edits | The script is the source of truth — that is the point. Hand edits to `chapters/` are explicitly meant to be replaced. |
| GPG signing accidentally re-enabled | Every git commit in this branch passes `--no-gpg-sign`. |

## Acceptance

- `python3 regenerate.py` runs to completion with non-zero output and
  exit 0.
- `chapters/` contains exactly 30 chapter folders numbered 01–30.
- `python3 loader.py` reports 30 chapters with non-zero papers count.
- `python3 server.py` starts and `/` returns HTTP 200 listing 30
  chapters under three parts.
- All commits land on `feature/regenerated-study-guide-2026-05-17`,
  none on `main`, all unsigned.
