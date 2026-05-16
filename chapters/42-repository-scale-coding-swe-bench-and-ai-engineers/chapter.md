---
id: 42
title: Repository-Scale Coding: SWE-bench and AI Engineers
part: XI. AI for Code & Software Engineering
---

<p>Function-level evals (HumanEval) saturated. The frontier moved to <b><a href="https://en.wikipedia.org/wiki/SWE-Bench" target="_blank" rel="noopener">SWE-bench</a></b> (Jimenez et al., 2024) —
real GitHub issues paired with passing tests. SWE-bench Verified is the de-facto credibility metric for
"AI software engineer" agents (Devin, OpenHands, Aider, Claude Code, Cursor agents).</p>
<p>Open results in 2025 routinely exceed 50% on SWE-bench Verified, up from <2% in early 2024. The
remaining gap is in long-horizon planning, large-codebase navigation, and graceful failure.</p>

## Papers

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Authors:** Jimenez et al.
- **Year:** 2024
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2310.06770

2,294 real Django/Flask/etc. issues with tests. The benchmark of record for coding agents.

### OpenDevin / OpenHands: An Open Platform for AI Software Developers
- **Authors:** Wang et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.16741

Open-source AI software engineer platform; reproducible SWE-bench evaluations.

### SWE-Gym: An Open Environment for Training Software Engineering Agents
- **Authors:** Pan et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2412.21139

Training environment + RL recipes for code agents. Reproducible.

### Agentless: Demystifying LLM-based Software Engineering Agents
- **Authors:** Xia et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.01489

A simple three-phase pipeline matches sophisticated agent frameworks. Sobering.

## Extras

- [SWE-bench leaderboard](https://www.swebench.com/)
