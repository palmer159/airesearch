"""Bridge chapters (Part II): connecting math foundations to LLMs/SLMs.

These three chapters sit between the math foundations (linear algebra,
calculus/optimization, probability+IT) and the deeper LLM internals.  They
answer the postgrad reader's first three questions after the math:

    1. What actually IS a language model?
    2. Where does the math show up inside one?
    3. Is a small model enough for my use case, or do I need a frontier one?

Voice: friendly, prose+HTML, no LaTeX.  Citations: open-access only.
"""

from _chapter_types import Chapter, Paper, Extra


OVERVIEW_CHAPTERS: list[Chapter] = [
    # ------------------------------------------------------------------ #
    # 4. What is a Language Model?
    # ------------------------------------------------------------------ #
    Chapter(
        id=4,
        slug="what-is-a-language-model",
        part="II. LLMs and SLMs: What and Why",
        title="What is a Language Model?",
        summary_html="""\
<p>A <a href="https://en.wikipedia.org/wiki/Language_model" target="_blank" rel="noopener">language model</a>
is, at its core, a probability distribution over sequences of tokens.  Given
some text so far, it assigns a number to "what comes next" — and the better
those numbers match real text, the better the model.  That's it.  Everything
else is engineering on top of this idea.</p>

<h4>Tokens, not words</h4>
<p>Modern LMs don't operate on words; they operate on <b>tokens</b> — sub-word
chunks produced by a tokenizer like
<a href="https://en.wikipedia.org/wiki/Byte_pair_encoding" target="_blank" rel="noopener">BPE</a>
or SentencePiece.  "tokenization" might become <code>token</code> +
<code>ization</code>.  Tokens give the model a finite vocabulary (typically
30k–200k entries) while still handling any string, including code and rare
proper nouns.</p>

<h4>Autoregressive next-token prediction</h4>
<p>A decoder-only LM factorizes the joint probability of a sequence using the
chain rule:</p>
<pre>
P(x_1, x_2, ..., x_n) = P(x_1) * P(x_2 | x_1) * P(x_3 | x_1, x_2) * ...
</pre>
<p>So generation is just sampling one token at a time and feeding it back in.
Training is just maximizing the log-probability of the next token across
billions of training examples.  Same objective at both ends.</p>

<h4>Perplexity: how we score them</h4>
<p>The standard intrinsic metric is
<a href="https://en.wikipedia.org/wiki/Perplexity" target="_blank" rel="noopener">perplexity</a>
— the exponential of the average per-token negative log-likelihood.  Lower is
better.  Roughly: "the model is, on average, this confused between this many
equally-likely next tokens."</p>

<h4>From n-grams to neural to scale</h4>
<ul>
  <li><b>n-grams</b> — count co-occurrences in a corpus, smooth, done.  Cheap,
      interpretable, but blind to anything beyond the window.</li>
  <li><b>Neural LMs</b> — learn dense token embeddings; an RNN/LSTM or
      Transformer compresses the entire history into a vector.</li>
  <li><b>"Scaling"</b> — keep the recipe, multiply parameters, data, and
      compute together.  Loss falls predictably along
      <a href="https://arxiv.org/abs/2001.08361" target="_blank" rel="noopener">power laws</a>,
      and capabilities you didn't train for start to emerge.</li>
</ul>
<p>That last bullet is the whole reason this field exploded — and it's what
the next chapters unpack.</p>
""",
        papers=[
            Paper(
                title="A Neural Probabilistic Language Model",
                authors="Bengio, Ducharme, Vincent, Jauvin",
                year="2003",
                venue="JMLR",
                url="https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf",
                summary="The paper that introduced learned word embeddings + a neural net for next-word prediction. Every modern LM is a descendant of this idea.",
            ),
            Paper(
                title="Language Models are Few-Shot Learners (GPT-3)",
                authors="Brown et al.",
                year="2020",
                venue="NeurIPS",
                url="https://arxiv.org/abs/2005.14165",
                summary="The 175B-parameter model that made 'just predict the next token' a general-purpose interface to language tasks. Read sections 1–3 for the framing.",
            ),
            Paper(
                title="Neural Machine Translation of Rare Words with Subword Units",
                authors="Sennrich, Haddow, Birch",
                year="2016",
                venue="ACL",
                url="https://arxiv.org/abs/1508.07909",
                summary="Where Byte-Pair Encoding for NLP comes from. The cleanest explanation of why we tokenize at the sub-word level.",
            ),
            Paper(
                title="Scaling Laws for Neural Language Models",
                authors="Kaplan et al.",
                year="2020",
                venue="arXiv",
                url="https://arxiv.org/abs/2001.08361",
                summary="Loss is a clean power law in parameters, data, and compute. The empirical foundation for the 'just make it bigger' era.",
            ),
            Paper(
                title="Training Compute-Optimal Large Language Models (Chinchilla)",
                authors="Hoffmann et al.",
                year="2022",
                venue="arXiv",
                url="https://arxiv.org/abs/2203.15556",
                summary="Corrects Kaplan: for a fixed compute budget, you should train a smaller model on more data. This paper is why modern small models punch above their weight.",
            ),
        ],
        extras=[
            Extra(
                label="Wikipedia: Language model",
                url="https://en.wikipedia.org/wiki/Language_model",
            ),
            Extra(
                label="Wikipedia: Perplexity",
                url="https://en.wikipedia.org/wiki/Perplexity",
            ),
            Extra(
                label="The Illustrated GPT-2 (Jay Alammar)",
                url="https://jalammar.github.io/illustrated-gpt2/",
            ),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 5. The Math Under the Hood
    # ------------------------------------------------------------------ #
    Chapter(
        id=5,
        slug="the-math-under-the-hood",
        part="II. LLMs and SLMs: What and Why",
        title="The Math Under the Hood",
        summary_html="""\
<p>You just read three chapters of math.  Here's the payoff: every piece of
it shows up at a specific place inside an LLM.  This chapter is the map.</p>

<h4>Linear algebra → attention is matmul + softmax</h4>
<p>Everything inside a Transformer is matrix multiplication.  Token embeddings
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
approximations, and SVD shows up later in
<a href="https://arxiv.org/abs/2106.09685" target="_blank" rel="noopener">LoRA</a>
and quantization.</p>

<h4>Calculus and optimization → backprop trains the model</h4>
<p>The loss is a single scalar.  To improve the model we need
<code>dLoss/dParameter</code> for every parameter — billions of them.  That's
<a href="https://en.wikipedia.org/wiki/Backpropagation" target="_blank" rel="noopener">backpropagation</a>:
the chain rule, applied mechanically, in reverse.  An optimizer like
<a href="https://arxiv.org/abs/1412.6980" target="_blank" rel="noopener">Adam</a>
or AdamW takes those gradients and nudges the parameters.  Learning-rate
schedules, warmup, gradient clipping — all are tools to keep that
multi-trillion-step optimization stable.</p>

<h4>Probability and information theory → loss and sampling</h4>
<ul>
  <li><b>Training loss = cross-entropy.</b>  At every position, the model
      outputs a distribution over the vocabulary; the loss is the
      negative log-probability assigned to the actual next token.  That's
      KL-divergence-from-the-data, dressed up.</li>
  <li><b>Perplexity = exp(cross-entropy).</b>  Same number, prettier units.</li>
  <li><b>Inference is sampling.</b>  Greedy, top-k, top-p (nucleus), and
      temperature are all just ways to draw from that next-token
      distribution.  Information theory tells you why temperature 0 is
      brittle and why top-p ≈ 0.9 tends to feel "right."</li>
</ul>
<p>If a future chapter mentions "the gradient flowed through the softmax" or
"we minimize the KL" — you already know what's happening.  Keep going.</p>
""",
        papers=[
            Paper(
                title="Attention Is All You Need",
                authors="Vaswani et al.",
                year="2017",
                venue="NeurIPS",
                url="https://arxiv.org/abs/1706.03762",
                summary="The original Transformer paper. Read it now that you have the linear algebra; the equations should feel obvious.",
            ),
            Paper(
                title="Learning representations by back-propagating errors",
                authors="Rumelhart, Hinton, Williams",
                year="1986",
                venue="Nature (open access via Stanford)",
                url="https://www.cs.toronto.edu/~hinton/absps/naturebp.pdf",
                summary="The 1986 paper that put backprop on the map. Short, readable, and you can follow every step with one calculus chapter under your belt.",
            ),
            Paper(
                title="Adam: A Method for Stochastic Optimization",
                authors="Kingma, Ba",
                year="2015",
                venue="ICLR",
                url="https://arxiv.org/abs/1412.6980",
                summary="The optimizer that trains nearly every modern LLM (usually as AdamW). Adaptive per-parameter learning rates with momentum.",
            ),
            Paper(
                title="The Curious Case of Neural Text Degeneration",
                authors="Holtzman, Buys, Du, Forbes, Choi",
                year="2020",
                venue="ICLR",
                url="https://arxiv.org/abs/1904.09751",
                summary="Where nucleus (top-p) sampling comes from. The clearest explanation of why naive sampling produces gibberish and how information theory points to the fix.",
            ),
            Paper(
                title="LoRA: Low-Rank Adaptation of Large Language Models",
                authors="Hu et al.",
                year="2021",
                venue="ICLR",
                url="https://arxiv.org/abs/2106.09685",
                summary="A direct payoff of the linear-algebra chapter: fine-tune by adding a low-rank update to weight matrices. Cuts the trainable-parameter count by orders of magnitude.",
            ),
            Paper(
                title="The Illustrated Transformer",
                authors="Jay Alammar",
                year="2018",
                venue="blog",
                url="https://jalammar.github.io/illustrated-transformer/",
                summary="The visual companion. Useful even on a re-read because the diagrams pin down which matmul is which.",
            ),
        ],
        extras=[
            Extra(
                label="Wikipedia: Backpropagation",
                url="https://en.wikipedia.org/wiki/Backpropagation",
            ),
            Extra(
                label="Wikipedia: Softmax function",
                url="https://en.wikipedia.org/wiki/Softmax_function",
            ),
            Extra(
                label="Lilian Weng: Attention? Attention!",
                url="https://lilianweng.github.io/posts/2018-06-24-attention/",
            ),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 6. SLMs vs LLMs: When to Choose Which
    # ------------------------------------------------------------------ #
    Chapter(
        id=6,
        slug="slms-vs-llms",
        part="II. LLMs and SLMs: What and Why",
        title="SLMs vs LLMs: When to Choose Which",
        summary_html="""\
<p>The default 2026 conversation in any engineering org goes: "do we use a
frontier model or a small one?"  This chapter gives you the framing.  There's
no universal answer — but the trade-offs are surprisingly clean once you see
them.</p>

<h4>What's an SLM?</h4>
<p>An <b>SLM</b> (small language model) is, by rough community convention, a
model with up to about 7B parameters — small enough to serve on a single
modern GPU, sometimes on a phone or laptop.  The "small" is relative: a 7B
model in 2026 is wildly more capable than a 175B model from 2020, thanks to
better data, better recipes, and Chinchilla-style training.  Names you'll see
on benchmarks: <a href="https://arxiv.org/abs/2306.11644" target="_blank" rel="noopener">Phi</a>,
<a href="https://huggingface.co/google/gemma-2-2b" target="_blank" rel="noopener">Gemma</a>,
<a href="https://arxiv.org/abs/2407.21783" target="_blank" rel="noopener">Llama-3 8B</a>,
and the
<a href="https://huggingface.co/blog/smollm" target="_blank" rel="noopener">SmolLM</a> family.</p>

<h4>The economics</h4>
<ul>
  <li><b>Inference cost</b> scales roughly with parameters and context length.
      A 7B model is ~25× cheaper per token than a 175B-class one and an
      order of magnitude cheaper than frontier models.</li>
  <li><b>Latency</b> is the killer dimension for UX.  Sub-second
      time-to-first-token typically requires either a small model or
      heavy caching infrastructure.</li>
  <li><b>On-device</b> matters when data can't leave the device — health,
      keyboards, enterprise search over confidential corpora.  Only SLMs
      fit there today.</li>
  <li><b>Operational simplicity</b> — one GPU, no sharding, no
      multi-node coordination, no custom inference stack.</li>
</ul>

<h4>When the LLM is the right tool</h4>
<p>Use a frontier LLM when the task needs broad world knowledge, long-horizon
reasoning, or the long tail of language and code that small models simply
haven't seen enough of.  Multi-step agentic workflows, novel-domain code
generation, complex analysis with many constraints — these still favor the
big models, often by a lot.</p>

<h4>When the SLM is the right tool</h4>
<ul>
  <li>The task is narrow and you can either fine-tune or prompt it tightly:
      classification, extraction, routing, summarization of in-domain text.</li>
  <li>Latency or cost dominates the product requirement.</li>
  <li>You need on-device or air-gapped deployment.</li>
  <li>You can put the LLM behind the SLM as a fallback — a router pattern that
      sends only the hard cases up.</li>
</ul>

<h4>The honest summary</h4>
<p>Quality scales with size, but utility scales with capability per dollar at
your latency budget.  For a lot of production workloads in 2026 the right
answer is a fine-tuned 7B model with the option to escalate — not the most
expensive thing on the menu.</p>
""",
        papers=[
            Paper(
                title="Textbooks Are All You Need (Phi-1)",
                authors="Gunasekar et al.",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2306.11644",
                summary="The paper that kicked off the small-but-strong era. A 1.3B model trained on curated 'textbook-quality' data competes with much larger models on code.",
            ),
            Paper(
                title="The Llama 3 Herd of Models",
                authors="Llama Team, Meta",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.21783",
                summary="The reference open-weights family. The 8B variant is the standard SLM baseline; the report itself is one of the most useful training-recipe documents in the open literature.",
            ),
            Paper(
                title="Training Compute-Optimal Large Language Models (Chinchilla)",
                authors="Hoffmann et al.",
                year="2022",
                venue="arXiv",
                url="https://arxiv.org/abs/2203.15556",
                summary="The reason small models got good. For a fixed compute budget, train a smaller model on more tokens — and SLMs benefit the most from that correction.",
            ),
            Paper(
                title="Scaling Laws for Neural Language Models",
                authors="Kaplan et al.",
                year="2020",
                venue="arXiv",
                url="https://arxiv.org/abs/2001.08361",
                summary="The original scaling-laws paper. Read it alongside Chinchilla to see what changed and why 'bigger is always better' was incomplete.",
            ),
            Paper(
                title="SmolLM: blazingly fast and remarkably powerful",
                authors="Hugging Face",
                year="2024",
                venue="HF blog",
                url="https://huggingface.co/blog/smollm",
                summary="A clear case study: 135M / 360M / 1.7B models trained on a curated open dataset. Excellent reading on what 'small' means in practice and where it breaks.",
            ),
        ],
        extras=[
            Extra(
                label="Hugging Face: Llama-3 8B Instruct model card",
                url="https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct",
            ),
            Extra(
                label="Hugging Face: Gemma-2 2B model card",
                url="https://huggingface.co/google/gemma-2-2b",
            ),
            Extra(
                label="Hugging Face: SmolLM2 collection",
                url="https://huggingface.co/blog/smollm",
            ),
        ],
    ),
]
