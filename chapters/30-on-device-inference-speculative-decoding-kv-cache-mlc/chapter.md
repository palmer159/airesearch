---
id: 30
title: On-Device Inference: Speculative Decoding, KV Cache, MLC
part: VII. Small Language Models
---

<p>SLM deployment is a systems problem. Pillars:</p>
<ul>
  <li><b>Speculative decoding</b> (Leviathan; Chen et al.) — run a tiny draft model, let the big model verify.
      2-3x speedups on real workloads.</li>
  <li><b>Medusa, EAGLE</b> — draft heads inside the same model; even cheaper.</li>
  <li><b>KV-cache compression</b> — quantize KV; sliding-window attention; H2O / StreamingLLM eviction policies.</li>
  <li><b>Compiler stacks</b> — MLC-LLM, llama.cpp, MLX (Apple), TensorRT-LLM.</li>
</ul>

## Papers

### Fast Inference from Transformers via Speculative Decoding
- **Authors:** Leviathan, Kalman, Matias
- **Year:** 2023
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/2211.17192

Speculative decoding: lossless 2-3x speedup.

### Accelerating Large Language Model Decoding with Speculative Sampling
- **Authors:** Chen et al. (DeepMind)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2302.01318

Concurrent formulation; rigorous correctness analysis.

### Medusa: Simple LLM Inference Acceleration via Multiple Decoding Heads
- **Authors:** Cai et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2401.10774

Add small prediction heads; no separate draft model needed.

### Efficient Streaming Language Models with Attention Sinks (StreamingLLM)
- **Authors:** Xiao et al.
- **Year:** 2024
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2309.17453

Keep the first few tokens always in KV; trivially extends context with sliding window.

## Extras

- [MLC-LLM](https://github.com/mlc-ai/mlc-llm)
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)
