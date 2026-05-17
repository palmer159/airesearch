---
id: 12
title: Function-Level: HumanEval, MBPP, MultiPL-E
part: IV. Coding and SWE Benchmarks
---

# Function-Level: HumanEval, MBPP, MultiPL-E

*IV. Coding and SWE Benchmarks*

<p>Coding benchmarks started small and concrete: give the model a
docstring, ask it to write a single Python function, then run a hidden
test suite. <b>HumanEval</b> (OpenAI, 2021, released alongside the Codex
paper) is the canonical example — 164 hand-written problems, each with a
function signature, a natural-language prompt, and a few unit tests.
<b>MBPP</b> (Google, 2021) — "Mostly Basic Programming Problems" — is
the same shape, scaled up to 974 short Python tasks crowd-sourced from
entry-level programmers.</p>

<h4>The pass@k metric</h4>
<p>Both benchmarks measure <b>pass@k</b>: the probability that at least
one of <code>k</code> sampled completions passes all unit tests. To
reduce variance you draw <code>n &gt;= k</code> samples per problem,
count how many are correct (<code>c</code>), and use the unbiased
estimator from the Codex paper:</p>

<pre>
                          /  C(n - c, k)  \
pass@k  =  E_problems  | 1 - ------------- |
                          \    C(n, k)    /
</pre>

<p>pass@1 is what you usually report; pass@10 and pass@100 show how much
the model gains from re-sampling. Temperature matters — pass@1 is
typically reported at <code>T = 0.2</code>, pass@k at higher T so the
samples are diverse.</p>

<h4>MultiPL-E: the same benchmarks, 18 languages</h4>
<p><b>MultiPL-E</b> (Cassano et al., 2022) translates HumanEval and MBPP
into roughly 18 programming languages — JavaScript, Java, C++, Rust, Go,
Lua, R, and so on — by mechanically rewriting the prompts and tests.
This is the cheapest way to check whether a model that crushes Python
HumanEval actually generalises beyond Python. Most do worse outside
their training distribution; the gap is informative.</p>

<h4>Why these are now mostly a sanity check</h4>
<p>Frontier models score above 90% on HumanEval pass@1, and decent
open-source SLMs (DeepSeek-Coder, Qwen-Coder, StarCoder2) score in the
70-90% range. The benchmark has effectively saturated for the models
people care about most. It still has uses:</p>
<ul>
  <li><b>SLM differentiation</b> — between a 1B and a 7B coding model,
  HumanEval still discriminates.</li>
  <li><b>Quick smoke test</b> — it runs in minutes and catches obvious
  regressions in fine-tuning or quantisation.</li>
  <li><b>Multilingual probing</b> via MultiPL-E — saturation in Python
  does not imply saturation in Rust.</li>
</ul>

<p>For anything more ambitious, you graduate to the harder benches in
chapters 13-15. But every coding-eval pipeline should still produce a
HumanEval number, if only as a baseline that lets you compare against
the thousands of papers that already report one. Treat it as the
push-up test, not the marathon.</p>

## Papers and references

### Evaluating Large Language Models Trained on Code (Codex / HumanEval)
- **Authors:** Chen, Tworek, Jun, Yuan, Pinto, Kaplan, et al.
- **Year:** 2021
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2107.03374

Introduces Codex, HumanEval (164 problems), and the unbiased pass@k estimator. The canonical first coding benchmark.

### Program Synthesis with Large Language Models (MBPP)
- **Authors:** Austin, Odena, Nye, Bosma, Michalewski, Dohan, et al.
- **Year:** 2021
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2108.07732

MBPP — 974 short Python problems written by entry-level programmers, plus a hand-curated subset and an edited 'sanitised' version.

### MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation
- **Authors:** Cassano, Gouwar, Nguyen, Nguyen, Phipps-Costin, et al.
- **Year:** 2022
- **Venue:** arXiv / TSE
- **URL:** https://arxiv.org/abs/2208.08227

Translates HumanEval and MBPP into ~18 languages by mechanically rewriting prompts and tests. The default multilingual coding bench.

### HumanEval+ / EvalPlus: Are Your Tests Really Catching Bugs?
- **Authors:** Liu, Xia, Wang, Zhang
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2305.01210

Augments HumanEval and MBPP with 80x more tests, exposing many 'passing' samples as actually wrong. Use HumanEval+ if you can.

## Extras
- [OpenAI human-eval repo (reference pass@k implementation)](https://github.com/openai/human-eval)
- [EvalPlus leaderboard (HumanEval+ / MBPP+)](https://evalplus.github.io/leaderboard.html)
- [MultiPL-E on GitHub](https://github.com/nuprl/MultiPL-E)
