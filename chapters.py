"""
Study guide chapter content for SLM/LLM research.
Each chapter: id, title, part, summary (HTML), papers [{title, authors, year, venue, url, summary}], extras.
"""

CHAPTERS = [
    # ============================================================
    # PART I — FOUNDATIONS
    # ============================================================
    {
        "id": 1, "part": "I. Foundations",
        "title": "From n-grams to Neural LMs: A Brief History",
        "summary": """
<p>Before transformers there were <b>n-gram</b> models (Shannon, 1948), <b>feed-forward neural language models</b>
(Bengio et al., 2003), and <b>recurrent</b> language models (Mikolov, 2010). The leap was learning <i>distributed
representations</i> instead of memorizing surface forms. Read this chapter as motivation: the modern stack inherits
the same objective — predict the next token — but at radically larger scale and with far better architectures.</p>

<h4>Illustrative example</h4>
<pre>
n-gram (trigram):  P(w_t | w_{t-2}, w_{t-1})       # sparse counts, no generalization
Neural LM:         P(w_t | h_t),  h_t = f(embedding(context))   # dense, generalizes
</pre>
<p>The neural LM's embeddings make "king - man + woman ≈ queen" possible. That single observation foreshadows
why scale-up of neural LMs eventually subsumed all of NLP.</p>
""",
        "papers": [
            {"title": "A Mathematical Theory of Communication", "authors": "Shannon", "year": 1948,
             "venue": "Bell System Tech. Journal",
             "url": "https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf",
             "summary": "Defines entropy and the predict-the-next-symbol formalism that underlies all modern LMs."},
            {"title": "A Neural Probabilistic Language Model", "authors": "Bengio, Ducharme, Vincent, Jauvin", "year": 2003,
             "venue": "JMLR", "url": "https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf",
             "summary": "First widely cited neural LM with learned word embeddings; defeats n-grams via distributed representations."},
            {"title": "Recurrent neural network based language model", "authors": "Mikolov et al.", "year": 2010,
             "venue": "Interspeech",
             "url": "https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.pdf",
             "summary": "RNN-LM beats n-grams on perplexity and ASR; the first crack in the n-gram dam."},
            {"title": "Distributed Representations of Words and Phrases (word2vec)", "authors": "Mikolov et al.", "year": 2013,
             "venue": "NeurIPS", "url": "https://arxiv.org/abs/1310.4546",
             "summary": "Skip-gram + negative sampling. Made dense word vectors the default input to NLP."},
            {"title": "GloVe: Global Vectors for Word Representation", "authors": "Pennington, Socher, Manning", "year": 2014,
             "venue": "EMNLP", "url": "https://nlp.stanford.edu/pubs/glove.pdf",
             "summary": "Matrix-factorization view of word embeddings; complement to word2vec."},
        ],
    },
    {
        "id": 2, "part": "I. Foundations",
        "title": "The Transformer: Attention Is All You Need",
        "summary": """
<p>The 2017 transformer replaces recurrence with <b>self-attention</b>: each token attends to every other token in
parallel. Three ingredients matter: scaled dot-product attention, multi-head attention, and positional encodings.</p>

<h4>Self-attention in one equation</h4>
<pre>
Attention(Q, K, V) = softmax( Q K^T / sqrt(d_k) ) V
</pre>
<p>Why this matters: O(1) path length between any two tokens (vs O(n) for RNNs), trivially parallelizable on GPUs,
and the inductive bias is mild enough that scaling up just keeps working.</p>

<h4>Encoder vs decoder vs encoder-decoder</h4>
<ul>
  <li><b>Encoder-only</b> (BERT family) — bidirectional, good for classification/retrieval.</li>
  <li><b>Decoder-only</b> (GPT family) — causal, good for generation. The dominant modern form.</li>
  <li><b>Encoder-decoder</b> (T5, original Transformer) — good for seq2seq translation/summarization.</li>
</ul>
""",
        "papers": [
            {"title": "Attention Is All You Need", "authors": "Vaswani et al.", "year": 2017, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/1706.03762",
             "summary": "The Transformer. Self-attention, multi-head, positional encoding. Foundation of every modern LM."},
            {"title": "The Illustrated Transformer", "authors": "Jay Alammar", "year": 2018, "venue": "blog",
             "url": "https://jalammar.github.io/illustrated-transformer/",
             "summary": "Best beginner-friendly visual explanation of attention; pair it with the original paper."},
            {"title": "The Annotated Transformer", "authors": "Sasha Rush et al.", "year": 2018, "venue": "Harvard NLP",
             "url": "http://nlp.seas.harvard.edu/annotated-transformer/",
             "summary": "Line-by-line PyTorch implementation interleaved with the paper. The canonical pedagogical resource."},
            {"title": "Layer Normalization", "authors": "Ba, Kiros, Hinton", "year": 2016, "venue": "arXiv",
             "url": "https://arxiv.org/abs/1607.06450",
             "summary": "LayerNorm — the normalization that made deep transformers trainable."},
        ],
    },
    {
        "id": 3, "part": "I. Foundations",
        "title": "BERT and the Encoder Era",
        "summary": """
<p><b>BERT</b> (2018) showed that a deep bidirectional transformer pretrained with masked-LM + next-sentence-prediction
beats every supervised SOTA on 11 NLP tasks after fine-tuning. The lesson: <i>pretrain once, fine-tune everywhere</i>.</p>

<p>Successors refined the recipe — <b>RoBERTa</b> (drop NSP, train longer), <b>ALBERT</b> (parameter sharing),
<b>DeBERTa</b> (disentangled attention), <b>ELECTRA</b> (replaced-token detection, more sample-efficient).</p>

<p>Encoders remain the right tool for <b>retrieval</b>, <b>classification</b>, and <b>embeddings</b> (see Ch. 30 on RAG).</p>
""",
        "papers": [
            {"title": "BERT: Pre-training of Deep Bidirectional Transformers", "authors": "Devlin et al.", "year": 2018,
             "venue": "NAACL", "url": "https://arxiv.org/abs/1810.04805",
             "summary": "Masked-LM pretraining on a deep bidirectional transformer; unified pretrain-then-finetune recipe for NLP."},
            {"title": "RoBERTa: A Robustly Optimized BERT", "authors": "Liu et al.", "year": 2019, "venue": "arXiv",
             "url": "https://arxiv.org/abs/1907.11692",
             "summary": "BERT done right: more data, longer training, no NSP. A reminder that hyperparameters dominate architecture."},
            {"title": "ELECTRA: Pre-training as Discriminators", "authors": "Clark et al.", "year": 2020, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2003.10555",
             "summary": "Replaced-token detection — every token contributes a training signal, so it's far more sample-efficient than MLM."},
            {"title": "DeBERTa: Decoding-enhanced BERT with Disentangled Attention", "authors": "He et al.", "year": 2020,
             "venue": "ICLR", "url": "https://arxiv.org/abs/2006.03654",
             "summary": "Separates content from position attention; current SOTA among encoder-only models on GLUE/SuperGLUE."},
            {"title": "Sentence-BERT", "authors": "Reimers, Gurevych", "year": 2019, "venue": "EMNLP",
             "url": "https://arxiv.org/abs/1908.10084",
             "summary": "Siamese BERT for sentence embeddings — the foundation of modern retrieval/RAG embedding models."},
        ],
    },
    {
        "id": 4, "part": "I. Foundations",
        "title": "GPT-1/2/3 and the Decoder-Only Paradigm",
        "summary": """
<p>OpenAI's GPT line bet on <b>decoder-only autoregressive</b> models and on <b>scale</b>. GPT-3 (2020) was the
inflection point: at 175B parameters, in-context learning emerged — you could prompt the model with examples and
get a usable downstream learner without any gradient updates.</p>

<h4>Why decoder-only won</h4>
<ul>
  <li>Single objective (next-token prediction) — no pretrain/finetune mismatch.</li>
  <li>Generation and classification fold into one interface (just generate the answer).</li>
  <li>Scales gracefully; tooling (sampling, beam, KV cache) is well-understood.</li>
</ul>
""",
        "papers": [
            {"title": "Improving Language Understanding by Generative Pre-Training (GPT-1)", "authors": "Radford, Narasimhan, Salimans, Sutskever", "year": 2018, "venue": "OpenAI",
             "url": "https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf",
             "summary": "Generative pretraining + discriminative fine-tuning. Sets the decoder-only template."},
            {"title": "Language Models are Unsupervised Multitask Learners (GPT-2)", "authors": "Radford et al.", "year": 2019,
             "venue": "OpenAI",
             "url": "https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf",
             "summary": "Zero-shot multitask via prompting. First widely-discussed dual-use safety release."},
            {"title": "Language Models are Few-Shot Learners (GPT-3)", "authors": "Brown et al.", "year": 2020, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2005.14165",
             "summary": "175B parameters; few-shot in-context learning emerges. The paper that changed everything."},
            {"title": "GPT-4 Technical Report", "authors": "OpenAI", "year": 2023,
             "url": "https://arxiv.org/abs/2303.08774",
             "summary": "Multimodal, professional-test performance, RLHF + heavy red-teaming. Light on architecture, heavy on capabilities/safety."},
        ],
    },
    {
        "id": 5, "part": "I. Foundations",
        "title": "T5, BART, and the Text-to-Text Frame",
        "summary": """
<p>Google's <b>T5</b> reframed every NLP task — translation, classification, QA, summarization — as
<i>text in, text out</i>. The C4 corpus, span corruption objective, and unified prefix-task tokens became
standard machinery in subsequent systems.</p>
<p><b>BART</b> (Facebook) used a denoising autoencoder over arbitrary corruptions; an excellent encoder-decoder
for summarization. <b>FLAN-T5</b> (Ch. 12) showed that instruction-tuning T5 makes it competitive with much larger
decoder-only models — an early hint that data quality > raw scale.</p>
""",
        "papers": [
            {"title": "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5)", "authors": "Raffel et al.", "year": 2020, "venue": "JMLR",
             "url": "https://arxiv.org/abs/1910.10683",
             "summary": "Unified text-to-text transformer; introduces C4. The most thorough ablation study in pretraining literature."},
            {"title": "BART: Denoising Sequence-to-Sequence Pre-training", "authors": "Lewis et al.", "year": 2019, "venue": "ACL",
             "url": "https://arxiv.org/abs/1910.13461",
             "summary": "Encoder-decoder pretrained on noisy-input → clean-output. Strong on summarization and dialogue."},
            {"title": "Scaling Instruction-Finetuned Language Models (FLAN-T5)", "authors": "Chung et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2210.11416",
             "summary": "Instruction-tunes T5 on 1,800+ tasks. Demonstrates instruction-tuning as a generic capability multiplier."},
        ],
    },

    # ============================================================
    # PART II — TRAINING & DATA
    # ============================================================
    {
        "id": 6, "part": "II. Training & Data",
        "title": "Tokenization: BPE, WordPiece, SentencePiece, Tiktoken",
        "summary": """
<p>Tokenization is the silent foundation. Modern LMs use <b>subword</b> tokenizers — most commonly
<b>Byte-Pair Encoding (BPE)</b> in its byte-level form (GPT-2/3/4, Llama). Subwords give an open vocabulary,
robustness to typos, and compactness across languages.</p>

<h4>Trade-offs</h4>
<ul>
  <li>Larger vocab → shorter sequences but more embedding parameters.</li>
  <li>Byte-level BPE handles arbitrary Unicode without UNK; this is non-negotiable for code and multilingual data.</li>
  <li>Tokenizer choice affects fairness — non-Latin scripts can use 2-4x more tokens for the same content
      (cost + context-window cost asymmetry).</li>
</ul>
""",
        "papers": [
            {"title": "Neural Machine Translation of Rare Words with Subword Units (BPE)", "authors": "Sennrich, Haddow, Birch", "year": 2016, "venue": "ACL",
             "url": "https://arxiv.org/abs/1508.07909",
             "summary": "Brings BPE to NLP. Open vocabulary, no UNK, handles rare words gracefully."},
            {"title": "SentencePiece: A simple and language independent subword tokenizer", "authors": "Kudo, Richardson", "year": 2018,
             "url": "https://arxiv.org/abs/1808.06226",
             "summary": "Pre-tokenizer-free, language-agnostic; the de facto choice for multilingual systems (T5, Llama)."},
            {"title": "Subword Regularization", "authors": "Kudo", "year": 2018, "venue": "ACL",
             "url": "https://arxiv.org/abs/1804.10959",
             "summary": "Stochastic tokenizations (unigram LM) as data augmentation."},
            {"title": "Language Model Tokenizers Introduce Unfairness Between Languages", "authors": "Petrov et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.15425",
             "summary": "Quantifies the multilingual tokenization tax. Read this before deploying a multilingual product."},
        ],
        "extras": [
            {"label": "tiktoken (OpenAI)", "url": "https://github.com/openai/tiktoken"},
            {"label": "Hugging Face tokenizers", "url": "https://github.com/huggingface/tokenizers"},
        ],
    },
    {
        "id": 7, "part": "II. Training & Data",
        "title": "Pretraining Data: C4, The Pile, RedPajama, Dolma, FineWeb",
        "summary": """
<p>Data is the dominant lever in pretraining. Public corpora have evolved from <b>C4</b> (T5, 2020) to
ever-larger, better-filtered web datasets — <b>The Pile</b>, <b>RedPajama</b>, <b>RefinedWeb</b>, <b>Dolma</b>,
and currently <b>FineWeb</b> / <b>FineWeb-Edu</b> (15T tokens).</p>

<h4>What "good data" looks like in 2026</h4>
<ul>
  <li>Aggressive deduplication (exact + near-duplicate via MinHash/LSH).</li>
  <li>Quality classifiers — model-based filtering for "educational content" beats heuristics.</li>
  <li>Domain mix tuned per stage (e.g., more math/code at the end of pretraining annealing).</li>
  <li>Decontamination from eval benchmarks (often missed; inflates reported scores).</li>
</ul>
""",
        "papers": [
            {"title": "The Pile: An 800GB Dataset of Diverse Text", "authors": "Gao et al.", "year": 2020,
             "url": "https://arxiv.org/abs/2101.00027",
             "summary": "The first widely-used open pretraining corpus combining 22 sources; reusable methodology."},
            {"title": "Deduplicating Training Data Makes Language Models Better", "authors": "Lee et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2107.06499",
             "summary": "Dedup → less memorization, better perplexity, faster training. A free win."},
            {"title": "The RefinedWeb Dataset for Falcon LLM", "authors": "Penedo et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2306.01116",
             "summary": "Shows web-only, well-filtered data can match curated mixes. Influenced FineWeb."},
            {"title": "Dolma: an Open Corpus of Three Trillion Tokens", "authors": "Soldaini et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2402.00159",
             "summary": "AI2's open recipe — releases the data, the toolkit, and the design rationale."},
            {"title": "FineWeb / FineWeb-Edu", "authors": "Penedo et al.", "year": 2024, "venue": "Hugging Face",
             "url": "https://huggingface.co/datasets/HuggingFaceFW/fineweb",
             "summary": "15T-token open web corpus; FineWeb-Edu uses an educational-quality classifier and improves benchmark scores significantly."},
        ],
    },
    {
        "id": 8, "part": "II. Training & Data",
        "title": "Optimization: AdamW, Schedules, Mixed Precision, ZeRO",
        "summary": """
<p>Training a transformer is mostly engineering. The defaults that work today:</p>
<ul>
  <li><b>AdamW</b> with β=(0.9, 0.95), weight decay 0.1.</li>
  <li><b>Cosine</b> learning-rate schedule with linear warmup (a few thousand steps), max LR scaled with batch size.</li>
  <li><b>Mixed precision</b> — bf16 dominates fp16 for stability; fp8 emerging for H100/B200.</li>
  <li><b>ZeRO</b> (DeepSpeed) and <b>FSDP</b> (PyTorch) for sharding optimizer state, gradients, and parameters across GPUs.</li>
  <li><b>Gradient clipping</b> at 1.0 to control loss spikes.</li>
  <li><b>μP</b> (Maximal Update Parameterization) — transfer hyperparameters from small to large models.</li>
</ul>
""",
        "papers": [
            {"title": "Decoupled Weight Decay Regularization (AdamW)", "authors": "Loshchilov, Hutter", "year": 2019,
             "url": "https://arxiv.org/abs/1711.05101",
             "summary": "Properly decouples weight decay from gradient-based updates. The default optimizer for LMs."},
            {"title": "Mixed Precision Training", "authors": "Micikevicius et al.", "year": 2018,
             "url": "https://arxiv.org/abs/1710.03740",
             "summary": "fp16 with loss scaling. The follow-up bfloat16 (Google) is now the de-facto standard for pretraining."},
            {"title": "ZeRO: Memory Optimizations for Training Trillion-Parameter Models", "authors": "Rajbhandari et al.", "year": 2020,
             "url": "https://arxiv.org/abs/1910.02054",
             "summary": "Shards optimizer state / gradients / parameters across data-parallel ranks. Enables truly large training runs."},
            {"title": "Tensor Programs V (μP)", "authors": "Yang et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2203.03466",
             "summary": "Hyperparameter-transfer across width: tune at 100M, deploy at 100B. Massively reduces tuning cost."},
        ],
    },
    {
        "id": 9, "part": "II. Training & Data",
        "title": "Scaling Laws: Kaplan, Chinchilla, and Beyond",
        "summary": """
<p>Scaling laws predict loss as a power-law in compute, parameters, and data. Two pivotal results:</p>
<ul>
  <li><b>Kaplan et al. (2020)</b> — loss is smooth and predictable in N (parameters) and D (data); recommended
      under-training relative to parameters.</li>
  <li><b>Chinchilla (Hoffmann et al., 2022)</b> — corrected the recipe: optimal compute uses roughly <b>20 tokens
      per parameter</b>. Most pre-2022 large models were under-trained.</li>
</ul>
<p>Chinchilla's insight reshaped the entire field. It also motivated the SLM movement (Ch. 17): if you train smaller
models on more tokens, you get inference-time efficiency for free.</p>
<p>Open question for 2026: with synthetic data and curriculum, are we approaching a regime where the data axis is the
true bottleneck — and should new scaling laws account for data quality, not just quantity?</p>
""",
        "papers": [
            {"title": "Scaling Laws for Neural Language Models", "authors": "Kaplan et al.", "year": 2020,
             "url": "https://arxiv.org/abs/2001.08361",
             "summary": "Power-law scaling in N, D, C. Influenced GPT-3 sizing — but later shown to under-train."},
            {"title": "Training Compute-Optimal Large Language Models (Chinchilla)", "authors": "Hoffmann et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2203.15556",
             "summary": "Re-derives optimal N and D under fixed compute; rule-of-thumb 20 tokens/parameter."},
            {"title": "Scaling Laws and Interpretability of Learning from Repeated Data", "authors": "Hernandez et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2205.10487",
             "summary": "Repeated data isn't free — performance plateaus and then degrades. Constrains how far we can ride a fixed corpus."},
            {"title": "Beyond neural scaling laws: beating power law scaling via data pruning", "authors": "Sorscher et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2206.14486",
             "summary": "Data quality can change the exponent of the scaling law, not just the constant."},
        ],
    },
    {
        "id": 10, "part": "II. Training & Data",
        "title": "Emergent Abilities, Mirages, and Phase Transitions",
        "summary": """
<p>"Emergence" — capabilities that appear sharply at some scale — became the central narrative of 2022.
Wei et al. cataloged dozens of emergent tasks. Schaeffer et al. (2023) argued many are <b>artifacts of
discontinuous metrics</b>: switch from exact-match accuracy to log-likelihood and the curve is smooth.</p>
<p>The honest synthesis: some capabilities (multi-step reasoning, instruction-following with realistic prompts)
do show non-trivial regime changes; others are metric mirages. Either way, a CS practitioner should be skeptical
of any "emergence" claim that depends on one specific scoring rule.</p>
""",
        "papers": [
            {"title": "Emergent Abilities of Large Language Models", "authors": "Wei et al.", "year": 2022, "venue": "TMLR",
             "url": "https://arxiv.org/abs/2206.07682",
             "summary": "Catalogs sharp capability transitions with scale; the most-cited 'emergence' paper."},
            {"title": "Are Emergent Abilities of Large Language Models a Mirage?", "authors": "Schaeffer, Miranda, Koyejo", "year": 2023,
             "venue": "NeurIPS (Outstanding Paper)", "url": "https://arxiv.org/abs/2304.15004",
             "summary": "Many emergence claims dissolve under continuous metrics. Required reading for the calibration of belief."},
        ],
    },

    # ============================================================
    # PART III — ARCHITECTURE FRONTIERS
    # ============================================================
    {
        "id": 11, "part": "III. Architecture Frontiers",
        "title": "Positional Encoding & Long Context (RoPE, ALiBi, YaRN)",
        "summary": """
<p>Vanilla absolute positions don't extrapolate beyond training length. Modern systems use:</p>
<ul>
  <li><b>RoPE</b> (Rotary Position Embedding) — rotates query/key vectors by a position-dependent angle. Llama, Qwen, Mistral.</li>
  <li><b>ALiBi</b> — adds a linear distance bias to attention; trivial extrapolation but slightly weaker quality.</li>
  <li><b>YaRN / NTK-aware scaling</b> — interpolation tricks that cheaply stretch a RoPE model to 32k–128k context.</li>
</ul>
<p>Combined with FlashAttention (Ch. 14) and ring attention, modern systems routinely reach 128k–1M tokens.</p>
""",
        "papers": [
            {"title": "RoFormer: Enhanced Transformer with Rotary Position Embedding", "authors": "Su et al.", "year": 2021,
             "url": "https://arxiv.org/abs/2104.09864",
             "summary": "RoPE encodes relative position via rotation; the dominant scheme in 2025-era LMs."},
            {"title": "Train Short, Test Long: Attention with Linear Biases (ALiBi)", "authors": "Press, Smith, Lewis", "year": 2022,
             "venue": "ICLR", "url": "https://arxiv.org/abs/2108.12409",
             "summary": "Position-free attention with simple distance bias; clean extrapolation properties."},
            {"title": "YaRN: Efficient Context Window Extension", "authors": "Peng et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2309.00071",
             "summary": "Extends RoPE-trained models to ~128k with minimal fine-tuning."},
            {"title": "Lost in the Middle: How Language Models Use Long Contexts", "authors": "Liu et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2307.03172",
             "summary": "Long-context models systematically under-use middle positions. Sobering when designing RAG layouts."},
            {"title": "Ring Attention with Blockwise Transformers", "authors": "Liu, Zaharia, Abbeel", "year": 2023,
             "url": "https://arxiv.org/abs/2310.01889",
             "summary": "Distributes attention across devices; underpins Gemini 1.5's 1M-token context."},
        ],
    },
    {
        "id": 12, "part": "III. Architecture Frontiers",
        "title": "Mixture-of-Experts (MoE)",
        "summary": """
<p>An MoE layer routes each token to <b>k of N</b> expert FFNs (typically k=2). You get the parameter count of
a huge model with the FLOPs of a small one — a different point on the cost/quality Pareto.</p>
<p>Modern MoE systems (Mixtral, DeepSeek-V2/V3, Qwen3-MoE, Grok-1) report 5-10x parameter counts at similar serving
cost. Challenges: load balancing, expert collapse, training instability, and routing-as-side-channel for inference cost prediction.</p>

<h4>Routing math (top-k softmax)</h4>
<pre>
g_i = softmax(W_gate · x)        # gate logits per expert
top_k = TopK(g_i, k)              # active experts for this token
y = sum_{i in top_k} (g_i / sum top_k) * Expert_i(x)
</pre>
""",
        "papers": [
            {"title": "Outrageously Large Neural Networks: Sparsely-Gated Mixture-of-Experts", "authors": "Shazeer et al.", "year": 2017,
             "url": "https://arxiv.org/abs/1701.06538", "summary": "The modern sparse MoE design (Google Brain)."},
            {"title": "Switch Transformers: Scaling to Trillion Parameter Models", "authors": "Fedus, Zoph, Shazeer", "year": 2022,
             "venue": "JMLR", "url": "https://arxiv.org/abs/2101.03961",
             "summary": "Top-1 routing simplifies training; demonstrates trillion-parameter feasibility."},
            {"title": "GLaM: Efficient Scaling of Language Models with Mixture-of-Experts", "authors": "Du et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2112.06905",
             "summary": "1.2T-parameter MoE consuming 1/3 the energy of GPT-3 to train and 1/2 the FLOPs at inference."},
            {"title": "Mixtral of Experts", "authors": "Jiang et al.", "year": 2024, "venue": "Mistral AI",
             "url": "https://arxiv.org/abs/2401.04088",
             "summary": "8x7B sparse MoE, k=2; canonical open-weight MoE recipe."},
            {"title": "DeepSeek-V3 Technical Report", "authors": "DeepSeek-AI", "year": 2024,
             "url": "https://arxiv.org/abs/2412.19437",
             "summary": "671B MoE (37B active) with multi-head latent attention and FP8 training. Best open-weight non-trivial frontier model of late 2024."},
        ],
    },
    {
        "id": 13, "part": "III. Architecture Frontiers",
        "title": "State-Space Models: Mamba and Hybrids",
        "summary": """
<p>Self-attention is O(n²) in sequence length. <b>State-space models (SSMs)</b> like S4 and <b>Mamba</b> compute
in O(n) using a learnable recurrence. Mamba uses <i>selective</i> SSMs — input-dependent dynamics — to recover the
context-routing flexibility that attention provides.</p>
<p>In 2024-25 the field converged on <b>hybrid</b> architectures (e.g., Jamba, Samba): mostly Mamba with a few attention
layers, getting linear scaling without sacrificing in-context recall. SSMs remain less effective than attention on tasks
that require pinpoint long-range copying, but the gap is narrowing.</p>
""",
        "papers": [
            {"title": "Efficiently Modeling Long Sequences with Structured State Spaces (S4)", "authors": "Gu, Goel, Ré", "year": 2022,
             "venue": "ICLR (Outstanding Paper)", "url": "https://arxiv.org/abs/2111.00396",
             "summary": "The structured SSM that started the wave; principled long-range memory."},
            {"title": "Mamba: Linear-Time Sequence Modeling with Selective State Spaces", "authors": "Gu, Dao", "year": 2023,
             "url": "https://arxiv.org/abs/2312.00752",
             "summary": "Selective SSMs — content-dependent state — close most of the gap with attention. Highly hardware-friendly."},
            {"title": "Jamba: A Hybrid Transformer-Mamba Language Model", "authors": "Lieber et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2403.19887",
             "summary": "Practical hybrid: SSM majority + attention minority + MoE. Strong long-context throughput."},
            {"title": "An Empirical Study of Mamba-based Language Models", "authors": "Waleffe et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2406.07887",
             "summary": "NVIDIA's controlled comparison: hybrid > pure-Mamba > pure-transformer at long context."},
        ],
    },
    {
        "id": 14, "part": "III. Architecture Frontiers",
        "title": "Efficient Attention: FlashAttention and Friends",
        "summary": """
<p><b>FlashAttention</b> (Tri Dao, 2022) recasts attention as an IO-aware tiled algorithm that never materializes
the n×n attention matrix in HBM. It's not an approximation — it's exact, but wall-clock 2-4x faster and dramatically
more memory-efficient. v2 and v3 added further hardware specialization (Ampere, Hopper).</p>

<p>This single kernel is one of the most consequential systems contributions to the field — without it, today's
context lengths would be impractical.</p>
""",
        "papers": [
            {"title": "FlashAttention: Fast and Memory-Efficient Exact Attention", "authors": "Dao et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2205.14135",
             "summary": "IO-aware attention algorithm; standard in every serious training/inference stack."},
            {"title": "FlashAttention-2", "authors": "Dao", "year": 2023,
             "url": "https://arxiv.org/abs/2307.08691",
             "summary": "Better work partitioning; ~2x speedup over v1 on A100."},
            {"title": "FlashAttention-3 (Hopper)", "authors": "Shah et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2407.08608",
             "summary": "Asynchrony + low-precision (fp8) on H100; near-peak utilization for transformer inference."},
            {"title": "PagedAttention / vLLM", "authors": "Kwon et al.", "year": 2023, "venue": "SOSP",
             "url": "https://arxiv.org/abs/2309.06180",
             "summary": "OS-style paging for KV cache → 2-4x throughput at serving time. vLLM is the dominant open inference engine."},
        ],
    },

    # ============================================================
    # PART IV — POST-TRAINING & ALIGNMENT
    # ============================================================
    {
        "id": 15, "part": "IV. Post-training & Alignment",
        "title": "Instruction Tuning (SFT)",
        "summary": """
<p>Supervised fine-tuning (SFT) on instruction-response pairs converts a base completion model into a usable
assistant. It is the cheapest, most reliable alignment intervention you have. Quality of data dominates quantity:
LIMA (Zhou et al., 2023) showed 1,000 carefully curated examples can produce a strong assistant.</p>
<h4>Practical tips</h4>
<ul>
  <li>Mix held-out evals into the training mix to monitor task distribution drift.</li>
  <li>Mask the prompt tokens in the loss; train only on assistant responses.</li>
  <li>Don't over-train — 1-3 epochs typically; more usually hurts diversity.</li>
</ul>
""",
        "papers": [
            {"title": "Finetuned Language Models Are Zero-Shot Learners (FLAN)", "authors": "Wei et al.", "year": 2022, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2109.01652",
             "summary": "Multi-task instruction-tuning improves unseen-task zero-shot performance. The seed of the modern recipe."},
            {"title": "Self-Instruct: Aligning Language Models with Self-Generated Instructions", "authors": "Wang et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2212.10560",
             "summary": "Bootstraps SFT data from a small seed via the model itself; democratized instruction-tuning."},
            {"title": "LIMA: Less Is More for Alignment", "authors": "Zhou et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.11206",
             "summary": "1,000 hand-crafted SFT examples ≈ much larger RLHF systems on many evals. Quality wins."},
            {"title": "The Flan Collection: Designing Data and Methods for Effective Instruction Tuning", "authors": "Longpre et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2301.13688",
             "summary": "Best ablation of what really matters in instruction-tuning data."},
        ],
    },
    {
        "id": 16, "part": "IV. Post-training & Alignment",
        "title": "RLHF and Constitutional AI",
        "summary": """
<p><b>RLHF</b> (Christiano 2017; OpenAI's InstructGPT 2022) trains a reward model from human pairwise preferences,
then runs PPO against the LM. It produced ChatGPT and remains the gold standard when human labels are abundant
and quality matters.</p>
<p><b>Constitutional AI</b> (Anthropic, 2022) replaces most human labels with model-generated critiques against a
written constitution. Cheaper, more transparent, and the foundation of Claude's harmlessness training.</p>
""",
        "papers": [
            {"title": "Deep Reinforcement Learning from Human Preferences", "authors": "Christiano et al.", "year": 2017,
             "url": "https://arxiv.org/abs/1706.03741",
             "summary": "The original RLHF formulation. Reward model + PPO."},
            {"title": "Training language models to follow instructions with human feedback (InstructGPT)", "authors": "Ouyang et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2203.02155",
             "summary": "GPT-3 → InstructGPT via SFT + RLHF. Direct ancestor of ChatGPT."},
            {"title": "Constitutional AI: Harmlessness from AI Feedback", "authors": "Bai et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2212.08073",
             "summary": "Use the model itself to critique under a written constitution; reduces human-label dependence."},
            {"title": "Llama 2", "authors": "Touvron et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2307.09288",
             "summary": "Best public RLHF + Ghost-Attention writeup at the time. Required reading for the production recipe."},
        ],
    },
    {
        "id": 17, "part": "IV. Post-training & Alignment",
        "title": "DPO, IPO, KTO: Reward-Free Preference Optimization",
        "summary": """
<p><b>Direct Preference Optimization</b> (Rafailov et al., 2023) collapses the reward model + PPO pipeline into
a single closed-form classification loss over preference pairs. It's <i>much</i> simpler to implement, more stable,
and matches RLHF on most benchmarks. DPO and its variants (IPO, KTO, ORPO) now dominate open-source post-training.</p>

<h4>The DPO loss in one line</h4>
<pre>
L_DPO = -log σ( β · ( log π(y_w|x)/π_ref(y_w|x) − log π(y_l|x)/π_ref(y_l|x) ) )
</pre>
<p>Where (y_w, y_l) is a (winner, loser) pair, π is the policy, π_ref the SFT reference, β a temperature.</p>
""",
        "papers": [
            {"title": "Direct Preference Optimization (DPO)", "authors": "Rafailov et al.", "year": 2023, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2305.18290",
             "summary": "Reformulates RLHF as a closed-form classification objective; no reward model, no PPO."},
            {"title": "A General Theoretical Paradigm to Understand Learning from Human Preferences (IPO)", "authors": "Azar et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2310.12036",
             "summary": "Generalizes RLHF/DPO; identifies and fixes overoptimization pathologies in DPO."},
            {"title": "KTO: Model Alignment as Prospect Theoretic Optimization", "authors": "Ethayarajh et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2402.01306",
             "summary": "Works with binary thumbs-up/down labels — no pairs needed; matches DPO when pairs exist."},
            {"title": "ORPO: Monolithic Preference Optimization without Reference Model", "authors": "Hong, Lee, Thorne", "year": 2024,
             "url": "https://arxiv.org/abs/2403.07691",
             "summary": "Combines SFT and preference optimization in one loss with no reference model. Cheap and surprisingly strong."},
        ],
    },
    {
        "id": 18, "part": "IV. Post-training & Alignment",
        "title": "PEFT: LoRA, QLoRA, Adapters",
        "summary": """
<p>Full fine-tuning a 70B model needs hundreds of GB of optimizer state. <b>Parameter-efficient fine-tuning</b>
freezes the base model and trains tiny add-ons:</p>
<ul>
  <li><b>LoRA</b> (Hu et al., 2021) — low-rank update <code>ΔW = B·A</code>, typically 0.1-1% of params.</li>
  <li><b>QLoRA</b> (Dettmers et al., 2023) — base model quantized to 4-bit; LoRA in fp16. Fine-tune 65B on a single 48GB GPU.</li>
  <li><b>Adapters</b> (Houlsby et al., 2019) — bottleneck modules inserted in each layer; pre-LoRA classic.</li>
</ul>
<p>Practical default in 2026: <b>QLoRA + DPO</b> on a strong open base. You'll spend more time on data than on optimization.</p>
""",
        "papers": [
            {"title": "LoRA: Low-Rank Adaptation of Large Language Models", "authors": "Hu et al.", "year": 2022, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2106.09685",
             "summary": "Inject low-rank trainable matrices into attention projections. Now ubiquitous."},
            {"title": "QLoRA: Efficient Finetuning of Quantized LLMs", "authors": "Dettmers et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.14314",
             "summary": "4-bit NormalFloat + paged optimizers + LoRA. Democratized large-model finetuning."},
            {"title": "Parameter-Efficient Transfer Learning for NLP (Adapters)", "authors": "Houlsby et al.", "year": 2019, "venue": "ICML",
             "url": "https://arxiv.org/abs/1902.00751",
             "summary": "Original adapter modules. Predates LoRA."},
            {"title": "DoRA: Weight-Decomposed Low-Rank Adaptation", "authors": "Liu et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2402.09353",
             "summary": "Decomposes weights into magnitude × direction; closes most of the LoRA→full-FT gap."},
        ],
    },

    # ============================================================
    # PART V — REASONING & AGENTS
    # ============================================================
    {
        "id": 19, "part": "V. Reasoning & Agents",
        "title": "Chain-of-Thought and Self-Consistency",
        "summary": """
<p>Asking a model to "think step by step" (Wei et al., 2022) materially improves multi-step reasoning at
sufficient scale. <b>Self-consistency</b> samples many CoTs and majority-votes the answer — robust and cheap.</p>
<p>Subsequent research (least-to-most, plan-and-solve, tree-of-thoughts, graph-of-thoughts) extended the basic
idea into structured search.</p>
""",
        "papers": [
            {"title": "Chain-of-Thought Prompting Elicits Reasoning", "authors": "Wei et al.", "year": 2022, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2201.11903",
             "summary": "The 'let's think step by step' paper; transforms math/commonsense reasoning above ~60B."},
            {"title": "Self-Consistency Improves Chain of Thought Reasoning", "authors": "Wang et al.", "year": 2023,
             "venue": "ICLR", "url": "https://arxiv.org/abs/2203.11171",
             "summary": "Sample many reasoning paths, majority-vote. Simple, almost free, robust."},
            {"title": "Tree of Thoughts: Deliberate Problem Solving with LLMs", "authors": "Yao et al.", "year": 2023,
             "venue": "NeurIPS", "url": "https://arxiv.org/abs/2305.10601",
             "summary": "Generalizes CoT to a search over partial solutions. Useful for puzzles, planning."},
            {"title": "Large Language Models are Zero-Shot Reasoners", "authors": "Kojima et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2205.11916",
             "summary": "'Let's think step by step.' One sentence, often a 10-50 point gain."},
        ],
    },
    {
        "id": 20, "part": "V. Reasoning & Agents",
        "title": "ReAct, Tool Use, and Function Calling",
        "summary": """
<p><b>ReAct</b> (Yao et al., 2023) interleaves <i>Thought → Action → Observation</i> traces, letting the model use
external tools (web search, calculators, APIs). Modern frontier models expose this via "function calling" /
"tool use" APIs (OpenAI 2023, Anthropic Claude tool-use, Gemini).</p>
<p>For practitioners: tool use turns an LM into a reasoning core that can act on real systems. The hardest part is
not the prompt — it's tool design (idempotent, well-typed, cheap-to-fail) and observability of the agent loop.</p>
""",
        "papers": [
            {"title": "ReAct: Synergizing Reasoning and Acting in Language Models", "authors": "Yao et al.", "year": 2023,
             "venue": "ICLR", "url": "https://arxiv.org/abs/2210.03629",
             "summary": "Interleaves reasoning and tool actions. Foundation of every modern agent loop."},
            {"title": "Toolformer: Language Models Can Teach Themselves to Use Tools", "authors": "Schick et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2302.04761",
             "summary": "Self-supervised tool insertion via perplexity reduction; trains the model to call APIs natively."},
            {"title": "Gorilla: Large Language Model Connected with Massive APIs", "authors": "Patil et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.15334",
             "summary": "API-call generation grounded in retrieval; reduces hallucinated function names."},
            {"title": "Reflexion: Language Agents with Verbal Reinforcement Learning", "authors": "Shinn et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2303.11366",
             "summary": "Agent self-reflection between trials; cheap iterative improvement without weight updates."},
        ],
    },
    {
        "id": 21, "part": "V. Reasoning & Agents",
        "title": "Agentic Workflows: Planning, Memory, Multi-Agent",
        "summary": """
<p>An "agent" in 2026 is typically a loop: <i>plan → call tools → observe → update memory → repeat</i>. The interesting
architectural questions are about state — episodic memory, scratchpads, retrieval over past traces — and about
multi-agent coordination (debate, hierarchical decomposition).</p>
<p>Important sober result: multi-agent systems often <i>don't</i> outperform a single strong model with a careful prompt
(Cemri et al., 2024). The win usually comes from giving the agent better tools, not more agents.</p>
""",
        "papers": [
            {"title": "Generative Agents: Interactive Simulacra of Human Behavior", "authors": "Park et al.", "year": 2023, "venue": "UIST",
             "url": "https://arxiv.org/abs/2304.03442",
             "summary": "25 agents in a simulated town with memory, reflection, planning. Influential agent-architecture paper."},
            {"title": "Voyager: An Open-Ended Embodied Agent with LLMs", "authors": "Wang et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.16291",
             "summary": "Lifelong skill library that grows; strong baseline for open-ended agent research (Minecraft)."},
            {"title": "AutoGen / Multi-Agent Conversation Framework", "authors": "Wu et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2308.08155",
             "summary": "Microsoft framework for multi-agent LLM applications; pragmatic and widely used."},
            {"title": "Why Do Multi-Agent LLM Systems Fail?", "authors": "Cemri et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2503.13657",
             "summary": "Empirical study: most multi-agent gains evaporate under controlled comparison. Important counterweight to hype."},
        ],
    },
    {
        "id": 22, "part": "V. Reasoning & Agents",
        "title": "Inference-Time Compute and Reasoning Models",
        "summary": """
<p>The big 2024-25 shift: <b>train models to spend more tokens thinking before answering</b>. OpenAI's <b>o1</b>
and <b>o3</b> series, DeepSeek's <b>R1</b>, and Anthropic's <b>extended thinking</b> mode all trade latency for
correctness on hard reasoning, math, and code tasks.</p>
<p>Two key results:</p>
<ul>
  <li><b>Snell et al. (2024)</b>: scaling test-time compute can outperform scaling parameters for hard problems.</li>
  <li><b>DeepSeek-R1 (2025)</b>: pure RL with verifiable rewards (correct/incorrect on math/code) elicits long
      reasoning chains <i>from a base model with no SFT data</i>. Reproducibly trainable in the open.</li>
</ul>
""",
        "papers": [
            {"title": "Scaling LLM Test-Time Compute Optimally", "authors": "Snell et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2408.03314",
             "summary": "Compute-matched test-time vs train-time scaling. Test-time wins on hard problems."},
            {"title": "OpenAI o1 System Card", "authors": "OpenAI", "year": 2024,
             "url": "https://cdn.openai.com/o1-system-card.pdf",
             "summary": "Public writeup of o1's reasoning approach + safety evaluations; light on architecture, sets the paradigm. (Direct PDF on cdn.openai.com.)"},
            {"title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", "authors": "DeepSeek-AI", "year": 2025,
             "url": "https://arxiv.org/abs/2501.12948",
             "summary": "Open recipe for reasoning models: GRPO over verifiable rewards. The most important open paper of 2025."},
            {"title": "Let's Verify Step by Step", "authors": "Lightman et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.20050",
             "summary": "Process reward models — supervise each step of a CoT, not just the final answer."},
        ],
    },

    # ============================================================
    # PART VI — RETRIEVAL & GROUNDING
    # ============================================================
    {
        "id": 23, "part": "VI. Retrieval & Grounding",
        "title": "Retrieval-Augmented Generation (RAG)",
        "summary": """
<p>RAG = retrieve relevant documents → put them in the prompt → generate. Unfashionable in 2024 hype-cycles but
indispensable in production: it grounds answers, scopes data freshness, and keeps proprietary content out of weights.</p>
<h4>Production RAG checklist</h4>
<ol>
  <li>Chunk smartly (hierarchical, semantic — not arbitrary 512-token slices).</li>
  <li>Hybrid retrieval — dense (BM25) + sparse + reranker.</li>
  <li>Decontaminate, deduplicate, attribute.</li>
  <li>Evaluate with RAG-aware metrics (faithfulness, context relevance), not just answer accuracy.</li>
  <li>Add a "did the retrieval find the right thing?" guard before "did the model answer correctly?"</li>
</ol>
""",
        "papers": [
            {"title": "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", "authors": "Lewis et al.", "year": 2020, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2005.11401", "summary": "The original RAG paper. Still worth re-reading."},
            {"title": "REALM: Retrieval-Augmented Language Model Pre-Training", "authors": "Guu et al.", "year": 2020,
             "url": "https://arxiv.org/abs/2002.08909", "summary": "Pre-RAG retrieval-pretraining; conceptually formative."},
            {"title": "Atlas: Few-shot Learning with Retrieval Augmented LMs", "authors": "Izacard et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2208.03299",
             "summary": "Strong few-shot learner via retrieval; the recipe many production RAG systems imitate."},
            {"title": "Self-RAG: Self-Reflective Retrieval", "authors": "Asai et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2310.11511",
             "summary": "Model decides when/what to retrieve and critiques its own outputs; strong on long-form QA."},
            {"title": "Lost in the Middle (revisit)", "authors": "Liu et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2307.03172",
             "summary": "Bookend retrieved passages with the most important ones — empirically robust."},
        ],
    },
    {
        "id": 24, "part": "VI. Retrieval & Grounding",
        "title": "Embeddings, Vector DBs, Rerankers",
        "summary": """
<p>Embedding models project text into a fixed-dimensional vector space where cosine similarity ≈ semantic similarity.
The <b>MTEB</b> leaderboard tracks the state of the art (BGE, E5, GTE, NV-Embed, then Cohere/OpenAI/Voyage).</p>
<p>Practical stack:</p>
<ul>
  <li>Embedder (BGE/E5/Voyage) → ANN index (FAISS, ScaNN, HNSW in Qdrant/Milvus/Weaviate/pgvector).</li>
  <li>Cross-encoder reranker (BGE-reranker, Cohere Rerank) on top-k candidates.</li>
  <li>For long docs: <b>ColBERT</b>-style late interaction beats single-vector when latency permits.</li>
</ul>
""",
        "papers": [
            {"title": "Dense Passage Retrieval (DPR)", "authors": "Karpukhin et al.", "year": 2020, "venue": "EMNLP",
             "url": "https://arxiv.org/abs/2004.04906", "summary": "The dual-encoder retrieval baseline that everything else iterates on."},
            {"title": "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction", "authors": "Khattab, Zaharia", "year": 2020, "venue": "SIGIR",
             "url": "https://arxiv.org/abs/2004.12832",
             "summary": "Late-interaction retrieval; recall of cross-encoders at near-bi-encoder cost."},
            {"title": "MTEB: Massive Text Embedding Benchmark", "authors": "Muennighoff et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2210.07316",
             "summary": "The standard benchmark suite. Always check MTEB before adopting an embedding model."},
            {"title": "Matryoshka Representation Learning", "authors": "Kusupati et al.", "year": 2022, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2205.13147",
             "summary": "Train embeddings so that prefixes are themselves valid embeddings → nested compression for serving."},
        ],
    },

    # ============================================================
    # PART VII — SLM-SPECIFIC
    # ============================================================
    {
        "id": 25, "part": "VII. Small Language Models",
        "title": "Why SLMs Now: Definition, Use Cases, Economics",
        "summary": """
<p>"Small" is relative. In 2026 a Small Language Model (SLM) is roughly <b>0.5B–10B parameters</b> — runnable on a
laptop or phone, deployable at the edge, fine-tunable on a single GPU. They power on-device assistants, latency-sensitive
production paths, agentic sub-tasks, and privacy-preserving deployments.</p>

<h4>Why an SVP cares</h4>
<ul>
  <li>Inference cost can be 10-100x lower than frontier models.</li>
  <li>Privacy: data never leaves the device or VPC.</li>
  <li>Predictable latency at the long tail.</li>
  <li>Specialization beats generality on narrow domains (e.g., one customer's API surface).</li>
</ul>

<h4>Open question</h4>
<p>Are SLMs the right substrate for agentic systems (one big general model + many small specialists)?
Belcak et al. (2024) make exactly this argument; see Ch. 27.</p>
""",
        "papers": [
            {"title": "A Survey of Small Language Models", "authors": "Lu et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2410.20011",
             "summary": "Comprehensive 2024 survey: capabilities, training, on-device deployment, datasets, evaluation."},
            {"title": "Small Language Models: Survey, Measurements, and Insights", "authors": "Lu et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2409.15790",
             "summary": "Hardware-grounded measurements on real devices; the most useful empirical reference for SLM deployment."},
            {"title": "Small Language Models are the Future of Agentic AI", "authors": "Belcak et al. (NVIDIA)", "year": 2024,
             "url": "https://arxiv.org/abs/2506.02153",
             "summary": "Argues most agent sub-steps don't need a frontier model; a manifesto for SLM-first agent design."},
        ],
    },
    {
        "id": 26, "part": "VII. Small Language Models",
        "title": "The Phi Series and 'Textbooks Are All You Need'",
        "summary": """
<p>Microsoft Research's <b>Phi</b> series argued that <i>data quality dominates scale</i>: with carefully curated
"textbook-quality" synthetic data, a 1.3B model can beat 7B contemporaries on coding and reasoning. Phi-2, Phi-3,
and Phi-4 (mini/medium/multimodal) made this practical: state-of-the-art tasks running at SLM cost.</p>
<p>The key technique is generating <i>diverse, pedagogically-structured</i> synthetic data with a stronger teacher
model, filtered for difficulty and quality. This recipe is now standard across SLM teams (Microsoft, Apple, Google).</p>
""",
        "papers": [
            {"title": "Textbooks Are All You Need (phi-1)", "authors": "Gunasekar et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2306.11644",
             "summary": "1.3B code model trained on textbook-quality synthetic data; beats much larger models on HumanEval."},
            {"title": "Textbooks Are All You Need II: phi-1.5 technical report", "authors": "Li et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2309.05463",
             "summary": "Extends to general reasoning; small model emergent capabilities discussion."},
            {"title": "Phi-3 Technical Report", "authors": "Abdin et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2404.14219",
             "summary": "3.8B model trained on heavily filtered web + synthetic data; runs on a phone."},
            {"title": "Phi-4 Technical Report", "authors": "Abdin et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2412.08905",
             "summary": "14B SLM with training-data-centric design; strong on reasoning evals."},
        ],
    },
    {
        "id": 27, "part": "VII. Small Language Models",
        "title": "Open SLM Families: Llama-3, Gemma, Qwen, Mistral, SmolLM",
        "summary": """
<p>The 2024-26 SLM ecosystem is dominated by a few open families:</p>
<ul>
  <li><b>Llama 3.x / 4</b> (Meta) — 1B / 3B / 8B / 70B; reference quality.</li>
  <li><b>Gemma 2 / 3</b> (Google) — 2B / 9B / 27B; strong multilingual; Gemma 3 adds vision.</li>
  <li><b>Qwen 2.5 / 3</b> (Alibaba) — 0.5B → 72B; excellent at math, code, multilingual; Qwen 2.5-Coder is a top open coder.</li>
  <li><b>Mistral / Ministral / Mixtral</b> — efficient dense + MoE.</li>
  <li><b>SmolLM2 / SmolLM3</b> (Hugging Face) — 135M / 360M / 1.7B / 3B fully open recipe (data, code, weights).</li>
  <li><b>Apple Intelligence Foundation Models</b> — ~3B on-device; technical report worth reading for production constraints.</li>
</ul>
""",
        "papers": [
            {"title": "The Llama 3 Herd of Models", "authors": "Meta AI", "year": 2024,
             "url": "https://arxiv.org/abs/2407.21783",
             "summary": "92-page recipe: data, scaling, post-training, multimodal. The most-cited open frontier-class paper."},
            {"title": "Gemma 2 Technical Report", "authors": "Gemma Team", "year": 2024,
             "url": "https://arxiv.org/abs/2408.00118",
             "summary": "Knowledge distillation + soft attention logit capping; strong 9B/27B SLMs."},
            {"title": "Qwen2.5 Technical Report", "authors": "Qwen Team", "year": 2024,
             "url": "https://arxiv.org/abs/2412.15115",
             "summary": "Sweep from 0.5B to 72B; strong multilingual + coding subseries."},
            {"title": "SmolLM2: When Smol Goes Big", "authors": "Allal et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2502.02737",
             "summary": "Fully open 135M-1.7B family with curated training mix; excellent baseline for SLM research."},
            {"title": "Apple Intelligence Foundation Language Models", "authors": "Apple", "year": 2024,
             "url": "https://arxiv.org/abs/2407.21075",
             "summary": "On-device 3B model with adapter-based personalization; production constraints articulated clearly."},
        ],
    },
    {
        "id": 28, "part": "VII. Small Language Models",
        "title": "Quantization: GPTQ, AWQ, GGUF, FP8/INT4",
        "summary": """
<p>Quantization is the bridge from research to deployment. Modern weight-only schemes:</p>
<ul>
  <li><b>GPTQ</b> — second-order error minimization; 4-bit, near-lossless on most LMs.</li>
  <li><b>AWQ</b> — activation-aware; preserves salient channels at higher precision.</li>
  <li><b>GGUF / llama.cpp</b> — practitioner format covering 2/3/4/5/6/8-bit, K-quants, IQ-quants.</li>
  <li><b>SmoothQuant</b> — migrate activation outliers into weights for W8A8 inference.</li>
  <li><b>FP8 (H100/B200) and INT4 + KV-cache compression</b> dominate production serving in 2025-26.</li>
</ul>
<p>Watch for benchmark sensitivity: a model "lossless" on perplexity can degrade noticeably on chain-of-thought
math at <8-bit. Always re-eval at deployment precision.</p>
""",
        "papers": [
            {"title": "GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers", "authors": "Frantar et al.", "year": 2023, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2210.17323", "summary": "Second-order, layer-wise; the canonical 4-bit weight-only quantizer."},
            {"title": "AWQ: Activation-aware Weight Quantization for LLM Compression", "authors": "Lin et al.", "year": 2024, "venue": "MLSys",
             "url": "https://arxiv.org/abs/2306.00978", "summary": "Protects salient channels; near-lossless 4-bit and fast on consumer GPUs."},
            {"title": "SmoothQuant: Accurate and Efficient Post-Training Quantization for LLMs", "authors": "Xiao et al.", "year": 2023,
             "venue": "ICML", "url": "https://arxiv.org/abs/2211.10438",
             "summary": "Shifts activation outliers into weights for W8A8 inference; production-friendly."},
            {"title": "LLM.int8(): 8-bit Matrix Multiplication", "authors": "Dettmers et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2208.07339", "summary": "First widely-used 8-bit inference for LLMs; introduces outlier handling."},
        ],
        "extras": [{"label": "llama.cpp / GGUF", "url": "https://github.com/ggerganov/llama.cpp"}],
    },
    {
        "id": 29, "part": "VII. Small Language Models",
        "title": "Knowledge Distillation and Model Compression",
        "summary": """
<p>Distillation trains a small student to imitate a large teacher's distributions, hidden states, or behavior.
Combined with quantization and pruning, it's the backbone of every successful SLM family.</p>
<h4>Modes</h4>
<ul>
  <li><b>Soft-label KL distillation</b> (Hinton 2015) — match the teacher's logits.</li>
  <li><b>Hidden-state matching</b> (DistilBERT, MiniLM).</li>
  <li><b>Synthetic-data SFT</b> — let the teacher write the training set (Alpaca, Phi, Gemma 2).</li>
  <li><b>Reasoning distillation</b> — distill long-CoT traces from o1/R1-style teachers into compact students.</li>
</ul>
""",
        "papers": [
            {"title": "Distilling the Knowledge in a Neural Network", "authors": "Hinton, Vinyals, Dean", "year": 2015,
             "url": "https://arxiv.org/abs/1503.02531",
             "summary": "Soft-label distillation. Origin story of modern compression."},
            {"title": "DistilBERT", "authors": "Sanh et al.", "year": 2019,
             "url": "https://arxiv.org/abs/1910.01108",
             "summary": "60% smaller, 60% faster, 97% of BERT performance via triple-loss distillation."},
            {"title": "Alpaca: An Instruction-following LLaMA Model", "authors": "Taori et al.", "year": 2023, "venue": "Stanford CRFM",
             "url": "https://crfm.stanford.edu/2023/03/13/alpaca.html",
             "summary": "Distill GPT-3.5 instruction-following into 7B Llama with 52K examples and ~$600. Sparked the open chatbot wave."},
            {"title": "MINILLM: Knowledge Distillation of Large Language Models", "authors": "Gu et al.", "year": 2024, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2306.08543",
             "summary": "Reverse KL distillation; principled handling of mode-seeking vs mode-covering for generative students."},
        ],
    },
    {
        "id": 30, "part": "VII. Small Language Models",
        "title": "On-Device Inference: Speculative Decoding, KV Cache, MLC",
        "summary": """
<p>SLM deployment is a systems problem. Pillars:</p>
<ul>
  <li><b>Speculative decoding</b> (Leviathan; Chen et al.) — run a tiny draft model, let the big model verify.
      2-3x speedups on real workloads.</li>
  <li><b>Medusa, EAGLE</b> — draft heads inside the same model; even cheaper.</li>
  <li><b>KV-cache compression</b> — quantize KV; sliding-window attention; H2O / StreamingLLM eviction policies.</li>
  <li><b>Compiler stacks</b> — MLC-LLM, llama.cpp, MLX (Apple), TensorRT-LLM.</li>
</ul>
""",
        "papers": [
            {"title": "Fast Inference from Transformers via Speculative Decoding", "authors": "Leviathan, Kalman, Matias", "year": 2023, "venue": "ICML",
             "url": "https://arxiv.org/abs/2211.17192", "summary": "Speculative decoding: lossless 2-3x speedup."},
            {"title": "Accelerating Large Language Model Decoding with Speculative Sampling", "authors": "Chen et al. (DeepMind)", "year": 2023,
             "url": "https://arxiv.org/abs/2302.01318", "summary": "Concurrent formulation; rigorous correctness analysis."},
            {"title": "Medusa: Simple LLM Inference Acceleration via Multiple Decoding Heads", "authors": "Cai et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2401.10774",
             "summary": "Add small prediction heads; no separate draft model needed."},
            {"title": "Efficient Streaming Language Models with Attention Sinks (StreamingLLM)", "authors": "Xiao et al.", "year": 2024, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2309.17453",
             "summary": "Keep the first few tokens always in KV; trivially extends context with sliding window."},
        ],
        "extras": [
            {"label": "MLC-LLM", "url": "https://github.com/mlc-ai/mlc-llm"},
            {"label": "TensorRT-LLM", "url": "https://github.com/NVIDIA/TensorRT-LLM"},
        ],
    },

    # ============================================================
    # PART VIII — MULTIMODAL
    # ============================================================
    {
        "id": 31, "part": "VIII. Multimodal",
        "title": "Vision-Language Models: CLIP, Flamingo, LLaVA",
        "summary": """
<p>Multimodal LMs feed images (and audio, video) into a language backbone. The dominant recipe:
encode the image with a Vision Transformer (often CLIP-pretrained), project into the LM's token space,
and finetune jointly. <b>LLaVA</b> (2023) made this practical at small scale; <b>Flamingo</b> (2022)
established the gated cross-attention approach.</p>
""",
        "papers": [
            {"title": "Learning Transferable Visual Models From Natural Language Supervision (CLIP)", "authors": "Radford et al.", "year": 2021,
             "url": "https://arxiv.org/abs/2103.00020",
             "summary": "Contrastive image-text pretraining. The vision encoder of choice for VLMs."},
            {"title": "Flamingo: a Visual Language Model for Few-Shot Learning", "authors": "Alayrac et al. (DeepMind)", "year": 2022,
             "url": "https://arxiv.org/abs/2204.14198",
             "summary": "Gated cross-attention from a frozen LM into vision features."},
            {"title": "Visual Instruction Tuning (LLaVA)", "authors": "Liu et al.", "year": 2023, "venue": "NeurIPS Oral",
             "url": "https://arxiv.org/abs/2304.08485",
             "summary": "Simple, reproducible projector-based VLM. The default starting point for open VLM work."},
            {"title": "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and LLMs", "authors": "Li et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2301.12597", "summary": "Q-Former bridge between frozen vision and language; influential design."},
            {"title": "An Image is Worth 16x16 Words (ViT)", "authors": "Dosovitskiy et al.", "year": 2021, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2010.11929", "summary": "The vision transformer. Background reading for any VLM work."},
        ],
    },
    {
        "id": 32, "part": "VIII. Multimodal",
        "title": "Image / Video / Audio Generation: Diffusion in the LM Era",
        "summary": """
<p>Generation in the modern stack is dominated by <b>diffusion</b> (Ho et al., 2020) and increasingly
<b>flow matching</b> (Lipman et al., 2023). DALL·E 2/3, Stable Diffusion, Imagen, Sora, Veo — all use a
text encoder (often a frozen LM) to condition a denoising diffusion / latent diffusion model.</p>
<p>For audio: <b>AudioLM</b>, <b>MusicLM</b>, and OpenAI's Whisper / Voice all show that the same
"discrete-tokens-on-a-transformer" recipe transfers to speech and music.</p>
""",
        "papers": [
            {"title": "Denoising Diffusion Probabilistic Models", "authors": "Ho, Jain, Abbeel", "year": 2020, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2006.11239", "summary": "Modern formulation of diffusion. Foundation of contemporary generative models."},
            {"title": "High-Resolution Image Synthesis with Latent Diffusion Models (Stable Diffusion)", "authors": "Rombach et al.", "year": 2022, "venue": "CVPR",
             "url": "https://arxiv.org/abs/2112.10752", "summary": "Diffusion in latent space; made open-weights image generation practical."},
            {"title": "Scalable Diffusion Models with Transformers (DiT)", "authors": "Peebles, Xie", "year": 2023, "venue": "ICCV",
             "url": "https://arxiv.org/abs/2212.09748", "summary": "Replaces UNet with a transformer; underpins Sora and Stable Diffusion 3."},
            {"title": "Robust Speech Recognition via Large-Scale Weak Supervision (Whisper)", "authors": "Radford et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2212.04356",
             "summary": "Open multilingual ASR. The de-facto baseline for speech-to-text."},
            {"title": "Flow Matching for Generative Modeling", "authors": "Lipman et al.", "year": 2023, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2210.02747",
             "summary": "Continuous-time generative training; cleaner alternative to diffusion. Powers Stable Diffusion 3 and beyond."},
        ],
    },
    {
        "id": 33, "part": "VIII. Multimodal",
        "title": "Native Multimodal Models: GPT-4o, Gemini, Claude 3+",
        "summary": """
<p>2024-25 brought "natively multimodal" frontier models: GPT-4o, Gemini 1.5/2.x, Claude 3/4. They share three
properties: (1) ingest text + images + audio + video in one prompt, (2) very long context (128k–10M), (3) often
also <i>generate</i> across modalities. Understanding their capabilities and failure modes is now
table-stakes for AI practitioners.</p>
""",
        "papers": [
            {"title": "Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context", "authors": "Google DeepMind", "year": 2024,
             "url": "https://arxiv.org/abs/2403.05530",
             "summary": "MoE + ring attention for 1M+ token context. Includes needle-in-a-haystack and multimodal evals."},
            {"title": "GPT-4o System Card", "authors": "OpenAI", "year": 2024,
             "url": "https://cdn.openai.com/gpt-4o-system-card.pdf",
             "summary": "Native audio/text/vision unified model. Heavy on safety evaluation, light on architecture. (Direct PDF on cdn.openai.com.)"},
            {"title": "The Claude 3 Model Family: Opus, Sonnet, Haiku", "authors": "Anthropic", "year": 2024,
             "url": "https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf",
             "summary": "Vision + long context; strong agentic + tool-use baseline. Solid model card."},
        ],
    },

    # ============================================================
    # PART IX — EVALUATION & BENCHMARKS
    # ============================================================
    {
        "id": 34, "part": "IX. Evaluation",
        "title": "Benchmarks: MMLU, BIG-Bench, HELM, GPQA, MATH",
        "summary": """
<p>Modern benchmarks span breadth (<b>MMLU</b> across 57 subjects), reasoning depth (<b>GPQA</b>, expert-written
PhD-level), math (<b>MATH</b>, AIME, FrontierMath), and code (<b>HumanEval</b>, <b>MBPP</b>, SWE-bench).
<b>HELM</b> (Stanford) advocates holistic, multi-metric evaluation; the <b>Open LLM Leaderboard 2</b> is the
practical reference for open-weights models.</p>
<p>Important: most popular benchmarks are now contaminated. Always pair an old benchmark with a recent contamination-free one
(e.g., MMLU-Pro 2024, GPQA-Diamond, LiveCodeBench, AIME 2024+).</p>
""",
        "papers": [
            {"title": "Measuring Massive Multitask Language Understanding (MMLU)", "authors": "Hendrycks et al.", "year": 2021,
             "venue": "ICLR", "url": "https://arxiv.org/abs/2009.03300", "summary": "57-subject knowledge benchmark; the most-quoted single number in LM papers."},
            {"title": "Beyond the Imitation Game (BIG-Bench)", "authors": "Srivastava et al.", "year": 2023, "venue": "TMLR",
             "url": "https://arxiv.org/abs/2206.04615", "summary": "204-task collaboratively-built benchmark; great for diversity."},
            {"title": "Holistic Evaluation of Language Models (HELM)", "authors": "Liang et al.", "year": 2022, "venue": "TMLR",
             "url": "https://arxiv.org/abs/2211.09110",
             "summary": "Multi-metric (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency). The right way to evaluate."},
            {"title": "GPQA: A Graduate-Level Google-Proof Q&A Benchmark", "authors": "Rein et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2311.12022",
             "summary": "PhD-written questions even Google-augmented humans struggle with. Headline reasoning benchmark."},
            {"title": "Measuring Mathematical Problem Solving with the MATH Dataset", "authors": "Hendrycks et al.", "year": 2021,
             "url": "https://arxiv.org/abs/2103.03874", "summary": "Competition math; canonical reasoning eval."},
        ],
    },
    {
        "id": 35, "part": "IX. Evaluation",
        "title": "LM-as-Judge, Arena, and Pairwise Eval",
        "summary": """
<p>For open-ended generation, automated metrics (BLEU, ROUGE) are weak. <b>LMSYS Chatbot Arena</b> uses crowdsourced
pairwise human votes; <b>MT-Bench</b> uses an LM judge. Both are influential, both have known issues (length bias,
position bias, judge-model preference for its own family). Read Zheng et al. for the standard caveats and
de-biasing techniques.</p>
""",
        "papers": [
            {"title": "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", "authors": "Zheng et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2306.05685",
             "summary": "Establishes LM-judge methodology, identifies biases, validates against human ranking."},
            {"title": "Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference", "authors": "Chiang et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2403.04132",
             "summary": "Live leaderboard methodology; the paper behind lmarena.ai."},
            {"title": "AlpacaEval", "authors": "Li et al.", "year": 2023, "venue": "Stanford",
             "url": "https://github.com/tatsu-lab/alpaca_eval",
             "summary": "Length-controlled LM-judge; cheap iteration during post-training."},
        ],
    },

    # ============================================================
    # PART X — AI SAFETY & ALIGNMENT
    # ============================================================
    {
        "id": 36, "part": "X. AI Safety & Alignment",
        "title": "AI Safety: Concrete Problems and Catastrophic Risks",
        "summary": """
<p>"Safety" spans many concerns: present-day misuse (bio/cyber uplift), bias and toxicity, autonomy/control,
deception, and longer-term catastrophic-risk arguments. The CS practitioner should hold both timelines in view —
near-term harms are real <i>now</i>, long-term concerns deserve serious attention without being hand-waved.</p>
<h4>Recommended starting set</h4>
<ul>
  <li>Amodei et al., "Concrete Problems in AI Safety" (2016) — taxonomy that still holds.</li>
  <li>Hendrycks et al., "An Overview of Catastrophic AI Risks" (2023) — clean modern survey.</li>
  <li>Anthropic's <b>Responsible Scaling Policy</b> and OpenAI's <b>Preparedness Framework</b> for industry practice.</li>
</ul>
""",
        "papers": [
            {"title": "Concrete Problems in AI Safety", "authors": "Amodei, Olah, et al.", "year": 2016,
             "url": "https://arxiv.org/abs/1606.06565",
             "summary": "Reward hacking, distributional shift, scalable oversight, safe exploration. Still the canonical primer."},
            {"title": "An Overview of Catastrophic AI Risks", "authors": "Hendrycks, Mazeika, Woodside", "year": 2023,
             "url": "https://arxiv.org/abs/2306.12001",
             "summary": "Misuse, AI race, organizational risks, rogue AIs. Best modern executive-summary survey."},
            {"title": "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training", "authors": "Hubinger et al. (Anthropic)", "year": 2024,
             "url": "https://arxiv.org/abs/2401.05566",
             "summary": "Deceptive backdoors survive standard safety training. A canonical empirical safety result."},
            {"title": "Foundational Challenges in Assuring Alignment and Safety of LLMs", "authors": "Anwar, Saparov, Bengio, et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2404.09932", "summary": "Comprehensive 200+ page survey of open safety problems with concrete research directions."},
        ],
        "extras": [
            {"label": "Anthropic Responsible Scaling Policy", "url": "https://www.anthropic.com/news/anthropics-responsible-scaling-policy"},
            {"label": "OpenAI Preparedness Framework (PDF)", "url": "https://cdn.openai.com/openai-preparedness-framework-beta.pdf"},
        ],
    },
    {
        "id": 37, "part": "X. AI Safety & Alignment",
        "title": "Red Teaming, Jailbreaks, and Robustness",
        "summary": """
<p>An aligned model is not a robust model. Adversarial prompts, gradient-based attacks (GCG), many-shot jailbreaks,
and prompt-injection in tool-use settings remain unsolved. Practitioners should:</p>
<ul>
  <li>Maintain an internal red-team and rotating attack library.</li>
  <li>Treat prompt-injection as a <b>security</b> problem (untrusted retrieved/tool output), not just an alignment one.</li>
  <li>Use defense-in-depth: input filters, output filters, and least-privilege tool design.</li>
</ul>
""",
        "papers": [
            {"title": "Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG)", "authors": "Zou et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2307.15043",
             "summary": "Gradient-based suffix attacks transfer across closed and open models. Foundational adversarial result."},
            {"title": "Many-shot Jailbreaking", "authors": "Anil et al. (Anthropic)", "year": 2024,
             "url": "https://www.anthropic.com/research/many-shot-jailbreaking",
             "summary": "Long context is itself an attack surface. Inverse-scaling failure mode."},
            {"title": "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection", "authors": "Greshake et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2302.12173",
             "summary": "Indirect prompt injection attacks; foundational result for tool-use security."},
            {"title": "Red Teaming Language Models with Language Models", "authors": "Perez et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2202.03286", "summary": "Automate red-teaming with another LM. Now a standard internal practice."},
        ],
    },
    {
        "id": 38, "part": "X. AI Safety & Alignment",
        "title": "Hallucination and Factuality",
        "summary": """
<p>LMs confabulate. Surveys (Huang et al., 2023) categorize input-conflicting, context-conflicting, and
fact-conflicting hallucinations. Mitigations: RAG (Ch. 23), self-consistency (Ch. 19), abstention training,
and verifier/critic models. <b>SelfCheckGPT</b> and <b>FActScore</b> are useful evaluators.</p>
<p>Honest framing for an executive: hallucination is <i>reduced</i>, not <i>eliminated</i>, by current techniques.
Treat any LM output that informs a customer-facing decision as needing grounding + verification.</p>
""",
        "papers": [
            {"title": "A Survey on Hallucination in Large Language Models", "authors": "Huang et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2311.05232",
             "summary": "Comprehensive taxonomy + mitigations. Best one-stop reference."},
            {"title": "SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection", "authors": "Manakul, Liusie, Gales", "year": 2023,
             "url": "https://arxiv.org/abs/2303.08896",
             "summary": "Sample multiple completions; inconsistency ≈ hallucination. Cheap and surprisingly effective."},
            {"title": "FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation", "authors": "Min et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2305.14251",
             "summary": "Decompose responses into atomic claims; score each. Standard factuality eval."},
        ],
    },
    {
        "id": 39, "part": "X. AI Safety & Alignment",
        "title": "Interpretability and Mechanistic Understanding",
        "summary": """
<p>Mechanistic interpretability tries to reverse-engineer what computation a model implements.
2023-25 milestones: <b>induction heads</b> (Olsson et al.), <b>features as directions</b> (Elhage et al.),
and the dramatic <b>Sparse Autoencoders</b> result (Anthropic, 2024) — extracting millions of
human-interpretable features from a frontier model's residual stream.</p>
<p>For practitioners: SAEs and steering vectors are starting to enable <i>controllable</i> deployment —
suppressing specific failure modes, steering tone, or adding structured policy without retraining.</p>
""",
        "papers": [
            {"title": "A Mathematical Framework for Transformer Circuits", "authors": "Elhage, Nanda et al. (Anthropic)", "year": 2021,
             "url": "https://transformer-circuits.pub/2021/framework/index.html",
             "summary": "Interprets attention-only transformers as compositions of QK and OV circuits. Foundational."},
            {"title": "In-context Learning and Induction Heads", "authors": "Olsson et al.", "year": 2022,
             "url": "https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html",
             "summary": "Identifies the circuit responsible for in-context learning. The first big mechanistic result."},
            {"title": "Toy Models of Superposition", "authors": "Elhage et al.", "year": 2022,
             "url": "https://transformer-circuits.pub/2022/toy_model/index.html",
             "summary": "Why neurons are polysemantic and why we need decomposition methods like SAEs."},
            {"title": "Scaling Monosemanticity (Sparse Autoencoders on Claude)", "authors": "Templeton et al. (Anthropic)", "year": 2024,
             "url": "https://transformer-circuits.pub/2024/scaling-monosemanticity/",
             "summary": "Millions of interpretable features extracted from a frontier model. Steering experiments included."},
            {"title": "Locating and Editing Factual Associations in GPT (ROME)", "authors": "Meng et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2202.05262",
             "summary": "Locate factual associations in MLP layers; edit them surgically. The standard knowledge-editing baseline."},
        ],
    },
    {
        "id": 40, "part": "X. AI Safety & Alignment",
        "title": "Bias, Fairness, and Sociotechnical Harms",
        "summary": """
<p>LMs encode the biases of their training data and amplify them via deployment scale. Bender et al.'s
"Stochastic Parrots" (2021) framed the sociotechnical critique that has shaped policy and academic discourse.
Practical evaluation: <b>BBQ</b> (bias QA), <b>StereoSet</b>, <b>RealToxicityPrompts</b>, <b>HELM</b>'s fairness
metrics. Mitigations are partial — assume residual bias and design for it (auditing, opt-outs, recourse).</p>
""",
        "papers": [
            {"title": "On the Dangers of Stochastic Parrots", "authors": "Bender, Gebru, McMillan-Major, Shmitchell", "year": 2021, "venue": "FAccT (Open Access)",
             "url": "https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf",
             "summary": "Foundational sociotechnical critique. Required reading regardless of prior. (Direct OA PDF; the FAccT proceedings paper is gold open access.)"},
            {"title": "BBQ: A Hand-Built Bias Benchmark for Question Answering", "authors": "Parrish et al.", "year": 2022,
             "url": "https://arxiv.org/abs/2110.08193", "summary": "Practical bias eval across 9 axes."},
            {"title": "RealToxicityPrompts", "authors": "Gehman et al.", "year": 2020,
             "url": "https://arxiv.org/abs/2009.11462", "summary": "Standard toxicity-elicitation benchmark."},
            {"title": "Datasheets for Datasets", "authors": "Gebru et al.", "year": 2021,
             "url": "https://arxiv.org/abs/1803.09010", "summary": "Documentation discipline for training data; widely adopted."},
        ],
    },

    # ============================================================
    # PART XI — AI FOR CODE
    # ============================================================
    {
        "id": 41, "part": "XI. AI for Code & Software Engineering",
        "title": "Code Models: Codex, AlphaCode, StarCoder, Code Llama",
        "summary": """
<p>Code is a near-perfect domain for LMs: massive supervised data (open-source), unambiguous correctness signal
(unit tests), structured outputs. The lineage runs Codex (2021) → AlphaCode (2022) → StarCoder/StarCoder2 →
Code Llama → Qwen2.5-Coder / DeepSeek-Coder-V2 / Codestral. Modern open coders match GPT-4-class performance
on HumanEval / MBPP.</p>
""",
        "papers": [
            {"title": "Evaluating Large Language Models Trained on Code (Codex)", "authors": "Chen et al.", "year": 2021,
             "url": "https://arxiv.org/abs/2107.03374",
             "summary": "Origin of Copilot; introduces HumanEval. Most-cited paper in AI-for-code."},
            {"title": "Competition-Level Code Generation with AlphaCode", "authors": "Li et al. (DeepMind)", "year": 2022,
             "url": "https://arxiv.org/abs/2203.07814",
             "summary": "Cluster-and-filter sampling for competitive programming. Reaches median Codeforces user."},
            {"title": "StarCoder 2 and The Stack v2", "authors": "Lozhkov et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2402.19173",
             "summary": "Best fully-open code model recipe; data, training, evaluation transparent."},
            {"title": "Code Llama: Open Foundation Models for Code", "authors": "Rozière et al.", "year": 2023,
             "url": "https://arxiv.org/abs/2308.12950",
             "summary": "Llama 2 specialized for code; long-context FIM training. Production-grade open coder."},
            {"title": "DeepSeek-Coder-V2", "authors": "DeepSeek-AI", "year": 2024,
             "url": "https://arxiv.org/abs/2406.11931",
             "summary": "MoE coder matching GPT-4 on coding evals; extensive multi-language coverage."},
        ],
    },
    {
        "id": 42, "part": "XI. AI for Code & Software Engineering",
        "title": "Repository-Scale Coding: SWE-bench and AI Engineers",
        "summary": """
<p>Function-level evals (HumanEval) saturated. The frontier moved to <b>SWE-bench</b> (Jimenez et al., 2024) —
real GitHub issues paired with passing tests. SWE-bench Verified is the de-facto credibility metric for
"AI software engineer" agents (Devin, OpenHands, Aider, Claude Code, Cursor agents).</p>
<p>Open results in 2025 routinely exceed 50% on SWE-bench Verified, up from <2% in early 2024. The
remaining gap is in long-horizon planning, large-codebase navigation, and graceful failure.</p>
""",
        "papers": [
            {"title": "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", "authors": "Jimenez et al.", "year": 2024, "venue": "ICLR",
             "url": "https://arxiv.org/abs/2310.06770", "summary": "2,294 real Django/Flask/etc. issues with tests. The benchmark of record for coding agents."},
            {"title": "OpenDevin / OpenHands: An Open Platform for AI Software Developers", "authors": "Wang et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2407.16741",
             "summary": "Open-source AI software engineer platform; reproducible SWE-bench evaluations."},
            {"title": "SWE-Gym: An Open Environment for Training Software Engineering Agents", "authors": "Pan et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2412.21139",
             "summary": "Training environment + RL recipes for code agents. Reproducible."},
            {"title": "Agentless: Demystifying LLM-based Software Engineering Agents", "authors": "Xia et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2407.01489",
             "summary": "A simple three-phase pipeline matches sophisticated agent frameworks. Sobering."},
        ],
        "extras": [
            {"label": "SWE-bench leaderboard", "url": "https://www.swebench.com/"},
        ],
    },
    {
        "id": 43, "part": "XI. AI for Code & Software Engineering",
        "title": "Practical AI Coding: Copilot, Cursor, Claude Code, Aider",
        "summary": """
<p>The practitioner stack in 2026:</p>
<ul>
  <li><b>Inline completions</b>: GitHub Copilot, Cursor Tab, Continue.</li>
  <li><b>Chat / refactor / multi-file edits</b>: Cursor Composer, Cline, Aider, Sourcegraph Cody.</li>
  <li><b>Autonomous agents (terminal-native)</b>: Claude Code, OpenHands, Devin.</li>
</ul>
<p>Lessons from production usage:</p>
<ul>
  <li>Code review and tests do <b>not</b> become optional — they become more important, because review surface
      grows when generation is cheap.</li>
  <li>Agents need narrow, well-documented tools — same lesson as LLM tool use generally.</li>
  <li>Ergonomics dominate model quality once you are above a threshold (Claude 3.5+, GPT-4o+, Llama 3.1 70B+).</li>
</ul>
""",
        "papers": [
            {"title": "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot", "authors": "Peng, Kalliamvakou, Cihon, Demirer", "year": 2023,
             "url": "https://arxiv.org/abs/2302.06590",
             "summary": "Controlled study: Copilot users finish coding tasks 55% faster. Foundational productivity evidence."},
            {"title": "Measuring GitHub Copilot's Impact on Productivity", "authors": "Cui et al. (Microsoft)", "year": 2024, "venue": "CACM (archive)",
             "url": "https://web.archive.org/web/20251023183058/https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/",
             "summary": "Larger field study; ~26% more PRs per developer. (Wayback snapshot — the live cacm.acm.org URL is gated by a Cloudflare bot challenge; CACM is otherwise free to read.)"},
            {"title": "Lost at C: A User Study on the Security Implications of Large Language Model Code Assistants", "authors": "Sandoval et al.", "year": 2023, "venue": "USENIX Sec",
             "url": "https://arxiv.org/abs/2208.09727",
             "summary": "AI-assisted code is not less secure on average — but reviewers must still review. Calibrates the productivity story."},
        ],
        "extras": [
            {"label": "Aider", "url": "https://aider.chat/"},
            {"label": "Continue (GitHub)", "url": "https://github.com/continuedev/continue"},
            {"label": "OpenHands", "url": "https://github.com/All-Hands-AI/OpenHands"},
        ],
    },

    # ============================================================
    # PART XII — RESEARCH FRONTIER
    # ============================================================
    {
        "id": 44, "part": "XII. Research Frontier",
        "title": "Synthetic Data and Self-Improvement",
        "summary": """
<p>As public web data plateaus, synthetic data generated by stronger models — filtered for quality, deduplicated,
and verified — is the dominant lever in 2025-26 post-training. <b>STaR</b> (Zelikman, 2022), <b>Self-Rewarding LMs</b>
(Yuan et al., 2024), and <b>RLAIF</b> all share a self-improvement structure.</p>
<p>Open question: where are the limits? Shumailov et al. (2024) show that naively training on a model's own outputs
collapses distributions. Filtering, verification, and external grounding (via tools, code execution, math checkers) appear
necessary to break out of the loop.</p>
""",
        "papers": [
            {"title": "STaR: Self-Taught Reasoner", "authors": "Zelikman, Wu, Mu, Goodman", "year": 2022, "venue": "NeurIPS",
             "url": "https://arxiv.org/abs/2203.14465",
             "summary": "Bootstrap rationales from successful samples; iterate. Conceptual ancestor of o1/R1."},
            {"title": "Self-Rewarding Language Models", "authors": "Yuan et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2401.10020",
             "summary": "Model serves as both generator and judge across iterations."},
            {"title": "AI models collapse when trained on recursively generated data", "authors": "Shumailov et al.", "year": 2024, "venue": "Nature",
             "url": "https://www.nature.com/articles/s41586-024-07566-y",
             "summary": "Repeated training on model outputs causes mode collapse. Watershed cautionary result."},
            {"title": "RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback", "authors": "Lee et al. (Google)", "year": 2023,
             "url": "https://arxiv.org/abs/2309.00267",
             "summary": "AI-judge preferences match human-judge for harmlessness; >10x cheaper data."},
        ],
    },
    {
        "id": 45, "part": "XII. Research Frontier",
        "title": "World Models and Embodied Agents",
        "summary": """
<p>Beyond text: models that learn <i>predictive models of environments</i> — simulators, video, robot dynamics —
and use them for planning. <b>Genie</b>, <b>Sora</b>, and Tesla / Wayve world models, plus the open-ended
<b>Diffusion World Model</b> agenda. Embodied AI (RT-2, OpenVLA, Pi0) plugs LMs into robot control,
demonstrating zero-shot transfer of common sense into actuation.</p>
""",
        "papers": [
            {"title": "Genie: Generative Interactive Environments", "authors": "Bruce et al. (DeepMind)", "year": 2024, "venue": "ICML",
             "url": "https://arxiv.org/abs/2402.15391",
             "summary": "Foundation world model trained on internet video; controllable virtual environments."},
            {"title": "RT-2: Vision-Language-Action Models", "authors": "Brohan et al. (Google)", "year": 2023,
             "url": "https://arxiv.org/abs/2307.15818",
             "summary": "VLM fine-tuned to output robot actions; transfers web-scale knowledge to manipulation."},
            {"title": "OpenVLA: An Open-Source Vision-Language-Action Model", "authors": "Kim et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2406.09246", "summary": "Open weights and code. The reproducible VLA baseline."},
            {"title": "Video generation models as world simulators (Sora technical report)", "authors": "OpenAI", "year": 2024,
             "url": "https://web.archive.org/web/20240429024704/https://openai.com/research/video-generation-models-as-world-simulators",
             "summary": "Diffusion-transformer-based video generator; raises 'is video pretraining a path to general world models?' (Wayback snapshot — the live openai.com URL is gated by a Cloudflare bot challenge.)"},
        ],
    },
    {
        "id": 46, "part": "XII. Research Frontier",
        "title": "AI for Science: AlphaFold, Materials, Theorem Proving",
        "summary": """
<p>The most consequential externally-validated AI results are in science: <b>AlphaFold</b> (Nobel-cited, 2024) and
<b>AlphaFold 3</b> (multi-molecule complexes), <b>GNoME</b> (2.2M new candidate materials), <b>AlphaProof / AlphaGeometry 2</b>
(IMO silver-medal-level, 2024). For practitioners these matter as proof-of-concept that <i>verifier-driven</i>
neural search is a genuinely new way to do science — when you have a reliable checker, the LM is mainly searching.</p>
""",
        "papers": [
            {"title": "Highly accurate protein structure prediction with AlphaFold", "authors": "Jumper et al. (DeepMind)", "year": 2021, "venue": "Nature",
             "url": "https://www.nature.com/articles/s41586-021-03819-2",
             "summary": "Solves protein structure prediction at near-experimental accuracy. 2024 Nobel Prize in Chemistry."},
            {"title": "Accurate structure prediction of biomolecular interactions with AlphaFold 3", "authors": "Abramson et al.", "year": 2024, "venue": "Nature",
             "url": "https://www.nature.com/articles/s41586-024-07487-w",
             "summary": "Generalizes AF2 to ligand, nucleic acid, and protein complexes via diffusion head."},
            {"title": "Scaling deep learning for materials discovery (GNoME)", "authors": "Merchant et al.", "year": 2023, "venue": "Nature",
             "url": "https://www.nature.com/articles/s41586-023-06735-9", "summary": "2.2M new stable materials candidates discovered by graph neural networks."},
            {"title": "AlphaGeometry: An Olympiad-level AI system for geometry", "authors": "Trinh et al.", "year": 2024, "venue": "Nature",
             "url": "https://www.nature.com/articles/s41586-023-06747-5",
             "summary": "Solves IMO-level geometry by neuro-symbolic search; influential template for verifier-guided LMs."},
        ],
    },
    {
        "id": 47, "part": "XII. Research Frontier",
        "title": "Open Problems and Research Directions (2026)",
        "summary": """
<p>A working researcher's list of currently-hot questions, biased toward what looks tractable:</p>
<ol>
  <li><b>Long-horizon agents</b>. Today's agents fall apart past ~50 steps. What's the right memory + planning + verifier stack?</li>
  <li><b>Inference-time compute scaling</b>. How does the optimal allocation of compute between training, search, and verification change with task?</li>
  <li><b>Verifiable rewards</b>. Can we build process-reward models that generalize beyond math/code?</li>
  <li><b>SLM specialization</b>. Routing + small expert models vs. one big model — what's the right operating point and how do we evaluate it?</li>
  <li><b>Mechanistic interpretability at scale</b>. Can SAE features become a primitive in production systems (steering, oversight)?</li>
  <li><b>Continual learning without catastrophic forgetting</b>. Still essentially unsolved at frontier scale.</li>
  <li><b>Multilingual and cultural alignment</b>. The frontier is mostly English; non-Latin-script speakers pay a tokenization tax and a quality tax.</li>
  <li><b>Energy and economic sustainability</b>. Ratios of cost-per-useful-task continue to drop ~10x/year — when does the curve bend?</li>
  <li><b>AI Safety: scalable oversight</b>. Debate, weak-to-strong generalization, RLHF without humans.</li>
  <li><b>Evaluation in the wild</b>. How do we measure usefulness of agentic systems doing real work, not benchmarks?</li>
</ol>
""",
        "papers": [
            {"title": "Foundational Challenges in Assuring Alignment and Safety of LLMs", "authors": "Anwar, Saparov, Bengio, et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2404.09932",
             "summary": "Best 'open problems' anchor — 18 challenges, hundreds of references."},
            {"title": "Position: Bayesian Deep Learning is Needed in the Age of Large-Scale AI", "authors": "Papamarkou et al.", "year": 2024,
             "url": "https://arxiv.org/abs/2402.00809",
             "summary": "Calibration and uncertainty as research directions for LMs."},
            {"title": "Weak-to-Strong Generalization", "authors": "Burns et al. (OpenAI)", "year": 2023,
             "url": "https://arxiv.org/abs/2312.09390",
             "summary": "Can a weak supervisor align a strong model? An analog for the future of human oversight."},
        ],
    },
    {
        "id": 48, "part": "XII. Research Frontier",
        "title": "How to Read a Paper, Reproduce, and Stay Current",
        "summary": """
<p>A practical operating manual for the postgrad practitioner who has to keep up while shipping.</p>

<h4>Reading</h4>
<ol>
  <li>First pass: title, abstract, intro, last sentence of each section, conclusion. 10 minutes.</li>
  <li>Second pass: figures (especially Fig 1 and the main results table), method outline. 30 minutes.</li>
  <li>Third pass: read for the gotcha — eval contamination, missing baselines, hyperparameter cherry-picking, ablation gaps.</li>
</ol>
<h4>Reproducing</h4>
<ul>
  <li>Prefer official code; otherwise <code>nanoGPT</code>, <code>llm.c</code>, <code>tinygrad</code>, or <code>HF transformers</code>.</li>
  <li>Get a tiny model training on your laptop in &lt;10 minutes before you spin GPUs.</li>
  <li>Match a reported number on a small subset before you scale.</li>
</ul>
<h4>Staying current</h4>
<ul>
  <li>arXiv-sanity, Hugging Face Daily Papers, Papers With Code, AlphaXiv.</li>
  <li>Follow specific researchers on GitHub and X — signal density beats most newsletters.</li>
  <li>Track conferences: NeurIPS / ICML / ICLR / ACL / EMNLP / NAACL; for systems: MLSys, SOSP, OSDI.</li>
  <li>Once a quarter: re-read one foundational paper to keep your prior calibrated.</li>
</ul>
""",
        "papers": [
            {"title": "How to Read a Paper", "authors": "Srinivasan Keshav", "year": 2007,
             "url": "https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf",
             "summary": "The classic three-pass method. Five pages; the highest ROI five pages in your career."},
            {"title": "nanoGPT", "authors": "Andrej Karpathy", "year": 2022, "venue": "code",
             "url": "https://github.com/karpathy/nanoGPT",
             "summary": "Minimal-but-real GPT pretraining + finetuning code. The right starting point for hands-on learning."},
            {"title": "Let's build GPT: from scratch, in code, spelled out", "authors": "Andrej Karpathy", "year": 2023, "venue": "video",
             "url": "https://www.youtube.com/watch?v=kCc8FmEb1nY",
             "summary": "Two-hour, line-by-line GPT build. The single best lecture on transformers."},
        ],
        "extras": [
            {"label": "Hugging Face Daily Papers", "url": "https://huggingface.co/papers"},
            {"label": "arXiv cs.CL (NLP)", "url": "https://arxiv.org/list/cs.CL/recent"},
            {"label": "Papers With Code", "url": "https://paperswithcode.com/"},
            {"label": "Anthropic Research", "url": "https://www.anthropic.com/research"},
            {"label": "OpenAI Research (archive)", "url": "https://web.archive.org/web/2026/https://openai.com/research/"},
            {"label": "Google DeepMind Research", "url": "https://deepmind.google/research/"},
        ],
    },
]


def by_part():
    parts = {}
    for ch in CHAPTERS:
        parts.setdefault(ch["part"], []).append(ch)
    return parts
