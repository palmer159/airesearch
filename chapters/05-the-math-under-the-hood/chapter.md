---
id: 5
title: The Math Under the Hood
part: II. LLMs and SLMs: What and Why
---

<p>You just read three chapters of math.  Here's the payoff: every piece of
it shows up at a specific place inside an LLM.  This chapter is the map.</p>

<h4>Linear algebra → attention is matmul + softmax</h4>
<p>Everything inside a Transformer is <a href="https://en.wikipedia.org/wiki/Matrix_multiplication" target="_blank" rel="noopener">matrix multiplication</a>.  Token embeddings
are rows of a matrix.  Each attention head computes three projections
(<code>Q</code>, <code>K</code>, <code>V</code>) — three matmuls.  The
attention pattern itself is one more matmul plus a
<a href="https://en.wikipedia.org/wiki/Softmax_function" target="_blank" rel="noopener">softmax</a>:</p>
<pre>
Attention(Q, K, V) = softmax( Q K^T / sqrt(d_k) ) V
</pre>
<p>The MLP block?  Two more matmuls with a nonlinearity in between.  When
people say "an LLM is just a stack of matmuls" they mean it almost literally —
which is exactly why GPUs and TPUs, which do nothing but matmul fast, are the
right hardware.  Everything you learned about eigenvectors, low-rank
approximations, and <a href="https://en.wikipedia.org/wiki/Singular_value_decomposition" target="_blank" rel="noopener">SVD</a> shows up later in
<a href="https://arxiv.org/abs/2106.09685" target="_blank" rel="noopener">LoRA</a>
and quantization.</p>

<h4>Calculus and optimization → backprop trains the model</h4>
<p>The loss is a single scalar.  To improve the model we need
<code>dLoss/dParameter</code> for every parameter — billions of them.  That's
<a href="https://en.wikipedia.org/wiki/Backpropagation" target="_blank" rel="noopener">backpropagation</a>:
the <a href="https://en.wikipedia.org/wiki/Chain_rule" target="_blank" rel="noopener">chain rule</a>, applied mechanically, in reverse.  An optimizer like
<a href="https://arxiv.org/abs/1412.6980" target="_blank" rel="noopener">Adam</a>
or <a href="https://en.wikipedia.org/wiki/Stochastic_gradient_descent#Adam" target="_blank" rel="noopener">AdamW</a> takes those gradients and nudges the parameters.  Learning-rate
schedules, warmup, gradient clipping — all are tools to keep that
multi-trillion-step optimization stable.</p>

<h4>Probability and <a href="https://en.wikipedia.org/wiki/Information_theory" target="_blank" rel="noopener">information theory</a> → loss and sampling</h4>
<ul>
  <li><b>Training loss = <a href="https://en.wikipedia.org/wiki/Cross-entropy" target="_blank" rel="noopener">cross-entropy</a>.</b>  At every position, the model
      outputs a distribution over the vocabulary; the loss is the
      negative log-probability assigned to the actual next token.  That's
      KL-divergence-from-the-data, dressed up.</li>
  <li><b>Perplexity = exp(cross-<a href="https://en.wikipedia.org/wiki/Entropy_(information_theory)" target="_blank" rel="noopener">entropy</a>).</b>  Same number, prettier units.</li>
  <li><b>Inference is sampling.</b>  Greedy, top-k, top-p (nucleus), and
      temperature are all just ways to draw from that next-token
      distribution.  Information theory tells you why temperature 0 is
      brittle and why top-p ≈ 0.9 tends to feel "right."</li>
</ul>
<p>If a future chapter mentions "the gradient flowed through the softmax" or
"we minimize the KL" — you already know what's happening.  Keep going.</p>

## Papers

### Attention Is All You Need
- **Authors:** Vaswani et al.
- **Year:** 2017
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/1706.03762

The original Transformer paper. Read it now that you have the linear algebra; the equations should feel obvious.

### Learning representations by back-propagating errors
- **Authors:** Rumelhart, Hinton, Williams
- **Year:** 1986
- **Venue:** Nature (open access via Stanford)
- **URL:** https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf

The 1986 paper that put backprop on the map. Short, readable, and you can follow every step with one calculus chapter under your belt.

### Adam: A Method for Stochastic Optimization
- **Authors:** Kingma, Ba
- **Year:** 2015
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/1412.6980

The optimizer that trains nearly every modern LLM (usually as AdamW). Adaptive per-parameter learning rates with momentum.

### The Curious Case of Neural Text Degeneration
- **Authors:** Holtzman, Buys, Du, Forbes, Choi
- **Year:** 2020
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/1904.09751

Where nucleus (top-p) sampling comes from. The clearest explanation of why naive sampling produces gibberish and how information theory points to the fix.

### LoRA: Low-Rank Adaptation of Large Language Models
- **Authors:** Hu et al.
- **Year:** 2021
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2106.09685

A direct payoff of the linear-algebra chapter: fine-tune by adding a low-rank update to weight matrices. Cuts the trainable-parameter count by orders of magnitude.

### The Illustrated Transformer
- **Authors:** Jay Alammar
- **Year:** 2018
- **Venue:** blog
- **URL:** https://jalammar.github.io/illustrated-transformer/

The visual companion. Useful even on a re-read because the diagrams pin down which matmul is which.

## Extras
- [Wikipedia: Backpropagation](https://en.wikipedia.org/wiki/Backpropagation)
- [Wikipedia: Softmax function](https://en.wikipedia.org/wiki/Softmax_function)
- [Lilian Weng: Attention? Attention!](https://lilianweng.github.io/posts/2018-06-24-attention/)
