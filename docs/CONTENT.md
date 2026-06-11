# Content Reference — Shared Copy & Details

This file is the single source of truth for all content that appears across multiple pages.  
When any of these details change, update this file first, then find and update each HTML file listed.

---

## Business Details

| Field | Value | Appears in |
|-------|-------|-----------|
| Business name | Papervale Trees | All pages (nav, footer, title tags) |
| Address line 1 | 48 Old Newry Road | contact.html, footer (all pages) |
| Address line 2 | Rathfriland | contact.html, footer |
| Address line 3 | Co. Down, Northern Ireland | contact.html, footer |
| Postcode | BT34 5BQ | contact.html, footer |
| Phone | 028 3085 0059 | contact.html, footer |
| Phone (tel: link) | tel:02830850059 | contact.html, footer, all trees/*.html schema-note |
| Email | info@papervaletrees.com | contact.html, footer, all trees/*.html schema-note |
| Google Maps link | https://www.google.com/maps/dir//48+Old,+Newry+Rd,+Rathfriland+BT34+5BQ | contact.html |
| Founded | 2015 | our-roots.html, index.html (stats) |
| Geo region | GB-DOW | All trees/*.html meta geo.region |
| Geo placename | Rathfriland, Co. Down, Northern Ireland | All trees/*.html meta geo.placename |

---

## Opening Hours

| Day | Hours | Appears in |
|-----|-------|-----------|
| Monday – Friday | By Appointment | contact.html, footer (all pages) |
| Saturday | 10am – 2pm | contact.html, footer |
| Sunday | Closed | contact.html, footer |

---

## Social Media

| Platform | Handle / URL | Status |
|----------|-------------|--------|
| Instagram | @papervaletrees | https://www.instagram.com/papervaletrees/ |
| Facebook | Papervale Trees | https://www.facebook.com/papervaletrees/ |
| X / Twitter | @papervaletrees | https://x.com/papervaletrees |

> Social links not yet added to footer — add when confirmed active.

---

## Key Stats (used in homepage and our-roots)

| Stat | Value | Notes |
|------|-------|-------|
| Varieties | 300+ | "Over 300 varieties grown in Co. Down" |
| Homegrown | 90% | "We produce over 90% of our trees at the nursery" |
| Founded | 2015 | |
| Delivery | UK + IRL | United Kingdom and Ireland |
| Products with pages | 228 | Ecwid products with real photos — individual pages in trees/ |

---

## Certifications (used across all pages)

| Cert | Full name | Notes |
|------|-----------|-------|
| UKISG | UK & Ireland Sourcing Guarantee | Northern Ireland's first tree nursery certified |
| BS8545 | British Standard for nursery tree cultivation | |
| Peat-Free | Self-declared | Committed since founding |

---

## UKISG Banner (appears top of every page)

```
🌿 Northern Ireland's first UKISG Certified tree nursery | genuinely homegrown | fully traceable
```

**Implementation:** Rendered via the `<ukisg-banner>` custom web component (`components/ukisg-banner.js`). To update the message, edit the component file — all pages (including all 228 tree product pages) update automatically.

---

## Footer Copyright Line

```
@2026 Papervale Trees All Rights Reserved
```

Update year annually. Appears in footer of every page via `<app-footer>` component (`components/app-footer.js`).

---

## Key Quotes (used in multiple pages)

### Founder mission statement
> "To provide a wide range of quality homegrown trees using sustainable, forward-thinking methods."

*Used in: our-roots.html*

### Jonathan Jackson quote
> "We firmly believe that there is a need for the continuation of plant production, as the skill of tree growing and nursery stock production is in decline."

*Used in: our-roots.html*

### Closing promise
> "By choosing Papervale, you're not just planting a tree — you're planting purpose, progress and promise."

*Used in: our-roots.html, index.html (image band)*

### Grow Strong legacy line
> "We don't grow trees for short-term impact. We grow legacies."

*Used in: grow-strong.html*

---

## Founders

| Name | Role | Background |
|------|------|-----------|
| Jonathan Jackson | Founder / Head Grower | Graduate in Arboriculture & Urban Forestry |
| Diane Jackson | Co-Founder | Background in Business & IT |

---

## Availability List Files

Update these links each season in `availability.html`:

| File | Current path | Notes |
|------|-------------|-------|
| Excel list | `/files/theme/AvailabilityListAutumnR_AW_2025.xlsx` | Update filename each season |
| PDF list | `/files/theme/AvailabilityListAutumnR_AW_2025.pdf` | Update filename each season |

---

## Image Asset Inventory

| File | Subject | Used in |
|------|---------|---------|
| `IMG_3491.jpg` | Nursery overview with polytunnels | index.html (Grow tile), our-roots.html |
| `IMG_3524.jpg` | Trees against stone wall | index.html (Select tile), contact.html |
| `plant_orig.jpg` | Field rows ready for planting | index.html (Plant tile), grow-strong.html |
| `bareroot3.jpg` | Bareroot trees bundled | index.html (featured card) |
| `autum.jpg` | Autumn maple leaves | index.html (featured card) |
| `giftcard.png` | Gift card icon | index.html (featured card) |
| `white_bk_logo.png` | Full logo (black bg, multiply blend) | Nav + footer via app-nav/app-footer, all pages |
| `favicon-dark.ico` | Favicon | All pages |

Tree product page images are served directly from the Ecwid/Lightspeed CDN (`d2j6dbq0eux0bg.cloudfront.net`) — they are not stored locally.

---

## Page Title Format

### Core pages
```
[Page Name] — Papervale Trees
```

Examples:
- `Contact — Papervale Trees`
- `Our Roots — Papervale Trees`
- `Grow Strong — Papervale Trees`
- `Trees — Papervale Trees` (tree-catalogue.html)

### Tree product pages
```
Buy [Common Name] Trees | UK Nursery | Papervale Trees
```

Example: `Buy Paperbark Maple Trees | UK Nursery | Papervale Trees`

### Homepage
```
Papervale Trees — Homegrown Trees Across the UK & Ireland
```

---

## Tree Catalogue Categories (16)

Used as filter buttons in `tree-catalogue.html` and as `data-cats` attributes on product cards:

| Display label | Slug |
|---------------|------|
| Autumn Colour | `autumn-colour` |
| Bark Interest | `bark-interest` |
| Flowering Trees | `flowering-trees` |
| Fruit Trees | `fruit-trees` |
| Conifers | `conifers` |
| Native Trees | `native-trees` |
| Specimen Trees | `specimen-trees` |
| Deciduous | `deciduous` |
| Evergreen | `evergreen` |
| Small Gardens | `small-gardens` |
| Fast Growing | `fast-growing` |
| Wildlife | `wildlife` |
| Shade Trees | `shade-trees` |
| Street Trees | `street-trees` |
| Weeping | `weeping` |
| Nut Trees | `nut-trees` |
