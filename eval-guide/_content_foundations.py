"""Section I — Foundations of LLM/SLM Evaluation.

The opening three chapters of the eval-guide.  They set up the vocabulary
the rest of the guide will rely on: what evaluation actually means, what
makes a benchmark trustworthy, and the contamination problem that quietly
invalidates a lot of headline numbers.

Voice: friendly, intuition-first, technically precise.  HTML body.
Citations: open-access only (arXiv, Wikipedia, lab CDNs, HuggingFace,
GitHub, BAIR/Stanford CRFM).
"""

from _chapter_types import Chapter, Paper, Extra


FOUNDATIONS_CHAPTERS: list[Chapter] = [
    # ------------------------------------------------------------------ #
    # 1. Why Evaluation Matters: Capability vs. Behavior
    # ------------------------------------------------------------------ #
    Chapter(
        id=1,
        slug="why-evaluation-matters",
        part="I. Foundations of LLM/SLM Evaluation",
        title="Why Evaluation Matters: Capability vs. Behavior",
        summary_html="""\
<p>Before we run a single benchmark, it's worth being precise about what
"evaluating a model" even means.  A language model is a probability
distribution over tokens; everything else — answering questions, writing
code, refusing harmful requests — is downstream behavior we coax out of
that distribution with a prompt.  Evaluation is the discipline of
quantifying how good those behaviors are.</p>

<h4>Three things people mean by "evaluation"</h4>
<ul>
  <li><b>Capability</b> — can the model, in principle, do the task?
  Solve a math problem, translate a sentence, write a working SQL
  query.  Measured with task accuracy on benchmarks like MMLU,
  GSM8K, HumanEval.</li>
  <li><b>Behavior</b> — how does it act in the wild?  Is it helpful,
  honest, calibrated, concise?  Measured with human preference,
  rubric-graded rollouts, and red-teaming.</li>
  <li><b>Alignment / safety</b> — does it refuse the things it should
  and only the things it should?  Measured with harm benchmarks,
  jailbreak suites, and policy compliance evals.</li>
</ul>

<h4>Intrinsic vs. extrinsic</h4>
<p>The oldest split in NLP eval is between <b>intrinsic</b> metrics
that score the model's distribution directly — most famously
<a href="https://en.wikipedia.org/wiki/Perplexity" target="_blank" rel="noopener">perplexity</a>
on a held-out corpus — and <b>extrinsic</b> metrics that score the
model on a downstream task.  Perplexity is cheap and continuous, which
makes it lovely for tracking pre-training runs, but it correlates only
loosely with what users actually care about.  A 5% perplexity
improvement might or might not move HumanEval at all.</p>

<h4>Why a single benchmark number lies</h4>
<p>Any one benchmark probes a narrow slice of behavior on a fixed
distribution of inputs.  Optimize for it and you get
<a href="https://en.wikipedia.org/wiki/Goodhart%27s_law" target="_blank" rel="noopener">Goodhart's law</a>
in action: the metric stops measuring the thing once the thing is
being measured.  Models can be trained, tuned, or even prompted in
ways that hill-climb a leaderboard while regressing on capabilities
the leaderboard doesn't see.</p>

<p>The fix is a <b>basket</b> of evals — broad coverage across
capabilities, behaviors, and risks, scored with multiple metrics,
across multiple prompt formats.  Stanford CRFM's
<a href="https://crfm.stanford.edu/helm/" target="_blank" rel="noopener">HELM</a>
("Holistic Evaluation of Language Models") is the canonical attempt
at this: dozens of scenarios crossed with seven metric categories
(accuracy, calibration, robustness, fairness, bias, toxicity,
efficiency).  Even that isn't the whole picture, but it's the right
shape: many tasks, many metrics, reported together rather than
collapsed into a single number.</p>
""",
        papers=[
            Paper(
                title="Holistic Evaluation of Language Models (HELM)",
                authors="Liang, Bommasani, Lee, et al.",
                year="2022",
                venue="arXiv / TMLR",
                url="https://arxiv.org/abs/2211.09110",
                summary="The reference framework for multi-metric, multi-scenario LM evaluation. Proposes evaluating across accuracy, calibration, robustness, fairness, bias, toxicity, and efficiency on dozens of scenarios.",
            ),
            Paper(
                title="BIG-Bench: Beyond the Imitation Game",
                authors="Srivastava et al.",
                year="2022",
                venue="arXiv / TMLR",
                url="https://arxiv.org/abs/2206.04615",
                summary="A 200+ task collaborative benchmark designed to probe capabilities current LMs are bad at. Defined the modern shape of broad-coverage capability evaluation.",
            ),
            Paper(
                title="Perplexity",
                authors="Wikipedia contributors",
                year="2025",
                venue="Wikipedia",
                url="https://en.wikipedia.org/wiki/Perplexity",
                summary="The standard intrinsic metric for language models: exp of average per-token negative log-likelihood. Lower is better; correlates loosely with downstream task performance.",
            ),
            Paper(
                title="Goodhart's Law",
                authors="Wikipedia contributors",
                year="2025",
                venue="Wikipedia",
                url="https://en.wikipedia.org/wiki/Goodhart%27s_law",
                summary="\"When a measure becomes a target, it ceases to be a good measure.\" The structural reason single-benchmark optimization breaks down in practice.",
            ),
            Paper(
                title="Evaluating Large Language Models: A Survey",
                authors="Chang et al.",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2307.03109",
                summary="A broad survey covering what to evaluate (capabilities, alignment, safety), where to evaluate, and how — useful as a map of the eval landscape.",
            ),
        ],
        extras=[
            Extra(
                label="HELM Lite leaderboard (Stanford CRFM)",
                url="https://crfm.stanford.edu/helm/lite/latest/",
            ),
            Extra(
                label="Lilian Weng — LLM Evaluation",
                url="https://lilianweng.github.io/posts/2023-06-23-agent/",
            ),
        ],
    ),
    # ------------------------------------------------------------------ #
    # 2. What Makes a Good Benchmark
    # ------------------------------------------------------------------ #
    Chapter(
        id=2,
        slug="what-makes-a-good-benchmark",
        part="I. Foundations of LLM/SLM Evaluation",
        title="What Makes a Good Benchmark",
        summary_html="""\
<p>Most benchmarks you'll encounter are bad in at least one specific,
fixable way.  Knowing the failure modes makes you a better consumer
of leaderboards and a much better designer of internal evals.</p>

<h4>The properties to look for</h4>
<ul>
  <li><b>Construct validity</b> — the benchmark actually measures the
  capability it claims to measure.  A "reasoning" benchmark that any
  retrieval-heavy model can solve by pattern-matching does not have
  construct validity.</li>
  <li><b>Coverage</b> — enough breadth across sub-skills, domains,
  difficulty levels, and input formats that no single trick wins.</li>
  <li><b>Discriminative power</b> — different models get visibly
  different scores.  If everyone clusters at 92–94%, the benchmark
  isn't telling you anything new.</li>
  <li><b>Headroom</b> — room left at the top.  Once frontier models
  exceed ~95% on a clean benchmark, it has effectively
  <b>saturated</b>: you can't tell a great model from a stunning one.
  This is what happened to the original GLUE, then SuperGLUE, then
  parts of MMLU.</li>
  <li><b>Easy automated grading</b> — a stable, reproducible scorer
  that doesn't itself need a frontier LLM in the loop.  Exact-match,
  unit tests, and regex graders are boring but trustworthy.</li>
  <li><b>Public vs. hidden splits</b> — public examples teach the
  community the format; a hidden test set you submit against keeps
  numbers honest.  BIG-Bench Hard, Kaggle-style hidden tests, and
  the SWE-bench leaderboard servers all use this pattern.</li>
</ul>

<h4>Two grading idioms you'll see everywhere</h4>
<ul>
  <li><b>Exact-match / multiple-choice</b> — the model's output
  string must equal the gold label, or its top-probability choice
  among A/B/C/D must match.  Cheap, deterministic, but brittle: a
  correct answer phrased differently scores zero, and MCQ removes
  the generation problem entirely.</li>
  <li><b>pass@k for code</b> — sample k completions, count the
  problem solved if any one passes the unit tests.  Originally
  defined in the
  <a href="https://arxiv.org/abs/2107.03374" target="_blank" rel="noopener">HumanEval / Codex paper</a>:</li>
</ul>

<pre>
pass@k = E_problems [ 1 - C(n - c, k) / C(n, k) ]

where n = total samples drawn per problem,
      c = number of those samples that pass,
      C(a, b) = a-choose-b
</pre>

<p>This unbiased estimator lets you draw n &gt;&gt; k samples once and
report pass@1, pass@10, pass@100 from the same run.</p>

<h4>Saturation and the next bench</h4>
<p>When 99% means "the bench is dead," the community responds by
building harder versions.
<a href="https://arxiv.org/abs/2210.09261" target="_blank" rel="noopener">BIG-Bench Hard</a>
is the 23 tasks from BIG-Bench where models still struggled; it
extended useful headroom by another generation of models.  HELM
itself is partly a response to GLUE-style saturation: instead of one
score going to 1.0, you get a dashboard where progress and
regressions are both visible.</p>
""",
        papers=[
            Paper(
                title="Holistic Evaluation of Language Models (HELM)",
                authors="Liang, Bommasani, Lee, et al.",
                year="2022",
                venue="arXiv / TMLR",
                url="https://arxiv.org/abs/2211.09110",
                summary="Beyond capability scoring: HELM treats benchmarks themselves as objects to evaluate (coverage, validity, missing metrics) and standardizes a multi-metric reporting format.",
            ),
            Paper(
                title="Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them (BBH)",
                authors="Suzgun et al.",
                year="2022",
                venue="arXiv / ACL Findings",
                url="https://arxiv.org/abs/2210.09261",
                summary="The 23 BIG-Bench tasks where models scored below the average human rater. The de-facto \"hard reasoning\" subset and a useful case study in restoring headroom.",
            ),
            Paper(
                title="Evaluating Large Language Models Trained on Code (HumanEval / Codex)",
                authors="Chen et al.",
                year="2021",
                venue="arXiv",
                url="https://arxiv.org/abs/2107.03374",
                summary="Introduced HumanEval and the pass@k metric. The grading template — sample, run unit tests, count solved — is the basis for almost every modern code benchmark.",
            ),
            Paper(
                title="BIG-Bench: Beyond the Imitation Game",
                authors="Srivastava et al.",
                year="2022",
                venue="arXiv / TMLR",
                url="https://arxiv.org/abs/2206.04615",
                summary="The original 200+ task collection. A long case study in coverage, construct validity, and what happens when you let hundreds of authors propose tasks.",
            ),
            Paper(
                title="Goodhart's Law",
                authors="Wikipedia contributors",
                year="2025",
                venue="Wikipedia",
                url="https://en.wikipedia.org/wiki/Goodhart%27s_law",
                summary="The structural reason saturated benchmarks stop being informative: once the score is the goal, the score stops measuring the underlying capability.",
            ),
        ],
        extras=[
            Extra(
                label="HELM Lite latest results",
                url="https://crfm.stanford.edu/helm/lite/latest/",
            ),
            Extra(
                label="BIG-Bench repository (Google / collaboration)",
                url="https://github.com/google/BIG-bench",
            ),
            Extra(
                label="HumanEval repository (OpenAI)",
                url="https://github.com/openai/human-eval",
            ),
        ],
    ),
    # ------------------------------------------------------------------ #
    # 3. Data Contamination and Leakage
    # ------------------------------------------------------------------ #
    Chapter(
        id=3,
        slug="contamination-and-data-leakage",
        part="I. Foundations of LLM/SLM Evaluation",
        title="Data Contamination and Leakage",
        summary_html="""\
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
""",
        papers=[
            Paper(
                title="Data Contamination Quiz: A Tool to Detect and Estimate Contamination in LLMs",
                authors="Golchin & Surdeanu",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2310.18018",
                summary="A practical method for probing whether a closed model has seen specific benchmark instances, framed as a multiple-choice quiz over original vs. perturbed examples.",
            ),
            Paper(
                title="LiveCodeBench: Holistic and Contamination-Free Evaluation of LLMs for Code",
                authors="Jain et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2403.07974",
                summary="A code benchmark that continuously incorporates problems posted after model training cutoffs, so each evaluation window is provably out of distribution for the models being scored.",
            ),
            Paper(
                title="SWE-bench: Can Language Models Resolve Real-World GitHub Issues?",
                authors="Jimenez, Yang, Wettig, et al.",
                year="2023",
                venue="arXiv / ICLR",
                url="https://arxiv.org/abs/2310.06770",
                summary="Real GitHub issues + repository state + reference patches. The original benchmark; SWE-bench Verified is the human-curated, cleanly-specified subset built on top of it.",
            ),
            Paper(
                title="Introducing SWE-bench Verified",
                authors="OpenAI",
                year="2024",
                venue="OpenAI Blog",
                url="https://openai.com/index/introducing-swe-bench-verified/",
                summary="A 500-task subset of SWE-bench, manually filtered for spec quality and grader correctness. The current standard reporting target for agentic coding.",
            ),
            Paper(
                title="HumanEval / Codex",
                authors="Chen et al.",
                year="2021",
                venue="arXiv",
                url="https://arxiv.org/abs/2107.03374",
                summary="The benchmark whose web-mirrored solutions are the canonical case study in code-eval contamination — and the reason careful labs decontaminate training data against it.",
            ),
            Paper(
                title="BIG-Bench: Beyond the Imitation Game",
                authors="Srivastava et al.",
                year="2022",
                venue="arXiv / TMLR",
                url="https://arxiv.org/abs/2206.04615",
                summary="Shipped explicit canary strings inside the benchmark so future models can be checked for memorization. A reusable pattern for any new public benchmark.",
            ),
        ],
        extras=[
            Extra(
                label="SWE-bench leaderboard",
                url="https://www.swebench.com/",
            ),
            Extra(
                label="LiveCodeBench leaderboard",
                url="https://livecodebench.github.io/",
            ),
            Extra(
                label="StarCoder paper (decontamination methodology)",
                url="https://arxiv.org/abs/2305.06161",
            ),
        ],
    ),
]
