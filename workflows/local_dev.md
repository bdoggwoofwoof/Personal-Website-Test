# Local Development

## Objective
Run the website locally for editing and review.

## Start the server

```bash
python3 tools/serve.py
```

Opens `http://localhost:3000` in your browser automatically.
Pass a port number to override: `python3 tools/serve.py 8080`

## Validate before reviewing changes

```bash
python3 tools/validate_html.py
```

Checks all pages for:
- Broken internal links
- Missing CSS/JS assets
- Missing nav or footer elements
- Image src references not yet in `images/`

Image warnings are expected until photos are added — they don't block the site.

## File locations

| What | Where |
|------|-------|
| Pages | `*.html` in root |
| Styles | `css/styles.css` |
| Interactions | `js/main.js` |
| Images (add here) | `images/` |
| Temp/scratch files | `.tmp/` |

## Edge cases
- Port 3000 already in use: run `lsof -i :3000` to find the process, or use a different port.
- Changes not showing: hard refresh with Cmd+Shift+R (Mac).
