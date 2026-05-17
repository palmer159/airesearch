---
id: 25
title: Retrieval-Augmented Generation
part: III. ML & AI in Chronological Order
---

<p>Parametric memory — facts stored in the weights — is expensive to
update and easy to misremember. <b><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation" target="_blank" rel="noopener">Retrieval-augmented generation</a>
(RAG)</b>, introduced by Lewis et al. in 2020 and operationalised
everywhere by 2022, splits the system into two parts: a frozen LM that
generates fluent text and an external <i>retriever</i> that fetches
relevant documents from a knowledge corpus at query time.</p>

<h4>The architecture</h4>
<pre>
question -&gt; retriever (DPR / BM25 / dense embeddings) -&gt; top-k docs
docs + question -&gt; LM -&gt; grounded answer
</pre>

<ul>
  <li>Retriever: encode every passage in your corpus once, store in a
  vector index (FAISS, HNSW, modern vector DBs). At query time, encode
  the question and pull the nearest neighbours.</li>
  <li>Generator: a standard <a href="https://en.wikipedia.org/wiki/Seq2seq" target="_blank" rel="noopener">seq2seq</a> or decoder-only LM, conditioned on
  the question plus retrieved passages.</li>
  <li>Both can be trained jointly (Lewis 2020) or assembled from
  pretrained components without extra training (the 2023-onward norm).</li>
</ul>

<h4>Why this is the right answer to a real problem</h4>
<ul>
  <li><b>Freshness</b>: the corpus can be updated continuously without
  retraining the LM.</li>
  <li><b>Citability</b>: the system can show its sources, which matters
  for enterprise and search use cases.</li>
  <li><b>Hallucination reduction</b>: grounding the prompt in retrieved
  text shifts the conditional distribution toward facts, though it does
  not eliminate hallucination — and the retriever introduces its own
  failure mode if it returns the wrong passages.</li>
  <li><b>Scale separation</b>: a small LM with a large corpus often beats
  a large LM with no retrieval, especially on enterprise data the LM
  has never seen.</li>
</ul>

<p>RAG is now the default architecture for every document-search,
customer-support, and "chat with your docs" product. Modern improvements
focus on reranking (cross-encoder rerankers), query rewriting, multi-step
agentic retrieval, and long-context models that can hold dozens of
retrieved passages at once.</p>

## Papers

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- **Authors:** Patrick Lewis et al.
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2005.11401

The original RAG paper. Joint training of a dense retriever and a seq2seq generator on open-domain QA.

### Dense Passage Retrieval for Open-Domain Question Answering
- **Authors:** Karpukhin et al.
- **Year:** 2020
- **Venue:** EMNLP
- **URL:** https://arxiv.org/abs/2004.04906

The dense-retriever recipe most RAG systems still use: dual-encoder BERT, in-batch negatives, FAISS index.

### REALM: Retrieval-Augmented Language Model Pre-Training
- **Authors:** Guu, Lee, Tung, Pasupat, Chang
- **Year:** 2020
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/2002.08909

Earlier and more principled: bake retrieval into the pretraining objective itself, so the LM learns to use the retriever during MLM.

## Extras
- [Meta AI: Introducing RAG](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/)
