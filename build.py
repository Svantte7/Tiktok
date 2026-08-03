#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rakentaa pakuavuksi.fi-sivuston staattiset HTML-tiedostot.

Käyttö:  python3 build.py
Esikatselu:  python3 -m http.server 8000  ->  http://localhost:8000

Valmiit HTML-tiedostot on versioitu repoon, joten sivuston voi julkaista
sellaisenaan ilman tätä skriptiä. Skripti on olemassa siksi, että navigaatio,
alatunniste ja rakenteinen data pysyvät identtisinä kaikilla sivuilla.
"""

import json
import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Yrityksen tiedot (yhdestä paikasta koko sivustolle)
# --------------------------------------------------------------------------

SITE = {
    "name": "Tmi Jarno ja pakuavuksi",
    "short": "Pakuavuksi",
    "base": "https://pakuavuksi.fi",
    "phone_display": "045 633 4700",
    "phone_link": "+358456334700",
    "email": "pakuavuksi@hotmail.com",
    "whatsapp": "https://wa.me/358456334700",
    "street": "Ojastintie 17",
    "zip": "54800",
    "city": "Savitaipale",
    "ytunnus": "3593123-5",
    "vat": "25,5",
    "year": "2026",
}

CONTACT_LINE = f'{SITE["street"]}, {SITE["zip"]} {SITE["city"]}'

# --------------------------------------------------------------------------
# Ikonit (inline-SVG, ei ulkoisia tiedostoja)
# --------------------------------------------------------------------------

ICONS = {
    "van": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M3 32V13h24v19"/><path d="M27 19h8l10 8v5h-6"/>'
           '<path d="M3 32h8"/><path d="M21 32h10"/>'
           '<circle cx="16" cy="35" r="4"/><circle cx="36" cy="35" r="4"/></svg>',
    "cabin": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" '
             'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M5 22 24 7l19 15"/><path d="M9 20v20h30V20"/>'
             '<path d="M19 40V28h10v12"/><path d="M24 7V2"/></svg>',
    "tree": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<path d="M24 4 13 20h6L9 34h30L29 20h6L24 4Z"/><path d="M24 34v10"/>'
            '<path d="M18 44h12"/></svg>',
    "battery": '<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2.4" '
               'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<rect x="4" y="14" width="36" height="22" rx="2"/>'
               '<path d="M40 21h4v8h-4"/><path d="M12 8v6"/><path d="M30 8v6"/>'
               '<path d="M24 19l-5 7h6l-4 6"/></svg>',
    "phone": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
             'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
             '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6'
             'A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1'
             'L8.1 9.9a16 16 0 0 0 6 6l1.3-1.2a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>',
    "whatsapp": '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
                '<path d="M12 2a10 10 0 0 0-8.6 15L2 22l5.2-1.4A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2'
                'l-.3-.2-3.1.8.8-3-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.5.1'
                '-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-2-1.2 7.4 7.4 0 0 1-1.3-1.7c-.2-.3 0-.4.1-.5l.4-.5.3-.4v-.4'
                'l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5a1 1 0 0 0-.7.3A2.9 2.9 0 0 0 6.9 10a5 5 0 0 0 1.1 2.7'
                'A11.4 11.4 0 0 0 12.3 16c.6.2 1.1.4 1.5.5a3.6 3.6 0 0 0 1.6.1 2.7 2.7 0 0 0 1.7-1.2 2.1 2.1 0 0 0 .2-1.2'
                'c-.1-.1-.3-.2-.5-.3Z"/></svg>',
    "mail": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
}

# --------------------------------------------------------------------------
# Navigaatio
# --------------------------------------------------------------------------

NAV = [
    ("Etusivu", "/", None),
    ("Palvelut", "/palvelut/", [
        ("Muutto- ja kuljetuspalvelut", "/palvelut/muutto-ja-kuljetuspalvelut/"),
        ("Mökkitalkkaripalvelut", "/palvelut/mokkitalkkari-palvelut/"),
        ("Metsuripalvelut", "/palvelut/metsuripalvelut/"),
        ("Apuvirta ja renkaiden vaihto", "/palvelut/apuvirta-paivysty-renkaiden-vaihto/"),
    ]),
    ("Hinnasto", "/hinnasto/", None),
    ("Toiminta-alue", "/toiminta-alue/", [
        ("Savitaipale", "/toiminta-alue/savitaipale/"),
        ("Lappeenranta", "/toiminta-alue/lappeenranta/"),
        ("Kouvola", "/toiminta-alue/kouvola/"),
        ("Helsinki", "/toiminta-alue/helsinki/"),
    ]),
    ("UKK", "/usein-kysytyt-kysymykset/", None),
    ("Tietoa", "/tietoa-meista/", None),
    ("Yhteystiedot", "/yhteystiedot/", None),
]


def nav_html(current):
    """Rakentaa navigaation ja merkitsee nykyisen sivun."""
    items = []
    for label, href, subs in NAV:
        active = current == href or (subs and any(current == s[1] for s in subs))
        aria = ' aria-current="page"' if current == href else ""
        cls = ' class="has-sub"' if subs else ""
        # Ylätason linkki näytetään aktiivisena myös alasivulla
        if active and current != href:
            aria = ' aria-current="true"'
        item = f'<li{cls}><a class="nav__link" href="{href}"{aria}>{label}</a>'
        if subs:
            sub_items = []
            for sub_label, sub_href in subs:
                sub_aria = ' aria-current="page"' if current == sub_href else ""
                sub_items.append(
                    f'<li><a href="{sub_href}"{sub_aria}>{sub_label}</a></li>'
                )
            item += '<ul class="subnav">' + "".join(sub_items) + "</ul>"
        item += "</li>"
        items.append(item)
    return "\n            ".join(items)


# --------------------------------------------------------------------------
# Rakenteinen data (JSON-LD)
# --------------------------------------------------------------------------

LOCAL_BUSINESS = {
    "@type": ["LocalBusiness", "MovingCompany"],
    "@id": SITE["base"] + "/#yritys",
    "name": SITE["name"],
    "alternateName": "Pakuavuksi",
    "url": SITE["base"] + "/",
    "telephone": SITE["phone_link"],
    "email": SITE["email"],
    "vatID": "FI" + SITE["ytunnus"].replace("-", ""),
    "taxID": SITE["ytunnus"],
    "priceRange": "€€",
    "currenciesAccepted": "EUR",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": SITE["street"],
        "postalCode": SITE["zip"],
        "addressLocality": SITE["city"],
        "addressCountry": "FI",
    },
    "areaServed": [
        {"@type": "City", "name": n}
        for n in ["Savitaipale", "Lappeenranta", "Kouvola", "Helsinki"]
    ],
    "openingHoursSpecification": [
        {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Friday", "Saturday", "Sunday"],
            "opens": "08:00",
            "closes": "20:00",
        }
    ],
    "knowsLanguage": "fi",
    "logo": {
        "@type": "ImageObject",
        "url": SITE["base"] + "/assets/img/logo.svg",
    },
    "image": SITE["base"] + "/assets/img/og-image.png",
}


def jsonld(*blocks):
    graph = {"@context": "https://schema.org", "@graph": list(blocks)}
    return (
        '<script type="application/ld+json">\n'
        + json.dumps(graph, ensure_ascii=False, indent=2)
        + "\n    </script>"
    )


def breadcrumb_schema(trail):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": i + 1,
                "name": name,
                "item": SITE["base"] + href,
            }
            for i, (name, href) in enumerate(trail)
        ],
    }


def service_schema(name, description, path, offers=None):
    data = {
        "@type": "Service",
        "@id": SITE["base"] + path + "#palvelu",
        "name": name,
        "description": description,
        "serviceType": name,
        "provider": {"@id": SITE["base"] + "/#yritys"},
        "areaServed": [
            {"@type": "City", "name": n}
            for n in ["Savitaipale", "Lappeenranta", "Kouvola", "Helsinki"]
        ],
    }
    if offers:
        data["hasOfferCatalog"] = {
            "@type": "OfferCatalog",
            "name": name + " – hinnasto",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "name": o["name"],
                    "price": o["price"],
                    "priceCurrency": "EUR",
                    "description": o.get("desc", ""),
                }
                for o in offers
            ],
        }
    return data


# --------------------------------------------------------------------------
# Sivupohja
# --------------------------------------------------------------------------

def breadcrumb_html(trail):
    if not trail:
        return ""
    parts = []
    for i, (name, href) in enumerate(trail):
        last = i == len(trail) - 1
        if last:
            parts.append(f'<li><span aria-current="page">{name}</span></li>')
        else:
            parts.append(f'<li><a href="{href}">{name}</a></li>')
    return (
        '<nav class="breadcrumb" aria-label="Murupolku">\n          <ol>'
        + "".join(parts)
        + "</ol>\n        </nav>"
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="fi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="theme-color" content="#15171b">
    <meta name="author" content="{sitename}">
    <meta name="geo.region" content="FI-08">
    <meta name="geo.placename" content="Savitaipale">

    <meta property="og:type" content="website">
    <meta property="og:site_name" content="{sitename}">
    <meta property="og:locale" content="fi_FI">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:url" content="{canonical}">
    <meta property="og:image" content="{base}/assets/img/og-image.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{sitename} &ndash; muutot, mökkitalkkari, metsurityöt ja apuvirta">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{base}/assets/img/og-image.png">

    <link rel="preload" href="/assets/fonts/barlowcondensed-700.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="preload" href="/assets/fonts/sourceserif4-400.woff2" as="font" type="font/woff2" crossorigin>
    <link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml">
    <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
    <link rel="stylesheet" href="/assets/css/style.css">
    {schema}
</head>
<body>
<a class="skip-link" href="#sisalto">Siirry sisältöön</a>

<div class="topbar">
    <div class="wrap">
        <span class="topbar__note">Palvelen viikonloppuisin &mdash; Savitaipale, Lappeenranta, Kouvola, Helsinki</span>
        <a href="tel:{phone_link}">{phone_display}</a>
        <a href="mailto:{email}">{email}</a>
    </div>
</div>

<header class="site-header">
    <div class="wrap">
        <nav class="nav" aria-label="Päävalikko">
            <a class="brand" href="/" aria-label="Pakuavuksi &ndash; etusivulle">
                <img class="brand__logo" src="/assets/img/logo-dark.svg"
                     width="306" height="74" alt="{sitename}">
            </a>

            <button class="nav__toggle" type="button" aria-expanded="false" aria-controls="paavalikko">
                <span class="nav__toggle-bars" aria-hidden="true"></span>
                Valikko
            </button>

            <div class="nav__menu" id="paavalikko">
                <ul class="nav__list">
            {nav}
                </ul>
                <a class="btn btn--primary btn--sm nav__cta" href="tel:{phone_link}">{icon_phone} Soita {phone_display}</a>
            </div>
        </nav>
    </div>
</header>
<div class="tape" aria-hidden="true"></div>

<main id="sisalto">
{body}
</main>

<section class="cta">
    <div class="wrap cta__inner">
        <div>
            <h2>Tarvitsetko apua ensi viikonloppuna?</h2>
            <p>Soita tai laita WhatsApp-viesti, niin katsotaan aikataulu ja hinta kuntoon. Vastaan yleensä saman päivän aikana.</p>
            <p class="small" style="color:#a8bcae">Turva- ja vastuuvakuutus on kunnossa ja kattaa tekemäni työt.</p>
        </div>
        <div class="btn-row">
            <a class="btn btn--primary" href="tel:{phone_link}">{icon_phone} {phone_display}</a>
            <a class="btn btn--ghost-light" href="{whatsapp}" rel="noopener">{icon_whatsapp} WhatsApp</a>
        </div>
    </div>
</section>

<footer class="site-footer">
    <div class="wrap">
        <div class="footer__grid">
            <div class="footer__brand">
                <img class="brand__logo brand__logo--footer" src="/assets/img/logo-dark.svg"
                     width="306" height="74" alt="{sitename}">
                <p class="mt-1">{sitename}. Muutot, kuljetukset, mökkitalkkarointi, metsurityöt sekä apuvirta ja renkaanvaihdot Etelä-Karjalassa ja Kymenlaaksossa.</p>
                <p class="mt-1 small">Y-tunnus: {ytunnus}</p>
            </div>

            <div>
                <h2>Palvelut</h2>
                <ul>
                    <li><a href="/palvelut/muutto-ja-kuljetuspalvelut/">Muutto- ja kuljetuspalvelut</a></li>
                    <li><a href="/palvelut/mokkitalkkari-palvelut/">Mökkitalkkaripalvelut</a></li>
                    <li><a href="/palvelut/metsuripalvelut/">Metsuripalvelut</a></li>
                    <li><a href="/palvelut/apuvirta-paivysty-renkaiden-vaihto/">Apuvirta ja renkaanvaihto</a></li>
                    <li><a href="/hinnasto/">Hinnasto</a></li>
                </ul>
            </div>

            <div>
                <h2>Toiminta-alue</h2>
                <ul>
                    <li><a href="/toiminta-alue/savitaipale/">Savitaipale</a></li>
                    <li><a href="/toiminta-alue/lappeenranta/">Lappeenranta</a></li>
                    <li><a href="/toiminta-alue/kouvola/">Kouvola</a></li>
                    <li><a href="/toiminta-alue/helsinki/">Helsinki</a></li>
                    <li><a href="/toiminta-alue/">Kaikki alueet</a></li>
                </ul>
            </div>

            <div>
                <h2>Yhteystiedot</h2>
                <ul>
                    <li><a href="tel:{phone_link}">{phone_display}</a></li>
                    <li><a href="mailto:{email}">{email}</a></li>
                    <li><a href="{whatsapp}" rel="noopener">WhatsApp</a></li>
                    <li>{street}<br>{zip} {city}</li>
                </ul>
                <p class="small mt-1">Palvelen viikonloppuisin.<br>Apuvirta 24/7 viikonloppuisin.</p>
            </div>
        </div>

        <div class="footer__legal">
            <span>&copy; {year} {sitename}. Kaikki oikeudet pidätetään.</span>
            <span><a href="/tietosuoja/">Tietosuojaseloste</a> &middot; <a href="/yhteystiedot/">Ota yhteyttä</a></span>
        </div>
    </div>
</footer>

<script src="/assets/js/main.js" defer></script>
</body>
</html>
"""


def render(page):
    path = page["path"]
    canonical = SITE["base"] + path
    schema_blocks = [LOCAL_BUSINESS] if page.get("include_business", True) else []
    schema_blocks += page.get("schema", [])
    if page.get("trail"):
        schema_blocks.append(breadcrumb_schema(page["trail"]))

    html = TEMPLATE.format(
        title=page["title"],
        og_title=page.get("og_title", page["title"]),
        description=page["description"],
        canonical=canonical,
        sitename=SITE["name"],
        base=SITE["base"],
        nav=nav_html(path),
        body=page["body"],
        schema=jsonld(*schema_blocks),
        phone_link=SITE["phone_link"],
        phone_display=SITE["phone_display"],
        email=SITE["email"],
        whatsapp=SITE["whatsapp"],
        ytunnus=SITE["ytunnus"],
        street=SITE["street"],
        zip=SITE["zip"],
        city=SITE["city"],
        year=SITE["year"],
        icon_phone=ICONS["phone"],
        icon_whatsapp=ICONS["whatsapp"],
    )
    return html


def pagehead(title, lead, trail=None, buttons=True):
    crumbs = breadcrumb_html(trail) if trail else ""
    btns = ""
    if buttons:
        btns = f"""
        <div class="btn-row">
          <a class="btn btn--primary" href="tel:{SITE['phone_link']}">{ICONS['phone']} Soita {SITE['phone_display']}</a>
          <a class="btn btn--ghost-light" href="{SITE['whatsapp']}" rel="noopener">{ICONS['whatsapp']} WhatsApp</a>
        </div>"""
    return f"""<section class="pagehead">
      <div class="wrap">
        {crumbs}
        <h1>{title}</h1>
        <p class="pagehead__lead">{lead}</p>{btns}
      </div>
    </section>"""


def price_rows(rows):
    out = []
    for name, desc, value in rows:
        sub = f"<small>{desc}</small>" if desc else ""
        out.append(
            f'<div class="price-row"><div class="price-row__name">{name}{sub}</div>'
            f'<div class="price-row__value">{value}</div></div>'
        )
    return '<div class="pricelist">' + "".join(out) + "</div>"


def faq_block(items):
    out = []
    for q, a in items:
        out.append(
            f"<details><summary>{q}</summary>"
            f'<div class="faq__answer">{a}</div></details>'
        )
    return '<div class="faq">' + "".join(out) + "</div>"


def faq_schema(items):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": re.sub(r"<[^>]+>", "", a).strip(),
                },
            }
            for q, a in items
        ],
    }


# Ladataan sivujen sisällöt erillisestä moduulista, jotta tämä tiedosto pysyy luettavana.
from content import build_pages  # noqa: E402


def main():
    pages = build_pages(
        SITE, ICONS, pagehead, price_rows, faq_block, faq_schema,
        service_schema, breadcrumb_html,
    )

    written = []
    for page in pages:
        path = page["path"]
        if path == "/":
            out_path = os.path.join(ROOT, "index.html")
        else:
            directory = os.path.join(ROOT, path.strip("/"))
            os.makedirs(directory, exist_ok=True)
            out_path = os.path.join(directory, "index.html")

        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(render(page))
        written.append((path, os.path.relpath(out_path, ROOT)))

    # 404-sivu
    notfound = next(p for p in pages if p["path"] == "/404/")
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(render(notfound))
    shutil.rmtree(os.path.join(ROOT, "404"), ignore_errors=True)

    # Sivukartta
    indexable = [p for p in pages if p["path"] != "/404/"]
    urls = "\n".join(
        f"  <url>\n    <loc>{SITE['base']}{p['path']}</loc>\n"
        f"    <changefreq>{p.get('changefreq', 'monthly')}</changefreq>\n"
        f"    <priority>{p.get('priority', '0.7')}</priority>\n  </url>"
        for p in indexable
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n"
    )
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(sitemap)

    robots = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {SITE['base']}/sitemap.xml\n"
    )
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(robots)

    print(f"Valmis: {len(written)} sivua + sitemap.xml + robots.txt + 404.html")
    for path, out in written:
        print(f"  {path:52} -> {out}")


if __name__ == "__main__":
    main()
