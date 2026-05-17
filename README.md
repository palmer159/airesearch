# LLM Study Guide

A reproducible study guide on **LLMs and SLMs** for postgraduate CS students,
served by a tiny stdlib-only Python HTTP server. Built so that a single
script — `regenerate.py` — can rebuild the entire content tree from one
in-script manifest.

- **30 chapters** across **3 sections**: math foundations, LLM/SLM overview,
  and the chronological history of ML/AI from the perceptron (1958) to
  inference-time reasoning models (2024–25).
- **Open access only** — every linked paper, lecture note, or article is
  reachable without a paywall.
- Inline **glossary** that hyperlinks first mentions of concepts to free
  explainers (Wikipedia, faculty pages, MIT OCW, 3Blue1Brown).

---

## Quick start

```bash
git clone git@github.com:palmer159/airesearch.git
cd airesearch
python3 server.py            # default port 47314
```

Open <http://127.0.0.1:47314/>.

Requirements: Python 3.10+. No third-party dependencies.

---

## Regenerating the guide

The chapter tree is generated from `regenerate.py`. To rebuild:

```bash
python3 regenerate.py
```

This wipes `chapters/`, rebuilds it from the in-script `MANIFEST`, refreshes
`glossary.py`, updates the curriculum table in this README, and runs the
inline-link injector. Per-chapter progress is printed to stdout.

Edit chapters by editing the entries in `MANIFEST` inside `regenerate.py`,
then re-run the script. Hand edits to `chapters/*` are deliberately
ephemeral.

If you use Claude Code, the repo ships a project skill at
`.claude/skills/regenerate-study-guide/` that drives this command for you —
just ask Claude to "regenerate the study guide" and it will run the
generator and print per-chapter progress.

---

## Curriculum

### I. Math Foundations for ML & AI

1. Linear Algebra for Machine Learning
2. Calculus and Optimization
3. Probability, Statistics, and Information Theory

### II. LLMs and SLMs: What and Why

4. What is a Language Model?
5. The Math Under the Hood
6. SLMs vs LLMs: When to Choose Which

### III. ML & AI in Chronological Order

7. The Perceptron
8. Backpropagation
9. Convolutional Networks (LeNet)
10. LSTM: Recurrent Networks That Worked
11. Neural Language Models (Bengio NPLM)
12. AlexNet and the Deep Learning Ignition
13. Word Embeddings: word2vec and GloVe
14. Seq2seq and Attention
15. Generative Adversarial Networks
16. ResNet and Batch Normalization
17. The Transformer
18. BERT and the Encoder Era
19. GPT-2 and the Decoder-only Paradigm
20. GPT-3, Scaling Laws, and In-Context Learning
21. Diffusion Models (DDPM)
22. CLIP and Multimodal Contrastive Learning
23. InstructGPT, RLHF, and ChatGPT
24. Chain-of-Thought Prompting
25. Retrieval-Augmented Generation
26. LLaMA and the Open-Weight Era
27. LoRA, QLoRA, and Parameter-Efficient Fine-Tuning
28. Mixture-of-Experts at Scale (Mixtral, DeepSeek-V3)
29. Phi and the SLM Thesis: Textbooks Are All You Need
30. Inference-Time Reasoning: o1 and DeepSeek-R1

---

## Layout

```
airesearch/
├── README.md
├── regenerate.py          # source of truth for chapter content
├── server.py              # HTTP server (renders pages from chapters/)
├── loader.py              # Markdown-with-frontmatter parser
├── glossary.py            # phrase → explainer-URL table (generated)
├── tools/
│   └── linkify.py         # injects glossary links into chapter READMEs
└── chapters/              # generated: NN-slug/README.md (rendered inline on GitHub)
```

---

## License

Chapter prose and curation: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Python code: MIT. Linked papers and resources retain their original licenses.
