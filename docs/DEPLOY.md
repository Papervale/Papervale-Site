# Deployment Guide — Netlify

Hosting: [Netlify](https://netlify.com)  
Method: Drag-and-drop or GitHub auto-deploy  
Current live site: https://www.papervaletrees.com (Weebly — being replaced)

---

## Why Netlify

- Free tier is more than sufficient for this site
- Drag-and-drop deploy — no command line needed
- Free SSL certificate (HTTPS) included automatically
- Handles contact form submissions natively (no backend needed)
- Custom domain connection is straightforward
- If using GitHub: push a change → site updates automatically within seconds

---

## Option A — Drag and Drop (Simplest)

1. Go to https://netlify.com and sign up for a free account
2. From the dashboard click **"Add new site → Deploy manually"**
3. Drag your entire `papervale-site` folder onto the upload area
   - **Important:** Include the `components/` directory (contains required web components like `ukisg-banner.js`)
4. Netlify gives you a random URL like `https://random-name-123.netlify.app`
5. Test everything works on that URL before switching your domain

**To update the site:** drag the folder again. Netlify replaces the previous version.

---

## Option B — GitHub Auto-Deploy (Recommended)

### One-time setup

1. Create a free account at https://github.com
2. Create a new repository called `papervale-site` (can be private)
3. Upload your project files to the repository
4. Go to https://netlify.com → **"Add new site → Import from Git"**
5. Connect your GitHub account and select the `papervale-site` repository
6. Leave build settings blank (no build command needed for plain HTML)
7. Click **Deploy site**

### After setup

Every time you push a change to GitHub, Netlify redeploys automatically within ~30 seconds. No manual uploading needed.

---

## Connecting Your Domain

Once the site is working on the Netlify URL:

1. In Netlify: **Site settings → Domain management → Add custom domain**
2. Enter `papervaletrees.com`
3. Netlify shows you DNS records to add

### DNS Changes (do this at your domain registrar)

You need to update two DNS records wherever your domain is registered:

```
Type: A
Name: @
Value: 75.2.60.5

Type: CNAME
Name: www
Value: [your-site-name].netlify.app
```

DNS changes can take up to 48 hours to propagate worldwide.

> ⚠️ **Important:** Change your DNS *after* you are happy the new site is working on the Netlify URL. Once DNS is pointed at Netlify, the Weebly site is no longer live.

---

## Contact Form Setup (Netlify Forms)

The contact form on `contact.html` currently has a JavaScript placeholder. To make it work with Netlify's built-in form handling:

### 1. Add the `netlify` attribute to the form tag

```html
<!-- Change this: -->
<form onsubmit="handleSubmit(event)">

<!-- To this: -->
<form name="contact" method="POST" netlify netlify-honeypot="bot-field">
  <input type="hidden" name="form-name" value="contact">
  <!-- hidden spam trap -->
  <p style="display:none">
    <label>Don't fill this out: <input name="bot-field"></label>
  </p>
  <!-- rest of form fields stay the same -->
```

### 2. Remove the JavaScript `handleSubmit` function

### 3. Add a thank-you page (optional)

Create `thank-you.html` and add to the form:
```html
<form ... action="/thank-you.html">
```

### 4. Set up email notifications

In Netlify dashboard: **Forms → contact → Form notifications → Add notification → Email**

Submissions go directly to your email inbox.

---

## Environment Notes

| Item | Current | Target |
|------|---------|--------|
| Domain registrar | *(check with Jonathan)* | Keep same registrar, update DNS |
| Email hosting | *(check — likely separate from Weebly)* | Unaffected by move |
| Hero video | Weebly CDN | Move to `assets/video/` or use Vimeo/YouTube embed |
| Availability PDFs | Weebly uploads | Move to `assets/docs/` |
| Shop | Ecwid (stays) | Stays — just re-embed the widget |

---

## Pre-Launch Checklist

- [ ] All pages tested on desktop Chrome, Safari, Firefox
- [ ] All pages tested on iOS Safari and Android Chrome
- [ ] All internal links work correctly
- [ ] Contact form tested and submits to correct email
- [ ] Shop embed loads correctly (test with real Ecwid store ID)
- [ ] All images load (check browser console for 404 errors)
- [ ] Hero video loads and autoplays on mobile
- [ ] Availability PDF links work
- [ ] Custom domain connected and HTTPS shows green padlock
- [ ] Old Weebly site confirmed offline (or redirected)
- [ ] Google Search Console updated with new sitemap
