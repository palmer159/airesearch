---
id: 6
title: Small Language Models: Phi, SmolLM, TinyLlama
part: II. The Open Model Landscape
---

# Small Language Models: Phi, SmolLM, TinyLlama

*II. The Open Model Landscape*

<p>If you're benchmarking, you should care about small models out of pure
self-interest.  A 1.7B model evaluates in a fraction of the time of a 70B
one, runs on a single consumer GPU, and lets you do ten ablations in the
time one frontier eval finishes.  The 2024–2025 wave of SLMs proved
something stronger than that: with curated data, small can be genuinely
useful, not just educational.</p>

<h4>Phi (Microsoft)</h4>
<p>The <a href="https://arxiv.org/abs/2404.14219" target="_blank" rel="noopener">Phi-3</a>
series — Phi-3-mini (3.8B), Phi-3-small (7B), Phi-3-medium (14B) — built on
the slogan "textbooks are all you need."  The thesis: train on tightly
curated, instruction-rich, "textbook-quality" synthetic and filtered data,
and a small model can match much larger ones on reasoning and code.  Phi-3.5
extended this with a small MoE variant, and
<a href="https://arxiv.org/abs/2412.08905" target="_blank" rel="noopener">Phi-4</a>
(14B) doubled down on synthetic-data curation and reasoning-focused
post-training.  All available on the
<a href="https://huggingface.co/microsoft" target="_blank" rel="noopener">microsoft</a>
HF org.</p>

<h4>SmolLM and SmolLM2 (Hugging Face)</h4>
<p><a href="https://huggingface.co/blog/smollm" target="_blank" rel="noopener">SmolLM</a>
ships at 135M, 360M, and 1.7B; the
<a href="https://huggingface.co/blog/smollm2" target="_blank" rel="noopener">SmolLM2</a>
follow-up improves all three on the same size ladder.  These are trained on
fully open data (Cosmopedia, FineWeb-Edu) and are a clean choice if you want
to evaluate or fine-tune at the very small end without license friction.
The 1.7B in particular is a useful "is this even a hard task?" probe — if it
can do your task, you don't need a bigger model.</p>

<h4>TinyLlama and Gemma 2B</h4>
<p>TinyLlama is a 1.1B model trained on 3T tokens — a community
demonstration that Chinchilla-optimal smallness pushed even further on
extra data still pays off.  Gemma 2B (covered in the previous chapter) is
distilled from a much larger teacher and remains one of the strongest 2B
models for general use.</p>

<h4>Why SLMs matter for evaluation</h4>
<ul>
  <li><b>Speed.</b>  Faster inference means more eval runs per day,
      which means better statistics — fewer single-seed claims, more
      confidence intervals.</li>
  <li><b>Cost.</b>  You can run a full benchmark suite against five SLMs
      for the cost of one pass against a 70B model.</li>
  <li><b>Reproducibility.</b>  Smaller models are easier to host, easier
      to quantize, and easier to ship as a fixed artifact in a paper or a
      reproducible experiment.</li>
  <li><b>Headroom intuition.</b>  Knowing where the SLM ceiling is for a
      task tells you whether the larger model's win is "broad capability"
      or just "more memorized facts."</li>
</ul>

<pre>
model         params    notes
------------  --------  ---------------------------------------------
SmolLM2-135M  135M      smallest end of the ladder; great for ablations
SmolLM2-1.7B  1.7B      open data, reasonable instruction following
TinyLlama     1.1B      community SLM; 3T training tokens
Gemma 2 2B    2B        distilled from a larger teacher
Phi-3-mini    3.8B      curated-data SLM, strong on reasoning
Phi-4         14B       reasoning-focused post-training, top of the SLM range
</pre>
<p>Build the habit: every time you reach for a 70B model, ask whether a
1.7B SmolLM2 or a 3.8B Phi-3-mini already nails the task.  Often it does.</p>

## Papers and references

### Phi-3 Technical Report
- **Authors:** Abdin et al. (Microsoft)
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2404.14219

The 'curated data, modest size' thesis applied at 3.8B/7B/14B. The clearest single document on why SLMs got so good so fast.

### Phi-4 Technical Report
- **Authors:** Microsoft Research
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2412.08905

14B model with heavy synthetic-data and reasoning-focused post-training. A useful study in pushing SLM quality without growing parameters.

### SmolLM: blazingly fast and remarkably powerful
- **Authors:** Hugging Face
- **Year:** 2024
- **Venue:** HF blog
- **URL:** https://huggingface.co/blog/smollm

Introduces the SmolLM family on fully open data. Read alongside the SmolLM2 follow-up for the recipe evolution.

### SmolLM2: when smol goes big
- **Authors:** Hugging Face
- **Year:** 2024
- **Venue:** HF blog
- **URL:** https://huggingface.co/blog/smollm2

The successor: same sizes, better data, better numbers. The most up-to-date open-data SLM family in this size class.

### Gemma 2: Improving Open Language Models at a Practical Size
- **Authors:** Gemma Team, Google
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2408.00118

2B variant is the distillation case study: a small student trained from a much larger teacher's logits, not just from raw text.

## Extras
- [Microsoft org on Hugging Face](https://huggingface.co/microsoft)
- [HuggingFaceTB SmolLM2 collection](https://huggingface.co/HuggingFaceTB)
- [TinyLlama project on Hugging Face](https://huggingface.co/TinyLlama)
