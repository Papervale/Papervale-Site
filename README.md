# Papervale Trees — Website

A plain static HTML site for [papervaletrees.com](https://www.papervaletrees.com), migrating away from Weebly/Block. The Ecwid shop (Lightspeed Commerce) is retained as an embedded widget, preserving existing stock control and CRM integration.

---

## Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Pages | Plain HTML5 + CSS | No frameworks, no build step |
| Design system | Clay (adapted) | See `docs/DESIGN.md` |
| Shop | Ecwid embed | Lightspeed Commerce backend retained |
| Hosting | Netlify | See `docs/DEPLOY.md` and `docs/DEPLOYMENT.md` |
| Fonts | Google Fonts | Fraunces + DM Sans |

---

## Project Structure

```
papervale-site/
│
├── styles.css                    Shared stylesheet (design tokens, nav, footer, buttons)
│
├── index.html                    Homepage
├── contact.html                  Contact form + info
├── our-roots.html                About the nursery
├── grow-strong.html              Growing methods overview
├── how-we-grow-our-trees.html    Detailed growing methods
├── selecting-a-tree.html         Tree selection guide
├── availability.html             Stock list + downloads
├── planting-aftercare.html       Planting guide
├── services-we-provide.html      Services page
├── gallery.html                  Photo gallery
├── faq.html                      Frequently asked questions
├── tree-catalogue.html           Full tree catalogue index
├── shop.html                     Ecwid shop embed
├── thank-you.html                Form submission confirmation
├── 404.html                      404 error page
│
├── trees/                        Auto-generated product pages (~430 files)
│   └── [species-slug].html       One page per tree product
│
├── components/
│   ├── app-nav.js               Global navigation web component
│   ├── app-footer.js            Global footer web component
│   ├── shared.js                Shared component utilities
│   └── ukisg-banner.js         UKISG banner web component
│
├── scripts/
│   └── generate-availability.ps1  Generates availability pages from Ecwid data
│
├── assets/
│   ├── images/                   Photography
│   ├── brand/                    Logo, favicon
│   └── video/                    Hero video (when self-hosted)
│
├── files/                        Downloadable files (PDFs, price lists, etc.)
│
├── ecwid-real-products.json      Live Ecwid product data
├── ecwid-products.json           Ecwid product data (working copy)
├── ecwid-placeholder-ids.json    Placeholder product IDs
├── ecwid-slugs.txt               Product slug list
│
├── netlify.toml                  Netlify build + redirect config
├── _redirects                    Netlify URL redirects
├── robots.txt                    Search engine crawl rules
├── sitemap.xml                   XML sitemap
├── site.webmanifest              PWA manifest
├── llms.txt                      LLMs.txt (AI crawler guidance)
│
├── docs/
│   ├── DESIGN.md                 Design tokens & system
│   ├── PAGES.md                  Page inventory & status
│   ├── INTERNAL-LINKING-STRATEGY.md   Internal link structure
│   ├── ECWID.md                  Shop embed reference
│   ├── DEPLOY.md                 Netlify deployment guide
│   ├── DEPLOYMENT.md             Deployment checklist
│   ├── CLIENT-SETUP.md           Client onboarding guide
│   └── CONTENT.md                Shared copy & contact details
│
└── README.md                     This file
```

---

## Running Locally

No build step needed. Just open any HTML file directly in your browser:

```
Double-click index.html
```

Or use a local server for a more accurate preview (optional):

```bash
# If you have Python installed
python -m http.server 8000
# Then open http://localhost:8000
```

---

## Pages Status

See `docs/PAGES.md` for the full page inventory and build status.

---

## Making Changes

**For site-wide changes** (colours, nav, footer, buttons, spacing):
1. Edit `styles.css` — changes apply to all pages automatically

**For page-specific changes** (hero section, specific band styling, etc.):
1. Open the relevant `.html` file in VS Code
2. Edit the page-specific `<style>` block and save
3. Refresh in browser to preview
4. Push to GitHub → Netlify auto-deploys

**For tree product pages** (`trees/`):
- Pages are auto-generated from Ecwid product data via `scripts/generate-availability.ps1`
- Do not edit individual tree pages by hand; regenerate from the script

---

## Key Contacts

See `docs/CONTENT.md` for all contact details, opening hours, and shared copy.

---

## Shop Integration

The Ecwid shop is embedded via JavaScript widget. See `docs/ECWID.md` for store ID, embed code, and all category/product IDs used across the site.
