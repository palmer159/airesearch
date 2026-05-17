---
id: 18
title: BERT and the Encoder Era
part: III. ML & AI in Chronological Order
---

<p><b><a href="https://en.wikipedia.org/wiki/BERT_(language_model)" target="_blank" rel="noopener">BERT</a></b> (Devlin, Chang, Lee, Toutanova, 2018) was the first model
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
  diverge for a while. <a href="https://en.wikipedia.org/wiki/GPT-3" target="_blank" rel="noopener">GPT-3</a> would later collapse some of that
  distinction, but in 2018 the split was clean.</li>
</ul>

## Papers

### BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- **Authors:** Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **Year:** 2018
- **Venue:** NAACL
- **URL:** https://arxiv.org/abs/1810.04805

The BERT paper. MLM + NSP, fine-tuning recipe, benchmark sweep. The point of departure for the encoder-only family.

### RoBERTa: A Robustly Optimized BERT Pretraining Approach
- **Authors:** Liu et al.
- **Year:** 2019
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/1907.11692

Showed that BERT was significantly undertrained. Drop NSP, train longer with bigger batches and more data.

### ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators
- **Authors:** Clark, Luong, Le, Manning
- **Year:** 2020
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2003.10555

Replaces MLM with a more sample-efficient discriminative objective. Often the first thing to try if compute is tight.

## Extras
- [The Illustrated BERT (Jay Alammar)](https://jalammar.github.io/illustrated-bert/)
