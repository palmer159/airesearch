---
id: 3
title: Data Contamination and Leakage
part: I. Foundations of LLM/SLM Evaluation
---

# Data Contamination and Leakage

*I. Foundations of LLM/SLM Evaluation*

<p>The dirtiest open secret in LLM evaluation is that the training
data probably ate your test set.  Modern pre-training corpora are
trillions of tokens scraped from the open web; many popular
benchmarks are also on the open web; the intersection is non-empty.
A model that has memorized HumanEval problem 47 isn't being
evaluated, it's being quizzed on its homework.</p>

<h4>Why this is hard to avoid</h4>
<ul>
  <li>Benchmarks like MMLU, GSM8K, HumanEval, and HellaSwag are all
  scraped, mirrored, and discussed across thousands of GitHub repos,
  blog posts, and Stack Overflow answers.</li>
  <li>Even when the original test split is held out, paraphrases,
  solutions, and partial leaks live in the wild.</li>
  <li>Frontier labs rarely publish full training data, so external
  researchers can't directly check overlap.</li>
</ul>

<h4>How people actually test for contamination</h4>
<ul>
  <li><b>n-gram overlap</b> — for each test example, check whether
  long n-grams (often 13-grams or 50-character windows) from it
  appear in the training corpus.  Crude but fast.</li>
  <li><b>Canary strings</b> — embed unique, unguessable strings in
  the benchmark.  If the model can complete or recite them, the
  benchmark is in its training data.  BIG-Bench shipped explicit
  canaries for this purpose.</li>
  <li><b>Membership inference / log-prob gap</b> — compare the
  model's perplexity on the test set vs. a freshly-collected,
  identically-distributed control set.  A suspiciously large gap is
  evidence of memorization.</li>
  <li><b>Held-out / "Verified" / "Live" splits</b> — the cleanest
  defense.
  <a href="https://arxiv.org/abs/2403.07974" target="_blank" rel="noopener">LiveCodeBench</a>
  continuously adds problems posted <i>after</i> a model's training
  cutoff;
  <a href="https://openai.com/index/introducing-swe-bench-verified/" target="_blank" rel="noopener">SWE-bench Verified</a>
  is a human-curated subset of
  <a href="https://arxiv.org/abs/2310.06770" target="_blank" rel="noopener">SWE-bench</a>
  with cleaner specs and known provenance.</li>
</ul>

<pre>
# Sketch: 13-gram contamination check
def contaminated(example, training_index, n=13):
    tokens = tokenize(example.prompt + example.answer)
    for i in range(len(tokens) - n + 1):
        ngram = tuple(tokens[i:i + n])
        if ngram in training_index:
            return True
    return False
</pre>

<h4>The Phi / StarCoder / GPT-4 debates</h4>
<p>Three episodes are worth knowing.  Microsoft's <b>Phi</b> models
were accused of being trained on data suspiciously close to common
benchmarks; the team published contamination analyses in response.
<b>StarCoder</b> shipped with explicit decontamination of its
training set against HumanEval and MBPP, and documented the
process — a good template.  <b>GPT-4</b>'s technical report
acknowledged contamination on several benchmarks and reported
"contamination-adjusted" numbers alongside the raw ones.</p>

<p>The takeaway is not "every result is fake."  It's that any
benchmark older than the model's training cutoff should be treated
as <i>potentially</i> contaminated, and the trustworthy numbers come
from live splits, hidden test sets, and benchmarks designed with
contamination defenses in mind.</p>

## Papers and references

### Data Contamination Quiz: A Tool to Detect and Estimate Contamination in LLMs
- **Authors:** Golchin & Surdeanu
- **Year:** 2023
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2310.18018

A practical method for probing whether a closed model has seen specific benchmark instances, framed as a multiple-choice quiz over original vs. perturbed examples.

### LiveCodeBench: Holistic and Contamination-Free Evaluation of LLMs for Code
- **Authors:** Jain et al.
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2403.07974

A code benchmark that continuously incorporates problems posted after model training cutoffs, so each evaluation window is provably out of distribution for the models being scored.

### SWE-bench: Can Language Models Resolve Real-World GitHub Issues?
- **Authors:** Jimenez, Yang, Wettig, et al.
- **Year:** 2023
- **Venue:** arXiv / ICLR
- **URL:** https://arxiv.org/abs/2310.06770

Real GitHub issues + repository state + reference patches. The original benchmark; SWE-bench Verified is the human-curated, cleanly-specified subset built on top of it.

### Introducing SWE-bench Verified
- **Authors:** OpenAI
- **Year:** 2024
- **Venue:** OpenAI Blog
- **URL:** https://openai.com/index/introducing-swe-bench-verified/

A 500-task subset of SWE-bench, manually filtered for spec quality and grader correctness. The current standard reporting target for agentic coding.

### HumanEval / Codex
- **Authors:** Chen et al.
- **Year:** 2021
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2107.03374

The benchmark whose web-mirrored solutions are the canonical case study in code-eval contamination — and the reason careful labs decontaminate training data against it.

### BIG-Bench: Beyond the Imitation Game
- **Authors:** Srivastava et al.
- **Year:** 2022
- **Venue:** arXiv / TMLR
- **URL:** https://arxiv.org/abs/2206.04615

Shipped explicit canary strings inside the benchmark so future models can be checked for memorization. A reusable pattern for any new public benchmark.

## Extras
- [SWE-bench leaderboard](https://www.swebench.com/)
- [LiveCodeBench leaderboard](https://livecodebench.github.io/)
- [StarCoder paper (decontamination methodology)](https://arxiv.org/abs/2305.06161)
