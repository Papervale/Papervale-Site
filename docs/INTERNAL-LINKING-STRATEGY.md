# Internal Linking Strategy

## Goal
Guide users through a logical journey from awareness → education → decision → action.

## User Journey Path

```
Home
├── Trees (Trees section — added 2026-06)
│   ├── Tree Catalogue (tree-catalogue.html)
│   └── Individual Product Pages (trees/*.html — 228 pages)
├── Learn (Grow Strong section)
│   ├── How We Grow Our Trees
│   ├── Selecting a Tree
│   └── Planting & Aftercare
├── Shop (Shop section)
│   ├── View Availability
│   └── Make Purchase (Ecwid widget)
└── About (Our Roots section)
    ├── Our Story
    ├── Services We Provide
    └── Contact
```

## Site Structure

### Core Pages (root level)
| File | Purpose |
|------|---------|
| `index.html` | Home / entry point |
| `shop.html` | Ecwid shop widget |
| `tree-catalogue.html` | Tree catalogue with category filters + live search |
| `availability.html` | Stock availability |
| `grow-strong.html` | Learning hub |
| `how-we-grow-our-trees.html` | Growing methods |
| `selecting-a-tree.html` | Selection guide |
| `planting-aftercare.html` | Planting guide |
| `our-roots.html` | About the nursery |
| `services-we-provide.html` | Services offered |
| `gallery.html` | Photo gallery |
| `contact.html` | Contact |

### Trees Section (228 product pages)
- `tree-catalogue.html` — category-filtered index (16 categories, live search)
- `trees/*.html` — 228 individual product pages, one per Ecwid product with real photos
  - Source: Ecwid API (read-only), filtered to products with non-placeholder images
  - Shared styles: `trees/product.css`
  - SEO: Schema.org Product + BreadcrumbList, canonical URLs, robots: index,follow
  - Each page links back to `tree-catalogue.html` (breadcrumb) and to `shop.html` (buy button)

---

## Page Relationships & Links

### Home (index.html) — Entry Point
**Links to:**
- Shop Trees → `shop.html`
- Trees Catalogue → `tree-catalogue.html`
- How We Grow → `grow-strong.html`
- About Us → `our-roots.html`
- Gallery → `gallery.html`

**Current status:** ✅ Has tile links; Trees nav link in header

---

### Tree Catalogue (tree-catalogue.html) — Trees Index
**Links to:**
- Individual product pages → `trees/[slug].html` (228 cards)
- Shop (buy CTA on each card) → `shop.html`

**Incoming links from:**
- Nav header (all pages)
- Each product page breadcrumb
- Home page

**Features:** 16-category filter bar, live search, price display, stock badges

---

### Individual Product Pages (trees/*.html) — 228 pages
**Links to:**
- Home → `index.html` (breadcrumb)
- Trees catalogue → `tree-catalogue.html` (breadcrumb)
- Shop → `shop.html#!/[product-id]` (Buy from Shop button — direct product link)

**SEO:**
- Title: `Buy [Common Name] Trees | UK Nursery | Papervale Trees`
- Meta description includes price, categories, peat-free / UKISG certified
- Schema.org: Product (SKU, price, availability) + BreadcrumbList
- Canonical: `https://www.papervaletrees.com/trees/[slug].html`
- Geo: `GB-DOW`, Rathfriland

**Opportunity:** Link from product description text to `selecting-a-tree.html` or `planting-aftercare.html`

---

### Shop (shop.html) — Conversion Point
**Links to:**
- Need help choosing? → `selecting-a-tree.html`
- Check availability → `availability.html`
- Questions? → `contact.html`

**Anchor text:** "Not sure which tree? See our selection guide" / "Check availability" / "Contact us"

---

### Grow Strong (grow-strong.html) — Learning Hub
**Links to:**
- How We Grow Our Trees → `how-we-grow-our-trees.html`
- Selecting Your Tree → `selecting-a-tree.html`
- Planting & Aftercare → `planting-aftercare.html`

**Position:** In guide content, link to specific guide pages as users read

---

### How We Grow (how-we-grow-our-trees.html) — Methods
**Links to:**
- Our Roots (about our nursery) → `our-roots.html`
- Services We Provide → `services-we-provide.html`
- Shop Trees → `shop.html`

**Anchor text:** "Learn more about who we are" / "Professional planting services" / "Browse our selection"

---

### Our Roots (our-roots.html) — About
**Links to:**
- How We Grow → `how-we-grow-our-trees.html`
- Services → `services-we-provide.html`
- Gallery → `gallery.html`
- Contact → `contact.html`

---

### Selecting a Tree (selecting-a-tree.html) — Guide #1
**Links to:**
- Shop Trees → `shop.html`
- Tree Catalogue → `tree-catalogue.html`
- Check Availability → `availability.html`
- Next: Planting Guide → `planting-aftercare.html`

**Anchor text:** "Ready to buy?" / "Browse by tree type" / "See what's in stock" / "After you purchase, follow our planting guide"

---

### Planting & Aftercare (planting-aftercare.html) — Guide #2
**Links to:**
- Back: Selecting a Tree → `selecting-a-tree.html`
- Need professional help? → `services-we-provide.html`
- Questions? → `contact.html`

**Anchor text:** "Step back to tree selection" / "Professional planting & aftercare services available" / "Still have questions? Get in touch"

---

### Services (services-we-provide.html) — Services
**Links to:**
- How We Grow (our expertise) → `how-we-grow-our-trees.html`
- About Us → `our-roots.html`
- Contact → `contact.html`

---

### Availability (availability.html) — Stock Check
**Links to:**
- Shop Trees → `shop.html`
- Tree Catalogue → `tree-catalogue.html`
- Selecting a Tree → `selecting-a-tree.html`

---

### Gallery (gallery.html) — Visual
**Links to:**
- Our Roots → `our-roots.html`
- How We Grow → `how-we-grow-our-trees.html`

---

### Contact (contact.html) — Conversion
**Links to:**
- Services → `services-we-provide.html`
- Our Roots → `our-roots.html`
- Shop → `shop.html`

---

## Implementation Notes

### Where to Add Links

1. **Contextual links in body copy** (best for SEO)
   - Link naturally within paragraphs
   - Use descriptive anchor text (not "click here")

2. **Call-to-action sections** (bottom of pages)
   - "Next step" guidance
   - "Learn more" buttons
   - "Related guides"

3. **Breadcrumbs** (all trees/ pages)
   - Home / Trees / [Product Name]
   - Already implemented on all 228 product pages

4. **Sidebar/Footer** (minimal)
   - Keep main footer links minimal (already consolidated)
   - Don't over-link

### Anchor Text Guidelines

✅ **Good:**
- "Learn how we grow our trees"
- "Check availability before ordering"
- "Next: Follow our planting guide"
- "Browse our tree catalogue"

❌ **Bad:**
- "Click here"
- "Link"
- "More info"

### Density

- **Target:** 2–5 internal links per page
- **Product pages:** already have 3 links (breadcrumb ×2 + buy button) — avoid overlinking
- **Avoid:** > 10 links per page (dilutes authority)
- **Quality over quantity** — link when it genuinely helps the user

---

## Sitemap Coverage

`sitemap.xml` includes 244 URLs:
- 11 core pages
- `tree-catalogue.html` (priority 0.8)
- 228 `trees/*.html` product pages (priority 0.7, changefreq: weekly)
- lastmod: 2026-06-11

---

## Expected Impact

- ✅ Users stay on site longer (reduced bounce rate)
- ✅ Search engines crawl more pages (244 URLs in sitemap)
- ✅ Distributes page authority across content
- ✅ Improves organic rankings for competitive keywords (tree-specific SEO on all 228 pages)
- ✅ Guides users through logical journey
- ✅ Increases conversion (shop/contact) through pathways

---

## Measurement

After implementation, track in Google Analytics:
- Average session duration
- Pages per session
- Conversion rates by landing page
- Exit pages (where users leave)
- Organic traffic to `trees/*.html` pages (new SEO surface area)
- Search Console: impressions for tree-specific queries (e.g. "buy [species] tree UK")
