---
id: 23
title: InstructGPT, RLHF, and ChatGPT
part: III. ML & AI in Chronological Order
---

<p><a href="https://en.wikipedia.org/wiki/GPT-3" target="_blank" rel="noopener">GPT-3</a> was capable but unhelpful. It would happily complete a prompt in
the most likely way according to its training distribution — which is not
the same as doing what the user asked. <b><a href="https://en.wikipedia.org/wiki/InstructGPT" target="_blank" rel="noopener">InstructGPT</a></b> (Ouyang et al.,
2022) introduced the three-stage recipe that turned raw LMs into
assistants and led directly to <b><a href="https://en.wikipedia.org/wiki/ChatGPT" target="_blank" rel="noopener">ChatGPT</a></b> in November 2022.</p>

<h4>The three stages</h4>
<ol>
  <li><b>Supervised fine-tuning (SFT)</b> on a small set of
  human-written demonstrations of the desired behaviour.</li>
  <li><b>Reward model (RM) training</b>. Show humans pairs of model
  outputs for the same prompt; have them pick the better one. Train a
  separate Transformer to score outputs the way humans do.</li>
  <li><b>Reinforcement Learning from Human Feedback (<a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback" target="_blank" rel="noopener">RLHF</a>)</b>.
  Optimise the SFT model with PPO against the RM, with a KL penalty
  back to the SFT model so it doesn't drift into degenerate text.</li>
</ol>

<h4>Why this mattered more than the model size</h4>
<p>InstructGPT's 1.3B-parameter version was preferred to GPT-3 175B by
human raters on the OpenAI prompt distribution. Alignment to user intent
turned out to be at least as important as raw scale. ChatGPT, released
seven months later, was essentially "InstructGPT with a better base model
and a chat UI" and famously hit 100M users in two months.</p>

<h4>Successors</h4>
<ul>
  <li><b>Constitutional AI</b> (Anthropic) replaced human preference
  labels with AI-generated critiques against a written set of rules.</li>
  <li><b>DPO / IPO / KTO</b> reframe preference optimisation without RL,
  using simpler classification-style losses on preference pairs. They
  are the default in 2024-25 because they are easier to tune.</li>
  <li>RLHF / RLAIF still wins for the trickiest behaviour-shaping problems
  and is now used in combination with verifiable-reward RL on math/code
  (chapter 30).</li>
</ul>

## Papers

### Training language models to follow instructions with human feedback (InstructGPT)
- **Authors:** Long Ouyang et al.
- **Year:** 2022
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2203.02155

The InstructGPT paper. The three-stage SFT → RM → RLHF recipe; the headline finding that a 1.3B aligned model beats a 175B unaligned model on human preference.

### Constitutional AI: Harmlessness from AI Feedback
- **Authors:** Bai et al. (Anthropic)
- **Year:** 2022
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2212.08073

Replaces a portion of the human-feedback loop with a written constitution and AI-generated critiques. Cheaper and arguably more transparent.

### Direct Preference Optimization: Your Language Model is Secretly a Reward Model
- **Authors:** Rafailov, Sharma, Mitchell, Manning, Ermon, Finn
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2305.18290

DPO. Eliminates the explicit reward model and the RL step; trains directly on preference pairs with a closed-form classification loss.

## Extras
- [OpenAI: Introducing ChatGPT](https://openai.com/index/chatgpt/)
