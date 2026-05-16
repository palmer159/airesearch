---
id: 14
title: Efficient Attention: FlashAttention and Friends
part: III. Architecture Frontiers
---

<p><b>FlashAttention</b> (Tri Dao, 2022) recasts attention as an IO-aware tiled algorithm that never materializes
the n×n attention matrix in HBM. It's not an approximation — it's exact, but wall-clock 2-4x faster and dramatically
more memory-efficient. v2 and v3 added further hardware specialization (Ampere, Hopper).</p>

<p>This single kernel is one of the most consequential systems contributions to the field — without it, today's
context lengths would be impractical.</p>

## Papers

### FlashAttention: Fast and Memory-Efficient Exact Attention
- **Authors:** Dao et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2205.14135

IO-aware attention algorithm; standard in every serious training/inference stack.

### FlashAttention-2
- **Authors:** Dao
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.08691

Better work partitioning; ~2x speedup over v1 on A100.

### FlashAttention-3 (Hopper)
- **Authors:** Shah et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.08608

Asynchrony + low-precision (fp8) on H100; near-peak utilization for transformer inference.

### PagedAttention / vLLM
- **Authors:** Kwon et al.
- **Year:** 2023
- **Venue:** SOSP
- **URL:** https://arxiv.org/abs/2309.06180

OS-style paging for KV cache → 2-4x throughput at serving time. vLLM is the dominant open inference engine.
