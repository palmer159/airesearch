---
id: 18
title: Reproducibility and Statistical Significance
part: V. Methodology: Running Evals in Practice
---

# Reproducibility and Statistical Significance

*V. Methodology: Running Evals in Practice*

<p>Treat a benchmark number the way you would treat any experiment: it
is a noisy estimate of an underlying quantity. The two questions you must
answer about every reported score are <i>can someone re-run this</i> and
<i>is the difference real</i>.</p>

<h4>What to report so others can reproduce</h4>
<ul>
  <li>Model name <b>and</b> revision (HF commit SHA, GGUF quant level, lora adapter).</li>
  <li>Harness name <b>and</b> commit SHA.</li>
  <li>Exact prompt template (or its name in the harness).</li>
  <li>Sampling: temperature, top-p, top-k, max-new-tokens, seed.</li>
  <li>Hardware + inference engine (vLLM 0.6.3, llama.cpp commit, etc.) — batched
  inference is non-deterministic on GPUs even at temperature=0 because
  reductions reorder, so the engine matters.</li>
  <li>Few-shot k and which examples (the harness usually fixes this).</li>
</ul>

<h4>Is the difference real?</h4>
<p>A benchmark with N items and a binary pass/fail metric has a standard
error of roughly sqrt(p(1-p)/N). For MMLU (N≈14k) at p=0.7 that is ≈0.4
points; a 1-point gap is borderline. For GPQA Diamond (N=198) at p=0.5 that
is ≈3.5 points; a 5-point gap is barely real. Bootstrap confidence intervals
let you compute this without assuming a Gaussian — re-sample the items with
replacement many times, recompute the score, take the 2.5/97.5 percentiles.</p>

<pre>
# 95% bootstrap CI for accuracy on N items
import numpy as np
correct = np.array([...])           # 1/0 per item, length N
B = 10_000
samples = [correct[np.random.randint(0, len(correct), len(correct))].mean()
           for _ in range(B)]
lo, hi = np.percentile(samples, [2.5, 97.5])
</pre>

<p>For pairwise comparisons (model A vs model B on the same items) use a
paired bootstrap or McNemar's test — they are tighter than two independent
CIs because they exploit per-item correlation.</p>

<h4>Hidden non-determinism</h4>
<p>Even with temperature=0 and a fixed seed, vLLM, TGI, and SGLang can
produce different outputs across batch sizes due to floating-point reduction
order. Always pin engine version <i>and</i> batch configuration. The Open
LLM Leaderboard pins both.</p>

## Papers and references

### What's In My Big Data? (and reproducibility crises in LM eval)
- **Authors:** Elazar et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.20707

Argues that without dataset and decoding transparency, reported LM scores are not reproducible — a position paper widely cited by leaderboard maintainers.

### Don't Make Your LLM an Evaluation Benchmark Cheater
- **Authors:** Zhou et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2311.01964

Empirically shows how minor harness differences (prompt format, log-likelihood vs generation, normalization) shift MMLU and other scores by 5-20 points across the 'same' eval.

### A Critical Evaluation of Evaluations for Long-form Question Answering
- **Authors:** Xu et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.18201

Practical guide on reporting confidence intervals and avoiding the 'one-run-and-done' trap; the bootstrap recipes here generalize beyond LFQA.

### Bootstrap Methods: Another Look at the Jackknife
- **Authors:** Bradley Efron
- **Year:** 1979
- **Venue:** Annals of Statistics
- **URL:** https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full

The original bootstrap paper — the technique behind every benchmark CI you should be reporting.

### Open LLM Leaderboard v2
- **Authors:** Fourrier et al.
- **Year:** 2024
- **Venue:** HuggingFace
- **URL:** https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard

Pins lm-eval-harness commits, prompt formats, and engine settings so numbers stay comparable across submissions; documents its decoding contract publicly.

## Extras
- [Bootstrapping (Wikipedia)](https://en.wikipedia.org/wiki/Bootstrapping_(statistics))
- [HF blog: What's going on with the Open LLM Leaderboard?](https://huggingface.co/blog/open-llm-leaderboard-mmlu)
- [vLLM determinism notes](https://docs.vllm.ai/en/latest/serving/faq.html)
