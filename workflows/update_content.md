# Update Website Content

## Objective
Edit copy, pricing, contact info, or other text across the site without breaking layout or navigation.

## Required inputs
- Which page to update (home, about, offerings, pricing, contact)
- What text to change and what it should become

## Steps

1. Open the relevant HTML file in root:
   - `index.html` — Home
   - `about.html` — About bio and credentials
   - `offerings.html` — Service descriptions
   - `pricing.html` — Session fee, sliding scale note, good faith text
   - `contact.html` — Intro text, email address, phone number

2. Make the edit. Text content lives inside elements — don't modify class names or structural tags.

3. If changing **contact info** (email or phone), it appears in three places:
   - The page itself (e.g. `contact.html`)
   - The footer of **every** page (`site-footer` in each `.html` file)
   - Update all of them.

4. Validate:
   ```bash
   python3 tools/validate_html.py
   ```

5. Review in browser at `http://localhost:3000`.

## Common locations

| Content | File | What to look for |
|---|---|---|
| Hero intro text | `index.html` | `<p>I'm a licensed psychotherapist…` |
| Dark section quote | `index.html` | `<p>Everything we need to heal…` |
| Bio paragraphs | `about.html` | `class="about-text"` |
| Accordion items | `about.html` | `class="accordion-item"` |
| Service descriptions | `offerings.html` | `class="offering-card"` |
| Session price | `pricing.html` | `<h2>Each 50 minute…` |
| Sliding scale note | `pricing.html` | `<p>Should finances…` |
| Good faith text | `pricing.html` | `class="good-faith-section"` |
| Contact email/phone | `contact.html` + all footers | `juliajarroldlcsw@gmail.com`, `646-974-1599` |

## Edge cases
- Accordion content: the `+` trigger and collapsible body are separate elements — only edit the text inside `class="accordion-body"`, not the button label if you want it to match.
- Links in the about bio: update both the visible text and the `href` attribute.
