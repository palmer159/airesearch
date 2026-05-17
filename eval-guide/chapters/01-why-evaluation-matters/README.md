---
id: 1
title: Why Evaluation Matters: Capability vs. Behavior
part: I. Foundations of LLM/SLM Evaluation
---

# Why Evaluation Matters: Capability vs. Behavior

*I. Foundations of LLM/SLM Evaluation*

<p>Before we run a single benchmark, it's worth being precise about what
"evaluating a model" even means.  A language model is a probability
distribution over tokens; everything else — answering questions, writing
code, refusing harmful requests — is downstream behavior we coax out of
that distribution with a prompt.  Evaluation is the discipline of
quantifying how good those behaviors are.</p>

<h4>Three things people mean by "evaluation"</h4>
<ul>
  <li><b>Capability</b> — can the model, in principle, do the task?
  Solve a math problem, translate a sentence, write a working SQL
  query.  Measured with task accuracy on benchmarks like MMLU,
  GSM8K, HumanEval.</li>
  <li><b>Behavior</b> — how does it act in the wild?  Is it helpful,
  honest, calibrated, concise?  Measured with human preference,
  rubric-graded rollouts, and red-teaming.</li>
  <li><b>Alignment / safety</b> — does it refuse the things it should
  and only the things it should?  Measured with harm benchmarks,
  jailbreak suites, and policy compliance evals.</li>
</ul>

<h4>Intrinsic vs. extrinsic</h4>
<p>The oldest split in NLP eval is between <b>intrinsic</b> metrics
that score the model's distribution directly — most famously
<a href="https://en.wikipedia.org/wiki/Perplexity" target="_blank" rel="noopener">perplexity</a>
on a held-out corpus — and <b>extrinsic</b> metrics that score the
model on a downstream task.  Perplexity is cheap and continuous, which
makes it lovely for tracking pre-training runs, but it correlates only
loosely with what users actually care about.  A 5% perplexity
improvement might or might not move HumanEval at all.</p>

<h4>Why a single benchmark number lies</h4>
<p>Any one benchmark probes a narrow slice of behavior on a fixed
distribution of inputs.  Optimize for it and you get
<a href="https://en.wikipedia.org/wiki/Goodhart%27s_law" target="_blank" rel="noopener">Goodhart's law</a>
in action: the metric stops measuring the thing once the thing is
being measured.  Models can be trained, tuned, or even prompted in
ways that hill-climb a leaderboard while regressing on capabilities
the leaderboard doesn't see.</p>

<p>The fix is a <b>basket</b> of evals — broad coverage across
capabilities, behaviors, and risks, scored with multiple metrics,
across multiple prompt formats.  Stanford CRFM's
<a href="https://crfm.stanford.edu/helm/" target="_blank" rel="noopener">HELM</a>
("Holistic Evaluation of Language Models") is the canonical attempt
at this: dozens of scenarios crossed with seven metric categories
(accuracy, calibration, robustness, fairness, bias, toxicity,
efficiency).  Even that isn't the whole picture, but it's the right
shape: many tasks, many metrics, reported together rather than
collapsed into a single number.</p>

## Papers and references

### Holistic Evaluation of Language Models (HELM)
- **Authors:** Liang, Bommasani, Lee, et al.
- **Year:** 2022
- **Venue:** arXiv / TMLR
- **URL:** https://arxiv.org/abs/2211.09110

The reference framework for multi-metric, multi-scenario LM evaluation. Proposes evaluating across accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency on dozens of scenarios.

### BIG-Bench: Beyond the Imitation Game
- **Authors:** Srivastava et al.
- **Year:** 2022
- **Venue:** arXiv / TMLR
- **URL:** https://arxiv.org/abs/2206.04615

A 200+ task collaborative benchmark designed to probe capabilities current LMs are bad at. Defined the modern shape of broad-coverage capability evaluation.

### Perplexity
- **Authors:** Wikipedia contributors
- **Year:** 2025
- **Venue:** Wikipedia
- **URL:** https://en.wikipedia.org/wiki/Perplexity

The standard intrinsic metric for language models: exp of average per-token negative log-likelihood. Lower is better; correlates loosely with downstream task performance.

### Goodhart's Law
- **Authors:** Wikipedia contributors
- **Year:** 2025
- **Venue:** Wikipedia
- **URL:** https://en.wikipedia.org/wiki/Goodhart%27s_law

"When a measure becomes a target, it ceases to be a good measure." The structural reason single-benchmark optimization breaks down in practice.

### Evaluating Large Language Models: A Survey
- **Authors:** Chang et al.
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2307.03109

A broad survey covering what to evaluate (capabilities, alignment, safety), where to evaluate, and how — useful as a map of the eval landscape.

## Extras
- [HELM Lite leaderboard (Stanford CRFM)](https://crfm.stanford.edu/helm/lite/latest/)
- [Lilian Weng — LLM Evaluation](https://lilianweng.github.io/posts/2023-06-23-agent/)
