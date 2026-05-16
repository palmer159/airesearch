#!/usr/bin/env python3
"""
SLM/LLM Study Guide — local HTTP server.

Serves a curated, ~48-chapter study guide on SLM and LLM research, technology, safety,
and software engineering applications. Most paper links go to authoritative public
sources (arXiv, Nature, ACM, lab blogs); only the index/chapter pages are rendered locally.

Run:
    python3 server.py [PORT]

Default port: 47314 (uncommon, unprivileged, unregistered).

No authn/authz. Bind is 127.0.0.1 only.
"""

from __future__ import annotations

import html
import json
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

from chapters import CHAPTERS, by_part

DEFAULT_PORT = 47314  # unregistered, unprivileged
HOST = "127.0.0.1"

CHAPTER_BY_ID = {c["id"]: c for c in CHAPTERS}

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------

CSS = """
:root {
  --bg: #0e1116;
  --panel: #161b22;
  --panel-2: #1c232c;
  --fg: #e6edf3;
  --muted: #8b949e;
  --accent: #79c0ff;
  --accent-2: #a5d6ff;
  --border: #30363d;
  --ok: #3fb950;
  --warn: #d29922;
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--fg);
  font: 16px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }
a { color: var(--accent); text-decoration: none; }
a:hover { color: var(--accent-2); text-decoration: underline; }
header.site {
  position: sticky; top: 0; z-index: 10;
  background: var(--panel); border-bottom: 1px solid var(--border);
  padding: 14px 24px; display: flex; align-items: center; gap: 16px;
}
header.site h1 { margin: 0; font-size: 18px; font-weight: 600; }
header.site .nav { margin-left: auto; display: flex; gap: 16px; }
.layout { display: grid; grid-template-columns: 320px 1fr; min-height: calc(100vh - 56px); }
aside.toc { background: var(--panel); border-right: 1px solid var(--border); padding: 20px;
  overflow-y: auto; max-height: calc(100vh - 56px); position: sticky; top: 56px; }
aside.toc h3 { font-size: 12px; text-transform: uppercase; letter-spacing: .12em;
  color: var(--muted); margin: 18px 0 6px; }
aside.toc h3:first-child { margin-top: 0; }
aside.toc ul { list-style: none; padding: 0; margin: 0; }
aside.toc li { margin: 2px 0; }
aside.toc a { display: block; padding: 4px 6px; border-radius: 4px; font-size: 14px; }
aside.toc a:hover { background: var(--panel-2); text-decoration: none; }
aside.toc a.active { background: var(--panel-2); color: var(--accent-2); }
aside.toc .ch-num { color: var(--muted); display: inline-block; width: 28px; }
main { padding: 36px 48px; max-width: 980px; }
main h1.chapter-title { font-size: 28px; margin: 0 0 4px; }
main .part-tag { color: var(--muted); font-size: 13px; letter-spacing: .04em; text-transform: uppercase; }
main .summary { background: var(--panel); border: 1px solid var(--border);
  border-radius: 8px; padding: 20px 24px; margin: 22px 0; }
main .summary h4 { color: var(--accent-2); margin-top: 18px; }
main h2 { font-size: 18px; margin: 32px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--border); }
.paper { background: var(--panel); border: 1px solid var(--border); border-left: 3px solid var(--accent);
  border-radius: 6px; padding: 14px 18px; margin: 12px 0; }
.paper .ptitle { font-size: 16px; font-weight: 600; }
.paper .pmeta { color: var(--muted); font-size: 13px; margin-top: 2px; }
.paper .pmeta .venue { color: var(--ok); }
.paper .psum { margin-top: 8px; color: #cdd5dd; font-size: 14.5px; }
.paper .plinks a { font-size: 13px; margin-right: 12px; }
pre { background: #0a0d12; border: 1px solid var(--border); padding: 12px 14px; border-radius: 6px;
  overflow-x: auto; font-size: 13.5px; }
code { background: #0a0d12; padding: 1px 5px; border-radius: 3px; font-size: 13.5px; }
.foot-nav { display: flex; justify-content: space-between; margin-top: 48px; padding-top: 18px;
  border-top: 1px solid var(--border); font-size: 14px; }
.foot-nav .empty { color: var(--muted); }
.search-box { width: 100%; padding: 8px 10px; background: var(--panel-2);
  border: 1px solid var(--border); border-radius: 4px; color: var(--fg); font-size: 14px; }
.cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 14px; margin-top: 18px; }
.card { background: var(--panel); border: 1px solid var(--border); border-radius: 8px; padding: 16px;
  border-top: 3px solid var(--accent); }
.card .num { color: var(--muted); font-size: 12px; }
.card h3 { margin: 4px 0 6px; font-size: 16px; }
.card p { margin: 0; color: var(--muted); font-size: 13.5px; }
.kv { color: var(--muted); font-size: 13px; }
.tag { display: inline-block; background: var(--panel-2); border: 1px solid var(--border);
  border-radius: 99px; padding: 1px 9px; font-size: 12px; color: var(--muted); margin-right: 6px; }
@media (max-width: 900px) {
  .layout { grid-template-columns: 1fr; }
  aside.toc { position: static; max-height: none; border-right: 0; border-bottom: 1px solid var(--border); }
}
"""


# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def render_layout(title: str, body: str, active_id: int | None = None) -> str:
    parts_html = []
    for part, chapters in by_part().items():
        parts_html.append(f"<h3>{html.escape(part)}</h3><ul>")
        for c in chapters:
            cls = "active" if c["id"] == active_id else ""
            parts_html.append(
                f'<li><a class="{cls}" href="/chapter/{c["id"]}">'
                f'<span class="ch-num">{c["id"]}.</span>{html.escape(c["title"])}</a></li>'
            )
        parts_html.append("</ul>")
    toc = "\n".join(parts_html)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — SLM/LLM Study Guide</title>
<style>{CSS}</style>
</head>
<body>
<header class="site">
  <h1><a href="/" style="color:inherit;text-decoration:none">SLM &amp; LLM Study Guide</a></h1>
  <span class="kv">A curated postgraduate path • 48 chapters</span>
  <nav class="nav">
    <a href="/">Index</a>
    <a href="/papers">All papers</a>
    <a href="/about">About</a>
  </nav>
</header>
<div class="layout">
  <aside class="toc">{toc}</aside>
  <main>{body}</main>
</div>
</body></html>"""


def render_index() -> str:
    parts = by_part()
    cards = []
    for part, chapters in parts.items():
        cards.append(f'<h2>{html.escape(part)}</h2><div class="cards">')
        for c in chapters:
            # take first sentence of the visible summary as a teaser
            from re import sub
            text = sub(r"<[^>]+>", " ", c["summary"])
            text = " ".join(text.split())
            teaser = text[:220] + ("…" if len(text) > 220 else "")
            cards.append(
                f'<a class="card" href="/chapter/{c["id"]}" style="display:block;color:inherit;text-decoration:none">'
                f'<span class="num">Chapter {c["id"]}</span>'
                f'<h3>{html.escape(c["title"])}</h3>'
                f'<p>{html.escape(teaser)}</p>'
                f"</a>"
            )
        cards.append("</div>")
    body = f"""
    <div class="part-tag">Welcome</div>
    <h1 class="chapter-title">A Comprehensive Study Guide for SLM &amp; LLM Research</h1>
    <div class="summary">
      <p>This guide is built for a postgraduate computer-science student who wants to do
      <b>AI research</b> and to operate as an <b>AI practitioner in tech companies</b>. It walks
      from the foundations (n-grams, transformers, BERT, GPT) through training, post-training and
      alignment, retrieval, small language models, multimodal models, evaluation, AI safety and
      interpretability, AI for code, and current open research directions.</p>
      <p>Most paper links point to authoritative public sources (arXiv, Nature, ACM, lab blogs).
      Chapter prose, illustrations, and curation are rendered locally — that's the part we generate.</p>
      <p>Start at <a href="/chapter/1">Chapter 1</a>, jump from the left-hand index, or browse all
      <a href="/papers">~150 referenced papers</a>.</p>
    </div>
    {''.join(cards)}
    """
    return render_layout("Index", body)


def render_chapter(ch: dict) -> str:
    prev_ch = CHAPTER_BY_ID.get(ch["id"] - 1)
    next_ch = CHAPTER_BY_ID.get(ch["id"] + 1)

    papers_html = []
    for p in ch.get("papers", []):
        venue = f' <span class="venue">· {html.escape(p["venue"])}</span>' if p.get("venue") else ""
        url = p["url"]
        papers_html.append(f"""
        <div class="paper">
          <div class="ptitle"><a href="{html.escape(url)}" target="_blank" rel="noopener">{html.escape(p["title"])}</a></div>
          <div class="pmeta">{html.escape(p["authors"])} · {p["year"]}{venue}</div>
          <div class="psum">{html.escape(p["summary"])}</div>
          <div class="plinks">
            <a href="{html.escape(url)}" target="_blank" rel="noopener">Open paper ↗</a>
          </div>
        </div>""")

    extras_html = ""
    if ch.get("extras"):
        items = "".join(
            f'<li><a href="{html.escape(e["url"])}" target="_blank" rel="noopener">{html.escape(e["label"])}</a></li>'
            for e in ch["extras"]
        )
        extras_html = f"<h2>Tools &amp; further reading</h2><ul>{items}</ul>"

    prev_link = (f'<a href="/chapter/{prev_ch["id"]}">← Ch. {prev_ch["id"]}: {html.escape(prev_ch["title"])}</a>'
                 if prev_ch else '<span class="empty">Start of guide</span>')
    next_link = (f'<a href="/chapter/{next_ch["id"]}">Ch. {next_ch["id"]}: {html.escape(next_ch["title"])} →</a>'
                 if next_ch else '<span class="empty">End of guide</span>')

    body = f"""
    <div class="part-tag">{html.escape(ch["part"])}</div>
    <h1 class="chapter-title">Chapter {ch["id"]} · {html.escape(ch["title"])}</h1>
    <div class="summary">{ch["summary"]}</div>
    <h2>Key papers &amp; readings</h2>
    {''.join(papers_html)}
    {extras_html}
    <div class="foot-nav">
      <div>{prev_link}</div>
      <div>{next_link}</div>
    </div>
    """
    return render_layout(ch["title"], body, active_id=ch["id"])


def render_papers() -> str:
    rows = []
    seen = set()
    total = 0
    for ch in CHAPTERS:
        for p in ch.get("papers", []):
            total += 1
            key = (p["title"], p["year"])
            if key in seen:
                continue
            seen.add(key)
            venue = f' · <span class="kv">{html.escape(p["venue"])}</span>' if p.get("venue") else ""
            rows.append(f"""
            <div class="paper">
              <div class="ptitle"><a href="{html.escape(p["url"])}" target="_blank" rel="noopener">{html.escape(p["title"])}</a></div>
              <div class="pmeta">{html.escape(p["authors"])} · {p["year"]}{venue} · <a href="/chapter/{ch["id"]}">Ch. {ch["id"]}: {html.escape(ch["title"])}</a></div>
              <div class="psum">{html.escape(p["summary"])}</div>
            </div>""")
    body = f"""
    <div class="part-tag">All references</div>
    <h1 class="chapter-title">Every paper, in one place</h1>
    <div class="summary">
      <p><b>{len(rows)}</b> unique papers and references across {len(CHAPTERS)} chapters
      (<b>{total}</b> total citations including cross-chapter overlap).
      Each entry links to the authoritative public source.</p>
    </div>
    {''.join(rows)}
    """
    return render_layout("All papers", body)


def render_about() -> str:
    body = """
    <div class="part-tag">About this guide</div>
    <h1 class="chapter-title">How this study guide is built</h1>
    <div class="summary">
      <h4>Audience</h4>
      <p>Written for a postgraduate CS student going into AI research or applied AI engineering at
      a tech company. Assumes comfort with calculus, linear algebra, probability, and basic deep learning.
      No prior NLP background required.</p>

      <h4>Structure</h4>
      <ol>
        <li>Foundations — n-grams to GPT-3 (Ch. 1-5)</li>
        <li>Training &amp; data (Ch. 6-10)</li>
        <li>Architecture frontiers — long context, MoE, SSM, FlashAttention (Ch. 11-14)</li>
        <li>Post-training &amp; alignment — SFT, RLHF, DPO, PEFT (Ch. 15-18)</li>
        <li>Reasoning &amp; agents — CoT, ReAct, agentic systems, o1/R1 reasoning (Ch. 19-22)</li>
        <li>Retrieval &amp; grounding (Ch. 23-24)</li>
        <li>Small Language Models — definition, Phi, open SLM families, quantization, distillation, on-device (Ch. 25-30)</li>
        <li>Multimodal (Ch. 31-33)</li>
        <li>Evaluation (Ch. 34-35)</li>
        <li>AI Safety &amp; alignment — including interpretability, hallucination, bias, red-teaming (Ch. 36-40)</li>
        <li>AI for code &amp; software engineering (Ch. 41-43)</li>
        <li>Research frontier &amp; open problems (Ch. 44-48)</li>
      </ol>

      <h4>Curation policy</h4>
      <p>Every cited paper is the most authoritative public source we could find — arXiv preprints
      (most reliably citable), peer-reviewed venues (NeurIPS, ICML, ICLR, ACL, EMNLP, Nature, JMLR),
      or canonical lab writeups (Anthropic Transformer Circuits, OpenAI/DeepMind technical reports).
      Where the same idea appears in both blog and paper, we prefer the paper.</p>

      <h4>Local rendering</h4>
      <p>Only chapter prose, illustrations, and the index are stored locally. Paper PDFs and HTML stay
      on their original sites — that's deliberate, both to respect publishers and to keep this server
      tiny. The tradeoff: working through this guide requires being online for the source readings.</p>
    </div>
    """
    return render_layout("About", body)


# ---------------------------------------------------------------------------
# HTTP layer
# ---------------------------------------------------------------------------

class Handler(BaseHTTPRequestHandler):
    server_version = "SLMLLMGuide/1.0"

    def _send(self, code: int, body: str, content_type: str = "text/html; charset=utf-8") -> None:
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self) -> None:  # noqa: N802
        path = unquote(urlparse(self.path).path)

        if path in ("/", "/index", "/index.html"):
            self._send(200, render_index()); return
        if path == "/papers":
            self._send(200, render_papers()); return
        if path == "/about":
            self._send(200, render_about()); return
        if path == "/health":
            self._send(200, json.dumps({"ok": True, "chapters": len(CHAPTERS)}),
                       "application/json"); return
        if path.startswith("/chapter/"):
            tail = path.removeprefix("/chapter/").strip("/")
            try:
                ch_id = int(tail)
            except ValueError:
                self._send(404, render_layout("Not found",
                    "<h1>404</h1><p>Unknown chapter.</p>")); return
            ch = CHAPTER_BY_ID.get(ch_id)
            if not ch:
                self._send(404, render_layout("Not found",
                    f"<h1>404</h1><p>No chapter {ch_id}.</p>")); return
            self._send(200, render_chapter(ch)); return

        self._send(404, render_layout("Not found",
            f"<h1>404</h1><p>No route for <code>{html.escape(path)}</code>.</p>"
            "<p><a href='/'>Back to index</a></p>"))

    def log_message(self, fmt, *args):  # quieter access log
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))


def main() -> None:
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"invalid port: {sys.argv[1]}", file=sys.stderr); sys.exit(2)

    httpd = ThreadingHTTPServer((HOST, port), Handler)
    url = f"http://{HOST}:{port}/"
    print(f"SLM/LLM Study Guide serving at {url}")
    print(f"  • {len(CHAPTERS)} chapters, ~150 references")
    print("  • Bound to 127.0.0.1 only · no auth · uncommon port")
    print("  • Ctrl-C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down")
        httpd.server_close()


if __name__ == "__main__":
    main()
