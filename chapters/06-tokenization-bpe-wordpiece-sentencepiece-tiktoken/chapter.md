---
id: 6
title: Tokenization: BPE, WordPiece, SentencePiece, Tiktoken
part: II. Training & Data
---

<p>Tokenization is the silent foundation. Modern LMs use <b>subword</b> tokenizers — most commonly
<b><a href="https://en.wikipedia.org/wiki/Byte_pair_encoding" target="_blank" rel="noopener">Byte-Pair Encoding</a> (BPE)</b> in its byte-level form (GPT-2/3/4, <a href="https://en.wikipedia.org/wiki/Llama_(language_model)" target="_blank" rel="noopener">Llama</a>). Subwords give an open vocabulary,
robustness to typos, and compactness across languages.</p>

<h4>Trade-offs</h4>
<ul>
  <li>Larger vocab → shorter sequences but more embedding parameters.</li>
  <li>Byte-level BPE handles arbitrary Unicode without UNK; this is non-negotiable for code and multilingual data.</li>
  <li>Tokenizer choice affects fairness — non-Latin scripts can use 2-4x more tokens for the same content
      (cost + context-window cost asymmetry).</li>
</ul>

## Papers

### Neural Machine Translation of Rare Words with Subword Units (BPE)
- **Authors:** Sennrich, Haddow, Birch
- **Year:** 2016
- **Venue:** ACL
- **URL:** https://arxiv.org/abs/1508.07909

Brings BPE to NLP. Open vocabulary, no UNK, handles rare words gracefully.

### SentencePiece: A simple and language independent subword tokenizer
- **Authors:** Kudo, Richardson
- **Year:** 2018
- **URL:** https://arxiv.org/abs/1808.06226

Pre-tokenizer-free, language-agnostic; the de facto choice for multilingual systems (T5, Llama).

### Subword Regularization
- **Authors:** Kudo
- **Year:** 2018
- **Venue:** ACL
- **URL:** https://arxiv.org/abs/1804.10959

Stochastic tokenizations (unigram LM) as data augmentation.

### Language Model Tokenizers Introduce Unfairness Between Languages
- **Authors:** Petrov et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.15425

Quantifies the multilingual tokenization tax. Read this before deploying a multilingual product.

## Extras

- [tiktoken (OpenAI)](https://github.com/openai/tiktoken)
- [Hugging Face tokenizers](https://github.com/huggingface/tokenizers)
