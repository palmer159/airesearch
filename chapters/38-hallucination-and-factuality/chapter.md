---
id: 38
title: Hallucination and Factuality
part: X. AI Safety & Alignment
---

<p>LMs confabulate. Surveys (Huang et al., 2023) categorize input-conflicting, context-conflicting, and
fact-conflicting hallucinations. Mitigations: RAG (Ch. 23), self-consistency (Ch. 19), abstention training,
and verifier/critic models. <b>SelfCheckGPT</b> and <b>FActScore</b> are useful evaluators.</p>
<p>Honest framing for an executive: hallucination is <i>reduced</i>, not <i>eliminated</i>, by current techniques.
Treat any LM output that informs a customer-facing decision as needing grounding + verification.</p>

## Papers

### A Survey on Hallucination in Large Language Models
- **Authors:** Huang et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2311.05232

Comprehensive taxonomy + mitigations. Best one-stop reference.

### SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection
- **Authors:** Manakul, Liusie, Gales
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2303.08896

Sample multiple completions; inconsistency ≈ hallucination. Cheap and surprisingly effective.

### FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation
- **Authors:** Min et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.14251

Decompose responses into atomic claims; score each. Standard factuality eval.
