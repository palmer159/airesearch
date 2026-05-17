---
id: 15
title: Generative Adversarial Networks
part: III. ML & AI in Chronological Order
---

<p>Ian Goodfellow's 2014 <b>Generative Adversarial Network</b> changed how
the field thought about generative modelling. Instead of writing down a
likelihood and optimising it, train two networks against each other: a
<b>generator</b> that produces fake samples and a <b>discriminator</b> that
tries to tell fakes from real data. At equilibrium, the generator's
distribution matches the data distribution.</p>

<h4>The minimax game</h4>
<pre>
min_G max_D  E_{x~p_data}[log D(x)] + E_{z~p_z}[log(1 - D(G(z)))]
</pre>
<p>The discriminator's gradient tells the generator how to adjust its
samples so they look more real. There is no explicit likelihood, no
partition function, no Markov chain. The training dynamics are notoriously
unstable — and most of the next five years of <a href="https://en.wikipedia.org/wiki/Generative_adversarial_network" target="_blank" rel="noopener">GAN</a> research was spent
stabilising them (DCGAN, WGAN, spectral norm, progressive growing,
StyleGAN).</p>

<h4>Why it mattered, even though <a href="https://en.wikipedia.org/wiki/Diffusion_model" target="_blank" rel="noopener">diffusion</a> eventually won</h4>
<ul>
  <li>It made photorealistic image synthesis a real research target. Pre-2014
  generative-model samples mostly looked like blurry MNIST.</li>
  <li>It introduced <i>adversarial</i> as a fundamental training paradigm —
  later reused for representation learning, domain adaptation, robustness,
  and even <a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback" target="_blank" rel="noopener">RLHF</a> (the reward model is, loosely, a discriminator).</li>
  <li>It taught the field to be comfortable with implicit generative models
  whose density is not tractable. Diffusion (chapter 21) and
  flow-matching are the same family.</li>
</ul>

<p>By 2022, diffusion models had taken over high-end image generation and
GANs had largely been retired from frontier work. But for almost a decade
GANs were how you got a realistic image out of a neural network, and the
adversarial training idea is permanently embedded in the toolbox.</p>

## Papers

### Generative Adversarial Networks
- **Authors:** Ian Goodfellow et al.
- **Year:** 2014
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1406.2661

The original GAN paper. Short, dense, and beautifully written. Read it once for the minimax formulation and once for the proof sketch that the optimum recovers p_data.

### Unsupervised Representation Learning with Deep Convolutional GANs (DCGAN)
- **Authors:** Radford, Metz, Chintala
- **Year:** 2015
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/1511.06434

The architectural recipe (strided convolutions, batchnorm, no fully-connected layers) that made GANs trainable in practice.

### Wasserstein GAN
- **Authors:** Arjovsky, Chintala, Bottou
- **Year:** 2017
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/1701.07875

Reframed GAN training as Wasserstein distance minimisation. Removed many of the mode-collapse and gradient pathologies of vanilla GANs.

## Extras
- [NIPS 2016 Tutorial: Generative Adversarial Networks](https://arxiv.org/abs/1701.00160)
