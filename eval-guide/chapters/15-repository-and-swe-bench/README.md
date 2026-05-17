---
id: 15
title: Repository-Level and SWE Tasks: SWE-bench, SWE-bench Verified, SWE-bench Lite, SWE-Lancer
part: IV. Coding and SWE Benchmarks
---

# Repository-Level and SWE Tasks: SWE-bench, SWE-bench Verified, SWE-bench Lite, SWE-Lancer

*IV. Coding and SWE Benchmarks*

<p>Function-level and contest benchmarks miss the core of software
engineering: <i>change a real codebase to satisfy a real bug report
without breaking anything else</i>. <b>SWE-bench</b> (Jimenez et al.,
Princeton, 2023) is the benchmark that finally measured that, and it
has become the headline number for any serious coding-agent claim.</p>

<h4>What a SWE-bench task looks like</h4>
<p>Each task is a real GitHub issue from one of 12 popular Python
projects (django, sympy, scikit-learn, matplotlib, requests, flask,
sphinx, pylint, pytest, astropy, xarray, seaborn). The harness gives
the agent the repo at the commit just before the fix, plus the issue
text. The agent must produce a <i>patch</i> (a unified diff) that, when
applied, makes the project's hidden post-fix test suite pass. Multi-file
edits are common; reading source code is mandatory.</p>

<pre>
task: django__django-12345
repo:  django/django @ a1b2c3d (parent of the fix commit)
issue: "QuerySet.update() raises FieldError on annotated fields..."

target tests (hidden):
  tests/queries/test_qs_combinators.py::QuerySetCombinatorsTests::test_update_annotated
  tests/queries/test_qs_combinators.py::QuerySetCombinatorsTests::test_update_annotated_filter

fail-to-pass:  these tests fail on the parent commit, must pass after the patch
pass-to-pass:  unrelated tests that already pass, must continue to pass

resolved iff   apply(patch) -> pytest -> all fail-to-pass + all pass-to-pass green
</pre>

<h4>The three official splits</h4>
<ul>
  <li><b>SWE-bench (full)</b> — 2,294 tasks. Wide, but noisy: some
  tasks have ambiguous specs, broken environments, or tests that depend
  on irrelevant behaviour.</li>
  <li><b>SWE-bench Verified</b> (OpenAI, 2024) — 500 tasks
  hand-screened by professional software engineers for unambiguous
  problem statements and clean test suites. This is the leaderboard
  number people now quote.</li>
  <li><b>SWE-bench Lite</b> — 300 small, single-file-ish fixes. Cheap
  enough to run in CI, useful for fast iteration on agents.</li>
</ul>

<p>Newer variants extend the idea: <b>SWE-bench Multimodal</b>
(JavaScript repos with screenshots), <b>SWE-bench Live</b> (continuously
refreshed to dodge contamination), and <b>SWE-Lancer</b> (real
freelance-marketplace tasks with payment-tied test cases).</p>

<h4>Agentic harnesses</h4>
<p>You cannot just feed a SWE-bench task to a chat completion. The
model needs to <i>act</i>: list files, read code, run tests, edit, and
iterate. The community has converged on a few harness families:</p>
<ul>
  <li><b>SWE-agent</b> (Princeton) — the original Agent-Computer
  Interface paper. A small, opinionated set of shell-like tools
  designed for LLMs.</li>
  <li><b>OpenHands</b> (formerly OpenDevin) — broader, modular agent
  with a sandbox, browser, and pluggable tools. The current
  open-source workhorse.</li>
  <li><b>Agentless</b> (Xia et al., 2024) — a deliberately
  non-agentic pipeline (localise → repair → patch) that scores
  surprisingly high. A useful baseline that exposes how much of the
  hard work is plain retrieval.</li>
  <li><b>Aider</b> — interactive coding tool that doubles as a
  passable benchmark harness.</li>
</ul>

<h4>The metric: %resolved</h4>
<p>Scoring is binary per task — patch applies cleanly and all required
tests turn green, or it doesn't. The reported number is
<b>%resolved</b> on the chosen split. Frontier closed models are in the
60-75% range on Verified; strong open-source agents (with DeepSeek-V3,
Qwen3-Coder, Llama-4-Coder etc.) reach the 40-55% range; weaker SLMs
fall below 10%. This is the benchmark that most cleanly separates
coding agents from glorified autocomplete.</p>

<h4>Things to watch out for</h4>
<ul>
  <li><b>Test leakage</b> — some agents peek at the hidden tests.
  Verified and Live mitigate this but be paranoid.</li>
  <li><b>Environment flakiness</b> — Docker images for old commits
  drift; reproducing published numbers exactly is harder than it
  looks.</li>
  <li><b>Cost</b> — a full Verified run with a strong agent can be
  hundreds of dollars in API calls. Lite is your friend for
  iteration.</li>
</ul>

## Papers and references

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Authors:** Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan
- **Year:** 2023
- **Venue:** ICLR 2024
- **URL:** https://arxiv.org/abs/2310.06770

The original SWE-bench: 2,294 issues from 12 Python repos, multi-file patches, hidden pytest suites. Defined the modern coding-agent eval.

### SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- **Authors:** Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press
- **Year:** 2024
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2405.15793

The Agent-Computer Interface paper. Introduces a custom set of LLM-friendly shell tools and shows large gains over plain prompting on SWE-bench.

### OpenHands: An Open Platform for AI Software Developers as Generalist Agents
- **Authors:** Wang, Li, Lin, Aroca-Ouellette, Han, Wang, et al.
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.16741

OpenHands (formerly OpenDevin). The dominant open-source agent harness, with sandboxed execution, browser tool, and a pluggable tool registry.

### Agentless: Demystifying LLM-Based Software Engineering Agents
- **Authors:** Xia, Deng, Dunlap, Zhang, Yu, Zheng, Zhang, Wang
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.01489

A deliberately non-agentic localise-repair-patch pipeline that competes with full agents on SWE-bench. Shows how much of the gain is retrieval, not autonomy.

### Introducing SWE-bench Verified
- **Authors:** OpenAI
- **Year:** 2024
- **Venue:** OpenAI blog
- **URL:** https://web.archive.org/web/2026/https://openai.com/index/introducing-swe-bench-verified/

OpenAI's 500-task human-screened subset. The default leaderboard split for serious agent claims.

## Extras
- [SWE-bench leaderboard](https://www.swebench.com/)
- [SWE-bench source repo (Princeton NLP)](https://github.com/princeton-nlp/SWE-bench)
- [OpenHands on GitHub (All-Hands-AI)](https://github.com/All-Hands-AI/OpenHands)
