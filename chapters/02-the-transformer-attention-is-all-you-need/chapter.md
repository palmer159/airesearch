---
id: 2
title: The Transformer: Attention Is All You Need
part: I. Foundations
---

<p>The 2017 transformer replaces recurrence with <b>self-attention</b>: each token attends to every other token in
parallel. Three ingredients matter: scaled dot-product attention, multi-head attention, and positional encodings.</p>

<h4>Self-attention in one equation</h4>
<pre>
Attention(Q, K, V) = softmax( Q K^T / sqrt(d_k) ) V
</pre>
<p>Why this matters: O(1) path length between any two tokens (vs O(n) for RNNs), trivially parallelizable on GPUs,
and the inductive bias is mild enough that scaling up just keeps working.</p>

<h4>Encoder vs decoder vs encoder-decoder</h4>
<ul>
  <li><b>Encoder-only</b> (BERT family) — bidirectional, good for classification/retrieval.</li>
  <li><b>Decoder-only</b> (GPT family) — causal, good for generation. The dominant modern form.</li>
  <li><b>Encoder-decoder</b> (T5, original Transformer) — good for seq2seq translation/summarization.</li>
</ul>

## Papers

### Attention Is All You Need
- **Authors:** Vaswani et al.
- **Year:** 2017
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1706.03762

The Transformer. Self-attention, multi-head, positional encoding. Foundation of every modern LM.

### The Illustrated Transformer
- **Authors:** Jay Alammar
- **Year:** 2018
- **Venue:** blog
- **URL:** https://jalammar.github.io/illustrated-transformer/

Best beginner-friendly visual explanation of attention; pair it with the original paper.

### The Annotated Transformer
- **Authors:** Sasha Rush et al.
- **Year:** 2018
- **Venue:** Harvard NLP
- **URL:** http://nlp.seas.harvard.edu/annotated-transformer/

Line-by-line PyTorch implementation interleaved with the paper. The canonical pedagogical resource.

### Layer Normalization
- **Authors:** Ba, Kiros, Hinton
- **Year:** 2016
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1607.06450

LayerNorm — the normalization that made deep transformers trainable.
