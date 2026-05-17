---
id: 19
title: GPT-2 and the Decoder-only Paradigm
part: III. ML & AI in Chronological Order
---

<p>OpenAI's <b><a href="https://en.wikipedia.org/wiki/GPT-2" target="_blank" rel="noopener">GPT-2</a></b> (Radford et al., 2019) was a 1.5B-parameter
decoder-only Transformer trained to predict the next token on 40GB of web
text. The paper's title — <i>Language Models are Unsupervised Multitask
Learners</i> — captures the thesis. With enough scale and data, a single
next-token-prediction objective produces a model that can do translation,
question answering, summarisation, and arithmetic with no task-specific
training, just the right prompt.</p>

<h4>What was new in 2019</h4>
<ul>
  <li><b>Decoder-only</b>: a stack of causal-masked <a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)" target="_blank" rel="noopener">self-attention</a> layers.
  Simpler than encoder-decoder, and the same architecture handles input
  and output uniformly.</li>
  <li><b>Zero-shot task transfer</b>: format the task as a text completion,
  feed it to the model, read off the answer. No fine-tuning, no labelled
  data per task.</li>
  <li><b>Scale as a research direction</b>. The paper trained four
  models at 117M / 345M / 762M / 1.5B parameters and showed monotonic
  improvement on every metric. This was the empirical hint that became
  the <a href="https://en.wikipedia.org/wiki/Neural_scaling_law" target="_blank" rel="noopener">scaling laws</a> (chapter 20).</li>
</ul>

<h4>The release controversy</h4>
<p>OpenAI initially withheld the largest GPT-2 weights citing misuse risk
— novel for ML at the time, and a foretaste of every model-release debate
since. They published the smaller checkpoints first and the full model
nine months later.</p>

<h4>Why this is the chapter where modern LMs really start</h4>
<p><a href="https://en.wikipedia.org/wiki/BERT_(language_model)" target="_blank" rel="noopener">BERT</a> showed pretraining works. GPT-2 showed that a <i>single
generative</i> pretrained model is, in principle, a multi-task system.
Every chatbot, code assistant, and agent in the rest of the book sits on
this architectural choice. The decoder-only Transformer trained with
next-token prediction on web-scale text is now <i>the</i> default
substrate for AI.</p>

## Papers

### Language Models are Unsupervised Multitask Learners
- **Authors:** Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever
- **Year:** 2019
- **Venue:** OpenAI tech report
- **URL:** https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf

The GPT-2 paper. Read for the architecture, the scaling curves, and the zero-shot results. The release-policy section is also a good piece of AI-policy history.

### Improving Language Understanding by Generative Pre-Training (GPT-1)
- **Authors:** Radford, Narasimhan, Salimans, Sutskever
- **Year:** 2018
- **Venue:** OpenAI tech report
- **URL:** https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf

The earlier and shorter precursor. Pretrain a Transformer LM, then fine-tune. Useful to read just to see how unimpressive the result was relative to BERT a few months later — and how fast that changed.

## Extras
- [The Illustrated GPT-2 (Jay Alammar)](https://jalammar.github.io/illustrated-gpt2/)
