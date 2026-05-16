---
id: 34
title: Benchmarks: MMLU, BIG-Bench, HELM, GPQA, MATH
part: IX. Evaluation
---

<p>Modern benchmarks span breadth (<b><a href="https://en.wikipedia.org/wiki/Massive_Multitask_Language_Understanding" target="_blank" rel="noopener">MMLU</a></b> across 57 subjects), reasoning depth (<b>GPQA</b>, expert-written
PhD-level), math (<b>MATH</b>, AIME, FrontierMath), and code (<b>HumanEval</b>, <b>MBPP</b>, <a href="https://en.wikipedia.org/wiki/SWE-Bench" target="_blank" rel="noopener">SWE-bench</a>).
<b>HELM</b> (Stanford) advocates holistic, multi-metric evaluation; the <b>Open LLM Leaderboard 2</b> is the
practical reference for open-weights models.</p>
<p>Important: most popular benchmarks are now contaminated. Always pair an old benchmark with a recent contamination-free one
(e.g., MMLU-Pro 2024, GPQA-Diamond, LiveCodeBench, AIME 2024+).</p>

## Papers

### Measuring Massive Multitask Language Understanding (MMLU)
- **Authors:** Hendrycks et al.
- **Year:** 2021
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2009.03300

57-subject knowledge benchmark; the most-quoted single number in LM papers.

### Beyond the Imitation Game (BIG-Bench)
- **Authors:** Srivastava et al.
- **Year:** 2023
- **Venue:** TMLR
- **URL:** https://arxiv.org/abs/2206.04615

204-task collaboratively-built benchmark; great for diversity.

### Holistic Evaluation of Language Models (HELM)
- **Authors:** Liang et al.
- **Year:** 2022
- **Venue:** TMLR
- **URL:** https://arxiv.org/abs/2211.09110

Multi-metric (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency). The right way to evaluate.

### GPQA: A Graduate-Level Google-Proof Q&A Benchmark
- **Authors:** Rein et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2311.12022

PhD-written questions even Google-augmented humans struggle with. Headline reasoning benchmark.

### Measuring Mathematical Problem Solving with the MATH Dataset
- **Authors:** Hendrycks et al.
- **Year:** 2021
- **URL:** https://arxiv.org/abs/2103.03874

Competition math; canonical reasoning eval.
