---
id: 5
title: T5, BART, and the Text-to-Text Frame
part: I. Foundations
---

<p>Google's <b>T5</b> reframed every NLP task — translation, classification, QA, summarization — as
<i>text in, text out</i>. The C4 corpus, span corruption objective, and unified prefix-task tokens became
standard machinery in subsequent systems.</p>
<p><b>BART</b> (Facebook) used a denoising autoencoder over arbitrary corruptions; an excellent encoder-decoder
for summarization. <b>FLAN-T5</b> (Ch. 12) showed that instruction-tuning T5 makes it competitive with much larger
decoder-only models — an early hint that data quality > raw scale.</p>

## Papers

### Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)
- **Authors:** Raffel et al.
- **Year:** 2020
- **Venue:** JMLR
- **URL:** https://arxiv.org/abs/1910.10683

Unified text-to-text transformer; introduces C4. The most thorough ablation study in pretraining literature.

### BART: Denoising Sequence-to-Sequence Pre-training
- **Authors:** Lewis et al.
- **Year:** 2019
- **Venue:** ACL
- **URL:** https://arxiv.org/abs/1910.13461

Encoder-decoder pretrained on noisy-input → clean-output. Strong on summarization and dialogue.

### Scaling Instruction-Finetuned Language Models (FLAN-T5)
- **Authors:** Chung et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2210.11416

Instruction-tunes T5 on 1,800+ tasks. Demonstrates instruction-tuning as a generic capability multiplier.
