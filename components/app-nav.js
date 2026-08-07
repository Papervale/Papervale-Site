class AppNav extends HTMLElement {
  connectedCallback() {
    const page = window.location.pathname.split('/').pop() || 'index.html';
    const rootsPages = ['our-roots.html', 'gallery.html', 'services-we-provide.html', 'faq.html'];

    const active = (href) => page === href ? ' active' : '';
    const rootsActive = rootsPages.includes(page) ? ' active' : '';

    this.innerHTML = `
      <nav>
        <div class="nav-inner">
          <a href="index.html" class="nav-logo">
            <img src="assets/brand/white_bk_logo.png" alt="Papervale Trees" style="height:64px; width:auto; display:block; mix-blend-mode:multiply;">
          </a>
          <div class="nav-search">
            <div id="my-search-73482057"></div>
            <div></div>
          </div>
          <ul class="nav-links">
            <li><a href="index.html"${active('index.html') ? ' class="active"' : ''}>Home</a></li>
            <li><a href="shop.html"${active('shop.html') ? ' class="active"' : ''}>Shop</a></li>
            <li><a href="tree-catalogue.html"${active('tree-catalogue.html') ? ' class="active"' : ''}>Trees</a></li>
            <li><a href="availability.html"${active('availability.html') ? ' class="active"' : ''}>Availability</a></li>
            <li class="nav-dropdown">
              <a href="our-roots.html"${rootsActive ? ' class="active"' : ''}>Our Roots</a>
              <ul class="nav-submenu">
                <li><a href="gallery.html">Life at Papervale</a></li>
                <li><a href="services-we-provide.html">Services We Provide</a></li>
                <li><a href="faq.html">FAQs</a></li>
              </ul>
            </li>
            <li><a href="grow-strong.html"${active('grow-strong.html') ? ' class="active"' : ''}>Grow Strong</a></li>
            <li><a href="contact.html" class="nav-cta${active('contact.html')}">Contact Us</a></li>
          </ul>
          <button class="nav-hamburger" id="hamburger" aria-label="Open menu">
            <span></span><span></span><span></span>
          </button>
        </div>
      </nav>
      <div class="mobile-menu" id="mobileMenu">
        <a href="index.html">Home</a>
        <a href="shop.html">Shop</a>
        <a href="tree-catalogue.html">Trees</a>
        <a href="availability.html">Availability</a>
        <div class="mobile-submenu">
          <button class="mobile-submenu-toggle">Our Roots</button>
          <div class="mobile-submenu-items">
            <a href="our-roots.html">Our Roots</a>
            <a href="gallery.html">Life at Papervale</a>
            <a href="services-we-provide.html">Services We Provide</a>
            <a href="faq.html">FAQs</a>
          </div>
        </div>
        <a href="grow-strong.html">Grow Strong</a>
        <a href="contact.html" class="mob-cta">Contact Us</a>
      </div>
    `;

    // Scripts in innerHTML don't execute — load search widget programmatically
    const clearSearchPlaceholder = () => {
      const container = document.getElementById('my-search-73482057');
      if (!container) return false;
      // try to find an input element inside the widget and clear its placeholder/value
      const input = container.querySelector('input, input[type="search"], input[type="text"]');
      if (input) {
        try { input.placeholder = ''; } catch (e) {}
        try { input.value = ''; } catch (e) {}
        try { input.removeAttribute('aria-label'); } catch (e) {}
        return true;
      }
      return false;
    };

    // Use a MutationObserver to catch when the widget renders asynchronously
    const observeAndClear = () => {
      const container = document.getElementById('my-search-73482057');
      if (!container) return;
      if (clearSearchPlaceholder()) return;
      const obs = new MutationObserver(() => {
        if (clearSearchPlaceholder()) obs.disconnect();
      });
      obs.observe(container, { childList: true, subtree: true, attributes: true });
      // safety: stop observing after 10s
      setTimeout(() => obs.disconnect(), 10000);
    };

    const tryClearWithRetry = (attempts = 20, delay = 300) => {
      let tries = 0;
      const t = setInterval(() => {
        if (clearSearchPlaceholder() || ++tries >= attempts) clearInterval(t);
      }, delay);
      observeAndClear();
    };

    if (!document.querySelector('script[src*="business.shop"]')) {
      const s = document.createElement('script');
      s.setAttribute('data-cfasync', 'false');
      s.charset = 'utf-8';
      s.src = 'https://app.business.shop/script.js?73482057&data_platform=code&data_date=2026-05-04';
      s.onload = () => {
        if (typeof xSearch === 'function') xSearch('id=my-search-73482057');
        // widget may render asynchronously — attempt to clear placeholder
        tryClearWithRetry();
      };
      document.head.appendChild(s);
    } else if (typeof xSearch === 'function') {
      xSearch('id=my-search-73482057');
      tryClearWithRetry();
    }
  }
}

customElements.define('app-nav', AppNav);
