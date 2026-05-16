# LLM Study Guide

A curated 12-section study guide on **Large Language Model (LLM) and Small
Language Model (SLM) research and engineering**, served by a tiny stdlib-only
Python HTTP server. Built for a postgraduate computer-science student aiming
to do AI research or operate as an AI practitioner in a tech company.

- **48 mini chapters** across 12 parts
- **194 paper citations** + **17 tool/extras links** + an inline **glossary**
  that hyperlinks first mentions of concepts and acronyms (n-gram, transformer,
  RLHF, MoE, RAG, CoT, AdamW, MMLU, …) to authoritative explainers
- **249 outbound links total**, every one verified to return HTTP 200
- **Open access only** — every link points to a free, public source (arXiv,
  Nature OA, lab CDNs like cdn.openai.com / www-cdn.anthropic.com,
  transformer-circuits.pub, JMLR, ISCA, Wikipedia, Stanford / Harvard faculty
  pages, GitHub, Wayback for a small handful that block programmatic fetches)
- Chapter content lives on disk as Markdown; the server renders it
- Citations have been verified against the actual cited paper (arXiv title
  match for arXiv links, PDF text inspection for PDFs, page-title check
  for everything else)

---

## Quick start
You can just browse all the chapters right here on git, or start the web server and
read and navigate there using the below instructions. Submit a PR for any additions 
to the content.

```bash
git clone git@github.com:palmer159/airesearch.git
cd airesearch
python3 server.py            # default port 47314
# or pick another port:
python3 server.py 51829
```

Then open <http://127.0.0.1:47314/>.

Requirements: Python 3.10+. No third-party dependencies.

---

## Layout

```
airesearch/
├── README.md
├── server.py              # HTTP server (renders pages from chapters/)
├── loader.py              # Markdown-with-frontmatter parser
├── glossary.py            # phrase → explainer-URL table
├── tools/
│   └── linkify.py         # injects glossary links into chapter.md files
└── chapters/
    ├── 01-from-n-grams-to-neural-lms-a-brief-history/
    │   └── chapter.md
    ├── 02-the-transformer-attention-is-all-you-need/
    │   └── chapter.md
    ├── ...
    └── 48-how-to-read-a-paper-reproduce-and-stay-current/
        └── chapter.md
```

Each `chapter.md` is self-contained: YAML-ish frontmatter (id, title, part),
an HTML body summary with examples and illustrations, a `## Papers` section
with structured paper entries, and an optional `## Extras` section with
tool / resource links.

---

## Curriculum (12 parts, 48 chapters)

### I. Foundations (Ch 1–5)
1. From n-grams to Neural LMs: a brief history
2. The Transformer: Attention Is All You Need
3. BERT and the encoder era
4. GPT-1/2/3 and the decoder-only paradigm
5. T5, BART, and the text-to-text frame

### II. Training & Data (Ch 6–10)
6. Tokenization (BPE, WordPiece, SentencePiece, tiktoken)
7. Pretraining data: C4, The Pile, RedPajama, Dolma, FineWeb
8. Optimization: AdamW, schedules, mixed precision, ZeRO
9. Scaling laws: Kaplan, Chinchilla, beyond
10. Emergent abilities, mirages, and phase transitions

### III. Architecture Frontiers (Ch 11–14)
11. Positional encoding & long context (RoPE, ALiBi, YaRN)
12. Mixture-of-Experts (MoE)
13. State-space models: Mamba and hybrids
14. Efficient attention: FlashAttention and friends

### IV. Post-training & Alignment (Ch 15–18)
15. Instruction tuning (SFT)
16. RLHF and Constitutional AI
17. DPO, IPO, KTO: reward-free preference optimization
18. PEFT: LoRA, QLoRA, adapters

### V. Reasoning & Agents (Ch 19–22)
19. Chain-of-thought and self-consistency
20. ReAct, tool use, and function calling
21. Agentic workflows: planning, memory, multi-agent
22. Inference-time compute and reasoning models (o1, R1)

### VI. Retrieval & Grounding (Ch 23–24)
23. Retrieval-augmented generation (RAG)
24. Embeddings, vector DBs, rerankers

### VII. Small Language Models (Ch 25–30)
25. Why SLMs now: definition, use cases, economics
26. The Phi series and "Textbooks Are All You Need"
27. Open SLM families: Llama-3, Gemma, Qwen, Mistral, SmolLM
28. Quantization: GPTQ, AWQ, GGUF, FP8/INT4
29. Knowledge distillation and model compression
30. On-device inference: speculative decoding, KV cache, MLC

### VIII. Multimodal (Ch 31–33)
31. Vision-language models: CLIP, Flamingo, LLaVA
32. Image / video / audio generation: diffusion in the LM era
33. Native multimodal models: GPT-4o, Gemini, Claude 3+

### IX. Evaluation (Ch 34–35)
34. Benchmarks: MMLU, BIG-Bench, HELM, GPQA, MATH
35. LM-as-judge, Arena, pairwise eval

### X. AI Safety & Alignment (Ch 36–40)
36. AI Safety: concrete problems and catastrophic risks
37. Red teaming, jailbreaks, and robustness
38. Hallucination and factuality
39. Interpretability and mechanistic understanding
40. Bias, fairness, and sociotechnical harms

### XI. AI for Code & Software Engineering (Ch 41–43)
41. Code models: Codex, AlphaCode, StarCoder, Code Llama
42. Repository-scale coding: SWE-bench and AI engineers
43. Practical AI coding: Copilot, Cursor, Claude Code, Aider

### XII. Research Frontier (Ch 44–48)
44. Synthetic data and self-improvement
45. World models and embodied agents
46. AI for science: AlphaFold, materials, theorem proving
47. Open problems and research directions (2026)
48. How to read a paper, reproduce, and stay current

---

## Editing chapters

Edit any `chapters/NN-slug/chapter.md` and reload the page — the server reads
files at startup, so restart `server.py` to pick up changes. Frontmatter
fields:

```markdown
---
id: 1
title: Chapter title
part: I. Foundations
---

<HTML body — passed through verbatim into the rendered page>

## Papers

### Title of paper
- **Authors:** A. Author, B. Coauthor
- **Year:** 2024
- **Venue:** NeurIPS    (optional)
- **URL:** https://arxiv.org/abs/...

Free-form summary paragraph about the paper.

### Next paper
- **Authors:** ...
- **Year:** ...
- **URL:** ...

Summary.

## Extras
- [Label](https://example.com/link)
- [Other label](https://example.com/other)
```

`loader.py` is the source of truth for the format.

### Inline glossary

`glossary.py` defines a list of `(phrase, url)` pairs that the server's
chapter prose links to. After editing it (or after rewriting any chapter's
summary section), run:

```bash
python3 tools/linkify.py
```

The script wraps the **first occurrence per chapter** of each glossary
phrase in an `<a>` tag pointing to the explainer. It is safe to re-run —
it skips text already inside `<a>`, `<pre>`, or `<code>` blocks, and
won't double-wrap a URL that's already present.

---

## Server design

- Bound to **127.0.0.1 only**, on the unprivileged unregistered port **47314**
  by default. No authn/authz — local-only.
- Pure Python stdlib (`http.server`, `urllib`, `re`). No deps.
- Routes:
  - `/` — index, grouped by part, with one card per chapter
  - `/chapter/{1..48}` — chapter view (summary + papers + extras + prev/next)
  - `/papers` — every paper, deduplicated, in one place
  - `/about` — methodology and curation policy
  - `/health` — JSON liveness check

---

## Why this exists

A study guide that meets two needs at once: depth for a postgrad student who
will need to *do* the research, and breadth for a practitioner who has to
ship in 2026. Most paper links are outbound — that respects publishers,
keeps the server tiny, and forces you to read the original work, which is
what actually builds intuition. Local content is reserved for curation,
illustrations, and connective prose.

---

## License

The chapter prose, illustrations, and curation in this repository are
released under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
The Python code is released under MIT. Linked papers and resources retain
their original licenses.
