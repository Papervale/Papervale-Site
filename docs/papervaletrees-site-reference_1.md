# Papervale Trees — Full Site Reference
**URL:** https://www.papervaletrees.com  
**Platform:** Static HTML on Netlify (migrated from Weebly, May 2026)  
**Ecommerce:** Ecwid (by Lightspeed Commerce) — embedded on shop.html, read-only API used for product pages  
**Last updated:** June 2026

---

## Site Structure

### Navigation (Primary — rendered by `<app-nav>` component)
- Home `/index.html`
- Shop `/shop.html` ← Ecwid embed
- Trees `/tree-catalogue.html` ← catalogue of 228 product pages
- Availability `/availability.html`
- Our Roots `/our-roots.html` ← dropdown: Life at Papervale, Services We Provide
- Grow Strong `/grow-strong.html`
- Contact Us `/contact.html` ← CTA style

### Core Pages (root level)
| File | Purpose |
|------|---------|
| `index.html` | Home |
| `shop.html` | Ecwid shop embed |
| `tree-catalogue.html` | Tree catalogue index — 228 cards, 16-category filter, live search |
| `availability.html` | Seasonal availability PDF/XLSX download |
| `grow-strong.html` | Learning hub |
| `how-we-grow-our-trees.html` | Growing methods |
| `selecting-a-tree.html` | Tree selection guide |
| `planting-aftercare.html` | Planting & aftercare guide |
| `our-roots.html` | About the nursery |
| `services-we-provide.html` | Professional planting services |
| `gallery.html` | Photo gallery (Life at Papervale) |
| `contact.html` | Contact form + address |

### Trees Section
| Item | Detail |
|------|--------|
| Index | `tree-catalogue.html` |
| Product pages | `trees/[slug].html` — 228 pages |
| Shared CSS | `trees/product.css` |
| Source | Ecwid API (read-only) — products with non-placeholder images |
| Excluded | 202 products with "Image Coming Soon" placeholder |

### Shared Components
| Component | File | Purpose |
|-----------|------|---------|
| `<app-nav>` | `components/app-nav.js` | Navigation (desktop + mobile hamburger) |
| `<app-footer>` | `components/app-footer.js` | Footer |
| `<ukisg-banner>` | `components/ukisg-banner.js` | Top certification banner |
| — | `components/shared.js` | Shared JS utilities |

---

## Page Content

---

### HOME `/index.html`

**Tagline:** Supplying over 300 varieties of home-grown trees across the UK and Ireland.

**Supporting Customers section:**
From our nursery to your landscape - trusted support every step of the way

Three tiles: Grow | Select | Plant

**Body copy:**
Whether you're a home gardener, landscape architect, or commercial contractor, Papervale Trees offers tailored support, expert advice, and product selection to match your specific needs.

**Featured section — three tiles:**
- Bareroot & Rootball (links to `shop.html#!/Bareroot-&-Rootball/c/192286841`)
- Autumn Colour (links to `shop.html#!/Autumn-Colour/c/171941051`)
- Gift Card (links to `shop.html#!/Gift-card/p/759030857`)

**Footer links:** Home, Shop, Trees, Availability, Our Roots, Grow Strong, Planting & Aftercare  
**Address:** 48 Old Newry Road, Rathfriland, Newry, Co. Down, BT34 5BQ  
**Phone:** 028 3085 0059

---

### SHOP `/shop.html`

**Headline:** Find your Perfect Partner

Ecwid full-store embed. Store ID: `73482057`. Product grid loads via JavaScript.

**Static copy below shop embed:**
Orders and Dispatch — Every day, trees leave our nursery on their way to homes, farms, and projects across the UK and Ireland. 2–3 day tracked courier service.

---

### TREE CATALOGUE `/tree-catalogue.html`

**Purpose:** Browse all 228 tree products with real photos from the Ecwid store.

**Features:**
- 16-category filter bar (sticky, top: 64px)
- Live search input
- Product cards with image, Latin name, common name, category tags, price, stock status
- Cards link to individual product pages (`trees/[slug].html`)
- Category data uses lowercase hyphenated slugs (`data-cats` attribute)

**Categories (16):** Autumn Colour, Bark Interest, Flowering Trees, Fruit Trees, Conifers, Native Trees, Specimen Trees, Deciduous, Evergreen, Small Gardens, Fast Growing, Wildlife, Shade Trees, Street Trees, Weeping, Nut Trees

---

### INDIVIDUAL PRODUCT PAGES `/trees/[slug].html` (228 pages)

**Path resolution:** `<base href="../">` — all assets and components load from root

**SEO per page:**
- Title: `Buy [Common Name] Trees | UK Nursery | Papervale Trees`
- Meta description: `Buy homegrown [Common] ([Latin]) trees from Papervale Trees. From £XX. [cats]. Peat-free, UKISG certified. UK & Ireland delivery.`
- `robots: index, follow`
- Canonical: `https://www.papervaletrees.com/trees/[slug].html`
- OpenGraph tags (title, description, image, url, type=product)
- Geo tags: `GB-DOW`, Rathfriland

**Schema.org:**
- `Product` — name, description, image, SKU, brand, offer (price, availability, seller, url)
- `BreadcrumbList` — Home / Trees / [Common Name]

**Layout:**
- Visible breadcrumb nav (Home / Trees / [Product Name])
- Product hero: sticky image gallery (main image + up to 5 thumbnails) | product info column
- Product info: Latin name, common name, RHS Award badge (if applicable), price, stock badge, category tags, available options table, Buy from Shop button
- Description section: full Ecwid product description (HTML)
- Schema note: nursery contact details

---

### AVAILABILITY `/availability.html`

**Downloadable files:**
- Excel Availability List: `/files/theme/AvailabilityListAutumnR_AW_2025.xlsx`
- PDF Availability List: `/files/theme/AvailabilityListAutumnR_AW_2025.pdf`

**CTA:** Visit Our Shop → `/shop.html`

---

### OUR ROOTS `/our-roots.html`

**Headline:** Family Run from the foothills of the Mournes

Founded 2015 by Jonathan and Diane Jackson. Located outside Rathfriland on the site of a historic Paper Mill.

Jonathan: graduate in Arboriculture & Urban Forestry  
Diane: background in Business & IT

Mission: "To provide a wide range of quality home-grown trees using sustainable, forward-thinking methods."

**Sustainability:** Peat-free from start, slotted air-pruning pots, IPM, efficient water use, natural weed suppression, low-input field growing.

---

### GROW STRONG `/grow-strong.html`

Strong Roots (corrugated slotted pots), Shaping for Success (formative pruning), Growing Sustainably (peat-free, IPM, green manure), British Standard Quality (BS8545), UKISG Certified (Northern Ireland's first).

---

### HOW WE GROW `/how-we-grow-our-trees.html`

Growing methods and nursery practices.

---

### SELECTING A TREE `/selecting-a-tree.html`

Tree selection guide. Species recommendations to be reviewed by Jonathan Jackson.

---

### PLANTING & AFTERCARE `/planting-aftercare.html`

Before Planting, Planting Your Tree (square hole technique), Supporting Your Tree (staking, ties, guards), Watering (establishment schedule), Feeding (slow-release fertiliser from second spring).

---

### SERVICES `/services-we-provide.html`

Professional planting and aftercare services.

---

### GALLERY `/gallery.html`

Photo gallery — Life at Papervale.

---

### CONTACT `/contact.html`

**Contact form fields:** First Name, Last Name, Email, Enquiry Details, Marketing consent checkbox  
**Status:** Form submission not yet wired to Netlify Forms (pending)

**Address:**
Papervale Trees  
48 Old Newry Road  
Rathfriland, Co. Down  
Northern Ireland, BT34 5BQ

**Hours:** Mon–Fri By Appointment | Sat 10am–2pm | Sun Closed  
**Phone:** 028 3085 0059  
**Email:** info@papervaletrees.com

---

## Old Species Pages (previously 404 on Weebly — now rebuilt)

Many old Weebly species pages that were returning 404 have now been replaced by new pages in `trees/`. The old URLs (e.g. `/acer-griseum.html`) do not redirect — users landing on old links should be guided via Search Console or a redirect rule if needed.

| Old URL (404) | New page |
|---------------|---------|
| `/acer-griseum.html` | `trees/acer-griseum-paperbark-maple.html` |
| `/betula-pendula-tristis.html` | `trees/betula-pendula-tristis-weeping-silver-birch.html` |
| `/liquidambar-styraciflua.html` | `trees/liquidambar-styraciflua-worplesdon-sweet-gum.html` |
| `/pinus-pinea.html` | `trees/pinus-pinea-stone-pine.html` |
| `/parrotia-persica-vanessa.html` | `trees/parrotia-persica-vanessa-persian-ironwood.html` |
| `/prunus-avium.html` | `trees/prunus-avium-wild-cherry.html` |
| `/search-trees-by-species.html` | `tree-catalogue.html` |

**Recommended:** Add a `_redirects` file to the repo root (Netlify supports this natively) to 301-redirect old URLs to new ones for SEO benefit.

---

## Key Assets

| Asset | Path |
|-------|------|
| Logo (white bg, multiply blend) | `assets/brand/white_bk_logo.png` |
| Favicon | `assets/brand/favicon-dark.ico` |
| Availability List (XLSX) | `assets/docs/AvailabilityListAutumnR_AW_2025.xlsx` |
| Availability List (PDF) | `assets/docs/AvailabilityListAutumnR_AW_2025.pdf` |
| Tree product images | Ecwid CDN: `d2j6dbq0eux0bg.cloudfront.net/images/73482057/` |

---

## Ecwid Store Integration

The shop at `/shop.html` embeds Ecwid via JavaScript (store ID: `73482057`).

228 static product pages have been generated in `trees/` using the Ecwid REST API (read-only). Each product page links directly to the Ecwid product for purchasing. Product data, stock control, orders, and CRM are all managed in the Ecwid/Lightspeed dashboard — not in the HTML.

See `docs/ECWID.md` for full API reference and credentials.
