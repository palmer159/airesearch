---
id: 7
title: The Perceptron
part: III. ML & AI in Chronological Order
---

<p>In 1958 Frank Rosenblatt introduced the <b><a href="https://en.wikipedia.org/wiki/Perceptron" target="_blank" rel="noopener">perceptron</a></b>: a single
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

## Papers

### The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain
- **Authors:** Frank Rosenblatt
- **Year:** 1958
- **Venue:** encyclopedia
- **URL:** https://en.wikipedia.org/wiki/Perceptron

Wikipedia's article reproduces the model, the update rule, and the convergence theorem with citations to the original Cornell technical report. Rosenblatt's own 1958 paper is paywalled in APA's archive; this is the authoritative open mirror.

### Perceptrons (book, 1969)
- **Authors:** Marvin Minsky, Seymour Papert
- **Year:** 1969
- **Venue:** MIT Press
- **URL:** https://en.wikipedia.org/wiki/Perceptrons_(book)

The critique that ended the first wave of neural-net research by formally showing the limits of single-layer perceptrons. Worth reading historically — its conclusions were narrower than the field assumed.

### Learning representations by back-propagating errors
- **Authors:** Rumelhart, Hinton, Williams
- **Year:** 1986
- **Venue:** Nature
- **URL:** https://web.archive.org/web/2026/https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf

The eventual answer to Minsky and Papert: train multi-layer perceptrons by backpropagation. Listed here so the reader can see how the next chapter directly responds to this one.

## Extras
- [Wikipedia: Perceptron](https://en.wikipedia.org/wiki/Perceptron)
