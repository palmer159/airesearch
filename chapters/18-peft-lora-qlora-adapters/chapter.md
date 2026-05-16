---
id: 18
title: PEFT: LoRA, QLoRA, Adapters
part: IV. Post-training & Alignment
---

<p>Full fine-tuning a 70B model needs hundreds of GB of optimizer state. <b>Parameter-efficient fine-tuning</b>
freezes the base model and trains tiny add-ons:</p>
<ul>
  <li><b>LoRA</b> (Hu et al., 2021) — low-rank update <code>ΔW = B·A</code>, typically 0.1-1% of params.</li>
  <li><b>QLoRA</b> (Dettmers et al., 2023) — base model quantized to 4-bit; LoRA in <a href="https://en.wikipedia.org/wiki/Half-precision_floating-point_format" target="_blank" rel="noopener">fp16</a>. Fine-tune 65B on a single 48GB GPU.</li>
  <li><b>Adapters</b> (Houlsby et al., 2019) — bottleneck modules inserted in each layer; pre-LoRA classic.</li>
</ul>
<p>Practical default in 2026: <b>QLoRA + DPO</b> on a strong open base. You'll spend more time on data than on optimization.</p>

## Papers

### LoRA: Low-Rank Adaptation of Large Language Models
- **Authors:** Hu et al.
- **Year:** 2022
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2106.09685

Inject low-rank trainable matrices into attention projections. Now ubiquitous.

### QLoRA: Efficient Finetuning of Quantized LLMs
- **Authors:** Dettmers et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.14314

4-bit NormalFloat + paged optimizers + LoRA. Democratized large-model finetuning.

### Parameter-Efficient Transfer Learning for NLP (Adapters)
- **Authors:** Houlsby et al.
- **Year:** 2019
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/1902.00751

Original adapter modules. Predates LoRA.

### DoRA: Weight-Decomposed Low-Rank Adaptation
- **Authors:** Liu et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.09353

Decomposes weights into magnitude × direction; closes most of the LoRA→full-FT gap.
