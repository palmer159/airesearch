---
id: 16
title: Setting Up a Coding-Agent Eval Harness
part: IV. Coding and SWE Benchmarks
---

# Setting Up a Coding-Agent Eval Harness

*IV. Coding and SWE Benchmarks*

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
python -m vllm.entrypoints.openai.api_server \
    --model deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct \
    --port 8000 --max-model-len 32768

# 2. Clone OpenHands and SWE-bench
git clone https://github.com/All-Hands-AI/OpenHands
git clone https://github.com/princeton-nlp/SWE-bench

# 3. Run SWE-bench Lite via OpenHands
cd OpenHands
export LLM_API_BASE="http://localhost:8000/v1"
export LLM_API_KEY="dummy"
export LLM_MODEL="openai/deepseek-coder-v2-lite-instruct"

./evaluation/swe_bench/scripts/run_infer.sh \
    --dataset princeton-nlp/SWE-bench_Lite \
    --split test \
    --max-iterations 30 \
    --timeout 600 \
    --output-dir runs/dsv2-lite-swebl

# 4. Score the patches with the official SWE-bench harness
cd ../SWE-bench
python -m swebench.harness.run_evaluation \
    --predictions_path ../OpenHands/runs/dsv2-lite-swebl/preds.jsonl \
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

## Papers and references

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Authors:** Jimenez, Yang, Wettig, Yao, Pei, Press, Narasimhan
- **Year:** 2023
- **Venue:** ICLR 2024
- **URL:** https://arxiv.org/abs/2310.06770

Reference paper for the SWE-bench harness, dataset structure, and grading protocol.

### SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- **Authors:** Yang, Jimenez, Wettig, Lieret, Yao, Narasimhan, Press
- **Year:** 2024
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2405.15793

The minimal-viable agent harness. Good baseline before adopting something heavier.

### OpenHands: An Open Platform for AI Software Developers as Generalist Agents
- **Authors:** Wang, Li, Lin, Aroca-Ouellette, Han, Wang, et al.
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.16741

Modular open-source agent. Has a maintained SWE-bench evaluation pipeline you can run end-to-end.

### BigCodeBench: Benchmarking Code Generation with Diverse Function Calls and Complex Instructions
- **Authors:** Zhuo et al.
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2406.15877

Cheaper than SWE-bench, harder than HumanEval. The right starting point for tight iteration loops.

### Agentless: Demystifying LLM-Based Software Engineering Agents
- **Authors:** Xia, Deng, Dunlap, Zhang, Yu, Zheng, Zhang, Wang
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2407.01489

Useful as a non-agentic baseline; if your fancy agent does not beat Agentless, your scaffolding is the problem.

## Extras
- [SWE-bench leaderboard (compare your numbers here)](https://www.swebench.com/)
- [OpenHands SWE-bench evaluation harness](https://github.com/All-Hands-AI/OpenHands)
- [vLLM (OpenAI-compatible serving for open-source models)](https://github.com/vllm-project/vllm)
