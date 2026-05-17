"""Section II — The Open Model Landscape.

Four chapters that orient a postgrad reader to the open model ecosystem they
will actually download, evaluate, and fine-tune.  We cover the openness
spectrum, the general-purpose families, the small-model families, and the
coding-specific families.  Citations are open-access only: arXiv, Hugging
Face model cards and blogs, and lab repositories.

Voice mirrors `chapters/17-the-transformer/README.md`: plain-language,
intuition-first, technically precise.  HTML uses <p>, <h4>, <ul>, with at
most one <pre> block per chapter where a small table genuinely helps.
"""

from _chapter_types import Chapter, Paper, Extra


MODELS_CHAPTERS: list[Chapter] = [
    # ------------------------------------------------------------------ #
    # 4. Open-Source vs. Open-Weight Models
    # ------------------------------------------------------------------ #
    Chapter(
        id=4,
        slug="open-source-vs-open-weight",
        part="II. The Open Model Landscape",
        title="Open-Source vs. Open-Weight Models",
        summary_html="""\
<p>"Open" is doing a lot of work in "open model."  Before you pick a model to
benchmark, it helps to know what you actually get when you download it — and
what you're allowed to do with it afterwards.  The ecosystem sits on a
spectrum, not a binary.</p>

<h4>Fully open: data + weights + training code</h4>
<p>A small but important group of models ships everything: the training data,
the data-mixing recipe, the training code, intermediate checkpoints, and the
final weights.  <a href="https://arxiv.org/abs/2402.00838" target="_blank" rel="noopener">OLMo</a>
from AI2 and the older Pythia suite from EleutherAI are the canonical
examples.  These are the only models you can truly <i>reproduce</i>, and
they're the right choice for research on training dynamics, data
attribution, or scaling behavior.</p>

<h4>Open-weight: weights yes, recipe no</h4>
<p>The bulk of what people call "open models" lives here.  You get the
weights and a model card; you don't get the training data or the full
training code.  Llama 3, Qwen 2.5, DeepSeek-V3, Mistral / Mixtral, Gemma 2,
and Phi all fit this category.  Open-weight is more than enough for most
real work: you can run inference, fine-tune, quantize, distill, and deploy.
You just can't re-train from scratch.</p>

<h4>Hosted closed: API only</h4>
<p>GPT-4-class models from OpenAI, Claude from Anthropic, and Gemini from
Google are accessed only through APIs.  No weights, no fine-tuning of the
base model, and your benchmark results are tied to whatever version the
provider is serving today.  That last point matters: closed models can and
do change underneath you between eval runs.</p>

<h4>Licenses actually matter</h4>
<p>Read the license before you commit a model to a benchmark suite, never
mind a product:</p>
<pre>
license type            examples                  commercial use?
----------------------  ------------------------  ----------------
Apache 2.0 / MIT        OLMo, Qwen, Mistral 7B    yes, broadly
Llama community         Llama 3 family            yes, with limits
Gemma terms             Gemma 2                   yes, with terms
research-only           some early releases       no
</pre>
<p>The Llama Community License, for example, has a 700M-MAU clause that
restricts very large deployments; Gemma has its own usage terms.  Apache
2.0 (Qwen, Mistral 7B, OLMo) is the friendliest.</p>

<h4>Why this matters for benchmarks</h4>
<p>Reproducibility lives or dies on openness.  An open-weight model gives
you a fixed artifact you can hash, version, and re-run a year later.  A
hosted closed model gives you a moving target.  When you publish numbers,
note the exact model checkpoint and license — and consider whether the
result is one a peer can reproduce.  The
<a href="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard" target="_blank" rel="noopener">Hugging Face Open LLM Leaderboard</a>
is the de-facto registry for open-weight models and a good place to start
when you're choosing what to evaluate.</p>
""",
        papers=[
            Paper(
                title="OLMo: Accelerating the Science of Language Models",
                authors="Groeneveld et al. (AI2)",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2402.00838",
                summary="The reference fully-open release: data, training code, intermediate checkpoints, and weights. Read this if you care about reproducibility.",
            ),
            Paper(
                title="The Llama 3 Herd of Models",
                authors="Llama Team, Meta",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.21783",
                summary="The flagship open-weight family. The report doubles as a candid description of what 'open-weight' currently includes — and what it doesn't.",
            ),
            Paper(
                title="Qwen2.5 Technical Report",
                authors="Qwen Team, Alibaba",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2412.15115",
                summary="Apache-2.0 open-weight family across many sizes. A clean example of broadly-permissive licensing applied to a strong modern model.",
            ),
            Paper(
                title="Mistral 7B",
                authors="Jiang et al.",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2310.06825",
                summary="Apache-2.0, 7B parameters, the model that mainstreamed truly-permissive open-weight releases at competitive quality.",
            ),
            Paper(
                title="Gemma 2: Improving Open Language Models at a Practical Size",
                authors="Gemma Team, Google",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2408.00118",
                summary="Open-weight under the Gemma terms. Useful counter-example to Apache-2.0: similar artifacts, materially different license obligations.",
            ),
        ],
        extras=[
            Extra(
                label="Hugging Face Open LLM Leaderboard",
                url="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard",
            ),
            Extra(
                label="OLMo collection on Hugging Face",
                url="https://huggingface.co/allenai",
            ),
            Extra(
                label="Llama 3.1 8B Instruct model card",
                url="https://huggingface.co/meta-llama/Meta-Llama-3.1-8B-Instruct",
            ),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 5. General-Purpose Open Models
    # ------------------------------------------------------------------ #
    Chapter(
        id=5,
        slug="general-purpose-llm-families",
        part="II. The Open Model Landscape",
        title="General-Purpose Open Models: Llama, Qwen, DeepSeek, Mistral, Gemma",
        summary_html="""\
<p>If you're picking one general-purpose open model to benchmark, you'll be
choosing among five families.  This is the short tour: who makes them, what
sizes ship, what they're known for, and where to download them.  All five
are open-weight; license details vary and are worth reading once.</p>

<h4>Llama 3 / 3.1 (Meta)</h4>
<p><a href="https://arxiv.org/abs/2407.21783" target="_blank" rel="noopener">Llama 3.1</a>
ships in 8B, 70B, and 405B parameter sizes.  The 8B is the default open SLM
baseline almost everyone reports against; the 70B is the workhorse for
serious self-hosted deployments; the 405B is a frontier-quality dense model.
The training report is one of the most detailed in the open literature.
License: Llama Community License (commercial-friendly with a large-MAU
clause).  Download from the
<a href="https://huggingface.co/meta-llama" target="_blank" rel="noopener">meta-llama org on Hugging Face</a>.</p>

<h4>Qwen 2.5 (Alibaba)</h4>
<p><a href="https://arxiv.org/abs/2412.15115" target="_blank" rel="noopener">Qwen 2.5</a>
covers 0.5B, 1.5B, 3B, 7B, 14B, 32B, and 72B — the widest size ladder in
open-weight land.  Particularly strong on reasoning, math, and code, and
multilingual to a degree most western models aren't.  Most variants are
Apache 2.0.  Pulls from
<a href="https://huggingface.co/Qwen" target="_blank" rel="noopener">huggingface.co/Qwen</a>.</p>

<h4>DeepSeek-V3</h4>
<p><a href="https://arxiv.org/abs/2412.19437" target="_blank" rel="noopener">DeepSeek-V3</a>
is a 671B-parameter Mixture-of-Experts (MoE) model that activates only ~37B
parameters per token.  That ratio is the headline: frontier-class quality at
inference cost closer to a 37B dense model.  The trade is memory — you still
need to hold all 671B parameters in GPU RAM.  Open-weight under the DeepSeek
license, with strong math and code numbers.</p>

<h4>Mistral 7B and Mixtral 8×7B</h4>
<p><a href="https://arxiv.org/abs/2310.06825" target="_blank" rel="noopener">Mistral 7B</a>
remains one of the cleanest 7B baselines on the leaderboard.
<a href="https://arxiv.org/abs/2401.04088" target="_blank" rel="noopener">Mixtral 8×7B</a>
is its MoE sibling: 8 experts of 7B each, 2 active per token, ~13B
effective compute, ~47B parameters total.  Both are Apache 2.0 — the most
permissive license in this list.</p>

<h4>Gemma 2 (Google)</h4>
<p><a href="https://arxiv.org/abs/2408.00118" target="_blank" rel="noopener">Gemma 2</a>
ships at 2B, 9B, and 27B.  The 9B is widely considered the best
single-GPU-friendly all-rounder; the 27B is competitive with much larger
models thanks to careful distillation from a teacher.  License: Gemma terms
(commercial use, with Google's responsible-use restrictions).</p>

<pre>
family       sizes (B)              license             notable for
-----------  ---------------------  ------------------  -----------------------
Llama 3.1    8 / 70 / 405           Llama Community     reference baseline
Qwen 2.5     0.5/1.5/3/7/14/32/72   Apache 2.0          breadth + reasoning/code
DeepSeek-V3  671 (37 active, MoE)   DeepSeek License    frontier MoE quality
Mistral      7 dense; 8x7 MoE       Apache 2.0          permissive + strong 7B
Gemma 2      2 / 9 / 27             Gemma terms         distillation-tuned
</pre>
<p>For a first benchmark suite, Llama-3.1-8B + Qwen2.5-7B + Gemma-2-9B +
Mistral-7B is a defensible four-way comparison: similar compute class, four
different research lineages, four different licenses.</p>
""",
        papers=[
            Paper(
                title="The Llama 3 Herd of Models",
                authors="Llama Team, Meta",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2407.21783",
                summary="Detailed training-recipe document for the 8B/70B/405B family. The most-cited open-weight LLM report of 2024.",
            ),
            Paper(
                title="Qwen2.5 Technical Report",
                authors="Qwen Team, Alibaba",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2412.15115",
                summary="Covers seven sizes from 0.5B to 72B with shared tokenizer and recipe. Useful for studying scale within a single model family.",
            ),
            Paper(
                title="DeepSeek-V3 Technical Report",
                authors="DeepSeek-AI",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2412.19437",
                summary="671B-parameter MoE with 37B active per token. Frontier-class quality with much cheaper inference than a comparable dense model.",
            ),
            Paper(
                title="Mistral 7B",
                authors="Jiang et al.",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2310.06825",
                summary="The 7B Apache-2.0 model that set the bar for open-weight SLMs. Sliding-window attention and grouped-query attention are introduced cleanly.",
            ),
            Paper(
                title="Mixtral of Experts",
                authors="Jiang et al.",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2401.04088",
                summary="8x7B sparse MoE; 2 of 8 experts active per token. The reference for understanding sparse MoE in an open-weight model.",
            ),
            Paper(
                title="Gemma 2: Improving Open Language Models at a Practical Size",
                authors="Gemma Team, Google",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2408.00118",
                summary="2B/9B/27B with knowledge distillation from a larger teacher. The 9B is the standout single-GPU model in this family.",
            ),
        ],
        extras=[
            Extra(
                label="meta-llama org on Hugging Face",
                url="https://huggingface.co/meta-llama",
            ),
            Extra(
                label="Qwen org on Hugging Face",
                url="https://huggingface.co/Qwen",
            ),
            Extra(
                label="Mistral AI org on Hugging Face",
                url="https://huggingface.co/mistralai",
            ),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 6. Small Language Models
    # ------------------------------------------------------------------ #
    Chapter(
        id=6,
        slug="small-language-models",
        part="II. The Open Model Landscape",
        title="Small Language Models: Phi, SmolLM, TinyLlama",
        summary_html="""\
<p>If you're benchmarking, you should care about small models out of pure
self-interest.  A 1.7B model evaluates in a fraction of the time of a 70B
one, runs on a single consumer GPU, and lets you do ten ablations in the
time one frontier eval finishes.  The 2024–2025 wave of SLMs proved
something stronger than that: with curated data, small can be genuinely
useful, not just educational.</p>

<h4>Phi (Microsoft)</h4>
<p>The <a href="https://arxiv.org/abs/2404.14219" target="_blank" rel="noopener">Phi-3</a>
series — Phi-3-mini (3.8B), Phi-3-small (7B), Phi-3-medium (14B) — built on
the slogan "textbooks are all you need."  The thesis: train on tightly
curated, instruction-rich, "textbook-quality" synthetic and filtered data,
and a small model can match much larger ones on reasoning and code.  Phi-3.5
extended this with a small MoE variant, and
<a href="https://arxiv.org/abs/2412.08905" target="_blank" rel="noopener">Phi-4</a>
(14B) doubled down on synthetic-data curation and reasoning-focused
post-training.  All available on the
<a href="https://huggingface.co/microsoft" target="_blank" rel="noopener">microsoft</a>
HF org.</p>

<h4>SmolLM and SmolLM2 (Hugging Face)</h4>
<p><a href="https://huggingface.co/blog/smollm" target="_blank" rel="noopener">SmolLM</a>
ships at 135M, 360M, and 1.7B; the
<a href="https://huggingface.co/blog/smollm2" target="_blank" rel="noopener">SmolLM2</a>
follow-up improves all three on the same size ladder.  These are trained on
fully open data (Cosmopedia, FineWeb-Edu) and are a clean choice if you want
to evaluate or fine-tune at the very small end without license friction.
The 1.7B in particular is a useful "is this even a hard task?" probe — if it
can do your task, you don't need a bigger model.</p>

<h4>TinyLlama and Gemma 2B</h4>
<p>TinyLlama is a 1.1B model trained on 3T tokens — a community
demonstration that Chinchilla-optimal smallness pushed even further on
extra data still pays off.  Gemma 2B (covered in the previous chapter) is
distilled from a much larger teacher and remains one of the strongest 2B
models for general use.</p>

<h4>Why SLMs matter for evaluation</h4>
<ul>
  <li><b>Speed.</b>  Faster inference means more eval runs per day,
      which means better statistics — fewer single-seed claims, more
      confidence intervals.</li>
  <li><b>Cost.</b>  You can run a full benchmark suite against five SLMs
      for the cost of one pass against a 70B model.</li>
  <li><b>Reproducibility.</b>  Smaller models are easier to host, easier
      to quantize, and easier to ship as a fixed artifact in a paper or a
      reproducible experiment.</li>
  <li><b>Headroom intuition.</b>  Knowing where the SLM ceiling is for a
      task tells you whether the larger model's win is "broad capability"
      or just "more memorized facts."</li>
</ul>

<pre>
model         params    notes
------------  --------  ---------------------------------------------
SmolLM2-135M  135M      smallest end of the ladder; great for ablations
SmolLM2-1.7B  1.7B      open data, reasonable instruction following
TinyLlama     1.1B      community SLM; 3T training tokens
Gemma 2 2B    2B        distilled from a larger teacher
Phi-3-mini    3.8B      curated-data SLM, strong on reasoning
Phi-4         14B       reasoning-focused post-training, top of the SLM range
</pre>
<p>Build the habit: every time you reach for a 70B model, ask whether a
1.7B SmolLM2 or a 3.8B Phi-3-mini already nails the task.  Often it does.</p>
""",
        papers=[
            Paper(
                title="Phi-3 Technical Report",
                authors="Abdin et al. (Microsoft)",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2404.14219",
                summary="The 'curated data, modest size' thesis applied at 3.8B/7B/14B. The clearest single document on why SLMs got so good so fast.",
            ),
            Paper(
                title="Phi-4 Technical Report",
                authors="Microsoft Research",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2412.08905",
                summary="14B model with heavy synthetic-data and reasoning-focused post-training. A useful study in pushing SLM quality without growing parameters.",
            ),
            Paper(
                title="SmolLM: blazingly fast and remarkably powerful",
                authors="Hugging Face",
                year="2024",
                venue="HF blog",
                url="https://huggingface.co/blog/smollm",
                summary="Introduces the SmolLM family on fully open data. Read alongside the SmolLM2 follow-up for the recipe evolution.",
            ),
            Paper(
                title="SmolLM2: when smol goes big",
                authors="Hugging Face",
                year="2024",
                venue="HF blog",
                url="https://huggingface.co/blog/smollm2",
                summary="The successor: same sizes, better data, better numbers. The most up-to-date open-data SLM family in this size class.",
            ),
            Paper(
                title="Gemma 2: Improving Open Language Models at a Practical Size",
                authors="Gemma Team, Google",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2408.00118",
                summary="2B variant is the distillation case study: a small student trained from a much larger teacher's logits, not just from raw text.",
            ),
        ],
        extras=[
            Extra(
                label="Microsoft org on Hugging Face",
                url="https://huggingface.co/microsoft",
            ),
            Extra(
                label="HuggingFaceTB SmolLM2 collection",
                url="https://huggingface.co/HuggingFaceTB",
            ),
            Extra(
                label="TinyLlama project on Hugging Face",
                url="https://huggingface.co/TinyLlama",
            ),
        ],
    ),

    # ------------------------------------------------------------------ #
    # 7. Coding-Specific Open Models
    # ------------------------------------------------------------------ #
    Chapter(
        id=7,
        slug="coding-specific-models",
        part="II. The Open Model Landscape",
        title="Coding-Specific Open Models: Code Llama, StarCoder, DeepSeek-Coder, Qwen-Coder",
        summary_html="""\
<p>General-purpose models can write code, but coding-specific families
consistently beat their general siblings on programming benchmarks at the
same parameter count — because they're trained on much more code, with
training objectives that match how code is actually edited.  If your
benchmark target is code, start here.</p>

<h4>Code Llama (Meta)</h4>
<p><a href="https://arxiv.org/abs/2308.12950" target="_blank" rel="noopener">Code Llama</a>
extends Llama 2 with extra training on a code-heavy mix.  Sizes: 7B, 13B,
34B, and 70B.  Variants exist for instruction following and Python
specifically.  The paper introduces fill-in-the-middle (FIM) and long-context
training (up to 100k tokens) at scale — both directly relevant for IDE-style
completion benchmarks.  License: Llama Community.</p>

<h4>StarCoder 2 (BigCode)</h4>
<p><a href="https://arxiv.org/abs/2402.19173" target="_blank" rel="noopener">StarCoder 2</a>
is the fully-open coding model: weights, training data (The Stack v2), and
training code are all released.  Sizes: 3B, 7B, 15B.  Trained on ~600
programming languages with FIM and repository-level context.  This is the
right choice when you want a coding model for research where reproducibility
matters; the
<a href="https://huggingface.co/bigcode/starcoder2-15b" target="_blank" rel="noopener">15B model card</a>
links the data and training pipeline.</p>

<h4>DeepSeek-Coder and DeepSeek-Coder-V2</h4>
<p><a href="https://arxiv.org/abs/2401.14196" target="_blank" rel="noopener">DeepSeek-Coder</a>
(1.3B / 6.7B / 33B) was the first family to seriously challenge Code Llama
on open benchmarks; the recipe leaned on repository-level training and FIM.
<a href="https://arxiv.org/abs/2406.11931" target="_blank" rel="noopener">DeepSeek-Coder-V2</a>
goes MoE: 236B parameters total with 21B active per token, plus a smaller
16B / 2.4B-active "lite" variant.  V2 is competitive with much larger
closed models on code benchmarks while staying open-weight.</p>

<h4>Qwen2.5-Coder</h4>
<p><a href="https://arxiv.org/abs/2409.12186" target="_blank" rel="noopener">Qwen2.5-Coder</a>
ships at 0.5B, 1.5B, 3B, 7B, 14B, and 32B — the same generous size ladder
as the base Qwen family but specialized on code.  The 32B variant is, as of
late 2024, the strongest open-weight code model on most public benchmarks.
Apache 2.0 for most sizes.</p>

<h4>What makes a "code model" different</h4>
<ul>
  <li><b>Fill-in-the-middle (FIM).</b>  Code isn't written start-to-end —
      you edit a function in the middle of a file.  FIM training reorders
      sequences so the model learns to predict a span given both prefix
      and suffix context.  This is what powers good IDE autocomplete.</li>
  <li><b>Repository-level training.</b>  Instead of treating each file
      independently, training packs related files from the same repo
      together, so the model sees the kind of cross-file context a real
      project has.</li>
  <li><b>Long-context training.</b>  100k+ token windows let the model
      reason about whole files or small repos at once.</li>
  <li><b>Multi-language coverage.</b>  StarCoder 2 hits ~600 languages;
      Code Llama and DeepSeek-Coder cover the main 80–100 carefully.</li>
</ul>

<p>You'll see HumanEval and MBPP cited everywhere as the public-benchmark
shorthand for "this model can code."  We'll dig into what those benchmarks
actually measure (and how they fail) in Section IV — for now, just know
that all four families above are at or near the top of the open-weight
leaderboards.</p>
""",
        papers=[
            Paper(
                title="Code Llama: Open Foundation Models for Code",
                authors="Rozière et al. (Meta)",
                year="2023",
                venue="arXiv",
                url="https://arxiv.org/abs/2308.12950",
                summary="The reference open-weight code-model report. Fill-in-the-middle, long-context training, and Python-specialist variants are all introduced cleanly.",
            ),
            Paper(
                title="StarCoder 2 and The Stack v2",
                authors="Lozhkov et al. (BigCode)",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2402.19173",
                summary="Fully-open code model: weights, training data, and training code are all released. The right baseline when reproducibility matters.",
            ),
            Paper(
                title="DeepSeek-Coder: When the Large Language Model Meets Programming",
                authors="Guo et al. (DeepSeek-AI)",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2401.14196",
                summary="The original DeepSeek-Coder family. Notable for repository-level training and very strong HumanEval / MBPP numbers at 6.7B and 33B.",
            ),
            Paper(
                title="DeepSeek-Coder-V2: Breaking the Barrier of Closed-Source Models in Code Intelligence",
                authors="DeepSeek-AI",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2406.11931",
                summary="236B-parameter MoE (21B active) plus a 16B-lite variant. The first open-weight family to credibly close the gap to closed code models.",
            ),
            Paper(
                title="Qwen2.5-Coder Technical Report",
                authors="Qwen Team, Alibaba",
                year="2024",
                venue="arXiv",
                url="https://arxiv.org/abs/2409.12186",
                summary="Code-specialized Qwen2.5 across 0.5B–32B. The 32B is the standout open-weight code model at the time of writing.",
            ),
        ],
        extras=[
            Extra(
                label="bigcode/starcoder2-15b model card",
                url="https://huggingface.co/bigcode/starcoder2-15b",
            ),
            Extra(
                label="DeepSeek-Coder org on Hugging Face",
                url="https://huggingface.co/deepseek-ai",
            ),
            Extra(
                label="Qwen2.5-Coder collection on Hugging Face",
                url="https://huggingface.co/Qwen",
            ),
        ],
    ),
]
