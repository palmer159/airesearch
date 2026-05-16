---
id: 40
title: Bias, Fairness, and Sociotechnical Harms
part: X. AI Safety & Alignment
---

<p>LMs encode the biases of their training data and amplify them via deployment scale. Bender et al.'s
"Stochastic Parrots" (2021) framed the sociotechnical critique that has shaped policy and academic discourse.
Practical evaluation: <b>BBQ</b> (bias QA), <b>StereoSet</b>, <b>RealToxicityPrompts</b>, <b>HELM</b>'s fairness
metrics. Mitigations are partial — assume residual bias and design for it (auditing, opt-outs, recourse).</p>

## Papers

### On the Dangers of Stochastic Parrots
- **Authors:** Bender, Gebru, McMillan-Major, Shmitchell
- **Year:** 2021
- **Venue:** FAccT (Open Access)
- **URL:** https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf

Foundational sociotechnical critique. Required reading regardless of prior. (Direct OA PDF; the FAccT proceedings paper is gold open access.)

### BBQ: A Hand-Built Bias Benchmark for Question Answering
- **Authors:** Parrish et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2110.08193

Practical bias eval across 9 axes.

### RealToxicityPrompts
- **Authors:** Gehman et al.
- **Year:** 2020
- **URL:** https://arxiv.org/abs/2009.11462

Standard toxicity-elicitation benchmark.

### Datasheets for Datasets
- **Authors:** Gebru et al.
- **Year:** 2021
- **URL:** https://arxiv.org/abs/1803.09010

Documentation discipline for training data; widely adopted.
