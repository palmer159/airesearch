---
id: 45
title: World Models and Embodied Agents
part: XII. Research Frontier
---

<p>Beyond text: models that learn <i>predictive models of environments</i> — simulators, video, robot dynamics —
and use them for planning. <b>Genie</b>, <b>Sora</b>, and Tesla / Wayve world models, plus the open-ended
<b>Diffusion World Model</b> agenda. Embodied AI (RT-2, OpenVLA, Pi0) plugs LMs into robot control,
demonstrating zero-shot transfer of common sense into actuation.</p>

## Papers

### Genie: Generative Interactive Environments
- **Authors:** Bruce et al. (DeepMind)
- **Year:** 2024
- **Venue:** ICML
- **URL:** https://arxiv.org/abs/2402.15391

Foundation world model trained on internet video; controllable virtual environments.

### RT-2: Vision-Language-Action Models
- **Authors:** Brohan et al. (Google)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2307.15818

VLM fine-tuned to output robot actions; transfers web-scale knowledge to manipulation.

### OpenVLA: An Open-Source Vision-Language-Action Model
- **Authors:** Kim et al.
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2406.09246

Open weights and code. The reproducible VLA baseline.

### Video generation models as world simulators (Sora technical report)
- **Authors:** OpenAI
- **Year:** 2024
- **URL:** https://web.archive.org/web/20240429024704/https://openai.com/research/video-generation-models-as-world-simulators

Diffusion-transformer-based video generator; raises 'is video pretraining a path to general world models?' (Wayback snapshot — the live openai.com URL is gated by a Cloudflare bot challenge.)
