---
id: 47
title: Open Problems and Research Directions (2026)
part: XII. Research Frontier
---

<p>A working researcher's list of currently-hot questions, biased toward what looks tractable:</p>
<ol>
  <li><b>Long-horizon agents</b>. Today's agents fall apart past ~50 steps. What's the right memory + planning + verifier stack?</li>
  <li><b>Inference-time compute scaling</b>. How does the optimal allocation of compute between training, search, and verification change with task?</li>
  <li><b>Verifiable rewards</b>. Can we build process-reward models that generalize beyond math/code?</li>
  <li><b>SLM specialization</b>. Routing + small expert models vs. one big model — what's the right operating point and how do we evaluate it?</li>
  <li><b><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability" target="_blank" rel="noopener">Mechanistic interpretability</a> at scale</b>. Can SAE features become a primitive in production systems (steering, oversight)?</li>
  <li><b>Continual learning without catastrophic forgetting</b>. Still essentially unsolved at frontier scale.</li>
  <li><b>Multilingual and cultural alignment</b>. The frontier is mostly English; non-Latin-script speakers pay a tokenization tax and a quality tax.</li>
  <li><b>Energy and economic sustainability</b>. Ratios of cost-per-useful-task continue to drop ~10x/year — when does the curve bend?</li>
  <li><b>AI Safety: scalable oversight</b>. Debate, weak-to-strong generalization, <a href="https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback" target="_blank" rel="noopener">RLHF</a> without humans.</li>
  <li><b>Evaluation in the wild</b>. How do we measure usefulness of agentic systems doing real work, not benchmarks?</li>
</ol>

## Papers

### Foundational Challenges in Assuring Alignment and Safety of LLMs
- **Authors:** Anwar, Saparov, Bengio, et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2404.09932

Best 'open problems' anchor — 18 challenges, hundreds of references.

### Position: Bayesian Deep Learning is Needed in the Age of Large-Scale AI
- **Authors:** Papamarkou et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.00809

Calibration and uncertainty as research directions for LMs.

### Weak-to-Strong Generalization
- **Authors:** Burns et al. (OpenAI)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2312.09390

Can a weak supervisor align a strong model? An analog for the future of human oversight.
