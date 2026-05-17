---
id: 6
title: SLMs vs LLMs: When to Choose Which
part: II. LLMs and SLMs: What and Why
---

<p>The default 2026 conversation in any engineering org goes: "do we use a
frontier model or a small one?"  This chapter gives you the framing.  There's
no universal answer — but the trade-offs are surprisingly clean once you see
them.</p>

<h4>What's an SLM?</h4>
<p>An <b>SLM</b> (small language model) is, by rough community convention, a
model with up to about 7B parameters — small enough to serve on a single
modern GPU, sometimes on a phone or laptop.  The "small" is relative: a 7B
model in 2026 is wildly more capable than a 175B model from 2020, thanks to
better data, better recipes, and Chinchilla-style training.  Names you'll see
on benchmarks: <a href="https://arxiv.org/abs/2306.11644" target="_blank" rel="noopener">Phi</a>,
<a href="https://huggingface.co/google/gemma-2-2b" target="_blank" rel="noopener">Gemma</a>,
<a href="https://arxiv.org/abs/2407.21783" target="_blank" rel="noopener">Llama-3 8B</a>,
and the
<a href="https://huggingface.co/blog/smollm" target="_blank" rel="noopener">SmolLM</a> family.</p>

<h4>The economics</h4>
<ul>
  <li><b>Inference cost</b> scales roughly with parameters and context length.
      A 7B model is ~25× cheaper per token than a 175B-class one and an
      order of magnitude cheaper than frontier models.</li>
  <li><b>Latency</b> is the killer dimension for UX.  Sub-second
      time-to-first-token typically requires either a small model or
      heavy caching infrastructure.</li>
  <li><b>On-device</b> matters when data can't leave the device — health,
      keyboards, enterprise search over confidential corpora.  Only SLMs
      fit there today.</li>
  <li><b>Operational simplicity</b> — one GPU, no sharding, no
      multi-node coordination, no custom inference stack.</li>
</ul>

<h4>When the LLM is the right tool</h4>
<p>Use a frontier LLM when the task needs broad world knowledge, long-horizon
reasoning, or the long tail of language and code that small models simply
haven't seen enough of.  Multi-step agentic workflows, novel-domain code
generation, complex analysis with many constraints — these still favor the
big models, often by a lot.</p>

<h4>When the SLM is the right tool</h4>
<ul>
  <li>The task is narrow and you can either fine-tune or prompt it tightly:
      classification, extraction, routing, summarization of in-domain text.</li>
  <li>Latency or cost dominates the product requirement.</li>
  <li>You need on-device or air-gapped deployment.</li>
  <li>You can put the LLM behind the SLM as a fallback — a router pattern that
      sends only the hard cases up.</li>
</ul>

<h4>The honest summary</h4>
<p>Quality scales with size, but utility scales with capability per dollar at
your latency budget.  For a lot of production workloads in 2026 the right
answer is a fine-tuned 7B model with the option to escalate — not the most
expensive thing on the menu.</p>

## Papers

### Textbooks Are All You Need (Phi-1)
- **Authors:** Gunasekar et al.
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2306.11644

The paper that kicked off the small-but-strong era. A 1.3B model trained on curated 'textbook-quality' data competes with much larger models on code.

### The Llama 3 Herd of Models
- **Authors:** Llama Team, Meta
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.21783

The reference open-weights family. The 8B variant is the standard SLM baseline; the report itself is one of the most useful training-recipe documents in the open literature.

### Training Compute-Optimal Large Language Models (Chinchilla)
- **Authors:** Hoffmann et al.
- **Year:** 2022
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2203.15556

The reason small models got good. For a fixed compute budget, train a smaller model on more tokens — and SLMs benefit the most from that correction.

### Scaling Laws for Neural Language Models
- **Authors:** Kaplan et al.
- **Year:** 2020
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2001.08361

The original scaling-laws paper. Read it alongside Chinchilla to see what changed and why 'bigger is always better' was incomplete.

### SmolLM: blazingly fast and remarkably powerful
- **Authors:** Hugging Face
- **Year:** 2024
- **Venue:** HF blog
- **URL:** https://huggingface.co/blog/smollm

A clear case study: 135M / 360M / 1.7B models trained on a curated open dataset. Excellent reading on what 'small' means in practice and where it breaks.

## Extras
- [Hugging Face: Llama-3 8B Instruct model card](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
- [Hugging Face: Gemma-2 2B model card](https://huggingface.co/google/gemma-2-2b)
- [Hugging Face: SmolLM2 collection](https://huggingface.co/blog/smollm)
