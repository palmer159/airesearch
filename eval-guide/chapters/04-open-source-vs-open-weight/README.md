---
id: 4
title: Open-Source vs. Open-Weight Models
part: II. The Open Model Landscape
---

# Open-Source vs. Open-Weight Models

*II. The Open Model Landscape*

<p>"Open" is doing a lot of work in "open model."  Before you pick a model to
benchmark, it helps to know what you actually get when you download it — and
what you're allowed to do with it afterwards.  The ecosystem sits on a
spectrum, not a binary.</p>

<h4>Fully open: data + weights + training code</h4>
<p>A small but important group of models ships everything: the training data,
the data-mixing recipe, the training code, intermediate checkpoints, and the
final weights.  <a href="https://arxiv.org/abs/2402.00838" target="_blank" rel="noopener">OLMo</a>
from AI2 and the older Pythia suite from EleutherAI are the canonical
examples.  These are the only models you can truly <i>reproduce</i>, and
they're the right choice for research on training dynamics, data
attribution, or scaling behavior.</p>

<h4>Open-weight: weights yes, recipe no</h4>
<p>The bulk of what people call "open models" lives here.  You get the
weights and a model card; you don't get the training data or the full
training code.  Llama 3, Qwen 2.5, DeepSeek-V3, Mistral / Mixtral, Gemma 2,
and Phi all fit this category.  Open-weight is more than enough for most
real work: you can run inference, fine-tune, quantize, distill, and deploy.
You just can't re-train from scratch.</p>

<h4>Hosted closed: API only</h4>
<p>GPT-4-class models from OpenAI, Claude from Anthropic, and Gemini from
Google are accessed only through APIs.  No weights, no fine-tuning of the
base model, and your benchmark results are tied to whatever version the
provider is serving today.  That last point matters: closed models can and
do change underneath you between eval runs.</p>

<h4>Licenses actually matter</h4>
<p>Read the license before you commit a model to a benchmark suite, never
mind a product:</p>
<pre>
license type            examples                  commercial use?
----------------------  ------------------------  ----------------
Apache 2.0 / MIT        OLMo, Qwen, Mistral 7B    yes, broadly
Llama community         Llama 3 family            yes, with limits
Gemma terms             Gemma 2                   yes, with terms
research-only           some early releases       no
</pre>
<p>The Llama Community License, for example, has a 700M-MAU clause that
restricts very large deployments; Gemma has its own usage terms.  Apache
2.0 (Qwen, Mistral 7B, OLMo) is the friendliest.</p>

<h4>Why this matters for benchmarks</h4>
<p>Reproducibility lives or dies on openness.  An open-weight model gives
you a fixed artifact you can hash, version, and re-run a year later.  A
hosted closed model gives you a moving target.  When you publish numbers,
note the exact model checkpoint and license — and consider whether the
result is one a peer can reproduce.  The
<a href="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard" target="_blank" rel="noopener">Hugging Face Open LLM Leaderboard</a>
is the de-facto registry for open-weight models and a good place to start
when you're choosing what to evaluate.</p>

## Papers and references

### OLMo: Accelerating the Science of Language Models
- **Authors:** Groeneveld et al. (AI2)
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2402.00838

The reference fully-open release: data, training code, intermediate checkpoints, and weights. Read this if you care about reproducibility.

### The Llama 3 Herd of Models
- **Authors:** Llama Team, Meta
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.21783

The flagship open-weight family. The report doubles as a candid description of what 'open-weight' currently includes — and what it doesn't.

### Qwen2.5 Technical Report
- **Authors:** Qwen Team, Alibaba
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2412.15115

Apache-2.0 open-weight family across many sizes. A clean example of broadly-permissive licensing applied to a strong modern model.

### Mistral 7B
- **Authors:** Jiang et al.
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2310.06825

Apache-2.0, 7B parameters, the model that mainstreamed truly-permissive open-weight releases at competitive quality.

### Gemma 2: Improving Open Language Models at a Practical Size
- **Authors:** Gemma Team, Google
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2408.00118

Open-weight under the Gemma terms. Useful counter-example to Apache-2.0: similar artifacts, materially different license obligations.

## Extras
- [Hugging Face Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [OLMo collection on Hugging Face](https://huggingface.co/allenai)
- [Llama 3.1 8B Instruct model card](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct)
