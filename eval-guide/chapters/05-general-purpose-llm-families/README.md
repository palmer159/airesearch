---
id: 5
title: General-Purpose Open Models: Llama, Qwen, DeepSeek, Mistral, Gemma
part: II. The Open Model Landscape
---

# General-Purpose Open Models: Llama, Qwen, DeepSeek, Mistral, Gemma

*II. The Open Model Landscape*

<p>If you're picking one general-purpose open model to benchmark, you'll be
choosing among five families.  This is the short tour: who makes them, what
sizes ship, what they're known for, and where to download them.  All five
are open-weight; license details vary and are worth reading once.</p>

<h4>Llama 3 / 3.1 (Meta)</h4>
<p><a href="https://arxiv.org/abs/2407.21783" target="_blank" rel="noopener">Llama 3.1</a>
ships in 8B, 70B, and 405B parameter sizes.  The 8B is the default open SLM
baseline almost everyone reports against; the 70B is the workhorse for
serious self-hosted deployments; the 405B is a frontier-quality dense model.
The training report is one of the most detailed in the open literature.
License: Llama Community License (commercial-friendly with a large-MAU
clause).  Download from the
<a href="https://huggingface.co/meta-llama" target="_blank" rel="noopener">meta-llama org on Hugging Face</a>.</p>

<h4>Qwen 2.5 (Alibaba)</h4>
<p><a href="https://arxiv.org/abs/2412.15115" target="_blank" rel="noopener">Qwen 2.5</a>
covers 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B — the widest size ladder in
open-weight land.  Particularly strong on reasoning, math, and code, and
multilingual to a degree most western models aren't.  Most variants are
Apache 2.0.  Pulls from
<a href="https://huggingface.co/Qwen" target="_blank" rel="noopener">huggingface.co/Qwen</a>.</p>

<h4>DeepSeek-V3</h4>
<p><a href="https://arxiv.org/abs/2412.19437" target="_blank" rel="noopener">DeepSeek-V3</a>
is a 671B-parameter Mixture-of-Experts (MoE) model that activates only ~37B
parameters per token.  That ratio is the headline: frontier-class quality at
inference cost closer to a 37B dense model.  The trade is memory — you still
need to hold all 671B parameters in GPU RAM.  Open-weight under the DeepSeek
license, with strong math and code numbers.</p>

<h4>Mistral 7B and Mixtral 8×7B</h4>
<p><a href="https://arxiv.org/abs/2310.06825" target="_blank" rel="noopener">Mistral 7B</a>
remains one of the cleanest 7B baselines on the leaderboard.
<a href="https://arxiv.org/abs/2401.04088" target="_blank" rel="noopener">Mixtral 8×7B</a>
is its MoE sibling: 8 experts of 7B each, 2 active per token, ~13B
effective compute, ~47B parameters total.  Both are Apache 2.0 — the most
permissive license in this list.</p>

<h4>Gemma 2 (Google)</h4>
<p><a href="https://arxiv.org/abs/2408.00118" target="_blank" rel="noopener">Gemma 2</a>
ships at 2B, 9B, and 27B.  The 9B is widely considered the best
single-GPU-friendly all-rounder; the 27B is competitive with much larger
models thanks to careful distillation from a teacher.  License: Gemma terms
(commercial use, with Google's responsible-use restrictions).</p>

<pre>
family       sizes (B)              license             notable for
-----------  ---------------------  ------------------  -----------------------
Llama 3.1    8 / 70 / 405           Llama Community     reference baseline
Qwen 2.5     0.5/1.5/3/7/14/32/72   Apache 2.0          breadth + reasoning/code
DeepSeek-V3  671 (37 active, MoE)   DeepSeek License    frontier MoE quality
Mistral      7 dense; 8x7 MoE       Apache 2.0          permissive + strong 7B
Gemma 2      2 / 9 / 27             Gemma terms         distillation-tuned
</pre>
<p>For a first benchmark suite, Llama-3.1-8B + Qwen2.5-7B + Gemma-2-9B +
Mistral-7B is a defensible four-way comparison: similar compute class, four
different research lineages, four different licenses.</p>

## Papers and references

### The Llama 3 Herd of Models
- **Authors:** Llama Team, Meta
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.21783

Detailed training-recipe document for the 8B/70B/405B family. The most-cited open-weight LLM report of 2024.

### Qwen2.5 Technical Report
- **Authors:** Qwen Team, Alibaba
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2412.15115

Covers seven sizes from 0.5B to 72B with shared tokenizer and recipe. Useful for studying scale within a single model family.

### DeepSeek-V3 Technical Report
- **Authors:** DeepSeek-AI
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2412.19437

671B-parameter MoE with 37B active per token. Frontier-class quality with much cheaper inference than a comparable dense model.

### Mistral 7B
- **Authors:** Jiang et al.
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2310.06825

The 7B Apache-2.0 model that set the bar for open-weight SLMs. Sliding-window attention and grouped-query attention are introduced cleanly.

### Mixtral of Experts
- **Authors:** Jiang et al.
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2401.04088

8x7B sparse MoE; 2 of 8 experts active per token. The reference for understanding sparse MoE in an open-weight model.

### Gemma 2: Improving Open Language Models at a Practical Size
- **Authors:** Gemma Team, Google
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2408.00118

2B/9B/27B with knowledge distillation from a larger teacher. The 9B is the standout single-GPU model in this family.

## Extras
- [meta-llama org on Hugging Face](https://huggingface.co/meta-llama)
- [Qwen org on Hugging Face](https://huggingface.co/Qwen)
- [Mistral AI org on Hugging Face](https://huggingface.co/mistralai)
