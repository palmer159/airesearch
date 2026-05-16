---
id: 23
title: Retrieval-Augmented Generation (RAG)
part: VI. Retrieval & Grounding
---

<p><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation" target="_blank" rel="noopener">RAG</a> = retrieve relevant documents → put them in the prompt → generate. Unfashionable in 2024 hype-cycles but
indispensable in production: it grounds answers, scopes data freshness, and keeps proprietary content out of weights.</p>
<h4>Production RAG checklist</h4>
<ol>
  <li>Chunk smartly (hierarchical, semantic — not arbitrary 512-token slices).</li>
  <li>Hybrid retrieval — dense (BM25) + sparse + reranker.</li>
  <li>Decontaminate, deduplicate, attribute.</li>
  <li>Evaluate with RAG-aware metrics (faithfulness, context relevance), not just answer accuracy.</li>
  <li>Add a "did the retrieval find the right thing?" guard before "did the model answer correctly?"</li>
</ol>

## Papers

### Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks
- **Authors:** Lewis et al.
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2005.11401

The original RAG paper. Still worth re-reading.

### REALM: Retrieval-Augmented Language Model Pre-Training
- **Authors:** Guu et al.
- **Year:** 2020
- **URL:** https://arxiv.org/abs/2002.08909

Pre-RAG retrieval-pretraining; conceptually formative.

### Atlas: Few-shot Learning with Retrieval Augmented LMs
- **Authors:** Izacard et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2208.03299

Strong few-shot learner via retrieval; the recipe many production RAG systems imitate.

### Self-RAG: Self-Reflective Retrieval
- **Authors:** Asai et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.11511

Model decides when/what to retrieve and critiques its own outputs; strong on long-form QA.

### Lost in the Middle (revisit)
- **Authors:** Liu et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.03172

Bookend retrieved passages with the most important ones — empirically robust.
