# -*- coding: utf-8 -*-
"""Regenerates assets/card.svg — the animated terminal readout at the top of the README.

    python3 tools/build_card.py

The ASCII portrait lives in assets/ascii.txt (54x39, 16-level ramp, generated from the
GitHub avatar). Edit that file or the `rows` list below and re-run.
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
ART_PATH = os.path.join(HERE, "..", "assets", "ascii.txt")
OUT_PATH = os.path.join(HERE, "..", "assets", "card.svg")

from xml.sax.saxutils import escape

ART = [l for l in open(ART_PATH).read().split("\n") if l.strip()]
COLS = max(len(l) for l in ART); ROWS = len(ART)

W, H   = 920, 520
BAR    = 34
AX, AY = 40, 64
AFS, ALH = 9.0, 9.9
DIVX   = 366
RX, RY, RLH, RFS = 392, 82, 16.4, 11.3
AW = COLS * AFS * 0.605
MONO = ("ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,"
        "'DejaVu Sans Mono','Liberation Mono',monospace")

KEY, VAL, SEC, ACC, DIM = "#7aa2f7", "#c0caf5", "#bb9af7", "#9ece6a", "#4a5880"

rows = [("head", "jinishshah00", "@github"), ("rule", "", ""), ("sec", "SYSTEM", "")]
rows += [("kv", k, v) for k, v in [
    ("subject",   "Jinish Shah"),
    ("role",      "AI-Native Software Engineer"),
    ("education", "M.S. Computer Science · Santa Clara Univ."),
    ("focus",     "Agentic AI · Distributed Backends · Devtools"),
    ("status",    "building systems that think"),
    ("shell",     "zsh · nvim · Claude Code"),
]]
rows += [("gap", "", ""), ("sec", "STACK", "")]
rows += [("kv", k, v) for k, v in [
    ("languages", "TypeScript · Python · Go · JavaScript · C"),
    ("frontend",  "React · Next.js · Tailwind"),
    ("backend",   "Node.js · FastAPI · Express · Kafka"),
    ("data",      "PostgreSQL · MongoDB · Redis"),
    ("infra",     "Docker · Kubernetes · AWS · GCP"),
    ("ai",        "Claude API · RAG · LangChain · PyTorch"),
]]
rows += [("gap", "", ""), ("sec", "CONTACT", "")]
rows += [("kv", k, v) for k, v in [
    ("email",     "j.dev.shah@gmail.com"),
    ("portfolio", "jinishshah00.github.io"),
    ("github",    "@jinishshah00"),
]]
rows += [("gap", "", ""), ("blocks", "", "")]

KEYW = 12
leader = lambda k: k + " " + "." * max(1, KEYW - len(k)) + " "

out = []; A = out.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
  f'role="img" aria-label="Terminal card: Jinish Shah, AI-native software engineer. '
  f'M.S. Computer Science, Santa Clara University. TypeScript, Python, Go, React, Node.js, '
  f'Docker, Kubernetes, AWS, GCP, Claude API.">')
A('<title>jinishshah00 — system readout</title>')

A('<defs>')
A('<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">'
  '<stop offset="0" stop-color="#7dcfff"/><stop offset=".5" stop-color="#7aa2f7"/>'
  '<stop offset="1" stop-color="#bb9af7"/></linearGradient>')
A('<linearGradient id="asciiGrad" x1="0" y1="0" x2=".3" y2="1">'
  '<stop offset="0" stop-color="#b8ecff"/><stop offset=".45" stop-color="#a9c8ff"/>'
  '<stop offset="1" stop-color="#d8bdff"/></linearGradient>')
A('<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">'
  '<stop offset="0" stop-color="#7dcfff" stop-opacity="0"/>'
  '<stop offset=".5" stop-color="#e6f6ff" stop-opacity=".55"/>'
  '<stop offset="1" stop-color="#bb9af7" stop-opacity="0"/></linearGradient>')
A('<linearGradient id="bg" x1="0" y1="0" x2=".7" y2="1">'
  '<stop offset="0" stop-color="#0b1020"/><stop offset=".55" stop-color="#0a0e18"/>'
  '<stop offset="1" stop-color="#0d1224"/></linearGradient>')
A('<radialGradient id="halo" cx=".5" cy=".4" r=".62">'
  '<stop offset="0" stop-color="#7aa2f7" stop-opacity=".34"/>'
  '<stop offset="1" stop-color="#7aa2f7" stop-opacity="0"/></radialGradient>')
A('<pattern id="crt" width="4" height="4" patternUnits="userSpaceOnUse">'
  '<rect width="4" height="2" fill="#0a0e18" opacity=".22"/></pattern>')
A(f'<clipPath id="artclip"><rect x="{AX-8}" y="{AY-12}" width="{AW+16:.0f}" '
  f'height="{(ROWS-1)*ALH+22:.0f}"/></clipPath>')
A(f'<clipPath id="cardclip"><rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="15"/></clipPath>')
A('<filter id="glow" x="-14%" y="-10%" width="128%" height="120%">'
  '<feGaussianBlur stdDeviation="2.1" result="b"/>'
  '<feComponentTransfer in="b" result="b2"><feFuncA type="linear" slope="1.45"/></feComponentTransfer>'
  '<feMerge><feMergeNode in="b2"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
A('</defs>')

sweep_to = int((ROWS - 1) * ALH + 34)
A('<style>'
  'text{font-family:%s;white-space:pre}'
  # --- intro: elements are opacity:1 by default, keyframes only animate them IN ---
  '.rv{animation:rv .5s cubic-bezier(.2,.8,.3,1) backwards}'
  '@keyframes rv{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:none}}'
  '.ar{animation:ar .45s ease-out backwards}'
  '@keyframes ar{from{opacity:0}to{opacity:1}}'
  # --- always-on motion ---
  '.sweep{animation:sweep 4.6s cubic-bezier(.45,0,.55,1) infinite}'
  '@keyframes sweep{0%%{transform:translateY(-30px);opacity:0}10%%{opacity:1}'
  '88%%{opacity:1}100%%{transform:translateY(%dpx);opacity:0}}'
  '.cur{animation:cur 1.05s steps(1) infinite}'
  '@keyframes cur{0%%,50%%{opacity:1}51%%,100%%{opacity:0}}'
  '.pulse{animation:pulse 5.2s ease-in-out infinite}'
  '@keyframes pulse{0%%,100%%{opacity:.32}50%%{opacity:.72}}'
  '.breathe{animation:breathe 5.2s ease-in-out infinite}'
  '@keyframes breathe{0%%,100%%{opacity:.92}50%%{opacity:1}}'
  '.dot{animation:dot 2.4s ease-in-out infinite}'
  '@keyframes dot{0%%,100%%{opacity:1}50%%{opacity:.35}}'
  '@media (prefers-reduced-motion:reduce){'
  '.rv,.ar,.sweep,.cur,.pulse,.breathe,.dot{animation:none}.sweep{opacity:0}}'
  '</style>' % (MONO, sweep_to))

# frame
A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="15" fill="url(#bg)"/>')
A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="15" fill="none" '
  f'stroke="url(#edge)" stroke-width="2.4" class="pulse"/>')
A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="15" fill="none" '
  f'stroke="url(#edge)" stroke-width="1" opacity=".9"/>')
A(f'<path d="M1.5 {BAR}H{W-1.5}" stroke="#1b2340"/>')
for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
    A(f'<circle cx="{26+i*17}" cy="{BAR/2}" r="5.2" fill="{c}"/>')
A(f'<text x="{W/2}" y="{BAR/2+4}" text-anchor="middle" font-size="11.5" fill="#5a678f">'
  'jinish@github — ~/profile — zsh</text>')
A(f'<text x="{W-24}" y="{BAR/2+4}" text-anchor="end" font-size="10.5" fill="{DIM}">80×24</text>')

# left: ascii portrait
A(f'<rect x="{AX-14}" y="{AY-18}" width="{AW+28:.0f}" height="{(ROWS-1)*ALH+34:.0f}" fill="url(#halo)"/>')
A('<g clip-path="url(#artclip)">')
A(f'<g class="breathe" filter="url(#glow)" fill="url(#asciiGrad)" font-size="{AFS}">')
for i, line in enumerate(ART):
    A(f'<text class="ar" style="animation-delay:{0.15+i*0.035:.2f}s" x="{AX}" '
      f'y="{AY+i*ALH:.1f}" xml:space="preserve">{escape(line)}</text>')
A('</g>')
A(f'<rect class="sweep" x="{AX-8}" y="{AY-12}" width="{AW+16:.0f}" height="26" '
  f'fill="url(#scan)" opacity=".13"/>')
A('</g>')
A(f'<text class="rv" style="animation-delay:1.7s" x="{AX}" y="{AY+(ROWS-1)*ALH+26:.0f}" '
  f'font-size="9.5" fill="{DIM}" xml:space="preserve">'
  f'avatar.jpg → ascii  ·  {COLS}×{ROWS}  ·  16 levels</text>')

# divider
A(f'<path d="M{DIVX} {BAR+14}V{H-16}" stroke="#182042"/>')

# right: neofetch readout
y = RY
for idx, (kind, a, b) in enumerate(rows):
    st = f'style="animation-delay:{0.35+idx*0.075:.2f}s"'
    if kind == "gap":
        y += RLH * 0.55; continue
    if kind == "head":
        A(f'<text class="rv" {st} x="{RX}" y="{y:.0f}" font-size="14.5" font-weight="700" '
          f'fill="{ACC}" xml:space="preserve">{a}<tspan fill="{DIM}" font-weight="400">{b}</tspan></text>')
    elif kind == "rule":
        A(f'<path class="rv" {st} d="M{RX} {y-9:.0f}H{W-30}" stroke="#232c52"/>')
        y -= RLH * 0.35
    elif kind == "sec":
        A(f'<text class="rv" {st} x="{RX}" y="{y:.0f}" font-size="10.6" font-weight="700" '
          f'letter-spacing="1.6" fill="{SEC}" xml:space="preserve">▚ {a}</text>')
    elif kind == "kv":
        A(f'<text class="rv" {st} x="{RX+10}" y="{y:.0f}" font-size="{RFS}" xml:space="preserve">'
          f'<tspan fill="{KEY}">{escape(leader(a))}</tspan><tspan fill="{VAL}">{escape(b)}</tspan></text>')
    elif kind == "blocks":
        for j, c in enumerate(["#f7768e","#ff9e64","#e0af68","#9ece6a","#73daca","#7dcfff","#7aa2f7","#bb9af7"]):
            A(f'<rect class="rv" style="animation-delay:{0.35+idx*0.075+j*0.05:.2f}s" '
              f'x="{RX+10+j*17}" y="{y-10:.0f}" width="13" height="13" rx="2.5" fill="{c}"/>')
        A(f'<text class="rv" style="animation-delay:{0.35+idx*0.075+0.5:.2f}s" x="{RX+10+8*17+12}" '
          f'y="{y:.0f}" font-size="10.5" fill="{DIM}" xml:space="preserve">tokyonight</text>')
    y += RLH

# footer prompt
fy = H - 26
PROMPT = "➜  ~/profile git push --force-of-habit "
A(f'<text class="rv" style="animation-delay:2.4s" x="{RX}" y="{fy}" font-size="{RFS}" xml:space="preserve">'
  f'<tspan fill="{ACC}">➜</tspan><tspan fill="{KEY}">  ~/profile </tspan>'
  f'<tspan fill="{VAL}">git push --force-of-habit</tspan></text>')
A(f'<rect class="cur" x="{RX+len(PROMPT)*RFS*0.605:.0f}" y="{fy-9}" width="7" height="11" fill="{ACC}"/>')
A(f'<circle class="dot" cx="{AX+4}" cy="{fy-4}" r="3.4" fill="{ACC}"/>')
A(f'<text class="rv" style="animation-delay:2.5s" x="{AX+16}" y="{fy}" font-size="10.5" '
  f'fill="{DIM}" xml:space="preserve">online · building in public</text>')

# crt overlay
A(f'<rect clip-path="url(#cardclip)" x="0" y="0" width="{W}" height="{H}" fill="url(#crt)" '
  f'opacity=".45" pointer-events="none"/>')
A('</svg>')

open(OUT_PATH, "w").write("\n".join(out))
print("cols", COLS, "rows", ROWS, "bytes", len("\n".join(out)))
