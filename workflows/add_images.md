# Add Images to the Website

## Objective
Resize, compress, and add photos to the correct slots in the site.

## Required inputs
- Source image file (any format: JPG, PNG, HEIC, etc.)
- The destination slot name (see table below)

## Image slots

| Slot filename | Page | Shape | Recommended source size |
|---|---|---|---|
| `julia-hero.jpg` | Home | Tall arch (portrait) | Portrait photo, face near top |
| `about-city.jpg` | About | Full-width rectangle | NYC skyline or landscape |
| `offering-therapy.jpg` | Offerings | Tall arch | Warm interior/nature |
| `offering-supervision.jpg` | Offerings | Tall arch | Neutral interior/texture |
| `offering-consultation.jpg` | Offerings | Tall arch | Warm neutral texture |
| `pricing-photo.jpg` | Pricing | Circle | Soft botanical / shadow |
| `contact-window.jpg` | Contact | Tall arch | Window with light/curtains |

## Steps

1. Locate or receive the source image.

2. Run the optimize tool:
   ```bash
   python3 tools/optimize_image.py <path/to/source> <slot-filename>
   ```
   Example:
   ```bash
   python3 tools/optimize_image.py ~/Downloads/julia_photo.jpg julia-hero.jpg
   ```
   The tool auto-selects the right max width per slot and saves to `images/`.

3. Validate:
   ```bash
   python3 tools/validate_html.py
   ```
   The warning for that slot should now be gone.

4. Check in browser at `http://localhost:3000`.

## Edge cases
- HEIC files (iPhone): convert to JPG first with `sips -s format jpeg file.HEIC --out file.jpg`
- Pillow not installed: `pip install Pillow`
- Image looks cropped wrong: the arch/circle frames use `object-fit: cover; object-position: center top`. For portraits, the face should be in the top-center of the source image.
