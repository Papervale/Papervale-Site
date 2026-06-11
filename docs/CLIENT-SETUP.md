# Client Setup Checklist

Tasks that require the client to act, or that need credentials/accounts we don't have access to. Each item notes what we need to do on our end once the client provides the details.

---

## 1. Google Analytics (GA4)

**Status:** Not started  
**Who:** Client creates account; we add the tag.

Steps:
1. Client creates a GA4 property at [analytics.google.com](https://analytics.google.com)
2. Client sends us the **Measurement ID** (format: `G-XXXXXXXXXX`)
3. We add one `<script>` tag to `components/app-nav.js` so it fires on every page:

```js
// Add inside connectedCallback(), before the closing backtick of this.innerHTML
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

Replace both instances of `G-XXXXXXXXXX` with the real Measurement ID.

---

## 2. GA4 Conversion Event — Contact Form

**Status:** Waiting on GA4 setup above  
**Who:** Client sets up in GA4 dashboard (takes 2 minutes once GA4 is live).

The contact form now redirects to `/thank-you.html` on successful submission. To track this as a conversion in GA4:

1. In GA4 go to **Configure → Events**
2. Click **Create event**
3. Name: `contact_form_submission`
4. Matching condition: `event_name` equals `page_view` AND `page_location` contains `thank-you.html`
5. Click **Save**, then mark it as a **Conversion** under Configure → Conversions

This gives the client a conversion count in GA4 showing how many enquiries the site generates each month.

---

## 3. Google Search Console

**Status:** Not started  
**Who:** Client verifies ownership; we submit the sitemap.

Steps:
1. Client goes to [search.google.com/search-console](https://search.google.com/search-console)
2. Adds property: `https://www.papervaletrees.com`
3. Verifies ownership via the **HTML tag method** — they'll get a `<meta>` tag like:
   ```html
   <meta name="google-site-verification" content="XXXXXXXXXXXX">
   ```
4. Client sends us that tag
5. We add it to `components/app-nav.js` inside `this.innerHTML` in the `<head>` equivalent area, or directly to `index.html` head (GSC only needs it on the homepage)
6. Once verified, client submits sitemap: `https://www.papervaletrees.com/sitemap.xml`

---

## 4. Google Merchant Center (Free Product Listings)

**Status:** Not started  
**Who:** Client sets up account and connects Ecwid; we add the verification tag.

Steps:
1. Client creates a Google Merchant Center account at [merchants.google.com](https://merchants.google.com)
2. Links the Ecwid store (Ecwid has a built-in Google Shopping integration under Apps → Google Shopping)
3. GMC will provide a site verification `<meta>` tag
4. Client sends us the tag
5. We add it to `components/app-nav.js` so it appears on every page

The Schema.org `Product` markup with `itemCondition`, `price`, `availability`, and `offers` is already in place on all 430 tree pages — the groundwork is done.

---

## 5. Newsletter Signup Form

**Status:** Not connected — form submits to nowhere  
**Who:** Client chooses a mailing list provider; we wire up the form.

The homepage (`index.html`) has an email signup form that currently does `onsubmit="return false"` — it collects nothing.

Options:
- **Mailchimp** — free up to 500 contacts, most popular
- **Klaviyo** — better e-commerce integration with Ecwid
- **Netlify Forms** — simplest, no third party, submissions appear in Netlify dashboard

Once the client decides, send us:
- The form `action` URL (Mailchimp/Klaviyo), or
- Confirm Netlify Forms is fine (we add `data-netlify="true"` and a honeypot)

We will also need to create a `/newsletter-thank-you.html` page for the redirect.

---

## 6. Availability List — Refresh from Ecwid API

**Status:** Done — `files/availability-list-2026.xlsx` generated (856 lines, 430+ species). `availability.html` updated.  
**Who:** We run the script periodically; client provides API token for live data.

The Excel file is now auto-generated from Ecwid product data and served directly from the repo at `/files/availability-list-2026.xlsx`. No more manual Weebly file uploads needed.

**To refresh with live stock levels:**
1. Client gets the Ecwid secret token from: https://my.ecwid.com → Settings → API
2. Run from the repo root:
   ```
   pwsh scripts/generate-availability.ps1 -EcwidToken YOUR_TOKEN_HERE
   ```
3. Commit and push `files/availability-list-2026.xlsx`

Without the token the script uses the cached `ecwid-products.json`. The heading in `availability.html` may need updating each season (currently: Spring / Summer 2026).

---

## 7. Netlify Forms — Verify Submissions Are Arriving

**Status:** Should be working — needs a test send  
**Who:** Client checks Netlify dashboard.

The contact form (`contact.html`) is wired with `data-netlify="true"` and should be storing submissions in Netlify already. Client should:

1. Log in to [app.netlify.com](https://app.netlify.com)
2. Go to the site → **Forms** tab
3. Confirm the `contact` form appears and submissions are showing

If no submissions appear, let us know and we will investigate.

---

## 8. Twitter / X — Verify Card Previews After Deployment

**Status:** Done — `twitter:card` tags added to all 13 core pages  
**Who:** Client checks after site goes live.

All core pages now have `summary_large_image` Twitter card tags matching their OG images. Once the site is deployed, verify each share looks correct using the X Card Validator:

1. Go to [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator)
2. Paste the live URL of any page (e.g. `https://www.papervaletrees.com/`)
3. Click **Preview card** — you should see the page title, description, and nursery photo

If the image doesn't appear, the image URL may not be publicly accessible yet — check that the asset is deployed alongside the HTML.

---

## 9. Ecwid — Add Product Photos for 202 Placeholder Pages

**Status:** Ongoing as photos become available  
**Who:** Client adds photos to Ecwid; we regenerate pages.

202 tree pages currently show "Photo coming soon" and are excluded from the tree catalogue. These pages are live and indexed but won't appear in the catalogue grid until they have images.

When the client adds a photo to a product in Ecwid:
1. Let us know (or batch them up and tell us periodically)
2. We will regenerate those pages with the real image and add them to `tree-catalogue.html`

The placeholder page list is at `ecwid-placeholder-ids.json` in the repo root (blocked from public access).

---

## 10. LocalBusiness Schema — Verify After Deployment

**Status:** Done — schema added to `index.html` and `contact.html`  
**Who:** We verify after deploy; client confirms social handles.

Three things to check once the site is live:

1. **Rich Results Test** — paste `https://www.papervaletrees.com/contact.html` into [search.google.com/test/rich-results](https://search.google.com/test/rich-results). Should detect a LocalBusiness entity with no errors.

2. **Geo coordinates** — the schema uses `54.1447, -6.1196` for 48 Old Newry Road. Client should verify this pin is accurate in Google Maps and let us know if it needs adjusting (edit `index.html` lines ~52–53 and the matching lines in `contact.html`).

3. **Social handles** — the `sameAs` block references `facebook.com/papervaletrees`, `instagram.com/papervaletrees`, and `x.com/papervaletrees`. Client to confirm these are the correct, active handles — or send us the correct URLs.

---

## 11. Open Graph — Facebook Sharing Debugger

**Status:** Post-deploy check  
**Who:** Client (or us) checks after site goes live.

All core pages have OG tags. Facebook caches previews aggressively — after first deploy, run the debugger to prime the cache:

1. Go to [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug)
2. Paste each key URL: homepage, shop, tree-catalogue, contact
3. Click **Scrape Again** if the preview looks stale
4. Confirm title, description, and image appear correctly

---

## 12. Core Web Vitals — PageSpeed Insights

**Status:** Post-deploy check  
**Who:** Us, after first deploy.

Once the site is live on Netlify, run PageSpeed Insights on the two most important pages:

1. Go to [pagespeed.web.dev](https://pagespeed.web.dev)
2. Test `https://www.papervaletrees.com/` (homepage with hero video)
3. Test a tree page, e.g. `https://www.papervaletrees.com/trees/quercus-robur-english-oak.html`
4. Address any red/orange issues, particularly LCP (hero image/video) and CLS

The hero video autoplay is likely the biggest performance cost on mobile — worth checking.

---

## 13. Google Business Profile

**Status:** Not started — high priority for local search  
**Who:** Client claims/creates the profile.

The LocalBusiness schema tells Google *about* the nursery. Google Business Profile (GBP) is what makes it appear in **Google Maps** and the **local pack** ("tree nurseries near me"). These are two different things and both are needed.

Steps:
1. Client goes to [business.google.com](https://business.google.com)
2. Searches for "Papervale Trees" — if it exists as an unclaimed listing, claim it; otherwise create it
3. Adds address, phone, hours, photos, and business category ("Plant nursery" or "Garden center")
4. Verifies ownership (Google sends a postcard or offers video/phone verification)

Once verified, the nursery appears on Google Maps and in local search results. Reviews collected here also count toward search ranking.

---

## 14. Trade / Wholesale Enquiry Page

**Status:** Client decision needed  
**Who:** Client confirms they want it; we build it.

Several pages (availability, CTA bands) mention trade pricing for landscape architects and grounds maintenance companies, but there's no dedicated landing page for trade customers. A `/trade.html` page could:

- Explain minimum order quantities, trade discount structure, and lead times
- Have a separate contact form pre-labelled for trade enquiries (tracked separately in GA4)
- Target keywords like "wholesale trees UK", "trade tree supplier Northern Ireland"

Client to confirm if this is something they want and provide any specific trade terms or pricing structure to include.

---

## 15. BreadcrumbList Schema on Tree Pages

**Status:** Done — all 430 tree pages already have BreadcrumbList JSON-LD.

Google can show breadcrumb trails in search results for all tree pages:

> Papervale Trees › Tree Catalogue › English Oak

No further action needed.
