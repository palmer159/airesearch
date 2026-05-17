---
id: 11
title: Instruction-Following and Chat: IFEval, MT-Bench, Chatbot Arena
part: III. General-Purpose Benchmarks
---

# Instruction-Following and Chat: IFEval, MT-Bench, Chatbot Arena

*III. General-Purpose Benchmarks*

<p>The benchmarks in earlier chapters mostly ask: <i>can the model get the
right answer?</i> Once a model is going to be deployed as a chat assistant,
the more important question becomes: <i>does it follow instructions, sound
helpful, and stay on task across a conversation?</i> That is a much harder
thing to score. The three benchmarks here represent the three main
strategies the field has settled on.</p>

<h4>IFEval — programmatic instruction-following</h4>
<p><a href="https://arxiv.org/abs/2311.07911" target="_blank" rel="noopener">IFEval</a>
sidesteps the subjectivity problem by using only <i>verifiable</i>
instructions: "respond in exactly three bullet points", "include the word
'algorithm' twice", "do not use the letter e", "answer in JSON with these
keys", "end your response with the word 'done'". A simple Python checker
decides pass or fail per instruction. Scores are reported as
<b>prompt-level</b> (all instructions in the prompt satisfied) and
<b>instruction-level</b> (per-clause). It is cheap, deterministic, and
correlates well with how usable a model is as an API.</p>

<h4>MT-Bench — LM-as-judge on multi-turn chats</h4>
<p><a href="https://arxiv.org/abs/2306.05685" target="_blank" rel="noopener">MT-Bench</a>
introduced the now-standard <b>LM-as-judge</b> evaluation. 80 hand-written
two-turn questions span writing, roleplay, reasoning, math, coding,
extraction, STEM, and humanities. Each model's response is scored on a
1-10 scale by a strong judge model (originally GPT-4). The same paper also
introduced pairwise judging for Chatbot Arena.</p>
<ul>
  <li><b>Strengths:</b> covers free-form quality dimensions a closed
  multiple-choice test cannot — tone, helpfulness, formatting, refusal
  calibration.</li>
  <li><b>Weaknesses:</b> <i>position bias</i> (judges prefer whichever
  answer comes first), <i>verbosity bias</i> (longer answers score
  higher), <i>self-preference</i> (a judge tends to favour answers that
  look like its own), and the obvious circularity of grading models with
  models. Mitigations include swapping order, using multiple judges, and
  reporting agreement with human raters.</li>
</ul>

<h4>Chatbot Arena — human pairwise Elo</h4>
<p><a href="https://arxiv.org/abs/2403.04132" target="_blank" rel="noopener">Chatbot Arena</a>
(LMSYS, now <a href="https://lmarena.ai/" target="_blank" rel="noopener">lmarena.ai</a>)
sidesteps automated judging entirely. Users type any prompt, see two
anonymised responses, and pick the better one. Votes are aggregated into
an Elo-style rating, and the leaderboard is updated continuously. It is
the closest thing the field has to a real-world preference signal — at
the cost of being slow, unreproducible, and biased toward whatever users
happen to ask about.</p>

<h4>Reading the three together</h4>
<ul>
  <li>If IFEval is high but Arena is mid, the model is technically
  compliant but unpleasant.</li>
  <li>If Arena is high but IFEval is low, the model is charismatic but
  ignores constraints — bad for agentic and structured-output use cases.</li>
  <li>MT-Bench has been largely supplanted by <a href="https://lmarena.ai/" target="_blank" rel="noopener">Arena</a>
  and harder LM-judged successors (Arena-Hard, MixEval), but it is still a
  useful cheap regression test.</li>
</ul>

## Papers and references

### Instruction-Following Evaluation for Large Language Models (IFEval)
- **Authors:** Zhou, Lu, Misra, Brahma, Basu, Luan, Zhou, Hou
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2311.07911

Defines a set of verifiable instructions checkable by Python, and reports prompt-level and instruction-level accuracy. The standard objective instruction-following eval.

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- **Authors:** Zheng, Chiang, Sheng, Zhuang, Wu, Zhuang, Lin, Li, Li, Xing, Zhang, Gonzalez, Stoica
- **Year:** 2023
- **Venue:** NeurIPS 2023 D&B
- **URL:** https://arxiv.org/abs/2306.05685

Introduces MT-Bench (LM-as-judge with GPT-4) and the original Chatbot Arena methodology, plus a sober analysis of judge biases.

### Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
- **Authors:** Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhang, Zhu, Jordan, Gonzalez, Stoica
- **Year:** 2024
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2403.04132

Describes the LMSYS Chatbot Arena pipeline — pairwise human votes, Bradley-Terry / Elo aggregation, sampling and bias controls.

### AlpacaEval: An Automatic Evaluator of Instruction-following Models
- **Authors:** Li, Zhang, Dubois, Taori, Gulrajani, Guestrin, Liang, Hashimoto
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2305.14387

Companion line of work on length-controlled LM-as-judge evaluation. Useful background for understanding judge bias mitigations.

## Extras
- [Chatbot Arena leaderboard (lmarena.ai)](https://lmarena.ai/)
- [IFEval on GitHub (google-research)](https://github.com/google-research/google-research/tree/master/instruction_following_eval)
- [MT-Bench / FastChat repository](https://github.com/lm-sys/FastChat)
