"""Section III — General-Purpose Benchmarks (chapters 8-11).

Knowledge & reasoning, multi-step reasoning, math, and instruction-following /
chat. These are the benchmarks you will see quoted in almost every model card,
so the goal is to give the reader a working intuition for what each one
actually measures and how to read the numbers.
"""

from __future__ import annotations

from _chapter_types import Chapter, Paper, Extra


GENERAL_BENCH_CHAPTERS: list[Chapter] = [
    Chapter(
        id=8,
        slug="knowledge-and-reasoning-mmlu-mmlu-pro-gpqa",
        part="III. General-Purpose Benchmarks",
        title="Knowledge and Reasoning: MMLU, MMLU-Pro, GPQA",
        summary_html="""
<p>If you have ever skimmed a model card and seen a single number labelled
"MMLU: 86.4", this chapter is about what that number is actually measuring,
and why people increasingly report MMLU-Pro and GPQA alongside it.</p>

<h4>MMLU — the breadth test</h4>
<p><a href="https://arxiv.org/abs/2009.03300" target="_blank" rel="noopener">MMLU</a>
(Massive Multitask Language Understanding) is a 4-choice multiple-choice
exam covering 57 subjects — high-school math, US history, professional
medicine, machine learning, moral disputes, and so on. The score is plain
accuracy: did the model pick the right letter?</p>
<ul>
  <li><b>Format.</b> Usually reported as <i>5-shot</i> (five worked examples
  in the prompt) for base models and <i>0-shot CoT</i> for chat models.</li>
  <li><b>Random baseline.</b> 25%. Frontier models now score 87-90%, which
  means the headroom is mostly in the trickiest professional sub-tasks.</li>
  <li><b>Saturation.</b> By 2024 the top of the leaderboard was bunched
  inside a couple of points, and several errors in the gold labels had been
  catalogued — a sign the benchmark was running out of signal.</li>
</ul>

<pre>
Q: One of the reasons that the government discourages and regulates monopolies is that
   (A) producer surplus is lost and consumer surplus is gained.
   (B) monopoly prices ensure productive efficiency but cost society allocative efficiency.
   (C) monopoly firms do not engage in significant research and development.
   (D) consumer surplus is lost with higher prices and lower levels of output.
Answer: D
</pre>

<h4>MMLU-Pro — harder and less contaminated</h4>
<p><a href="https://arxiv.org/abs/2406.01574" target="_blank" rel="noopener">MMLU-Pro</a>
keeps the same idea but bumps the choice set from 4 to 10, filters out
trivially answerable questions, and adds reasoning-heavy items pulled from
textbooks and STEM exams. The random baseline drops to 10%, and even
strong models lose 15-25 points relative to their MMLU score, which gives
the leaderboard room to breathe again.</p>

<h4>GPQA — Google-proof graduate science</h4>
<p><a href="https://arxiv.org/abs/2311.12022" target="_blank" rel="noopener">GPQA</a>
is a small (≈450 question) set of biology, physics, and chemistry questions
written by domain PhDs. It is "Google-proof" by construction: validators
with web access but outside the field still got most of them wrong. The
"Diamond" subset (~198 items) is the hardest tier and the one usually
quoted. Numbers in the 50-70% range here separate genuinely strong
reasoners from models that are merely well-read.</p>

<h4>How to read the numbers</h4>
<ul>
  <li>Always check whether a score is 0-shot, 5-shot, or CoT — they are not
  comparable.</li>
  <li>Suspect contamination when MMLU is unusually high relative to
  MMLU-Pro and GPQA on the same model.</li>
  <li>For SLMs, MMLU is still useful; for frontier LLMs, GPQA-Diamond and
  MMLU-Pro carry more information.</li>
</ul>
""",
        papers=[
            Paper(
                title="Measuring Massive Multitask Language Understanding (MMLU)",
                authors="Hendrycks, Burns, Basart, Zou, Mazeika, Song, Steinhardt",
                year="2020",
                url="https://arxiv.org/abs/2009.03300",
                summary="The original MMLU benchmark — 57 subjects, 4-choice MCQ, the de facto knowledge-and-reasoning test for LLMs.",
                venue="ICLR 2021",
            ),
            Paper(
                title="MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark",
                authors="Wang, Ma, Zhang, Ni, Chandra, Guo, Ren, Arulraj, He, Jiang, Li, Liu, Wang, Yang, Sun, Bhardwaj, Boukouvalas, Wang, Sun, Tan, Yue, Yu, Cheng, Chen",
                year="2024",
                url="https://arxiv.org/abs/2406.01574",
                summary="Ten-choice, contamination-filtered, reasoning-heavy successor to MMLU. Used to re-spread the leaderboard once MMLU saturated.",
                venue="NeurIPS 2024 D&B",
            ),
            Paper(
                title="GPQA: A Graduate-Level Google-Proof Q&A Benchmark",
                authors="Rein, Hou, Stickland, Petty, Pang, Dirani, Michael, Bowman",
                year="2023",
                url="https://arxiv.org/abs/2311.12022",
                summary="PhD-written biology, physics, and chemistry questions designed to resist web search. The Diamond subset is the standard reasoning-frontier eval.",
                venue="COLM 2024",
            ),
            Paper(
                title="Beyond the Imitation Game (BIG-Bench)",
                authors="Srivastava et al.",
                year="2022",
                url="https://arxiv.org/abs/2206.04615",
                summary="Companion benchmark to MMLU — 200+ tasks contributed by the community. Important context for why narrower harder suites like GPQA exist.",
                venue="TMLR",
            ),
        ],
        extras=[
            Extra(
                label="Open LLM Leaderboard (HuggingFace)",
                url="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard",
            ),
            Extra(
                label="MMLU on Wikipedia",
                url="https://en.wikipedia.org/wiki/Massive_Multitask_Language_Understanding",
            ),
            Extra(
                label="MMLU-Pro leaderboard (HuggingFace)",
                url="https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro",
            ),
        ],
    ),
    Chapter(
        id=9,
        slug="reasoning-and-multistep-bbh-arc-hellaswag",
        part="III. General-Purpose Benchmarks",
        title="Reasoning and Multi-Step: BBH, ARC, HellaSwag",
        summary_html="""
<p>MMLU-style tests reward recall plus a single step of inference. The
benchmarks in this chapter target the next thing up: multi-step reasoning
and commonsense inference. They are old enough that several of them are
near-saturated for frontier models — yet they remain genuinely useful for
comparing small language models, where headroom is still abundant.</p>

<h4>BBH — the hard tail of BIG-Bench</h4>
<p><a href="https://arxiv.org/abs/2210.09261" target="_blank" rel="noopener">BIG-Bench Hard</a>
is the 23-task subset of <a href="https://arxiv.org/abs/2206.04615" target="_blank" rel="noopener">BIG-Bench</a>
where, at the time of selection, the average human rater beat the best
model. Tasks include logical deduction, tracking shuffled objects, date
arithmetic, multi-step word problems, and Boolean expression evaluation.
Two things made BBH influential:</p>
<ul>
  <li>It is the benchmark where <b>chain-of-thought prompting</b> first
  showed dramatic, often double-digit improvements over direct answering.</li>
  <li>It is multi-format — some tasks are multiple-choice, some are
  free-form — which forces evaluation harnesses to handle both.</li>
</ul>

<h4>ARC — grade-school science, hard subset</h4>
<p>The <a href="https://arxiv.org/abs/1803.05457" target="_blank" rel="noopener">AI2 Reasoning Challenge</a>
splits standardised US grade-school science questions into <i>Easy</i> and
<i>Challenge</i> sets. The Challenge set was specifically the questions
where simple retrieval and word-matching baselines failed. ARC-Challenge
was a real test of reasoning in the GPT-2/GPT-3 era; today, leading
frontier LLMs score above 95% and it has effectively saturated. It still
discriminates well between sub-3B parameter SLMs.</p>

<h4>HellaSwag — adversarial sentence completion</h4>
<p><a href="https://arxiv.org/abs/1905.07830" target="_blank" rel="noopener">HellaSwag</a>
gives a short context (often a WikiHow or video caption) and four
candidate continuations, of which only one is plausible. The wrong
continuations were generated and adversarially filtered so that an earlier
generation of language models could not distinguish them from the right
answer — but humans easily can.</p>
<ul>
  <li><b>Random baseline:</b> 25%.</li>
  <li><b>Human:</b> ~95%.</li>
  <li><b>Frontier LLMs:</b> 95%+; the benchmark is essentially solved at
  the top end but is still informative for SLMs and base models.</li>
</ul>

<h4>How to use this trio today</h4>
<p>Treat ARC-Challenge and HellaSwag as <b>floor checks</b> — if a small
model is well below 80%, it is genuinely weak at basic commonsense and
science. Use BBH (especially with CoT) as the more discriminating signal
for reasoning, and pair it with GPQA or MATH when you care about the
upper end. None of these three should be a model's only reasoning eval
in 2026.</p>
""",
        papers=[
            Paper(
                title="Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them (BBH)",
                authors="Suzgun, Scales, Schärli, Gehrmann, Tay, Chung, Chowdhery, Le, Chi, Zhou, Wei",
                year="2022",
                url="https://arxiv.org/abs/2210.09261",
                summary="Defines BIG-Bench Hard and shows that chain-of-thought prompting closes much of the gap to human raters on these 23 tasks.",
                venue="ACL 2023 Findings",
            ),
            Paper(
                title="Beyond the Imitation Game: Quantifying and Extrapolating the Capabilities of Language Models (BIG-Bench)",
                authors="Srivastava et al.",
                year="2022",
                url="https://arxiv.org/abs/2206.04615",
                summary="The umbrella BIG-Bench paper — 200+ tasks contributed by 400+ authors. BBH is the hard subset distilled out of this.",
                venue="TMLR",
            ),
            Paper(
                title="Think You Have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge",
                authors="Clark, Cowhey, Etzioni, Khot, Sabharwal, Schoenick, Tafjord",
                year="2018",
                url="https://arxiv.org/abs/1803.05457",
                summary="Introduces the ARC Easy and Challenge sets of US grade-school science questions and a knowledge corpus to go with them.",
                venue="arXiv",
            ),
            Paper(
                title="HellaSwag: Can a Machine Really Finish Your Sentence?",
                authors="Zellers, Holtzman, Bisk, Farhadi, Choi",
                year="2019",
                url="https://arxiv.org/abs/1905.07830",
                summary="Adversarially filtered sentence-completion task built with Adversarial Filtering. Once near-impossible for LMs, now near-saturated.",
                venue="ACL 2019",
            ),
        ],
        extras=[
            Extra(
                label="BIG-Bench GitHub repository",
                url="https://github.com/google/BIG-bench",
            ),
            Extra(
                label="Open LLM Leaderboard (HuggingFace)",
                url="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard",
            ),
        ],
    ),
    Chapter(
        id=10,
        slug="math-gsm8k-math-aime",
        part="III. General-Purpose Benchmarks",
        title="Math: GSM8K, MATH, and AIME",
        summary_html="""
<p>Math benchmarks have outsized influence on how the field talks about
"reasoning". They are unambiguous (the answer is a number), they reward
multi-step thought, and they expose differences between models that
otherwise look similar on knowledge tests. This chapter walks through the
three math suites you will see in nearly every modern model card.</p>

<h4>GSM8K — grade-school word problems</h4>
<p><a href="https://arxiv.org/abs/2110.14168" target="_blank" rel="noopener">GSM8K</a>
is ~8,500 grade-school arithmetic word problems written by human
annotators, with full step-by-step solutions. Each problem takes 2-8
elementary operations. GSM8K is the canonical place to demonstrate that
<b>chain-of-thought prompting</b> works: directly asking for the answer
is far worse than asking the model to "think step by step" and then read
off the final number.</p>

<pre>
Q: Janet's ducks lay 16 eggs per day. She eats three for breakfast,
   bakes muffins with four, and sells the rest at the farmers' market
   for $2 per egg. How much does she make per day?

Reasoning: 16 - 3 - 4 = 9 eggs sold.  9 * 2 = 18.
Final answer: 18
</pre>

<h4>MATH — competition problems</h4>
<p>The <a href="https://arxiv.org/abs/2103.03874" target="_blank" rel="noopener">MATH dataset</a>
contains 12,500 problems from US high-school competitions (AMC, AIME,
USAMO and similar), labelled with difficulty 1-5 and split across algebra,
geometry, number theory, counting and probability, intermediate algebra,
prealgebra, and precalculus. Solutions require real techniques — telescoping
sums, modular arithmetic, generating functions — not just careful
arithmetic. As of 2025-2026 frontier reasoning models are above 90% on
MATH while strong SLMs are still in the 30-60% range, so it remains a
discriminating benchmark.</p>

<h4>AIME — the very hard tail</h4>
<p>AIME (American Invitational Mathematics Examination) is the qualifier
for the USA Math Olympiad. Each year produces only ~30 problems, all
integer-answered (000-999). It is small, but solving AIME problems
reliably requires substantial planning and case analysis, and it has
become the headline benchmark for "reasoning" models in the o1 / R1 /
Claude-thinking class. Numbers like "AIME 2024: 83%" are now common in
launch posts.</p>

<h4>How to evaluate math properly</h4>
<ul>
  <li><b>Use chain-of-thought.</b> Always. Direct-answer scores understate
  capability by 30-50 points on these benchmarks.</li>
  <li><b>Sampling matters.</b> Run with non-zero temperature and report
  <i>pass@1</i> averaged over k samples, or <i>maj@k</i> (self-consistency
  / majority voting) — a single greedy decode is high-variance.</li>
  <li><b>Tool use.</b> Many recent results allow Python execution.
  Always disclose: a 92% MATH score with a calculator is a different
  number than a 92% MATH score without one.</li>
  <li><b>Answer parsing.</b> A surprising amount of math-eval noise is
  the grader, not the model — boxed answers, fraction normalisation,
  units. Check the harness.</li>
</ul>
""",
        papers=[
            Paper(
                title="Training Verifiers to Solve Math Word Problems (GSM8K)",
                authors="Cobbe, Kosaraju, Bavarian, Chen, Jun, Kaiser, Plappert, Tworek, Hilton, Nakano, Hesse, Schulman",
                year="2021",
                url="https://arxiv.org/abs/2110.14168",
                summary="Introduces GSM8K and a verifier-based reranking method. The dataset became the standard sanity-check for chain-of-thought reasoning.",
                venue="arXiv",
            ),
            Paper(
                title="Measuring Mathematical Problem Solving With the MATH Dataset",
                authors="Hendrycks, Burns, Kadavath, Arora, Basart, Tang, Song, Steinhardt",
                year="2021",
                url="https://arxiv.org/abs/2103.03874",
                summary="12,500 competition problems with worked solutions and difficulty labels. Still the dominant general math benchmark.",
                venue="NeurIPS 2021 D&B",
            ),
            Paper(
                title="Self-Consistency Improves Chain of Thought Reasoning in Language Models",
                authors="Wang, Wei, Schuurmans, Le, Chi, Narang, Chowdhery, Zhou",
                year="2022",
                url="https://arxiv.org/abs/2203.11171",
                summary="Sample many CoT solutions, take the majority answer. The technique behind every maj@k math number you have seen.",
                venue="ICLR 2023",
            ),
            Paper(
                title="Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
                authors="Wei, Wang, Schuurmans, Bosma, Ichter, Xia, Chi, Le, Zhou",
                year="2022",
                url="https://arxiv.org/abs/2201.11903",
                summary="Establishes that prompting models to show their work dramatically improves multi-step arithmetic and word-problem accuracy.",
                venue="NeurIPS 2022",
            ),
        ],
        extras=[
            Extra(
                label="GSM8K dataset on HuggingFace",
                url="https://huggingface.co/datasets/openai/gsm8k",
            ),
            Extra(
                label="MATH dataset on HuggingFace",
                url="https://huggingface.co/datasets/hendrycks/competition_math",
            ),
            Extra(
                label="AIME problems archive (Art of Problem Solving)",
                url="https://artofproblemsolving.com/wiki/index.php/AIME_Problems_and_Solutions",
            ),
        ],
    ),
    Chapter(
        id=11,
        slug="instruction-following-and-chat-ifeval-mt-bench-arena",
        part="III. General-Purpose Benchmarks",
        title="Instruction-Following and Chat: IFEval, MT-Bench, Chatbot Arena",
        summary_html="""
<p>The benchmarks in earlier chapters mostly ask: <i>can the model get the
right answer?</i> Once a model is going to be deployed as a chat assistant,
the more important question becomes: <i>does it follow instructions, sound
helpful, and stay on task across a conversation?</i> That is a much harder
thing to score. The three benchmarks here represent the three main
strategies the field has settled on.</p>

<h4>IFEval — programmatic instruction-following</h4>
<p><a href="https://arxiv.org/abs/2311.07911" target="_blank" rel="noopener">IFEval</a>
sidesteps the subjectivity problem by using only <i>verifiable</i>
instructions: "respond in exactly three bullet points", "include the word
'algorithm' twice", "do not use the letter e", "answer in JSON with these
keys", "end your response with the word 'done'". A simple Python checker
decides pass or fail per instruction. Scores are reported as
<b>prompt-level</b> (all instructions in the prompt satisfied) and
<b>instruction-level</b> (per-clause). It is cheap, deterministic, and
correlates well with how usable a model is as an API.</p>

<h4>MT-Bench — LM-as-judge on multi-turn chats</h4>
<p><a href="https://arxiv.org/abs/2306.05685" target="_blank" rel="noopener">MT-Bench</a>
introduced the now-standard <b>LM-as-judge</b> evaluation. 80 hand-written
two-turn questions span writing, roleplay, reasoning, math, coding,
extraction, STEM, and humanities. Each model's response is scored on a
1-10 scale by a strong judge model (originally GPT-4). The same paper also
introduced pairwise judging for Chatbot Arena.</p>
<ul>
  <li><b>Strengths:</b> covers free-form quality dimensions a closed
  multiple-choice test cannot — tone, helpfulness, formatting, refusal
  calibration.</li>
  <li><b>Weaknesses:</b> <i>position bias</i> (judges prefer whichever
  answer comes first), <i>verbosity bias</i> (longer answers score
  higher), <i>self-preference</i> (a judge tends to favour answers that
  look like its own), and the obvious circularity of grading models with
  models. Mitigations include swapping order, using multiple judges, and
  reporting agreement with human raters.</li>
</ul>

<h4>Chatbot Arena — human pairwise Elo</h4>
<p><a href="https://arxiv.org/abs/2403.04132" target="_blank" rel="noopener">Chatbot Arena</a>
(LMSYS, now <a href="https://lmarena.ai/" target="_blank" rel="noopener">lmarena.ai</a>)
sidesteps automated judging entirely. Users type any prompt, see two
anonymised responses, and pick the better one. Votes are aggregated into
an Elo-style rating, and the leaderboard is updated continuously. It is
the closest thing the field has to a real-world preference signal — at
the cost of being slow, unreproducible, and biased toward whatever users
happen to ask about.</p>

<h4>Reading the three together</h4>
<ul>
  <li>If IFEval is high but Arena is mid, the model is technically
  compliant but unpleasant.</li>
  <li>If Arena is high but IFEval is low, the model is charismatic but
  ignores constraints — bad for agentic and structured-output use cases.</li>
  <li>MT-Bench has been largely supplanted by <a href="https://lmarena.ai/" target="_blank" rel="noopener">Arena</a>
  and harder LM-judged successors (Arena-Hard, MixEval), but it is still a
  useful cheap regression test.</li>
</ul>
""",
        papers=[
            Paper(
                title="Instruction-Following Evaluation for Large Language Models (IFEval)",
                authors="Zhou, Lu, Misra, Brahma, Basu, Luan, Zhou, Hou",
                year="2023",
                url="https://arxiv.org/abs/2311.07911",
                summary="Defines a set of verifiable instructions checkable by Python, and reports prompt-level and instruction-level accuracy. The standard objective instruction-following eval.",
                venue="arXiv",
            ),
            Paper(
                title="Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena",
                authors="Zheng, Chiang, Sheng, Zhuang, Wu, Zhuang, Lin, Li, Li, Xing, Zhang, Gonzalez, Stoica",
                year="2023",
                url="https://arxiv.org/abs/2306.05685",
                summary="Introduces MT-Bench (LM-as-judge with GPT-4) and the original Chatbot Arena methodology, plus a sober analysis of judge biases.",
                venue="NeurIPS 2023 D&B",
            ),
            Paper(
                title="Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference",
                authors="Chiang, Zheng, Sheng, Angelopoulos, Li, Li, Zhang, Zhu, Jordan, Gonzalez, Stoica",
                year="2024",
                url="https://arxiv.org/abs/2403.04132",
                summary="Describes the LMSYS Chatbot Arena pipeline — pairwise human votes, Bradley-Terry / Elo aggregation, sampling and bias controls.",
                venue="ICML 2024",
            ),
            Paper(
                title="AlpacaEval: An Automatic Evaluator of Instruction-following Models",
                authors="Li, Zhang, Dubois, Taori, Gulrajani, Guestrin, Liang, Hashimoto",
                year="2023",
                url="https://arxiv.org/abs/2305.14387",
                summary="Companion line of work on length-controlled LM-as-judge evaluation. Useful background for understanding judge bias mitigations.",
                venue="arXiv",
            ),
        ],
        extras=[
            Extra(
                label="Chatbot Arena leaderboard (lmarena.ai)",
                url="https://lmarena.ai/",
            ),
            Extra(
                label="IFEval on GitHub (google-research)",
                url="https://github.com/google-research/google-research/tree/master/instruction_following_eval",
            ),
            Extra(
                label="MT-Bench / FastChat repository",
                url="https://github.com/lm-sys/FastChat",
            ),
        ],
    ),
]
