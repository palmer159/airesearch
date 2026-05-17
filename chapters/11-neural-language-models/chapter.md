---
id: 11
title: Neural Language Models (Bengio NPLM)
part: III. ML & AI in Chronological Order
---

<p>Up to 2003, language modelling was n-grams: count sequences, smooth, hope
the test set looks like the training set. Bengio, Ducharme, Vincent, and
Janvin proposed a different idea: <b>learn a continuous vector for every
word, and let a neural network predict the next word from the vectors of the
previous few</b>. This is the <i>neural probabilistic language model</i> —
NPLM — and it is the first chapter where the word "embedding" means what we
mean by it today.</p>

<h4>Architecture in one breath</h4>
<pre>
context: w_{t-n+1}, ..., w_{t-1}
e_i = C[w_i]                  # embedding lookup, shared across positions
h   = tanh(W [e_1; ...; e_{n-1}] + b)
p(w_t | context) = softmax(U h + d)
</pre>

<p>Two things happen during training. First, the network learns to predict
the next word — that is the loss. Second, and more importantly,
<i>similar words end up with similar vectors</i>, because the network has no
way to use a word other than through its embedding. Words that play similar
roles in similar contexts must therefore be encoded similarly. This is the
distributional hypothesis made concrete and learnable.</p>

<h4>Why it matters</h4>
<ul>
  <li>It killed the curse of dimensionality for n-grams: instead of needing
  to see every <a href="https://en.wikipedia.org/wiki/N-gram" target="_blank" rel="noopener">n-gram</a>, the model generalises through embeddings.</li>
  <li>It introduced the input layer that every later language model still
  uses: an embedding matrix of shape (vocab, d_model).</li>
  <li>It connected language modelling to representation learning. Word2vec,
  GloVe, ELMo, and <a href="https://en.wikipedia.org/wiki/BERT_(language_model)" target="_blank" rel="noopener">BERT</a> are all in the same family tree.</li>
</ul>

<p>Read this paper before <a href="https://en.wikipedia.org/wiki/Word2vec" target="_blank" rel="noopener">word2vec</a> — it is older, denser, and the better
education.</p>

## Papers

### A Neural Probabilistic Language Model
- **Authors:** Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Janvin
- **Year:** 2003
- **Venue:** JMLR
- **URL:** https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf

The original NPLM paper. The maths is elementary; the conceptual move from discrete counts to learned vectors is the whole point.

### A Scalable Hierarchical Distributed Language Model
- **Authors:** Mnih, Hinton
- **Year:** 2008
- **Venue:** NeurIPS
- **URL:** https://www.cs.toronto.edu/~amnih/papers/hlbl_final.pdf

Hierarchical softmax — a key trick for making NPLMs trainable at vocabularies above ~10k words. Sets up word2vec's later optimisations.

## Extras
- [Wikipedia: Language model](https://en.wikipedia.org/wiki/Language_model)
