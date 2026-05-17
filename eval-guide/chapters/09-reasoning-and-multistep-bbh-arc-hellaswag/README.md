---
id: 9
title: Reasoning and Multi-Step: BBH, ARC, HellaSwag
part: III. General-Purpose Benchmarks
---

# Reasoning and Multi-Step: BBH, ARC, HellaSwag

*III. General-Purpose Benchmarks*

<p>MMLU-style tests reward recall plus a single step of inference. The
benchmarks in this chapter target the next thing up: multi-step reasoning
and commonsense inference. They are old enough that several of them are
near-saturated for frontier models — yet they remain genuinely useful for
comparing small language models, where headroom is still abundant.</p>

<h4>BBH — the hard tail of BIG-Bench</h4>
<p><a href="https://arxiv.org/abs/2210.09261" target="_blank" rel="noopener">BIG-Bench Hard</a>
is the 23-task subset of <a href="https://arxiv.org/abs/2206.04615" target="_blank" rel="noopener">BIG-Bench</a>
where, at the time of selection, the average human rater beat the best
model. Tasks include logical deduction, tracking shuffled objects, date
arithmetic, multi-step word problems, and Boolean expression evaluation.
Two things made BBH influential:</p>
<ul>
  <li>It is the benchmark where <b>chain-of-thought prompting</b> first
  showed dramatic, often double-digit improvements over direct answering.</li>
  <li>It is multi-format — some tasks are multiple-choice, some are
  free-form — which forces evaluation harnesses to handle both.</li>
</ul>

<h4>ARC — grade-school science, hard subset</h4>
<p>The <a href="https://arxiv.org/abs/1803.05457" target="_blank" rel="noopener">AI2 Reasoning Challenge</a>
splits standardised US grade-school science questions into <i>Easy</i> and
<i>Challenge</i> sets. The Challenge set was specifically the questions
where simple retrieval and word-matching baselines failed. ARC-Challenge
was a real test of reasoning in the GPT-2/GPT-3 era; today, leading
frontier LLMs score above 95% and it has effectively saturated. It still
discriminates well between sub-3B parameter SLMs.</p>

<h4>HellaSwag — adversarial sentence completion</h4>
<p><a href="https://arxiv.org/abs/1905.07830" target="_blank" rel="noopener">HellaSwag</a>
gives a short context (often a WikiHow or video caption) and four
candidate continuations, of which only one is plausible. The wrong
continuations were generated and adversarially filtered so that an earlier
generation of language models could not distinguish them from the right
answer — but humans easily can.</p>
<ul>
  <li><b>Random baseline:</b> 25%.</li>
  <li><b>Human:</b> ~95%.</li>
  <li><b>Frontier LLMs:</b> 95%+; the benchmark is essentially solved at
  the top end but is still informative for SLMs and base models.</li>
</ul>

<h4>How to use this trio today</h4>
<p>Treat ARC-Challenge and HellaSwag as <b>floor checks</b> — if a small
model is well below 80%, it is genuinely weak at basic commonsense and
science. Use BBH (especially with CoT) as the more discriminating signal
for reasoning, and pair it with GPQA or MATH when you care about the
upper end. None of these three should be a model's only reasoning eval
in 2026.</p>

## Papers and references

### Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them (BBH)
- **Authors:** Suzgun, Scales, Schärli, Gehrmann, Tay, Chung, Chowdhery, Le, Chi, Zhou, Wei
- **Year:** 2022
- **Venue:** ACL 2023 Findings
- **URL:** https://arxiv.org/abs/2210.09261

Defines BIG-Bench Hard and shows that chain-of-thought prompting closes much of the gap to human raters on these 23 tasks.

### Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models (BIG-Bench)
- **Authors:** Srivastava et al.
- **Year:** 2022
- **Venue:** TMLR
- **URL:** https://arxiv.org/abs/2206.04615

The umbrella BIG-Bench paper — 200+ tasks contributed by 400+ authors. BBH is the hard subset distilled out of this.

### Think You Have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge
- **Authors:** Clark, Cowhey, Etzioni, Khot, Sabharwal, Schoenick, Tafjord
- **Year:** 2018
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1803.05457

Introduces the ARC Easy and Challenge sets of US grade-school science questions and a knowledge corpus to go with them.

### HellaSwag: Can a Machine Really Finish Your Sentence?
- **Authors:** Zellers, Holtzman, Bisk, Farhadi, Choi
- **Year:** 2019
- **Venue:** ACL 2019
- **URL:** https://arxiv.org/abs/1905.07830

Adversarially filtered sentence-completion task built with Adversarial Filtering. Once near-impossible for LMs, now near-saturated.

## Extras
- [BIG-Bench GitHub repository](https://github.com/google/BIG-bench)
- [Open LLM Leaderboard (HuggingFace)](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
