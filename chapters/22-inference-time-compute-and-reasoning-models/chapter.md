---
id: 22
title: Inference-Time Compute and Reasoning Models
part: V. Reasoning & Agents
---

<p>The big 2024-25 shift: <b>train models to spend more tokens thinking before answering</b>. OpenAI's <b>o1</b>
and <b>o3</b> series, DeepSeek's <b>R1</b>, and Anthropic's <b>extended thinking</b> mode all trade latency for
correctness on hard reasoning, math, and code tasks.</p>
<p>Two key results:</p>
<ul>
  <li><b>Snell et al. (2024)</b>: scaling test-time compute can outperform scaling parameters for hard problems.</li>
  <li><b>DeepSeek-R1 (2025)</b>: pure RL with verifiable rewards (correct/incorrect on math/code) elicits long
      reasoning chains <i>from a base model with no SFT data</i>. Reproducibly trainable in the open.</li>
</ul>

## Papers

### Scaling LLM Test-Time Compute Optimally
- **Authors:** Snell et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2408.03314

Compute-matched test-time vs train-time scaling. Test-time wins on hard problems.

### OpenAI o1 System Card
- **Authors:** OpenAI
- **Year:** 2024
- **URL:** https://cdn.openai.com/o1-system-card.pdf

Public writeup of o1's reasoning approach + safety evaluations; light on architecture, sets the paradigm. (Direct PDF on cdn.openai.com.)

### DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning
- **Authors:** DeepSeek-AI
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2501.12948

Open recipe for reasoning models: GRPO over verifiable rewards. The most important open paper of 2025.

### Let's Verify Step by Step
- **Authors:** Lightman et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.20050

Process reward models — supervise each step of a CoT, not just the final answer.
