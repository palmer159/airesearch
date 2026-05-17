---
id: 28
title: Mixture-of-Experts at Scale (Mixtral, DeepSeek-V3)
part: III. ML & AI in Chronological Order
---

<p>By 2024 it was clear that dense Transformers were not the
compute-optimal way to keep scaling. <b><a href="https://en.wikipedia.org/wiki/Mixture_of_experts" target="_blank" rel="noopener">Mixture-of-Experts</a> (MoE)</b>
models replace each feed-forward block with a bank of E experts and a
small router that activates only k of them per token. Total parameters
go up; <a href="https://en.wikipedia.org/wiki/FLOPS" target="_blank" rel="noopener">FLOPs</a> per token stay roughly constant.</p>

<h4>The router</h4>
<pre>
For each token x:
  scores = router(x)                # vector over E experts
  top_k_experts = topk(scores, k)   # typically k = 2
  y = sum_{e in top_k_experts}  softmax(scores)[e] * Expert_e(x)
</pre>

<h4>The headline 2024 results</h4>
<ul>
  <li><b>Mixtral 8x7B</b> (Mistral, January 2024): 8 experts, 2 active per
  token. ~47B total parameters, ~13B active. Matched or beat <a href="https://en.wikipedia.org/wiki/Llama_(language_model)" target="_blank" rel="noopener">Llama</a> 2
  70B at a fraction of the inference cost. The model that made MoE
  mainstream in open-source.</li>
  <li><b><a href="https://en.wikipedia.org/wiki/DeepSeek" target="_blank" rel="noopener">DeepSeek</a>-V3</b> (December 2024): 671B total parameters, 37B
  active per token, 256 routed experts. Trained on 14.8T tokens for a
  reported $5.6M of compute. Competitive with frontier closed models on
  standard benchmarks. Showed that MoE plus careful systems engineering
  could collapse the cost gap between open and closed labs.</li>
</ul>

<h4>Why MoE is hard, and why it works anyway</h4>
<ul>
  <li>Routers like to collapse — sending everything to a single expert.
  Auxiliary load-balancing losses are needed to spread tokens.</li>
  <li>Inference is memory-bound: you have to hold all experts in VRAM
  even though you only use a few per token. This is why MoE is great
  for batch serving and awkward for single-stream low-latency use.</li>
  <li>The same FLOP budget buys more parameters, which buys more capacity
  for niche skills and languages — the "specialist experts" intuition,
  loosely.</li>
</ul>

<p>Almost every frontier-class model in 2025 is now MoE. The dense
Transformer is becoming the SLM choice for on-device inference; MoE is
the data-center choice for raw quality per FLOP.</p>

## Papers

### Mixtral of Experts
- **Authors:** Albert Q. Jiang et al. (Mistral AI)
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2401.04088

Mixtral 8x7B. The open-weight MoE model that made the architecture mainstream. Clean ablations on routing and load balancing.

### DeepSeek-V3 Technical Report
- **Authors:** DeepSeek-AI
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2412.19437

671B-parameter MoE with 37B active per token. The most detailed open description of a frontier-scale MoE training run, including auxiliary-loss-free balancing and FP8 training infrastructure.

### Switch Transformer: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity
- **Authors:** William Fedus, Barret Zoph, Noam Shazeer
- **Year:** 2021
- **Venue:** JMLR
- **URL:** https://arxiv.org/abs/2101.03961

The earlier Google MoE paper that worked through routing instabilities and scaled to 1.6T parameters. Most modern MoE recipes descend from this one.

## Extras
- [A Visual Guide to Mixture of Experts (Maarten Grootendorst)](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts)
