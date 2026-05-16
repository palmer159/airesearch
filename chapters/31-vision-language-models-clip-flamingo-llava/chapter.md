---
id: 31
title: Vision-Language Models: CLIP, Flamingo, LLaVA
part: VIII. Multimodal
---

<p>Multimodal LMs feed images (and audio, video) into a language backbone. The dominant recipe:
encode the image with a Vision Transformer (often CLIP-pretrained), project into the LM's token space,
and finetune jointly. <b>LLaVA</b> (2023) made this practical at small scale; <b>Flamingo</b> (2022)
established the gated cross-attention approach.</p>

## Papers

### Learning Transferable Visual Models From Natural Language Supervision (CLIP)
- **Authors:** Radford et al.
- **Year:** 2021
- **URL:** https://arxiv.org/abs/2103.00020

Contrastive image-text pretraining. The vision encoder of choice for VLMs.

### Flamingo: a Visual Language Model for Few-Shot Learning
- **Authors:** Alayrac et al. (DeepMind)
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2204.14198

Gated cross-attention from a frozen LM into vision features.

### Visual Instruction Tuning (LLaVA)
- **Authors:** Liu et al.
- **Year:** 2023
- **Venue:** NeurIPS Oral
- **URL:** https://arxiv.org/abs/2304.08485

Simple, reproducible projector-based VLM. The default starting point for open VLM work.

### BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and LLMs
- **Authors:** Li et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2301.12597

Q-Former bridge between frozen vision and language; influential design.

### An Image is Worth 16x16 Words (ViT)
- **Authors:** Dosovitskiy et al.
- **Year:** 2021
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2010.11929

The vision transformer. Background reading for any VLM work.
