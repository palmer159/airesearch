---
id: 28
title: Quantization: GPTQ, AWQ, GGUF, FP8/INT4
part: VII. Small Language Models
---

<p>Quantization is the bridge from research to deployment. Modern weight-only schemes:</p>
<ul>
  <li><b>GPTQ</b> — second-order error minimization; 4-bit, near-lossless on most LMs.</li>
  <li><b>AWQ</b> — activation-aware; preserves salient channels at higher precision.</li>
  <li><b>GGUF / llama.cpp</b> — practitioner format covering 2/3/4/5/6/8-bit, K-quants, IQ-quants.</li>
  <li><b>SmoothQuant</b> — migrate activation outliers into weights for W8A8 inference.</li>
  <li><b>FP8 (H100/B200) and INT4 + KV-cache compression</b> dominate production serving in 2025-26.</li>
</ul>
<p>Watch for benchmark sensitivity: a model "lossless" on perplexity can degrade noticeably on chain-of-thought
math at <8-bit. Always re-eval at deployment precision.</p>

## Papers

### GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers
- **Authors:** Frantar et al.
- **Year:** 2023
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2210.17323

Second-order, layer-wise; the canonical 4-bit weight-only quantizer.

### AWQ: Activation-aware Weight Quantization for LLM Compression
- **Authors:** Lin et al.
- **Year:** 2024
- **Venue:** MLSys
- **URL:** https://arxiv.org/abs/2306.00978

Protects salient channels; near-lossless 4-bit and fast on consumer GPUs.

### SmoothQuant: Accurate and Efficient Post-Training Quantization for LLMs
- **Authors:** Xiao et al.
- **Year:** 2023
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/2211.10438

Shifts activation outliers into weights for W8A8 inference; production-friendly.

### LLM.int8(): 8-bit Matrix Multiplication
- **Authors:** Dettmers et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2208.07339

First widely-used 8-bit inference for LLMs; introduces outlier handling.

## Extras

- [llama.cpp / GGUF](https://github.com/ggerganov/llama.cpp)
