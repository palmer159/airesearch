---
id: 48
title: How to Read a Paper, Reproduce, and Stay Current
part: XII. Research Frontier
---

<p>A practical operating manual for the postgrad practitioner who has to keep up while shipping.</p>

<h4>Reading</h4>
<ol>
  <li>First pass: title, abstract, intro, last sentence of each section, conclusion. 10 minutes.</li>
  <li>Second pass: figures (especially Fig 1 and the main results table), method outline. 30 minutes.</li>
  <li>Third pass: read for the gotcha — eval contamination, missing baselines, hyperparameter cherry-picking, ablation gaps.</li>
</ol>
<h4>Reproducing</h4>
<ul>
  <li>Prefer official code; otherwise <code>nanoGPT</code>, <code>llm.c</code>, <code>tinygrad</code>, or <code>HF transformers</code>.</li>
  <li>Get a tiny model training on your laptop in &lt;10 minutes before you spin GPUs.</li>
  <li>Match a reported number on a small subset before you scale.</li>
</ul>
<h4>Staying current</h4>
<ul>
  <li>arXiv-sanity, Hugging Face Daily Papers, Papers With Code, AlphaXiv.</li>
  <li>Follow specific researchers on GitHub and X — signal density beats most newsletters.</li>
  <li>Track conferences: NeurIPS / ICML / ICLR / ACL / EMNLP / NAACL; for systems: MLSys, SOSP, OSDI.</li>
  <li>Once a quarter: re-read one foundational paper to keep your prior calibrated.</li>
</ul>

## Papers

### How to Read a Paper
- **Authors:** Srinivasan Keshav
- **Year:** 2007
- **URL:** https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf

The classic three-pass method. Five pages; the highest ROI five pages in your career.

### nanoGPT
- **Authors:** Andrej Karpathy
- **Year:** 2022
- **Venue:** code
- **URL:** https://github.com/karpathy/nanoGPT

Minimal-but-real GPT pretraining + finetuning code. The right starting point for hands-on learning.

### Let's build GPT: from scratch, in code, spelled out
- **Authors:** Andrej Karpathy
- **Year:** 2023
- **Venue:** video
- **URL:** https://www.youtube.com/watch?v=kCc8FmEb1nY

Two-hour, line-by-line GPT build. The single best lecture on transformers.

## Extras

- [Hugging Face Daily Papers](https://huggingface.co/papers)
- [arXiv cs.CL (NLP)](https://arxiv.org/list/cs.CL/recent)
- [Papers With Code](https://paperswithcode.com/)
- [Anthropic Research](https://www.anthropic.com/research)
- [OpenAI Research (archive)](https://web.archive.org/web/2026/https://openai.com/research/)
- [Google DeepMind Research](https://deepmind.google/research/)
