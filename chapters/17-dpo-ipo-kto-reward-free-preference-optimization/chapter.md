---
id: 17
title: DPO, IPO, KTO: Reward-Free Preference Optimization
part: IV. Post-training & Alignment
---

<p><b>Direct Preference Optimization</b> (Rafailov et al., 2023) collapses the reward model + PPO pipeline into
a single closed-form classification loss over preference pairs. It's <i>much</i> simpler to implement, more stable,
and matches RLHF on most benchmarks. DPO and its variants (IPO, KTO, ORPO) now dominate open-source post-training.</p>

<h4>The DPO loss in one line</h4>
<pre>
L_DPO = -log σ( β · ( log π(y_w|x)/π_ref(y_w|x) − log π(y_l|x)/π_ref(y_l|x) ) )
</pre>
<p>Where (y_w, y_l) is a (winner, loser) pair, π is the policy, π_ref the SFT reference, β a temperature.</p>

## Papers

### Direct Preference Optimization (DPO)
- **Authors:** Rafailov et al.
- **Year:** 2023
- **Venue:** NeurIPS
- **URL:** https://arxiv.org/abs/2305.18290

Reformulates RLHF as a closed-form classification objective; no reward model, no PPO.

### A General Theoretical Paradigm to Understand Learning from Human Preferences (IPO)
- **Authors:** Azar et al.
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.12036

Generalizes RLHF/DPO; identifies and fixes overoptimization pathologies in DPO.

### KTO: Model Alignment as Prospect Theoretic Optimization
- **Authors:** Ethayarajh et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.01306

Works with binary thumbs-up/down labels — no pairs needed; matches DPO when pairs exist.

### ORPO: Monolithic Preference Optimization without Reference Model
- **Authors:** Hong, Lee, Thorne
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.07691

Combines SFT and preference optimization in one loss with no reference model. Cheap and surprisingly strong.
