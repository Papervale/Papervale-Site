# Pages — Inventory & Status

Live site: https://www.papervaletrees.com  
Rebuilt site: Static HTML on Netlify

---

## Status Key

| Symbol | Meaning |
|--------|---------|
| ✅ | Built and complete |
| 🔧 | Built but needs work |
| 🔲 | Not yet started |
| ❌ | Will not rebuild (deprecated) |

---

## Page Inventory

| Page | HTML File | Status | Source URL | Notes |
|------|-----------|--------|------------|-------|
| Home | `index.html` | ✅ | `/` | Hero video, tiles, featured cards, email signup |
| Contact | `contact.html` | 🔧 | `/contact.html` | Form needs backend wiring (Netlify Forms) |
| Our Roots | `our-roots.html` | ✅ | `/our-roots.html` | Uses IMG_3491.jpg |
| Grow Strong | `grow-strong.html` | ✅ | `/grow-strong.html` | |
| Selecting | `selecting-a-tree.html` | 🔧 | `/selecting-a-tree.html` | Original had visual guides — expanded with structured content. Jonathan to review species recommendations |
| Availability | `availability.html` | ✅ | `/availability.html` | PDF + XLSX download links; updated each season |
| Planting & Aftercare | `planting-aftercare.html` | ✅ | `/planting-aftercare.html` | |
| Shop | `shop.html` | ✅ | `/shop.html` | Ecwid full-store embed only — see `ECWID.md` |
| How We Grow | `how-we-grow-our-trees.html` | ✅ | `/how-we-grow-our-trees.html` | Growing methods & nursery practices |
| Services | `services-we-provide.html` | ✅ | `/services-we-provide.html` | Professional planting & aftercare services |
| Gallery | `gallery.html` | ✅ | `/gallery.html` | Photo gallery |

**All pages now use the `<ukisg-banner>` custom web component** for the top banner. Update `components/ukisg-banner.js` to change the banner message across all pages at once.

---

## Deprecated Pages (404 on live site — do not rebuild)

These pages exist in Google's index but return 404 on the current live site. They were part of an older version of the site and should not be rebuilt unless content is confirmed.

| Page | Old URL |
|------|---------|
| Carpinus betulus 'Frans Fontaine' | `/carpinus-betulus-frans-fontaine.html` |
| Betula papyrifera | `/betula-papyrifera.html` |
| Acer griseum | `/acer-griseum.html` |
| Liquidambar styraciflua | `/liquidambar-styraciflua.html` |
| Search Trees by Species | `/search-trees-by-species.html` |
| Past Present & Future | `/past-present--future.html` |
| (+ 15 other old species pages) | See site reference doc |

---

## Outstanding Tasks

### Contact page
- [ ] Wire form to Netlify Forms (add `netlify` attribute to `<form>` tag)
- [ ] Test form submission and confirmation message
- [ ] Confirm email address is correct

### Selecting page
- [ ] Jonathan to review species recommendations for accuracy
- [ ] Check all species mentioned are in current Papervale stock range

### Availability page (to build)
- [ ] Upload current availability PDF + XLSX to assets
- [ ] Update download links each season
- [ ] Consider whether to embed PDF inline

### Shop page (to build)
- [ ] Get Ecwid embed script from Ecwid dashboard
- [ ] Confirm store ID
- [ ] Test widget loads correctly on static page

### All pages
- [ ] Replace `href="/shop.html"` links with correct relative paths once shop page is built
- [ ] Add Open Graph meta tags for social sharing
- [ ] Add Google Analytics or privacy-respecting alternative
- [ ] Test on iOS Safari, Android Chrome, Firefox
- [ ] Check all images have descriptive `alt` text
