---
id: 20
title: GPT-3, Scaling Laws, and In-Context Learning
part: III. ML & AI in Chronological Order
---

<p>Two papers in 2020 made the modern frontier LM era inevitable. Kaplan et
al.'s <b><a href="https://en.wikipedia.org/wiki/Neural_scaling_law" target="_blank" rel="noopener">scaling laws</a></b> showed that loss is a smooth power-law function
of compute, model size, and data. Brown et al.'s <b><a href="https://en.wikipedia.org/wiki/GPT-3" target="_blank" rel="noopener">GPT-3</a></b> paper
operationalised that prediction at 175B parameters and demonstrated a new
phenomenon: <b><a href="https://en.wikipedia.org/wiki/In-context_learning" target="_blank" rel="noopener">in-context learning</a></b>.</p>

<h4>Scaling laws</h4>
<pre>
L(N) ≈ (N_c / N)^alpha     # loss as a function of parameters N
L(D) ≈ (D_c / D)^alpha_D   # and as a function of data D
</pre>
<p>For Transformer LMs trained on web text, loss scales smoothly and
predictably as you increase parameters or data — for many orders of
magnitude. There are no obvious diminishing returns until you blow past
the optimum data-to-parameters ratio. This single empirical curve is what
turned "let's scale up" from a guess into a plan.</p>

<h4>GPT-3 and in-context learning</h4>
<ul>
  <li>175B parameters, ~300B training tokens.</li>
  <li><b>Few-shot prompting</b>: provide a handful of input/output examples
  in the prompt, then a new input; the model completes the pattern. No
  gradient updates; no fine-tuning.</li>
  <li>The capability emerged smoothly with scale on some tasks and
  apparently abruptly on others. The "emergent abilities" debate
  (Wei et al. 2022, Schaeffer et al. 2023) traces back to GPT-3's
  task plots.</li>
</ul>

<h4>Why this chapter is the inflection point</h4>
<p>Before GPT-3, NLP was dozens of fine-tuned models on dozens of
datasets. After GPT-3, the entire field reorganised around a single
generic LM you prompt. The "Chinchilla" paper (Hoffmann et al., 2022)
later corrected the scaling laws — for a fixed compute budget, you should
spend more on data and less on parameters than Kaplan recommended — but
the basic "compute predicts loss" framework is intact and is now how every
serious lab plans training runs.</p>

## Papers

### Scaling Laws for Neural Language Models
- **Authors:** Jared Kaplan, Sam McCandlish et al.
- **Year:** 2020
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2001.08361

The empirical paper. Loss as a power law in N, D, and C. The plots are the most important figures of the decade in language modelling.

### Language Models are Few-Shot Learners (GPT-3)
- **Authors:** Tom Brown et al.
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2005.14165

The GPT-3 paper. The few-shot evaluation methodology is as influential as the model itself.

### Training Compute-Optimal Large Language Models (Chinchilla)
- **Authors:** Hoffmann et al.
- **Year:** 2022
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2203.15556

DeepMind's correction: at any compute budget, optimal training spends roughly equal effort on parameters and tokens, which means most models prior to 2022 were undertrained.

## Extras
- [How GPT-3 Works (Jay Alammar)](https://jalammar.github.io/how-gpt3-works-visualizations-animations/)
