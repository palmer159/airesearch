---
id: 2
title: What Makes a Good Benchmark
part: I. Foundations of LLM/SLM Evaluation
---

# What Makes a Good Benchmark

*I. Foundations of LLM/SLM Evaluation*

<p>Most benchmarks you'll encounter are bad in at least one specific,
fixable way.  Knowing the failure modes makes you a better consumer
of leaderboards and a much better designer of internal evals.</p>

<h4>The properties to look for</h4>
<ul>
  <li><b>Construct validity</b> — the benchmark actually measures the
  capability it claims to measure.  A "reasoning" benchmark that any
  retrieval-heavy model can solve by pattern-matching does not have
  construct validity.</li>
  <li><b>Coverage</b> — enough breadth across sub-skills, domains,
  difficulty levels, and input formats that no single trick wins.</li>
  <li><b>Discriminative power</b> — different models get visibly
  different scores.  If everyone clusters at 92–94%, the benchmark
  isn't telling you anything new.</li>
  <li><b>Headroom</b> — room left at the top.  Once frontier models
  exceed ~95% on a clean benchmark, it has effectively
  <b>saturated</b>: you can't tell a great model from a stunning one.
  This is what happened to the original GLUE, then SuperGLUE, then
  parts of MMLU.</li>
  <li><b>Easy automated grading</b> — a stable, reproducible scorer
  that doesn't itself need a frontier LLM in the loop.  Exact-match,
  unit tests, and regex graders are boring but trustworthy.</li>
  <li><b>Public vs. hidden splits</b> — public examples teach the
  community the format; a hidden test set you submit against keeps
  numbers honest.  BIG-Bench Hard, Kaggle-style hidden tests, and
  the SWE-bench leaderboard servers all use this pattern.</li>
</ul>

<h4>Two grading idioms you'll see everywhere</h4>
<ul>
  <li><b>Exact-match / multiple-choice</b> — the model's output
  string must equal the gold label, or its top-probability choice
  among A/B/C/D must match.  Cheap, deterministic, but brittle: a
  correct answer phrased differently scores zero, and MCQ removes
  the generation problem entirely.</li>
  <li><b>pass@k for code</b> — sample k completions, count the
  problem solved if any one passes the unit tests.  Originally
  defined in the
  <a href="https://arxiv.org/abs/2107.03374" target="_blank" rel="noopener">HumanEval / Codex paper</a>:</li>
</ul>

<pre>
pass@k = E_problems [ 1 - C(n - c, k) / C(n, k) ]

where n = total samples drawn per problem,
      c = number of those samples that pass,
      C(a, b) = a-choose-b
</pre>

<p>This unbiased estimator lets you draw n &gt;&gt; k samples once and
report pass@1, pass@10, pass@100 from the same run.</p>

<h4>Saturation and the next bench</h4>
<p>When 99% means "the bench is dead," the community responds by
building harder versions.
<a href="https://arxiv.org/abs/2210.09261" target="_blank" rel="noopener">BIG-Bench Hard</a>
is the 23 tasks from BIG-Bench where models still struggled; it
extended useful headroom by another generation of models.  HELM
itself is partly a response to GLUE-style saturation: instead of one
score going to 1.0, you get a dashboard where progress and
regressions are both visible.</p>

## Papers and references

### Holistic Evaluation of Language Models (HELM)
- **Authors:** Liang, Bommasani, Lee, et al.
- **Year:** 2022
- **Venue:** arXiv / TMLR
- **URL:** https://arxiv.org/abs/2211.09110

Beyond capability scoring: HELM treats benchmarks themselves as objects to evaluate (coverage, validity, missing metrics) and standardizes a multi-metric reporting format.

### Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them (BBH)
- **Authors:** Suzgun et al.
- **Year:** 2022
- **Venue:** arXiv / ACL Findings
- **URL:** https://arxiv.org/abs/2210.09261

The 23 BIG-Bench tasks where models scored below the average human rater. The de-facto "hard reasoning" subset and a useful case study in restoring headroom.

### Evaluating Large Language Models Trained on Code (HumanEval / Codex)
- **Authors:** Chen et al.
- **Year:** 2021
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2107.03374

Introduced HumanEval and the pass@k metric. The grading template — sample, run unit tests, count solved — is the basis for almost every modern code benchmark.

### BIG-Bench: Beyond the Imitation Game
- **Authors:** Srivastava et al.
- **Year:** 2022
- **Venue:** arXiv / TMLR
- **URL:** https://arxiv.org/abs/2206.04615

The original 200+ task collection. A long case study in coverage, construct validity, and what happens when you let hundreds of authors propose tasks.

### Goodhart's Law
- **Authors:** Wikipedia contributors
- **Year:** 2025
- **Venue:** Wikipedia
- **URL:** https://en.wikipedia.org/wiki/Goodhart%27s_law

The structural reason saturated benchmarks stop being informative: once the score is the goal, the score stops measuring the underlying capability.

## Extras
- [HELM Lite latest results](https://crfm.stanford.edu/helm/lite/latest/)
- [BIG-Bench repository (Google / collaboration)](https://github.com/google/BIG-bench)
- [HumanEval repository (OpenAI)](https://github.com/openai/human-eval)
