---
id: 3
title: Probability, Statistics, and Information Theory
part: I. Math Foundations for ML & AI
---

<p>Language models don't predict <i>the</i> next token; they predict a
<b>probability distribution</b> over the next token. To reason about that you need a working
fluency in probability, a pinch of statistics, and the slice of <a href="https://en.wikipedia.org/wiki/Information_theory" target="_blank" rel="noopener">information theory</a> that gives us
our loss function.</p>

<h4>Random variables and distributions</h4>
<p>A random variable is a number whose value depends on chance. A distribution is the recipe that
says how likely each value is. The two distributions to know cold for ML are the <b>Gaussian</b>
(used everywhere — weight init, noise models, latent variables) and the <b>categorical</b>
(used every time a model picks one of a finite set of options, like the next token).</p>

<h4><a href="https://en.wikipedia.org/wiki/Bayes%27_theorem" target="_blank" rel="noopener">Bayes</a> and <a href="https://en.wikipedia.org/wiki/Maximum_likelihood_estimation" target="_blank" rel="noopener">maximum likelihood</a></h4>
<p>Bayes' rule is just bookkeeping for "how should I update my beliefs given new evidence":</p>
<pre>
P(H | D) = P(D | H) &middot; P(H) / P(D)
</pre>
<p><b>Maximum likelihood estimation</b> (MLE) is the workhorse training principle: pick the
parameters &theta; that make the observed data as probable as possible. Almost all neural-network
training, including LLM pretraining, is MLE in disguise.</p>

<h4>Entropy, <a href="https://en.wikipedia.org/wiki/Cross-entropy" target="_blank" rel="noopener">cross-entropy</a>, KL — and why they matter</h4>
<ul>
  <li><b>Entropy</b> H(p) measures how uncertain a distribution is. A fair coin has 1 bit of
      <a href="https://en.wikipedia.org/wiki/Entropy_(information_theory)" target="_blank" rel="noopener">entropy</a>; a loaded coin has less.</li>
  <li><b>Cross-entropy</b> H(p, q) measures how surprised you are when reality is <i>p</i> but
      you expected <i>q</i>. If your model q matches the true distribution p, surprise is
      minimal.</li>
  <li><b><a href="https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence" target="_blank" rel="noopener">KL divergence</a></b> KL(p || q) is the "extra surprise" from using q instead of p — it
      shows up in <a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback" target="_blank" rel="noopener">RLHF</a>, variational inference, and distillation.</li>
</ul>

<p>Here's the punchline that connects all of this to LLMs. When you train a language model, you
have one true next-token (a one-hot p) and the model's predicted distribution q. Minimizing
cross-entropy is exactly maximizing the log-likelihood of the training corpus:</p>

<pre>
L = - &Sigma;_t  log q(x_t | x_&lt;t)
</pre>

<p>Every loss curve you've ever seen on an LLM training dashboard is plotting this number. And
<a href="https://en.wikipedia.org/wiki/Perplexity" target="_blank" rel="noopener">perplexity</a>,
the metric LLM people quote, is just <code>exp(L)</code> — cross-entropy in nicer units.</p>

## Papers

### A Mathematical Theory of Communication
- **Authors:** Claude Shannon
- **Year:** 1948
- **URL:** https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf

The paper that invented information theory. Defines entropy, channel capacity, and the conceptual machinery underneath cross-entropy loss. Astonishingly readable for a foundational paper.

### Mathematics for Machine Learning (book, Ch 6: Probability and Distributions)
- **Authors:** Deisenroth, Faisal, Ong
- **Year:** 2020
- **URL:** https://mml-book.github.io/

The probability chapter you wish you'd had in undergrad — distributions, Bayes, conjugate priors, sufficient statistics, all framed for ML use.

### OpenIntro Statistics (4th ed.)
- **Authors:** Diez, Çetinkaya-Rundel, Barr
- **Year:** 2019
- **URL:** https://www.openintro.org/book/os/

The clearest free intro-stats textbook. Skim for fluency on sampling, estimation, hypothesis testing — the dialect of every applied ML paper's results section.

### Probability Theory Review (CS229 notes)
- **Authors:** Arian Maleki, Tom Do
- **Year:** 2015
- **URL:** https://cs229.stanford.edu/section/cs229-prob.pdf

Stanford's compact ML-flavored probability primer. Pairs perfectly with the linear-algebra notes from Chapter 1.

### Pattern Recognition and Machine Learning — Chapter 1.6: Information Theory (author's free PDF)
- **Authors:** Christopher Bishop
- **Year:** 2006
- **URL:** https://www.microsoft.com/en-us/research/wp-content/uploads/2016/05/Bishop-PRML-sample.pdf

Bishop's elegant derivation of entropy, mutual information, and KL divergence in the ML context. The official sample-chapter PDF that Microsoft Research hosts.

### Information Theory, Inference, and Learning Algorithms
- **Authors:** David MacKay
- **Year:** 2003
- **URL:** https://www.inference.org.uk/itprnn/book.pdf

MacKay's whole book, free on his Cambridge site. Connects Shannon information, Bayesian inference, and neural networks under one cover. The single best resource for this chapter if you only pick one.

## Extras
- [3Blue1Brown — Bayes' theorem, the geometry of changing beliefs](https://www.3blue1brown.com/lessons/bayes-theorem)
- [Wikipedia: Cross-entropy](https://en.wikipedia.org/wiki/Cross-entropy)
- [Wikipedia: Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
