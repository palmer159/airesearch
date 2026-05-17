---
id: 17
title: Prompting, Few-Shot, and Sampling
part: V. Methodology: Running Evals in Practice
---

# Prompting, Few-Shot, and Sampling

*V. Methodology: Running Evals in Practice*

<p>An open-weight model has no single "score". The number you get on a
benchmark depends on how you prompted it, how many examples you showed it,
and how you sampled. If you change any of these and forget to say so, you
have not measured the model — you have measured your own setup.</p>

<h4>Zero-shot, few-shot, and chain-of-thought</h4>
<ul>
  <li><b>Zero-shot</b>: just the question. Hard for small models, fair for
  instruction-tuned ones.</li>
  <li><b>Few-shot (k-shot)</b>: prepend k worked examples. MMLU is canonically
  reported 5-shot. Big wins for base models, modest for instruct models.</li>
  <li><b>Chain-of-thought</b>: tell the model "think step by step". GSM8K and
  MATH are usually CoT. Many leaderboards now use 0-shot CoT for everything.</li>
</ul>

<p>Prompt format matters more than people think. The same MMLU question
phrased "Question: X\nA) … B) …" vs "&lt;|user|&gt; X" can swing 5-10 points.
Always publish the exact template; cite the harness's default if you used
one.</p>

<h4>Sampling parameters</h4>
<p>Three knobs: temperature (how peaky the next-token distribution is), top-p
(keep only the smallest set of tokens whose mass ≥ p), and top-k (keep the k
most-likely). For greedy/deterministic eval use temperature=0 and seed your
RNG. For pass@k metrics — where you want to measure "given k tries, did at
least one work" — use temperature ≈ 0.6-0.8 and draw k samples per problem.</p>

<pre>
# pass@k bias-corrected estimator (Codex paper)
# n = total samples drawn, c = number that passed, k = budget
pass_at_k(n, c, k) = 1 - C(n - c, k) / C(n, k)
</pre>

<h4>Tooling</h4>
<p>EleutherAI's <b>lm-evaluation-harness</b> is the closest thing to a
community standard. It handles few-shot formatting, log-likelihood vs
generative grading, and dozens of public benchmarks. Hugging Face's Open LLM
Leaderboard pins specific commits of it so numbers are comparable.</p>

<p>For coding evals use BigCode's <code>bigcode-evaluation-harness</code> for
HumanEval/MBPP/MultiPL-E and the official SWE-bench harness for agentic
tasks.</p>

## Papers and references

### Language Models are Few-Shot Learners (GPT-3)
- **Authors:** Brown et al.
- **Year:** 2020
- **URL:** https://arxiv.org/abs/2005.14165

Coined few-shot in-context learning as the eval mode for instruction-less base models. The k=5 / k=32 conventions trace to this paper.

### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Authors:** Wei et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2201.11903

The original CoT paper — adding 'let's think step by step' style demonstrations gave huge boosts on GSM8K and arithmetic, and reframed how reasoning benchmarks are run.

### Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **Authors:** Wang et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2203.11171

Sample many CoT traces at temperature > 0, take the majority answer. The standard 'maj@N' protocol on math benches comes from here.

### Evaluating Large Language Models Trained on Code (Codex / HumanEval)
- **Authors:** Chen et al.
- **Year:** 2021
- **URL:** https://arxiv.org/abs/2107.03374

Defines pass@k and the bias-corrected estimator everyone now reports. Section 2 of the paper is the source of truth for the formula.

### A Framework for Few-Shot Language Model Evaluation
- **Authors:** Gao et al.
- **Year:** 2023
- **Venue:** GitHub / EleutherAI
- **URL:** https://github.com/EleutherAI/lm-evaluation-harness

lm-eval-harness — the community-standard runner. Pinning a specific commit hash is the difference between comparable and incomparable numbers.

### Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design
- **Authors:** Sclar et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.11324

Same task, same model, eight cosmetic prompt variations: scores swing >50 points. The empirical case for always publishing the exact template.

## Extras
- [lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness)
- [bigcode-evaluation-harness](https://github.com/bigcode-project/bigcode-evaluation-harness)
- [HuggingFace generation parameter docs](https://huggingface.co/docs/transformers/generation_strategies)
