# -*- coding: utf-8 -*-
"""Regenerates assets/card.svg — the SYSTEM.INFO hero panel at the top of the README.

    python3 tools/build_card.py

Left  : assets/portrait.png (see tools/make_portrait.py) as an SVG luminance mask.
Right : dotted-leader readout. Edit `rows` below to change what it says.
"""
import base64, os, sys
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from theme import (MONO, BG1, CYAN, CYAN2, VIO, VIO2, MAG, GREEN, TEXT, DIM, DIM2,
                   LINE, defs_common, style_common, window, brackets, crt)

HERE = os.path.dirname(os.path.abspath(__file__))
PORTRAIT = os.path.join(HERE, "..", "assets", "portrait.png")
OUT_PATH = os.path.join(HERE, "..", "assets", "card.svg")

W, H = 920, 540
FX, FY, FW, FH = 30, 76, 288, 404          # portrait frame
PX, PY, PW, PH = 44, 90, 260, 376          # portrait
DIVX = 346
RX, RY, RLH, RFS = 372, 78, 16.0, 11.2     # readout column

# ── readout ────────────────────────────────────────────────────────────────
rows = [("chip", "jinishshah00", "@github")]
rows += [("kv", k, v) for k, v in [
    ("Subject",       "Jinish Shah"),
    ("Role",          "AI-Native Software Engineer"),
    ("Education",     "M.S. Computer Science · Santa Clara Univ."),
    ("Focus",         "Agentic AI · Distributed Systems · Devtools"),
    ("Status",        "building systems that think"),
    ("ToolChain",     "zsh · nvim · Claude Code · Docker"),
]]
rows += [("gap", "", "")]
rows += [("kv", k, v) for k, v in [
    ("Core.Lang",     "TypeScript · Python · Go · JavaScript · C"),
    ("Core.Frontend", "React · Next.js · Tailwind"),
    ("Core.Backend",  "Node.js · FastAPI · Express · Kafka"),
    ("Core.Database", "PostgreSQL · MongoDB · Redis"),
    ("Core.Infra",    "Docker · Kubernetes · AWS · GCP"),
    ("Core.AI",       "Claude API · RAG · LangChain · PyTorch"),
]]
rows += [("gap", "", ""), ("sec", "Contact", "")]
rows += [("kv", k, v) for k, v in [
    ("Grid.Mail",      "j.dev.shah@gmail.com"),
    ("Grid.Portfolio", "jinishshah00.github.io"),
    ("Grid.GitHub",    "@jinishshah00"),
]]
rows += [("gap", "", ""), ("sec", "Live", "")]
rows += [("kv", k, v) for k, v in [
    ("Repos",         "17 public · 22 total"),
    ("Orgs",          "HalfByteCloudServices · Web-Team-Encode"),
]]
rows += [("gap", "", ""), ("blocks", "", ""), ("gap", "", ""), ("more", "", "")]

KEYW = 15
leader = lambda k: k + " " + "." * max(1, KEYW - len(k)) + " "
b64 = base64.b64encode(open(PORTRAIT, "rb").read()).decode()

out = []; A = out.append
A(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
  f'viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
  f'aria-label="Jinish Shah — AI-native software engineer. M.S. Computer Science, Santa Clara '
  f'University. TypeScript, Python, Go, React, Node.js, Docker, Kubernetes, AWS, GCP, Claude API. '
  f'Contact j.dev.shah@gmail.com, jinishshah00.github.io, github.com/jinishshah00.">')
A('<title>jinishshah00 — SYSTEM.INFO</title>')

A(defs_common(
    f'<linearGradient id="skin" x1="0" y1="0" x2=".3" y2="1">'
    f'<stop offset="0" stop-color="#d7f6ff"/><stop offset=".45" stop-color="#a9cdff"/>'
    f'<stop offset="1" stop-color="{VIO2}"/></linearGradient>'
    f'<linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{CYAN}" stop-opacity="0"/>'
    f'<stop offset=".5" stop-color="#e6f6ff" stop-opacity=".55"/>'
    f'<stop offset="1" stop-color="{VIO}" stop-opacity="0"/></linearGradient>'
    f'<radialGradient id="halo" cx=".5" cy=".4" r=".62">'
    f'<stop offset="0" stop-color="{VIO}" stop-opacity=".30"/>'
    f'<stop offset="1" stop-color="{VIO}" stop-opacity="0"/></radialGradient>'
    f'<mask id="pmask" maskUnits="userSpaceOnUse" x="{PX}" y="{PY}" width="{PW}" height="{PH}">'
    f'<image href="data:image/png;base64,{b64}" xlink:href="data:image/png;base64,{b64}" '
    f'x="{PX}" y="{PY}" width="{PW}" height="{PH}" preserveAspectRatio="none" '
    f'image-rendering="pixelated" style="image-rendering:pixelated;image-rendering:crisp-edges"/>'
    f'</mask>'
    f'<clipPath id="pclip"><rect x="{PX}" y="{PY}" width="{PW}" height="{PH}"/></clipPath>'))

A(style_common(
    '.sweep{animation:sweep 4.6s cubic-bezier(.45,0,.55,1) infinite}'
    '@keyframes sweep{0%{transform:translateY(-34px);opacity:0}10%{opacity:1}'
    '88%{opacity:1}100%{transform:translateY(__SW__px);opacity:0}}'
    '.cur{animation:cur 1.05s steps(1) infinite}'
    '@keyframes cur{0%,50%{opacity:1}51%,100%{opacity:0}}'
    '.breathe{animation:breathe 5.2s ease-in-out infinite}'
    '@keyframes breathe{0%,100%{opacity:.92}50%{opacity:1}}'
    .replace('__SW__', str(PH + 38))))

window(A, W, H, "jinish@github — ~/profile — zsh", "jinish.connect@github")

# ── left: VISUAL.MAP ───────────────────────────────────────────────────────
A(f'<text class="rv" style="animation-delay:.1s" x="{FX+2}" y="{FY-12}" font-size="10.4" '
  f'font-weight="700" letter-spacing="2.4" fill="{CYAN2}">VISUAL.MAP</text>')
A(f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="10" fill="#050912"/>')
A(f'<rect x="{PX-8}" y="{PY-8}" width="{PW+16}" height="{PH+16}" fill="url(#halo)"/>')
A('<g class="fade" style="animation-delay:.35s">')
A('<g class="breathe" filter="url(#glow)">')
A(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="url(#skin)" mask="url(#pmask)"/>')
A('</g>')
A(f'<g clip-path="url(#pclip)"><rect class="sweep" x="{PX}" y="{PY-10}" width="{PW}" '
  f'height="34" fill="url(#scan)" opacity=".12"/></g>')
A('</g>')
A(f'<rect x="{FX}" y="{FY}" width="{FW}" height="{FH}" rx="10" fill="none" '
  f'stroke="{CYAN}" stroke-width="1.3" opacity=".55"/>')
brackets(A, FX, FY, FW, FH, CYAN)
A(f'<text class="rv" style="animation-delay:1.7s" x="{FX+2}" y="{FY+FH+20}" font-size="9.4" '
  f'fill="{DIM2}" xml:space="preserve">avatar.jpg → floyd-steinberg  ·  140×192  ·  1-bit</text>')

# ── right: SYSTEM.INFO ─────────────────────────────────────────────────────
A(f'<path d="M{DIVX} 50V{H-22}" stroke="{LINE}"/>')
A(f'<text class="rv" x="{RX}" y="{RY}" font-size="12.4" font-weight="700" letter-spacing="2.6" '
  f'fill="{CYAN2}">SYSTEM.INFO</text>')
A(f'<path class="rv" style="animation-delay:.15s" d="M{RX+118} {RY-4}H{W-30}" stroke="{LINE}"/>')

y = RY + 26
for idx, (kind, a, b) in enumerate(rows):
    st = f'style="animation-delay:{0.3+idx*0.07:.2f}s"'
    if kind == "gap":
        y += RLH * 0.5; continue
    if kind == "chip":
        tw = (len(a) + len(b)) * 7.0 + 18
        A(f'<g class="rv" {st}>')
        A(f'<rect x="{RX}" y="{y-12}" width="{tw:.0f}" height="19" rx="5" fill="{VIO}" opacity=".18"/>')
        A(f'<rect x="{RX}" y="{y-12}" width="{tw:.0f}" height="19" rx="5" fill="none" '
          f'stroke="{VIO}" stroke-width="1" opacity=".55"/>')
        A(f'<text x="{RX+9}" y="{y+1}" font-size="11.4" font-weight="700" fill="{VIO2}" '
          f'xml:space="preserve">{a}<tspan fill="{DIM}" font-weight="400">{b}</tspan></text>')
        A('</g>'); y += RLH + 8; continue
    if kind == "sec":
        A(f'<text class="rv" {st} x="{RX}" y="{y:.0f}" font-size="10.6" font-weight="700" '
          f'letter-spacing="1.4" fill="{MAG}" xml:space="preserve">- {a} </text>')
        A(f'<path class="rv" {st} d="M{RX+78} {y-4:.0f}H{W-30}" stroke="{LINE}"/>')
    elif kind == "kv":
        A(f'<text class="rv" {st} x="{RX+4}" y="{y:.0f}" font-size="{RFS}" xml:space="preserve">'
          f'<tspan fill="{CYAN2}">{escape(leader(a))}</tspan>'
          f'<tspan fill="{TEXT}">{escape(b)}</tspan></text>')
    elif kind == "blocks":
        pal = ["#f7768e", "#ff9e64", "#e0af68", GREEN, "#73daca", CYAN, "#7aa2f7", VIO]
        for j, c in enumerate(pal):
            A(f'<rect class="rv" style="animation-delay:{0.3+idx*0.07+j*0.05:.2f}s" '
              f'x="{RX+4+j*17}" y="{y-10:.0f}" width="13" height="13" rx="2.5" fill="{c}"/>')
        A(f'<text class="rv" {st} x="{RX+4+8*17+12}" y="{y:.0f}" font-size="10.2" '
          f'fill="{DIM2}" xml:space="preserve">tokyonight · neon</text>')
    elif kind == "more":
        A(f'<text class="rv" {st} x="{RX}" y="{y:.0f}" font-size="10.6" xml:space="preserve">'
          f'<tspan fill="{GREEN}">▸ </tspan>'
          f'<tspan fill="{DIM}">more about me &amp; projects below in README</tspan></text>')
    y += RLH

# ── footer ─────────────────────────────────────────────────────────────────
fy = H - 24
PROMPT = "➜  ~/profile git push --force-of-habit "
A(f'<text class="rv" style="animation-delay:2.4s" x="{RX}" y="{fy}" font-size="{RFS}" xml:space="preserve">'
  f'<tspan fill="{GREEN}">➜</tspan><tspan fill="{CYAN2}">  ~/profile </tspan>'
  f'<tspan fill="{TEXT}">git push --force-of-habit</tspan></text>')
A(f'<rect class="cur" x="{RX+len(PROMPT)*RFS*0.605:.0f}" y="{fy-9}" width="7" height="11" fill="{GREEN}"/>')
A(f'<circle class="dot" cx="{FX+6}" cy="{fy-4}" r="3.4" fill="{GREEN}"/>')
A(f'<text class="rv" style="animation-delay:2.5s" x="{FX+18}" y="{fy}" font-size="10.4" '
  f'fill="{DIM}" xml:space="preserve">online · building in public</text>')

crt(A, W, H)
A('</svg>')
open(OUT_PATH, "w").write("\n".join(out))
print("card.svg", len("\n".join(out)), "bytes")
