---
id: 26
title: LLaMA and the Open-Weight Era
part: III. ML & AI in Chronological Order
---

<p>Until February 2023, the strongest LLMs were proprietary. Meta's
<b>LLaMA</b> release — and especially the leak of its weights two weeks
later — broke that. Within months, an entire open-source ecosystem of
fine-tunes, quantisations, and inference engines had grown up around
LLaMA, and the centre of gravity for academic and indie LLM work
permanently shifted toward open weights.</p>

<h4>What LLaMA 1 actually was</h4>
<ul>
  <li>A standard decoder-only Transformer at 7B / 13B / 33B / 65B
  parameters.</li>
  <li>Trained on ~1.4T tokens of public web data (Common Crawl, Wikipedia,
  GitHub, ArXiv, Books, StackExchange).</li>
  <li>Architectural details that became defaults: <b>RoPE</b> positional
  encodings, <b>SwiGLU</b> activations, <b>RMSNorm</b>, no biases.</li>
  <li>Trained well past the Kaplan-optimal point — closer to Chinchilla —
  which is why a 13B model could approach <a href="https://en.wikipedia.org/wiki/GPT-3" target="_blank" rel="noopener">GPT-3</a> 175B's quality.</li>
</ul>

<h4>The follow-ups that mattered</h4>
<ul>
  <li><b><a href="https://en.wikipedia.org/wiki/Llama_(language_model)" target="_blank" rel="noopener">Llama</a> 2</b> (2023): commercially licensed, paired-up SFT + <a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback" target="_blank" rel="noopener">RLHF</a>
  recipe, chat variants. Made open-weight assistants legitimate for
  enterprise use.</li>
  <li><b>Llama 3</b> (2024): up to 405B parameters, ~15T training tokens,
  GQA, careful data curation. Broadly competitive with frontier
  closed models on standard benchmarks.</li>
</ul>

<h4>Why this changed the field</h4>
<p>Open weights mean reproducibility, mechanistic interpretability work
on real frontier-class models, and a Cambrian explosion of fine-tunes
(Alpaca, Vicuna, WizardLM, OpenChat, ...). They also gave the SLM
movement (chapter 29) a credible foundation: nearly every open small
model after 2023 starts from a Llama, Mistral, or Qwen base. The
"closed labs vs. open ecosystem" dynamic that defines AI in 2026 starts
here.</p>

## Papers

### LLaMA: Open and Efficient Foundation Language Models
- **Authors:** Hugo Touvron et al.
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2302.13971

The LLaMA 1 paper. The architecture decisions and the data mix are still the template every later open model follows.

### Llama 2: Open Foundation and Fine-Tuned Chat Models
- **Authors:** Hugo Touvron et al.
- **Year:** 2023
- **Venue:** Meta tech report
- **URL:** https://arxiv.org/abs/2307.09288

Commercial license, paired SFT + RLHF, chat variants, ghost-attention. The model that legitimised open-weight assistants.

### The Llama 3 Herd of Models
- **Authors:** Meta Llama team
- **Year:** 2024
- **Venue:** Meta tech report
- **URL:** https://arxiv.org/abs/2407.21783

The 90-page paper detailing Llama 3 / 3.1 — data pipelines, training infrastructure, multimodal extensions. The most thorough description of a frontier-scale training run available in the open literature.

## Extras
- [Meta Llama official site](https://www.llama.com/)
