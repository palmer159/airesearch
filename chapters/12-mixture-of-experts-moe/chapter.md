---
id: 12
title: Mixture-of-Experts (MoE)
part: III. Architecture Frontiers
---

<p>An MoE layer routes each token to <b>k of N</b> expert FFNs (typically k=2). You get the parameter count of
a huge model with the FLOPs of a small one — a different point on the cost/quality Pareto.</p>
<p>Modern MoE systems (Mixtral, DeepSeek-V2/V3, Qwen3-MoE, Grok-1) report 5-10x parameter counts at similar serving
cost. Challenges: load balancing, expert collapse, training instability, and routing-as-side-channel for inference cost prediction.</p>

<h4>Routing math (top-k softmax)</h4>
<pre>
g_i = softmax(W_gate · x)        # gate logits per expert
top_k = TopK(g_i, k)              # active experts for this token
y = sum_{i in top_k} (g_i / sum top_k) * Expert_i(x)
</pre>

## Papers

### Outrageously Large Neural Networks: Sparsely-Gated Mixture-of-Experts
- **Authors:** Shazeer et al.
- **Year:** 2017
- **URL:** https://arxiv.org/abs/1701.06538

The modern sparse MoE design (Google Brain).

### Switch Transformers: Scaling to Trillion Parameter Models
- **Authors:** Fedus, Zoph, Shazeer
- **Year:** 2022
- **Venue:** JMLR
- **URL:** https://arxiv.org/abs/2101.03961

Top-1 routing simplifies training; demonstrates trillion-parameter feasibility.

### GLaM: Efficient Scaling of Language Models with Mixture-of-Experts
- **Authors:** Du et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2112.06905

1.2T-parameter MoE consuming 1/3 the energy of GPT-3 to train and 1/2 the FLOPs at inference.

### Mixtral of Experts
- **Authors:** Jiang et al.
- **Year:** 2024
- **Venue:** Mistral AI
- **URL:** https://arxiv.org/abs/2401.04088

8x7B sparse MoE, k=2; canonical open-weight MoE recipe.

### DeepSeek-V3 Technical Report
- **Authors:** DeepSeek-AI
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2412.19437

671B MoE (37B active) with multi-head latent attention and FP8 training. Best open-weight non-trivial frontier model of late 2024.
