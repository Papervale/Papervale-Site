# Deployment & SEO Setup Guide

## File Placement

### Files to Upload to Website Root

#### `llms.txt`
- **Destination:** `papervaletrees.com/llms.txt`
- **Purpose:** Helps AI search engines (Claude, ChatGPT, Gemini) understand your catalogue and business
- **Status:** Growing standard — submit now before competitors do
- **Action:** Place in website root (already present in repo)

#### `sitemap.xml`
- **Destination:** `papervaletrees.com/sitemap.xml`
- **Purpose:** Maps all pages to search engines, indicates priority and update frequency
- **Current coverage:** 244 URLs — 11 core pages + `tree-catalogue.html` + 228 `trees/*.html` product pages
- **Action:**
  1. File is already in repo root — auto-deployed via Netlify
  2. Submit to Google Search Console (see section below)
  3. Submit to Bing Webmaster Tools

### Files NOT to Upload

| File | Reason |
|------|--------|
| `papervale_products.csv` | Internal use only — add to `.gitignore` |
| `ecwid-products.json` | API cache — large, internal only |
| `ecwid-slugs.txt` | Internal slug list |
| `ecwid-placeholder-ids.json` | Internal placeholder filter list |

## Git Configuration

Update `.gitignore` to exclude internal files:

```gitignore
# Internal/sensitive files
papervale_products.csv
ecwid-products.json
ecwid-placeholder-ids.json

# Dependencies
node_modules/

# Build output
dist/
.cache/

# Environment variables
.env
.env.local

# OS files
.DS_Store
Thumbs.db
```

## Deployment Workflow

### Current setup: GitHub → Netlify auto-deploy

The site is live on Netlify connected to this GitHub repository. Every push to `main` triggers an automatic redeploy within ~30 seconds.

```
git add <changed files>
git commit -m "your message"
git push
# Netlify deploys automatically
```

### To regenerate tree product pages

If products are added/removed/updated in Ecwid:
1. Re-run the PowerShell generation script (fetches Ecwid API, generates `trees/*.html`)
2. Update `sitemap.xml` with new page count and URLs
3. Commit and push — Netlify redeploys

---

## Google Search Console Setup

### Initial Verification

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Click "Add property" and enter `https://www.papervaletrees.com`
3. Choose verification method:
   - **Recommended for Netlify:** HTML file
   - Google provides file like `google1234abcd.html`
   - Place in repo root, push, then click verify in GSC

### Submit Sitemap

1. In Search Console, go to **Sitemaps** (left menu)
2. Paste: `https://www.papervaletrees.com/sitemap.xml`
3. Click "Submit"
4. Google crawls and shows:
   - ✅ Pages indexed
   - ❌ Crawl errors
   - 📊 Site performance metrics
   - 🔍 Search impression data

### Monitor & Optimize

**What you'll see in Search Console:**
- Which pages are indexed
- Search queries bringing traffic
- Click-through rates (CTR) from search results
- Mobile usability issues
- Core Web Vitals (page speed)
- Crawl errors or warnings
- Impressions for tree-specific queries (e.g. "buy silver birch tree UK")

---

## Bing Webmaster Tools

1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Add property and verify (similar to Google)
3. Submit sitemap: `https://www.papervaletrees.com/sitemap.xml`
4. **Note:** Bing index powers DuckDuckGo — worth 5 minutes of setup

---

## Sitemap Details

Current `sitemap.xml` covers 244 URLs:

| Section | Count | Priority | Changefreq |
|---------|-------|----------|-----------|
| Core pages (inc. homepage) | 11 | 0.5–1.0 | weekly/monthly |
| Tree catalogue | 1 | 0.8 | weekly |
| Tree product pages (`trees/*.html`) | 228 | 0.7 | weekly |
| Homepage | 1 | 1.0 | weekly |

Last modified: 2026-06-11

Update `sitemap.xml` whenever:
- Adding/removing pages
- Adding/removing tree product pages
- Major content updates

---

## SEO Notes

### Product pages
228 dedicated tree product pages (`trees/*.html`) are now indexed individually. Each has:
- Unique title: `Buy [Common Name] Trees | UK Nursery | Papervale Trees`
- Unique meta description with species, price, and categories
- Schema.org Product + BreadcrumbList structured data
- `robots: index, follow`
- Canonical URL
- Geo tags for Rathfriland, Co. Down

This resolves the earlier limitation where searches like "buy Silver Birch tree Northern Ireland" only found the generic shop page.

---

## Checklist

- [x] Netlify connected to GitHub — auto-deploys on push
- [x] `sitemap.xml` in repo root (244 URLs)
- [x] `trees/*.html` — 228 SEO-optimised product pages
- [x] Schema.org structured data on all product pages
- [x] Canonical URLs on all product pages
- [ ] Verify domain in Google Search Console
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Monitor Search Console for indexing and search performance
- [ ] Add `ecwid-products.json` and cache files to `.gitignore`
