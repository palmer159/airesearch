---
id: 13
title: State-Space Models: Mamba and Hybrids
part: III. Architecture Frontiers
---

<p>Self-attention is O(n²) in sequence length. <b><a href="https://en.wikipedia.org/wiki/State-space_model" target="_blank" rel="noopener">State-space models</a> (SSMs)</b> like S4 and <b>Mamba</b> compute
in O(n) using a learnable recurrence. Mamba uses <i>selective</i> SSMs — input-dependent dynamics — to recover the
context-routing flexibility that attention provides.</p>
<p>In 2024-25 the field converged on <b>hybrid</b> architectures (e.g., Jamba, Samba): mostly Mamba with a few attention
layers, getting linear scaling without sacrificing in-context recall. SSMs remain less effective than attention on tasks
that require pinpoint long-range copying, but the gap is narrowing.</p>

## Papers

### Efficiently Modeling Long Sequences with Structured State Spaces (S4)
- **Authors:** Gu, Goel, Ré
- **Year:** 2022
- **Venue:** ICLR (Outstanding Paper)
- **URL:** https://arxiv.org/abs/2111.00396

The structured SSM that started the wave; principled long-range memory.

### Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- **Authors:** Gu, Dao
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2312.00752

Selective SSMs — content-dependent state — close most of the gap with attention. Highly hardware-friendly.

### Jamba: A Hybrid Transformer-Mamba Language Model
- **Authors:** Lieber et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.19887

Practical hybrid: SSM majority + attention minority + MoE. Strong long-context throughput.

### An Empirical Study of Mamba-based Language Models
- **Authors:** Waleffe et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2406.07887

NVIDIA's controlled comparison: hybrid > pure-Mamba > pure-transformer at long context.
