---
id: 24
title: Embeddings, Vector DBs, Rerankers
part: VI. Retrieval & Grounding
---

<p>Embedding models project text into a fixed-dimensional vector space where cosine similarity ≈ semantic similarity.
The <b>MTEB</b> leaderboard tracks the state of the art (BGE, E5, GTE, NV-Embed, then Cohere/OpenAI/Voyage).</p>
<p>Practical stack:</p>
<ul>
  <li>Embedder (BGE/E5/Voyage) → ANN index (FAISS, ScaNN, HNSW in Qdrant/Milvus/Weaviate/pgvector).</li>
  <li>Cross-encoder reranker (BGE-reranker, Cohere Rerank) on top-k candidates.</li>
  <li>For long docs: <b>ColBERT</b>-style late interaction beats single-vector when latency permits.</li>
</ul>

## Papers

### Dense Passage Retrieval (DPR)
- **Authors:** Karpukhin et al.
- **Year:** 2020
- **Venue:** EMNLP
- **URL:** https://arxiv.org/abs/2004.04906

The dual-encoder retrieval baseline that everything else iterates on.

### ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction
- **Authors:** Khattab, Zaharia
- **Year:** 2020
- **Venue:** SIGIR
- **URL:** https://arxiv.org/abs/2004.12832

Late-interaction retrieval; recall of cross-encoders at near-bi-encoder cost.

### MTEB: Massive Text Embedding Benchmark
- **Authors:** Muennighoff et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2210.07316

The standard benchmark suite. Always check MTEB before adopting an embedding model.

### Matryoshka Representation Learning
- **Authors:** Kusupati et al.
- **Year:** 2022
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2205.13147

Train embeddings so that prefixes are themselves valid embeddings → nested compression for serving.
