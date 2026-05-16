---
id: 41
title: Code Models: Codex, AlphaCode, StarCoder, Code Llama
part: XI. AI for Code & Software Engineering
---

<p>Code is a near-perfect domain for LMs: massive supervised data (open-source), unambiguous correctness signal
(unit tests), structured outputs. The lineage runs Codex (2021) → AlphaCode (2022) → StarCoder/StarCoder2 →
Code <a href="https://en.wikipedia.org/wiki/Llama_(language_model)" target="_blank" rel="noopener">Llama</a> → Qwen2.5-Coder / DeepSeek-Coder-V2 / Codestral. Modern open coders match GPT-4-class performance
on HumanEval / MBPP.</p>

## Papers

### Evaluating Large Language Models Trained on Code (Codex)
- **Authors:** Chen et al.
- **Year:** 2021
- **URL:** https://arxiv.org/abs/2107.03374

Origin of Copilot; introduces HumanEval. Most-cited paper in AI-for-code.

### Competition-Level Code Generation with AlphaCode
- **Authors:** Li et al. (DeepMind)
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2203.07814

Cluster-and-filter sampling for competitive programming. Reaches median Codeforces user.

### StarCoder 2 and The Stack v2
- **Authors:** Lozhkov et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.19173

Best fully-open code model recipe; data, training, evaluation transparent.

### Code Llama: Open Foundation Models for Code
- **Authors:** Rozière et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2308.12950

Llama 2 specialized for code; long-context FIM training. Production-grade open coder.

### DeepSeek-Coder-V2
- **Authors:** DeepSeek-AI
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2406.11931

MoE coder matching GPT-4 on coding evals; extensive multi-language coverage.
