# pakuavuksi.fi

Tmi Jarno ja pakuavuksi -yrityksen verkkosivusto. Staattinen, monisivuinen ja
hakukoneoptimoitu sivusto ilman ulkoisia riippuvuuksia — ei verkkofontteja,
ei seurantaskriptejä, ei JavaScript-kehyksiä.

## Sivut

| Osoite | Sisältö |
|---|---|
| `/` | Etusivu: palvelut, toimintatapa, toiminta-alue |
| `/palvelut/` | Palvelujen kooste |
| `/palvelut/muutto-ja-kuljetuspalvelut/` | Muutot, kuolinpesät, tavarakuljetukset |
| `/palvelut/mokkitalkkari-palvelut/` | Pihatyöt, nurmikko, lumityöt |
| `/palvelut/metsuripalvelut/` | Puiden kaato, karsiminen, polttopuut |
| `/palvelut/apuvirta-paivysty-renkaiden-vaihto/` | Apuvirta 24/7, renkaanvaihto |
| `/hinnasto/` | Kaikki hinnat yhdellä sivulla |
| `/toiminta-alue/` | Vakioreitit ja alueet |
| `/toiminta-alue/savitaipale/` | Paikallissivu |
| `/toiminta-alue/lappeenranta/` | Paikallissivu |
| `/toiminta-alue/kouvola/` | Paikallissivu |
| `/toiminta-alue/helsinki/` | Paikallissivu |
| `/usein-kysytyt-kysymykset/` | UKK (FAQ-rakennedata) |
| `/tietoa-meista/` | Yritysesittely |
| `/yhteystiedot/` | Yhteystiedot ja lomake |
| `/tietosuoja/` | Tietosuojaseloste |
| `404.html` | Virhesivu |

Vanhan sivuston osoitteet (`/palvelut/...`, `/tietoa-meista`, `/yhteystiedot`)
on säilytetty sellaisinaan, jotta hakukonenäkyvyys ei katoa uudistuksessa.

## Hakukoneoptimointi

- Jokaisella sivulla oma `<title>` (enintään 65 merkkiä) ja meta-kuvaus (120–175 merkkiä)
- Kanoniset osoitteet, Open Graph- ja Twitter-kortit
- JSON-LD-rakennedata: `LocalBusiness`, `Service` + `OfferCatalog` hinnoilla,
  `FAQPage`, `BreadcrumbList`, `ContactPage`
- `sitemap.xml` ja `robots.txt` luodaan automaattisesti
- Semanttinen HTML, yksi `<h1>` sivua kohti, murupolut
- Ei render-estäviä ulkoisia resursseja

## Logo

Logo on eurooppalainen pakettiauto sivuprofiilina ja nimi pienenä kursiivina
aivan sen perässä. Teksti on muunnettu poluiksi (Liberation Sans Bold Italic,
metrisesti sama kuin Arial Bold Italic), joten logo näyttää samalta joka
koneella ja painossa — fonttia ei tarvitse asentaa.

| Tiedosto | Käyttö |
|---|---|
| `assets/img/logo-dark.svg` | Tummalle pohjalle — sivuston ylä- ja alapalkki |
| `assets/img/logo.svg` | Vaalealle pohjalle — asiakirjat, valkoinen tausta |
| `assets/img/logo-mono.svg` | Yksivärinen tummalle tekstille — leimat, laskut |
| `assets/img/logo-mono-light.svg` | Yksivärinen vaalealle — tumma tausta |
| `assets/img/favicon.svg` | Selaimen välilehti |
| `assets/img/apple-touch-icon.png` | iOS-kotinäytön kuvake (180 × 180) |
| `assets/img/og-image.png` | Jakokuva somelinkkeihin (1200 × 630) |

Logot luodaan `logo_build.py`-skriptillä:

```bash
python3 logo_build.py
```

Skripti ei tarvitse ulkoisia kirjastoja: korin muoto ja kirjainten polut ovat
tiedostossa valmiina. `apple-touch-icon.png` ja `og-image.png` on renderöity
kertaalleen selaimella SVG:istä, eikä niitä tarvitse luoda uudelleen ellei
logo muutu.

**Pienin suositeltu koko** on noin 160 pikseliä leveä. Sitä pienempänä nimen
kursiivi käy vaikealukuiseksi — käytä silloin pelkkää `favicon.svg`-merkkiä.
Auton kylkiteippaukseen kannattaa suurentaa nimeä erikseen suhteessa pakuun.

## Kehittäminen

Sivut luodaan `build.py`-skriptillä, jotta navigaatio, alatunniste ja
rakennedata pysyvät identtisinä kaikilla sivuilla.

```bash
python3 build.py                 # luo HTML-tiedostot, sitemap.xml ja robots.txt
python3 -m http.server 8000      # esikatselu osoitteessa http://localhost:8000
```

- `build.py` — sivupohja, navigaatio, rakennedata, yrityksen tiedot (`SITE`)
- `content.py` — kaikkien sivujen tekstit ja hinnat
- `assets/css/style.css` — tyylit
- `assets/js/main.js` — mobiilivalikko ja lomakkeen käsittely
- `logo_build.py` — logotiedostot
- `preview_build.py` — yhden tiedoston esikatselu jaettavaksi

Valmiit HTML-tiedostot on versioitu repoon, joten sivuston voi julkaista
sellaisenaan ilman Pythonia.

**Hintojen tai tekstien muuttaminen:** muokkaa `content.py`-tiedostoa ja aja
`python3 build.py`. Yhteystiedot ja Y-tunnus muutetaan `build.py`-tiedoston
`SITE`-sanakirjasta yhdestä paikasta.

## Julkaisu

Sivusto on tavallinen staattinen sivusto. Se toimii esimerkiksi Netlifyssä,
GitHub Pagesissa tai perinteisellä webhotellilla: siirrä repon sisältö
palvelimen juureen.

Aseta palvelin näyttämään `404.html` virhesivuna. Netlifyssä tämä toimii
automaattisesti; Apachella lisää `.htaccess`-tiedostoon:

```
ErrorDocument 404 /404.html
```

## Yhteydenottolomake

Staattinen sivusto ei voi itse lähettää sähköpostia, joten lomake tarvitsee
välityspalvelun. Toistaiseksi lomake **ei lähetä viestejä** vaan ohjaa
kävijän puhelimeen ja sähköpostiin — se ei siis katoa hiljaisesti kuten
vanhalla sivustolla.

Käyttöönotto:

1. Luo tili osoitteessa [formspree.io](https://formspree.io) ja ota lomakkeen
   osoite talteen.
2. Korvaa `content.py`-tiedostossa merkkijono `LISAA-LOMAKKEEN-OSOITE`
   omalla lomaketunnuksellasi.
3. Aja `python3 build.py`.

Vaihtoehtoisesti Netlify Forms: lisää `<form>`-elementtiin attribuutti
`data-netlify="true"` ja poista `action`-attribuutti.

Jos otat lomakepalvelun käyttöön, lisää sen nimi myös tietosuojaselosteeseen
(`content.py`, kohta Tietosuoja).

## Vielä tehtävää

- **Yritysesittely.** Sivulla `/tietoa-meista/` on kohta, johon kannattaa
  lisätä muutama lause omin sanoin. Kohta on merkitty HTML-kommentilla
  `content.py`-tiedostossa. Vanhan sivuston paikkamerkkitekstit
  ("Tähän esittely teksti") on poistettu.
- **Valokuvat.** Sivusto toimii ilman kuvia, mutta oikeat kuvat pakusta,
  työkohteista ja tekijästä parantaisivat luotettavuutta selvästi. Lisää
  kuvat hakemistoon `assets/img/` ja muista `alt`-tekstit.
- **Google Business -profiili.** Paikallishauissa tämä vaikuttaa usein
  enemmän kuin itse sivusto. Kannattaa luoda ja yhdistää sivustoon.
- **Sivukartan lähetys.** Lisää sivusto Google Search Consoleen ja lähetä
  `https://pakuavuksi.fi/sitemap.xml`.
