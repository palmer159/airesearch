---
id: 27
title: Open SLM Families: Llama-3, Gemma, Qwen, Mistral, SmolLM
part: VII. Small Language Models
---

<p>The 2024-26 SLM ecosystem is dominated by a few open families:</p>
<ul>
  <li><b><a href="https://en.wikipedia.org/wiki/Llama_(language_model)" target="_blank" rel="noopener">Llama</a> 3.x / 4</b> (Meta) — 1B / 3B / 8B / 70B; reference quality.</li>
  <li><b>Gemma 2 / 3</b> (Google) — 2B / 9B / 27B; strong multilingual; Gemma 3 adds vision.</li>
  <li><b>Qwen 2.5 / 3</b> (Alibaba) — 0.5B → 72B; excellent at math, code, multilingual; Qwen 2.5-Coder is a top open coder.</li>
  <li><b><a href="https://en.wikipedia.org/wiki/Mistral_AI" target="_blank" rel="noopener">Mistral</a> / Ministral / Mixtral</b> — efficient dense + MoE.</li>
  <li><b>SmolLM2 / SmolLM3</b> (Hugging Face) — 135M / 360M / 1.7B / 3B fully open recipe (data, code, weights).</li>
  <li><b>Apple Intelligence Foundation Models</b> — ~3B on-device; technical report worth reading for production constraints.</li>
</ul>

## Papers

### The Llama 3 Herd of Models
- **Authors:** Meta AI
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.21783

92-page recipe: data, scaling, post-training, multimodal. The most-cited open frontier-class paper.

### Gemma 2 Technical Report
- **Authors:** Gemma Team
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2408.00118

Knowledge distillation + soft attention logit capping; strong 9B/27B SLMs.

### Qwen2.5 Technical Report
- **Authors:** Qwen Team
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2412.15115

Sweep from 0.5B to 72B; strong multilingual + coding subseries.

### SmolLM2: When Smol Goes Big
- **Authors:** Allal et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2502.02737

Fully open 135M-1.7B family with curated training mix; excellent baseline for SLM research.

### Apple Intelligence Foundation Language Models
- **Authors:** Apple
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.21075

On-device 3B model with adapter-based personalization; production constraints articulated clearly.
