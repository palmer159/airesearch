---
id: 29
title: Knowledge Distillation and Model Compression
part: VII. Small Language Models
---

<p><a href="https://en.wikipedia.org/wiki/Knowledge_distillation" target="_blank" rel="noopener">Distillation</a> trains a small student to imitate a large teacher's distributions, hidden states, or behavior.
Combined with quantization and pruning, it's the backbone of every successful SLM family.</p>
<h4>Modes</h4>
<ul>
  <li><b>Soft-label KL distillation</b> (Hinton 2015) — match the teacher's logits.</li>
  <li><b>Hidden-state matching</b> (DistilBERT, MiniLM).</li>
  <li><b>Synthetic-data SFT</b> — let the teacher write the training set (Alpaca, Phi, Gemma 2).</li>
  <li><b>Reasoning distillation</b> — distill long-CoT traces from o1/R1-style teachers into compact students.</li>
</ul>

## Papers

### Distilling the Knowledge in a Neural Network
- **Authors:** Hinton, Vinyals, Dean
- **Year:** 2015
- **URL:** https://arxiv.org/abs/1503.02531

Soft-label distillation. Origin story of modern compression.

### DistilBERT
- **Authors:** Sanh et al.
- **Year:** 2019
- **URL:** https://arxiv.org/abs/1910.01108

60% smaller, 60% faster, 97% of BERT performance via triple-loss distillation.

### Alpaca: An Instruction-following LLaMA Model
- **Authors:** Taori et al.
- **Year:** 2023
- **Venue:** Stanford CRFM
- **URL:** https://crfm.stanford.edu/2023/03/13/alpaca.html

Distill GPT-3.5 instruction-following into 7B Llama with 52K examples and ~$600. Sparked the open chatbot wave.

### MINILLM: Knowledge Distillation of Large Language Models
- **Authors:** Gu et al.
- **Year:** 2024
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2306.08543

Reverse KL distillation; principled handling of mode-seeking vs mode-covering for generative students.
