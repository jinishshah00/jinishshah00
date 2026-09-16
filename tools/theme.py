# -*- coding: utf-8 -*-
"""Shared palette, fonts and small SVG helpers for the README panels."""

MONO = ("ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,"
        "'DejaVu Sans Mono','Liberation Mono',monospace")

# neon-on-navy
BG0   = "#060a16"   # page / card ground
BG1   = "#080e1e"   # inner panels
BG2   = "#0b1226"   # cards
CYAN  = "#22d3ee"
CYAN2 = "#67e8f9"
VIO   = "#a78bfa"
VIO2  = "#c4b5fd"
MAG   = "#e879f9"
GREEN = "#4ade80"
TEXT  = "#dbe4ff"
DIM   = "#5b6b93"
DIM2  = "#3d4a6e"
LINE  = "#17213f"

LANG = {          # GitHub language colours
    "TypeScript": "#3178c6", "Python": "#3572A5", "Go": "#00ADD8",
    "JavaScript": "#f1e05a", "C": "#555555", "HTML": "#e34c26",
    "Swift": "#F05138", "Dart": "#00B4AB",
}


def defs_common(extra=""):
    """Gradients, glow filters and the CRT overlay shared by every panel."""
    return (
        '<defs>'
        f'<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="#7aa2f7"/>'
        f'<stop offset="1" stop-color="{VIO}"/></linearGradient>'
        f'<linearGradient id="bg" x1="0" y1="0" x2=".7" y2="1">'
        f'<stop offset="0" stop-color="#081028"/><stop offset=".55" stop-color="{BG0}"/>'
        f'<stop offset="1" stop-color="#0a0f28"/></linearGradient>'
        '<pattern id="crt" width="4" height="4" patternUnits="userSpaceOnUse">'
        f'<rect width="4" height="2" fill="{BG0}" opacity=".20"/></pattern>'
        '<filter id="neon" x="-25%" y="-25%" width="150%" height="150%">'
        '<feGaussianBlur stdDeviation="4" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="b"/>'
        '<feMergeNode in="SourceGraphic"/></feMerge></filter>'
        '<filter id="glow" x="-14%" y="-10%" width="128%" height="120%">'
        '<feGaussianBlur stdDeviation="1.3" result="b"/>'
        '<feComponentTransfer in="b" result="b2"><feFuncA type="linear" slope="1.25"/></feComponentTransfer>'
        '<feMerge><feMergeNode in="b2"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        + extra + '</defs>'
    )


def style_common(extra=""):
    return (
        '<style>'
        f'text{{font-family:{MONO};white-space:pre}}'
        '.rv{animation:rv .5s cubic-bezier(.2,.8,.3,1) backwards}'
        '@keyframes rv{from{opacity:0;transform:translateX(-6px)}to{opacity:1;transform:none}}'
        '.fade{animation:fade .9s ease-out backwards}'
        '@keyframes fade{from{opacity:0}to{opacity:1}}'
        '.pulse{animation:pulse 5.2s ease-in-out infinite}'
        '@keyframes pulse{0%,100%{opacity:.30}50%{opacity:.70}}'
        '.dot{animation:dot 2.4s ease-in-out infinite}'
        '@keyframes dot{0%,100%{opacity:1}50%{opacity:.35}}'
        + extra +
        '@media (prefers-reduced-motion:reduce){'
        '.rv,.fade,.pulse,.dot,.sweep,.cur,.breathe{animation:none}.sweep{opacity:0}}'
        '</style>'
    )


def window(A, W, H, title, right_label):
    """Rounded terminal window: neon frame, title bar, traffic lights."""
    A(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="url(#bg)"/>')
    A(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="none" '
      f'stroke="url(#edge)" stroke-width="3" filter="url(#neon)" class="pulse"/>')
    A(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="none" '
      f'stroke="url(#edge)" stroke-width="1.2" opacity=".95"/>')
    A(f'<path d="M2 36H{W-2}" stroke="{LINE}"/>')
    for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")):
        A(f'<circle cx="{28+i*18}" cy="19" r="5.4" fill="{c}"/>')
    A(f'<text x="{W/2}" y="23" text-anchor="middle" font-size="11.5" fill="{DIM}">{title}</text>')
    A(f'<text x="{W-26}" y="23" text-anchor="end" font-size="10.5" fill="{CYAN}" '
      f'opacity=".8">{right_label}</text>')


def brackets(A, x, y, w, h, color, cls="pulse", arm=20, inset=3):
    """Corner brackets, the scanner-frame detail from the reference."""
    for cx, cy, sx, sy in ((x, y, 1, 1), (x+w, y, -1, 1), (x, y+h, 1, -1), (x+w, y+h, -1, -1)):
        A(f'<path d="M{cx+sx*inset} {cy+sy*arm}V{cy+sy*9}'
          f'Q{cx+sx*inset} {cy+sy*inset} {cx+sx*9} {cy+sy*inset}H{cx+sx*arm}" '
          f'fill="none" stroke="{color}" stroke-width="2" class="{cls}"/>')


def crt(A, W, H):
    A(f'<clipPath id="cardclip"><rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16"/></clipPath>')
    A(f'<rect clip-path="url(#cardclip)" x="0" y="0" width="{W}" height="{H}" fill="url(#crt)" '
      f'opacity=".45" pointer-events="none"/>')
