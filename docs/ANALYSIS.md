# oldtownparfums.com — rakenne- ja suorituskykyanalyysi

Analysoitu 2026-07-08 (`https://www.oldtownparfums.com/`).

## Miksi nykyinen sivu on raskas

**Alusta: WordPress 7.0 + Elementor-sivunrakentaja + WooCommerce 10.9.3.**
Tämä on pääsyy raskauteen. Elementor ja WooCommerce lataavat suuren määrän
geneeristä CSS/JS:ää jokaisella sivunlatauksella riippumatta siitä,
käytetäänkö niitä kyseisellä sivulla.

Mitattua (etusivu, jossa on vain logo, navigaatio, yksi otsikko ja footer):

| Mittari | Arvo |
|---|---|
| Alusta | WordPress 7.0 + Elementor + WooCommerce 10.9.3 |
| Erilliset CSS-tiedostot | 9 |
| Erilliset JS-tiedostot | 13 |
| Inline `<style>`-lohkot | 11 |
| HTML-dokumentin koko | ~82 kt (pelkkä runko, ennen kuvia) |
| Latautuvat liitännäiset etusivulla | WooCommerce, WooPayments, Snapchat-for-WooCommerce, Reddit-for-WooCommerce |
| Tuotekuvat | ~2 Mt/kpl käsittelemättömiä PNG-tiedostoja (yht. ~10 Mt optimoimattomana) |

Yhteenveto: **sisältö on kevyt, mutta alusta on raskas.** Koko WooCommerce-
kauppakoodi ja markkinointiliitännäiset (Snapchat/Reddit-pikselit) latautuvat
jo etusivulla, vaikka mitään tuotetta ei näytetä. Optimoimattomat 2 Mt:n PNG-
tuotekuvat kasvattavat sivupainoa kymmenkertaisesti.

**Ratkaisu:** uudelleenrakennus kevyellä React + Tailwind -staattissivustolla
(Lovable) poistaa Elementorin/WooCommercen turhat resurssit ja optimoidut
kuvat pudottavat kuvapainon ~10 Mt → ~1,1 Mt.

## Sivukartta (WordPress REST API `/wp-json/wp/v2/pages`)

Sisältösivut:
- `home` (272) — "Fragrance as identity, Perfume as presence"
- `fragrances` (315)
- `jasmin-obscure` (319)
- `oud-nocturne` (321)
- `velvet-carnival` (323)
- `house-manifesto-2` (260) — "House Manifesto"
- `founders-story` (257)
- `contact` (259)
- `shop` (347) — hinnat + tiedustelutilaus

Verkkokauppasivut (WooCommerce — "verkkokauppa myöhemmin"):
- `kauppa` (377), `ostoskori` (378), `kassa` (379), `oma-tili` (380)

## Kieli

Sivu on kaksikielinen: **englanti + suomi.** Navigaatio on englanniksi;
House Manifesto ja kaikki tuoksukuvaukset ovat sekä englanniksi että suomeksi.
Founder's Story on vain englanniksi.

Uudelleenrakennuksen valinta (asiakkaan vahvistama): **kaksikielinen,
englanti oletuksena + suomivaihto (EN/FI-valitsin).**
