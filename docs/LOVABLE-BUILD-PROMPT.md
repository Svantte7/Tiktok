# Lovable build prompt (valmis ajettavaksi)

Kun Lovable-työtilaan on lisätty krediittejä, tämä on lähetettävä viesti
Lovable-projektiin. Kaikki sanatarkat tekstit ovat tiedostossa `CONTENT.md`.

**Lovable-projekti:** "Atelier Brilliance"
`https://lovable.dev/projects/87a43982-089c-423a-b71b-ae41f8fed900`
(6 kuvaa on jo ladattu projektiin; ne löytyvät myös `assets/images/`-kansiosta.)

---

## Viesti Lovable-agentille

Build the full Old Town Atelier Parfums site (currently only a blank placeholder
exists). Lightweight, fast, elegant static marketing site for a niche luxury
perfume house — small-batch atelier in Porvoo Old Town, Finland. No backend/DB/
auth. Save the 6 attached images into `src/assets` and import them (no external
URLs, no stock photos). Use the EXACT copy from CONTENT.md — do not invent,
translate, or paraphrase.

**Bilingual:** English (default) + Finnish, with an EN/FI toggle in the header
that persists in localStorage and switches all nav, buttons, headings and body.
Founder's Story is English-only for now (use EN for both languages).

**Style/mood (preserve exactly):** quiet timeless luxury; warm, moody,
artisanal. Cream/ivory background (~#fcfbf8), deep charcoal text, warm amber/
muted gold accents. Refined serif headings (Cormorant / EB Garamond), clean
sans-serif body. Generous whitespace, hairline dividers, small flourishes
echoing the logo. Editorial, gallery-like — not flashy, not colorful.

**Nav (EN/FI):** Home/Etusivu · Fragrances/Tuoksut · Shop/Kauppa ·
House Manifesto/Talon manifesti · Founder's Story/Perustajan tarina ·
Contact/Yhteystiedot. Sticky minimal header w/ logo + mobile hamburger.
Footer: "© 2026 Old Town Atelier Parfums. Crafted in Porvoo, Finland."
(FI: "…Valmistettu Porvoossa, Suomessa.")

**Routes:**
- `/` Home — full-bleed hero (hero-trio.jpg, soft dark overlay), centered
  logo + tagline; then a short manifesto intro line, three fragrance preview
  cards, and a quiet CTA to House Manifesto / Contact.
- `/fragrances` — three fragrances as editorial image+text blocks, each linking
  to its page.
- `/fragrances/jasmin-obscure` — jasmin-obscure.jpg + copy & notes.
- `/fragrances/oud-nocturne` — oud-nocturne.jpg + copy & notes.
- `/fragrances/velvet-carnival` — velvet-carnival.jpg + copy & notes.
- `/house-manifesto` — manifesto (EN/FI).
- `/founders-story` — founder.jpg portrait + story.
- `/shop` — NOT a working webshop yet (no cart/checkout/payment; real store
  comes later — leave clean structure). Three fragrances w/ images, sizes &
  prices (50 ml €147,00 / 30 ml €92,00 / 10 ml €32,00), the availability &
  orders text, "Finland: Free shipping on orders over €120,00", order emails,
  and an "Enquire / Order by email" button → mailto:contact@oldtownparfums.com.
- `/contact` — email + WhatsApp (+358 50 5444 847 → https://wa.me/358505444847)
  + Porvoo location.

All exact text (EN + FI), notes, prices, contact details and image mapping are
in `CONTENT.md` in this repo.

---

## Verkkokauppa — myöhempi vaihe (EI nyt)

Asiakkaalla on tarve toimivalle verkkokaupalle verkkosivujen sisään. Tämä
tehdään myöhemmin. Nykyinen `/shop` on vain hinnasto + sähköpostitiedustelu.
Toteutusvaihtoehdot kaupalle myöhemmin:
- Lovablen Stripe-integraatio (ostoskori + kassa) tai
- WooCommerce/Shopify-upotus.
Rakenne on jätetty valmiiksi laajennettavaksi.
