# Deployment Guide — Netlify

Hosting: [Netlify](https://netlify.com)  
Method: GitHub auto-deploy (connected to `main` branch)  
Live site: https://www.papervaletrees.com  
Status: ✅ Live — previously on Weebly, migrated to static HTML on Netlify

---

## Current Deployment Setup

The site is already live on Netlify connected to this GitHub repository. Deployment is automatic:

1. Make changes locally
2. `git add` the changed files
3. `git commit -m "description"`
4. `git push`
5. Netlify detects the push and redeploys within ~30 seconds

No build command is needed — the site is plain HTML/CSS/JS.

---

## Why Netlify

- Free tier is more than sufficient for this site
- Auto-deploy from GitHub — push a change, site updates within 30 seconds
- Free SSL certificate (HTTPS) included automatically
- Handles contact form submissions natively (no backend needed)

---

## Re-Deploying (Manual Drag-and-Drop)

If you ever need to deploy without GitHub:

1. Go to https://netlify.com and log in
2. From the dashboard click the site → **Deploys → Deploy manually**
3. Drag your entire project folder onto the upload area
   - **Important:** Include `components/`, `trees/`, `assets/` directories
4. Netlify replaces the previous version

---

## Folder Structure to Deploy

```
papervale-site/
├── index.html
├── shop.html
├── tree-catalogue.html
├── availability.html
├── grow-strong.html
├── how-we-grow-our-trees.html
├── selecting-a-tree.html
├── planting-aftercare.html
├── our-roots.html
├── services-we-provide.html
├── gallery.html
├── contact.html
├── styles.css
├── sitemap.xml
├── llms.txt
├── assets/
│   └── brand/, images/, docs/
├── components/
│   ├── app-nav.js
│   ├── app-footer.js
│   ├── ukisg-banner.js
│   └── shared.js
└── trees/
    ├── product.css
    └── [228 product pages].html
```

Do **not** deploy: `ecwid-products.json`, `ecwid-slugs.txt`, `ecwid-placeholder-ids.json`, `docs/`, `papervale_products.csv`.

---

## Contact Form Setup (Netlify Forms)

The contact form on `contact.html` needs Netlify Forms wiring to submit to email.

### 1. Add the `netlify` attribute to the form tag

```html
<!-- Change this: -->
<form onsubmit="handleSubmit(event)">

<!-- To this: -->
<form name="contact" method="POST" netlify netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact">
  <!-- hidden spam trap -->
  <p style="display:none">
    <label>Don't fill this out: <input name="bot-field"></label>
  </p>
  <!-- rest of form fields stay the same -->
```

### 2. Remove the JavaScript `handleSubmit` function

### 3. Add a thank-you page (optional)

Create `thank-you.html` and add to the form:
```html
<form ... action="/thank-you.html">
```

### 4. Set up email notifications

In Netlify dashboard: **Forms → contact → Form notifications → Add notification → Email**

---

## Domain & DNS

Domain is already connected to Netlify. DNS records point at Netlify:

```
Type: A     Name: @    Value: 75.2.60.5
Type: CNAME Name: www  Value: [site-name].netlify.app
```

If the domain ever needs to be reconnected: **Netlify → Site settings → Domain management**.

---

## Pre-Launch Checklist (for reference)

- [x] All core pages built and deployed
- [x] Tree catalogue page (tree-catalogue.html) live
- [x] 228 tree product pages (trees/*.html) live
- [x] Nav updated — Trees link added
- [x] Sitemap (244 URLs) deployed
- [x] HTTPS / SSL — green padlock
- [x] Custom domain connected (papervaletrees.com)
- [x] Ecwid shop embed loads correctly
- [ ] Contact form wired to Netlify Forms
- [ ] Google Analytics added
- [ ] Google Search Console — sitemap submitted
- [ ] Test on iOS Safari, Android Chrome, Firefox
