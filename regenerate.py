#!/usr/bin/env python3
"""Regenerate the LLM Study Guide from a single in-script manifest.

Running `python3 regenerate.py` will:
  1. Wipe the `chapters/` directory.
  2. Re-create chapter folders from MANIFEST below.
  3. Re-write `glossary.py` to match the new content.
  4. Re-write the curriculum table in `README.md`.
  5. Run `tools/linkify.py` to inject inline glossary links.

The script prints progress for every step so a human can watch it work in the
terminal. It is the source of truth for the guide; hand-edits to chapters/ are
expected to be replaced.

Citation policy: every URL must be open-access (no paywall).
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from _chapter_types import Chapter, Paper, Extra  # noqa: F401

ROOT = os.path.dirname(os.path.abspath(__file__))
CHAPTERS_DIR = os.path.join(ROOT, "chapters")
GLOSSARY_PATH = os.path.join(ROOT, "glossary.py")
README_PATH = os.path.join(ROOT, "README.md")
LINKIFY_PATH = os.path.join(ROOT, "tools", "linkify.py")


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
    out.append(ch.summary_html.strip())
    out.append("")
    if ch.papers:
        out.append("## Papers")
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
    md_path = os.path.join(folder, "chapter.md")
    with open(md_path, "w") as f:
        f.write(render_chapter_md(ch))
    rel = os.path.relpath(md_path, ROOT)
    print(f"[{ch.id:>2}/{total:>2}] wrote {rel}")


# --------------------------------------------------------------------------- #
# Glossary
# --------------------------------------------------------------------------- #

GLOSSARY_PHRASES: list[tuple[str, str]] = [
    # ---- Math foundations
    ("eigenvalue", "https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors"),
    ("eigenvector", "https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors"),
    ("singular value decomposition", "https://en.wikipedia.org/wiki/Singular_value_decomposition"),
    ("SVD", "https://en.wikipedia.org/wiki/Singular_value_decomposition"),
    ("dot product", "https://en.wikipedia.org/wiki/Dot_product"),
    ("matrix multiplication", "https://en.wikipedia.org/wiki/Matrix_multiplication"),
    ("chain rule", "https://en.wikipedia.org/wiki/Chain_rule"),
    ("gradient descent", "https://en.wikipedia.org/wiki/Gradient_descent"),
    ("stochastic gradient descent", "https://en.wikipedia.org/wiki/Stochastic_gradient_descent"),
    ("convex", "https://en.wikipedia.org/wiki/Convex_function"),
    ("KL divergence", "https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence"),
    ("cross-entropy", "https://en.wikipedia.org/wiki/Cross-entropy"),
    ("Bayes", "https://en.wikipedia.org/wiki/Bayes%27_theorem"),
    ("maximum likelihood", "https://en.wikipedia.org/wiki/Maximum_likelihood_estimation"),
    ("information theory", "https://en.wikipedia.org/wiki/Information_theory"),
    ("entropy", "https://en.wikipedia.org/wiki/Entropy_(information_theory)"),
    ("perplexity", "https://en.wikipedia.org/wiki/Perplexity"),
    ("softmax", "https://en.wikipedia.org/wiki/Softmax_function"),

    # ---- Architecture / ideas
    ("perceptron", "https://en.wikipedia.org/wiki/Perceptron"),
    ("backpropagation", "https://en.wikipedia.org/wiki/Backpropagation"),
    ("convolutional neural network", "https://en.wikipedia.org/wiki/Convolutional_neural_network"),
    ("LSTM", "https://en.wikipedia.org/wiki/Long_short-term_memory"),
    ("recurrent neural network", "https://en.wikipedia.org/wiki/Recurrent_neural_network"),
    ("recurrent", "https://en.wikipedia.org/wiki/Recurrent_neural_network"),
    ("ResNet", "https://en.wikipedia.org/wiki/Residual_neural_network"),
    ("batch normalization", "https://en.wikipedia.org/wiki/Batch_normalization"),
    ("self-attention", "https://en.wikipedia.org/wiki/Attention_(machine_learning)"),
    ("transformer", "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"),
    ("Mixture-of-Experts", "https://en.wikipedia.org/wiki/Mixture_of_experts"),
    ("MoE", "https://en.wikipedia.org/wiki/Mixture_of_experts"),
    ("autoregressive", "https://en.wikipedia.org/wiki/Autoregressive_model"),
    ("word embeddings", "https://en.wikipedia.org/wiki/Word_embedding"),
    ("word2vec", "https://en.wikipedia.org/wiki/Word2vec"),
    ("n-gram", "https://en.wikipedia.org/wiki/N-gram"),

    # ---- Models / families
    ("BERT", "https://en.wikipedia.org/wiki/BERT_(language_model)"),
    ("GPT-2", "https://en.wikipedia.org/wiki/GPT-2"),
    ("GPT-3", "https://en.wikipedia.org/wiki/GPT-3"),
    ("Llama", "https://en.wikipedia.org/wiki/Llama_(language_model)"),
    ("Phi", "https://en.wikipedia.org/wiki/Phi_(language_model)"),
    ("CLIP", "https://en.wikipedia.org/wiki/CLIP_(model)"),
    ("AlexNet", "https://en.wikipedia.org/wiki/AlexNet"),
    ("LeNet", "https://en.wikipedia.org/wiki/LeNet"),
    ("InstructGPT", "https://en.wikipedia.org/wiki/InstructGPT"),
    ("ChatGPT", "https://en.wikipedia.org/wiki/ChatGPT"),
    ("DeepSeek", "https://en.wikipedia.org/wiki/DeepSeek"),

    # ---- Concepts
    ("scaling laws", "https://en.wikipedia.org/wiki/Neural_scaling_law"),
    ("in-context learning", "https://en.wikipedia.org/wiki/In-context_learning"),
    ("RLHF", "https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback"),
    ("Chain-of-thought", "https://en.wikipedia.org/wiki/Chain-of-thought_prompting"),
    ("Retrieval-augmented generation", "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"),
    ("RAG", "https://en.wikipedia.org/wiki/Retrieval-augmented_generation"),
    ("LoRA", "https://en.wikipedia.org/wiki/Low-rank_adaptation"),
    ("QLoRA", "https://en.wikipedia.org/wiki/Low-rank_adaptation"),
    ("diffusion", "https://en.wikipedia.org/wiki/Diffusion_model"),
    ("GAN", "https://en.wikipedia.org/wiki/Generative_adversarial_network"),
    ("seq2seq", "https://en.wikipedia.org/wiki/Seq2seq"),

    # ---- Training infra
    ("AdamW", "https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam"),
    ("Adam", "https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam"),
    ("FLOPs", "https://en.wikipedia.org/wiki/FLOPS"),
    ("Quantization", "https://en.wikipedia.org/wiki/Quantization_(signal_processing)"),

    # ---- Evaluation
    ("MMLU", "https://en.wikipedia.org/wiki/Massive_Multitask_Language_Understanding"),
]


def write_glossary() -> None:
    lines = [
        '"""Glossary: maps concepts/acronyms to authoritative, free,',
        'paywall-free explainer URLs. Used by tools/linkify.py.',
        "",
        "Generated by regenerate.py — do not hand-edit; edit the script.",
        '"""',
        "",
        "GLOSSARY: list[tuple[str, str]] = [",
    ]
    for phrase, url in GLOSSARY_PHRASES:
        lines.append(f"    ({phrase!r}, {url!r}),")
    lines.append("]")
    with open(GLOSSARY_PATH, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"[glossary] wrote {os.path.relpath(GLOSSARY_PATH, ROOT)} "
          f"({len(GLOSSARY_PHRASES)} phrases)")


# --------------------------------------------------------------------------- #
# README curriculum block
# --------------------------------------------------------------------------- #

README_TEMPLATE = """# LLM Study Guide

A reproducible study guide on **LLMs and SLMs** for postgraduate CS students,
served by a tiny stdlib-only Python HTTP server. Built so that a single
script — `regenerate.py` — can rebuild the entire content tree from one
in-script manifest.

- **30 chapters** across **3 sections**: math foundations, LLM/SLM overview,
  and the chronological history of ML/AI from the perceptron (1958) to
  inference-time reasoning models (2024–25).
- **Open access only** — every linked paper, lecture note, or article is
  reachable without a paywall.
- Inline **glossary** that hyperlinks first mentions of concepts to free
  explainers (Wikipedia, faculty pages, MIT OCW, 3Blue1Brown).

---

## Quick start

```bash
git clone git@github.com:palmer159/airesearch.git
cd airesearch
python3 server.py            # default port 47314
```

Open <http://127.0.0.1:47314/>.

Requirements: Python 3.10+. No third-party dependencies.

---

## Regenerating the guide

The chapter tree is generated from `regenerate.py`. To rebuild:

```bash
python3 regenerate.py
```

This wipes `chapters/`, rebuilds it from the in-script `MANIFEST`, refreshes
`glossary.py`, updates the curriculum table in this README, and runs the
inline-link injector. Per-chapter progress is printed to stdout.

Edit chapters by editing the entries in `MANIFEST` inside `regenerate.py`,
then re-run the script. Hand edits to `chapters/*` are deliberately
ephemeral.

---

## Curriculum

{curriculum}

---

## Layout

```
airesearch/
├── README.md
├── regenerate.py          # source of truth for chapter content
├── server.py              # HTTP server (renders pages from chapters/)
├── loader.py              # Markdown-with-frontmatter parser
├── glossary.py            # phrase → explainer-URL table (generated)
├── tools/
│   └── linkify.py         # injects glossary links into chapter.md files
└── chapters/              # generated: NN-slug/chapter.md
```

---

## License

Chapter prose and curation: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Python code: MIT. Linked papers and resources retain their original licenses.
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
            out.append(f"{ch.id}. {ch.title}")
        out.append("")
    return "\n".join(out).rstrip()


def write_readme(manifest: list[Chapter]) -> None:
    text = README_TEMPLATE.format(curriculum=render_curriculum(manifest))
    with open(README_PATH, "w") as f:
        f.write(text)
    print(f"[readme]  wrote {os.path.relpath(README_PATH, ROOT)}")


# --------------------------------------------------------------------------- #
# Manifest — authored in three sections
# --------------------------------------------------------------------------- #

# NOTE: MANIFEST is filled out by importing the three section modules below,
# which are colocated in this file (kept inline to keep the regenerator a
# single script).

# Imports of the section authoring modules:
from _content_math import MATH_CHAPTERS         # noqa: E402
from _content_overview import OVERVIEW_CHAPTERS # noqa: E402
from _content_history import HISTORY_CHAPTERS   # noqa: E402

MANIFEST: list[Chapter] = MATH_CHAPTERS + OVERVIEW_CHAPTERS + HISTORY_CHAPTERS


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #

def reset_chapters_dir() -> None:
    if os.path.isdir(CHAPTERS_DIR):
        shutil.rmtree(CHAPTERS_DIR)
        print(f"[wipe]    removed {os.path.relpath(CHAPTERS_DIR, ROOT)}")
    os.makedirs(CHAPTERS_DIR, exist_ok=True)


def run_linkify() -> None:
    print("[linkify] running tools/linkify.py …")
    res = subprocess.run([sys.executable, LINKIFY_PATH], cwd=ROOT)
    if res.returncode != 0:
        raise SystemExit(f"linkify failed with exit {res.returncode}")


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
    print(f"=== regenerate.py ({len(MANIFEST)} chapters) ===")
    validate_manifest(MANIFEST)
    reset_chapters_dir()
    total = len(MANIFEST)
    for ch in MANIFEST:
        write_chapter(ch, total)
    write_glossary()
    write_readme(MANIFEST)
    run_linkify()
    print(f"=== done: {total} chapters regenerated ===")


if __name__ == "__main__":
    main()
