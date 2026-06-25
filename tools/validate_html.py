#!/usr/bin/env python3
"""
Check all HTML pages for broken internal links, missing image src references,
and missing required page elements (title, nav, footer).
Outputs a pass/fail report to stdout.
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
PAGES = list(ROOT.glob("*.html"))
IMAGES_DIR = ROOT / "images"

errors = []
warnings = []


def check(page: Path):
    html = page.read_text(encoding="utf-8")
    name = page.name

    # Required elements
    for tag, label in [
        (r"<title>", "missing <title>"),
        (r'class="nav-links"', "missing nav-links"),
        (r'class="site-footer"', "missing site-footer"),
    ]:
        if not re.search(tag, html):
            errors.append(f"{name}: {label}")

    # Internal links resolve to real files
    for href in re.findall(r'href="([^"#]+\.html)"', html):
        target = ROOT / href
        if not target.exists():
            errors.append(f"{name}: broken link → {href}")

    # Image src references exist (skip external and onerror-hidden ones)
    for src in re.findall(r'src="(images/[^"]+)"', html):
        img_path = ROOT / src
        if not img_path.exists():
            warnings.append(f"{name}: missing image → {src} (add to images/)")

    # CSS / JS assets
    for ref in re.findall(r'(?:href|src)="((?:css|js)/[^"]+)"', html):
        if not (ROOT / ref).exists():
            errors.append(f"{name}: missing asset → {ref}")


for page in sorted(PAGES):
    check(page)

print(f"\nValidated {len(PAGES)} pages\n")

if errors:
    print("ERRORS (must fix):")
    for e in errors:
        print(f"  ✗ {e}")
else:
    print("  ✓ No errors")

if warnings:
    print("\nWARNINGS (images not yet added):")
    for w in warnings:
        print(f"  ⚠ {w}")

print()
sys.exit(1 if errors else 0)
