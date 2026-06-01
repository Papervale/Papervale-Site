# Internal Linking Strategy

## Goal
Guide users through a logical journey from awareness → education → decision → action.

## User Journey Path

```
Home
├── Learn (Grow Strong section)
│   ├── How We Grow Our Trees
│   ├── Selecting a Tree
│   └── Planting & Aftercare
├── Shop (Shop section)
│   ├── View Availability
│   └── Make Purchase
└── About (Our Roots section)
    ├── Our Story
    ├── Services We Provide
    └── Contact
```

## Page Relationships & Links

### Home (index.html) — Entry Point
**Links to:**
- Shop Trees → `shop.html`
- How We Grow → `grow-strong.html`
- About Us → `our-roots.html`
- Gallery → `gallery.html`

**Current status:** ✅ Already has tile links

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
- Check Availability → `availability.html`
- Next: Planting Guide → `planting-aftercare.html`

**Anchor text:** "Ready to buy?" / "See what's in stock" / "After you purchase, follow our planting guide"

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

3. **Sidebar/Footer** (minimal)
   - Keep main footer links minimal (already consolidated)
   - Don't over-link

### Anchor Text Guidelines

✅ **Good:**
- "Learn how we grow our trees"
- "Check availability before ordering"
- "Next: Follow our planting guide"

❌ **Bad:**
- "Click here"
- "Link"
- "More info"

### Density

- **Target:** 2-5 internal links per page
- **Avoid:** > 10 links per page (dilutes authority)
- **Quality over quantity** — link when it genuinely helps user

---

## Expected Impact

- ✅ Users stay on site longer (reduced bounce rate)
- ✅ Search engines crawl more pages
- ✅ Distributes page authority across content
- ✅ Improves organic rankings for competitive keywords
- ✅ Guides users through logical journey
- ✅ Increases conversion (shop/contact) through pathways

---

## Measurement

After implementation, track in Google Analytics:
- Average session duration
- Pages per session
- Conversion rates by landing page
- Exit pages (where users leave)
