---
id: 14
title: Competitive Programming: CodeContests, APPS
part: IV. Coding and SWE Benchmarks
---

# Competitive Programming: CodeContests, APPS

*IV. Coding and SWE Benchmarks*

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

## Papers and references

### Measuring Coding Challenge Competence With APPS
- **Authors:** Hendrycks, Basart, Kadavath, Mazeika, Arora, Guo, et al.
- **Year:** 2021
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2105.09938

10,000 coding problems graded across three difficulty levels. Strict pass-rate scoring; the de facto algorithmic benchmark before AlphaCode.

### Competition-Level Code Generation with AlphaCode (CodeContests)
- **Authors:** Li, Choi, Chung, Kushman, Schrittwieser, Leblond, et al.
- **Year:** 2022
- **Venue:** Science
- **URL:** https://arxiv.org/abs/2203.07814

DeepMind's AlphaCode and the CodeContests dataset — Codeforces-style problems with extra generated tests and a sample-and-filter protocol.

### Can Language Models Solve Olympiad Programming? (USACO)
- **Authors:** Shi, Tang, Narasimhan, Yao
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2404.10952

USACO problems with contamination filtering and reflection-style scaffolding; isolates algorithmic reasoning vs. memorisation.

### LiveCodeBench (contest split)
- **Authors:** Jain et al.
- **Year:** 2024
- **Venue:** arXiv
- **URL:** https://arxiv.org/abs/2403.07974

LiveCodeBench's date-filtered Codeforces/LeetCode/AtCoder problems are the cleanest modern way to evaluate competitive coding.

## Extras
- [APPS dataset on GitHub](https://github.com/hendrycks/apps)
- [CodeContests dataset (DeepMind)](https://github.com/google-deepmind/code_contests)
- [USACO bench repository](https://github.com/princeton-nlp/USACO)
