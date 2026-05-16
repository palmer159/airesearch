---
id: 33
title: Native Multimodal Models: GPT-4o, Gemini, Claude 3+
part: VIII. Multimodal
---

<p>2024-25 brought "natively multimodal" frontier models: GPT-4o, Gemini 1.5/2.x, Claude 3/4. They share three
properties: (1) ingest text + images + audio + video in one prompt, (2) very long context (128k–10M), (3) often
also <i>generate</i> across modalities. Understanding their capabilities and failure modes is now
table-stakes for AI practitioners.</p>

## Papers

### Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context
- **Authors:** Google DeepMind
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.05530

MoE + ring attention for 1M+ token context. Includes needle-in-a-haystack and multimodal evals.

### GPT-4o System Card
- **Authors:** OpenAI
- **Year:** 2024
- **URL:** https://cdn.openai.com/gpt-4o-system-card.pdf

Native audio/text/vision unified model. Heavy on safety evaluation, light on architecture. (Direct PDF on cdn.openai.com.)

### The Claude 3 Model Family: Opus, Sonnet, Haiku
- **Authors:** Anthropic
- **Year:** 2024
- **URL:** https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf

Vision + long context; strong agentic + tool-use baseline. Solid model card.
