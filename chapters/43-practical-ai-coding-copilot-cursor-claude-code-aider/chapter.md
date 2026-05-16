---
id: 43
title: Practical AI Coding: Copilot, Cursor, Claude Code, Aider
part: XI. AI for Code & Software Engineering
---

<p>The practitioner stack in 2026:</p>
<ul>
  <li><b>Inline completions</b>: GitHub Copilot, Cursor Tab, Continue.</li>
  <li><b>Chat / refactor / multi-file edits</b>: Cursor Composer, Cline, Aider, Sourcegraph Cody.</li>
  <li><b>Autonomous agents (terminal-native)</b>: Claude Code, OpenHands, Devin.</li>
</ul>
<p>Lessons from production usage:</p>
<ul>
  <li>Code review and tests do <b>not</b> become optional — they become more important, because review surface
      grows when generation is cheap.</li>
  <li>Agents need narrow, well-documented tools — same lesson as LLM tool use generally.</li>
  <li>Ergonomics dominate model quality once you are above a threshold (Claude 3.5+, GPT-4o+, Llama 3.1 70B+).</li>
</ul>

## Papers

### The Impact of AI on Developer Productivity: Evidence from GitHub Copilot
- **Authors:** Peng, Kalliamvakou, Cihon, Demirer
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2302.06590

Controlled study: Copilot users finish coding tasks 55% faster. Foundational productivity evidence.

### Measuring GitHub Copilot's Impact on Productivity
- **Authors:** Cui et al. (Microsoft)
- **Year:** 2024
- **Venue:** CACM (archive)
- **URL:** https://web.archive.org/web/20251023183058/https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/

Larger field study; ~26% more PRs per developer. (Wayback snapshot — the live cacm.acm.org URL is gated by a Cloudflare bot challenge; CACM is otherwise free to read.)

### Lost at C: A User Study on the Security Implications of Large Language Model Code Assistants
- **Authors:** Sandoval et al.
- **Year:** 2023
- **Venue:** USENIX Sec
- **URL:** https://arxiv.org/abs/2208.09727

AI-assisted code is not less secure on average — but reviewers must still review. Calibrates the productivity story.

## Extras

- [Aider](https://aider.chat/)
- [Continue (GitHub)](https://github.com/continuedev/continue)
- [OpenHands](https://github.com/All-Hands-AI/OpenHands)
