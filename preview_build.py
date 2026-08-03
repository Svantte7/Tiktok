#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kokoaa koko sivuston yhdeksi HTML-tiedostoksi esikatselua varten.

Tuotantosivusto koostuu erillisistä HTML-tiedostoista. Tämä skripti niputtaa
ne yhteen tiedostoon, jossa navigointi toimii hash-osoitteilla (#/palvelut/).
Tarkoitettu vain jaettavaa esikatselulinkkiä varten — ei julkaisuun.

Käyttö: python3 preview_build.py [kohdetiedosto]
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))

ROUTES = [
    "/", "/palvelut/",
    "/palvelut/muutto-ja-kuljetuspalvelut/",
    "/palvelut/mokkitalkkari-palvelut/",
    "/palvelut/metsuripalvelut/",
    "/palvelut/apuvirta-paivysty-renkaiden-vaihto/",
    "/hinnasto/", "/toiminta-alue/",
    "/toiminta-alue/savitaipale/", "/toiminta-alue/lappeenranta/",
    "/toiminta-alue/kouvola/", "/toiminta-alue/helsinki/",
    "/usein-kysytyt-kysymykset/", "/tietoa-meista/",
    "/yhteystiedot/", "/tietosuoja/",
]


def body_of(route):
    path = "index.html" if route == "/" else os.path.join(route.strip("/"), "index.html")
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        html = fh.read()

    body = re.search(r"<body>(.*)</body>", html, re.S).group(1)
    # Ulkoinen skripti korvataan yhdellä yhteisellä skriptillä lopussa
    body = re.sub(r'<script src="[^"]*"[^>]*></script>', "", body)
    # Sisäiset linkit hash-muotoon; puhelin, sähköposti ja WhatsApp jätetään ennalleen
    body = re.sub(r'href="(/(?!assets/)[^"]*)"', r'href="#\1"', body)
    # Ohita-linkki toimisi vain ensimmäisellä sivulla, joten poistetaan kopiot
    if route != "/":
        body = body.replace(
            '<a class="skip-link" href="#/#sisalto">Siirry sisältöön</a>', ""
        )
    else:
        body = body.replace('href="#/#sisalto"', 'href="#sisalto"')
    return body.strip()


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "esikatselu.html")

    with open(os.path.join(ROOT, "assets/css/style.css"), encoding="utf-8") as fh:
        css = fh.read()

    sections = []
    for route in ROUTES:
        sections.append(
            f'<div class="pv-page" data-route="{route}" hidden>\n{body_of(route)}\n</div>'
        )

    extra_css = """
/* --- Vain esikatselua varten --- */
.pv-page[hidden] { display: none; }
.pv-bar {
  position: fixed; left: 0; right: 0; bottom: 0; z-index: 500;
  background: #15171b; color: #a9b0ba;
  border-top: 1px solid #363b44;
  font-size: .8rem; line-height: 1.4;
  padding: 9px 14px;
  display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
}
.pv-bar strong { color: #fff; }
.pv-bar code { color: #f08a5a; font-size: .78rem; }
.pv-bar button {
  margin-left: auto; background: transparent; border: 1px solid #363b44;
  color: #c3c9d2; font: inherit; font-size: .78rem; padding: 4px 10px;
  border-radius: 3px; cursor: pointer;
}
.pv-bar button:hover { background: #2b3038; color: #fff; }
.pv-bar[hidden] { display: none; }
body.pv-has-bar { padding-bottom: 52px; }
"""

    script = """
(function () {
  "use strict";
  var pages = Array.prototype.slice.call(document.querySelectorAll(".pv-page"));

  function currentRoute() {
    var h = location.hash.replace(/^#/, "");
    if (!h || h.charAt(0) !== "/") return "/";
    return h.split("#")[0];
  }

  function show(route) {
    var found = false;
    pages.forEach(function (p) {
      var match = p.getAttribute("data-route") === route;
      p.hidden = !match;
      if (match) found = true;
    });
    if (!found) {
      pages.forEach(function (p) { p.hidden = p.getAttribute("data-route") !== "/"; });
      route = "/";
    }
    var label = document.getElementById("pv-route");
    if (label) label.textContent = route;
    window.scrollTo(0, 0);
    closeMenus();
  }

  function closeMenus() {
    document.querySelectorAll(".nav__menu.is-open").forEach(function (m) {
      m.classList.remove("is-open");
    });
    document.querySelectorAll(".nav__toggle").forEach(function (t) {
      t.setAttribute("aria-expanded", "false");
    });
  }

  window.addEventListener("hashchange", function () { show(currentRoute()); });
  show(currentRoute());

  /* Mobiilivalikko toimii kaikilla sivuosioilla */
  document.addEventListener("click", function (e) {
    var toggle = e.target.closest(".nav__toggle");
    if (!toggle) return;
    var menu = toggle.parentElement.querySelector(".nav__menu");
    if (!menu) return;
    var open = menu.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") closeMenus();
  });

  /* Lomake: sama suojaus kuin tuotannossa */
  document.addEventListener("submit", function (e) {
    var form = e.target.closest("#yhteydenotto");
    if (!form) return;
    e.preventDefault();
    var status = form.querySelector("#lomake-tila");
    if (status) {
      status.textContent =
        "Lomakkeen lähetys ei ole vielä käytössä. Soita 045 633 4700, laita " +
        "WhatsApp-viesti tai sähköpostia osoitteeseen pakuavuksi@hotmail.com.";
      status.hidden = false;
    }
  });

  /* Esikatselupalkki */
  var bar = document.getElementById("pv-bar");
  document.body.classList.add("pv-has-bar");
  document.getElementById("pv-close").addEventListener("click", function () {
    bar.hidden = true;
    document.body.classList.remove("pv-has-bar");
  });
})();
"""

    page = f"""<title>Pakuavuksi – sivuston esikatselu</title>
<style>
{css}
{extra_css}
</style>

{chr(10).join(sections)}

<div class="pv-bar" id="pv-bar">
  <span><strong>Esikatselu</strong> &mdash; kaikki 17 sivua yhdessä tiedostossa. Nykyinen sivu: <code id="pv-route">/</code></span>
  <span>Puhelin-, WhatsApp- ja sähköpostilinkit toimivat normaalisti.</span>
  <button type="button" id="pv-close">Piilota</button>
</div>

<script>
{script}
</script>
"""

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(page)

    kb = os.path.getsize(out_path) / 1024
    print(f"Esikatselu kirjoitettu: {out_path} ({kb:.0f} kt, {len(ROUTES)} sivua)")


if __name__ == "__main__":
    main()
