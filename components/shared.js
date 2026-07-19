// Mobile hamburger menu
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('open');
  mobileMenu.classList.toggle('open');
});

// Close menu when a link is clicked
mobileMenu.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('open');
    mobileMenu.classList.remove('open');
  });
});

// Handle mobile submenu toggle
const mobileSubmenus = mobileMenu.querySelectorAll('.mobile-submenu-toggle');
mobileSubmenus.forEach(toggle => {
  toggle.addEventListener('click', (e) => {
    e.preventDefault();
    const submenu = toggle.parentElement;
    submenu.classList.toggle('open');
  });
});

// Lightbox functionality for guide images
const lightbox = document.getElementById('lightbox');
const lightboxImg = document.getElementById('lightboxImg');
const lightboxClose = document.getElementById('lightboxClose');

if (lightbox) {
  // Double-click on guide images to open lightbox
  document.querySelectorAll('.guide-img img').forEach(img => {
    img.addEventListener('dblclick', () => {
      lightboxImg.src = img.src;
      lightboxImg.alt = img.alt;
      lightbox.classList.add('open');
    });
  });

  // Close lightbox
  lightboxClose.addEventListener('click', () => {
    lightbox.classList.remove('open');
  });

  lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
      lightbox.classList.remove('open');
    }
  });
}

// Inject a site-wide Google Merchant ID meta tag so the Merchant ID
// is present on every page. This does not replace Merchant Center
// verification or feeds — see docs/ECWID.md and docs/DEPLOYMENT.md for next steps.
(function() {
  try {
    const MERCHANT_ID = '5694263882';
    if (typeof document !== 'undefined' && document.head) {
      if (!document.head.querySelector('meta[name="google-merchant-id"]')) {
        const m = document.createElement('meta');
        m.setAttribute('name', 'google-merchant-id');
        m.setAttribute('content', MERCHANT_ID);
        document.head.appendChild(m);
      }
      // helpful HTML comment for humans inspecting the source
      const commentText = ` Google Merchant ID: ${MERCHANT_ID} `;
      const existing = Array.from(document.head.childNodes).some(n => n.nodeType === Node.COMMENT_NODE && n.nodeValue && n.nodeValue.includes('Google Merchant ID'));
      if (!existing) document.head.appendChild(document.createComment(commentText));
    }
  } catch (err) {
    // fail silently; this script runs in many static pages
    console.error('Merchant ID injection failed', err);
  }
})();
