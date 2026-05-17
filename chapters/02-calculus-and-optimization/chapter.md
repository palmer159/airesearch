---
id: 2
title: Calculus and Optimization
part: I. Math Foundations for ML & AI
---

<p>Linear algebra tells you what a network <i>computes</i>. Calculus tells you
how to <i>train</i> it. Every modern model — from a tiny logistic regression to a frontier LLM —
learns by nudging billions of parameters in the direction that makes the loss go down a little
bit. That direction is the gradient.</p>

<h4>Derivatives, partials, gradients</h4>
<p>The derivative of a one-variable function <code>f(x)</code> is its slope: how much does the
output change if I tickle the input? In ML the loss depends on millions of parameters, so we
need <b>partial derivatives</b> — the slope along one axis at a time. Stack all those partials
into a vector and you have the <b>gradient</b> &nabla;L. The gradient points in the direction of
steepest increase; its negative points downhill toward lower loss.</p>

<h4>The <a href="https://en.wikipedia.org/wiki/Chain_rule" target="_blank" rel="noopener">chain rule</a>, AKA <a href="https://en.wikipedia.org/wiki/Backpropagation" target="_blank" rel="noopener">backpropagation</a></h4>
<p>A neural net is a composition of functions: <code>L(f3(f2(f1(x))))</code>. The chain rule
says you can compute the derivative of the whole thing by multiplying the local derivatives of
each piece. That's it — that's backprop. Frameworks like PyTorch implement this automatically by
recording each operation in a graph and walking backward through it.</p>

<h4>Gradient descent and its grown-up cousins</h4>
<pre>
&theta;_{t+1} = &theta;_t - &eta; &middot; &nabla;L(&theta;_t)
</pre>
<p>That's vanilla <a href="https://en.wikipedia.org/wiki/Gradient_descent" target="_blank" rel="noopener">gradient descent</a>: take a step of size &eta; (the learning rate) downhill. In
practice we use:</p>
<ul>
  <li><b>SGD</b> — estimate the gradient on a mini-batch instead of the whole dataset. Noisier,
      but cheap and a bit of noise actually helps escape bad local minima.</li>
  <li><b>Adam / <a href="https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam" target="_blank" rel="noopener">AdamW</a></b> — keep a running estimate of the gradient's mean and variance per
      parameter, then take a normalized step. Roughly: "big steps where the gradient is small and
      stable, small steps where it's noisy." AdamW additionally decouples weight decay, which is
      the version every LLM trainer actually uses.</li>
</ul>

<h4>Convex vs non-<a href="https://en.wikipedia.org/wiki/Convex_function" target="_blank" rel="noopener">convex</a></h4>
<p>A convex loss has one bowl-shaped minimum — gradient descent is guaranteed to find it.
Neural-network losses are wildly <b>non-convex</b>: a jagged landscape with countless local
minima and saddle points. The empirical miracle of deep learning is that, in very high
dimensions, most local minima are roughly equivalent and SGD finds a good one anyway.</p>

## Papers

### Mathematics for Machine Learning (book, Part I, Chs 5 & 7)
- **Authors:** Deisenroth, Faisal, Ong
- **Year:** 2020
- **URL:** https://mml-book.github.io/

Vector calculus and continuous optimization, presented for ML readers. The chain-rule derivation here is exactly the one your autograd library implements.

### An Overview of Gradient Descent Optimization Algorithms
- **Authors:** Sebastian Ruder
- **Year:** 2017
- **URL:** https://arxiv.org/abs/1609.04747

A clear tour from vanilla SGD through momentum, Nesterov, Adagrad, RMSProp, Adam. If you've wondered why everyone uses Adam without thinking about it, this paper is the missing context.

### Adam: A Method for Stochastic Optimization
- **Authors:** Kingma, Ba
- **Year:** 2015
- **URL:** https://arxiv.org/abs/1412.6980

The original Adam paper. Section 2 is the whole algorithm in 6 lines; the rest is convergence analysis. Worth reading once to internalize what those moving averages actually represent.

### Decoupled Weight Decay Regularization (AdamW)
- **Authors:** Loshchilov, Hutter
- **Year:** 2019
- **URL:** https://arxiv.org/abs/1711.05101

Shows that the L2 regularization baked into Adam is subtly wrong and proposes AdamW. This is the optimizer used to train essentially every production LLM.

### Convex Optimization (book, full PDF)
- **Authors:** Boyd, Vandenberghe
- **Year:** 2004
- **URL:** https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf

The reference for convex optimization. Even though deep learning is non-convex, convex tools (duality, KKT, projection) show up constantly in regularizers, RLHF objectives, and constrained decoding.

### Deep Learning Book — Chapter 4: Numerical Computation, Chapter 8: Optimization
- **Authors:** Goodfellow, Bengio, Courville
- **Year:** 2016
- **URL:** https://www.deeplearningbook.org/contents/optimization.html

The chapter most ML PhD students cite when explaining why training deep nets actually works. Free HTML version on the authors' site.

## Extras
- [3Blue1Brown — Essence of Calculus](https://www.3blue1brown.com/topics/calculus)
- [3Blue1Brown — Backpropagation, intuitively](https://www.3blue1brown.com/lessons/backpropagation)
- [Distill: Why Momentum Really Works](https://distill.pub/2017/momentum/)
