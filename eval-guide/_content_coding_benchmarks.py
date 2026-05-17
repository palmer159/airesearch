"""Section IV — Coding and SWE Benchmarks.

Five chapters (12-16) covering coding evaluations from function-level
HumanEval through SWE-bench-style repository-level agents, ending with a
practical recipe for running a coding-agent harness against an
open-source model.
"""

from __future__ import annotations

from _chapter_types import Chapter, Paper, Extra


CODING_BENCH_CHAPTERS: list[Chapter] = [
    # ------------------------------------------------------------------ 12
    Chapter(
        id=12,
        slug="function-level-humaneval-mbpp-multipl-e",
        part="IV. Coding and SWE Benchmarks",
        title="Function-Level: HumanEval, MBPP, MultiPL-E",
        summary_html="""
<p>Coding benchmarks started small and concrete: give the model a
docstring, ask it to write a single Python function, then run a hidden
test suite. <b>HumanEval</b> (OpenAI, 2021, released alongside the Codex
paper) is the canonical example — 164 hand-written problems, each with a
function signature, a natural-language prompt, and a few unit tests.
<b>MBPP</b> (Google, 2021) — "Mostly Basic Programming Problems" — is
the same shape, scaled up to 974 short Python tasks crowd-sourced from
entry-level programmers.</p>

<h4>The pass@k metric</h4>
<p>Both benchmarks measure <b>pass@k</b>: the probability that at least
one of <code>k</code> sampled completions passes all unit tests. To
reduce variance you draw <code>n &gt;= k</code> samples per problem,
count how many are correct (<code>c</code>), and use the unbiased
estimator from the Codex paper:</p>

<pre>
                          /  C(n - c, k)  \\
pass@k  =  E_problems  | 1 - ------------- |
                          \\    C(n, k)    /
</pre>

<p>pass@1 is what you usually report; pass@10 and pass@100 show how much
the model gains from re-sampling. Temperature matters — pass@1 is
typically reported at <code>T = 0.2</code>, pass@k at higher T so the
samples are diverse.</p>

<h4>MultiPL-E: the same benchmarks, 18 languages</h4>
<p><b>MultiPL-E</b> (Cassano et al., 2022) translates HumanEval and MBPP
into roughly 18 programming languages — JavaScript, Java, C++, Rust, Go,
Lua, R, and so on — by mechanically rewriting the prompts and tests.
This is the cheapest way to check whether a model that crushes Python
HumanEval actually generalises beyond Python. Most do worse outside
their training distribution; the gap is informative.</p>

<h4>Why these are now mostly a sanity check</h4>
<p>Frontier models score above 90% on HumanEval pass@1, and decent
open-source SLMs (DeepSeek-Coder, Qwen-Coder, StarCoder2) score in the
70-90% range. The benchmark has effectively saturated for the models
people care about most. It still has uses:</p>
<ul>
  <li><b>SLM differentiation</b> — between a 1B and a 7B coding model,
  HumanEval still discriminates.</li>
  <li><b>Quick smoke test</b> — it runs in minutes and catches obvious
  regressions in fine-tuning or quantisation.</li>
  <li><b>Multilingual probing</b> via MultiPL-E — saturation in Python
  does not imply saturation in Rust.</li>
</ul>

<p>For anything more ambitious, you graduate to the harder benches in
chapters 13-15. But every coding-eval pipeline should still produce a
HumanEval number, if only as a baseline that lets you compare against
the thousands of papers that already report one. Treat it as the
push-up test, not the marathon.</p>
""",
        papers=[
            Paper(
                title="Evaluating Large Language Models Trained on Code (Codex / HumanEval)",
                authors="Chen, Tworek, Jun, Yuan, Pinto, Kaplan, et al.",
                year="2021",
                venue="arXiv",
                url="https://arxiv.org/abs/2107.03374",
                summary="Introduces Codex, HumanEval (164 problems), and the unbiased pass@k estimator. The canonical first coding benchmark.",
            ),
            Paper(
                title="Program Synthesis with Large Language Models (MBPP)",
                authors="Austin, Odena, Nye, Bosma, Michalewski, Dohan, et al.",
                year="2021",
                venue="arXiv",
                url="https://arxiv.org/abs/2108.07732",
                summary="MBPP — 974 short Python problems written by entry-level programmers, plus a hand-curated subset and an edited 'sanitised' version.",
            ),
            Paper(
                title="MultiPL-E: A Scalable and Polyglot Approach to Benchmarking Neural Code Generation",
                authors="Cassano, Gouwar, Nguyen, Nguyen, Phipps-Costin, et al.",
                year="2022",
                venue="arXiv / TSE",
                url="https://arxiv.org/abs/2208.08227",
                summary="Translates HumanEval and MBPP into ~18 languages by mechanically rewriting prompts and tests. The default multilingual coding bench.",
            ),
            Paper(
                title="HumanEval+ / EvalPlus: Are Your Tests Really Catching Bugs?",
                authors="Liu, Xia, Wang, Zhang",
                year="2023",
                venue="NeurIPS",
                url="https://arxiv.org/abs/2305.01210",
                summary="Augments HumanEval and MBPP with 80x more tests, exposing many 'passing' samples as actually wrong. Use HumanEval+ if you can.",
            ),
        ],
        extras=[
            Extra(
                label="OpenAI human-eval repo (reference pass@k implementation)",
                url="https://github.com/openai/human-eval",
            ),
            Extra(
                label="EvalPlus leaderboard (HumanEval+ / MBPP+)",
                url="https://evalplus.github.io/leaderboard.html",
            ),
            Extra(
                label="MultiPL-E on GitHub",
                url="https://github.com/nuprl/MultiPL-E",
            ),
        ],
    ),
    # ------------------------------------------------------------------ 13
    Chapter(
        id=13,
        slug="harder-and-fresher-livecodebench-bigcodebench-classeval",
        part="IV. Coding and SWE Benchmarks",
        title="Harder and Fresher: LiveCodeBench, BigCodeBench, ClassEval",
        summary_html="""
<p>Once HumanEval saturated and contamination concerns mounted (every
post-2022 web crawl probably includes the test set), the field reached
for benchmarks that are either <i>harder</i>, <i>fresher</i>, or
<i>structurally different</i>. Three of them are now standard.</p>

<h4>LiveCodeBench — fresh problems, dated cutoffs</h4>
<p><b>LiveCodeBench</b> (Jain et al., 2024) continuously scrapes new
problems from <a href="https://leetcode.com/" target="_blank" rel="noopener">LeetCode</a>, <a href="https://codeforces.com/" target="_blank" rel="noopener">Codeforces</a>, and <a href="https://atcoder.jp/" target="_blank" rel="noopener">AtCoder</a>, tagging each with the date it was
published. When you evaluate a model, you filter to problems released
<i>after</i> that model's training cutoff. The contamination problem
mostly disappears, and the benchmark stays alive year after year. It
also separates four sub-tasks: code generation, self-repair, test
output prediction, and execution simulation, so you get a
finer-grained view of reasoning vs. raw generation.</p>

<h4>BigCodeBench — real-world API juggling</h4>
<p><b>BigCodeBench</b> (Zhuo et al., 2024) is 1,140 tasks deliberately
designed to require <i>diverse function calls</i> across 139 Python
libraries — NumPy, pandas, requests, sklearn, Pillow, cryptography,
matplotlib, and so on. Each task has a rich set of branching tests
(99% branch coverage on average). It ships in two splits:</p>
<ul>
  <li><b>BigCodeBench-Complete</b> — the model gets a thorough
  docstring with type hints and examples. This isolates raw coding
  ability.</li>
  <li><b>BigCodeBench-Instruct</b> — the docstring is rewritten as a
  short natural-language instruction. Now the model also has to infer
  what APIs and arguments to use. Scores drop sharply, which is the
  whole point.</li>
</ul>

<h4>ClassEval — beyond single functions</h4>
<p><b>ClassEval</b> (Du et al., 2023) is 100 hand-crafted Python class
generation tasks. The model must produce an entire class — multiple
methods, internal state, sometimes inheritance — and the tests
exercise interactions between methods. This catches a failure mode
function-level benches cannot: models that write fine local code but
botch the larger structural picture (forgetting <code>self</code>,
inconsistent attribute names, methods that conflict). It is a useful
bridge between HumanEval and full repository tasks.</p>

<h4>How to read these together</h4>
<ul>
  <li>If a model is <b>great on HumanEval but mediocre on
  BigCodeBench-Instruct</b>, it has memorised idioms but cannot reason
  about library choice.</li>
  <li>If it is <b>good on LiveCodeBench-pre-cutoff but collapses
  post-cutoff</b>, you are seeing contamination, not capability.</li>
  <li>If it is <b>strong at function-level but weak on ClassEval</b>,
  it has a structure problem, not a syntax problem.</li>
</ul>

<p>None of these are perfect — Codeforces problems still over-weight
algorithmic puzzles, BigCodeBench's tests can be brittle, ClassEval is
small — but together they form the modern "harder coding bench" stack
that you should reach for once HumanEval flattens.</p>
""",
        papers=[
            Paper(
                title="LiveCodeBench: Holistic and Contamination-Free Evaluation of Large Language Models for Code",
                authors="Jain, Han, Gu, Li, Yan, Zhang, et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2403.07974",
                summary="A continuously updated coding benchmark with date-tagged problems from LeetCode/Codeforces/AtCoder. Lets you filter to post-cutoff tasks to neutralise contamination.",
            ),
            Paper(
                title="BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions",
                authors="Zhuo, Vu, Chim, Hu, Yu, Widyasari, et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2406.15877",
                summary="1,140 tasks across 139 Python libraries with high branch-coverage tests. Two splits (Complete, Instruct) tease apart coding skill from instruction following.",
            ),
            Paper(
                title="ClassEval: A Manually-Crafted Benchmark for Evaluating LLMs on Class-Level Code Generation",
                authors="Du, Liu, Li, Wang, Liu, Lou, et al.",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2308.01861",
                summary="100 Python class generation tasks. Tests cross-method state, inheritance, and structural consistency that single-function benches miss.",
            ),
            Paper(
                title="Is Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation (HumanEval+ / MBPP+)",
                authors="Liu, Xia, Wang, Zhang",
                year="2023",
                venue="NeurIPS",
                url="https://arxiv.org/abs/2305.01210",
                summary="The methodology paper that motivated everything in this chapter: HumanEval's tests are too lax, and many 'correct' samples are actually buggy.",
            ),
        ],
        extras=[
            Extra(
                label="LiveCodeBench leaderboard and dataset",
                url="https://livecodebench.github.io/",
            ),
            Extra(
                label="BigCodeBench on GitHub",
                url="https://github.com/bigcode-project/bigcodebench",
            ),
            Extra(
                label="ClassEval repository",
                url="https://github.com/FudanSELab/ClassEval",
            ),
        ],
    ),
    # ------------------------------------------------------------------ 14
    Chapter(
        id=14,
        slug="competitive-programming-codecontests-apps",
        part="IV. Coding and SWE Benchmarks",
        title="Competitive Programming: CodeContests, APPS",
        summary_html="""
<p>Competitive programming benchmarks ask a model to solve algorithmic
puzzles of the kind you would see at a programming contest:
constraints, sample I/O, hidden test cases, and tight time/memory
limits. They are useful because they probe <i>reasoning under
constraints</i> — but biased, because real software engineering rarely
looks like Codeforces.</p>

<h4>APPS</h4>
<p><b>APPS</b> (Hendrycks et al., 2021) was the first large-scale entry:
10,000 problems scraped from open coding sites, partitioned into three
difficulty buckets — <i>Introductory</i>, <i>Interview</i>, and
<i>Competition</i>. Each problem ships with input/output examples and a
hidden test suite. APPS is graded with strict pass-rate (every test
must pass) and is significantly harder than HumanEval; even strong
models struggle on the Competition split.</p>

<h4>CodeContests</h4>
<p><b>CodeContests</b> (Li et al., 2022) was assembled by DeepMind for
<a href="https://en.wikipedia.org/wiki/AlphaCode" target="_blank" rel="noopener">AlphaCode</a>. It is curated specifically for contest programming —
problems from Codeforces, Description2Code, and similar sources, with
many additional generated test cases to reduce false positives (a real
issue: contest problems often have weak public tests). CodeContests is
the standard reference when people quote AlphaCode-style results.</p>

<h4>1-shot vs. sample-and-filter</h4>
<p>Competitive programming exposes a tension that the rest of the field
mostly ignores: <i>how many samples are you allowed?</i> AlphaCode
generated up to a million samples per problem and used clustering plus
the public sample tests to pick a few to submit. That dramatically
boosts the effective pass rate, but it is wildly different from
"write the function once and you are done." Be explicit about which
regime you are evaluating in:</p>
<ul>
  <li><b>pass@1</b> — single sample, the realistic engineering case.</li>
  <li><b>pass@k</b> for small <code>k</code> (10, 100) — closer to a
  developer who tries a few times.</li>
  <li><b>n@k</b> with filtering — sample <code>k</code>, submit the
  best <code>n</code> after filtering with public tests; the
  AlphaCode-style protocol.</li>
</ul>

<h4>USACO and friends</h4>
<p>The <b>USACO benchmark</b> (Shi et al., 2024) brings the U.S. high
school computing olympiad problems into the same evaluation frame, with
careful contamination control. Other refreshes — Codeforces-Bench,
LiveCodeBench's contests slice — fill similar niches.</p>

<h4>What competitive programming actually measures</h4>
<p>It is a strong signal for <i>algorithmic reasoning</i> — graph
traversal, DP, number theory, ad-hoc combinatorics — and a reasonable
proxy for "this model can think." It is a weak signal for the work
real engineers do: navigating a 200k-line repo, fixing a flaky test,
adding a feature without breaking three others. Treat APPS and
CodeContests as the IQ-test slice of your eval, not the job-test slice.
That latter slice is what the next chapter is about.</p>
""",
        papers=[
            Paper(
                title="Measuring Coding Challenge Competence With APPS",
                authors="Hendrycks, Basart, Kadavath, Mazeika, Arora, Guo, et al.",
                year="2021",
                venue="NeurIPS",
                url="https://arxiv.org/abs/2105.09938",
                summary="10,000 coding problems graded across three difficulty levels. Strict pass-rate scoring; the de facto algorithmic benchmark before AlphaCode.",
            ),
            Paper(
                title="Competition-Level Code Generation with AlphaCode (CodeContests)",
                authors="Li, Choi, Chung, Kushman, Schrittwieser, Leblond, et al.",
                year="2022",
                venue="Science",
                url="https://arxiv.org/abs/2203.07814",
                summary="DeepMind's AlphaCode and the CodeContests dataset — Codeforces-style problems with extra generated tests and a sample-and-filter protocol.",
            ),
            Paper(
                title="Can Language Models Solve Olympiad Programming? (USACO)",
                authors="Shi, Tang, Narasimhan, Yao",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2404.10952",
                summary="USACO problems with contamination filtering and reflection-style scaffolding; isolates algorithmic reasoning vs. memorisation.",
            ),
            Paper(
                title="LiveCodeBench (contest split)",
                authors="Jain et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2403.07974",
                summary="LiveCodeBench's date-filtered Codeforces/LeetCode/AtCoder problems are the cleanest modern way to evaluate competitive coding.",
            ),
        ],
        extras=[
            Extra(
                label="APPS dataset on GitHub",
                url="https://github.com/hendrycks/apps",
            ),
            Extra(
                label="CodeContests dataset (DeepMind)",
                url="https://github.com/google-deepmind/code_contests",
            ),
            Extra(
                label="USACO bench repository",
                url="https://github.com/princeton-nlp/USACO",
            ),
        ],
    ),
    # ------------------------------------------------------------------ 15
    Chapter(
        id=15,
        slug="repository-and-swe-bench",
        part="IV. Coding and SWE Benchmarks",
        title="Repository-Level and SWE Tasks: SWE-bench, SWE-bench Verified, SWE-bench Lite, SWE-Lancer",
        summary_html="""
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
""",
        papers=[
            Paper(
                title="SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
                authors="Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan",
                year="2023",
                venue="ICLR 2024",
                url="https://arxiv.org/abs/2310.06770",
                summary="The original SWE-bench: 2,294 issues from 12 Python repos, multi-file patches, hidden pytest suites. Defined the modern coding-agent eval.",
            ),
            Paper(
                title="SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering",
                authors="Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press",
                year="2024",
                venue="NeurIPS",
                url="https://arxiv.org/abs/2405.15793",
                summary="The Agent-Computer Interface paper. Introduces a custom set of LLM-friendly shell tools and shows large gains over plain prompting on SWE-bench.",
            ),
            Paper(
                title="OpenHands: An Open Platform for AI Software Developers as Generalist Agents",
                authors="Wang, Li, Lin, Aroca-Ouellette, Han, Wang, et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.16741",
                summary="OpenHands (formerly OpenDevin). The dominant open-source agent harness, with sandboxed execution, browser tool, and a pluggable tool registry.",
            ),
            Paper(
                title="Agentless: Demystifying LLM-Based Software Engineering Agents",
                authors="Xia, Deng, Dunlap, Zhang, Yu, Zheng, Zhang, Wang",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.01489",
                summary="A deliberately non-agentic localise-repair-patch pipeline that competes with full agents on SWE-bench. Shows how much of the gain is retrieval, not autonomy.",
            ),
            Paper(
                title="Introducing SWE-bench Verified",
                authors="OpenAI",
                year="2024",
                venue="OpenAI blog",
                url="https://web.archive.org/web/2026/https://openai.com/index/introducing-swe-bench-verified/",
                summary="OpenAI's 500-task human-screened subset. The default leaderboard split for serious agent claims.",
            ),
        ],
        extras=[
            Extra(
                label="SWE-bench leaderboard",
                url="https://www.swebench.com/",
            ),
            Extra(
                label="SWE-bench source repo (Princeton NLP)",
                url="https://github.com/princeton-nlp/SWE-bench",
            ),
            Extra(
                label="OpenHands on GitHub (All-Hands-AI)",
                url="https://github.com/All-Hands-AI/OpenHands",
            ),
        ],
    ),
    # ------------------------------------------------------------------ 16
    Chapter(
        id=16,
        slug="setting-up-a-coding-agent-eval-harness",
        part="IV. Coding and SWE Benchmarks",
        title="Setting Up a Coding-Agent Eval Harness",
        summary_html="""
<p>Reading about benchmarks is one thing; running them is another. This
chapter is the practical recipe — what you actually need to wire up to
get real numbers for an open-source coding model. The goal is a
reproducible loop where you can swap models, change agents, and trust
the deltas.</p>

<h4>1. Pick a model</h4>
<p>For open-source coding work in 2026 the defaults are
<b>DeepSeek-Coder-V2</b>, <b>Qwen3-Coder</b>, <b>Code Llama</b>
descendants, and <b>StarCoder2</b>. Serve via <a href="https://github.com/vllm-project/vllm" target="_blank" rel="noopener">vLLM</a> for throughput
or <a href="https://ollama.com/" target="_blank" rel="noopener">Ollama</a> for convenience. Either way, expose an
OpenAI-compatible <code>/v1/chat/completions</code> endpoint — every
agent harness already speaks that protocol.</p>

<h4>2. Pick a harness</h4>
<ul>
  <li><b>SWE-agent</b> if you want the smallest, most-cited reference
  implementation.</li>
  <li><b>OpenHands</b> if you want the broadest tool surface and the
  best-maintained Docker sandboxing.</li>
  <li><b>Agentless</b> if you want a strong, cheap baseline before
  spending real money.</li>
</ul>

<h4>3. Pick a bench</h4>
<ul>
  <li><b>BigCodeBench</b> — hours of compute, function-level, fast
  iteration.</li>
  <li><b>SWE-bench Lite</b> — overnight on a small box, a real signal
  for agent capability.</li>
  <li><b>SWE-bench Verified</b> — the headline number, but plan for
  significant compute and a non-trivial dollar cost.</li>
</ul>

<h4>4. Isolate execution</h4>
<p>Every task runs the model's code. <b>Always</b> sandbox it. SWE-bench
ships per-repo Docker images; OpenHands runs each agent step inside a
container. Set wall-clock and step-count timeouts (5-10 minutes per
task is a reasonable starting point), cap memory, and disable network
access except where the task requires it. Log everything — full
trajectories, tool calls, stdout/stderr — so failures are debuggable.</p>

<h4>5. A minimal end-to-end recipe</h4>

<pre>
# 1. Serve the model with vLLM (one GPU, OpenAI-compatible API)
python -m vllm.entrypoints.openai.api_server \\
    --model deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct \\
    --port 8000 --max-model-len 32768

# 2. Clone OpenHands and SWE-bench
git clone https://github.com/All-Hands-AI/OpenHands
git clone https://github.com/princeton-nlp/SWE-bench

# 3. Run SWE-bench Lite via OpenHands
cd OpenHands
export LLM_API_BASE="http://localhost:8000/v1"
export LLM_API_KEY="dummy"
export LLM_MODEL="openai/deepseek-coder-v2-lite-instruct"

./evaluation/swe_bench/scripts/run_infer.sh \\
    --dataset princeton-nlp/SWE-bench_Lite \\
    --split test \\
    --max-iterations 30 \\
    --timeout 600 \\
    --output-dir runs/dsv2-lite-swebl

# 4. Score the patches with the official SWE-bench harness
cd ../SWE-bench
python -m swebench.harness.run_evaluation \\
    --predictions_path ../OpenHands/runs/dsv2-lite-swebl/preds.jsonl \\
    --max_workers 8 --run_id dsv2-lite-swebl
# -> prints %resolved and per-task pass/fail
</pre>

<h4>6. Sanity-check your numbers</h4>
<p>Compare against the public leaderboard. If your DeepSeek-Coder-V2
+ OpenHands run on Lite is wildly above or below published numbers,
something is wrong before something is interesting. Common bugs: wrong
chat template, truncated context window, agent silently giving up at
step 1, Docker images not actually rebuilding the patched code.</p>

<h4>7. Watch for contamination</h4>
<p>If your model scores suspiciously well on SWE-bench full but
mediocre on Verified or Live, suspect training-set leakage of the
public splits. Cross-check with LiveCodeBench post-cutoff problems —
a model that aces stale benches and falls apart on fresh ones is
giving you a memorisation score, not a capability score.</p>

<h4>8. Report honestly</h4>
<p>Always state: model + revision, harness + revision, exact split,
sampling parameters, max iterations, timeout, and total dollar/GPU
cost. A pass@1 on SWE-bench Verified means very different things at
20 iterations vs. 100, and at <code>T = 0</code> vs.
<code>T = 0.7</code>. Publish the trajectories if you can — the
community gets stronger when failures are inspectable.</p>
""",
        papers=[
            Paper(
                title="SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
                authors="Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan",
                year="2023",
                venue="ICLR 2024",
                url="https://arxiv.org/abs/2310.06770",
                summary="Reference paper for the SWE-bench harness, dataset structure, and grading protocol.",
            ),
            Paper(
                title="SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering",
                authors="Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press",
                year="2024",
                venue="NeurIPS",
                url="https://arxiv.org/abs/2405.15793",
                summary="The minimal-viable agent harness. Good baseline before adopting something heavier.",
            ),
            Paper(
                title="OpenHands: An Open Platform for AI Software Developers as Generalist Agents",
                authors="Wang, Li, Lin, Aroca-Ouellette, Han, Wang, et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.16741",
                summary="Modular open-source agent. Has a maintained SWE-bench evaluation pipeline you can run end-to-end.",
            ),
            Paper(
                title="BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions",
                authors="Zhuo et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2406.15877",
                summary="Cheaper than SWE-bench, harder than HumanEval. The right starting point for tight iteration loops.",
            ),
            Paper(
                title="Agentless: Demystifying LLM-Based Software Engineering Agents",
                authors="Xia, Deng, Dunlap, Zhang, Yu, Zheng, Zhang, Wang",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.01489",
                summary="Useful as a non-agentic baseline; if your fancy agent does not beat Agentless, your scaffolding is the problem.",
            ),
        ],
        extras=[
            Extra(
                label="SWE-bench leaderboard (compare your numbers here)",
                url="https://www.swebench.com/",
            ),
            Extra(
                label="OpenHands SWE-bench evaluation harness",
                url="https://github.com/All-Hands-AI/OpenHands",
            ),
            Extra(
                label="vLLM (OpenAI-compatible serving for open-source models)",
                url="https://github.com/vllm-project/vllm",
            ),
        ],
    ),
]
