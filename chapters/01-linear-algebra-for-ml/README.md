---
id: 1
title: Linear Algebra for Machine Learning
part: I. Math Foundations for ML & AI
---

<p>If you only learn one branch of math for modern ML, make it linear algebra. A
neural network — including every <a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)" target="_blank" rel="noopener">transformer</a> you'll meet later in this guide — is, at runtime,
just a long chain of matrix multiplications glued together by a few cheap nonlinearities. Get
comfortable with vectors and matrices and most of the rest of deep learning becomes notation.</p>

<h4>Vectors are directions; matrices are functions</h4>
<p>Think of a vector as an arrow in some high-dimensional space (a token embedding lives in
<i>d</i>-dimensional space, often 768 or 4096). A matrix is a <b>linear function</b> that takes
arrows in and spits new arrows out — it stretches, rotates, or projects them. Matrix
multiplication <i>composes</i> two such functions. Once that picture clicks, "deep network" just
means "compose a lot of these, with little squashing functions in between."</p>

<h4>The <a href="https://en.wikipedia.org/wiki/Dot_product" target="_blank" rel="noopener">dot product</a> is similarity</h4>
<p>The <b>dot product</b> <code>a &middot; b</code> measures how aligned two vectors are. This is
the entire intuition behind attention: query and key vectors with a big dot product are "talking
about the same thing." Stack a batch of queries and keys into matrices and you get the
attention score matrix in one shot:</p>

<pre>
scores = Q K^T          # every query dotted with every key
output = softmax(scores) V
</pre>

<h4>Eigenvectors and <a href="https://en.wikipedia.org/wiki/Singular_value_decomposition" target="_blank" rel="noopener">SVD</a>: finding the natural axes</h4>
<ul>
  <li><b>Eigenvectors</b> are the directions a matrix doesn't rotate — it only scales them, by
      its <a href="https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors" target="_blank" rel="noopener">eigenvalue</a>. They reveal a transformation's "natural axes."</li>
  <li><b>Singular Value Decomposition</b> generalizes this to any matrix:
      <code>A = U &Sigma; V^T</code>. The columns of <i>U</i> and <i>V</i> are orthogonal axes;
      &Sigma; tells you how much the matrix stretches along each. SVD underpins PCA, low-rank
      approximation, and the <b><a href="https://en.wikipedia.org/wiki/Low-rank_adaptation" target="_blank" rel="noopener">LoRA</a></b> adapters used to fine-tune big LLMs cheaply.</li>
</ul>

<p>So when you read "every transformer step is matmul," it's not hype — it's literal. Embeddings,
attention, MLP blocks, output projection: matmul, matmul, matmul. Linear algebra is the
substrate.</p>

## Papers

### Mathematics for Machine Learning (book, Part I)
- **Authors:** Deisenroth, Faisal, Ong
- **Year:** 2020
- **URL:** https://mml-book.github.io/

The friendliest from-scratch treatment of linear algebra for ML. Chapters 2–4 cover vectors, matrices, decompositions, and analytic geometry with the right amount of rigor for a postgrad reader.

### Essence of Linear Algebra (video series)
- **Authors:** Grant Sanderson (3Blue1Brown)
- **Year:** 2016
- **URL:** https://www.3blue1brown.com/topics/linear-algebra

The visual gold standard. Watch this if you ever felt like you were memorizing matrix rules without seeing them. Pair the videos with the MML book and you have a complete intuition pipeline.

### Linear Algebra Review and Reference (CS229 notes)
- **Authors:** Zico Kolter, updated by Chuong Do
- **Year:** 2015
- **URL:** https://cs229.stanford.edu/section/cs229-linalg.pdf

Stanford's compact reference for the linear algebra you actually use in ML — inner products, norms, eigenstuff, matrix calculus. Print it, fold it, keep it next to your laptop.

### The Matrix Cookbook
- **Authors:** Petersen, Pedersen
- **Year:** 2012
- **URL:** https://www2.compute.dtu.dk/pubdb/views/edoc_download.php/3274/pdf/imm3274.pdf

The lookup table for matrix identities and derivatives. You will not read this front-to-back; you will Ctrl-F it forever.

### Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions
- **Authors:** Halko, Martinsson, Tropp
- **Year:** 2011
- **URL:** https://arxiv.org/abs/0909.4061

The randomized SVD paper. Explains how the low-rank approximations behind PCA, embeddings, and LoRA are computed at scale. A good bridge from textbook SVD to production-grade matrix math.

## Extras
- [immersivemath — interactive linear algebra](http://immersivemath.com/ila/index.html)
- [MIT OCW 18.06 — Gilbert Strang's Linear Algebra](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)
- [Wikipedia: Singular Value Decomposition](https://en.wikipedia.org/wiki/Singular_value_decomposition)
