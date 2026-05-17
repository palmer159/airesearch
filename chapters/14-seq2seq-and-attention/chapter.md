---
id: 14
title: Seq2seq and Attention
part: III. ML & AI in Chronological Order
---

<p>2014 produced two papers that, in retrospect, drew the blueprint for
every modern language model. Sutskever, Vinyals, and Le's <b><a href="https://en.wikipedia.org/wiki/Seq2seq" target="_blank" rel="noopener">seq2seq</a></b>
paper showed that an <a href="https://en.wikipedia.org/wiki/Long_short-term_memory" target="_blank" rel="noopener">LSTM</a> encoder could compress an entire input sentence
into a single vector, and a second LSTM decoder could generate the
translated output from that vector — end-to-end neural machine translation.
Bahdanau, Cho, and Bengio's <b>attention</b> paper, published almost
simultaneously, fixed the obvious bottleneck.</p>

<h4>Why a single vector wasn't enough</h4>
<p>Compressing a 30-word sentence into one fixed-size vector loses
information; long sentences degraded fast. Bahdanau et al.'s solution: at
each decoding step, let the decoder <i>look back</i> at all encoder hidden
states and form a weighted sum determined by a small alignment network.
This is attention. The alignment weights even produced interpretable
soft word-by-word translations as a free side effect.</p>

<pre>
alpha_{ij} = softmax_j( a(s_{i-1}, h_j) )
c_i        = sum_j alpha_{ij} h_j
</pre>

<h4>What this set up</h4>
<ul>
  <li><b>Encoder-decoder</b> as the default frame for any input-to-output
  sequence task: translation, summarisation, dialogue.</li>
  <li><b>Attention</b> as a content-based routing mechanism. Three years
  later the Transformer would drop the recurrence entirely and keep only
  the attention.</li>
  <li><b>Soft alignments</b> as a debugging tool — you could finally see
  what the model was looking at.</li>
</ul>

<p>If you read only one pair of papers in this chapter, read these two
together. They are the immediate prehistory of the Transformer; everything
after 2017 is a refinement of the question they asked.</p>

## Papers

### Sequence to Sequence Learning with Neural Networks
- **Authors:** Ilya Sutskever, Oriol Vinyals, Quoc Le
- **Year:** 2014
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1409.3215

The seq2seq paper. LSTM encoder + LSTM decoder. The trick of reversing the source sentence to ease optimisation is one of those small details that mattered a lot at the time.

### Neural Machine Translation by Jointly Learning to Align and Translate
- **Authors:** Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio
- **Year:** 2014
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/1409.0473

The attention paper. Read it once for the mechanism and once for the alignment visualisations — they are where the field's intuition for attention was forged.

### Effective Approaches to Attention-based Neural Machine Translation
- **Authors:** Luong, Pham, Manning
- **Year:** 2015
- **Venue:** EMNLP
- **URL:** https://arxiv.org/abs/1508.04025

Cleaner formalisation of dot-product vs. additive attention. The dot-product variant is the one that survives into the Transformer.

## Extras
- [Visualizing A Neural Machine Translation Model (Alammar)](https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/)
