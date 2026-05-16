---
id: 7
title: Pretraining Data: C4, The Pile, RedPajama, Dolma, FineWeb
part: II. Training & Data
---

<p>Data is the dominant lever in pretraining. Public corpora have evolved from <b>C4</b> (T5, 2020) to
ever-larger, better-filtered web datasets — <b>The Pile</b>, <b>RedPajama</b>, <b>RefinedWeb</b>, <b>Dolma</b>,
and currently <b>FineWeb</b> / <b>FineWeb-Edu</b> (15T tokens).</p>

<h4>What "good data" looks like in 2026</h4>
<ul>
  <li>Aggressive deduplication (exact + near-duplicate via MinHash/LSH).</li>
  <li>Quality classifiers — model-based filtering for "educational content" beats heuristics.</li>
  <li>Domain mix tuned per stage (e.g., more math/code at the end of pretraining annealing).</li>
  <li>Decontamination from eval benchmarks (often missed; inflates reported scores).</li>
</ul>

## Papers

### The Pile: An 800GB Dataset of Diverse Text
- **Authors:** Gao et al.
- **Year:** 2020
- **URL:** https://arxiv.org/abs/2101.00027

The first widely-used open pretraining corpus combining 22 sources; reusable methodology.

### Deduplicating Training Data Makes Language Models Better
- **Authors:** Lee et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2107.06499

Dedup → less memorization, better perplexity, faster training. A free win.

### The RefinedWeb Dataset for Falcon LLM
- **Authors:** Penedo et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2306.01116

Shows web-only, well-filtered data can match curated mixes. Influenced FineWeb.

### Dolma: an Open Corpus of Three Trillion Tokens
- **Authors:** Soldaini et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.00159

AI2's open recipe — releases the data, the toolkit, and the design rationale.

### FineWeb / FineWeb-Edu
- **Authors:** Penedo et al.
- **Year:** 2024
- **Venue:** Hugging Face
- **URL:** https://huggingface.co/datasets/HuggingFaceFW/fineweb

15T-token open web corpus; FineWeb-Edu uses an educational-quality classifier and improves benchmark scores significantly.
