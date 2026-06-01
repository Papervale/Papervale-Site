# Papervale Trees — Website Rebuild

A plain static HTML rebuild of [papervaletrees.com](https://www.papervaletrees.com), migrating away from Weebly/Block. The Ecwid shop (Lightspeed Commerce) is retained as an embedded widget, preserving existing stock control and CRM integration.

---

## Stack

| Layer | Technology | Notes |
|-------|-----------|-------|
| Pages | Plain HTML5 + CSS | No frameworks, no build step |
| Design system | Clay (adapted) | See `docs/DESIGN.md` |
| Shop | Ecwid embed | Lightspeed Commerce backend retained |
| Hosting | Netlify (planned) | See `docs/DEPLOY.md` |
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
├── grow-strong.html              Growing methods
├── selecting.html                Tree selection guide
├── availability.html             Stock list + downloads
├── planting-aftercare.html       Planting guide
├── shop.html                     Ecwid shop embed
│
├── components/
│   └── ukisg-banner.js          Custom web component for UKISG banner
│
├── assets/
│   ├── images/                   Photography
│   ├── brand/                    Logo, favicon
│   └── video/                    Hero video (when self-hosted)
│
├── docs/
│   ├── DESIGN.md                 Design tokens & system
│   ├── PAGES.md                  Page inventory & status
│   ├── INTERNAL-LINKING-STRATEGY.md   Internal link structure
│   ├── ECWID.md                  Shop embed reference
│   ├── DEPLOY.md                 Netlify deployment guide
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
1. Edit `styles.css` — changes apply to all 8 pages automatically

**For page-specific changes** (hero section, specific band styling, etc.):
1. Open the relevant `.html` file in any text editor (VS Code recommended)
2. Edit the page-specific `<style>` block and save
3. Refresh in browser to preview
4. When happy, push to GitHub → Netlify auto-deploys

---

## Key Contacts

See `docs/CONTENT.md` for all contact details, opening hours, and shared copy.

---

## Shop Integration

The Ecwid shop is embedded via JavaScript widget. See `docs/ECWID.md` for store ID, embed code, and all category/product IDs used across the site.
