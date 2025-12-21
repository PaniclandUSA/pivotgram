#!/usr/bin/env python3
"""
PIVOTGRAM-92 Master Sheet Generator

Generates a periodic-table-style SVG referencing canonical glyph SVGs.
"""

import os
from pathlib import Path

# -------- CONFIG --------

ROOT = Path(__file__).resolve().parents[1]

GLYPH_DIR = ROOT / "glyphs" / "canonical"
OUT_DIR = ROOT / "docs"
OUT_FILE = OUT_DIR / "PIVOTGRAM_92_MASTER_SHEET.svg"

COLUMNS = 12
CELL_W = 200
CELL_H = 120
START_Y = 100

SVG_WIDTH = CELL_W * COLUMNS
SVG_HEIGHT = START_Y + CELL_H * 8 + 40

# -------- HELPERS --------

def parse_glyph_filename(fname: str):
    """
    E100_INSTANT.svg → ("E100", "INSTANT")
    """
    base = fname.replace(".svg", "")
    parts = base.split("_", 1)
    if len(parts) != 2:
        return None
    return parts[0], parts[1].replace("_", " ")

# -------- LOAD GLYPHS --------

glyphs = []

for f in sorted(GLYPH_DIR.iterdir()):
    if f.suffix.lower() != ".svg":
        continue
    parsed = parse_glyph_filename(f.name)
    if not parsed:
        continue
    code, name = parsed
    glyphs.append((code, name, f))

if len(glyphs) != 92:
    print(f"⚠️ Warning: expected 92 glyphs, found {len(glyphs)}")

# -------- SVG BUILD --------

OUT_DIR.mkdir(exist_ok=True)

with open(OUT_FILE, "w", encoding="utf-8") as svg:
    svg.write(f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}"
     viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">

  <title>PIVOTGRAM-92 — Canonical Semantic Audit Table</title>

  <rect width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="#ffffff"/>

  <text x="{SVG_WIDTH//2}" y="40"
        font-family="Arial, sans-serif"
        font-size="32"
        font-weight="bold"
        text-anchor="middle">
    PIVOTGRAM-92 — Canonical Semantic Audit Vocabulary
  </text>

  <text x="{SVG_WIDTH//2}" y="70"
        font-family="Arial, sans-serif"
        font-size="16"
        text-anchor="middle"
        fill="#444">
    4-Axis Semantic Manifold · Audit-Safe · Compiler-Stable
  </text>
''')

    for i, (code, name, path) in enumerate(glyphs):
        col = i % COLUMNS
        row = i // COLUMNS

        x = col * CELL_W
        y = START_Y + row * CELL_H

        svg.write(f'''
  <g id="cell_{code}">
    <rect x="{x}" y="{y}"
          width="{CELL_W}" height="{CELL_H}"
          fill="none" stroke="#ddd" stroke-width="1"/>

    <image x="{x + (CELL_W-64)//2}"
           y="{y + 18}"
           width="64" height="64"
           xlink:href="../glyphs/canonical/{path.name}"/>

    <text x="{x + CELL_W//2}" y="{y + 92}"
          font-family="Arial, sans-serif"
          font-size="13"
          text-anchor="middle">
      {name}
    </text>

    <text x="{x + CELL_W//2}" y="{y + 108}"
          font-family="Courier, monospace"
          font-size="11"
          text-anchor="middle"
          fill="#666">
      U+{code}
    </text>
  </g>
''')

    svg.write(f'''
  <text x="{SVG_WIDTH//2}" y="{SVG_HEIGHT - 12}"
        font-family="Courier, monospace"
        font-size="12"
        text-anchor="middle"
        fill="#888">
    92 Canonical Glyphs · Non-Invertible Semantic Audit Layer · github.com/PaniclandUSA/pivotgram
  </text>

</svg>
''')

print(f"✅ Generated: {OUT_FILE}")
