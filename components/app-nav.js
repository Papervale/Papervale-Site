class AppNav extends HTMLElement {
  connectedCallback() {
    const page = window.location.pathname.split('/').pop() || 'index.html';
    const rootsPages = ['our-roots.html', 'gallery.html', 'services-we-provide.html'];

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
          </div>
        </div>
        <a href="grow-strong.html">Grow Strong</a>
        <a href="contact.html" class="mob-cta">Contact Us</a>
      </div>
    `;

    // Scripts in innerHTML don't execute — load search widget programmatically
    if (!document.querySelector('script[src*="business.shop"]')) {
      const s = document.createElement('script');
      s.setAttribute('data-cfasync', 'false');
      s.charset = 'utf-8';
      s.src = 'https://app.business.shop/script.js?73482057&data_platform=code&data_date=2026-05-04';
      s.onload = () => { if (typeof xSearch === 'function') xSearch('id=my-search-73482057'); };
      document.head.appendChild(s);
    } else if (typeof xSearch === 'function') {
      xSearch('id=my-search-73482057');
    }
  }
}

customElements.define('app-nav', AppNav);
