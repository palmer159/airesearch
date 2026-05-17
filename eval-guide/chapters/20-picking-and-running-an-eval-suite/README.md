---
id: 20
title: Picking and Running an Eval Suite: A Practical Checklist
part: V. Methodology: Running Evals in Practice
---

# Picking and Running an Eval Suite: A Practical Checklist

*V. Methodology: Running Evals in Practice*

<p>The hardest part of evaluation is not running the harness; it is
picking the right benchmarks for the question you actually have. Most
mistakes here are scope errors — using a chat leaderboard to predict
production retrieval quality, or using HumanEval to predict whether a model
can handle your repo.</p>

<h4>Step 1 — define the question</h4>
<ul>
  <li><b>Capability</b> ("can this model do X at all?") — pick narrow,
  high-headroom benches: GPQA, MATH-level-5, SWE-bench Verified.</li>
  <li><b>Deployment fitness</b> ("is this model good enough for my product?")
  — build a private bench from your own traffic; public benches are a
  triangulation, not the answer.</li>
  <li><b>Alignment / safety</b> — IFEval, refusal-rate suites, red-team sets.</li>
</ul>

<h4>Step 2 — pick 3-5 benches that triangulate</h4>
<p>One general-knowledge (MMLU-Pro), one reasoning (GPQA or BBH), one math
(MATH or GSM8K), one coding (HumanEval or BigCodeBench). For coding agents
add SWE-bench Verified. A single number lies; three numbers that all move
together is a signal.</p>

<h4>Step 3 — defend against contamination</h4>
<p>Prefer benches with a Verified / Live / hidden split (LiveCodeBench
post-cutoff slice; SWE-bench Verified). For older benches, run an n-gram
overlap check between your model's training data (where known) and the
test set, or at minimum cite the model's training-data cutoff vs the
benchmark release date.</p>

<h4>Step 4 — pin everything and run</h4>
<pre>
# Minimal lm-eval-harness invocation
lm_eval \
  --model vllm \
  --model_args pretrained=Qwen/Qwen2.5-7B-Instruct,dtype=bfloat16 \
  --tasks mmlu_pro,gpqa_diamond,bbh,ifeval,gsm8k \
  --num_fewshot 0 \
  --batch_size auto \
  --log_samples \
  --output_path runs/qwen25-7b-instruct.json
</pre>

<h4>Step 5 — compare and publish</h4>
<p>Always run ≥2 baselines on the same setup (a known-strong open model and
a known-weak one). Publish prompts, harness commit, model commit, sampling
parameters, and bootstrap CIs. If you cannot publish all of these, you have
a sales pitch, not an evaluation.</p>

## Papers and references

### Holistic Evaluation of Language Models (HELM)
- **Authors:** Liang et al.
- **Year:** 2022
- **Venue:** Stanford CRFM
- **URL:** https://arxiv.org/abs/2211.09110

The original HELM paper — the multi-axis eval philosophy that motivates a 3-5 benchmark portfolio rather than one number.

### Are Emergent Abilities of Large Language Models a Mirage?
- **Authors:** Schaeffer et al.
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2304.15004

Argues that benchmark choice (especially the metric — accuracy vs token-level log-prob) can manufacture or hide phase transitions. A reminder to triangulate.

### Investigating Data Contamination in Modern Benchmarks for Large Language Models
- **Authors:** Sainz et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.18018

Catalogues contamination across MMLU, GSM8K, HumanEval and others; provides the n-gram overlap recipe for defending your own runs.

### lm-evaluation-harness
- **Authors:** Gao et al.
- **Year:** 2023
- **Venue:** EleutherAI
- **URL:** https://github.com/EleutherAI/lm-evaluation-harness

The runner referenced by the example invocation above. Supports vLLM, HuggingFace, and OpenAI-compatible endpoints behind a single CLI.

### The Open LLM Leaderboard v2 paper
- **Authors:** Fourrier et al.
- **Year:** 2024
- **Venue:** HuggingFace
- **URL:** https://huggingface.co/blog/open-llm-leaderboard-rlhf

Documents the exact six-bench portfolio HF landed on after a year of v1 saturation. A defensible default if you do not have a strong opinion.

## Extras
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)
- [HELM lite leaderboard](https://crfm.stanford.edu/helm/lite/latest/)
- [vLLM (recommended inference engine)](https://github.com/vllm-project/vllm)
