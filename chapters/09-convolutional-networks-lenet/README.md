---
id: 9
title: Convolutional Networks (LeNet)
part: III. ML & AI in Chronological Order
---

<p>Yann LeCun's 1989 work at Bell Labs took backprop and added the right
inductive biases for images: <b>local receptive fields</b>, <b>weight
sharing</b>, and <b>spatial pooling</b>. The result — a convolutional neural
network, later christened <a href="https://en.wikipedia.org/wiki/LeNet" target="_blank" rel="noopener">LeNet</a> — could read handwritten ZIP-code digits
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

## Papers

### Backpropagation Applied to Handwritten Zip Code Recognition
- **Authors:** Yann LeCun et al.
- **Year:** 1989
- **Venue:** Neural Computation
- **URL:** http://yann.lecun.com/exdb/publis/pdf/lecun-89e.pdf

The original LeNet-1 paper. Read it for the architecture, the weight-sharing argument, and a reminder of how much can be done with a few thousand training examples and a careful prior.

### Gradient-Based Learning Applied to Document Recognition
- **Authors:** LeCun, Bottou, Bengio, Haffner
- **Year:** 1998
- **Venue:** Proc. IEEE
- **URL:** http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf

The mature LeNet-5 paper plus a wide-ranging survey of gradient-based learning. Often the easier read of the two.

## Extras
- [LeCun's publications page](http://yann.lecun.com/exdb/publis/)
