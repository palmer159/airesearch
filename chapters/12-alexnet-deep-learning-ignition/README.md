---
id: 12
title: AlexNet and the Deep Learning Ignition
part: III. ML & AI in Chronological Order
---

<p>The 2012 ImageNet result is the moment deep learning stopped being a
niche academic interest and became the dominant paradigm in AI. Krizhevsky,
Sutskever, and Hinton's <b><a href="https://en.wikipedia.org/wiki/AlexNet" target="_blank" rel="noopener">AlexNet</a></b> halved the previous best error rate
on a 1000-class image-classification task. The community's reaction was
swift and total — within two years almost every vision lab had switched to
deep CNNs.</p>

<h4>What was actually new</h4>
<ul>
  <li><b>Scale</b>: an 8-layer CNN with 60M parameters, trained on 1.2M
  labelled images.</li>
  <li><b>Hardware</b>: two consumer NVIDIA GTX 580 GPUs, hand-split across
  the network. The CUDA convolution kernel was the unsung hero.</li>
  <li><b>ReLU activations</b>: faster to train than tanh, and well-behaved at
  depth.</li>
  <li><b>Dropout</b>: a stochastic regulariser that prevents co-adaptation
  of units.</li>
  <li><b>Heavy data augmentation</b>: random crops, horizontal flips, PCA
  colour jitter.</li>
</ul>

<p>None of these ingredients was strictly new — ReLU, dropout, GPUs, and
ImageNet itself had all been published earlier. AlexNet's contribution was
to put them together and demonstrate that the resulting system <i>worked at
scale on a hard, real benchmark</i>. After 2012, the rest of the decade was
spent following the curve: deeper networks (VGG, GoogLeNet, <a href="https://en.wikipedia.org/wiki/Residual_neural_network" target="_blank" rel="noopener">ResNet</a>), better
optimisers, better regularisation.</p>

<h4>The lesson the field learned</h4>
<p>Compute and data, applied to a model with the right inductive biases,
beats decades of hand-engineered features. This is the same lesson that
<a href="https://en.wikipedia.org/wiki/GPT-3" target="_blank" rel="noopener">GPT-3</a> will hammer home eight years later in language. AlexNet is where the
"bitter lesson" first hit the mainstream.</p>

## Papers

### ImageNet Classification with Deep Convolutional Neural Networks
- **Authors:** Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton
- **Year:** 2012
- **Venue:** NeurIPS
- **URL:** https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html

The AlexNet paper. Worth reading both for the architecture and for the engineering — the GPU implementation notes are the part most modern readers skip and shouldn't.

### Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG)
- **Authors:** Simonyan, Zisserman
- **Year:** 2014
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/1409.1556

Showed that uniform stacks of 3x3 convolutions could go much deeper, given enough compute.

### Going Deeper with Convolutions (GoogLeNet / Inception)
- **Authors:** Szegedy et al.
- **Year:** 2014
- **Venue:** CVPR
- **URL:** https://arxiv.org/abs/1409.4842

Inception modules and the first serious attempt to think about parameter efficiency in deep CNNs.

## Extras
- [ImageNet Large Scale Visual Recognition Challenge](https://arxiv.org/abs/1409.0575)
