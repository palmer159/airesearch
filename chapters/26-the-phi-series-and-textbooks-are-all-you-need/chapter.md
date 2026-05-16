---
id: 26
title: The Phi Series and 'Textbooks Are All You Need'
part: VII. Small Language Models
---

<p>Microsoft Research's <b>Phi</b> series argued that <i>data quality dominates scale</i>: with carefully curated
"textbook-quality" synthetic data, a 1.3B model can beat 7B contemporaries on coding and reasoning. Phi-2, Phi-3,
and Phi-4 (mini/medium/multimodal) made this practical: state-of-the-art tasks running at SLM cost.</p>
<p>The key technique is generating <i>diverse, pedagogically-structured</i> synthetic data with a stronger teacher
model, filtered for difficulty and quality. This recipe is now standard across SLM teams (Microsoft, Apple, Google).</p>

## Papers

### Textbooks Are All You Need (phi-1)
- **Authors:** Gunasekar et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2306.11644

1.3B code model trained on textbook-quality synthetic data; beats much larger models on HumanEval.

### Textbooks Are All You Need II: phi-1.5 technical report
- **Authors:** Li et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2309.05463

Extends to general reasoning; small model emergent capabilities discussion.

### Phi-3 Technical Report
- **Authors:** Abdin et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2404.14219

3.8B model trained on heavily filtered web + synthetic data; runs on a phone.

### Phi-4 Technical Report
- **Authors:** Abdin et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2412.08905

14B SLM with training-data-centric design; strong on reasoning evals.
