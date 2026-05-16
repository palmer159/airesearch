---
id: 32
title: Image / Video / Audio Generation: Diffusion in the LM Era
part: VIII. Multimodal
---

<p>Generation in the modern stack is dominated by <b><a href="https://en.wikipedia.org/wiki/Diffusion_model" target="_blank" rel="noopener">diffusion</a></b> (Ho et al., 2020) and increasingly
<b>flow matching</b> (Lipman et al., 2023). DALL·E 2/3, Stable Diffusion, Imagen, Sora, Veo — all use a
text encoder (often a frozen LM) to condition a denoising diffusion / latent diffusion model.</p>
<p>For audio: <b>AudioLM</b>, <b>MusicLM</b>, and OpenAI's <a href="https://en.wikipedia.org/wiki/Whisper_(speech_recognition_system)" target="_blank" rel="noopener">Whisper</a> / Voice all show that the same
"discrete-tokens-on-a-<a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)" target="_blank" rel="noopener">transformer</a>" recipe transfers to speech and music.</p>

## Papers

### Denoising Diffusion Probabilistic Models
- **Authors:** Ho, Jain, Abbeel
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2006.11239

Modern formulation of diffusion. Foundation of contemporary generative models.

### High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)
- **Authors:** Rombach et al.
- **Year:** 2022
- **Venue:** CVPR
- **URL:** https://arxiv.org/abs/2112.10752

Diffusion in latent space; made open-weights image generation practical.

### Scalable Diffusion Models with Transformers (DiT)
- **Authors:** Peebles, Xie
- **Year:** 2023
- **Venue:** ICCV
- **URL:** https://arxiv.org/abs/2212.09748

Replaces UNet with a transformer; underpins Sora and Stable Diffusion 3.

### Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)
- **Authors:** Radford et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2212.04356

Open multilingual ASR. The de-facto baseline for speech-to-text.

### Flow Matching for Generative Modeling
- **Authors:** Lipman et al.
- **Year:** 2023
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2210.02747

Continuous-time generative training; cleaner alternative to diffusion. Powers Stable Diffusion 3 and beyond.
