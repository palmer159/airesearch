---
id: 10
title: Math: GSM8K, MATH, and AIME
part: III. General-Purpose Benchmarks
---

# Math: GSM8K, MATH, and AIME

*III. General-Purpose Benchmarks*

<p>Math benchmarks have outsized influence on how the field talks about
"reasoning". They are unambiguous (the answer is a number), they reward
multi-step thought, and they expose differences between models that
otherwise look similar on knowledge tests. This chapter walks through the
three math suites you will see in nearly every modern model card.</p>

<h4>GSM8K — grade-school word problems</h4>
<p><a href="https://arxiv.org/abs/2110.14168" target="_blank" rel="noopener">GSM8K</a>
is ~8,500 grade-school arithmetic word problems written by human
annotators, with full step-by-step solutions. Each problem takes 2-8
elementary operations. GSM8K is the canonical place to demonstrate that
<b>chain-of-thought prompting</b> works: directly asking for the answer
is far worse than asking the model to "think step by step" and then read
off the final number.</p>

<pre>
Q: Janet's ducks lay 16 eggs per day. She eats three for breakfast,
   bakes muffins with four, and sells the rest at the farmers' market
   for $2 per egg. How much does she make per day?

Reasoning: 16 - 3 - 4 = 9 eggs sold.  9 * 2 = 18.
Final answer: 18
</pre>

<h4>MATH — competition problems</h4>
<p>The <a href="https://arxiv.org/abs/2103.03874" target="_blank" rel="noopener">MATH dataset</a>
contains 12,500 problems from US high-school competitions (AMC, AIME,
USAMO and similar), labelled with difficulty 1-5 and split across algebra,
geometry, number theory, counting and probability, intermediate algebra,
prealgebra, and precalculus. Solutions require real techniques — telescoping
sums, modular arithmetic, generating functions — not just careful
arithmetic. As of 2025-2026 frontier reasoning models are above 90% on
MATH while strong SLMs are still in the 30-60% range, so it remains a
discriminating benchmark.</p>

<h4>AIME — the very hard tail</h4>
<p>AIME (American Invitational Mathematics Examination) is the qualifier
for the USA Math Olympiad. Each year produces only ~30 problems, all
integer-answered (000-999). It is small, but solving AIME problems
reliably requires substantial planning and case analysis, and it has
become the headline benchmark for "reasoning" models in the o1 / R1 /
Claude-thinking class. Numbers like "AIME 2024: 83%" are now common in
launch posts.</p>

<h4>How to evaluate math properly</h4>
<ul>
  <li><b>Use chain-of-thought.</b> Always. Direct-answer scores understate
  capability by 30-50 points on these benchmarks.</li>
  <li><b>Sampling matters.</b> Run with non-zero temperature and report
  <i>pass@1</i> averaged over k samples, or <i>maj@k</i> (self-consistency
  / majority voting) — a single greedy decode is high-variance.</li>
  <li><b>Tool use.</b> Many recent results allow Python execution.
  Always disclose: a 92% MATH score with a calculator is a different
  number than a 92% MATH score without one.</li>
  <li><b>Answer parsing.</b> A surprising amount of math-eval noise is
  the grader, not the model — boxed answers, fraction normalisation,
  units. Check the harness.</li>
</ul>

## Papers and references

### Training Verifiers to Solve Math Word Problems (GSM8K)
- **Authors:** Cobbe, Kosaraju, Bavarian, Chen, Jun, Kaiser, Plappert, Tworek, Hilton, Nakano, Hesse, Schulman
- **Year:** 2021
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2110.14168

Introduces GSM8K and a verifier-based reranking method. The dataset became the standard sanity-check for chain-of-thought reasoning.

### Measuring Mathematical Problem Solving With the MATH Dataset
- **Authors:** Hendrycks, Burns, Kadavath, Arora, Basart, Tang, Song, Steinhardt
- **Year:** 2021
- **Venue:** NeurIPS 2021 D&B
- **URL:** https://arxiv.org/abs/2103.03874

12,500 competition problems with worked solutions and difficulty labels. Still the dominant general math benchmark.

### Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **Authors:** Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou
- **Year:** 2022
- **Venue:** ICLR 2023
- **URL:** https://arxiv.org/abs/2203.11171

Sample many CoT solutions, take the majority answer. The technique behind every maj@k math number you have seen.

### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Authors:** Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le, Zhou
- **Year:** 2022
- **Venue:** NeurIPS 2022
- **URL:** https://arxiv.org/abs/2201.11903

Establishes that prompting models to show their work dramatically improves multi-step arithmetic and word-problem accuracy.

## Extras
- [GSM8K dataset on HuggingFace](https://huggingface.co/datasets/openai/gsm8k)
- [MATH dataset on HuggingFace](https://huggingface.co/datasets/hendrycks/competition_math)
- [AIME problems archive (Art of Problem Solving)](https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions)
