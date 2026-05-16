---
id: 25
title: Why SLMs Now: Definition, Use Cases, Economics
part: VII. Small Language Models
---

<p>"Small" is relative. In 2026 a Small Language Model (SLM) is roughly <b>0.5B–10B parameters</b> — runnable on a
laptop or phone, deployable at the edge, fine-tunable on a single GPU. They power on-device assistants, latency-sensitive
production paths, agentic sub-tasks, and privacy-preserving deployments.</p>

<h4>Why an SVP cares</h4>
<ul>
  <li>Inference cost can be 10-100x lower than frontier models.</li>
  <li>Privacy: data never leaves the device or VPC.</li>
  <li>Predictable latency at the long tail.</li>
  <li>Specialization beats generality on narrow domains (e.g., one customer's API surface).</li>
</ul>

<h4>Open question</h4>
<p>Are SLMs the right substrate for agentic systems (one big general model + many small specialists)?
Belcak et al. (2024) make exactly this argument; see Ch. 27.</p>

## Papers

### A Survey of Small Language Models
- **Authors:** Lu et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2410.20011

Comprehensive 2024 survey: capabilities, training, on-device deployment, datasets, evaluation.

### Small Language Models: Survey, Measurements, and Insights
- **Authors:** Lu et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2409.15790

Hardware-grounded measurements on real devices; the most useful empirical reference for SLM deployment.

### Small Language Models are the Future of Agentic AI
- **Authors:** Belcak et al. (NVIDIA)
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2506.02153

Argues most agent sub-steps don't need a frontier model; a manifesto for SLM-first agent design.
