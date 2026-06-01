# Design System — Papervale Trees

Based on: [Clay design system](https://getdesign.md) (`npx getdesign@latest add clay`)  
Adapted for: Papervale Trees brand colours and typography

---

## CSS Architecture

All pages use a **shared stylesheet** (`styles.css`) that contains:
- Design tokens (colours, typography, spacing, border-radius)
- Reset & base styles
- Reusable components (nav, footer, buttons, forms, badges)
- Responsive breakpoints

**Each HTML page** includes the shared stylesheet + page-specific styles:
```html
<link rel="stylesheet" href="styles.css">
<style>
  /* Page-specific styles only */
</style>
```

This means:
- ✅ Single source of truth for design tokens (change once, applies everywhere)
- ✅ Consistent nav, footer, buttons across all pages
- ✅ Smaller HTML file sizes
- ✅ Better browser caching (shared CSS is cached)
- ✅ Easier to update brand colours, spacing, or responsive rules

To update the **entire site** (e.g. change button color):
1. Edit `styles.css` 
2. All 8 pages update automatically

To update a **single page** (e.g. hero section):
1. Edit the `<style>` block in that HTML file

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
| `--radius-xs` | 6px | Small badges |
| `--radius-sm` | 8px | Small buttons |
| `--radius-md` | 12px | Buttons, inputs |
| `--radius-lg` | 16px | Cards |
| `--radius-xl` | 24px | Feature cards, tiles |
| `--radius-pill` | 9999px | Tags, badges |

---

## Spacing

| Token | Value | Usage |
|-------|-------|-------|
| `--sp-xs` | 8px | Tight gaps |
| `--sp-sm` | 12px | Small gaps |
| `--sp-md` | 16px | Default gap |
| `--sp-lg` | 24px | Card padding |
| `--sp-xl` | 32px | Section padding |
| `--sp-xxl` | 48px | Large gaps |
| `--sp-section` | 96px | Between major page bands |

---

## Web Components

The site uses custom HTML elements (Web Components) for reusable UI patterns:

| Component | File | Usage |
|-----------|------|-------|
| `<ukisg-banner>` | `components/ukisg-banner.js` | Top banner with UKISG certification message |

To use a component on a page:
1. Add `<script src="components/component-name.js"></script>` to the page `<head>` (before closing `</head>`)
2. Use the element in the HTML: `<component-name></component-name>`

Components use Shadow DOM for style encapsulation — their internal CSS does not affect the page, and page CSS does not affect the component (unless explicitly set via CSS custom properties).

**All existing pages already include the UKISG banner component.** This is centralized in the component file, so to update the banner message across all pages at once, edit `components/ukisg-banner.js` instead of updating individual HTML files.

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

```css
.page-header {
  background: var(--brand-forest);
  padding: 64px 0 56px;
  position: relative;
  overflow: hidden;
}
.page-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(160deg, rgba(51,72,50,0.85) 0%, rgba(51,72,50,0.4) 100%);
}
.page-header h1 em { color: var(--brand-fern); }
```

---

## Button Patterns

### Primary button
```html
<a href="#" class="btn-primary">
  Label
  <svg ...arrow icon.../>
</a>
```
```css
.btn-primary {
  background: var(--primary);
  color: var(--on-primary);
  padding: 13px 24px;
  border-radius: var(--radius-md);
  font-size: 14px;
  font-weight: 600;
}
```

### Ghost button (on dark backgrounds)
```html
<a href="#" class="btn-ghost">Label</a>
```
```css
.btn-ghost {
  background: rgba(255,255,255,0.12);
  border: 1px solid rgba(255,255,255,0.3);
  color: #fff;
  border-radius: var(--radius-md);
}
```

---

## Nav Pattern

All pages share identical nav HTML:

```html
<ukisg-banner></ukisg-banner>

<nav>
  <div class="nav-inner">
    <a href="index.html" class="nav-logo">
      <img src="assets/brand/white_bk_logo.png" ...>
    </a>
    <ul class="nav-links">
      <li><a href="index.html">Home</a></li>
      <li><a href="/shop.html">Shop</a></li>
      <li><a href="/availability.html">Availability</a></li>
      <li><a href="our-roots.html">Our Roots</a></li>
      <li><a href="grow-strong.html">Grow Strong</a></li>
      <li><a href="contact.html" class="nav-cta">Contact Us</a></li>
    </ul>
    <button class="nav-hamburger" id="hamburger">...</button>
  </div>
</nav>
<div class="mobile-menu" id="mobileMenu">...</div>
```

**The UKISG banner is now a custom web component.** Include `<script src="components/ukisg-banner.js"></script>` in the `<head>` of all pages, then use the `<ukisg-banner></ukisg-banner>` element to render it. This provides encapsulated styling (Shadow DOM) and ensures consistent appearance across all pages.

Add `class="active"` to the link matching the current page.

---

## Responsive Breakpoints

| Breakpoint | Width | Key changes |
|------------|-------|-------------|
| Desktop | > 1024px | Full nav, multi-column grids |
| Tablet | ≤ 1024px | 2-column grids, stacked about sections |
| Mobile | ≤ 768px | Hamburger nav, single column, reduced spacing |
| Small mobile | ≤ 400px | Further reductions for 360px phones |

---

## Do's

- Always use CSS variables — never hardcode hex values in page CSS
- Always use `mix-blend-mode: multiply` on the logo PNG (black background)
- Use `object-fit: cover` on all photography
- Keep section rhythm at `--sp-section` (96px) between major bands
- Use `clamp()` for all display font sizes

## Don'ts

- Don't add new colours outside the token set — adapt from what's there
- Don't use `font-weight` heavier than 400 on Fraunces display headings
- Don't use the dark footer pattern (stays as `--surface-soft`)
- Don't inline hex values — always use tokens
