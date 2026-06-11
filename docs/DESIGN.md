# Design System — Papervale Trees

Based on: Clay design system (`npx getdesign@latest add clay`)  
Adapted for: Papervale Trees brand colours and typography

---

## CSS Architecture

All pages use a **shared stylesheet** (`styles.css`) that contains:
- Design tokens (colours, typography, spacing, border-radius)
- Reset & base styles
- Reusable components (nav, footer, buttons, forms, badges)
- Tree Catalogue page styles (`.cat-header`, `.ci-*` classes)
- Responsive breakpoints

**Tree product pages** (`trees/*.html`) additionally load a shared subfolder stylesheet:
```html
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="trees/product.css">
```

`trees/product.css` contains all product page layout styles: `.product-hero`, `.product-image-wrap`, `.product-main-img`, `.product-thumbs`, `.product-thumb`, `.product-info`, `.product-latin`, `.product-title`, `.product-award`, `.product-price-row`, `.stock-badge`, `.product-tags`, `.product-tag`, `.product-options`, `.btn-buy`, `.product-description`, `.back-link`, `.schema-note`.

**All other pages** use only `styles.css` — no inline `<style>` blocks.

This means:
- ✅ Single source of truth for design tokens (change once, applies everywhere)
- ✅ Consistent nav, footer, buttons across all pages (12 core + 228 product pages)
- ✅ Smaller HTML file sizes
- ✅ Better browser caching (shared CSS is cached)
- ✅ Easier to update brand colours, spacing, or responsive rules

To update the **entire site** (e.g. change button color):
1. Edit `styles.css`
2. All pages update automatically

To update **all product pages** (e.g. change product layout):
1. Edit `trees/product.css`

---

## Colours

### Brand

| Token | Hex | Usage |
|-------|-----|-------|
| `--primary` | `#334832` | Buttons, nav CTA, accent backgrounds |
| `--on-primary` | `#ffffff` | Text on primary buttons |
| `--brand-forest` | `#334832` | Hero backgrounds, dark bands, UKISG banner |
| `--brand-sage` | `#4c5f4b` | Tile bodies, secondary accents |
| `--brand-moss` | `#4c5f4b` | Dot accents, form focus states |
| `--brand-fern` | `#a8bf9e` | Light green accent on dark backgrounds |
| `--brand-bark` | `#5a7259` | Tile variant (Plant tile) |
| `--brand-terra` | `#c96b3d` | Featured card (Autumn Colour) |
| `--brand-wheat` | `#d4a85a` | Featured card (Gift card) |

### Canvas & Surfaces

| Token | Hex | Usage |
|-------|-----|-------|
| `--canvas` | `#faf8f3` | Page background |
| `--surface-soft` | `#f3f0e6` | Section backgrounds, about band |
| `--surface-card` | `#edeadb` | Card backgrounds |
| `--surface-strong` | `#e4e0ce` | Stronger card emphasis |
| `--hairline` | `#ddd9c8` | Borders, dividers |

### Text

| Token | Hex | Usage |
|-------|-----|-------|
| `--ink` | `#334832` | Headlines, primary text |
| `--body-strong` | `#334832` | Emphasised body copy |
| `--body` | `#4c5f4b` | Default body text |
| `--muted` | `#6b7a6c` | Secondary text, nav links |
| `--muted-soft` | `#9aaa9b` | Captions, footer fine print |

---

## Typography

### Fonts

| Font | Role | Import |
|------|------|--------|
| **Fraunces** | Display headings | Google Fonts |
| **DM Sans** | Body, UI, navigation | Google Fonts |

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,400;0,9..144,500;1,9..144,300;1,9..144,400&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### CSS Variables

```css
--font-display: 'Fraunces', Georgia, serif;
--font-body:    'DM Sans', system-ui, sans-serif;
```

### Scale

| Class | Font | Size | Weight | Use |
|-------|------|------|--------|-----|
| `.display-xl` | Fraunces | clamp(44px→80px) | 400 | Large hero titles |
| `.display-lg` | Fraunces | clamp(32px→56px) | 400 | Section openers |
| `.display-md` | Fraunces | clamp(24px→40px) | 400 | Sub-section heads |
| `.section-label` | DM Sans | 11px | 600 | Eyebrow labels (all caps) |
| body | DM Sans | 16px | 400 | Running text |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-xs` | 6px | Small badges, thumbnails |
| `--radius-sm` | 8px | Small buttons |
| `--radius-md` | 12px | Buttons, inputs, product options block |
| `--radius-lg` | 16px | Cards, product main image |
| `--radius-xl` | 24px | Feature cards, tiles |
| `--radius-pill` | 9999px | Tags, badges, filter buttons |

---

## Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--sp-xs` | 8px | Tight gaps |
| `--sp-sm` | 12px | Small gaps |
| `--sp-md` | 16px | Default gap |
| `--sp-lg` | 24px | Card padding, nav gap |
| `--sp-xl` | 32px | Section padding, nav margin-left |
| `--sp-xxl` | 48px | Large gaps, product hero gap |
| `--sp-section` | 96px | Between major page bands |

---

## Web Components

The site uses custom HTML elements (Web Components) for reusable UI:

| Component | File | Usage |
|-----------|------|-------|
| `<app-nav>` | `components/app-nav.js` | Main navigation — all pages |
| `<app-footer>` | `components/app-footer.js` | Footer — all pages |
| `<ukisg-banner>` | `components/ukisg-banner.js` | Top banner — all pages |

To use a component on a page:
1. Add `<script src="components/component-name.js"></script>` near the closing `</body>`
2. Use the element in the HTML: `<component-name></component-name>`

Tree product pages in `trees/` use `<base href="../">` so component paths resolve correctly from the subfolder without any changes to the component files.

---

## Nav Pattern

Nav is rendered by the `<app-nav>` web component (`components/app-nav.js`). To change any nav links, edit that file once — all pages update automatically.

### Current nav links (desktop + mobile)

```
Home → index.html
Shop → shop.html
Trees → tree-catalogue.html        ← added 2026-06
Availability → availability.html
Our Roots → our-roots.html         ← has dropdown
  └── Life at Papervale → gallery.html
  └── Services We Provide → services-we-provide.html
Grow Strong → grow-strong.html
Contact Us → contact.html          ← .nav-cta style
```

### CSS gotcha — breadcrumb `<nav>` vs sticky nav

The bare `nav` selector in `styles.css` applies `position: sticky; z-index: 100; height: 64px` to all `<nav>` elements. Any semantic `<nav aria-label="...">` (e.g. breadcrumbs) must be overridden with:

```css
nav[aria-label] {
  position: static;
  z-index: auto;
  height: auto;
  background: none;
  border-bottom: none;
}
```

This override is already in `styles.css` and prevents the breadcrumb from creating a competing stacking context that would hide the Our Roots dropdown.

---

## Page Header Pattern

All inner pages (not homepage) use this dark green header:

```html
<div class="page-header">
  <div class="page-header-inner">
    <p class="page-eyebrow">Eyebrow Label</p>
    <h1>Main Title<br><em>Italic accent</em></h1>
    <p>Supporting subtitle text.</p>
  </div>
</div>
```

Tree catalogue uses `.cat-header` (dark forest background with centred copy) instead of `.page-header`.

---

## Button Patterns

### Primary button
```html
<a href="#" class="btn-primary">
  Label
  <svg ...arrow icon.../>
</a>
```

### Ghost button (on dark backgrounds)
```html
<a href="#" class="btn-ghost">Label</a>
```

### Buy button (product pages)
```html
<a class="btn-buy" href="shop.html#!/PRODUCT-NAME/p/PRODUCTID">
  Buy from Shop
  <svg ...arrow icon.../>
</a>
```

---

## Responsive Breakpoints

| Breakpoint | Width | Key changes |
|------------|-------|-------------|
| Desktop | > 1100px | Full nav, 4-col product grid |
| Tablet | ≤ 1100px | 3-col product grid |
| Tablet small | ≤ 1024px | 2-col grids, stacked about sections |
| Mobile | ≤ 768px | Hamburger nav, product hero stacks |
| Mobile small | ≤ 720px | 2-col product grid |
| Small mobile | ≤ 460px | Single-col product grid |

---

## Do's

- Always use CSS variables — never hardcode hex values in page CSS
- Always use `mix-blend-mode: multiply` on the logo PNG (black background)
- Use `object-fit: cover` on all photography
- Keep section rhythm at `--sp-section` (96px) between major bands
- Use `clamp()` for all display font sizes
- Use `<base href="../">` for all `trees/` subpages to resolve root-level paths

## Don'ts

- Don't add new colours outside the token set — adapt from what's there
- Don't use `font-weight` heavier than 400 on Fraunces display headings
- Don't use the dark footer pattern (stays as `--surface-soft`)
- Don't inline hex values — always use tokens
- Don't put page-specific CSS inline in `trees/*.html` — use `trees/product.css`
