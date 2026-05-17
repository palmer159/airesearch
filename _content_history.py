"""Chronological-history chapters (ids 7..30) for the LLM Study Guide.

This module is consumed by ``regenerate.py``. Each entry is a single key idea
in the history of ML/AI, in order of invention, written for a postgrad CS
reader who has just finished the math and overview chapters.

Citation policy: open-access only.
"""

from __future__ import annotations

from _chapter_types import Chapter, Paper, Extra


PART = "III. ML & AI in Chronological Order"


HISTORY_CHAPTERS: list[Chapter] = [
    # ----------------------------------------------------------------- #
    # 7. 1958 — Perceptron
    # ----------------------------------------------------------------- #
    Chapter(
        id=7,
        slug="perceptron",
        part=PART,
        title="The Perceptron",
        summary_html="""
<p>In 1958 Frank Rosenblatt introduced the <b>perceptron</b>: a single
trainable linear threshold unit that could learn a binary classification rule
from labelled examples. It is the seed from which everything in this book
grows. The model itself is almost trivially simple — a weighted sum followed
by a step function — but the <i>learning rule</i> was the breakthrough.</p>

<h4>The model and its update rule</h4>
<pre>
y_hat = sign( w . x + b )
if y_hat != y:  w &lt;- w + eta * y * x
</pre>
<p>Rosenblatt proved a convergence theorem: if the data is linearly separable,
the perceptron rule will find a separating hyperplane in finite steps. For the
first time, "learning from data" had a mechanical, terminating procedure.</p>

<h4>Why it stalled</h4>
<ul>
  <li>Minsky and Papert's 1969 book <i>Perceptrons</i> showed that a single
  unit cannot represent XOR or any non-linearly-separable function.</li>
  <li>Stacking units into multiple layers was known to fix this in principle,
  but nobody had a working algorithm to train the hidden weights.</li>
  <li>Funding dried up. The first "AI winter" followed.</li>
</ul>

<p>The perceptron sets the template that every later model in this part
inherits: <i>parameters, a loss, and an update rule that nudges the
parameters toward lower loss</i>. Modern neurons are still
<code>activation(W x + b)</code>; what changed is depth, the activation, the
optimizer, and the scale of the data. Reading Rosenblatt today is striking
because so little of the core idea has changed in 68 years — only the
engineering around it.</p>
""",
        papers=[
            Paper(
                title="The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain",
                authors="Frank Rosenblatt",
                year="1958",
                url="https://en.wikipedia.org/wiki/Perceptron",
                summary="Wikipedia's article reproduces the model, the update rule, and the convergence theorem with citations to the original Cornell technical report. Rosenblatt's own 1958 paper is paywalled in APA's archive; this is the authoritative open mirror.",
                venue="encyclopedia",
            ),
            Paper(
                title="Perceptrons (book, 1969)",
                authors="Marvin Minsky, Seymour Papert",
                year="1969",
                url="https://en.wikipedia.org/wiki/Perceptrons_(book)",
                summary="The critique that ended the first wave of neural-net research by formally showing the limits of single-layer perceptrons. Worth reading historically — its conclusions were narrower than the field assumed.",
                venue="MIT Press",
            ),
            Paper(
                title="Learning representations by back-propagating errors",
                authors="Rumelhart, Hinton, Williams",
                year="1986",
                url="https://web.archive.org/web/2026/https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf",
                summary="The eventual answer to Minsky and Papert: train multi-layer perceptrons by backpropagation. Listed here so the reader can see how the next chapter directly responds to this one.",
                venue="Nature",
            ),
        ],
        extras=[
            Extra(
                label="Wikipedia: Perceptron",
                url="https://en.wikipedia.org/wiki/Perceptron",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 8. 1986 — Backpropagation
    # ----------------------------------------------------------------- #
    Chapter(
        id=8,
        slug="backpropagation",
        part=PART,
        title="Backpropagation",
        summary_html="""
<p>Backpropagation is the algorithm that finally made <b>multi-layer</b>
neural networks trainable. Rumelhart, Hinton, and Williams's 1986 paper
popularised the technique by showing it could learn useful internal
representations — hidden units that were not specified by the programmer but
that emerged from gradient descent on a labelled task.</p>

<h4>The one-line idea</h4>
<pre>
dL/dW_l = (dL/dz_l) * (dz_l/dW_l)    # chain rule, layer by layer
</pre>
<p>The forward pass computes activations; the backward pass propagates the
loss gradient back through the same computation graph using the chain rule.
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
""",
        papers=[
            Paper(
                title="Learning representations by back-propagating errors",
                authors="David Rumelhart, Geoffrey Hinton, Ronald Williams",
                year="1986",
                url="https://web.archive.org/web/2026/https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf",
                summary="The canonical reference for backprop. Hinton's own archived PDF is the open-access copy of the Nature paper.",
                venue="Nature",
            ),
            Paper(
                title="Beyond Regression: New Tools for Prediction and Analysis in the Behavioral Sciences",
                authors="Paul Werbos",
                year="1974",
                url="https://en.wikipedia.org/wiki/Backpropagation",
                summary="Werbos's PhD thesis derived backprop a decade earlier in a control-theory context. Wikipedia's history section is the cleanest open survey of priority.",
                venue="PhD thesis",
            ),
            Paper(
                title="Automatic differentiation in machine learning: a survey",
                authors="Baydin, Pearlmutter, Radul, Siskind",
                year="2018",
                url="https://arxiv.org/abs/1502.05767",
                summary="Modern autograd as the generalisation of backprop. Useful background for anyone who has only ever used PyTorch and wants to know what the framework actually does.",
                venue="JMLR",
            ),
        ],
        extras=[
            Extra(
                label="Wikipedia: Backpropagation",
                url="https://en.wikipedia.org/wiki/Backpropagation",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 9. 1989 — LeNet / CNNs
    # ----------------------------------------------------------------- #
    Chapter(
        id=9,
        slug="convolutional-networks-lenet",
        part=PART,
        title="Convolutional Networks (LeNet)",
        summary_html="""
<p>Yann LeCun's 1989 work at Bell Labs took backprop and added the right
inductive biases for images: <b>local receptive fields</b>, <b>weight
sharing</b>, and <b>spatial pooling</b>. The result — a convolutional neural
network, later christened LeNet — could read handwritten ZIP-code digits
straight from bitmaps with accuracy good enough for the US Postal Service to
deploy.</p>

<h4>Why convolution is the right prior for images</h4>
<ul>
  <li>Local pixels are correlated; distant pixels usually are not.</li>
  <li>A useful feature (an edge, a corner) at one location is useful at
  others — so share the weights across positions.</li>
  <li>Pooling provides translation tolerance: a "7" is a "7" whether it sits
  in the top-left or the centre of the image.</li>
</ul>

<p>These three choices cut parameters by orders of magnitude versus a fully
connected network of the same depth, which is what made training tractable
on 1989 hardware. The same three ideas reappear, in different clothes, in
every later vision model — including the patch-tokenisation step in Vision
Transformers.</p>

<h4>Why this paper</h4>
<p>The LeNet-1 paper is the first end-to-end deep-learning success story on a
real problem. It is also a clean illustration of how architecture is the
art of <i>baking the right invariances into the model</i> so that the
optimiser has less work to do. Decades later, the field would swing back
toward weaker priors plus more data (transformers), but LeCun's recipe
defined what "deep learning for vision" meant for 25 years.</p>
""",
        papers=[
            Paper(
                title="Backpropagation Applied to Handwritten Zip Code Recognition",
                authors="Yann LeCun et al.",
                year="1989",
                url="http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf",
                summary="The original LeNet-1 paper. Read it for the architecture, the weight-sharing argument, and a reminder of how much can be done with a few thousand training examples and a careful prior.",
                venue="Neural Computation",
            ),
            Paper(
                title="Gradient-Based Learning Applied to Document Recognition",
                authors="LeCun, Bottou, Bengio, Haffner",
                year="1998",
                url="http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf",
                summary="The mature LeNet-5 paper plus a wide-ranging survey of gradient-based learning. Often the easier read of the two.",
                venue="Proc. IEEE",
            ),
        ],
        extras=[
            Extra(
                label="LeCun's publications page",
                url="http://yann.lecun.com/exdb/publis/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 10. 1997 — LSTM
    # ----------------------------------------------------------------- #
    Chapter(
        id=10,
        slug="lstm",
        part=PART,
        title="LSTM: Recurrent Networks That Worked",
        summary_html="""
<p>Naive recurrent neural networks were known to be expressive but
untrainable on long sequences: gradients either vanished to zero or exploded.
Hochreiter and Schmidhuber's 1997 <b>Long Short-Term Memory</b> network
solved the vanishing-gradient problem with a clever architectural trick — a
linear cell state guarded by multiplicative <i>gates</i>.</p>

<h4>The gates</h4>
<ul>
  <li><b>Forget gate</b> — what to drop from the cell state.</li>
  <li><b>Input gate</b> — what new information to write.</li>
  <li><b>Output gate</b> — what part of the cell state to expose as the
  hidden state.</li>
</ul>

<pre>
c_t = f_t * c_{t-1} + i_t * tanh(W x_t + U h_{t-1})
h_t = o_t * tanh(c_t)
</pre>

<p>Because the cell-state update is additive (modulated by a sigmoid gate
near 1), the gradient can flow back through hundreds of timesteps without
collapsing. That single design choice made it possible to train RNNs on
real-world speech, handwriting, and language data.</p>

<h4>Why it matters historically</h4>
<p>From 1997 through about 2017, LSTM (and its cousin GRU) was the default
sequence model for everything that mattered in language: speech recognition,
machine translation, language modelling, handwriting generation, even early
captioning systems. Google Translate ran on stacked LSTMs in 2016. The
transformer eventually replaced it for high-end tasks because attention
parallelises across the sequence while LSTM is inherently serial — but the
intuitions about gating, residual paths, and additive updates carried over.
Modern state-space models (Mamba) are arguably an attempt to recover LSTM's
linear-time inference while keeping transformer-grade quality.</p>
""",
        papers=[
            Paper(
                title="Long Short-Term Memory",
                authors="Sepp Hochreiter, Jürgen Schmidhuber",
                year="1997",
                url="https://www.bioinf.jku.at/publications/older/2604.pdf",
                summary="The original LSTM paper. Dense but worth working through — the analysis of constant error carousels is the core of why the architecture works.",
                venue="Neural Computation",
            ),
            Paper(
                title="Sequence to Sequence Learning with Neural Networks",
                authors="Sutskever, Vinyals, Le",
                year="2014",
                url="https://arxiv.org/abs/1409.3215",
                summary="LSTM-based encoder-decoder for machine translation. The first credible neural alternative to phrase-based statistical MT.",
                venue="NeurIPS",
            ),
            Paper(
                title="Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling",
                authors="Chung, Gulcehre, Cho, Bengio",
                year="2014",
                url="https://arxiv.org/abs/1412.3555",
                summary="Compares LSTM against the simpler GRU. Useful for understanding which gates are doing real work.",
                venue="arXiv",
            ),
        ],
        extras=[
            Extra(
                label="Understanding LSTM Networks (colah's blog)",
                url="https://colah.github.io/posts/2015-08-Understanding-LSTMs/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 11. 2003 — Bengio NPLM
    # ----------------------------------------------------------------- #
    Chapter(
        id=11,
        slug="neural-language-models",
        part=PART,
        title="Neural Language Models (Bengio NPLM)",
        summary_html="""
<p>Up to 2003, language modelling was n-grams: count sequences, smooth, hope
the test set looks like the training set. Bengio, Ducharme, Vincent, and
Janvin proposed a different idea: <b>learn a continuous vector for every
word, and let a neural network predict the next word from the vectors of the
previous few</b>. This is the <i>neural probabilistic language model</i> —
NPLM — and it is the first chapter where the word "embedding" means what we
mean by it today.</p>

<h4>Architecture in one breath</h4>
<pre>
context: w_{t-n+1}, ..., w_{t-1}
e_i = C[w_i]                  # embedding lookup, shared across positions
h   = tanh(W [e_1; ...; e_{n-1}] + b)
p(w_t | context) = softmax(U h + d)
</pre>

<p>Two things happen during training. First, the network learns to predict
the next word — that is the loss. Second, and more importantly,
<i>similar words end up with similar vectors</i>, because the network has no
way to use a word other than through its embedding. Words that play similar
roles in similar contexts must therefore be encoded similarly. This is the
distributional hypothesis made concrete and learnable.</p>

<h4>Why it matters</h4>
<ul>
  <li>It killed the curse of dimensionality for n-grams: instead of needing
  to see every n-gram, the model generalises through embeddings.</li>
  <li>It introduced the input layer that every later language model still
  uses: an embedding matrix of shape (vocab, d_model).</li>
  <li>It connected language modelling to representation learning. Word2vec,
  GloVe, ELMo, and BERT are all in the same family tree.</li>
</ul>

<p>Read this paper before word2vec — it is older, denser, and the better
education.</p>
""",
        papers=[
            Paper(
                title="A Neural Probabilistic Language Model",
                authors="Yoshua Bengio, Réjean Ducharme, Pascal Vincent, Christian Janvin",
                year="2003",
                url="https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf",
                summary="The original NPLM paper. The maths is elementary; the conceptual move from discrete counts to learned vectors is the whole point.",
                venue="JMLR",
            ),
            Paper(
                title="A Scalable Hierarchical Distributed Language Model",
                authors="Mnih, Hinton",
                year="2008",
                url="https://www.cs.toronto.edu/~amnih/papers/hlbl_final.pdf",
                summary="Hierarchical softmax — a key trick for making NPLMs trainable at vocabularies above ~10k words. Sets up word2vec's later optimisations.",
                venue="NeurIPS",
            ),
        ],
        extras=[
            Extra(
                label="Wikipedia: Language model",
                url="https://en.wikipedia.org/wiki/Language_model",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 12. 2012 — AlexNet
    # ----------------------------------------------------------------- #
    Chapter(
        id=12,
        slug="alexnet-deep-learning-ignition",
        part=PART,
        title="AlexNet and the Deep Learning Ignition",
        summary_html="""
<p>The 2012 ImageNet result is the moment deep learning stopped being a
niche academic interest and became the dominant paradigm in AI. Krizhevsky,
Sutskever, and Hinton's <b>AlexNet</b> halved the previous best error rate
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
spent following the curve: deeper networks (VGG, GoogLeNet, ResNet), better
optimisers, better regularisation.</p>

<h4>The lesson the field learned</h4>
<p>Compute and data, applied to a model with the right inductive biases,
beats decades of hand-engineered features. This is the same lesson that
GPT-3 will hammer home eight years later in language. AlexNet is where the
"bitter lesson" first hit the mainstream.</p>
""",
        papers=[
            Paper(
                title="ImageNet Classification with Deep Convolutional Neural Networks",
                authors="Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton",
                year="2012",
                url="https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html",
                summary="The AlexNet paper. Worth reading both for the architecture and for the engineering — the GPU implementation notes are the part most modern readers skip and shouldn't.",
                venue="NeurIPS",
            ),
            Paper(
                title="Very Deep Convolutional Networks for Large-Scale Image Recognition (VGG)",
                authors="Simonyan, Zisserman",
                year="2014",
                url="https://arxiv.org/abs/1409.1556",
                summary="Showed that uniform stacks of 3x3 convolutions could go much deeper, given enough compute.",
                venue="ICLR",
            ),
            Paper(
                title="Going Deeper with Convolutions (GoogLeNet / Inception)",
                authors="Szegedy et al.",
                year="2014",
                url="https://arxiv.org/abs/1409.4842",
                summary="Inception modules and the first serious attempt to think about parameter efficiency in deep CNNs.",
                venue="CVPR",
            ),
        ],
        extras=[
            Extra(
                label="ImageNet Large Scale Visual Recognition Challenge",
                url="https://arxiv.org/abs/1409.0575",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 13. 2013 — Word embeddings
    # ----------------------------------------------------------------- #
    Chapter(
        id=13,
        slug="word-embeddings",
        part=PART,
        title="Word Embeddings: word2vec and GloVe",
        summary_html="""
<p>Bengio's NPLM gave us the idea of word embeddings. The 2013-14 trio of
<b>word2vec</b>, <b>GloVe</b>, and the surrounding tooling made embeddings
fast, scalable, and shockingly useful. For about three years, downloading
pretrained word vectors was the entire "transfer learning" story in NLP.</p>

<h4>word2vec — Mikolov et al., 2013</h4>
<ul>
  <li><b>Skip-gram</b>: given a centre word, predict its neighbours.</li>
  <li><b>CBOW</b>: given the neighbours, predict the centre word.</li>
  <li><b>Negative sampling</b>: replace the full softmax with a binary
  classifier that distinguishes real (word, context) pairs from random
  noise. This is the trick that made training 100B-token corpora
  feasible on a single machine.</li>
</ul>

<h4>GloVe — Pennington, Socher, Manning, 2014</h4>
<p>GloVe instead factorises the global word-word co-occurrence matrix
directly, with a weighted least-squares objective. It often produced
slightly better vectors than word2vec on analogy tasks and made the
mathematical link to classical distributional semantics explicit.</p>

<h4>Why it caught fire</h4>
<p>The embeddings turned out to encode startling amounts of structure:
<code>king - man + woman ≈ queen</code> became the canonical demo. More
practically, every NLP system that previously used one-hot word features
could now be initialised with 300-dim vectors trained on Wikipedia or
Common Crawl and immediately do better. This was the first taste of
"pretrain on a generic corpus, fine-tune on your task" — the playbook that
BERT and GPT would later industrialise.</p>

<p>Limitations were obvious: a single vector per word cannot disambiguate
"bank" the financial institution from "bank" the river edge. ELMo (2018)
fixed that with contextual embeddings, and BERT (2018) fixed it harder. But
word2vec is still the cleanest pedagogical entry point to representation
learning in NLP.</p>
""",
        papers=[
            Paper(
                title="Efficient Estimation of Word Representations in Vector Space",
                authors="Mikolov, Chen, Corrado, Dean",
                year="2013",
                url="https://arxiv.org/abs/1301.3781",
                summary="The word2vec paper. CBOW and skip-gram architectures, plus the analogy-task evaluation that made the work famous.",
                venue="ICLR Workshop",
            ),
            Paper(
                title="Distributed Representations of Words and Phrases and their Compositionality",
                authors="Mikolov, Sutskever, Chen, Corrado, Dean",
                year="2013",
                url="https://arxiv.org/abs/1310.4546",
                summary="The follow-up that introduces negative sampling and subsampling of frequent words. This is the version most implementations actually use.",
                venue="NeurIPS",
            ),
            Paper(
                title="GloVe: Global Vectors for Word Representation",
                authors="Pennington, Socher, Manning",
                year="2014",
                url="https://nlp.stanford.edu/pubs/glove.pdf",
                summary="Matrix-factorisation alternative. The introduction is one of the clearest explanations in NLP of what an embedding is and what it should encode.",
                venue="EMNLP",
            ),
        ],
        extras=[
            Extra(
                label="The amazing power of word vectors (Adrian Colyer)",
                url="https://blog.acolyer.org/2016/04/21/the-amazing-power-of-word-vectors/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 14. 2014 — Seq2seq + attention
    # ----------------------------------------------------------------- #
    Chapter(
        id=14,
        slug="seq2seq-and-attention",
        part=PART,
        title="Seq2seq and Attention",
        summary_html="""
<p>2014 produced two papers that, in retrospect, drew the blueprint for
every modern language model. Sutskever, Vinyals, and Le's <b>seq2seq</b>
paper showed that an LSTM encoder could compress an entire input sentence
into a single vector, and a second LSTM decoder could generate the
translated output from that vector — end-to-end neural machine translation.
Bahdanau, Cho, and Bengio's <b>attention</b> paper, published almost
simultaneously, fixed the obvious bottleneck.</p>

<h4>Why a single vector wasn't enough</h4>
<p>Compressing a 30-word sentence into one fixed-size vector loses
information; long sentences degraded fast. Bahdanau et al.'s solution: at
each decoding step, let the decoder <i>look back</i> at all encoder hidden
states and form a weighted sum determined by a small alignment network.
This is attention. The alignment weights even produced interpretable
soft word-by-word translations as a free side effect.</p>

<pre>
alpha_{ij} = softmax_j( a(s_{i-1}, h_j) )
c_i        = sum_j alpha_{ij} h_j
</pre>

<h4>What this set up</h4>
<ul>
  <li><b>Encoder-decoder</b> as the default frame for any input-to-output
  sequence task: translation, summarisation, dialogue.</li>
  <li><b>Attention</b> as a content-based routing mechanism. Three years
  later the Transformer would drop the recurrence entirely and keep only
  the attention.</li>
  <li><b>Soft alignments</b> as a debugging tool — you could finally see
  what the model was looking at.</li>
</ul>

<p>If you read only one pair of papers in this chapter, read these two
together. They are the immediate prehistory of the Transformer; everything
after 2017 is a refinement of the question they asked.</p>
""",
        papers=[
            Paper(
                title="Sequence to Sequence Learning with Neural Networks",
                authors="Ilya Sutskever, Oriol Vinyals, Quoc Le",
                year="2014",
                url="https://arxiv.org/abs/1409.3215",
                summary="The seq2seq paper. LSTM encoder + LSTM decoder. The trick of reversing the source sentence to ease optimisation is one of those small details that mattered a lot at the time.",
                venue="NeurIPS",
            ),
            Paper(
                title="Neural Machine Translation by Jointly Learning to Align and Translate",
                authors="Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio",
                year="2014",
                url="https://arxiv.org/abs/1409.0473",
                summary="The attention paper. Read it once for the mechanism and once for the alignment visualisations — they are where the field's intuition for attention was forged.",
                venue="ICLR",
            ),
            Paper(
                title="Effective Approaches to Attention-based Neural Machine Translation",
                authors="Luong, Pham, Manning",
                year="2015",
                url="https://arxiv.org/abs/1508.04025",
                summary="Cleaner formalisation of dot-product vs. additive attention. The dot-product variant is the one that survives into the Transformer.",
                venue="EMNLP",
            ),
        ],
        extras=[
            Extra(
                label="Visualizing A Neural Machine Translation Model (Alammar)",
                url="https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 15. 2014 — GANs
    # ----------------------------------------------------------------- #
    Chapter(
        id=15,
        slug="generative-adversarial-networks",
        part=PART,
        title="Generative Adversarial Networks",
        summary_html="""
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
unstable — and most of the next five years of GAN research was spent
stabilising them (DCGAN, WGAN, spectral norm, progressive growing,
StyleGAN).</p>

<h4>Why it mattered, even though diffusion eventually won</h4>
<ul>
  <li>It made photorealistic image synthesis a real research target. Pre-2014
  generative-model samples mostly looked like blurry MNIST.</li>
  <li>It introduced <i>adversarial</i> as a fundamental training paradigm —
  later reused for representation learning, domain adaptation, robustness,
  and even RLHF (the reward model is, loosely, a discriminator).</li>
  <li>It taught the field to be comfortable with implicit generative models
  whose density is not tractable. Diffusion (chapter 21) and
  flow-matching are the same family.</li>
</ul>

<p>By 2022, diffusion models had taken over high-end image generation and
GANs had largely been retired from frontier work. But for almost a decade
GANs were how you got a realistic image out of a neural network, and the
adversarial training idea is permanently embedded in the toolbox.</p>
""",
        papers=[
            Paper(
                title="Generative Adversarial Networks",
                authors="Ian Goodfellow et al.",
                year="2014",
                url="https://arxiv.org/abs/1406.2661",
                summary="The original GAN paper. Short, dense, and beautifully written. Read it once for the minimax formulation and once for the proof sketch that the optimum recovers p_data.",
                venue="NeurIPS",
            ),
            Paper(
                title="Unsupervised Representation Learning with Deep Convolutional GANs (DCGAN)",
                authors="Radford, Metz, Chintala",
                year="2015",
                url="https://arxiv.org/abs/1511.06434",
                summary="The architectural recipe (strided convolutions, batchnorm, no fully-connected layers) that made GANs trainable in practice.",
                venue="ICLR",
            ),
            Paper(
                title="Wasserstein GAN",
                authors="Arjovsky, Chintala, Bottou",
                year="2017",
                url="https://arxiv.org/abs/1701.07875",
                summary="Reframed GAN training as Wasserstein distance minimisation. Removed many of the mode-collapse and gradient pathologies of vanilla GANs.",
                venue="ICML",
            ),
        ],
        extras=[
            Extra(
                label="NIPS 2016 Tutorial: Generative Adversarial Networks",
                url="https://arxiv.org/abs/1701.00160",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 16. 2015 — ResNet + BatchNorm
    # ----------------------------------------------------------------- #
    Chapter(
        id=16,
        slug="resnet-and-batchnorm",
        part=PART,
        title="ResNet and Batch Normalization",
        summary_html="""
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

<h4>ResNet (He, Zhang, Ren, Sun, 2015)</h4>
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
""",
        papers=[
            Paper(
                title="Deep Residual Learning for Image Recognition",
                authors="Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun",
                year="2015",
                url="https://arxiv.org/abs/1512.03385",
                summary="The ResNet paper. The plot of training error vs depth, with and without residuals, is one of the most influential figures in deep learning.",
                venue="CVPR",
            ),
            Paper(
                title="Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift",
                authors="Sergey Ioffe, Christian Szegedy",
                year="2015",
                url="https://arxiv.org/abs/1502.03167",
                summary="The BatchNorm paper. The 'internal covariate shift' framing has been challenged by later work, but the method is universal.",
                venue="ICML",
            ),
            Paper(
                title="Layer Normalization",
                authors="Ba, Kiros, Hinton",
                year="2016",
                url="https://arxiv.org/abs/1607.06450",
                summary="The variant that works for recurrent and transformer models, where mini-batch statistics aren't a clean signal.",
                venue="arXiv",
            ),
        ],
        extras=[
            Extra(
                label="Identity Mappings in Deep Residual Networks",
                url="https://arxiv.org/abs/1603.05027",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 17. 2017 — Transformer
    # ----------------------------------------------------------------- #
    Chapter(
        id=17,
        slug="the-transformer",
        part=PART,
        title="The Transformer",
        summary_html="""
<p>"Attention Is All You Need" (Vaswani et al., 2017) is the architectural
hinge of this entire book. It removes recurrence and convolution from
sequence modelling and keeps only attention, normalised, residualised, and
stacked.</p>

<h4>The three ingredients</h4>
<ul>
  <li><b>Scaled dot-product attention</b> — the core mechanism, with the
  <code>1/sqrt(d_k)</code> scale that keeps softmax gradients well-behaved.</li>
  <li><b>Multi-head attention</b> — run several attention layers in parallel
  with different learned projections, then concatenate. Different heads end
  up specialising on different relations.</li>
  <li><b>Positional encodings</b> — sinusoidal or learned, because pure
  attention is permutation-invariant and language is not.</li>
</ul>

<pre>
Attention(Q, K, V) = softmax( Q K^T / sqrt(d_k) ) V
</pre>

<h4>Why it took over</h4>
<p>Compared to LSTM:</p>
<ul>
  <li><b>Constant path length</b> between any two tokens. RNNs need O(n)
  steps for information to flow; attention needs one.</li>
  <li><b>Parallel training</b>. Every position can be computed
  simultaneously on a GPU. This unlocked training at scales LSTMs simply
  could not reach.</li>
  <li><b>Mild inductive bias</b>. Less wired-in structure means the model
  improves smoothly as you scale data and parameters — exactly the
  property scaling laws (chapter 20) would later quantify.</li>
</ul>

<p>The original Transformer was an encoder-decoder for translation. The
field quickly forked into encoder-only (BERT, chapter 18), decoder-only
(GPT, chapter 19), and the original encoder-decoder (T5, BART). All
modern frontier LMs are decoder-only Transformers; almost every modern
embedding model is an encoder-only one. The architecture has been refined
heavily — RoPE, FlashAttention, grouped-query attention, MoE — but the
2017 skeleton is still recognisable.</p>
""",
        papers=[
            Paper(
                title="Attention Is All You Need",
                authors="Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, Polosukhin",
                year="2017",
                url="https://arxiv.org/abs/1706.03762",
                summary="The Transformer paper. Self-attention, multi-head attention, sinusoidal positional encodings. The most-cited ML paper of the late 2010s.",
                venue="NeurIPS",
            ),
            Paper(
                title="Layer Normalization",
                authors="Ba, Kiros, Hinton",
                year="2016",
                url="https://arxiv.org/abs/1607.06450",
                summary="LayerNorm — the normalization that made deep transformers trainable in the first place.",
                venue="arXiv",
            ),
        ],
        extras=[
            Extra(
                label="The Illustrated Transformer (Jay Alammar)",
                url="https://jalammar.github.io/illustrated-transformer/",
            ),
            Extra(
                label="The Annotated Transformer (Harvard NLP)",
                url="http://nlp.seas.harvard.edu/annotated-transformer/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 18. 2018 — BERT
    # ----------------------------------------------------------------- #
    Chapter(
        id=18,
        slug="bert-encoder-era",
        part=PART,
        title="BERT and the Encoder Era",
        summary_html="""
<p><b>BERT</b> (Devlin, Chang, Lee, Toutanova, 2018) was the first model
to make "pretrain a giant Transformer encoder, fine-tune it on whatever you
want" the default NLP recipe. For the next two years, every leaderboard in
text classification, NER, QA, and natural-language inference was topped by
some descendant of BERT.</p>

<h4>The training objective</h4>
<ul>
  <li><b>Masked Language Modelling (MLM)</b>: randomly mask 15% of the
  input tokens and train the model to predict them from the surrounding
  context. Because attention is bidirectional, the model can use both
  left and right context — unlike GPT's left-to-right model.</li>
  <li><b>Next Sentence Prediction (NSP)</b>: was the second objective in
  the original paper. Later work (RoBERTa) showed it doesn't help, and
  it has largely been dropped.</li>
</ul>

<h4>The transfer-learning recipe</h4>
<pre>
1. Pretrain on Wikipedia + BookCorpus  (3.3B words)
2. Fine-tune on your target task        (a few thousand labels)
3. Win the leaderboard
</pre>

<p>BERT-Base had 110M parameters; BERT-Large had 340M. By today's
standards, that is small. The shock at the time was that this single
pretrained checkpoint, with task-specific heads bolted on, beat
heavily engineered task-specific systems on 11 different NLP benchmarks.</p>

<h4>Legacy</h4>
<ul>
  <li>The encoder lineage — RoBERTa, ALBERT, ELECTRA, DeBERTa — drove a
  generation of practical NLP. Modern embedding and reranker models are
  fine-tuned BERT-family encoders.</li>
  <li>BERT introduced the [CLS] token, sub-word WordPiece tokenisation,
  and the convention that "fine-tune the whole network end-to-end" is
  the default, not feature extraction.</li>
  <li>It also marked the moment the field accepted that decoder-only
  generative models and encoder-only representation models would
  diverge for a while. GPT-3 would later collapse some of that
  distinction, but in 2018 the split was clean.</li>
</ul>
""",
        papers=[
            Paper(
                title="BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
                authors="Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova",
                year="2018",
                url="https://arxiv.org/abs/1810.04805",
                summary="The BERT paper. MLM + NSP, fine-tuning recipe, benchmark sweep. The point of departure for the encoder-only family.",
                venue="NAACL",
            ),
            Paper(
                title="RoBERTa: A Robustly Optimized BERT Pretraining Approach",
                authors="Liu et al.",
                year="2019",
                url="https://arxiv.org/abs/1907.11692",
                summary="Showed that BERT was significantly undertrained. Drop NSP, train longer with bigger batches and more data.",
                venue="arXiv",
            ),
            Paper(
                title="ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators",
                authors="Clark, Luong, Le, Manning",
                year="2020",
                url="https://arxiv.org/abs/2003.10555",
                summary="Replaces MLM with a more sample-efficient discriminative objective. Often the first thing to try if compute is tight.",
                venue="ICLR",
            ),
        ],
        extras=[
            Extra(
                label="The Illustrated BERT (Jay Alammar)",
                url="https://jalammar.github.io/illustrated-bert/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 19. 2019 — GPT-2
    # ----------------------------------------------------------------- #
    Chapter(
        id=19,
        slug="gpt-2-decoder-only",
        part=PART,
        title="GPT-2 and the Decoder-only Paradigm",
        summary_html="""
<p>OpenAI's <b>GPT-2</b> (Radford et al., 2019) was a 1.5B-parameter
decoder-only Transformer trained to predict the next token on 40GB of web
text. The paper's title — <i>Language Models are Unsupervised Multitask
Learners</i> — captures the thesis. With enough scale and data, a single
next-token-prediction objective produces a model that can do translation,
question answering, summarisation, and arithmetic with no task-specific
training, just the right prompt.</p>

<h4>What was new in 2019</h4>
<ul>
  <li><b>Decoder-only</b>: a stack of causal-masked self-attention layers.
  Simpler than encoder-decoder, and the same architecture handles input
  and output uniformly.</li>
  <li><b>Zero-shot task transfer</b>: format the task as a text completion,
  feed it to the model, read off the answer. No fine-tuning, no labelled
  data per task.</li>
  <li><b>Scale as a research direction</b>. The paper trained four
  models at 117M / 345M / 762M / 1.5B parameters and showed monotonic
  improvement on every metric. This was the empirical hint that became
  the scaling laws (chapter 20).</li>
</ul>

<h4>The release controversy</h4>
<p>OpenAI initially withheld the largest GPT-2 weights citing misuse risk
— novel for ML at the time, and a foretaste of every model-release debate
since. They published the smaller checkpoints first and the full model
nine months later.</p>

<h4>Why this is the chapter where modern LMs really start</h4>
<p>BERT showed pretraining works. GPT-2 showed that a <i>single
generative</i> pretrained model is, in principle, a multi-task system.
Every chatbot, code assistant, and agent in the rest of the book sits on
this architectural choice. The decoder-only Transformer trained with
next-token prediction on web-scale text is now <i>the</i> default
substrate for AI.</p>
""",
        papers=[
            Paper(
                title="Language Models are Unsupervised Multitask Learners",
                authors="Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever",
                year="2019",
                url="https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf",
                summary="The GPT-2 paper. Read for the architecture, the scaling curves, and the zero-shot results. The release-policy section is also a good piece of AI-policy history.",
                venue="OpenAI tech report",
            ),
            Paper(
                title="Improving Language Understanding by Generative Pre-Training (GPT-1)",
                authors="Radford, Narasimhan, Salimans, Sutskever",
                year="2018",
                url="https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf",
                summary="The earlier and shorter precursor. Pretrain a Transformer LM, then fine-tune. Useful to read just to see how unimpressive the result was relative to BERT a few months later — and how fast that changed.",
                venue="OpenAI tech report",
            ),
        ],
        extras=[
            Extra(
                label="The Illustrated GPT-2 (Jay Alammar)",
                url="https://jalammar.github.io/illustrated-gpt2/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 20. 2020 — GPT-3, scaling laws, ICL
    # ----------------------------------------------------------------- #
    Chapter(
        id=20,
        slug="gpt-3-scaling-laws-icl",
        part=PART,
        title="GPT-3, Scaling Laws, and In-Context Learning",
        summary_html="""
<p>Two papers in 2020 made the modern frontier LM era inevitable. Kaplan et
al.'s <b>scaling laws</b> showed that loss is a smooth power-law function
of compute, model size, and data. Brown et al.'s <b>GPT-3</b> paper
operationalised that prediction at 175B parameters and demonstrated a new
phenomenon: <b>in-context learning</b>.</p>

<h4>Scaling laws</h4>
<pre>
L(N) ≈ (N_c / N)^alpha     # loss as a function of parameters N
L(D) ≈ (D_c / D)^alpha_D   # and as a function of data D
</pre>
<p>For Transformer LMs trained on web text, loss scales smoothly and
predictably as you increase parameters or data — for many orders of
magnitude. There are no obvious diminishing returns until you blow past
the optimum data-to-parameters ratio. This single empirical curve is what
turned "let's scale up" from a guess into a plan.</p>

<h4>GPT-3 and in-context learning</h4>
<ul>
  <li>175B parameters, ~300B training tokens.</li>
  <li><b>Few-shot prompting</b>: provide a handful of input/output examples
  in the prompt, then a new input; the model completes the pattern. No
  gradient updates; no fine-tuning.</li>
  <li>The capability emerged smoothly with scale on some tasks and
  apparently abruptly on others. The "emergent abilities" debate
  (Wei et al. 2022, Schaeffer et al. 2023) traces back to GPT-3's
  task plots.</li>
</ul>

<h4>Why this chapter is the inflection point</h4>
<p>Before GPT-3, NLP was dozens of fine-tuned models on dozens of
datasets. After GPT-3, the entire field reorganised around a single
generic LM you prompt. The "Chinchilla" paper (Hoffmann et al., 2022)
later corrected the scaling laws — for a fixed compute budget, you should
spend more on data and less on parameters than Kaplan recommended — but
the basic "compute predicts loss" framework is intact and is now how every
serious lab plans training runs.</p>
""",
        papers=[
            Paper(
                title="Scaling Laws for Neural Language Models",
                authors="Jared Kaplan, Sam McCandlish et al.",
                year="2020",
                url="https://arxiv.org/abs/2001.08361",
                summary="The empirical paper. Loss as a power law in N, D, and C. The plots are the most important figures of the decade in language modelling.",
                venue="arXiv",
            ),
            Paper(
                title="Language Models are Few-Shot Learners (GPT-3)",
                authors="Tom Brown et al.",
                year="2020",
                url="https://arxiv.org/abs/2005.14165",
                summary="The GPT-3 paper. The few-shot evaluation methodology is as influential as the model itself.",
                venue="NeurIPS",
            ),
            Paper(
                title="Training Compute-Optimal Large Language Models (Chinchilla)",
                authors="Hoffmann et al.",
                year="2022",
                url="https://arxiv.org/abs/2203.15556",
                summary="DeepMind's correction: at any compute budget, optimal training spends roughly equal effort on parameters and tokens, which means most models prior to 2022 were undertrained.",
                venue="NeurIPS",
            ),
        ],
        extras=[
            Extra(
                label="How GPT-3 Works (Jay Alammar)",
                url="https://jalammar.github.io/how-gpt3-works-visualizations-animations/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 21. 2020 — DDPM
    # ----------------------------------------------------------------- #
    Chapter(
        id=21,
        slug="diffusion-models",
        part=PART,
        title="Diffusion Models (DDPM)",
        summary_html="""
<p>Ho, Jain, and Abbeel's 2020 <b>Denoising Diffusion Probabilistic
Models</b> paper turned a 2015 thermodynamics-flavoured idea into a
practical generative model that, within two years, had taken over image
synthesis. By 2022, Stable Diffusion, DALL·E 2, and Imagen — all diffusion
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
""",
        papers=[
            Paper(
                title="Denoising Diffusion Probabilistic Models",
                authors="Jonathan Ho, Ajay Jain, Pieter Abbeel",
                year="2020",
                url="https://arxiv.org/abs/2006.11239",
                summary="The DDPM paper. Reframes diffusion as variational denoising and gives the simple MSE training objective that everything later builds on.",
                venue="NeurIPS",
            ),
            Paper(
                title="High-Resolution Image Synthesis with Latent Diffusion Models",
                authors="Rombach, Blattmann, Lorenz, Esser, Ommer",
                year="2022",
                url="https://arxiv.org/abs/2112.10752",
                summary="Latent diffusion / Stable Diffusion. Run the diffusion process in a compressed latent space for orders-of-magnitude speedup. The basis of most open-source image generators.",
                venue="CVPR",
            ),
            Paper(
                title="Classifier-Free Diffusion Guidance",
                authors="Ho, Salimans",
                year="2022",
                url="https://arxiv.org/abs/2207.12598",
                summary="The trick that lets a single conditional/unconditional model trade off fidelity and diversity at sample time. Universally used in text-to-image.",
                venue="arXiv",
            ),
        ],
        extras=[
            Extra(
                label="What are Diffusion Models? (Lilian Weng)",
                url="https://lilianweng.github.io/posts/2021-07-11-diffusion-models/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 22. 2021 — CLIP
    # ----------------------------------------------------------------- #
    Chapter(
        id=22,
        slug="clip-multimodal-contrastive",
        part=PART,
        title="CLIP and Multimodal Contrastive Learning",
        summary_html="""
<p>OpenAI's <b>CLIP</b> (Radford et al., 2021) — Contrastive
Language-Image Pretraining — trained an image encoder and a text encoder
jointly so that matching (image, caption) pairs end up nearby in a shared
embedding space, and mismatched pairs end up far apart. The training data
was 400M image-text pairs scraped from the web. The result is a single
embedding space that spans both modalities.</p>

<h4>The contrastive objective</h4>
<pre>
sim(I, T) = (image_emb . text_emb) / (||image_emb|| ||text_emb||)

For a batch of N pairs, the loss treats it as 2N classification problems:
each image picks its caption out of N captions, each caption picks its image.
</pre>

<h4>Why this was a big deal</h4>
<ul>
  <li><b>Zero-shot image classification</b>: to classify an image, embed
  the image and embed candidate class names as text ("a photo of a
  cat"); pick the highest similarity. CLIP matched fully supervised
  ResNet-50 on ImageNet without seeing a single ImageNet label.</li>
  <li><b>Distribution robustness</b>: CLIP's accuracy on ImageNet-Sketch,
  ImageNet-A, and ObjectNet was far higher than supervised models. The
  language signal acts as a regulariser that suppresses spurious
  visual shortcuts.</li>
  <li><b>A multimodal substrate</b>: text-conditioned diffusion (Stable
  Diffusion, DALL·E 2) uses CLIP-style text encoders to translate
  prompts into the diffusion model's conditioning signal. Vision-language
  models (LLaVA, etc.) project CLIP image features into an LLM's token
  space.</li>
</ul>

<p>Contrastive learning itself was not new — SimCLR and MoCo had pushed
self-supervised image representations the year before. CLIP's contribution
was to use <i>natural-language supervision</i> at scale and show that the
resulting embeddings were both more general and more robust than
single-modality alternatives.</p>
""",
        papers=[
            Paper(
                title="Learning Transferable Visual Models From Natural Language Supervision (CLIP)",
                authors="Alec Radford et al.",
                year="2021",
                url="https://arxiv.org/abs/2103.00020",
                summary="The CLIP paper. The zero-shot transfer experiments are the headline; the analysis of distribution shift is the under-appreciated section.",
                venue="ICML",
            ),
            Paper(
                title="A Simple Framework for Contrastive Learning of Visual Representations (SimCLR)",
                authors="Chen, Kornblith, Norouzi, Hinton",
                year="2020",
                url="https://arxiv.org/abs/2002.05709",
                summary="Single-modality self-supervised contrastive learning on images. Useful background for what CLIP added with the text side.",
                venue="ICML",
            ),
            Paper(
                title="Visual Instruction Tuning (LLaVA)",
                authors="Liu, Li, Wu, Lee",
                year="2023",
                url="https://arxiv.org/abs/2304.08485",
                summary="Bolts a CLIP image encoder onto an LLM through a small projection layer and instruction-tunes the result. The simplest recipe for turning an LLM into a vision-language model.",
                venue="NeurIPS",
            ),
        ],
        extras=[
            Extra(
                label="OpenAI CLIP blog post",
                url="https://openai.com/index/clip/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 23. 2022 — InstructGPT / RLHF / ChatGPT
    # ----------------------------------------------------------------- #
    Chapter(
        id=23,
        slug="instructgpt-rlhf-chatgpt",
        part=PART,
        title="InstructGPT, RLHF, and ChatGPT",
        summary_html="""
<p>GPT-3 was capable but unhelpful. It would happily complete a prompt in
the most likely way according to its training distribution — which is not
the same as doing what the user asked. <b>InstructGPT</b> (Ouyang et al.,
2022) introduced the three-stage recipe that turned raw LMs into
assistants and led directly to <b>ChatGPT</b> in November 2022.</p>

<h4>The three stages</h4>
<ol>
  <li><b>Supervised fine-tuning (SFT)</b> on a small set of
  human-written demonstrations of the desired behaviour.</li>
  <li><b>Reward model (RM) training</b>. Show humans pairs of model
  outputs for the same prompt; have them pick the better one. Train a
  separate Transformer to score outputs the way humans do.</li>
  <li><b>Reinforcement Learning from Human Feedback (RLHF)</b>.
  Optimise the SFT model with PPO against the RM, with a KL penalty
  back to the SFT model so it doesn't drift into degenerate text.</li>
</ol>

<h4>Why this mattered more than the model size</h4>
<p>InstructGPT's 1.3B-parameter version was preferred to GPT-3 175B by
human raters on the OpenAI prompt distribution. Alignment to user intent
turned out to be at least as important as raw scale. ChatGPT, released
seven months later, was essentially "InstructGPT with a better base model
and a chat UI" and famously hit 100M users in two months.</p>

<h4>Successors</h4>
<ul>
  <li><b>Constitutional AI</b> (Anthropic) replaced human preference
  labels with AI-generated critiques against a written set of rules.</li>
  <li><b>DPO / IPO / KTO</b> reframe preference optimisation without RL,
  using simpler classification-style losses on preference pairs. They
  are the default in 2024-25 because they are easier to tune.</li>
  <li>RLHF / RLAIF still wins for the trickiest behaviour-shaping problems
  and is now used in combination with verifiable-reward RL on math/code
  (chapter 30).</li>
</ul>
""",
        papers=[
            Paper(
                title="Training language models to follow instructions with human feedback (InstructGPT)",
                authors="Long Ouyang et al.",
                year="2022",
                url="https://arxiv.org/abs/2203.02155",
                summary="The InstructGPT paper. The three-stage SFT → RM → RLHF recipe; the headline finding that a 1.3B aligned model beats a 175B unaligned model on human preference.",
                venue="NeurIPS",
            ),
            Paper(
                title="Constitutional AI: Harmlessness from AI Feedback",
                authors="Bai et al. (Anthropic)",
                year="2022",
                url="https://arxiv.org/abs/2212.08073",
                summary="Replaces a portion of the human-feedback loop with a written constitution and AI-generated critiques. Cheaper and arguably more transparent.",
                venue="arXiv",
            ),
            Paper(
                title="Direct Preference Optimization: Your Language Model is Secretly a Reward Model",
                authors="Rafailov, Sharma, Mitchell, Manning, Ermon, Finn",
                year="2023",
                url="https://arxiv.org/abs/2305.18290",
                summary="DPO. Eliminates the explicit reward model and the RL step; trains directly on preference pairs with a closed-form classification loss.",
                venue="NeurIPS",
            ),
        ],
        extras=[
            Extra(
                label="OpenAI: Introducing ChatGPT",
                url="https://openai.com/index/chatgpt/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 24. 2022 — Chain-of-thought
    # ----------------------------------------------------------------- #
    Chapter(
        id=24,
        slug="chain-of-thought-prompting",
        part=PART,
        title="Chain-of-Thought Prompting",
        summary_html="""
<p>Wei et al.'s 2022 <b>chain-of-thought (CoT)</b> paper made one of those
findings that seems obvious in retrospect: if you prompt a sufficiently
large language model with worked examples that show their reasoning step
by step, the model will produce its own step-by-step reasoning on new
problems — and its accuracy on math, commonsense, and symbolic reasoning
benchmarks goes up sharply.</p>

<h4>The prompt</h4>
<pre>
Q: Roger has 5 tennis balls. He buys 2 cans, each with 3 balls. How many now?
A: Roger started with 5. 2 cans of 3 is 6. 5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. They used 20, then bought 6. How many?
A: ...
</pre>

<h4>Two key empirical findings</h4>
<ul>
  <li><b>Emergence with scale</b>: CoT only helps once the underlying model
  is large enough (roughly &gt; 60B parameters in the original paper).
  Smaller models hallucinate plausible-looking reasoning that is
  arithmetically wrong.</li>
  <li><b>Zero-shot CoT</b> (Kojima et al., 2022): you don't even need
  exemplars — appending "Let's think step by step." to the prompt is
  often enough. Cheap, model-agnostic, surprisingly effective.</li>
</ul>

<h4>Why this is its own chapter</h4>
<p>CoT decouples reasoning quality from raw single-pass accuracy. With it,
the same model can be prompted into producing far better answers on
multi-step problems by spending more tokens on intermediate work. That
single observation is the seed of:</p>
<ul>
  <li><b>Self-consistency</b> (Wang et al.): sample multiple CoTs and
  majority-vote the final answer.</li>
  <li><b>Tree-of-thoughts</b>: search over reasoning paths.</li>
  <li><b>Inference-time reasoning models</b> (chapter 30): bake CoT into
  the model with RL on verifiable rewards.</li>
</ul>

<p>It is also the moment the field accepted that <i>compute at inference
time</i> is a real axis to scale on, not just compute at training time.</p>
""",
        papers=[
            Paper(
                title="Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
                authors="Jason Wei et al.",
                year="2022",
                url="https://arxiv.org/abs/2201.11903",
                summary="The CoT paper. Few-shot exemplars with explicit reasoning steps; sharp gains on GSM8K and similar benchmarks at sufficient model scale.",
                venue="NeurIPS",
            ),
            Paper(
                title="Large Language Models are Zero-Shot Reasoners",
                authors="Kojima, Gu, Reid, Matsuo, Iwasawa",
                year="2022",
                url="https://arxiv.org/abs/2205.11916",
                summary="Zero-shot CoT — 'Let's think step by step' as a universal prompt. Two-line change, large gains.",
                venue="NeurIPS",
            ),
            Paper(
                title="Self-Consistency Improves Chain of Thought Reasoning in Language Models",
                authors="Wang et al.",
                year="2022",
                url="https://arxiv.org/abs/2203.11171",
                summary="Sample many CoTs and majority-vote the final answer. The simplest and still one of the most reliable inference-time tricks.",
                venue="ICLR",
            ),
        ],
        extras=[],
    ),

    # ----------------------------------------------------------------- #
    # 25. 2022 — RAG
    # ----------------------------------------------------------------- #
    Chapter(
        id=25,
        slug="retrieval-augmented-generation",
        part=PART,
        title="Retrieval-Augmented Generation",
        summary_html="""
<p>Parametric memory — facts stored in the weights — is expensive to
update and easy to misremember. <b>Retrieval-augmented generation
(RAG)</b>, introduced by Lewis et al. in 2020 and operationalised
everywhere by 2022, splits the system into two parts: a frozen LM that
generates fluent text and an external <i>retriever</i> that fetches
relevant documents from a knowledge corpus at query time.</p>

<h4>The architecture</h4>
<pre>
question -&gt; retriever (DPR / BM25 / dense embeddings) -&gt; top-k docs
docs + question -&gt; LM -&gt; grounded answer
</pre>

<ul>
  <li>Retriever: encode every passage in your corpus once, store in a
  vector index (FAISS, HNSW, modern vector DBs). At query time, encode
  the question and pull the nearest neighbours.</li>
  <li>Generator: a standard seq2seq or decoder-only LM, conditioned on
  the question plus retrieved passages.</li>
  <li>Both can be trained jointly (Lewis 2020) or assembled from
  pretrained components without extra training (the 2023-onward norm).</li>
</ul>

<h4>Why this is the right answer to a real problem</h4>
<ul>
  <li><b>Freshness</b>: the corpus can be updated continuously without
  retraining the LM.</li>
  <li><b>Citability</b>: the system can show its sources, which matters
  for enterprise and search use cases.</li>
  <li><b>Hallucination reduction</b>: grounding the prompt in retrieved
  text shifts the conditional distribution toward facts, though it does
  not eliminate hallucination — and the retriever introduces its own
  failure mode if it returns the wrong passages.</li>
  <li><b>Scale separation</b>: a small LM with a large corpus often beats
  a large LM with no retrieval, especially on enterprise data the LM
  has never seen.</li>
</ul>

<p>RAG is now the default architecture for every document-search,
customer-support, and "chat with your docs" product. Modern improvements
focus on reranking (cross-encoder rerankers), query rewriting, multi-step
agentic retrieval, and long-context models that can hold dozens of
retrieved passages at once.</p>
""",
        papers=[
            Paper(
                title="Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks",
                authors="Patrick Lewis et al.",
                year="2020",
                url="https://arxiv.org/abs/2005.11401",
                summary="The original RAG paper. Joint training of a dense retriever and a seq2seq generator on open-domain QA.",
                venue="NeurIPS",
            ),
            Paper(
                title="Dense Passage Retrieval for Open-Domain Question Answering",
                authors="Karpukhin et al.",
                year="2020",
                url="https://arxiv.org/abs/2004.04906",
                summary="The dense-retriever recipe most RAG systems still use: dual-encoder BERT, in-batch negatives, FAISS index.",
                venue="EMNLP",
            ),
            Paper(
                title="REALM: Retrieval-Augmented Language Model Pre-Training",
                authors="Guu, Lee, Tung, Pasupat, Chang",
                year="2020",
                url="https://arxiv.org/abs/2002.08909",
                summary="Earlier and more principled: bake retrieval into the pretraining objective itself, so the LM learns to use the retriever during MLM.",
                venue="ICML",
            ),
        ],
        extras=[
            Extra(
                label="Meta AI: Introducing RAG",
                url="https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 26. 2023 — LLaMA
    # ----------------------------------------------------------------- #
    Chapter(
        id=26,
        slug="llama-open-weights",
        part=PART,
        title="LLaMA and the Open-Weight Era",
        summary_html="""
<p>Until February 2023, the strongest LLMs were proprietary. Meta's
<b>LLaMA</b> release — and especially the leak of its weights two weeks
later — broke that. Within months, an entire open-source ecosystem of
fine-tunes, quantisations, and inference engines had grown up around
LLaMA, and the centre of gravity for academic and indie LLM work
permanently shifted toward open weights.</p>

<h4>What LLaMA 1 actually was</h4>
<ul>
  <li>A standard decoder-only Transformer at 7B / 13B / 33B / 65B
  parameters.</li>
  <li>Trained on ~1.4T tokens of public web data (Common Crawl, Wikipedia,
  GitHub, ArXiv, Books, StackExchange).</li>
  <li>Architectural details that became defaults: <b>RoPE</b> positional
  encodings, <b>SwiGLU</b> activations, <b>RMSNorm</b>, no biases.</li>
  <li>Trained well past the Kaplan-optimal point — closer to Chinchilla —
  which is why a 13B model could approach GPT-3 175B's quality.</li>
</ul>

<h4>The follow-ups that mattered</h4>
<ul>
  <li><b>Llama 2</b> (2023): commercially licensed, paired-up SFT + RLHF
  recipe, chat variants. Made open-weight assistants legitimate for
  enterprise use.</li>
  <li><b>Llama 3</b> (2024): up to 405B parameters, ~15T training tokens,
  GQA, careful data curation. Broadly competitive with frontier
  closed models on standard benchmarks.</li>
</ul>

<h4>Why this changed the field</h4>
<p>Open weights mean reproducibility, mechanistic interpretability work
on real frontier-class models, and a Cambrian explosion of fine-tunes
(Alpaca, Vicuna, WizardLM, OpenChat, ...). They also gave the SLM
movement (chapter 29) a credible foundation: nearly every open small
model after 2023 starts from a Llama, Mistral, or Qwen base. The
"closed labs vs. open ecosystem" dynamic that defines AI in 2026 starts
here.</p>
""",
        papers=[
            Paper(
                title="LLaMA: Open and Efficient Foundation Language Models",
                authors="Hugo Touvron et al.",
                year="2023",
                url="https://arxiv.org/abs/2302.13971",
                summary="The LLaMA 1 paper. The architecture decisions and the data mix are still the template every later open model follows.",
                venue="arXiv",
            ),
            Paper(
                title="Llama 2: Open Foundation and Fine-Tuned Chat Models",
                authors="Hugo Touvron et al.",
                year="2023",
                url="https://arxiv.org/abs/2307.09288",
                summary="Commercial license, paired SFT + RLHF, chat variants, ghost-attention. The model that legitimised open-weight assistants.",
                venue="Meta tech report",
            ),
            Paper(
                title="The Llama 3 Herd of Models",
                authors="Meta Llama team",
                year="2024",
                url="https://arxiv.org/abs/2407.21783",
                summary="The 90-page paper detailing Llama 3 / 3.1 — data pipelines, training infrastructure, multimodal extensions. The most thorough description of a frontier-scale training run available in the open literature.",
                venue="Meta tech report",
            ),
        ],
        extras=[
            Extra(
                label="Meta Llama official site",
                url="https://www.llama.com/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 27. 2023 — LoRA / QLoRA
    # ----------------------------------------------------------------- #
    Chapter(
        id=27,
        slug="lora-qlora-peft",
        part=PART,
        title="LoRA, QLoRA, and Parameter-Efficient Fine-Tuning",
        summary_html="""
<p>Full fine-tuning of a 70B-parameter model needs hundreds of GB of GPU
memory. <b>Parameter-efficient fine-tuning (PEFT)</b> methods change that
by training only a tiny fraction of the weights — and yet matching or
nearly matching full-fine-tune quality on most downstream tasks.
<b>LoRA</b> (2021) is the dominant method; <b>QLoRA</b> (2023) made it
practical on a single consumer GPU.</p>

<h4>LoRA in one equation</h4>
<pre>
Original:    y = W x
With LoRA:   y = W x + (B A) x         # A is r-by-d, B is d-by-r, rank r &lt;&lt; d
</pre>
<p>Freeze the original weights W; train only the low-rank update B·A.
Typical r is 8 or 16. For a 7B model, that means training ~10M
parameters instead of 7B, and the LoRA adapters can be swapped in and
out at inference time per task.</p>

<h4>QLoRA</h4>
<ul>
  <li>Quantise the frozen base model to <b>4-bit NF4</b> (Normal Float 4,
  designed for the actual distribution of LLM weights).</li>
  <li>Keep LoRA adapters in fp16 / bf16.</li>
  <li>Use <b>paged optimisers</b> to spill optimiser state to CPU RAM
  during memory spikes.</li>
  <li>Result: fine-tune a 65B model on a single 48GB GPU, with no quality
  loss vs full-precision LoRA on the Guanaco benchmarks.</li>
</ul>

<h4>Why this is its own chapter</h4>
<p>PEFT democratised fine-tuning. Before LoRA, customising an LLM for
your domain required either a research lab's GPU cluster or paying for
a closed-source provider's fine-tune endpoint. After QLoRA, an engineer
with a single A100 or even a 24GB consumer card can fine-tune a 13B-70B
open-weight model on a few thousand examples overnight. Modern adapter
hubs (Hugging Face PEFT, Together, Predibase) all assume this workflow.
The cost of customising open-weight LLMs collapsed by two orders of
magnitude in 18 months.</p>
""",
        papers=[
            Paper(
                title="LoRA: Low-Rank Adaptation of Large Language Models",
                authors="Edward Hu et al.",
                year="2021",
                url="https://arxiv.org/abs/2106.09685",
                summary="The original LoRA paper. Read for the rank-deficiency hypothesis and the empirical sweep across GPT-2, GPT-3, and RoBERTa.",
                venue="ICLR",
            ),
            Paper(
                title="QLoRA: Efficient Finetuning of Quantized LLMs",
                authors="Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer",
                year="2023",
                url="https://arxiv.org/abs/2305.14314",
                summary="NF4, double quantisation, paged optimisers. The paper that put 65B fine-tuning on a single GPU.",
                venue="NeurIPS",
            ),
            Paper(
                title="Parameter-Efficient Transfer Learning for NLP (Adapters)",
                authors="Houlsby et al.",
                year="2019",
                url="https://arxiv.org/abs/1902.00751",
                summary="The earlier, broader idea: insert small bottleneck layers into a frozen Transformer and only train those. Useful prehistory for LoRA.",
                venue="ICML",
            ),
        ],
        extras=[
            Extra(
                label="Hugging Face PEFT library",
                url="https://huggingface.co/docs/peft/index",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 28. 2024 — MoE at scale
    # ----------------------------------------------------------------- #
    Chapter(
        id=28,
        slug="moe-at-scale-mixtral-deepseek",
        part=PART,
        title="Mixture-of-Experts at Scale (Mixtral, DeepSeek-V3)",
        summary_html="""
<p>By 2024 it was clear that dense Transformers were not the
compute-optimal way to keep scaling. <b>Mixture-of-Experts (MoE)</b>
models replace each feed-forward block with a bank of E experts and a
small router that activates only k of them per token. Total parameters
go up; FLOPs per token stay roughly constant.</p>

<h4>The router</h4>
<pre>
For each token x:
  scores = router(x)                # vector over E experts
  top_k_experts = topk(scores, k)   # typically k = 2
  y = sum_{e in top_k_experts}  softmax(scores)[e] * Expert_e(x)
</pre>

<h4>The headline 2024 results</h4>
<ul>
  <li><b>Mixtral 8x7B</b> (Mistral, January 2024): 8 experts, 2 active per
  token. ~47B total parameters, ~13B active. Matched or beat Llama 2
  70B at a fraction of the inference cost. The model that made MoE
  mainstream in open-source.</li>
  <li><b>DeepSeek-V3</b> (December 2024): 671B total parameters, 37B
  active per token, 256 routed experts. Trained on 14.8T tokens for a
  reported $5.6M of compute. Competitive with frontier closed models on
  standard benchmarks. Showed that MoE plus careful systems engineering
  could collapse the cost gap between open and closed labs.</li>
</ul>

<h4>Why MoE is hard, and why it works anyway</h4>
<ul>
  <li>Routers like to collapse — sending everything to a single expert.
  Auxiliary load-balancing losses are needed to spread tokens.</li>
  <li>Inference is memory-bound: you have to hold all experts in VRAM
  even though you only use a few per token. This is why MoE is great
  for batch serving and awkward for single-stream low-latency use.</li>
  <li>The same FLOP budget buys more parameters, which buys more capacity
  for niche skills and languages — the "specialist experts" intuition,
  loosely.</li>
</ul>

<p>Almost every frontier-class model in 2025 is now MoE. The dense
Transformer is becoming the SLM choice for on-device inference; MoE is
the data-center choice for raw quality per FLOP.</p>
""",
        papers=[
            Paper(
                title="Mixtral of Experts",
                authors="Albert Q. Jiang et al. (Mistral AI)",
                year="2024",
                url="https://arxiv.org/abs/2401.04088",
                summary="Mixtral 8x7B. The open-weight MoE model that made the architecture mainstream. Clean ablations on routing and load balancing.",
                venue="arXiv",
            ),
            Paper(
                title="DeepSeek-V3 Technical Report",
                authors="DeepSeek-AI",
                year="2024",
                url="https://arxiv.org/abs/2412.19437",
                summary="671B-parameter MoE with 37B active per token. The most detailed open description of a frontier-scale MoE training run, including auxiliary-loss-free balancing and FP8 training infrastructure.",
                venue="arXiv",
            ),
            Paper(
                title="Switch Transformer: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity",
                authors="William Fedus, Barret Zoph, Noam Shazeer",
                year="2021",
                url="https://arxiv.org/abs/2101.03961",
                summary="The earlier Google MoE paper that worked through routing instabilities and scaled to 1.6T parameters. Most modern MoE recipes descend from this one.",
                venue="JMLR",
            ),
        ],
        extras=[
            Extra(
                label="A Visual Guide to Mixture of Experts (Maarten Grootendorst)",
                url="https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 29. 2024 — Phi / SLMs
    # ----------------------------------------------------------------- #
    Chapter(
        id=29,
        slug="phi-and-the-slm-thesis",
        part=PART,
        title="Phi and the SLM Thesis: Textbooks Are All You Need",
        summary_html="""
<p>While the frontier labs scaled up, Microsoft Research asked the
opposite question: how small can a capable language model be if you
spend your effort on <i>data quality</i> rather than <i>data quantity</i>?
The <b>Phi</b> series — <i>Textbooks Are All You Need</i> (2023), Phi-2,
Phi-3 (2024) — answered: surprisingly small.</p>

<h4>The data thesis</h4>
<ul>
  <li><b>Pretrain on textbook-quality data</b>: synthetic textbooks
  generated by GPT-3.5 / GPT-4, plus heavily filtered web text picked
  for educational value.</li>
  <li><b>Filter aggressively</b>: a classifier trained to recognise
  "educational" content removes most of the web noise. Quantity drops
  by orders of magnitude; the loss curve looks better.</li>
  <li><b>Fine-tune on textbook-quality exercises</b>: synthetic worked
  problems and their solutions, again generated by a stronger model.</li>
</ul>

<h4>The results</h4>
<ul>
  <li><b>Phi-1</b>: 1.3B parameters, ~7B tokens, beats much larger models
  on HumanEval (Python code).</li>
  <li><b>Phi-2</b>: 2.7B parameters, competitive with 7B-13B
  general-purpose models on reasoning and code.</li>
  <li><b>Phi-3-mini</b>: 3.8B parameters, comparable to GPT-3.5 on broad
  benchmarks while running on a phone.</li>
</ul>

<h4>Why this is the SLM chapter</h4>
<p>The Phi line crystallised what people now call the <b>SLM thesis</b>:
for many real-world tasks, a 2-8B-parameter model trained on
high-quality data — and optionally fine-tuned for the task — is good
enough, runs locally, costs cents instead of dollars, and ships in
products where a 70B+ frontier model can't go. SLMs are why on-device AI
on phones, laptops, and robots is plausible in 2026; chapter 29 is where
that story formally starts in this guide. The follow-ups to read are
Llama 3.2 1B/3B, Gemma 2 2B, Qwen 2.5 1.5B/3B, and SmolLM 2 — all of
which now sit in the 1-4B sweet spot Phi defined.</p>
""",
        papers=[
            Paper(
                title="Textbooks Are All You Need",
                authors="Suriya Gunasekar et al.",
                year="2023",
                url="https://arxiv.org/abs/2306.11644",
                summary="Phi-1. The first paper to make the textbook-quality-data thesis explicit and quantitative. Read for the data-curation methodology more than the model.",
                venue="arXiv",
            ),
            Paper(
                title="Textbooks Are All You Need II: phi-1.5 technical report",
                authors="Yuanzhi Li et al.",
                year="2023",
                url="https://arxiv.org/abs/2309.05463",
                summary="Phi-1.5. Generalises the Phi recipe from code to broad reasoning. Useful intermediate step before Phi-3.",
                venue="arXiv",
            ),
            Paper(
                title="Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone",
                authors="Marah Abdin et al.",
                year="2024",
                url="https://arxiv.org/abs/2404.14219",
                summary="Phi-3-mini, small, and medium. Detailed training and safety methodology, plus the on-device inference characterisation that made the SLM-on-phone narrative concrete.",
                venue="Microsoft tech report",
            ),
        ],
        extras=[
            Extra(
                label="Microsoft Research: Phi-3 announcement",
                url="https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/",
            ),
        ],
    ),

    # ----------------------------------------------------------------- #
    # 30. 2024 — o1 / R1
    # ----------------------------------------------------------------- #
    Chapter(
        id=30,
        slug="inference-time-reasoning-o1-r1",
        part=PART,
        title="Inference-Time Reasoning: o1 and DeepSeek-R1",
        summary_html="""
<p>Through 2023, the answer to "how do we get LLMs to reason better?"
was: prompt them to think step by step (chapter 24), and scale the
training compute. In late 2024, OpenAI's <b>o1</b> and DeepSeek's
<b>R1</b> made the next move: <b>scale inference-time compute</b> by
training models to produce long internal chains of thought and then
optimise those chains with reinforcement learning against verifiable
rewards.</p>

<h4>The recipe (R1, in the open)</h4>
<ol>
  <li>Start from a strong base LM (DeepSeek-V3).</li>
  <li><b>RL with verifiable rewards</b>: math problems with known
  answers, code with unit tests. Reward = 1 if the final answer is
  correct, else 0. No human labels in the loop.</li>
  <li>The model learns to spend hundreds or thousands of tokens
  exploring, backtracking, and verifying — i.e., it discovers
  chain-of-thought from RL signal alone.</li>
  <li>Distil the long-CoT behaviour into a smaller, faster model for
  serving.</li>
</ol>

<h4>The two empirical findings</h4>
<ul>
  <li><b>Inference-time scaling is real</b>: accuracy on hard math and
  competitive coding scales smoothly with how many tokens of internal
  thought the model is allowed to spend.</li>
  <li><b>"Aha moments" emerge</b>: R1's RL run produces self-correction
  behaviour ("Wait, let me reconsider...") with no demonstration data,
  purely from outcome rewards. Reasoning is, at least in this regime,
  a learned strategy rather than a hard-coded prompt pattern.</li>
</ul>

<h4>Why this is the right closing chapter</h4>
<p>This is the second time in five years the field has discovered a new
<i>scaling axis</i>. Pretraining compute (2020). Then preference data
and instruction-following (2022-23). Now inference-time thinking
(2024-25). Each axis gave a step-change in capability that the previous
one would not have predicted. As of 2026, the open question is how far
this axis goes — and whether it composes with multimodal inputs, tool
use, and agentic memory in the way prior axes did. Chapters 18-22 of
this book pick that thread up in detail. Here, the story ends where
2026 begins.</p>
""",
        papers=[
            Paper(
                title="Learning to Reason with LLMs (o1)",
                authors="OpenAI",
                year="2024",
                url="https://web.archive.org/web/2026/https://openai.com/index/learning-to-reason-with-llms/",
                summary="OpenAI's o1 announcement. Sparse on technical detail, generous with capability charts. The first public articulation of inference-time-compute scaling as a deliberate research direction.",
                venue="OpenAI blog",
            ),
            Paper(
                title="DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
                authors="DeepSeek-AI",
                year="2025",
                url="https://arxiv.org/abs/2501.12948",
                summary="The open recipe. Pure-RL reasoning training on a strong base, the 'aha moment' analysis, and distillation into smaller models. The most important open paper of 2025 for understanding modern reasoning models.",
                venue="arXiv",
            ),
            Paper(
                title="Self-Consistency Improves Chain of Thought Reasoning in Language Models",
                authors="Wang et al.",
                year="2022",
                url="https://arxiv.org/abs/2203.11171",
                summary="The pre-history: spend more inference compute by sampling many chains and majority-voting. The simple precursor to learned long-CoT reasoning.",
                venue="ICLR",
            ),
        ],
        extras=[
            Extra(
                label="OpenAI: Learning to Reason with LLMs",
                url="https://web.archive.org/web/2026/https://openai.com/index/learning-to-reason-with-llms/",
            ),
        ],
    ),
]
