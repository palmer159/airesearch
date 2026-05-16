---
id: 21
title: Agentic Workflows: Planning, Memory, Multi-Agent
part: V. Reasoning & Agents
---

<p>An "agent" in 2026 is typically a loop: <i>plan → call tools → observe → update memory → repeat</i>. The interesting
architectural questions are about state — episodic memory, scratchpads, retrieval over past traces — and about
multi-agent coordination (debate, hierarchical decomposition).</p>
<p>Important sober result: multi-agent systems often <i>don't</i> outperform a single strong model with a careful prompt
(Cemri et al., 2024). The win usually comes from giving the agent better tools, not more agents.</p>

## Papers

### Generative Agents: Interactive Simulacra of Human Behavior
- **Authors:** Park et al.
- **Year:** 2023
- **Venue:** UIST
- **URL:** https://arxiv.org/abs/2304.03442

25 agents in a simulated town with memory, reflection, planning. Influential agent-architecture paper.

### Voyager: An Open-Ended Embodied Agent with LLMs
- **Authors:** Wang et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.16291

Lifelong skill library that grows; strong baseline for open-ended agent research (Minecraft).

### AutoGen / Multi-Agent Conversation Framework
- **Authors:** Wu et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2308.08155

Microsoft framework for multi-agent LLM applications; pragmatic and widely used.

### Why Do Multi-Agent LLM Systems Fail?
- **Authors:** Cemri et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2503.13657

Empirical study: most multi-agent gains evaporate under controlled comparison. Important counterweight to hype.
