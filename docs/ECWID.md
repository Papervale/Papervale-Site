# Ecwid Shop — Embed Reference

Platform: Ecwid by Lightspeed Commerce  
Live shop URL: https://www.papervaletrees.com/shop.html  
Ecwid dashboard: https://my.ecwid.com

---

## Store Details

| Field | Value |
|-------|-------|
| Store ID | *(get from Ecwid dashboard → Settings → General)* |
| Store owner | Papervale Trees |
| Platform | Ecwid (Lightspeed Commerce) |
| Currency | GBP |

---

## How to Find Your Store ID

1. Log in to https://my.ecwid.com
2. Go to **Settings → General**
3. Your Store ID is shown at the top of the page
4. It is also visible in the embed code snippet

---

## Full Store Embed

This is what goes on `shop.html` to render the complete Ecwid storefront.  
Get the exact code from your Ecwid dashboard: **Website → Embed Store → Get code**

```html
<!-- Ecwid full store widget — paste your actual embed code here -->
<div id="my-store-XXXXXXXX"></div>
<script>
  window.ecwid_script_defer = true;
  window.ecwid_dynamic_widgets = true;
  if (typeof Ecwid !== 'undefined') Ecwid.init();
</script>
<script data-cfasync="false" type="text/javascript"
  src="https://app.ecwid.com/script.js?XXXXXXXX&data_platform=code"
  charset="utf-8">
</script>
```

Replace `XXXXXXXX` with your actual Store ID.

---

## Category IDs

These are used in homepage featured card links and any category-specific embeds.

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

## Search Widget

To embed a product search bar:

```html
<div class="ecwid ecwid-search"></div>
```

This is already on the homepage above the supporting section.

---

## Important Notes

- The Ecwid widget loads entirely via JavaScript — the shop page HTML will appear empty if JavaScript is disabled
- Do **not** try to scrape or replicate product data in static HTML — always use the Ecwid embed
- The Ecwid backend handles: stock levels, orders, customer accounts, payments, CRM
- Delivery settings, pricing, and product management are all done in the Ecwid dashboard, not in the HTML
- The embed script must be present on every page that shows shop content

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
