---
id: 4
title: GPT-1/2/3 and the Decoder-Only Paradigm
part: I. Foundations
---

<p>OpenAI's GPT line bet on <b>decoder-only <a href="https://en.wikipedia.org/wiki/Autoregressive_model" target="_blank" rel="noopener">autoregressive</a></b> models and on <b>scale</b>. <a href="https://en.wikipedia.org/wiki/GPT-3" target="_blank" rel="noopener">GPT-3</a> (2020) was the
inflection point: at 175B parameters, <a href="https://en.wikipedia.org/wiki/In-context_learning" target="_blank" rel="noopener">in-context learning</a> emerged — you could prompt the model with examples and
get a usable downstream learner without any gradient updates.</p>

<h4>Why decoder-only won</h4>
<ul>
  <li>Single objective (next-token prediction) — no pretrain/finetune mismatch.</li>
  <li>Generation and classification fold into one interface (just generate the answer).</li>
  <li>Scales gracefully; tooling (sampling, beam, KV cache) is well-understood.</li>
</ul>

## Papers

### Improving Language Understanding by Generative Pre-Training (GPT-1)
- **Authors:** Radford, Narasimhan, Salimans, Sutskever
- **Year:** 2018
- **Venue:** OpenAI
- **URL:** https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

Generative pretraining + discriminative fine-tuning. Sets the decoder-only template.

### Language Models are Unsupervised Multitask Learners (GPT-2)
- **Authors:** Radford et al.
- **Year:** 2019
- **Venue:** OpenAI
- **URL:** https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

Zero-shot multitask via prompting. First widely-discussed dual-use safety release.

### Language Models are Few-Shot Learners (GPT-3)
- **Authors:** Brown et al.
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2005.14165

175B parameters; few-shot in-context learning emerges. The paper that changed everything.

### GPT-4 Technical Report
- **Authors:** OpenAI
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2303.08774

Multimodal, professional-test performance, RLHF + heavy red-teaming. Light on architecture, heavy on capabilities/safety.
