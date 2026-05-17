---
id: 8
title: Backpropagation
part: III. ML & AI in Chronological Order
---

<p>Backpropagation is the algorithm that finally made <b>multi-layer</b>
neural networks trainable. Rumelhart, Hinton, and Williams's 1986 paper
popularised the technique by showing it could learn useful internal
representations — hidden units that were not specified by the programmer but
that emerged from <a href="https://en.wikipedia.org/wiki/Gradient_descent" target="_blank" rel="noopener">gradient descent</a> on a labelled task.</p>

<h4>The one-line idea</h4>
<pre>
dL/dW_l = (dL/dz_l) * (dz_l/dW_l)    # chain rule, layer by layer
</pre>
<p>The forward pass computes activations; the backward pass propagates the
loss gradient back through the same computation graph using the <a href="https://en.wikipedia.org/wiki/Chain_rule" target="_blank" rel="noopener">chain rule</a>.
The cost is roughly twice the forward pass — cheap enough to be practical.
Today's autograd engines (PyTorch, JAX) are direct descendants.</p>

<h4>Why this chapter matters</h4>
<ul>
  <li>It answers the XOR objection from chapter 7: a hidden layer plus
  backprop can represent and learn any reasonable function.</li>
  <li>It established the <i>differentiable programming</i> mindset: design any
  architecture you like, as long as it is end-to-end differentiable, and let
  gradients do the work.</li>
  <li>It introduced "distributed representations" — the idea that meaning
  lives in patterns of activation across many units, not in single symbols.
  Word embeddings (chapter 13) are the obvious payoff.</li>
</ul>

<p>The technique was independently discovered several times before 1986
(Werbos 1974, Parker 1985, LeCun 1985). What Rumelhart, Hinton, and Williams
did was demonstrate it on small but suggestive problems — symmetry detection,
family-tree relations — and frame it as a general method. The field
re-entered a period of optimism, though hardware would not catch up for
another two decades.</p>

## Papers

### Learning representations by back-propagating errors
- **Authors:** David Rumelhart, Geoffrey Hinton, Ronald Williams
- **Year:** 1986
- **Venue:** Nature
- **URL:** https://web.archive.org/web/2026/https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf

The canonical reference for backprop. Hinton's own archived PDF is the open-access copy of the Nature paper.

### Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences
- **Authors:** Paul Werbos
- **Year:** 1974
- **Venue:** PhD thesis
- **URL:** https://en.wikipedia.org/wiki/Backpropagation

Werbos's PhD thesis derived backprop a decade earlier in a control-theory context. Wikipedia's history section is the cleanest open survey of priority.

### Automatic differentiation in machine learning: a survey
- **Authors:** Baydin, Pearlmutter, Radul, Siskind
- **Year:** 2018
- **Venue:** JMLR
- **URL:** https://arxiv.org/abs/1502.05767

Modern autograd as the generalisation of backprop. Useful background for anyone who has only ever used PyTorch and wants to know what the framework actually does.

## Extras
- [Wikipedia: Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
