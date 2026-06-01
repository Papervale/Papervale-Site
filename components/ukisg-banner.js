class UkisgBanner extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          background: #334832;
          color: rgba(255,255,255,0.9);
          text-align: center;
          padding: 14px 32px;
          gap: 2px;
        }

        .headline {
          font-size: 13px;
          font-weight: 600;
        }

        .subline {
          font-size: 11px;
          font-weight: 400;
          color: rgba(255,255,255,0.65);
          letter-spacing: 0.3px;
        }

        strong { color: #a8bf9e; }

        @media (min-width: 769px) {
          :host {
            flex-direction: row;
            gap: 10px;
            padding: 14px 32px;
          }

          .subline {
            font-size: 13px;
            font-weight: 500;
            color: rgba(255,255,255,0.9);
          }

          .sep { display: inline; }
        }

        @media (max-width: 768px) {
          :host { padding: 10px 20px; }
        }
      </style>
      <span class="headline">🌿 Northern Ireland's first <strong>UKISG Certified</strong> tree nursery</span>
      <span class="subline">genuinely homegrown | fully traceable</span>
    `;
  }
}

customElements.define('ukisg-banner', UkisgBanner);
