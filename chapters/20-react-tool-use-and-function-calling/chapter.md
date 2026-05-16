---
id: 20
title: ReAct, Tool Use, and Function Calling
part: V. Reasoning & Agents
---

<p><b>ReAct</b> (Yao et al., 2023) interleaves <i>Thought → Action → Observation</i> traces, letting the model use
external tools (web search, calculators, APIs). Modern frontier models expose this via "function calling" /
"tool use" APIs (OpenAI 2023, Anthropic Claude tool-use, Gemini).</p>
<p>For practitioners: tool use turns an LM into a reasoning core that can act on real systems. The hardest part is
not the prompt — it's tool design (idempotent, well-typed, cheap-to-fail) and observability of the agent loop.</p>

## Papers

### ReAct: Synergizing Reasoning and Acting in Language Models
- **Authors:** Yao et al.
- **Year:** 2023
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2210.03629

Interleaves reasoning and tool actions. Foundation of every modern agent loop.

### Toolformer: Language Models Can Teach Themselves to Use Tools
- **Authors:** Schick et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2302.04761

Self-supervised tool insertion via perplexity reduction; trains the model to call APIs natively.

### Gorilla: Large Language Model Connected with Massive APIs
- **Authors:** Patil et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.15334

API-call generation grounded in retrieval; reduces hallucinated function names.

### Reflexion: Language Agents with Verbal Reinforcement Learning
- **Authors:** Shinn et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2303.11366

Agent self-reflection between trials; cheap iterative improvement without weight updates.
