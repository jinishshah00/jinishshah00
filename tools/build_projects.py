# -*- coding: utf-8 -*-
"""Regenerates assets/projects.svg — the PROJECTS.LIST panel.

    python3 tools/build_projects.py

Static by design: everything here is checked in, so edit `PROJECTS` below when a
repo changes. Star counts are point-in-time, not live.
"""
import os, sys, textwrap
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from theme import (BG2, CYAN, CYAN2, VIO, VIO2, MAG, GREEN, TEXT, DIM, DIM2, LINE,
                   LANG, defs_common, style_common, window, brackets, crt)

OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "assets", "projects.svg")

W, H = 920, 556
CW, CH, GAPX, GAPY = 424, 128, 18, 14
X0, Y0 = 26, 104

PROJECTS = [
    dict(repo="jinishshah00/meridian", name="meridian_", icon="◆", tint=CYAN2, lang="TypeScript", stars=1,
         desc="Mac-resident assistant agent. Intent / Plan / Reality layers, "
              "Apple Calendar + Reminders, Claude Code executor.",
         pills=["TypeScript", "Claude API", "AppleScript"]),
    dict(repo="jinishshah00/DocGPT-pdf-rag-qa", name="DocGPT_", icon="◈", tint=VIO2, lang="Python", stars=5,
         desc="PDF question-answering with RAG, agentic search and "
              "self-reflection loops. Cited answers, not guesses.",
         pills=["Python", "RAG", "LangChain"]),
    dict(repo="jinishshah00/logsleuth", name="logsleuth_", icon="▣", tint=GREEN, lang="TypeScript", stars=1,
         desc="Full-stack security log analyzer. CSV / Nginx / Apache in, "
              "SOC summaries, timelines and anomalies out.",
         pills=["TypeScript", "React", "Node.js"]),
    dict(repo="jinishshah00/sentinelflow", name="sentinelflow_", icon="◉", tint=MAG, lang="Go", stars=1,
         desc="Security event ingestion, triage and action on GCP. "
              "Zero-trust service auth, ML classifier, Next.js console.",
         pills=["Go", "GCP", "Pub/Sub"]),
    dict(repo="jinishshah00/TrashBox", name="TrashBox_", icon="▲", tint=CYAN2, lang="Python", stars=1,
         desc="AI trash classifier. One photo to 94.8% accuracy across "
              "12 categories and 32 subcategories.",
         pills=["Python", "FastAPI", "EfficientNet"]),
    dict(repo="jinishshah00/orderstream", name="orderstream_", icon="⬢", tint=VIO2, lang="TypeScript", stars=1,
         desc="Event-driven order processing. Kafka topics, idempotent "
              "consumers, Postgres for truth, Redis for speed.",
         pills=["TypeScript", "Kafka", "Redis"]),
]

out = []; A = out.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
  f'role="img" aria-label="Projects: ' +
  escape("; ".join(f"{p['repo']} — {p['desc']}" for p in PROJECTS)) + '">')
A('<title>PROJECTS.LIST</title>')
A(defs_common())
A(style_common())
window(A, W, H, "jinish@github — ~/projects — zsh", "./projects.sh --all")

# header
A(f'<text class="rv" x="26" y="72" font-size="12.4" font-weight="700" letter-spacing="2.6" '
  f'fill="{CYAN2}">PROJECTS.LIST</text>')
A(f'<path class="rv" style="animation-delay:.12s" d="M168 68H{W-26}" stroke="{LINE}"/>')
A(f'<text class="rv" style="animation-delay:.18s" x="{W-26}" y="72" text-anchor="end" '
  f'font-size="10" fill="{DIM2}">6 public · 45+ across orgs</text>')


def wrap(s, n=60):
    return textwrap.wrap(s, n)[:2]


for i, p in enumerate(PROJECTS):
    cx = X0 + (i % 2) * (CW + GAPX)
    cy = Y0 + (i // 2) * (CH + GAPY)
    d = 0.3 + i * 0.12
    st = f'style="animation-delay:{d:.2f}s"'
    A(f'<g class="rv" {st}>')
    A(f'<rect x="{cx}" y="{cy}" width="{CW}" height="{CH}" rx="10" fill="{BG2}" '
      f'stroke="{LINE}" stroke-width="1"/>')
    A(f'<rect x="{cx}" y="{cy}" width="3" height="{CH}" rx="1.5" fill="{p["tint"]}" opacity=".85"/>')
    # repo path
    A(f'<text x="{cx+16}" y="{cy+22}" font-size="9.2" fill="{DIM2}">{escape(p["repo"])}</text>')
    # name
    A(f'<text x="{cx+16}" y="{cy+44}" font-size="13.4" font-weight="700" fill="{p["tint"]}" '
      f'xml:space="preserve">{p["icon"]}  {escape(p["name"])}</text>')
    # description
    for j, line in enumerate(wrap(p["desc"])):
        A(f'<text x="{cx+16}" y="{cy+63+j*14}" font-size="10" fill="{DIM}">{escape(line)}</text>')
    # tech pills
    px = cx + 16
    for label in p["pills"]:
        pw = len(label) * 5.9 + 16
        A(f'<rect x="{px}" y="{cy+CH-30}" width="{pw:.0f}" height="17" rx="8.5" '
          f'fill="{p["tint"]}" opacity=".13"/>')
        A(f'<rect x="{px}" y="{cy+CH-30}" width="{pw:.0f}" height="17" rx="8.5" fill="none" '
          f'stroke="{p["tint"]}" stroke-width=".8" opacity=".40"/>')
        A(f'<text x="{px+pw/2:.0f}" y="{cy+CH-18}" text-anchor="middle" font-size="8.8" '
          f'fill="{p["tint"]}">{escape(label)}</text>')
        px += pw + 7
    # language dot + stars
    lc = LANG.get(p["lang"], CYAN)
    A(f'<circle cx="{cx+CW-104}" cy="{cy+40}" r="4.2" fill="{lc}"/>')
    A(f'<text x="{cx+CW-94}" y="{cy+44}" font-size="9.6" fill="{DIM}">{escape(p["lang"])}</text>')
    A(f'<circle cx="{cx+CW-30}" cy="{cy+CH-22}" r="15" fill="none" stroke="{LINE}" stroke-width="2"/>')
    A(f'<circle cx="{cx+CW-30}" cy="{cy+CH-22}" r="15" fill="none" stroke="{p["tint"]}" '
      f'stroke-width="2" stroke-linecap="round" stroke-dasharray="{min(94, 14+p["stars"]*16)} 94" '
      f'transform="rotate(-90 {cx+CW-30} {cy+CH-22})" opacity=".9"/>')
    A(f'<text x="{cx+CW-30}" y="{cy+CH-18}" text-anchor="middle" font-size="9.6" '
      f'font-weight="700" fill="{TEXT}">★{p["stars"]}</text>')
    A('</g>')

# footer
fy = H - 24
A(f'<circle class="dot" cx="32" cy="{fy-4}" r="3.4" fill="{GREEN}"/>')
A(f'<text class="rv" style="animation-delay:1.3s" x="44" y="{fy}" font-size="10.4" fill="{DIM}" '
  f'xml:space="preserve">also: square-peg-explorer · Spam-Msg-Classifier · PAPapp · '
  f'Explora-Geometry-App · PageReplaceSimAOS</text>')
A(f'<text class="rv" style="animation-delay:1.4s" x="{W-26}" y="{fy}" text-anchor="end" '
  f'font-size="10.4" fill="{DIM2}">links below ▾</text>')

crt(A, W, H)
A('</svg>')
open(OUT_PATH, "w").write("\n".join(out))
print("projects.svg", len("\n".join(out)), "bytes")
