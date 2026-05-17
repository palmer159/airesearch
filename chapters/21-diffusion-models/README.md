---
id: 21
title: Diffusion Models (DDPM)
part: III. ML & AI in Chronological Order
---

<p>Ho, Jain, and Abbeel's 2020 <b>Denoising Diffusion Probabilistic
Models</b> paper turned a 2015 thermodynamics-flavoured idea into a
practical generative model that, within two years, had taken over image
synthesis. By 2022, Stable Diffusion, DALL·E 2, and Imagen — all <a href="https://en.wikipedia.org/wiki/Diffusion_model" target="_blank" rel="noopener">diffusion</a>
models — had pushed text-to-image generation from research curiosity to
consumer product.</p>

<h4>The forward and reverse processes</h4>
<ul>
  <li><b>Forward</b>: take a real image and add Gaussian noise over T
  steps until it is pure noise. This process is fixed, not learned.</li>
  <li><b>Reverse</b>: train a neural network (a U-Net) to <i>denoise</i> —
  predict the noise that was added at each step — so that you can run
  the chain backwards from pure noise to a sample.</li>
</ul>

<pre>
forward:  x_t  = sqrt(alpha_bar_t) * x_0 + sqrt(1 - alpha_bar_t) * eps
loss:     L = || eps - eps_theta(x_t, t) ||^2
</pre>

<p>The training objective reduces to a clean MSE on predicted noise.
Stable, easy to scale, no minimax, no mode collapse — all the things
GANs were not.</p>

<h4>Why diffusion replaced GANs</h4>
<ul>
  <li><b>Stable training</b>: a denoising regression objective.</li>
  <li><b>Diverse samples</b>: GANs collapse modes; diffusion does not.</li>
  <li><b>Conditioning is easy</b>: classifier-free guidance lets you
  trade off sample quality and prompt fidelity at inference time.</li>
  <li><b>Latent diffusion</b> (Stable Diffusion, 2022) runs the diffusion
  process in a compressed VAE latent space, cutting compute by ~50× and
  enabling consumer-GPU image generation.</li>
</ul>

<p>Diffusion is also reaching into video (Sora, Veo), audio
(AudioLDM), molecular design, and robotics action policies. As an
end-of-2020s generative paradigm, it is to images and video roughly what
the Transformer is to text.</p>

## Papers

### Denoising Diffusion Probabilistic Models
- **Authors:** Jonathan Ho, Ajay Jain, Pieter Abbeel
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2006.11239

The DDPM paper. Reframes diffusion as variational denoising and gives the simple MSE training objective that everything later builds on.

### High-Resolution Image Synthesis with Latent Diffusion Models
- **Authors:** Rombach, Blattmann, Lorenz, Esser, Ommer
- **Year:** 2022
- **Venue:** CVPR
- **URL:** https://arxiv.org/abs/2112.10752

Latent diffusion / Stable Diffusion. Run the diffusion process in a compressed latent space for orders-of-magnitude speedup. The basis of most open-source image generators.

### Classifier-Free Diffusion Guidance
- **Authors:** Ho, Salimans
- **Year:** 2022
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2207.12598

The trick that lets a single conditional/unconditional model trade off fidelity and diversity at sample time. Universally used in text-to-image.

## Extras
- [What are Diffusion Models? (Lilian Weng)](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/)
