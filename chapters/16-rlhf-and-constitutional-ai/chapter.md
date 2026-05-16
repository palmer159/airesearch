---
id: 16
title: RLHF and Constitutional AI
part: IV. Post-training & Alignment
---

<p><b>RLHF</b> (Christiano 2017; OpenAI's InstructGPT 2022) trains a reward model from human pairwise preferences,
then runs PPO against the LM. It produced ChatGPT and remains the gold standard when human labels are abundant
and quality matters.</p>
<p><b>Constitutional AI</b> (Anthropic, 2022) replaces most human labels with model-generated critiques against a
written constitution. Cheaper, more transparent, and the foundation of Claude's harmlessness training.</p>

## Papers

### Deep Reinforcement Learning from Human Preferences
- **Authors:** Christiano et al.
- **Year:** 2017
- **URL:** https://arxiv.org/abs/1706.03741

The original RLHF formulation. Reward model + PPO.

### Training language models to follow instructions with human feedback (InstructGPT)
- **Authors:** Ouyang et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2203.02155

GPT-3 → InstructGPT via SFT + RLHF. Direct ancestor of ChatGPT.

### Constitutional AI: Harmlessness from AI Feedback
- **Authors:** Bai et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2212.08073

Use the model itself to critique under a written constitution; reduces human-label dependence.

### Llama 2
- **Authors:** Touvron et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.09288

Best public RLHF + Ghost-Attention writeup at the time. Required reading for the production recipe.
