"""Section V — Methodology: Running Evals in Practice.

Chapters 17-20 of the eval guide. Practical advice on how to actually run
benchmarks, get reproducible numbers, read leaderboards, and pick a suite.
"""

from _chapter_types import Chapter, Paper, Extra


METHODOLOGY_CHAPTERS: list[Chapter] = [
    Chapter(
        id=17,
        slug="prompting-few-shot-and-sampling",
        part="V. Methodology: Running Evals in Practice",
        title="Prompting, Few-Shot, and Sampling",
        summary_html="""<p>An open-weight model has no single "score". The number you get on a
benchmark depends on how you prompted it, how many examples you showed it,
and how you sampled. If you change any of these and forget to say so, you
have not measured the model — you have measured your own setup.</p>

<h4>Zero-shot, few-shot, and chain-of-thought</h4>
<ul>
  <li><b>Zero-shot</b>: just the question. Hard for small models, fair for
  instruction-tuned ones.</li>
  <li><b>Few-shot (k-shot)</b>: prepend k worked examples. MMLU is canonically
  reported 5-shot. Big wins for base models, modest for instruct models.</li>
  <li><b>Chain-of-thought</b>: tell the model "think step by step". GSM8K and
  MATH are usually CoT. Many leaderboards now use 0-shot CoT for everything.</li>
</ul>

<p>Prompt format matters more than people think. The same MMLU question
phrased "Question: X\\nA) … B) …" vs "&lt;|user|&gt; X" can swing 5-10 points.
Always publish the exact template; cite the harness's default if you used
one.</p>

<h4>Sampling parameters</h4>
<p>Three knobs: temperature (how peaky the next-token distribution is), top-p
(keep only the smallest set of tokens whose mass ≥ p), and top-k (keep the k
most-likely). For greedy/deterministic eval use temperature=0 and seed your
RNG. For pass@k metrics — where you want to measure "given k tries, did at
least one work" — use temperature ≈ 0.6-0.8 and draw k samples per problem.</p>

<pre>
# pass@k bias-corrected estimator (Codex paper)
# n = total samples drawn, c = number that passed, k = budget
pass_at_k(n, c, k) = 1 - C(n - c, k) / C(n, k)
</pre>

<h4>Tooling</h4>
<p>EleutherAI's <b>lm-evaluation-harness</b> is the closest thing to a
community standard. It handles few-shot formatting, log-likelihood vs
generative grading, and dozens of public benchmarks. Hugging Face's Open LLM
Leaderboard pins specific commits of it so numbers are comparable.</p>

<p>For coding evals use BigCode's <code>bigcode-evaluation-harness</code> for
HumanEval/MBPP/MultiPL-E and the official SWE-bench harness for agentic
tasks.</p>""",
        papers=[
            Paper(
                title="Language Models are Few-Shot Learners (GPT-3)",
                authors="Brown et al.",
                year="2020",
                url="https://arxiv.org/abs/2005.14165",
                summary="Coined few-shot in-context learning as the eval mode for instruction-less base models. The k=5 / k=32 conventions trace to this paper.",
            ),
            Paper(
                title="Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
                authors="Wei et al.",
                year="2022",
                url="https://arxiv.org/abs/2201.11903",
                summary="The original CoT paper — adding 'let's think step by step' style demonstrations gave huge boosts on GSM8K and arithmetic, and reframed how reasoning benchmarks are run.",
            ),
            Paper(
                title="Self-Consistency Improves Chain of Thought Reasoning in Language Models",
                authors="Wang et al.",
                year="2022",
                url="https://arxiv.org/abs/2203.11171",
                summary="Sample many CoT traces at temperature > 0, take the majority answer. The standard 'maj@N' protocol on math benches comes from here.",
            ),
            Paper(
                title="Evaluating Large Language Models Trained on Code (Codex / HumanEval)",
                authors="Chen et al.",
                year="2021",
                url="https://arxiv.org/abs/2107.03374",
                summary="Defines pass@k and the bias-corrected estimator everyone now reports. Section 2 of the paper is the source of truth for the formula.",
            ),
            Paper(
                title="A Framework for Few-Shot Language Model Evaluation",
                authors="Gao et al.",
                year="2023",
                url="https://github.com/EleutherAI/lm-evaluation-harness",
                summary="lm-eval-harness — the community-standard runner. Pinning a specific commit hash is the difference between comparable and incomparable numbers.",
                venue="GitHub / EleutherAI",
            ),
            Paper(
                title="Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design",
                authors="Sclar et al.",
                year="2023",
                url="https://arxiv.org/abs/2310.11324",
                summary="Same task, same model, eight cosmetic prompt variations: scores swing >50 points. The empirical case for always publishing the exact template.",
            ),
        ],
        extras=[
            Extra(label="lm-evaluation-harness (EleutherAI)", url="https://github.com/EleutherAI/lm-evaluation-harness"),
            Extra(label="bigcode-evaluation-harness", url="https://github.com/bigcode-project/bigcode-evaluation-harness"),
            Extra(label="HuggingFace generation parameter docs", url="https://huggingface.co/docs/transformers/generation_strategies"),
        ],
    ),

    Chapter(
        id=18,
        slug="reproducibility-and-statistical-significance",
        part="V. Methodology: Running Evals in Practice",
        title="Reproducibility and Statistical Significance",
        summary_html="""<p>Treat a benchmark number the way you would treat any experiment: it
is a noisy estimate of an underlying quantity. The two questions you must
answer about every reported score are <i>can someone re-run this</i> and
<i>is the difference real</i>.</p>

<h4>What to report so others can reproduce</h4>
<ul>
  <li>Model name <b>and</b> revision (HF commit SHA, GGUF quant level, lora adapter).</li>
  <li>Harness name <b>and</b> commit SHA.</li>
  <li>Exact prompt template (or its name in the harness).</li>
  <li>Sampling: temperature, top-p, top-k, max-new-tokens, seed.</li>
  <li>Hardware + inference engine (vLLM 0.6.3, llama.cpp commit, etc.) — batched
  inference is non-deterministic on GPUs even at temperature=0 because
  reductions reorder, so the engine matters.</li>
  <li>Few-shot k and which examples (the harness usually fixes this).</li>
</ul>

<h4>Is the difference real?</h4>
<p>A benchmark with N items and a binary pass/fail metric has a standard
error of roughly sqrt(p(1-p)/N). For MMLU (N≈14k) at p=0.7 that is ≈0.4
points; a 1-point gap is borderline. For GPQA Diamond (N=198) at p=0.5 that
is ≈3.5 points; a 5-point gap is barely real. Bootstrap confidence intervals
let you compute this without assuming a Gaussian — re-sample the items with
replacement many times, recompute the score, take the 2.5/97.5 percentiles.</p>

<pre>
# 95% bootstrap CI for accuracy on N items
import numpy as np
correct = np.array([...])           # 1/0 per item, length N
B = 10_000
samples = [correct[np.random.randint(0, len(correct), len(correct))].mean()
           for _ in range(B)]
lo, hi = np.percentile(samples, [2.5, 97.5])
</pre>

<p>For pairwise comparisons (model A vs model B on the same items) use a
paired bootstrap or McNemar's test — they are tighter than two independent
CIs because they exploit per-item correlation.</p>

<h4>Hidden non-determinism</h4>
<p>Even with temperature=0 and a fixed seed, vLLM, TGI, and SGLang can
produce different outputs across batch sizes due to floating-point reduction
order. Always pin engine version <i>and</i> batch configuration. The Open
LLM Leaderboard pins both.</p>""",
        papers=[
            Paper(
                title="What's In My Big Data? (and reproducibility crises in LM eval)",
                authors="Elazar et al.",
                year="2023",
                url="https://arxiv.org/abs/2310.20707",
                summary="Argues that without dataset and decoding transparency, reported LM scores are not reproducible — a position paper widely cited by leaderboard maintainers.",
            ),
            Paper(
                title="Don't Make Your LLM an Evaluation Benchmark Cheater",
                authors="Zhou et al.",
                year="2023",
                url="https://arxiv.org/abs/2311.01964",
                summary="Empirically shows how minor harness differences (prompt format, log-likelihood vs generation, normalization) shift MMLU and other scores by 5-20 points across the 'same' eval.",
            ),
            Paper(
                title="A Critical Evaluation of Evaluations for Long-form Question Answering",
                authors="Xu et al.",
                year="2023",
                url="https://arxiv.org/abs/2305.18201",
                summary="Practical guide on reporting confidence intervals and avoiding the 'one-run-and-done' trap; the bootstrap recipes here generalize beyond LFQA.",
            ),
            Paper(
                title="Bootstrap Methods: Another Look at the Jackknife",
                authors="Bradley Efron",
                year="1979",
                url="https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full",
                summary="The original bootstrap paper — the technique behind every benchmark CI you should be reporting.",
                venue="Annals of Statistics",
            ),
            Paper(
                title="Open LLM Leaderboard v2",
                authors="Fourrier et al.",
                year="2024",
                url="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard",
                summary="Pins lm-eval-harness commits, prompt formats, and engine settings so numbers stay comparable across submissions; documents its decoding contract publicly.",
                venue="HuggingFace",
            ),
        ],
        extras=[
            Extra(label="Bootstrapping (Wikipedia)", url="https://en.wikipedia.org/wiki/Bootstrapping_(statistics)"),
            Extra(label="HF blog: What's going on with the Open LLM Leaderboard?", url="https://huggingface.co/blog/open-llm-leaderboard-mmlu"),
            Extra(label="vLLM determinism notes", url="https://docs.vllm.ai/en/latest/serving/faq.html"),
        ],
    ),

    Chapter(
        id=19,
        slug="leaderboards-and-arena",
        part="V. Methodology: Running Evals in Practice",
        title="Leaderboards: Open LLM, BigCode, SWE-bench, Arena",
        summary_html="""<p>Leaderboards do two jobs at once: they aggregate evals into a single
ranking, and they constrain methodology so the ranking is meaningful. The
ranking is the part most people look at; the constrained methodology is the
part that actually matters.</p>

<h4>Hugging Face Open LLM Leaderboard v2</h4>
<p>The default for general open-weight LLM evaluation. v2 (2024) replaced
the saturated v1 mix with six harder benchmarks: <b>IFEval</b>,
<b>BBH</b>, <b>MATH</b> (level-5 subset), <b>GPQA</b>, <b>MUSR</b>,
<b>MMLU-Pro</b>. All run via lm-eval-harness at pinned commits.</p>

<h4>BigCode Models Leaderboard</h4>
<p>The coding-specific counterpart. Tracks HumanEval, MBPP, MultiPL-E across
~18 languages, plus throughput metrics. Useful for choosing a base coding
model before going to SWE-style benches.</p>

<h4>SWE-bench Leaderboard</h4>
<p>The flagship for coding agents — resolved-rate on SWE-bench
Verified/Lite/Live, broken down by harness (SWE-agent, Agentless, OpenHands,
proprietary). Look at the trajectory logs published alongside each
submission; opaque submissions are worth less.</p>

<h4>Chatbot Arena (lmarena.ai)</h4>
<p>Pairwise human preferences turned into Elo ratings via Bradley-Terry. It
captures something none of the static benches do — overall <i>chat
helpfulness</i> as judged by real users — but it is sensitive to style
(verbose, friendly answers do well) and is hard to use for narrow
capabilities.</p>

<h4>Aider LLM Leaderboard</h4>
<p>A small but well-loved practical bench: 133 Python edit tasks where the
model has to apply diffs to existing files. Tracks 'percent of edits that
work' separately from 'percent of test cases that pass'. Closer to real IDE
usage than HumanEval.</p>

<p><b>Reading rule:</b> a model that wins one leaderboard and loses another
is not a contradiction — it is a signal that the leaderboards measure
different things. Triangulate.</p>""",
        papers=[
            Paper(
                title="Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference",
                authors="Chiang et al.",
                year="2024",
                url="https://arxiv.org/abs/2403.04132",
                summary="Describes the LMSys / lmarena.ai pairwise-vote pipeline and the Bradley-Terry Elo math behind the ranking. Required reading before quoting Arena scores.",
            ),
            Paper(
                title="Open LLM Leaderboard v2 (HuggingFace blog)",
                authors="Fourrier et al.",
                year="2024",
                url="https://huggingface.co/blog/open-llm-leaderboard-rlhf",
                summary="Why v1 was retired (saturation, contamination), what v2 measures, and how prompts/decoders are pinned. The blog is the authoritative description.",
                venue="HuggingFace",
            ),
            Paper(
                title="Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena",
                authors="Zheng et al.",
                year="2023",
                url="https://arxiv.org/abs/2306.05685",
                summary="Establishes that GPT-4 judging correlates ~0.8 with human prefs on chat tasks but has known biases (verbosity, position). Background for any leaderboard that uses LM-as-judge.",
            ),
            Paper(
                title="SWE-bench Verified",
                authors="OpenAI Preparedness team",
                year="2024",
                url="https://web.archive.org/web/2026/https://openai.com/index/introducing-swe-bench-verified/",
                summary="The 500-task human-validated subset of SWE-bench. The official leaderboard at swebench.com tracks resolved-rate on this set as the headline number for coding agents.",
                venue="OpenAI",
            ),
            Paper(
                title="Aider's LLM Leaderboards",
                authors="Paul Gauthier",
                year="2024",
                url="https://aider.chat/docs/leaderboards/",
                summary="Practitioner-oriented coding leaderboard built around real diff-application tasks. Documents prompt, harness, and methodology in full.",
                venue="aider.chat",
            ),
        ],
        extras=[
            Extra(label="Open LLM Leaderboard v2", url="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"),
            Extra(label="BigCode Models Leaderboard", url="https://huggingface.co/spaces/bigcode/bigcode-models-leaderboard"),
            Extra(label="SWE-bench leaderboard", url="https://www.swebench.com/"),
            Extra(label="LMArena", url="https://lmarena.ai/"),
        ],
    ),

    Chapter(
        id=20,
        slug="picking-and-running-an-eval-suite",
        part="V. Methodology: Running Evals in Practice",
        title="Picking and Running an Eval Suite: A Practical Checklist",
        summary_html="""<p>The hardest part of evaluation is not running the harness; it is
picking the right benchmarks for the question you actually have. Most
mistakes here are scope errors — using a chat leaderboard to predict
production retrieval quality, or using HumanEval to predict whether a model
can handle your repo.</p>

<h4>Step 1 — define the question</h4>
<ul>
  <li><b>Capability</b> ("can this model do X at all?") — pick narrow,
  high-headroom benches: GPQA, MATH-level-5, SWE-bench Verified.</li>
  <li><b>Deployment fitness</b> ("is this model good enough for my product?")
  — build a private bench from your own traffic; public benches are a
  triangulation, not the answer.</li>
  <li><b>Alignment / safety</b> — IFEval, refusal-rate suites, red-team sets.</li>
</ul>

<h4>Step 2 — pick 3-5 benches that triangulate</h4>
<p>One general-knowledge (MMLU-Pro), one reasoning (GPQA or BBH), one math
(MATH or GSM8K), one coding (HumanEval or BigCodeBench). For coding agents
add SWE-bench Verified. A single number lies; three numbers that all move
together is a signal.</p>

<h4>Step 3 — defend against contamination</h4>
<p>Prefer benches with a Verified / Live / hidden split (LiveCodeBench
post-cutoff slice; SWE-bench Verified). For older benches, run an n-gram
overlap check between your model's training data (where known) and the
test set, or at minimum cite the model's training-data cutoff vs the
benchmark release date.</p>

<h4>Step 4 — pin everything and run</h4>
<pre>
# Minimal lm-eval-harness invocation
lm_eval \\
  --model vllm \\
  --model_args pretrained=Qwen/Qwen2.5-7B-Instruct,dtype=bfloat16 \\
  --tasks mmlu_pro,gpqa_diamond,bbh,ifeval,gsm8k \\
  --num_fewshot 0 \\
  --batch_size auto \\
  --log_samples \\
  --output_path runs/qwen25-7b-instruct.json
</pre>

<h4>Step 5 — compare and publish</h4>
<p>Always run ≥2 baselines on the same setup (a known-strong open model and
a known-weak one). Publish prompts, harness commit, model commit, sampling
parameters, and bootstrap CIs. If you cannot publish all of these, you have
a sales pitch, not an evaluation.</p>""",
        papers=[
            Paper(
                title="Holistic Evaluation of Language Models (HELM)",
                authors="Liang et al.",
                year="2022",
                url="https://arxiv.org/abs/2211.09110",
                summary="The original HELM paper — the multi-axis eval philosophy that motivates a 3-5 benchmark portfolio rather than one number.",
                venue="Stanford CRFM",
            ),
            Paper(
                title="Are Emergent Abilities of Large Language Models a Mirage?",
                authors="Schaeffer et al.",
                year="2023",
                url="https://arxiv.org/abs/2304.15004",
                summary="Argues that benchmark choice (especially the metric — accuracy vs token-level log-prob) can manufacture or hide phase transitions. A reminder to triangulate.",
                venue="NeurIPS",
            ),
            Paper(
                title="Investigating Data Contamination in Modern Benchmarks for Large Language Models",
                authors="Sainz et al.",
                year="2023",
                url="https://arxiv.org/abs/2310.18018",
                summary="Catalogues contamination across MMLU, GSM8K, HumanEval and others; provides the n-gram overlap recipe for defending your own runs.",
            ),
            Paper(
                title="lm-evaluation-harness",
                authors="Gao et al.",
                year="2023",
                url="https://github.com/EleutherAI/lm-evaluation-harness",
                summary="The runner referenced by the example invocation above. Supports vLLM, HuggingFace, and OpenAI-compatible endpoints behind a single CLI.",
                venue="EleutherAI",
            ),
            Paper(
                title="The Open LLM Leaderboard v2 paper",
                authors="Fourrier et al.",
                year="2024",
                url="https://huggingface.co/blog/open-llm-leaderboard-rlhf",
                summary="Documents the exact six-bench portfolio HF landed on after a year of v1 saturation. A defensible default if you do not have a strong opinion.",
                venue="HuggingFace",
            ),
        ],
        extras=[
            Extra(label="lm-evaluation-harness", url="https://github.com/EleutherAI/lm-evaluation-harness"),
            Extra(label="HELM lite leaderboard", url="https://crfm.stanford.edu/helm/lite/latest/"),
            Extra(label="vLLM (recommended inference engine)", url="https://github.com/vllm-project/vllm"),
        ],
    ),
]
