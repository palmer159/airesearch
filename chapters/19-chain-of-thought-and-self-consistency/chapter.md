---
id: 19
title: Chain-of-Thought and Self-Consistency
part: V. Reasoning & Agents
---

<p>Asking a model to "think step by step" (Wei et al., 2022) materially improves multi-step reasoning at
sufficient scale. <b>Self-consistency</b> samples many CoTs and majority-votes the answer — robust and cheap.</p>
<p>Subsequent research (least-to-most, plan-and-solve, tree-of-thoughts, graph-of-thoughts) extended the basic
idea into structured search.</p>

## Papers

### Chain-of-Thought Prompting Elicits Reasoning
- **Authors:** Wei et al.
- **Year:** 2022
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2201.11903

The 'let's think step by step' paper; transforms math/commonsense reasoning above ~60B.

### Self-Consistency Improves Chain of Thought Reasoning
- **Authors:** Wang et al.
- **Year:** 2023
- **Venue:** ICLR
- **URL:** https://arxiv.org/abs/2203.11171

Sample many reasoning paths, majority-vote. Simple, almost free, robust.

### Tree of Thoughts: Deliberate Problem Solving with LLMs
- **Authors:** Yao et al.
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2305.10601

Generalizes CoT to a search over partial solutions. Useful for puzzles, planning.

### Large Language Models are Zero-Shot Reasoners
- **Authors:** Kojima et al.
- **Year:** 2022
- **URL:** https://arxiv.org/abs/2205.11916

'Let's think step by step.' One sentence, often a 10-50 point gain.
