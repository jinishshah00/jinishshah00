# -*- coding: utf-8 -*-
"""Regenerates assets/portrait.png — the 1-bit dithered portrait used by the card.

    python3 tools/make_portrait.py

Reads assets/avatar.jpg, isolates the subject from the flat studio background,
flattens the lighting, then Floyd-Steinberg dithers to a 140x192 bitmap of white
pixels on transparency. The card uses it as an SVG luminance mask, so the colour
comes from the card's gradient, not from this file.
"""
import os, statistics
from collections import deque
from PIL import Image, ImageOps, ImageEnhance, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "assets", "avatar.jpg")
OUT = os.path.join(HERE, "..", "assets", "portrait.png")

CROP = (0.15, 0.01, 0.85, 0.97)   # left, top, right, bottom as fractions
GW, GH = 140, 192                 # dither grid
MIX, CTR, GAMMA, K, RADIUS = 0.35, 1.35, 0.85, 1.5, 0.12


def load():
    im = Image.open(SRC).convert("L")
    w, h = im.size
    l, t, r, b = CROP
    return im.crop((int(w*l), int(h*t), int(w*r), int(h*b)))


def bg_mask(im, tol=26):
    """Flood-fill the flat studio background inward from the border."""
    small = im.resize((200, 200), Image.LANCZOS); px = small.load(); W, H = small.size
    border = ([px[x, 0] for x in range(W)] + [px[x, H-1] for x in range(W)] +
              [px[0, y] for y in range(H)] + [px[W-1, y] for y in range(H)])
    med = statistics.median(border)
    seen = bytearray(W*H); q = deque()

    def push(x, y):
        if not seen[y*W+x] and abs(px[x, y]-med) <= tol:
            seen[y*W+x] = 1; q.append((x, y))

    for x in range(W): push(x, 0); push(x, H-1)
    for y in range(H): push(0, y); push(W-1, y)
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < W and 0 <= ny < H: push(nx, ny)
    m = Image.frombytes("L", (W, H), bytes(255 if b else 0 for b in seen))
    m = m.filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1.5))
    return m.resize(im.size, Image.LANCZOS).point(lambda v: 255 if v > 128 else 0)


def local_contrast(im, radius, k):
    """Subtract the low-frequency illumination so features survive dithering."""
    blur = im.filter(ImageFilter.GaussianBlur(radius))
    diff = ImageChops.subtract(im, blur, scale=1, offset=128)
    return diff.point(lambda v: max(0, min(255, int(128 + (v-128)*k))))


def main():
    im = load()
    subj = ImageOps.invert(bg_mask(im))
    g = Image.blend(local_contrast(im, int(im.size[0]*RADIUS), K),
                    ImageOps.autocontrast(im, cutoff=1, mask=subj), MIX)
    g = ImageEnhance.Contrast(g).enhance(CTR)
    g = g.filter(ImageFilter.UnsharpMask(radius=3, percent=120, threshold=2))
    g = g.point(lambda v: max(0, min(255, int(255*((v/255.0)**GAMMA)))))

    bits = g.resize((GW, GH), Image.LANCZOS).convert("1").load()
    msk = subj.resize((GW, GH), Image.LANCZOS).point(lambda v: 255 if v > 120 else 0).load()
    out = Image.new("RGBA", (GW, GH), (0, 0, 0, 0)); op = out.load()
    lit = 0
    for y in range(GH):
        for x in range(GW):
            if msk[x, y] and bits[x, y]:
                op[x, y] = (255, 255, 255, 255); lit += 1
    out.save(OUT)
    print(f"{GW}x{GH}, {lit} lit pixels -> {OUT}")


if __name__ == "__main__":
    main()
