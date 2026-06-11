class AppFooter extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          --surface-soft: #f8f7f5;
          --hairline: #e8e6e4;
          --ink: #1a1a1a;
          --muted: #7a7a7a;
          --muted-soft: #a0a0a0;
          --sp-xl: 32px;
          --sp-lg: 24px;
          --sp-md: 16px;
          --sp-sm: 12px;
          --radius-md: 8px;
        }

        footer {
          background: var(--surface-soft);
          border-top: 1px solid var(--hairline);
          padding: 64px 0 40px;
        }

        .footer-inner {
          max-width: 1240px;
          margin: 0 auto;
          padding: 0 var(--sp-xl);
        }

        .footer-grid {
          display: grid;
          grid-template-columns: 2fr 1fr 1fr 1fr;
          gap: 48px;
          padding-bottom: 48px;
          border-bottom: 1px solid var(--hairline);
          margin-bottom: 32px;
        }

        .footer-brand p {
          font-size: 14px;
          color: var(--muted);
          line-height: 1.6;
          margin-top: var(--sp-md);
          max-width: 280px;
          margin-bottom: 0;
        }

        .footer-col h4 {
          font-size: 13px;
          font-weight: 600;
          color: var(--ink);
          margin-bottom: var(--sp-md);
          letter-spacing: 0.5px;
          margin-top: 0;
        }

        .footer-col ul {
          list-style: none;
          display: flex;
          flex-direction: column;
          gap: 10px;
          padding: 0;
          margin: 0;
        }

        .footer-col a {
          text-decoration: none;
          font-size: 14px;
          color: var(--muted);
          transition: color 0.2s;
        }

        .footer-col a:hover {
          color: var(--ink);
        }

        .footer-bottom {
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-size: 13px;
          color: var(--muted-soft);
        }

        .certifications {
          display: flex;
          gap: var(--sp-sm);
          align-items: center;
          flex-wrap: wrap;
          margin-top: 16px;
          margin-bottom: 0;
        }

        .cert-badge {
          display: inline-block;
          padding: 4px 8px;
          background: rgba(51, 72, 50, 0.08);
          border-radius: 4px;
          font-size: 12px;
          color: var(--ink);
          font-weight: 500;
        }

        .social-links {
          display: flex;
          gap: var(--sp-sm);
          margin-top: var(--sp-lg);
          margin-bottom: 0;
        }

        .social-links a {
          display: inline-flex;
          align-items: center;
          justify-content: center;
          width: 38px;
          height: 38px;
          border-radius: var(--radius-md);
          text-decoration: none;
          transition: opacity 0.2s, transform 0.2s;
          flex-shrink: 0;
        }

        .social-links a:hover {
          opacity: 0.85;
          transform: translateY(-2px);
        }

        .social-links a svg {
          display: block;
        }

        .social-link-fb {
          background: #1877F2;
        }

        .social-link-ig {
          background: linear-gradient(
            45deg,
            #f09433 0%, #e6683c 25%,
            #dc2743 50%, #cc2366 75%,
            #bc1888 100%
          );
        }

        .opening-hours {
          margin-top: 16px;
          font-size: 13px;
          color: var(--muted);
        }

        .opening-hours strong {
          color: var(--ink);
          font-size: 12px;
          display: block;
          margin-bottom: 4px;
        }

        .nav-logo {
          display: inline-flex;
          margin-bottom: 4px;
        }

        .nav-logo img {
          height: 64px;
          width: auto;
          display: block;
          mix-blend-mode: multiply;
        }

        @media (max-width: 768px) {
          footer {
            padding: 40px 0 24px;
          }

          .footer-inner {
            padding: 0 var(--sp-lg);
          }

          .footer-grid {
            grid-template-columns: 1fr;
            gap: 28px;
          }

          .footer-bottom {
            flex-direction: column;
            gap: 8px;
            text-align: center;
          }

          .certifications {
            flex-wrap: wrap;
          }
        }
      </style>

      <footer>
        <div class="footer-inner">
          <div class="footer-grid">
            <div class="footer-brand">
              <a href="index.html" class="nav-logo">
                <img src="assets/brand/white_bk_logo.png" alt="Papervale Trees">
              </a>
              <p>Northern Ireland's specialist home-grown tree nursery, supplying over 300 varieties across the UK and Ireland since 2015.</p>
              <div class="certifications">
                <span class="cert-badge">UKISG Certified</span>
                <span class="cert-badge">BS8545</span>
                <span class="cert-badge">Peat-Free</span>
              </div>
              <div class="social-links">
                <a href="https://facebook.com/papervaletrees" target="_blank" rel="noopener noreferrer" class="social-link-fb" aria-label="Facebook">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="#ffffff"><path d="M24 12.073C24 5.405 18.627 0 12 0S0 5.405 0 12.073C0 18.1 4.388 23.094 10.125 24v-8.437H7.078v-3.49h3.047V9.41c0-3.025 1.792-4.697 4.533-4.697 1.312 0 2.686.236 2.686.236v2.97h-1.513c-1.491 0-1.956.93-1.956 1.886v2.267h3.328l-.532 3.49h-2.796V24C19.612 23.094 24 18.1 24 12.073z"/></svg>
                </a>
                <a href="https://instagram.com/papervaletrees" target="_blank" rel="noopener noreferrer" class="social-link-ig" aria-label="Instagram">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="#ffffff"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
                </a>
              </div>
            </div>
            <div class="footer-col">
              <h4>Explore</h4>
              <ul>
                <li><a href="shop.html">Shop Trees</a></li>
                <li><a href="availability.html">Availability List</a></li>
                <li><a href="our-roots.html">Our Roots</a></li>
                <li><a href="grow-strong.html">Grow Strong</a></li>
              </ul>
            </div>
            <div class="footer-col">
              <h4>Guidance</h4>
              <ul>
                <li><a href="how-we-grow-our-trees.html">How We Grow</a></li>
                <li><a href="selecting-a-tree.html">Selecting a Tree</a></li>
                <li><a href="planting-aftercare.html">Aftercare Guide</a></li>
                <li><a href="services-we-provide.html">Services Provided</a></li>
                <li><a href="faq.html">FAQs</a></li>
              </ul>
            </div>
            <div class="footer-col">
              <h4>Location &amp; Contact</h4>
              <ul>
                <li><a href="https://maps.google.com/?q=Papervale+Trees+Old+Newry+Road+Rathfriland" target="_blank">48 Old Newry Road<br>Rathfriland, Co. Down<br>BT34 5BQ</a></li>
                <li><a href="tel:02830850059">028 3085 0059</a></li>
                <li><a href="contact.html">Contact Form</a></li>
              </ul>
              <div class="opening-hours">
                <strong>Opening Hours</strong>
                Mon–Fri: By Appointment<br>
                Sat: 10am – 2pm &nbsp;|&nbsp; Sun: Closed
              </div>
            </div>
          </div>
          <div class="footer-bottom">
            <span>© 2026 Papervale Trees. All rights reserved.</span>
            <span>Grown with care in Northern Ireland 🌿</span>
          </div>
        </div>
      </footer>
    `;
  }
}

customElements.define('app-footer', AppFooter);
