---
id: 27
title: LoRA, QLoRA, and Parameter-Efficient Fine-Tuning
part: III. ML & AI in Chronological Order
---

<p>Full fine-tuning of a 70B-parameter model needs hundreds of GB of GPU
memory. <b>Parameter-efficient fine-tuning (PEFT)</b> methods change that
by training only a tiny fraction of the weights — and yet matching or
nearly matching full-fine-tune quality on most downstream tasks.
<b><a href="https://en.wikipedia.org/wiki/Low-rank_adaptation" target="_blank" rel="noopener">LoRA</a></b> (2021) is the dominant method; <b>QLoRA</b> (2023) made it
practical on a single consumer GPU.</p>

<h4>LoRA in one equation</h4>
<pre>
Original:    y = W x
With LoRA:   y = W x + (B A) x         # A is r-by-d, B is d-by-r, rank r &lt;&lt; d
</pre>
<p>Freeze the original weights W; train only the low-rank update B·A.
Typical r is 8 or 16. For a 7B model, that means training ~10M
parameters instead of 7B, and the LoRA adapters can be swapped in and
out at inference time per task.</p>

<h4>QLoRA</h4>
<ul>
  <li>Quantise the frozen base model to <b>4-bit NF4</b> (Normal Float 4,
  designed for the actual distribution of LLM weights).</li>
  <li>Keep LoRA adapters in fp16 / bf16.</li>
  <li>Use <b>paged optimisers</b> to spill optimiser state to CPU RAM
  during memory spikes.</li>
  <li>Result: fine-tune a 65B model on a single 48GB GPU, with no quality
  loss vs full-precision LoRA on the Guanaco benchmarks.</li>
</ul>

<h4>Why this is its own chapter</h4>
<p>PEFT democratised fine-tuning. Before LoRA, customising an LLM for
your domain required either a research lab's GPU cluster or paying for
a closed-source provider's fine-tune endpoint. After QLoRA, an engineer
with a single A100 or even a 24GB consumer card can fine-tune a 13B-70B
open-weight model on a few thousand examples overnight. Modern adapter
hubs (Hugging Face PEFT, Together, Predibase) all assume this workflow.
The cost of customising open-weight LLMs collapsed by two orders of
magnitude in 18 months.</p>

## Papers

### LoRA: Low-Rank Adaptation of Large Language Models
- **Authors:** Edward Hu et al.
- **Year:** 2021
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2106.09685

The original LoRA paper. Read for the rank-deficiency hypothesis and the empirical sweep across GPT-2, GPT-3, and RoBERTa.

### QLoRA: Efficient Finetuning of Quantized LLMs
- **Authors:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2305.14314

NF4, double quantisation, paged optimisers. The paper that put 65B fine-tuning on a single GPU.

### Parameter-Efficient Transfer Learning for NLP (Adapters)
- **Authors:** Houlsby et al.
- **Year:** 2019
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/1902.00751

The earlier, broader idea: insert small bottleneck layers into a frozen Transformer and only train those. Useful prehistory for LoRA.

## Extras
- [Hugging Face PEFT library](https://huggingface.co/docs/peft/index)
