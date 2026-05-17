---
id: 10
title: LSTM: Recurrent Networks That Worked
part: III. ML & AI in Chronological Order
---

<p>Naive <a href="https://en.wikipedia.org/wiki/Recurrent_neural_network" target="_blank" rel="noopener">recurrent</a> neural networks were known to be expressive but
untrainable on long sequences: gradients either vanished to zero or exploded.
Hochreiter and Schmidhuber's 1997 <b>Long Short-Term Memory</b> network
solved the vanishing-gradient problem with a clever architectural trick — a
linear cell state guarded by multiplicative <i>gates</i>.</p>

<h4>The gates</h4>
<ul>
  <li><b>Forget gate</b> — what to drop from the cell state.</li>
  <li><b>Input gate</b> — what new information to write.</li>
  <li><b>Output gate</b> — what part of the cell state to expose as the
  hidden state.</li>
</ul>

<pre>
c_t = f_t * c_{t-1} + i_t * tanh(W x_t + U h_{t-1})
h_t = o_t * tanh(c_t)
</pre>

<p>Because the cell-state update is additive (modulated by a sigmoid gate
near 1), the gradient can flow back through hundreds of timesteps without
collapsing. That single design choice made it possible to train RNNs on
real-world speech, handwriting, and language data.</p>

<h4>Why it matters historically</h4>
<p>From 1997 through about 2017, <a href="https://en.wikipedia.org/wiki/Long_short-term_memory" target="_blank" rel="noopener">LSTM</a> (and its cousin GRU) was the default
sequence model for everything that mattered in language: speech recognition,
machine translation, language modelling, handwriting generation, even early
captioning systems. Google Translate ran on stacked LSTMs in 2016. The
<a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)" target="_blank" rel="noopener">transformer</a> eventually replaced it for high-end tasks because attention
parallelises across the sequence while LSTM is inherently serial — but the
intuitions about gating, residual paths, and additive updates carried over.
Modern state-space models (Mamba) are arguably an attempt to recover LSTM's
linear-time inference while keeping transformer-grade quality.</p>

## Papers

### Long Short-Term Memory
- **Authors:** Sepp Hochreiter, Jürgen Schmidhuber
- **Year:** 1997
- **Venue:** Neural Computation
- **URL:** https://www.bioinf.jku.at/publications/older/2604.pdf

The original LSTM paper. Dense but worth working through — the analysis of constant error carousels is the core of why the architecture works.

### Sequence to Sequence Learning with Neural Networks
- **Authors:** Sutskever, Vinyals, Le
- **Year:** 2014
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1409.3215

LSTM-based encoder-decoder for machine translation. The first credible neural alternative to phrase-based statistical MT.

### Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling
- **Authors:** Chung, Gulcehre, Cho, Bengio
- **Year:** 2014
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1412.3555

Compares LSTM against the simpler GRU. Useful for understanding which gates are doing real work.

## Extras
- [Understanding LSTM Networks (colah's blog)](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
