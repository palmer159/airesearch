---
id: 13
title: Word Embeddings: word2vec and GloVe
part: III. ML & AI in Chronological Order
---

<p>Bengio's NPLM gave us the idea of <a href="https://en.wikipedia.org/wiki/Word_embedding" target="_blank" rel="noopener">word embeddings</a>. The 2013-14 trio of
<b><a href="https://en.wikipedia.org/wiki/Word2vec" target="_blank" rel="noopener">word2vec</a></b>, <b>GloVe</b>, and the surrounding tooling made embeddings
fast, scalable, and shockingly useful. For about three years, downloading
pretrained word vectors was the entire "transfer learning" story in NLP.</p>

<h4>word2vec — Mikolov et al., 2013</h4>
<ul>
  <li><b>Skip-gram</b>: given a centre word, predict its neighbours.</li>
  <li><b>CBOW</b>: given the neighbours, predict the centre word.</li>
  <li><b>Negative sampling</b>: replace the full <a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank" rel="noopener">softmax</a> with a binary
  classifier that distinguishes real (word, context) pairs from random
  noise. This is the trick that made training 100B-token corpora
  feasible on a single machine.</li>
</ul>

<h4>GloVe — Pennington, Socher, Manning, 2014</h4>
<p>GloVe instead factorises the global word-word co-occurrence matrix
directly, with a weighted least-squares objective. It often produced
slightly better vectors than word2vec on analogy tasks and made the
mathematical link to classical distributional semantics explicit.</p>

<h4>Why it caught fire</h4>
<p>The embeddings turned out to encode startling amounts of structure:
<code>king - man + woman ≈ queen</code> became the canonical demo. More
practically, every NLP system that previously used one-hot word features
could now be initialised with 300-dim vectors trained on Wikipedia or
Common Crawl and immediately do better. This was the first taste of
"pretrain on a generic corpus, fine-tune on your task" — the playbook that
<a href="https://en.wikipedia.org/wiki/BERT_(language_model)" target="_blank" rel="noopener">BERT</a> and GPT would later industrialise.</p>

<p>Limitations were obvious: a single vector per word cannot disambiguate
"bank" the financial institution from "bank" the river edge. ELMo (2018)
fixed that with contextual embeddings, and BERT (2018) fixed it harder. But
word2vec is still the cleanest pedagogical entry point to representation
learning in NLP.</p>

## Papers

### Efficient Estimation of Word Representations in Vector Space
- **Authors:** Mikolov, Chen, Corrado, Dean
- **Year:** 2013
- **Venue:** ICLR Workshop
- **URL:** https://arxiv.org/abs/1301.3781

The word2vec paper. CBOW and skip-gram architectures, plus the analogy-task evaluation that made the work famous.

### Distributed Representations of Words and Phrases and their Compositionality
- **Authors:** Mikolov, Sutskever, Chen, Corrado, Dean
- **Year:** 2013
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1310.4546

The follow-up that introduces negative sampling and subsampling of frequent words. This is the version most implementations actually use.

### GloVe: Global Vectors for Word Representation
- **Authors:** Pennington, Socher, Manning
- **Year:** 2014
- **Venue:** EMNLP
- **URL:** https://nlp.stanford.edu/pubs/glove.pdf

Matrix-factorisation alternative. The introduction is one of the clearest explanations in NLP of what an embedding is and what it should encode.

## Extras
- [The amazing power of word vectors (Adrian Colyer)](https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/)
