# Ecwid Shop — Embed Reference

Platform: Ecwid by Lightspeed Commerce  
Live shop URL: https://www.papervaletrees.com/shop.html  
Ecwid dashboard: https://my.ecwid.com

---

## Store Details

| Field | Value |
|-------|-------|
| Store ID | `73482057` |
| Store owner | Papervale Trees |
| Platform | Ecwid (Lightspeed Commerce) |
| Currency | GBP |

---

## API Access

| Field | Value |
|-------|-------|
| Public token | see Ecwid dashboard → Settings → API |
| Secret token | see Ecwid dashboard → Settings → API (keep private — do not commit) |
| Base URL | `https://app.ecwid.com/api/v3/73482057` |
| Auth header | `Authorization: Bearer <secret_token>` |

> **Important:** All API usage is read-only. Never use POST, PUT, or DELETE operations — the shop is managed exclusively through the Ecwid dashboard.

> **Auth note:** The `?token=` query parameter does NOT work. Always use the `Authorization: Bearer` header.

### Useful endpoints

```
GET /products            — list all products (paged)
GET /products/{id}       — single product with full image URLs
GET /categories          — all categories
```

### Placeholder image detection

202 products have an "Image Coming Soon" placeholder. These are excluded from the static product pages.  
Placeholder MD5 hash: `8E73739D2817EBCCBE6DE7F2F6DEA14D`  
Excluded product IDs are listed in `ecwid-placeholder-ids.json` at the project root.  
Cache files: `ecwid-products.json`, `ecwid-slugs.txt`

---

## How to Find Your Store ID

1. Log in to https://my.ecwid.com
2. Go to **Settings → General**
3. Your Store ID is shown at the top of the page
4. It is also visible in the embed code snippet

---

## Full Store Embed

This is what goes on `shop.html` to render the complete Ecwid storefront.

```html
<div id="my-store-73482057"></div>
<script>
  window.ecwid_script_defer = true;
  window.ecwid_dynamic_widgets = true;
  if (typeof Ecwid !== 'undefined') Ecwid.init();
</script>
<script data-cfasync="false" type="text/javascript"
  src="https://app.business.shop/script.js?73482057&data_platform=code&data_date=2026-05-04"
  charset="utf-8">
</script>
```

---

## Search Widget

The search bar in the nav header uses:

```html
<div id="my-search-73482057"></div>
```

Loaded programmatically via `components/app-nav.js` using `xSearch('id=my-search-73482057')`.

---

## Category IDs

| Category | ID | URL fragment |
|----------|----|-------------|
| Bareroot & Rootball | `192286841` | `#!/Bareroot-&-Rootball/c/192286841` |
| Autumn Colour | `171941051` | `#!/Autumn-Colour/c/171941051` |

To link to a category from any page:
```html
<a href="shop.html#!/Bareroot-&-Rootball/c/192286841">Shop Bareroot</a>
```

---

## Product IDs

| Product | ID | URL fragment |
|---------|----|-------------|
| Gift Card | `759030857` | `#!/Gift-card/p/759030857` |

To link to a specific product:
```html
<a href="shop.html#!/Gift-card/p/759030857">Buy Gift Card</a>
```

Product pages in `trees/` link to individual products using the deep-link format:
```html
<a href="shop.html#!/ACER-griseum-Paperbark-Maple/p/673684379">Buy from Shop</a>
```

---

## Single Product Widget

To embed an individual product on any page (e.g. a featured product):

```html
<div class="ecwid ecwid-product ecwid-product-PRODUCTID"
  data-single-product-id="PRODUCTID">
</div>
```

Replace `PRODUCTID` with the product's numeric ID.

---

## Static Product Pages (trees/)

228 individual product pages have been generated in the `trees/` folder — one per Ecwid product that has a real (non-placeholder) photo.

- Index page: `tree-catalogue.html` (root level)
- Product pages: `trees/[slug].html`
- Each page links to the shop via a direct product deep-link
- Source data cached in: `ecwid-products.json`, `ecwid-slugs.txt`

These pages are static HTML — they do not update automatically when products change in Ecwid. If you add, remove, or update products, regenerate the affected pages.

---

## Important Notes

- The Ecwid widget loads entirely via JavaScript — the shop page HTML will appear empty if JavaScript is disabled
- The Ecwid backend handles: stock levels, orders, customer accounts, payments, CRM
- Delivery settings, pricing, and product management are all done in the Ecwid dashboard, not in the HTML
- The embed script must be present on every page that shows shop content
- All API calls are read-only — do not modify products via the API

---

## Ecwid Dashboard Quick Links

| Task | Link |
|------|------|
| Products | https://my.ecwid.com/#products |
| Orders | https://my.ecwid.com/#orders |
| Customers | https://my.ecwid.com/#customers |
| Availability / Stock | https://my.ecwid.com/#products |
| Embed code | https://my.ecwid.com/#embed |
| Settings | https://my.ecwid.com/#settings |
