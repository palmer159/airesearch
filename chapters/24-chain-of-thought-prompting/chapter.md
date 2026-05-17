---
id: 24
title: Chain-of-Thought Prompting
part: III. ML & AI in Chronological Order
---

<p>Wei et al.'s 2022 <b>chain-of-thought (CoT)</b> paper made one of those
findings that seems obvious in retrospect: if you prompt a sufficiently
large language model with worked examples that show their reasoning step
by step, the model will produce its own step-by-step reasoning on new
problems — and its accuracy on math, commonsense, and symbolic reasoning
benchmarks goes up sharply.</p>

<h4>The prompt</h4>
<pre>
Q: Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. How many now?
A: Roger started with 5. 2 cans of 3 is 6. 5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. They used 20, then bought 6. How many?
A: ...
</pre>

<h4>Two key empirical findings</h4>
<ul>
  <li><b>Emergence with scale</b>: CoT only helps once the underlying model
  is large enough (roughly &gt; 60B parameters in the original paper).
  Smaller models hallucinate plausible-looking reasoning that is
  arithmetically wrong.</li>
  <li><b>Zero-shot CoT</b> (Kojima et al., 2022): you don't even need
  exemplars — appending "Let's think step by step." to the prompt is
  often enough. Cheap, model-agnostic, surprisingly effective.</li>
</ul>

<h4>Why this is its own chapter</h4>
<p>CoT decouples reasoning quality from raw single-pass accuracy. With it,
the same model can be prompted into producing far better answers on
multi-step problems by spending more tokens on intermediate work. That
single observation is the seed of:</p>
<ul>
  <li><b>Self-consistency</b> (Wang et al.): sample multiple CoTs and
  majority-vote the final answer.</li>
  <li><b>Tree-of-thoughts</b>: search over reasoning paths.</li>
  <li><b>Inference-time reasoning models</b> (chapter 30): bake CoT into
  the model with RL on verifiable rewards.</li>
</ul>

<p>It is also the moment the field accepted that <i>compute at inference
time</i> is a real axis to scale on, not just compute at training time.</p>

## Papers

### Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
- **Authors:** Jason Wei et al.
- **Year:** 2022
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2201.11903

The CoT paper. Few-shot exemplars with explicit reasoning steps; sharp gains on GSM8K and similar benchmarks at sufficient model scale.

### Large Language Models are Zero-Shot Reasoners
- **Authors:** Kojima, Gu, Reid, Matsuo, Iwasawa
- **Year:** 2022
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2205.11916

Zero-shot CoT — 'Let's think step by step' as a universal prompt. Two-line change, large gains.

### Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **Authors:** Wang et al.
- **Year:** 2022
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2203.11171

Sample many CoTs and majority-vote the final answer. The simplest and still one of the most reliable inference-time tricks.
