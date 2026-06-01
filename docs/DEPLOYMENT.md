# Deployment & SEO Setup Guide

## File Placement

### Files to Upload to Website Root

#### `llms.txt`
- **Destination:** `papervaletrees.com/llms.txt`
- **Purpose:** Helps AI search engines (Claude, ChatGPT, Gemini) understand your catalogue and business
- **Status:** Growing standard — submit now before competitors do
- **Action:** Place in website root or Netlify public folder

#### `sitemap.xml`
- **Destination:** `papervaletrees.com/sitemap.xml`
- **Purpose:** Maps all pages to search engines, indicates priority and update frequency
- **Action:** 
  1. Place in website root or Netlify public folder
  2. Submit to Google Search Console (see section below)
  3. Submit to Bing Webmaster Tools

### Files NOT to Upload

#### `papervale_products.csv`
- **Purpose:** Internal use only — product export for imports, Google Merchant feeds, or developer handoff
- **Action:** Keep locally, add to `.gitignore`

## Git Configuration

Update `.gitignore` to exclude internal files:

```gitignore
# Internal/sensitive files
papervale_products.csv

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

### For Netlify Setup

1. **Determine publish directory:**
   - Check Netlify dashboard: Settings → Build & Deploy → Publish directory
   - Usually `public/`, `dist/`, or root

2. **Place files:**
   - `llms.txt` → root of publish directory
   - `sitemap.xml` → root of publish directory

3. **Deploy:**
   - Commit files to Git: `git add llms.txt sitemap.xml`
   - Push to main branch
   - Netlify automatically builds and deploys
   - Files live at `papervaletrees.com/llms.txt` and `papervaletrees.com/sitemap.xml`

4. **Regenerate on updates:**
   - After updating product stock list or site content
   - Regenerate `sitemap.xml` and `papervale_products.csv`
   - Push changes — Netlify redeploys automatically

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

## Bing Webmaster Tools

1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Add property and verify (similar to Google)
3. Submit sitemap: `https://www.papervaletrees.com/sitemap.xml`
4. **Note:** Bing index powers DuckDuckGo — worth 5 minutes of setup

## Important Notes

### SEO Gap: Product Pages

⚠️ **Current limitation:** The sitemap covers main site pages only, not individual products
- **Why:** Lightspeed Shop loads products dynamically (no dedicated URLs)
- **Impact:** Searches like "buy Silver Birch tree Northern Ireland" hit generic shop page, not specific product page
- **Long-term consideration:** Evaluate dedicated product page URLs for better SEO

### Sitemap Frequency

Current configuration:
- Homepage: `weekly` priority 1.0
- Content pages: `weekly` priority 0.8-1.0
- Last modified: Updated when files regenerated

Update `sitemap.xml` whenever:
- Adding/removing pages
- Major content updates
- Product availability changes

## Checklist

- [ ] Determine Netlify publish directory
- [ ] Place `llms.txt` in publish directory
- [ ] Place `sitemap.xml` in publish directory
- [ ] Commit and push to Git
- [ ] Verify deployment at `papervaletrees.com/llms.txt` and `.com/sitemap.xml`
- [ ] Verify domain in Google Search Console
- [ ] Submit sitemap to Google Search Console
- [ ] Submit sitemap to Bing Webmaster Tools
- [ ] Monitor Search Console for indexing and search performance
- [ ] Add `papervale_products.csv` to `.gitignore`
