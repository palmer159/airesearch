---
id: 4
title: What is a Language Model?
part: II. LLMs and SLMs: What and Why
---

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
<a href="https://en.wikipedia.org/wiki/Chain_rule" target="_blank" rel="noopener">chain rule</a>:</p>
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
  <li><b>Neural LMs</b> — learn dense token embeddings; an RNN/<a href="https://en.wikipedia.org/wiki/Long_short-term_memory" target="_blank" rel="noopener">LSTM</a> or
      Transformer compresses the entire history into a vector.</li>
  <li><b>"Scaling"</b> — keep the recipe, multiply parameters, data, and
      compute together.  Loss falls predictably along
      <a href="https://arxiv.org/abs/2001.08361" target="_blank" rel="noopener">power laws</a>,
      and capabilities you didn't train for start to emerge.</li>
</ul>
<p>That last bullet is the whole reason this field exploded — and it's what
the next chapters unpack.</p>

## Papers

### A Neural Probabilistic Language Model
- **Authors:** Bengio, Ducharme, Vincent, Jauvin
- **Year:** 2003
- **Venue:** JMLR
- **URL:** https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf

The paper that introduced learned word embeddings + a neural net for next-word prediction. Every modern LM is a descendant of this idea.

### Language Models are Few-Shot Learners (GPT-3)
- **Authors:** Brown et al.
- **Year:** 2020
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2005.14165

The 175B-parameter model that made 'just predict the next token' a general-purpose interface to language tasks. Read sections 1–3 for the framing.

### Neural Machine Translation of Rare Words with Subword Units
- **Authors:** Sennrich, Haddow, Birch
- **Year:** 2016
- **Venue:** ACL
- **URL:** https://arxiv.org/abs/1508.07909

Where Byte-Pair Encoding for NLP comes from. The cleanest explanation of why we tokenize at the sub-word level.

### Scaling Laws for Neural Language Models
- **Authors:** Kaplan et al.
- **Year:** 2020
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2001.08361

Loss is a clean power law in parameters, data, and compute. The empirical foundation for the 'just make it bigger' era.

### Training Compute-Optimal Large Language Models (Chinchilla)
- **Authors:** Hoffmann et al.
- **Year:** 2022
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2203.15556

Corrects Kaplan: for a fixed compute budget, you should train a smaller model on more data. This paper is why modern small models punch above their weight.

## Extras
- [Wikipedia: Language model](https://en.wikipedia.org/wiki/Language_model)
- [Wikipedia: Perplexity](https://en.wikipedia.org/wiki/Perplexity)
- [The Illustrated GPT-2 (Jay Alammar)](https://jalammar.github.io/illustrated-gpt2/)
