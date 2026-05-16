---
id: 35
title: LM-as-Judge, Arena, and Pairwise Eval
part: IX. Evaluation
---

<p>For open-ended generation, automated metrics (BLEU, ROUGE) are weak. <b>LMSYS Chatbot Arena</b> uses crowdsourced
pairwise human votes; <b>MT-Bench</b> uses an LM judge. Both are influential, both have known issues (length bias,
position bias, judge-model preference for its own family). Read Zheng et al. for the standard caveats and
de-biasing techniques.</p>

## Papers

### Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- **Authors:** Zheng et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2306.05685

Establishes LM-judge methodology, identifies biases, validates against human ranking.

### Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference
- **Authors:** Chiang et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.04132

Live leaderboard methodology; the paper behind lmarena.ai.

### AlpacaEval
- **Authors:** Li et al.
- **Year:** 2023
- **Venue:** Stanford
- **URL:** https://github.com/tatsu-lab/alpaca_eval

Length-controlled LM-judge; cheap iteration during post-training.
