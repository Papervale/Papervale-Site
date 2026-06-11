# Pages — Inventory & Status

Live site: https://www.papervaletrees.com  
Platform: Static HTML on Netlify

---

## Status Key

| Symbol | Meaning |
|--------|---------|
| ✅ | Built and complete |
| 🔧 | Built but needs work |
| 🔲 | Not yet started |
| ❌ | Will not rebuild (deprecated) |

---

## Core Pages (root level)

| Page | HTML File | Status | Notes |
|------|-----------|--------|-------|
| Home | `index.html` | ✅ | Hero video, tiles, featured cards, email signup |
| Shop | `shop.html` | ✅ | Ecwid full-store embed — see `ECWID.md` |
| Tree Catalogue | `tree-catalogue.html` | ✅ | 228 product cards, 16-category filter, live search |
| Availability | `availability.html` | ✅ | PDF + XLSX download links; updated each season |
| Grow Strong | `grow-strong.html` | ✅ | Learning hub with links to guides |
| How We Grow | `how-we-grow-our-trees.html` | ✅ | Growing methods & nursery practices |
| Selecting a Tree | `selecting-a-tree.html` | 🔧 | Jonathan to review species recommendations for accuracy |
| Planting & Aftercare | `planting-aftercare.html` | ✅ | Full aftercare guide |
| Our Roots | `our-roots.html` | ✅ | About page — founders, sustainability, UKISG |
| Services | `services-we-provide.html` | ✅ | Professional planting & aftercare services |
| Gallery | `gallery.html` | ✅ | Photo gallery |
| Contact | `contact.html` | 🔧 | Form needs Netlify Forms wiring |

**All pages use the `<app-nav>` and `<app-footer>` web components** — update `components/app-nav.js` or `components/app-footer.js` to change nav/footer across all pages at once.

---

## Tree Product Pages (trees/ subfolder)

| Item | Detail |
|------|--------|
| Count | 228 pages |
| Location | `trees/[slug].html` |
| Source | Ecwid API (read-only) — products with real (non-placeholder) photos |
| Shared CSS | `trees/product.css` |
| Path resolution | `<base href="../">` — all asset/component paths resolve from root |
| Index page | `tree-catalogue.html` (root level) |

Each product page includes:
- Breadcrumb: Home / Trees / [Product Name]
- Schema.org Product + BreadcrumbList structured data
- SEO title: `Buy [Common Name] Trees | UK Nursery | Papervale Trees`
- Gallery with main image + up to 5 thumbnails
- "Buy from Shop" button → direct Ecwid product deep-link
- RHS Award badge (auto-detected from description text)

---

## Web Components

| Component | File | Used on |
|-----------|------|---------|
| `<app-nav>` | `components/app-nav.js` | All pages |
| `<app-footer>` | `components/app-footer.js` | All pages |
| `<ukisg-banner>` | `components/ukisg-banner.js` | All pages |

Note: `trees/*.html` pages load components via `<base href="../">` so no path changes are needed.

---

## Deprecated Pages (404 on old Weebly site — do not rebuild at old URLs)

These pages existed in Google's index on the old Weebly site. Many of the species listed below now have new dedicated pages at `trees/[slug].html` — do not redirect to the old paths.

| Page | Old URL (was 404) | New URL |
|------|---------|---------|
| Carpinus betulus | `/carpinus-betulus-fransfs-fontaine.html` | `trees/carpinus-betulus-common-hornbeam.html` |
| Betula pendula 'Tristis' | `/betula-pendula-tristis.html` | `trees/betula-pendula-tristis-weeping-silver-birch.html` |
| Acer griseum | `/acer-griseum.html` | `trees/acer-griseum-paperbark-maple.html` |
| Liquidambar styraciflua | `/liquidambar-styraciflua.html` | `trees/liquidambar-styraciflua-worplesdon-sweet-gum.html` |
| Pinus pinea | `/pinus-pinea.html` | `trees/pinus-pinea-stone-pine.html` |
| Parrotia persica 'Vanessa' | `/parrotia-persica-vanessa.html` | `trees/parrotia-persica-vanessa-persian-ironwood.html` |
| Prunus avium | `/prunus-avium.html` | `trees/prunus-avium-wild-cherry.html` |
| Search Trees by Species | `/search-trees-by-species.html` | `tree-catalogue.html` |
| Past Present & Future | `/past-present--future.html` | — |

---

## Outstanding Tasks

### Contact page
- [ ] Wire form to Netlify Forms (add `netlify` attribute to `<form>` tag)
- [ ] Test form submission and confirmation message

### Selecting page
- [ ] Jonathan to review species recommendations for accuracy
- [ ] Check all species mentioned are in current Papervale stock range

### Availability page
- [ ] Upload current season's PDF + XLSX to assets
- [ ] Update download links for new season

### All pages
- [ ] Add Google Analytics or privacy-respecting alternative
- [ ] Test on iOS Safari, Android Chrome, Firefox
- [ ] Check all images have descriptive `alt` text

### Tree product pages (future)
- [ ] Regenerate pages if products are added/removed/updated in Ecwid
- [ ] Consider adding contextual links from product descriptions to `selecting-a-tree.html` or `planting-aftercare.html`
