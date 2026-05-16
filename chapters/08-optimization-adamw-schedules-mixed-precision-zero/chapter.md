---
id: 8
title: Optimization: AdamW, Schedules, Mixed Precision, ZeRO
part: II. Training & Data
---

<p>Training a transformer is mostly engineering. The defaults that work today:</p>
<ul>
  <li><b>AdamW</b> with β=(0.9, 0.95), weight decay 0.1.</li>
  <li><b>Cosine</b> learning-rate schedule with linear warmup (a few thousand steps), max LR scaled with batch size.</li>
  <li><b>Mixed precision</b> — bf16 dominates fp16 for stability; fp8 emerging for H100/B200.</li>
  <li><b>ZeRO</b> (DeepSpeed) and <b>FSDP</b> (PyTorch) for sharding optimizer state, gradients, and parameters across GPUs.</li>
  <li><b>Gradient clipping</b> at 1.0 to control loss spikes.</li>
  <li><b>μP</b> (Maximal Update Parameterization) — transfer hyperparameters from small to large models.</li>
</ul>

## Papers

### Decoupled Weight Decay Regularization (AdamW)
- **Authors:** Loshchilov, Hutter
- **Year:** 2019
- **URL:** https://arxiv.org/abs/1711.05101

Properly decouples weight decay from gradient-based updates. The default optimizer for LMs.

### Mixed Precision Training
- **Authors:** Micikevicius et al.
- **Year:** 2018
- **URL:** https://arxiv.org/abs/1710.03740

fp16 with loss scaling. The follow-up bfloat16 (Google) is now the de-facto standard for pretraining.

### ZeRO: Memory Optimizations for Training Trillion-Parameter Models
- **Authors:** Rajbhandari et al.
- **Year:** 2020
- **URL:** https://arxiv.org/abs/1910.02054

Shards optimizer state / gradients / parameters across data-parallel ranks. Enables truly large training runs.

### Tensor Programs V (μP)
- **Authors:** Yang et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2203.03466

Hyperparameter-transfer across width: tune at 100M, deploy at 100B. Massively reduces tuning cost.
