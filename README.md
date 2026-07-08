# Old Town Atelier Parfums — frontend-uudistus

Porvoolaisen niche-parfyymitalon (`oldtownparfums.com`) verkkosivun
uudelleenrakennus kevyeksi, nopeaksi ja tyylikkääksi. Nykyinen sivu on raskas
WordPress + Elementor + WooCommerce -toteutus; uusi rakennetaan Lovablella
(React + Tailwind, staattinen).

## Tila

| Vaihe | Tila |
|---|---|
| Rakenne- ja suorituskykyanalyysi | ✅ valmis → `docs/ANALYSIS.md` |
| Kaiken sisällön keruu (EN + FI, sanatarkka) | ✅ valmis → `docs/CONTENT.md` |
| Kuvien lataus + optimointi (~10 Mt → ~1,1 Mt) | ✅ valmis → `assets/images/` |
| Lovable-projekti luotu + kuvat ladattu | ✅ "Atelier Brilliance" |
| Sivun generointi Lovablella | ✅ **valmis (kaikki 8 sivua)** |
| Kaksikielisyys (EN oletus + FI-vaihto) | ✅ toimii (`src/lib/i18n.tsx`) |
| Demo | ✅ rakennettu (julkaisu otettu alas — yksityinen) |
| Verkkokauppa | ⏳ myöhempi vaihe (asiakkaan pyyntö) |

## 🔗 Demo (yksityinen)

Julkinen `.lovable.app`-julkaisu on otettu alas. Demoa pääsee katsomaan vain
Lovable-työtilan jäsenet:

- **Esikatselu (vaatii kirjautumisen):** https://id-preview--87a43982-089c-423a-b71b-ae41f8fed900.lovable.app
- **Lovable-editori:** https://lovable.dev/projects/87a43982-089c-423a-b71b-ae41f8fed900

Voi julkaista uudelleen milloin vain (Lovable → Publish).

Rakennettu 2026-07-08, ~2,1 Lovable-krediittiä. Kaikki tekstit sanatarkkoja
(EN + FI), oikeat optimoidut kuvat, tyyli ja tunnelma säilytetty.

## Hakemistot

- `docs/ANALYSIS.md` — miksi nykyinen sivu on raskas + sivukartta
- `docs/CONTENT.md` — kaikki tekstit sanatarkasti (EN + FI), hinnat, yhteystiedot
- `docs/LOVABLE-BUILD-PROMPT.md` — valmis build-prompt Lovablelle
- `assets/images/` — optimoidut kuvat (logo, hero, 3 tuoksua, perustaja)
