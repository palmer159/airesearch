---
id: 39
title: Interpretability and Mechanistic Understanding
part: X. AI Safety & Alignment
---

<p><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability" target="_blank" rel="noopener">Mechanistic interpretability</a> tries to reverse-engineer what computation a model implements.
2023-25 milestones: <b>induction heads</b> (Olsson et al.), <b>features as directions</b> (Elhage et al.),
and the dramatic <b>Sparse Autoencoders</b> result (Anthropic, 2024) — extracting millions of
human-interpretable features from a frontier model's residual stream.</p>
<p>For practitioners: SAEs and steering vectors are starting to enable <i>controllable</i> deployment —
suppressing specific failure modes, steering tone, or adding structured policy without retraining.</p>

## Papers

### A Mathematical Framework for Transformer Circuits
- **Authors:** Elhage, Nanda et al. (Anthropic)
- **Year:** 2021
- **URL:** https://transformer-circuits.pub/2021/framework/index.html

Interprets attention-only transformers as compositions of QK and OV circuits. Foundational.

### In-context Learning and Induction Heads
- **Authors:** Olsson et al.
- **Year:** 2022
- **URL:** https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html

Identifies the circuit responsible for in-context learning. The first big mechanistic result.

### Toy Models of Superposition
- **Authors:** Elhage et al.
- **Year:** 2022
- **URL:** https://transformer-circuits.pub/2022/toy_model/index.html

Why neurons are polysemantic and why we need decomposition methods like SAEs.

### Scaling Monosemanticity (Sparse Autoencoders on Claude)
- **Authors:** Templeton et al. (Anthropic)
- **Year:** 2024
- **URL:** https://transformer-circuits.pub/2024/scaling-monosemanticity/

Millions of interpretable features extracted from a frontier model. Steering experiments included.

### Locating and Editing Factual Associations in GPT (ROME)
- **Authors:** Meng et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2202.05262

Locate factual associations in MLP layers; edit them surgically. The standard knowledge-editing baseline.
