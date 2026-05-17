"""Math foundations chapters (Part I) for the LLM Study Guide.

Authored as plain Python data so regenerate.py can ingest them. Citation
policy: open-access only — arXiv, Wikipedia, 3Blue1Brown, MIT OCW, MML book,
immersivemath, Stanford public notes, OpenIntro, faculty PDFs.
"""

from _chapter_types import Chapter, Paper, Extra


MATH_CHAPTERS: list[Chapter] = [
    Chapter(
        id=1,
        slug="linear-algebra-for-ml",
        part="I. Math Foundations for ML & AI",
        title="Linear Algebra for Machine Learning",
        summary_html="""<p>If you only learn one branch of math for modern ML, make it linear algebra. A
neural network — including every transformer you'll meet later in this guide — is, at runtime,
just a long chain of matrix multiplications glued together by a few cheap nonlinearities. Get
comfortable with vectors and matrices and most of the rest of deep learning becomes notation.</p>

<h4>Vectors are directions; matrices are functions</h4>
<p>Think of a vector as an arrow in some high-dimensional space (a token embedding lives in
<i>d</i>-dimensional space, often 768 or 4096). A matrix is a <b>linear function</b> that takes
arrows in and spits new arrows out — it stretches, rotates, or projects them. Matrix
multiplication <i>composes</i> two such functions. Once that picture clicks, "deep network" just
means "compose a lot of these, with little squashing functions in between."</p>

<h4>The dot product is similarity</h4>
<p>The <b>dot product</b> <code>a &middot; b</code> measures how aligned two vectors are. This is
the entire intuition behind attention: query and key vectors with a big dot product are "talking
about the same thing." Stack a batch of queries and keys into matrices and you get the
attention score matrix in one shot:</p>

<pre>
scores = Q K^T          # every query dotted with every key
output = softmax(scores) V
</pre>

<h4>Eigenvectors and SVD: finding the natural axes</h4>
<ul>
  <li><b>Eigenvectors</b> are the directions a matrix doesn't rotate — it only scales them, by
      its eigenvalue. They reveal a transformation's "natural axes."</li>
  <li><b>Singular Value Decomposition</b> generalizes this to any matrix:
      <code>A = U &Sigma; V^T</code>. The columns of <i>U</i> and <i>V</i> are orthogonal axes;
      &Sigma; tells you how much the matrix stretches along each. SVD underpins PCA, low-rank
      approximation, and the <b>LoRA</b> adapters used to fine-tune big LLMs cheaply.</li>
</ul>

<p>So when you read "every transformer step is matmul," it's not hype — it's literal. Embeddings,
attention, MLP blocks, output projection: matmul, matmul, matmul. Linear algebra is the
substrate.</p>""",
        papers=[
            Paper(
                title="Mathematics for Machine Learning (book, Part I)",
                authors="Deisenroth, Faisal, Ong",
                year="2020",
                url="https://mml-book.github.io/",
                summary="The friendliest from-scratch treatment of linear algebra for ML. Chapters 2–4 cover vectors, matrices, decompositions, and analytic geometry with the right amount of rigor for a postgrad reader.",
            ),
            Paper(
                title="Essence of Linear Algebra (video series)",
                authors="Grant Sanderson (3Blue1Brown)",
                year="2016",
                url="https://www.3blue1brown.com/topics/linear-algebra",
                summary="The visual gold standard. Watch this if you ever felt like you were memorizing matrix rules without seeing them. Pair the videos with the MML book and you have a complete intuition pipeline.",
            ),
            Paper(
                title="Linear Algebra Review and Reference (CS229 notes)",
                authors="Zico Kolter, updated by Chuong Do",
                year="2015",
                url="https://cs229.stanford.edu/section/cs229-linalg.pdf",
                summary="Stanford's compact reference for the linear algebra you actually use in ML — inner products, norms, eigenstuff, matrix calculus. Print it, fold it, keep it next to your laptop.",
            ),
            Paper(
                title="The Matrix Cookbook",
                authors="Petersen, Pedersen",
                year="2012",
                url="https://www2.compute.dtu.dk/pubdb/views/edoc_download.php/3274/pdf/imm3274.pdf",
                summary="The lookup table for matrix identities and derivatives. You will not read this front-to-back; you will Ctrl-F it forever.",
            ),
            Paper(
                title="Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions",
                authors="Halko, Martinsson, Tropp",
                year="2011",
                url="https://arxiv.org/abs/0909.4061",
                summary="The randomized SVD paper. Explains how the low-rank approximations behind PCA, embeddings, and LoRA are computed at scale. A good bridge from textbook SVD to production-grade matrix math.",
            ),
        ],
        extras=[
            Extra(
                label="immersivemath — interactive linear algebra",
                url="http://immersivemath.com/ila/index.html",
            ),
            Extra(
                label="MIT OCW 18.06 — Gilbert Strang's Linear Algebra",
                url="https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/",
            ),
            Extra(
                label="Wikipedia: Singular Value Decomposition",
                url="https://en.wikipedia.org/wiki/Singular_value_decomposition",
            ),
        ],
    ),
    Chapter(
        id=2,
        slug="calculus-and-optimization",
        part="I. Math Foundations for ML & AI",
        title="Calculus and Optimization",
        summary_html="""<p>Linear algebra tells you what a network <i>computes</i>. Calculus tells you
how to <i>train</i> it. Every modern model — from a tiny logistic regression to a frontier LLM —
learns by nudging billions of parameters in the direction that makes the loss go down a little
bit. That direction is the gradient.</p>

<h4>Derivatives, partials, gradients</h4>
<p>The derivative of a one-variable function <code>f(x)</code> is its slope: how much does the
output change if I tickle the input? In ML the loss depends on millions of parameters, so we
need <b>partial derivatives</b> — the slope along one axis at a time. Stack all those partials
into a vector and you have the <b>gradient</b> &nabla;L. The gradient points in the direction of
steepest increase; its negative points downhill toward lower loss.</p>

<h4>The chain rule, AKA backpropagation</h4>
<p>A neural net is a composition of functions: <code>L(f3(f2(f1(x))))</code>. The chain rule
says you can compute the derivative of the whole thing by multiplying the local derivatives of
each piece. That's it — that's backprop. Frameworks like PyTorch implement this automatically by
recording each operation in a graph and walking backward through it.</p>

<h4>Gradient descent and its grown-up cousins</h4>
<pre>
&theta;_{t+1} = &theta;_t - &eta; &middot; &nabla;L(&theta;_t)
</pre>
<p>That's vanilla gradient descent: take a step of size &eta; (the learning rate) downhill. In
practice we use:</p>
<ul>
  <li><b>SGD</b> — estimate the gradient on a mini-batch instead of the whole dataset. Noisier,
      but cheap and a bit of noise actually helps escape bad local minima.</li>
  <li><b>Adam / AdamW</b> — keep a running estimate of the gradient's mean and variance per
      parameter, then take a normalized step. Roughly: "big steps where the gradient is small and
      stable, small steps where it's noisy." AdamW additionally decouples weight decay, which is
      the version every LLM trainer actually uses.</li>
</ul>

<h4>Convex vs non-convex</h4>
<p>A convex loss has one bowl-shaped minimum — gradient descent is guaranteed to find it.
Neural-network losses are wildly <b>non-convex</b>: a jagged landscape with countless local
minima and saddle points. The empirical miracle of deep learning is that, in very high
dimensions, most local minima are roughly equivalent and SGD finds a good one anyway.</p>""",
        papers=[
            Paper(
                title="Mathematics for Machine Learning (book, Part I, Chs 5 & 7)",
                authors="Deisenroth, Faisal, Ong",
                year="2020",
                url="https://mml-book.github.io/",
                summary="Vector calculus and continuous optimization, presented for ML readers. The chain-rule derivation here is exactly the one your autograd library implements.",
            ),
            Paper(
                title="An Overview of Gradient Descent Optimization Algorithms",
                authors="Sebastian Ruder",
                year="2017",
                url="https://arxiv.org/abs/1609.04747",
                summary="A clear tour from vanilla SGD through momentum, Nesterov, Adagrad, RMSProp, Adam. If you've wondered why everyone uses Adam without thinking about it, this paper is the missing context.",
            ),
            Paper(
                title="Adam: A Method for Stochastic Optimization",
                authors="Kingma, Ba",
                year="2015",
                url="https://arxiv.org/abs/1412.6980",
                summary="The original Adam paper. Section 2 is the whole algorithm in 6 lines; the rest is convergence analysis. Worth reading once to internalize what those moving averages actually represent.",
            ),
            Paper(
                title="Decoupled Weight Decay Regularization (AdamW)",
                authors="Loshchilov, Hutter",
                year="2019",
                url="https://arxiv.org/abs/1711.05101",
                summary="Shows that the L2 regularization baked into Adam is subtly wrong and proposes AdamW. This is the optimizer used to train essentially every production LLM.",
            ),
            Paper(
                title="Convex Optimization (book, full PDF)",
                authors="Boyd, Vandenberghe",
                year="2004",
                url="https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf",
                summary="The reference for convex optimization. Even though deep learning is non-convex, convex tools (duality, KKT, projection) show up constantly in regularizers, RLHF objectives, and constrained decoding.",
            ),
            Paper(
                title="Deep Learning Book — Chapter 4: Numerical Computation, Chapter 8: Optimization",
                authors="Goodfellow, Bengio, Courville",
                year="2016",
                url="https://www.deeplearningbook.org/contents/optimization.html",
                summary="The chapter most ML PhD students cite when explaining why training deep nets actually works. Free HTML version on the authors' site.",
            ),
        ],
        extras=[
            Extra(
                label="3Blue1Brown — Essence of Calculus",
                url="https://www.3blue1brown.com/topics/calculus",
            ),
            Extra(
                label="3Blue1Brown — Backpropagation, intuitively",
                url="https://www.3blue1brown.com/lessons/backpropagation",
            ),
            Extra(
                label="Distill: Why Momentum Really Works",
                url="https://distill.pub/2017/momentum/",
            ),
        ],
    ),
    Chapter(
        id=3,
        slug="probability-statistics-information-theory",
        part="I. Math Foundations for ML & AI",
        title="Probability, Statistics, and Information Theory",
        summary_html="""<p>Language models don't predict <i>the</i> next token; they predict a
<b>probability distribution</b> over the next token. To reason about that you need a working
fluency in probability, a pinch of statistics, and the slice of information theory that gives us
our loss function.</p>

<h4>Random variables and distributions</h4>
<p>A random variable is a number whose value depends on chance. A distribution is the recipe that
says how likely each value is. The two distributions to know cold for ML are the <b>Gaussian</b>
(used everywhere — weight init, noise models, latent variables) and the <b>categorical</b>
(used every time a model picks one of a finite set of options, like the next token).</p>

<h4>Bayes and maximum likelihood</h4>
<p>Bayes' rule is just bookkeeping for "how should I update my beliefs given new evidence":</p>
<pre>
P(H | D) = P(D | H) &middot; P(H) / P(D)
</pre>
<p><b>Maximum likelihood estimation</b> (MLE) is the workhorse training principle: pick the
parameters &theta; that make the observed data as probable as possible. Almost all neural-network
training, including LLM pretraining, is MLE in disguise.</p>

<h4>Entropy, cross-entropy, KL — and why they matter</h4>
<ul>
  <li><b>Entropy</b> H(p) measures how uncertain a distribution is. A fair coin has 1 bit of
      entropy; a loaded coin has less.</li>
  <li><b>Cross-entropy</b> H(p, q) measures how surprised you are when reality is <i>p</i> but
      you expected <i>q</i>. If your model q matches the true distribution p, surprise is
      minimal.</li>
  <li><b>KL divergence</b> KL(p || q) is the "extra surprise" from using q instead of p — it
      shows up in RLHF, variational inference, and distillation.</li>
</ul>

<p>Here's the punchline that connects all of this to LLMs. When you train a language model, you
have one true next-token (a one-hot p) and the model's predicted distribution q. Minimizing
cross-entropy is exactly maximizing the log-likelihood of the training corpus:</p>

<pre>
L = - &Sigma;_t  log q(x_t | x_&lt;t)
</pre>

<p>Every loss curve you've ever seen on an LLM training dashboard is plotting this number. And
<a href="https://en.wikipedia.org/wiki/Perplexity" target="_blank" rel="noopener">perplexity</a>,
the metric LLM people quote, is just <code>exp(L)</code> — cross-entropy in nicer units.</p>""",
        papers=[
            Paper(
                title="A Mathematical Theory of Communication",
                authors="Claude Shannon",
                year="1948",
                url="https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf",
                summary="The paper that invented information theory. Defines entropy, channel capacity, and the conceptual machinery underneath cross-entropy loss. Astonishingly readable for a foundational paper.",
            ),
            Paper(
                title="Mathematics for Machine Learning (book, Ch 6: Probability and Distributions)",
                authors="Deisenroth, Faisal, Ong",
                year="2020",
                url="https://mml-book.github.io/",
                summary="The probability chapter you wish you'd had in undergrad — distributions, Bayes, conjugate priors, sufficient statistics, all framed for ML use.",
            ),
            Paper(
                title="OpenIntro Statistics (4th ed.)",
                authors="Diez, Çetinkaya-Rundel, Barr",
                year="2019",
                url="https://www.openintro.org/book/os/",
                summary="The clearest free intro-stats textbook. Skim for fluency on sampling, estimation, hypothesis testing — the dialect of every applied ML paper's results section.",
            ),
            Paper(
                title="Probability Theory Review (CS229 notes)",
                authors="Arian Maleki, Tom Do",
                year="2015",
                url="https://cs229.stanford.edu/section/cs229-prob.pdf",
                summary="Stanford's compact ML-flavored probability primer. Pairs perfectly with the linear-algebra notes from Chapter 1.",
            ),
            Paper(
                title="Pattern Recognition and Machine Learning — Chapter 1.6: Information Theory (author's free PDF)",
                authors="Christopher Bishop",
                year="2006",
                url="https://www.microsoft.com/en-us/research/wp-content/uploads/2016/05/Bishop-PRML-sample.pdf",
                summary="Bishop's elegant derivation of entropy, mutual information, and KL divergence in the ML context. The official sample-chapter PDF that Microsoft Research hosts.",
            ),
            Paper(
                title="Information Theory, Inference, and Learning Algorithms",
                authors="David MacKay",
                year="2003",
                url="https://www.inference.org.uk/itprnn/book.pdf",
                summary="MacKay's whole book, free on his Cambridge site. Connects Shannon information, Bayesian inference, and neural networks under one cover. The single best resource for this chapter if you only pick one.",
            ),
        ],
        extras=[
            Extra(
                label="3Blue1Brown — Bayes' theorem, the geometry of changing beliefs",
                url="https://www.3blue1brown.com/lessons/bayes-theorem",
            ),
            Extra(
                label="Wikipedia: Cross-entropy",
                url="https://en.wikipedia.org/wiki/Cross-entropy",
            ),
            Extra(
                label="Wikipedia: Kullback-Leibler divergence",
                url="https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence",
            ),
        ],
    ),
]
