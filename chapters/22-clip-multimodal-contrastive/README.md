---
id: 22
title: CLIP and Multimodal Contrastive Learning
part: III. ML & AI in Chronological Order
---

<p>OpenAI's <b><a href="https://en.wikipedia.org/wiki/CLIP_(model)" target="_blank" rel="noopener">CLIP</a></b> (Radford et al., 2021) — Contrastive
Language-Image Pretraining — trained an image encoder and a text encoder
jointly so that matching (image, caption) pairs end up nearby in a shared
embedding space, and mismatched pairs end up far apart. The training data
was 400M image-text pairs scraped from the web. The result is a single
embedding space that spans both modalities.</p>

<h4>The contrastive objective</h4>
<pre>
sim(I, T) = (image_emb . text_emb) / (||image_emb|| ||text_emb||)

For a batch of N pairs, the loss treats it as 2N classification problems:
each image picks its caption out of N captions, each caption picks its image.
</pre>

<h4>Why this was a big deal</h4>
<ul>
  <li><b>Zero-shot image classification</b>: to classify an image, embed
  the image and embed candidate class names as text ("a photo of a
  cat"); pick the highest similarity. CLIP matched fully supervised
  <a href="https://en.wikipedia.org/wiki/Residual_neural_network" target="_blank" rel="noopener">ResNet</a>-50 on ImageNet without seeing a single ImageNet label.</li>
  <li><b>Distribution robustness</b>: CLIP's accuracy on ImageNet-Sketch,
  ImageNet-A, and ObjectNet was far higher than supervised models. The
  language signal acts as a regulariser that suppresses spurious
  visual shortcuts.</li>
  <li><b>A multimodal substrate</b>: text-conditioned <a href="https://en.wikipedia.org/wiki/Diffusion_model" target="_blank" rel="noopener">diffusion</a> (Stable
  Diffusion, DALL·E 2) uses CLIP-style text encoders to translate
  prompts into the diffusion model's conditioning signal. Vision-language
  models (LLaVA, etc.) project CLIP image features into an LLM's token
  space.</li>
</ul>

<p>Contrastive learning itself was not new — SimCLR and MoCo had pushed
self-supervised image representations the year before. CLIP's contribution
was to use <i>natural-language supervision</i> at scale and show that the
resulting embeddings were both more general and more robust than
single-modality alternatives.</p>

## Papers

### Learning Transferable Visual Models From Natural Language Supervision (CLIP)
- **Authors:** Alec Radford et al.
- **Year:** 2021
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/2103.00020

The CLIP paper. The zero-shot transfer experiments are the headline; the analysis of distribution shift is the under-appreciated section.

### A Simple Framework for Contrastive Learning of Visual Representations (SimCLR)
- **Authors:** Chen, Kornblith, Norouzi, Hinton
- **Year:** 2020
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/2002.05709

Single-modality self-supervised contrastive learning on images. Useful background for what CLIP added with the text side.

### Visual Instruction Tuning (LLaVA)
- **Authors:** Liu, Li, Wu, Lee
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2304.08485

Bolts a CLIP image encoder onto an LLM through a small projection layer and instruction-tunes the result. The simplest recipe for turning an LLM into a vision-language model.

## Extras
- [OpenAI CLIP blog post](https://openai.com/index/clip/)
