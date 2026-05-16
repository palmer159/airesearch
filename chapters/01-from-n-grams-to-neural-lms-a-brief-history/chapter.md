---
id: 1
title: From n-grams to Neural LMs: A Brief History
part: I. Foundations
---

<p>Before transformers there were <b>n-gram</b> models (Shannon, 1948), <b>feed-forward neural language models</b>
(Bengio et al., 2003), and <b>recurrent</b> language models (Mikolov, 2010). The leap was learning <i>distributed
representations</i> instead of memorizing surface forms. Read this chapter as motivation: the modern stack inherits
the same objective — predict the next token — but at radically larger scale and with far better architectures.</p>

<h4>Illustrative example</h4>
<pre>
n-gram (trigram):  P(w_t | w_{t-2}, w_{t-1})       # sparse counts, no generalization
Neural LM:         P(w_t | h_t),  h_t = f(embedding(context))   # dense, generalizes
</pre>
<p>The neural LM's embeddings make "king - man + woman ≈ queen" possible. That single observation foreshadows
why scale-up of neural LMs eventually subsumed all of NLP.</p>

## Papers

### A Mathematical Theory of Communication
- **Authors:** Shannon
- **Year:** 1948
- **Venue:** Bell System Tech. Journal
- **URL:** https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf

Defines entropy and the predict-the-next-symbol formalism that underlies all modern LMs.

### A Neural Probabilistic Language Model
- **Authors:** Bengio, Ducharme, Vincent, Jauvin
- **Year:** 2003
- **Venue:** JMLR
- **URL:** https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf

First widely cited neural LM with learned word embeddings; defeats n-grams via distributed representations.

### Recurrent neural network based language model
- **Authors:** Mikolov et al.
- **Year:** 2010
- **Venue:** Interspeech
- **URL:** https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.pdf

RNN-LM beats n-grams on perplexity and ASR; the first crack in the n-gram dam.

### Distributed Representations of Words and Phrases (word2vec)
- **Authors:** Mikolov et al.
- **Year:** 2013
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1310.4546

Skip-gram + negative sampling. Made dense word vectors the default input to NLP.

### GloVe: Global Vectors for Word Representation
- **Authors:** Pennington, Socher, Manning
- **Year:** 2014
- **Venue:** EMNLP
- **URL:** https://nlp.stanford.edu/pubs/glove.pdf

Matrix-factorization view of word embeddings; complement to word2vec.
