---
id: 11
title: Positional Encoding & Long Context (RoPE, ALiBi, YaRN)
part: III. Architecture Frontiers
---

<p>Vanilla absolute positions don't extrapolate beyond training length. Modern systems use:</p>
<ul>
  <li><b>RoPE</b> (Rotary Position Embedding) — rotates query/key vectors by a position-dependent angle. Llama, Qwen, Mistral.</li>
  <li><b>ALiBi</b> — adds a linear distance bias to attention; trivial extrapolation but slightly weaker quality.</li>
  <li><b>YaRN / NTK-aware scaling</b> — interpolation tricks that cheaply stretch a RoPE model to 32k–128k context.</li>
</ul>
<p>Combined with FlashAttention (Ch. 14) and ring attention, modern systems routinely reach 128k–1M tokens.</p>

## Papers

### RoFormer: Enhanced Transformer with Rotary Position Embedding
- **Authors:** Su et al.
- **Year:** 2021
- **URL:** https://arxiv.org/abs/2104.09864

RoPE encodes relative position via rotation; the dominant scheme in 2025-era LMs.

### Train Short, Test Long: Attention with Linear Biases (ALiBi)
- **Authors:** Press, Smith, Lewis
- **Year:** 2022
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2108.12409

Position-free attention with simple distance bias; clean extrapolation properties.

### YaRN: Efficient Context Window Extension
- **Authors:** Peng et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2309.00071

Extends RoPE-trained models to ~128k with minimal fine-tuning.

### Lost in the Middle: How Language Models Use Long Contexts
- **Authors:** Liu et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.03172

Long-context models systematically under-use middle positions. Sobering when designing RAG layouts.

### Ring Attention with Blockwise Transformers
- **Authors:** Liu, Zaharia, Abbeel
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.01889

Distributes attention across devices; underpins Gemini 1.5's 1M-token context.
