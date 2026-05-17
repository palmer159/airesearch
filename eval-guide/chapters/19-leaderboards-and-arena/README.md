---
id: 19
title: Leaderboards: Open LLM, BigCode, SWE-bench, Arena
part: V. Methodology: Running Evals in Practice
---

# Leaderboards: Open LLM, BigCode, SWE-bench, Arena

*V. Methodology: Running Evals in Practice*

<p>Leaderboards do two jobs at once: they aggregate evals into a single
ranking, and they constrain methodology so the ranking is meaningful. The
ranking is the part most people look at; the constrained methodology is the
part that actually matters.</p>

<h4>Hugging Face Open LLM Leaderboard v2</h4>
<p>The default for general open-weight LLM evaluation. v2 (2024) replaced
the saturated v1 mix with six harder benchmarks: <b>IFEval</b>,
<b>BBH</b>, <b>MATH</b> (level-5 subset), <b>GPQA</b>, <b>MUSR</b>,
<b>MMLU-Pro</b>. All run via lm-eval-harness at pinned commits.</p>

<h4>BigCode Models Leaderboard</h4>
<p>The coding-specific counterpart. Tracks HumanEval, MBPP, MultiPL-E across
~18 languages, plus throughput metrics. Useful for choosing a base coding
model before going to SWE-style benches.</p>

<h4>SWE-bench Leaderboard</h4>
<p>The flagship for coding agents — resolved-rate on SWE-bench
Verified/Lite/Live, broken down by harness (SWE-agent, Agentless, OpenHands,
proprietary). Look at the trajectory logs published alongside each
submission; opaque submissions are worth less.</p>

<h4>Chatbot Arena (lmarena.ai)</h4>
<p>Pairwise human preferences turned into Elo ratings via Bradley-Terry. It
captures something none of the static benches do — overall <i>chat
helpfulness</i> as judged by real users — but it is sensitive to style
(verbose, friendly answers do well) and is hard to use for narrow
capabilities.</p>

<h4>Aider LLM Leaderboard</h4>
<p>A small but well-loved practical bench: 133 Python edit tasks where the
model has to apply diffs to existing files. Tracks 'percent of edits that
work' separately from 'percent of test cases that pass'. Closer to real IDE
usage than HumanEval.</p>

<p><b>Reading rule:</b> a model that wins one leaderboard and loses another
is not a contradiction — it is a signal that the leaderboards measure
different things. Triangulate.</p>

## Papers and references

### Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
- **Authors:** Chiang et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.04132

Describes the LMSys / lmarena.ai pairwise-vote pipeline and the Bradley-Terry Elo math behind the ranking. Required reading before quoting Arena scores.

### Open LLM Leaderboard v2 (HuggingFace blog)
- **Authors:** Fourrier et al.
- **Year:** 2024
- **Venue:** HuggingFace
- **URL:** https://huggingface.co/blog/open-llm-leaderboard-rlhf

Why v1 was retired (saturation, contamination), what v2 measures, and how prompts/decoders are pinned. The blog is the authoritative description.

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- **Authors:** Zheng et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2306.05685

Establishes that GPT-4 judging correlates ~0.8 with human prefs on chat tasks but has known biases (verbosity, position). Background for any leaderboard that uses LM-as-judge.

### SWE-bench Verified
- **Authors:** OpenAI Preparedness team
- **Year:** 2024
- **Venue:** OpenAI
- **URL:** https://web.archive.org/web/2026/https://openai.com/index/introducing-swe-bench-verified/

The 500-task human-validated subset of SWE-bench. The official leaderboard at swebench.com tracks resolved-rate on this set as the headline number for coding agents.

### Aider's LLM Leaderboards
- **Authors:** Paul Gauthier
- **Year:** 2024
- **Venue:** aider.chat
- **URL:** https://aider.chat/docs/leaderboards/

Practitioner-oriented coding leaderboard built around real diff-application tasks. Documents prompt, harness, and methodology in full.

## Extras
- [Open LLM Leaderboard v2](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [BigCode Models Leaderboard](https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard)
- [SWE-bench leaderboard](https://www.swebench.com/)
- [LMArena](https://lmarena.ai/)
