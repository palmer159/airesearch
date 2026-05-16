---
id: 15
title: Instruction Tuning (SFT)
part: IV. Post-training & Alignment
---

<p>Supervised fine-tuning (SFT) on instruction-response pairs converts a base completion model into a usable
assistant. It is the cheapest, most reliable alignment intervention you have. Quality of data dominates quantity:
LIMA (Zhou et al., 2023) showed 1,000 carefully curated examples can produce a strong assistant.</p>
<h4>Practical tips</h4>
<ul>
  <li>Mix held-out evals into the training mix to monitor task distribution drift.</li>
  <li>Mask the prompt tokens in the loss; train only on assistant responses.</li>
  <li>Don't over-train — 1-3 epochs typically; more usually hurts diversity.</li>
</ul>

## Papers

### Finetuned Language Models Are Zero-Shot Learners (FLAN)
- **Authors:** Wei et al.
- **Year:** 2022
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2109.01652

Multi-task instruction-tuning improves unseen-task zero-shot performance. The seed of the modern recipe.

### Self-Instruct: Aligning Language Models with Self-Generated Instructions
- **Authors:** Wang et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2212.10560

Bootstraps SFT data from a small seed via the model itself; democratized instruction-tuning.

### LIMA: Less Is More for Alignment
- **Authors:** Zhou et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.11206

1,000 hand-crafted SFT examples ≈ much larger RLHF systems on many evals. Quality wins.

### The Flan Collection: Designing Data and Methods for Effective Instruction Tuning
- **Authors:** Longpre et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2301.13688

Best ablation of what really matters in instruction-tuning data.
