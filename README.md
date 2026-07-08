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
| Sivun generointi Lovablella | ⛔ **estetty: työtila ilman krediittejä** |
| Kaksikielisyys (EN oletus + FI-vaihto) | määritelty, odottaa buildia |
| Verkkokauppa | ⏳ myöhempi vaihe (asiakkaan pyyntö) |

## ⛔ Seuraava askel — vaatii sinua

Lovable-työtilasta ("Jesse's Lovable", free-plan) **loppuivat krediitit**,
joten agentti ei voi generoida sivua. Kun olet lisännyt krediittejä
(`https://lovable.dev/settings/billing`), sivu rakentuu yhdellä viestillä:
lähetä `docs/LOVABLE-BUILD-PROMPT.md`:n viesti projektiin
**"Atelier Brilliance"** (`lovable.dev/projects/87a43982-089c-423a-b71b-ae41f8fed900`).
Kaikki tekstit, kuvat ja tyyliohjeet ovat valmiina tässä repossa.

## Hakemistot

- `docs/ANALYSIS.md` — miksi nykyinen sivu on raskas + sivukartta
- `docs/CONTENT.md` — kaikki tekstit sanatarkasti (EN + FI), hinnat, yhteystiedot
- `docs/LOVABLE-BUILD-PROMPT.md` — valmis build-prompt Lovablelle
- `assets/images/` — optimoidut kuvat (logo, hero, 3 tuoksua, perustaja)
