---
id: 3
title: BERT and the Encoder Era
part: I. Foundations
---

<p><b><a href="https://en.wikipedia.org/wiki/BERT_(language_model)" target="_blank" rel="noopener">BERT</a></b> (2018) showed that a deep bidirectional <a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)" target="_blank" rel="noopener">transformer</a> pretrained with masked-LM + next-sentence-prediction
beats every supervised SOTA on 11 NLP tasks after fine-tuning. The lesson: <i>pretrain once, fine-tune everywhere</i>.</p>

<p>Successors refined the recipe — <b>RoBERTa</b> (drop NSP, train longer), <b>ALBERT</b> (parameter sharing),
<b>DeBERTa</b> (disentangled attention), <b>ELECTRA</b> (replaced-token detection, more sample-efficient).</p>

<p>Encoders remain the right tool for <b>retrieval</b>, <b>classification</b>, and <b>embeddings</b> (see Ch. 30 on <a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation" target="_blank" rel="noopener">RAG</a>).</p>

## Papers

### BERT: Pre-training of Deep Bidirectional Transformers
- **Authors:** Devlin et al.
- **Year:** 2018
- **Venue:** NAACL
- **URL:** https://arxiv.org/abs/1810.04805

Masked-LM pretraining on a deep bidirectional transformer; unified pretrain-then-finetune recipe for NLP.

### RoBERTa: A Robustly Optimized BERT
- **Authors:** Liu et al.
- **Year:** 2019
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1907.11692

BERT done right: more data, longer training, no NSP. A reminder that hyperparameters dominate architecture.

### ELECTRA: Pre-training as Discriminators
- **Authors:** Clark et al.
- **Year:** 2020
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2003.10555

Replaced-token detection — every token contributes a training signal, so it's far more sample-efficient than MLM.

### DeBERTa: Decoding-enhanced BERT with Disentangled Attention
- **Authors:** He et al.
- **Year:** 2020
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2006.03654

Separates content from position attention; current SOTA among encoder-only models on GLUE/SuperGLUE.

### Sentence-BERT
- **Authors:** Reimers, Gurevych
- **Year:** 2019
- **Venue:** EMNLP
- **URL:** https://arxiv.org/abs/1908.10084

Siamese BERT for sentence embeddings — the foundation of modern retrieval/RAG embedding models.
