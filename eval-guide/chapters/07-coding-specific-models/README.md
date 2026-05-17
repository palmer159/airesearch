---
id: 7
title: Coding-Specific Open Models: Code Llama, StarCoder, DeepSeek-Coder, Qwen-Coder
part: II. The Open Model Landscape
---

# Coding-Specific Open Models: Code Llama, StarCoder, DeepSeek-Coder, Qwen-Coder

*II. The Open Model Landscape*

<p>General-purpose models can write code, but coding-specific families
consistently beat their general siblings on programming benchmarks at the
same parameter count — because they're trained on much more code, with
training objectives that match how code is actually edited.  If your
benchmark target is code, start here.</p>

<h4>Code Llama (Meta)</h4>
<p><a href="https://arxiv.org/abs/2308.12950" target="_blank" rel="noopener">Code Llama</a>
extends Llama 2 with extra training on a code-heavy mix.  Sizes: 7B, 13B,
34B, and 70B.  Variants exist for instruction following and Python
specifically.  The paper introduces fill-in-the-middle (FIM) and long-context
training (up to 100k tokens) at scale — both directly relevant for IDE-style
completion benchmarks.  License: Llama Community.</p>

<h4>StarCoder 2 (BigCode)</h4>
<p><a href="https://arxiv.org/abs/2402.19173" target="_blank" rel="noopener">StarCoder 2</a>
is the fully-open coding model: weights, training data (The Stack v2), and
training code are all released.  Sizes: 3B, 7B, 15B.  Trained on ~600
programming languages with FIM and repository-level context.  This is the
right choice when you want a coding model for research where reproducibility
matters; the
<a href="https://huggingface.co/bigcode/starcoder2-15b" target="_blank" rel="noopener">15B model card</a>
links the data and training pipeline.</p>

<h4>DeepSeek-Coder and DeepSeek-Coder-V2</h4>
<p><a href="https://arxiv.org/abs/2401.14196" target="_blank" rel="noopener">DeepSeek-Coder</a>
(1.3B / 6.7B / 33B) was the first family to seriously challenge Code Llama
on open benchmarks; the recipe leaned on repository-level training and FIM.
<a href="https://arxiv.org/abs/2406.11931" target="_blank" rel="noopener">DeepSeek-Coder-V2</a>
goes MoE: 236B parameters total with 21B active per token, plus a smaller
16B / 2.4B-active "lite" variant.  V2 is competitive with much larger
closed models on code benchmarks while staying open-weight.</p>

<h4>Qwen2.5-Coder</h4>
<p><a href="https://arxiv.org/abs/2409.12186" target="_blank" rel="noopener">Qwen2.5-Coder</a>
ships at 0.5B, 1.5B, 3B, 7B, 14B, and 32B — the same generous size ladder
as the base Qwen family but specialized on code.  The 32B variant is, as of
late 2024, the strongest open-weight code model on most public benchmarks.
Apache 2.0 for most sizes.</p>

<h4>What makes a "code model" different</h4>
<ul>
  <li><b>Fill-in-the-middle (FIM).</b>  Code isn't written start-to-end —
      you edit a function in the middle of a file.  FIM training reorders
      sequences so the model learns to predict a span given both prefix
      and suffix context.  This is what powers good IDE autocomplete.</li>
  <li><b>Repository-level training.</b>  Instead of treating each file
      independently, training packs related files from the same repo
      together, so the model sees the kind of cross-file context a real
      project has.</li>
  <li><b>Long-context training.</b>  100k+ token windows let the model
      reason about whole files or small repos at once.</li>
  <li><b>Multi-language coverage.</b>  StarCoder 2 hits ~600 languages;
      Code Llama and DeepSeek-Coder cover the main 80–100 carefully.</li>
</ul>

<p>You'll see HumanEval and MBPP cited everywhere as the public-benchmark
shorthand for "this model can code."  We'll dig into what those benchmarks
actually measure (and how they fail) in Section IV — for now, just know
that all four families above are at or near the top of the open-weight
leaderboards.</p>

## Papers and references

### Code Llama: Open Foundation Models for Code
- **Authors:** Rozière et al. (Meta)
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2308.12950

The reference open-weight code-model report. Fill-in-the-middle, long-context training, and Python-specialist variants are all introduced cleanly.

### StarCoder 2 and The Stack v2
- **Authors:** Lozhkov et al. (BigCode)
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2402.19173

Fully-open code model: weights, training data, and training code are all released. The right baseline when reproducibility matters.

### DeepSeek-Coder: When the Large Language Model Meets Programming
- **Authors:** Guo et al. (DeepSeek-AI)
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2401.14196

The original DeepSeek-Coder family. Notable for repository-level training and very strong HumanEval / MBPP numbers at 6.7B and 33B.

### DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence
- **Authors:** DeepSeek-AI
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2406.11931

236B-parameter MoE (21B active) plus a 16B-lite variant. The first open-weight family to credibly close the gap to closed code models.

### Qwen2.5-Coder Technical Report
- **Authors:** Qwen Team, Alibaba
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2409.12186

Code-specialized Qwen2.5 across 0.5B–32B. The 32B is the standout open-weight code model at the time of writing.

## Extras
- [bigcode/starcoder2-15b model card](https://huggingface.co/bigcode/starcoder2-15b)
- [DeepSeek-Coder org on Hugging Face](https://huggingface.co/deepseek-ai)
- [Qwen2.5-Coder collection on Hugging Face](https://huggingface.co/Qwen)
