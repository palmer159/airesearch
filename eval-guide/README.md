# Eval Guide: Testing and Benchmarking Open SLMs and LLMs

A companion study guide to the main airesearch LLM Study Guide, focused on
**how to test and benchmark open-source and open-weight SLMs and LLMs** —
with extra depth on **coding agents** and **software-engineering benchmarks**.

It is organized into **5 sections** and **20 chapters total**:

1. **Foundations of evaluation** — what we measure, why it's hard, the
   contamination problem, and the difference between capability and behavior.
2. **The model landscape** — open-source and open-weight families to test
   (Llama, Qwen, DeepSeek, Mistral, Gemma, Phi, SmolLM, plus coding-specific
   models like StarCoder and Code Llama).
3. **General-purpose benchmarks** — MMLU, MMLU-Pro, GPQA, BBH, IFEval, GSM8K,
   MATH, ARC, HellaSwag — what each one actually tests and how to read the
   numbers.
4. **Coding and SWE benchmarks** — HumanEval, MBPP, LiveCodeBench, BigCodeBench,
   SWE-bench (Verified, Lite, Live), CodeContests, MultiPL-E, ClassEval — and
   how to set up a coding-agent harness.
5. **Methodology** — running evals, prompting & few-shot, sampling & temperature,
   reproducibility, statistical significance, leaderboards, contamination
   defense, and a benchmark-shopping checklist.

Every reference is open-access. No paywalls.

## Quick start

The eval guide is regenerated from `regenerate.py`:

```bash
python3 eval-guide/regenerate.py
```

This wipes `eval-guide/chapters/`, recreates each chapter's `README.md`, and
rewrites this file. Per-chapter progress prints to stdout.

To browse: each `eval-guide/chapters/NN-slug/` directory contains a
`README.md` that GitHub renders inline when you click into the folder.

## Curriculum

### I. Foundations of LLM/SLM Evaluation

1. [Why Evaluation Matters: Capability vs. Behavior](chapters/01-why-evaluation-matters/)
2. [What Makes a Good Benchmark](chapters/02-what-makes-a-good-benchmark/)
3. [Data Contamination and Leakage](chapters/03-contamination-and-data-leakage/)

### II. The Open Model Landscape

4. [Open-Source vs. Open-Weight Models](chapters/04-open-source-vs-open-weight/)
5. [General-Purpose Open Models: Llama, Qwen, DeepSeek, Mistral, Gemma](chapters/05-general-purpose-llm-families/)
6. [Small Language Models: Phi, SmolLM, TinyLlama](chapters/06-small-language-models/)
7. [Coding-Specific Open Models: Code Llama, StarCoder, DeepSeek-Coder, Qwen-Coder](chapters/07-coding-specific-models/)

### III. General-Purpose Benchmarks

8. [Knowledge and Reasoning: MMLU, MMLU-Pro, GPQA](chapters/08-knowledge-and-reasoning-mmlu-mmlu-pro-gpqa/)
9. [Reasoning and Multi-Step: BBH, ARC, HellaSwag](chapters/09-reasoning-and-multistep-bbh-arc-hellaswag/)
10. [Math: GSM8K, MATH, and AIME](chapters/10-math-gsm8k-math-aime/)
11. [Instruction-Following and Chat: IFEval, MT-Bench, Chatbot Arena](chapters/11-instruction-following-and-chat-ifeval-mt-bench-arena/)

### IV. Coding and SWE Benchmarks

12. [Function-Level: HumanEval, MBPP, MultiPL-E](chapters/12-function-level-humaneval-mbpp-multipl-e/)
13. [Harder and Fresher: LiveCodeBench, BigCodeBench, ClassEval](chapters/13-harder-and-fresher-livecodebench-bigcodebench-classeval/)
14. [Competitive Programming: CodeContests, APPS](chapters/14-competitive-programming-codecontests-apps/)
15. [Repository-Level and SWE Tasks: SWE-bench, SWE-bench Verified, SWE-bench Lite, SWE-Lancer](chapters/15-repository-and-swe-bench/)
16. [Setting Up a Coding-Agent Eval Harness](chapters/16-setting-up-a-coding-agent-eval-harness/)

### V. Methodology: Running Evals in Practice

17. [Prompting, Few-Shot, and Sampling](chapters/17-prompting-few-shot-and-sampling/)
18. [Reproducibility and Statistical Significance](chapters/18-reproducibility-and-statistical-significance/)
19. [Leaderboards: Open LLM, BigCode, SWE-bench, Arena](chapters/19-leaderboards-and-arena/)
20. [Picking and Running an Eval Suite: A Practical Checklist](chapters/20-picking-and-running-an-eval-suite/)

## License

Chapter prose: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).
Linked papers and resources retain their original licenses.
