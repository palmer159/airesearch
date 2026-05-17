---
id: 8
title: Knowledge and Reasoning: MMLU, MMLU-Pro, GPQA
part: III. General-Purpose Benchmarks
---

# Knowledge and Reasoning: MMLU, MMLU-Pro, GPQA

*III. General-Purpose Benchmarks*

<p>If you have ever skimmed a model card and seen a single number labelled
"MMLU: 86.4", this chapter is about what that number is actually measuring,
and why people increasingly report MMLU-Pro and GPQA alongside it.</p>

<h4>MMLU — the breadth test</h4>
<p><a href="https://arxiv.org/abs/2009.03300" target="_blank" rel="noopener">MMLU</a>
(Massive Multitask Language Understanding) is a 4-choice multiple-choice
exam covering 57 subjects — high-school math, US history, professional
medicine, machine learning, moral disputes, and so on. The score is plain
accuracy: did the model pick the right letter?</p>
<ul>
  <li><b>Format.</b> Usually reported as <i>5-shot</i> (five worked examples
  in the prompt) for base models and <i>0-shot CoT</i> for chat models.</li>
  <li><b>Random baseline.</b> 25%. Frontier models now score 87-90%, which
  means the headroom is mostly in the trickiest professional sub-tasks.</li>
  <li><b>Saturation.</b> By 2024 the top of the leaderboard was bunched
  inside a couple of points, and several errors in the gold labels had been
  catalogued — a sign the benchmark was running out of signal.</li>
</ul>

<pre>
Q: One of the reasons that the government discourages and regulates monopolies is that
   (A) producer surplus is lost and consumer surplus is gained.
   (B) monopoly prices ensure productive efficiency but cost society allocative efficiency.
   (C) monopoly firms do not engage in significant research and development.
   (D) consumer surplus is lost with higher prices and lower levels of output.
Answer: D
</pre>

<h4>MMLU-Pro — harder and less contaminated</h4>
<p><a href="https://arxiv.org/abs/2406.01574" target="_blank" rel="noopener">MMLU-Pro</a>
keeps the same idea but bumps the choice set from 4 to 10, filters out
trivially answerable questions, and adds reasoning-heavy items pulled from
textbooks and STEM exams. The random baseline drops to 10%, and even
strong models lose 15-25 points relative to their MMLU score, which gives
the leaderboard room to breathe again.</p>

<h4>GPQA — Google-proof graduate science</h4>
<p><a href="https://arxiv.org/abs/2311.12022" target="_blank" rel="noopener">GPQA</a>
is a small (≈450 question) set of biology, physics, and chemistry questions
written by domain PhDs. It is "Google-proof" by construction: validators
with web access but outside the field still got most of them wrong. The
"Diamond" subset (~198 items) is the hardest tier and the one usually
quoted. Numbers in the 50-70% range here separate genuinely strong
reasoners from models that are merely well-read.</p>

<h4>How to read the numbers</h4>
<ul>
  <li>Always check whether a score is 0-shot, 5-shot, or CoT — they are not
  comparable.</li>
  <li>Suspect contamination when MMLU is unusually high relative to
  MMLU-Pro and GPQA on the same model.</li>
  <li>For SLMs, MMLU is still useful; for frontier LLMs, GPQA-Diamond and
  MMLU-Pro carry more information.</li>
</ul>

## Papers and references

### Measuring Massive Multitask Language Understanding (MMLU)
- **Authors:** Hendrycks, Burns, Basart, Zou, Mazeika, Song, Steinhardt
- **Year:** 2020
- **Venue:** ICLR 2021
- **URL:** https://arxiv.org/abs/2009.03300

The original MMLU benchmark — 57 subjects, 4-choice MCQ, the de facto knowledge-and-reasoning test for LLMs.

### MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark
- **Authors:** Wang, Ma, Zhang, Ni, Chandra, Guo, Ren, Arulraj, He, Jiang, Li, Liu, Wang, Yang, Sun, Bhardwaj, Boukouvalas, Wang, Sun, Tan, Yue, Yu, Cheng, Chen
- **Year:** 2024
- **Venue:** NeurIPS 2024 D&B
- **URL:** https://arxiv.org/abs/2406.01574

Ten-choice, contamination-filtered, reasoning-heavy successor to MMLU. Used to re-spread the leaderboard once MMLU saturated.

### GPQA: A Graduate-Level Google-Proof Q&A Benchmark
- **Authors:** Rein, Hou, Stickland, Petty, Pang, Dirani, Michael, Bowman
- **Year:** 2023
- **Venue:** COLM 2024
- **URL:** https://arxiv.org/abs/2311.12022

PhD-written biology, physics, and chemistry questions designed to resist web search. The Diamond subset is the standard reasoning-frontier eval.

### Beyond the Imitation Game (BIG-Bench)
- **Authors:** Srivastava et al.
- **Year:** 2022
- **Venue:** TMLR
- **URL:** https://arxiv.org/abs/2206.04615

Companion benchmark to MMLU — 200+ tasks contributed by the community. Important context for why narrower harder suites like GPQA exist.

## Extras
- [Open LLM Leaderboard (HuggingFace)](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [MMLU on Wikipedia](https://en.wikipedia.org/wiki/Massive_Multitask_Language_Understanding)
- [MMLU-Pro leaderboard (HuggingFace)](https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro)
