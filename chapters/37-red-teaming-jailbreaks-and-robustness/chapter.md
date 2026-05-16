---
id: 37
title: Red Teaming, Jailbreaks, and Robustness
part: X. AI Safety & Alignment
---

<p>An aligned model is not a robust model. Adversarial prompts, gradient-based attacks (GCG), many-shot jailbreaks,
and <a href="https://en.wikipedia.org/wiki/Prompt_injection" target="_blank" rel="noopener">prompt-injection</a> in tool-use settings remain unsolved. Practitioners should:</p>
<ul>
  <li>Maintain an internal red-team and rotating attack library.</li>
  <li>Treat prompt-injection as a <b>security</b> problem (untrusted retrieved/tool output), not just an alignment one.</li>
  <li>Use defense-in-depth: input filters, output filters, and least-privilege tool design.</li>
</ul>

## Papers

### Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG)
- **Authors:** Zou et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.15043

Gradient-based suffix attacks transfer across closed and open models. Foundational adversarial result.

### Many-shot Jailbreaking
- **Authors:** Anil et al. (Anthropic)
- **Year:** 2024
- **URL:** https://www.anthropic.com/research/many-shot-jailbreaking

Long context is itself an attack surface. Inverse-scaling failure mode.

### Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
- **Authors:** Greshake et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2302.12173

Indirect prompt injection attacks; foundational result for tool-use security.

### Red Teaming Language Models with Language Models
- **Authors:** Perez et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2202.03286

Automate red-teaming with another LM. Now a standard internal practice.
