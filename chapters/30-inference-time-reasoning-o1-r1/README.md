---
id: 30
title: Inference-Time Reasoning: o1 and DeepSeek-R1
part: III. ML & AI in Chronological Order
---

<p>Through 2023, the answer to "how do we get LLMs to reason better?"
was: prompt them to think step by step (chapter 24), and scale the
training compute. In late 2024, OpenAI's <b>o1</b> and <a href="https://en.wikipedia.org/wiki/DeepSeek" target="_blank" rel="noopener">DeepSeek</a>'s
<b>R1</b> made the next move: <b>scale inference-time compute</b> by
training models to produce long internal chains of thought and then
optimise those chains with reinforcement learning against verifiable
rewards.</p>

<h4>The recipe (R1, in the open)</h4>
<ol>
  <li>Start from a strong base LM (DeepSeek-V3).</li>
  <li><b>RL with verifiable rewards</b>: math problems with known
  answers, code with unit tests. Reward = 1 if the final answer is
  correct, else 0. No human labels in the loop.</li>
  <li>The model learns to spend hundreds or thousands of tokens
  exploring, backtracking, and verifying — i.e., it discovers
  chain-of-thought from RL signal alone.</li>
  <li>Distil the long-CoT behaviour into a smaller, faster model for
  serving.</li>
</ol>

<h4>The two empirical findings</h4>
<ul>
  <li><b>Inference-time scaling is real</b>: accuracy on hard math and
  competitive coding scales smoothly with how many tokens of internal
  thought the model is allowed to spend.</li>
  <li><b>"Aha moments" emerge</b>: R1's RL run produces self-correction
  behaviour ("Wait, let me reconsider...") with no demonstration data,
  purely from outcome rewards. Reasoning is, at least in this regime,
  a learned strategy rather than a hard-coded prompt pattern.</li>
</ul>

<h4>Why this is the right closing chapter</h4>
<p>This is the second time in five years the field has discovered a new
<i>scaling axis</i>. Pretraining compute (2020). Then preference data
and instruction-following (2022-23). Now inference-time thinking
(2024-25). Each axis gave a step-change in capability that the previous
one would not have predicted. As of 2026, the open question is how far
this axis goes — and whether it composes with multimodal inputs, tool
use, and agentic memory in the way prior axes did. Chapters 18-22 of
this book pick that thread up in detail. Here, the story ends where
2026 begins.</p>

## Papers

### Learning to Reason with LLMs (o1)
- **Authors:** OpenAI
- **Year:** 2024
- **Venue:** OpenAI blog
- **URL:** https://web.archive.org/web/2026/https://openai.com/index/learning-to-reason-with-llms/

OpenAI's o1 announcement. Sparse on technical detail, generous with capability charts. The first public articulation of inference-time-compute scaling as a deliberate research direction.

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **Authors:** DeepSeek-AI
- **Year:** 2025
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2501.12948

The open recipe. Pure-RL reasoning training on a strong base, the 'aha moment' analysis, and distillation into smaller models. The most important open paper of 2025 for understanding modern reasoning models.

### Self-Consistency Improves Chain of Thought Reasoning in Language Models
- **Authors:** Wang et al.
- **Year:** 2022
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2203.11171

The pre-history: spend more inference compute by sampling many chains and majority-voting. The simple precursor to learned long-CoT reasoning.

## Extras
- [OpenAI: Learning to Reason with LLMs](https://web.archive.org/web/2026/https://openai.com/index/learning-to-reason-with-llms/)
