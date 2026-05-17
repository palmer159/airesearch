---
id: 17
title: The Transformer
part: III. ML & AI in Chronological Order
---

<p>"Attention Is All You Need" (Vaswani et al., 2017) is the architectural
hinge of this entire book. It removes recurrence and convolution from
sequence modelling and keeps only attention, normalised, residualised, and
stacked.</p>

<h4>The three ingredients</h4>
<ul>
  <li><b>Scaled dot-product attention</b> — the core mechanism, with the
  <code>1/sqrt(d_k)</code> scale that keeps <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank" rel="noopener">softmax</a> gradients well-behaved.</li>
  <li><b>Multi-head attention</b> — run several attention layers in parallel
  with different learned projections, then concatenate. Different heads end
  up specialising on different relations.</li>
  <li><b>Positional encodings</b> — sinusoidal or learned, because pure
  attention is permutation-invariant and language is not.</li>
</ul>

<pre>
Attention(Q, K, V) = softmax( Q K^T / sqrt(d_k) ) V
</pre>

<h4>Why it took over</h4>
<p>Compared to <a href="https://en.wikipedia.org/wiki/Long_short-term_memory" target="_blank" rel="noopener">LSTM</a>:</p>
<ul>
  <li><b>Constant path length</b> between any two tokens. RNNs need O(n)
  steps for information to flow; attention needs one.</li>
  <li><b>Parallel training</b>. Every position can be computed
  simultaneously on a GPU. This unlocked training at scales LSTMs simply
  could not reach.</li>
  <li><b>Mild inductive bias</b>. Less wired-in structure means the model
  improves smoothly as you scale data and parameters — exactly the
  property <a href="https://en.wikipedia.org/wiki/Neural_scaling_law" target="_blank" rel="noopener">scaling laws</a> (chapter 20) would later quantify.</li>
</ul>

<p>The original Transformer was an encoder-decoder for translation. The
field quickly forked into encoder-only (<a href="https://en.wikipedia.org/wiki/BERT_(language_model)" target="_blank" rel="noopener">BERT</a>, chapter 18), decoder-only
(GPT, chapter 19), and the original encoder-decoder (T5, BART). All
modern frontier LMs are decoder-only Transformers; almost every modern
embedding model is an encoder-only one. The architecture has been refined
heavily — RoPE, FlashAttention, grouped-query attention, <a href="https://en.wikipedia.org/wiki/Mixture_of_experts" target="_blank" rel="noopener">MoE</a> — but the
2017 skeleton is still recognisable.</p>

## Papers

### Attention Is All You Need
- **Authors:** Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin
- **Year:** 2017
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1706.03762

The Transformer paper. Self-attention, multi-head attention, sinusoidal positional encodings. The most-cited ML paper of the late 2010s.

### Layer Normalization
- **Authors:** Ba, Kiros, Hinton
- **Year:** 2016
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1607.06450

LayerNorm — the normalization that made deep transformers trainable in the first place.

## Extras
- [The Illustrated Transformer (Jay Alammar)](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer (Harvard NLP)](http://nlp.seas.harvard.edu/annotated-transformer/)
