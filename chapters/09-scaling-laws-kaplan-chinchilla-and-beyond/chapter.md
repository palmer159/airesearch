---
id: 9
title: Scaling Laws: Kaplan, Chinchilla, and Beyond
part: II. Training & Data
---

<p>Scaling laws predict loss as a power-law in compute, parameters, and data. Two pivotal results:</p>
<ul>
  <li><b>Kaplan et al. (2020)</b> — loss is smooth and predictable in N (parameters) and D (data); recommended
      under-training relative to parameters.</li>
  <li><b>Chinchilla (Hoffmann et al., 2022)</b> — corrected the recipe: optimal compute uses roughly <b>20 tokens
      per parameter</b>. Most pre-2022 large models were under-trained.</li>
</ul>
<p>Chinchilla's insight reshaped the entire field. It also motivated the SLM movement (Ch. 17): if you train smaller
models on more tokens, you get inference-time efficiency for free.</p>
<p>Open question for 2026: with synthetic data and curriculum, are we approaching a regime where the data axis is the
true bottleneck — and should new scaling laws account for data quality, not just quantity?</p>

## Papers

### Scaling Laws for Neural Language Models
- **Authors:** Kaplan et al.
- **Year:** 2020
- **URL:** https://arxiv.org/abs/2001.08361

Power-law scaling in N, D, C. Influenced GPT-3 sizing — but later shown to under-train.

### Training Compute-Optimal Large Language Models (Chinchilla)
- **Authors:** Hoffmann et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2203.15556

Re-derives optimal N and D under fixed compute; rule-of-thumb 20 tokens/parameter.

### Scaling Laws and Interpretability of Learning from Repeated Data
- **Authors:** Hernandez et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2205.10487

Repeated data isn't free — performance plateaus and then degrades. Constrains how far we can ride a fixed corpus.

### Beyond neural scaling laws: beating power law scaling via data pruning
- **Authors:** Sorscher et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2206.14486

Data quality can change the exponent of the scaling law, not just the constant.
