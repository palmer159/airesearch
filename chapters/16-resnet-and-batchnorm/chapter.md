---
id: 16
title: ResNet and Batch Normalization
part: III. ML & AI in Chronological Order
---

<p>2015 was the year deep networks stopped being shallow. Two ideas, both
from Microsoft Research and Google Brain respectively, made it possible to
train networks of 50, 100, even 1000 layers. They are the architectural
plumbing that every modern model — Transformer included — quietly relies
on.</p>

<h4>Batch Normalization (Ioffe and Szegedy, 2015)</h4>
<p>Normalise each activation across the mini-batch to zero mean and unit
variance, then scale and shift with learned parameters. The effect is to
keep activations well-conditioned through training and to make the loss
landscape much smoother. BatchNorm cut ImageNet training time by a factor
of 14× and quietly raised the depth ceiling.</p>

<h4><a href="https://en.wikipedia.org/wiki/Residual_neural_network" target="_blank" rel="noopener">ResNet</a> (He, Zhang, Ren, Sun, 2015)</h4>
<p>Add a skip connection around every couple of layers:</p>
<pre>
y = F(x, W) + x
</pre>
<p>If the optimal mapping for a block is close to the identity, the residual
F can stay near zero — much easier than asking deep stacked layers to learn
the identity from scratch. The result: ImageNet networks with 152 layers
that beat human-level top-5 accuracy. The same paper introduced the
"deep is fine, just make it residual" principle that the field has not yet
walked back from.</p>

<h4>Why both belong in the same chapter</h4>
<ul>
  <li>BatchNorm controlled the <i>scale</i> of activations and gradients.</li>
  <li>ResNet gave gradients a <i>highway</i> back to early layers.</li>
  <li>Together they made arbitrary depth practical.</li>
  <li>The Transformer's "Add &amp; Norm" sub-block — the residual connection
  followed by LayerNorm — is a direct descendant of these two ideas.</li>
</ul>

<p>Almost every architecture in the rest of this book has ResNet-style
skips and some form of normalisation in it. The exceptions are conscious
research choices, not defaults.</p>

## Papers

### Deep Residual Learning for Image Recognition
- **Authors:** Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun
- **Year:** 2015
- **Venue:** CVPR
- **URL:** https://arxiv.org/abs/1512.03385

The ResNet paper. The plot of training error vs depth, with and without residuals, is one of the most influential figures in deep learning.

### Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift
- **Authors:** Sergey Ioffe, Christian Szegedy
- **Year:** 2015
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/1502.03167

The BatchNorm paper. The 'internal covariate shift' framing has been challenged by later work, but the method is universal.

### Layer Normalization
- **Authors:** Ba, Kiros, Hinton
- **Year:** 2016
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1607.06450

The variant that works for recurrent and transformer models, where mini-batch statistics aren't a clean signal.

## Extras
- [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027)
