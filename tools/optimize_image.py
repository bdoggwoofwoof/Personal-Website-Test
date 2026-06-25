#!/usr/bin/env python3
"""
Resize and compress an image for web use, then save it to images/.
Requires Pillow: pip install Pillow

Usage:
  python tools/optimize_image.py <source_image> <output_name> [max_width]

Example:
  python tools/optimize_image.py ~/Downloads/julia.jpg julia-hero.jpg 800
"""

import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Missing dependency: pip install Pillow")
    sys.exit(1)

ROOT = Path(__file__).parent.parent
IMAGES_DIR = ROOT / "images"

# Sensible defaults per image slot
MAX_WIDTHS = {
    "julia-hero": 800,
    "about-city": 1000,
    "pricing-photo": 700,
    "contact-window": 700,
    "offering-therapy": 500,
    "offering-supervision": 500,
    "offering-consultation": 500,
}


def optimize(src: str, dest_name: str, max_width: int = 900):
    src_path = Path(src).expanduser()
    if not src_path.exists():
        print(f"Source not found: {src_path}")
        sys.exit(1)

    IMAGES_DIR.mkdir(exist_ok=True)
    dest_path = IMAGES_DIR / dest_name

    img = Image.open(src_path).convert("RGB")
    w, h = img.size

    # Auto-detect max_width from dest name stem
    stem = dest_path.stem
    auto_width = next((v for k, v in MAX_WIDTHS.items() if stem.startswith(k)), max_width)

    if w > auto_width:
        ratio = auto_width / w
        img = img.resize((auto_width, int(h * ratio)), Image.LANCZOS)

    quality = 82
    img.save(dest_path, "JPEG", quality=quality, optimize=True)

    orig_kb = src_path.stat().st_size // 1024
    new_kb = dest_path.stat().st_size // 1024
    print(f"  {src_path.name} → {dest_path.name}  ({orig_kb}KB → {new_kb}KB)")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    max_w = int(sys.argv[3]) if len(sys.argv) > 3 else 900
    optimize(sys.argv[1], sys.argv[2], max_w)
