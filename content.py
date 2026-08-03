# -*- coding: utf-8 -*-
"""
Sivujen sisällöt. Tekstit perustuvat pakuavuksi.fi-sivuston tietoihin:
palvelut, hinnat, toiminta-alueet ja yhteystiedot on poimittu sellaisenaan.
"""


def build_pages(SITE, ICONS, pagehead, price_rows, faq_block, faq_schema,
                service_schema, breadcrumb_html):

    P = SITE["phone_link"]
    PD = SITE["phone_display"]
    WA = SITE["whatsapp"]
    MAIL = SITE["email"]
    ICON_P = ICONS["phone"]
    ICON_W = ICONS["whatsapp"]
    ICON_M = ICONS["mail"]

    def cta_buttons(light=False):
        second = "btn--ghost-light" if light else "btn--outline"
        return (
            f'<div class="btn-row">'
            f'<a class="btn btn--primary" href="tel:{P}">{ICON_P} Soita {PD}</a>'
            f'<a class="btn {second}" href="{WA}" rel="noopener">{ICON_W} WhatsApp</a>'
            f"</div>"
        )

    def aside_contact(title, text):
        return f"""<aside class="aside-box">
            <h2>{title}</h2>
            <p>{text}</p>
            <a class="btn btn--primary btn--wide" href="tel:{P}">{ICON_P} {PD}</a>
            <a class="btn btn--outline btn--wide" href="{WA}" rel="noopener">{ICON_W} WhatsApp</a>
            <a class="btn btn--outline btn--wide" href="mailto:{MAIL}">{ICON_M} Sähköposti</a>
            <p class="small mt-2">Palvelen viikonloppuisin. Kerro tarpeesi, niin annan hinta-arvion.</p>
        </aside>"""

    SERVICES = [
        {
            "slug": "/palvelut/muutto-ja-kuljetuspalvelut/",
            "nav": "Muutto- ja kuljetuspalvelut",
            "title": "Muutto- ja kuljetuspalvelut",
            "icon": "van",
            "teaser": "Pakettiauto ja kantoapu muuttoihin, kuolinpesien tyhjennyksiin sekä tavara- ja työmaakuljetuksiin.",
            "price": "Muutot 45 €/h &middot; opiskelijamuutot alk. 90 €",
        },
        {
            "slug": "/palvelut/mokkitalkkari-palvelut/",
            "nav": "Mökkitalkkaripalvelut",
            "title": "Mökkitalkkaripalvelut",
            "icon": "cabin",
            "teaser": "Pihatyöt, nurmikonleikkuu, lumityöt ja kulkuväylien aukaisu, kun et itse pääse mökille.",
            "price": "Pihatyöt 18 €/h &middot; lumityöt 15 €/h",
        },
        {
            "slug": "/palvelut/metsuripalvelut/",
            "nav": "Metsuripalvelut",
            "title": "Metsuripalvelut",
            "icon": "tree",
            "teaser": "Puiden kaato, karsiminen ja polttopuiden teko. Moottorisaha pysyy kädessä myös ahtaassa paikassa.",
            "price": "24 €/h",
        },
        {
            "slug": "/palvelut/apuvirta-paivysty-renkaiden-vaihto/",
            "nav": "Apuvirta ja renkaiden vaihto",
            "title": "Apuvirta ja renkaiden vaihto",
            "icon": "battery",
            "teaser": "Kesä- ja talvirenkaiden vaihto sekä apuvirtapäivystys 24/7 viikonloppuisin.",
            "price": "15 €",
        },
    ]

    def service_cards():
        cards = []
        for s in SERVICES:
            cards.append(f"""<article class="card card--link">
              <div class="card__icon">{ICONS[s['icon']]}</div>
              <h3>{s['title']}</h3>
              <p>{s['teaser']}</p>
              <div class="card__price">{s['price']}</div>
              <a class="card__link" href="{s['slug']}">Lue lisää<span class="visually-hidden"> palvelusta {s['title']}</span></a>
            </article>""")
        return '<div class="grid grid--4">' + "".join(cards) + "</div>"

    pages = []

    # ======================================================================
    # ETUSIVU
    # ======================================================================

    pages.append({
        "path": "/",
        "priority": "1.0",
        "changefreq": "weekly",
        "title": "Muuttoapu ja pakettiauto viikonloppuisin | Pakuavuksi",
        "og_title": "Tmi Jarno ja pakuavuksi – muutot, mökkitalkkari ja metsurityöt",
        "description": (
            "Muutot, kuljetukset, mökkitalkkaripalvelut, metsurityöt sekä apuvirta ja "
            "renkaanvaihto viikonloppuisin. Savitaipale, Lappeenranta, Kouvola ja Helsinki. "
            f"Soita {PD}."
        ),
        "schema": [{
            "@type": "WebSite",
            "@id": SITE["base"] + "/#sivusto",
            "url": SITE["base"] + "/",
            "name": SITE["name"],
            "inLanguage": "fi",
            "publisher": {"@id": SITE["base"] + "/#yritys"},
        }],
        "body": f"""<section class="hero">
      <div class="wrap">
        <div class="hero__grid">
          <div>
            <span class="eyebrow">Yhden miehen apu &mdash; viikonloppuisin</span>
            <h1>Muuttoapu, mökkitalkkari ja metsuri samasta numerosta</h1>
            <p class="hero__lead">Olen Jarno, kokenut yhdistelmäajoneuvon kuljettaja pakun puikoissa.
            Hoidan muutot ja kuljetukset, mökin pihatyöt, puiden kaadot sekä renkaanvaihdot
            silloin kun sinulle sopii &mdash; viikonloppuisin, ilman arjen aikataulupaineita.</p>
            {cta_buttons(light=True)}
            <p class="small" style="color:#a4abb5">Turva- ja vastuuvakuutus on kunnossa ja kattaa tekemäni työt.</p>
          </div>

          <div class="hero__card">
            <h2>Ota yhteyttä</h2>
            <dl>
              <div><dt>Puhelin</dt><dd><a href="tel:{P}">{PD}</a></dd></div>
              <div><dt>WhatsApp</dt><dd><a href="{WA}" rel="noopener">{PD}</a></dd></div>
              <div><dt>Sähköposti</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
              <div><dt>Toimipaikka</dt><dd>{SITE['street']}<br>{SITE['zip']} {SITE['city']}</dd></div>
              <div><dt>Palveluajat</dt><dd>Viikonloppuisin<br>Apuvirta 24/7 viikonloppuisin</dd></div>
            </dl>
          </div>
        </div>

        <div class="hero__strip">
          <div class="hero__stat"><b>45 €/h</b><span>Muuttoapu pakettiautolla</span></div>
          <div class="hero__stat"><b>4</b><span>Palvelua samalta mieheltä</span></div>
          <div class="hero__stat"><b>24/7</b><span>Apuvirta viikonloppuisin</span></div>
          <div class="hero__stat"><b>4 kaupunkia</b><span>Savitaipale &ndash; Helsinki</span></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section__head">
          <span class="eyebrow">Palvelut</span>
          <h2>Mitä teen</h2>
          <p>Monipuolista apua monenlaiseen tarpeeseen. Voit tilata koko homman tai
          vain sen osan, johon oma aika ei riitä.</p>
        </div>
        {service_cards()}
      </div>
    </section>

    <section class="section section--paper3">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <span class="eyebrow">Näin homma etenee</span>
            <h2>Soitosta valmiiseen työhön</h2>
            <p>Yhden miehen firmassa ei ole soittoketjuja eikä asiakaspalvelujonoja.
            Puhut suoraan sen kanssa, joka työn myös tekee.</p>
            <div class="grid grid--2 steps mt-2">
              <div class="step">
                <h3>Soita tai viestitä</h3>
                <p>Kerro mistä on kyse, milloin ja missä. WhatsApp käy myös &mdash; kuvat helpottavat arviota.</p>
              </div>
              <div class="step">
                <h3>Saat hinta-arvion</h3>
                <p>Käydään läpi työn laajuus ja kesto. Hinnat ovat sivuilla näkyvissä, ei yllätyksiä.</p>
              </div>
              <div class="step">
                <h3>Sovitaan aika</h3>
                <p>Työt hoituvat viikonloppuisin. Muuttokeikat myös perjantai-iltaisin ja maanantaiaamuisin.</p>
              </div>
              <div class="step">
                <h3>Homma hoituu</h3>
                <p>Teen sovitun työn ja siistin jäljet. Vastuuvakuutus kattaa työt.</p>
              </div>
            </div>
          </div>

          {aside_contact("Kysy hinta-arviota",
                        "Kerro lyhyesti mitä tarvitset, niin kerron paljonko se maksaa ja milloin pystyn tulemaan.")}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <span class="eyebrow">Toiminta-alue</span>
            <h2>Savitaipaleelta Helsinkiin &mdash; ja siltä väliltä</h2>
            <p>Toimin Savitaipaleelta käsin, ja muuttokeikat ulottuvat pääkaupunkiseudulle asti.
            Perjantai-iltaisin liikun Helsingin, Kouvolan, Lappeenrannan ja Savitaipaleen
            alueilla sekä näiden välillä. Maanantaiaamuisin suunta on Savitaipaleelta
            Lappeenrannan ja Kouvolan kautta Helsinkiin.</p>
            <p>Jos muuttosi osuu tälle reitille, kuljetus on usein selvästi edullisempi kuin
            erikseen ajettuna. Kysy rohkeasti, vaikka osoite olisi hieman reitin sivussa.</p>
            <ul class="arealist mt-2">
              <li><a href="/toiminta-alue/savitaipale/">Savitaipale</a></li>
              <li><a href="/toiminta-alue/lappeenranta/">Lappeenranta</a></li>
              <li><a href="/toiminta-alue/kouvola/">Kouvola</a></li>
              <li><a href="/toiminta-alue/helsinki/">Helsinki</a></li>
            </ul>
          </div>

          <aside class="aside-box">
            <h2>Miksi minä</h2>
            <ul style="list-style:none;margin:0;padding:0">
              <li style="padding:10px 0;border-bottom:1px solid var(--line)"><strong>Edulliset hinnat</strong><br><span class="small muted">Hinnasto on avoimesti näkyvillä.</span></li>
              <li style="padding:10px 0;border-bottom:1px solid var(--line)"><strong>Joustavat palvelut</strong><br><span class="small muted">Tilaa koko homma tai vain osa siitä.</span></li>
              <li style="padding:10px 0;border-bottom:1px solid var(--line)"><strong>Reilu asenne</strong><br><span class="small muted">Sovitut ajat pitävät ja työ tehdään loppuun.</span></li>
              <li style="padding:10px 0"><strong>Vakuutukset kunnossa</strong><br><span class="small muted">Turva- ja vastuuvakuutus kattaa palvelut.</span></li>
            </ul>
            <a class="btn btn--ink btn--wide mt-2" href="/hinnasto/">Katso koko hinnasto</a>
          </aside>
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # PALVELUT (kooste)
    # ======================================================================

    pages.append({
        "path": "/palvelut/",
        "priority": "0.9",
        "title": "Palvelut – muutot, mökkitalkkari ja metsurityöt | Pakuavuksi",
        "description": (
            "Muutot ja kuljetukset, mökkitalkkaripalvelut, metsurityöt sekä apuvirta ja "
            "renkaiden vaihto viikonloppuisin Savitaipaleella, Lappeenrannassa ja Kouvolassa."
        ),
        "trail": [("Etusivu", "/"), ("Palvelut", "/palvelut/")],
        "body": pagehead(
            "Palvelut",
            "Neljä palvelua, yksi numero. Kaikki työt hoituvat viikonloppuisin, "
            "ja voit tilata joko koko homman tai vain sen osan, johon oma aika ei riitä.",
            [("Etusivu", "/"), ("Palvelut", "/palvelut/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        {service_cards()}
      </div>
    </section>

    <section class="section section--paper3">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Yksi tekijä, monta osaamista</h2>
            <p>Moni pieni homma jää tekemättä siksi, ettei niitä varten viitsi tilata
            erikseen muuttofirmaa, pihahuoltoa ja metsuria. Minulta saat ne samalla
            käynnillä: pakettiauto on mukana, moottorisaha pysyy kädessä ja akkukaapelit
            löytyvät takakontista.</p>
            <p>Käytännössä tämä tarkoittaa, että esimerkiksi mökin kevätsiivouksen
            yhteydessä voidaan kaataa se yksi harmillinen puu ja viedä romut samalla
            kyydillä pois. Kysy vain, niin katsotaan mikä onnistuu samalla reissulla.</p>

            <h2>Hinnoittelu on avointa</h2>
            <p>Kaikki hinnat ovat sivustolla näkyvissä ja niihin lisätään arvonlisävero
            {SITE['vat']} %. Isommista tai epäselvistä töistä sovitaan hinta etukäteen,
            jotta molemmat tietävät mistä puhutaan.</p>
            <a class="btn btn--ink mt-1" href="/hinnasto/">Avaa koko hinnasto</a>
          </div>
          {aside_contact("Mitä tarvitset?",
                        "Soita tai laita WhatsApp-viesti. Kerron heti onnistuuko homma ja mitä se maksaa.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # PALVELU 1: MUUTTO JA KULJETUS
    # ======================================================================

    muutto_prices = [
        ("Muutot", "Muuttoapu pakettiautolla. Mukana nokkakärryt raskaampien tavaroiden siirtelyyn.", "45 €/h"),
        ("Opiskelijamuutot", "Kevyempään budjettiin mitoitettu paketti. Hinta riippuu matkasta ja tavaramäärästä. Lisäksi polttoaineet.", "alk. 90–190 €"),
        ("Paketti- ja tavarakuljetukset", "Esimerkiksi työmaakuljetukset ja tavaran vienti metsäkonetyömaille.", "1 €/km + työ 20 €/h"),
    ]

    pages.append({
        "path": "/palvelut/muutto-ja-kuljetuspalvelut/",
        "priority": "0.9",
        "title": "Muuttoapu ja pakettiautokuljetukset viikonloppuisin | Pakuavuksi",
        "og_title": "Muutto- ja kuljetuspalvelut – Tmi Jarno ja pakuavuksi",
        "description": (
            "Muuttoapu 45 €/h, opiskelijamuutot alk. 90 € ja tavarakuljetukset 1 €/km. "
            "Muutot ja kuljetukset viikonloppuisin Savitaipale–Lappeenranta–Kouvola–Helsinki."
        ),
        "trail": [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
                  ("Muutto- ja kuljetuspalvelut", "/palvelut/muutto-ja-kuljetuspalvelut/")],
        "schema": [service_schema(
            "Muutto- ja kuljetuspalvelut",
            "Muuttoapu pakettiautolla, opiskelijamuutot sekä paketti- ja tavarakuljetukset "
            "viikonloppuisin Etelä-Karjalan, Kymenlaakson ja pääkaupunkiseudun välillä.",
            "/palvelut/muutto-ja-kuljetuspalvelut/",
            offers=[
                {"name": "Muuttoapu", "price": "45", "desc": "Tuntihinta, sis. pakettiauto ja nokkakärryt"},
                {"name": "Opiskelijamuutto", "price": "90", "desc": "Alkaen-hinta, lisäksi polttoaineet"},
                {"name": "Tavarakuljetus", "price": "20", "desc": "Työn tuntihinta, lisäksi 1 €/km"},
            ],
        )],
        "body": pagehead(
            "Muutto- ja kuljetuspalvelut",
            "Kokenut yhdistelmäajoneuvon kuljettaja pakun puikoissa. Rehtiä muutto- ja "
            "kuljetusapua yksityisille ja yrityksille &mdash; silloin kun arki ei ole tiellä.",
            [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
             ("Muutto- ja kuljetuspalvelut", "/palvelut/muutto-ja-kuljetuspalvelut/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Muuttopalvelut kaikenkokoisiin muuttoihin</h2>
            <p>Tarjoan sujuvia, huolellisia ja asiakaslähtöisiä muuttopalveluita sekä tavara- ja
            pakettikuljetuksia yksityisille ja yrityksille. Palvelen joustavasti viikonloppuisin,
            jolloin muutto tai kuljetus onnistuu ilman arjen aikataulupaineita.</p>
            <p>Olipa kyseessä pieni yksiö, perheasunto tai suurempi muutto, hoidan muuton alusta
            loppuun. Palvelun voi räätälöidä tarpeen mukaan &mdash; voit tilata koko muuton tai
            vain sen osan, johon oma väki ei riitä.</p>

            <h3>Muuttopalvelu voi sisältää esimerkiksi</h3>
            <ul>
              <li>Huonekalujen ja tavaroiden kantamisen</li>
              <li>Kuljetuksen lähtö- ja kohdeosoitteen välillä</li>
              <li>Tavaroiden huolellisen käsittelyn ja turvallisen kuljetuksen</li>
              <li>Nokkakärryt raskaampien tavaroiden siirtelyyn</li>
            </ul>

            <h2>Kuolinpesien muutot ja tyhjennykset</h2>
            <p>Kuolinpesän tyhjennys on harvoin pelkkä logistinen suoritus. Teen työn rauhallisesti
            ja sovitussa järjestyksessä: säilytettävät tavarat kuljetetaan sinne minne pitää ja
            loput viedään pois. Kerro etukäteen, mitkä tavarat ovat tärkeitä, niin ne käsitellään
            erikseen.</p>

            <h2>Paketti- ja tavarakuljetukset</h2>
            <p>Yksittäisen huonekalun haku, työmaakuljetus tai tavaran vienti vaikka metsäkonetyömaalle
            &mdash; pakettiauto liikkuu myös silloin, kun kyseessä ei ole muutto. Kuljetukset onnistuvat
            viikonloppuisin, mikä sopii hyvin niille työmaille, joilla arkipäivät ovat kiireisimmät.</p>

            <h2>Aikataulut ja reitit</h2>
            <p>Toiminta-alue kattaa perjantai-iltaisin Helsingin, Kouvolan, Lappeenrannan ja
            Savitaipaleen alueet sekä näiden väliset kuljetukset. Maanantaiaamuisin reitti kulkee
            Savitaipaleelta Lappeenrannan ja Kouvolan kautta Helsinkiin.</p>
            <p>Jos muuttosi osuu tälle reitille, kannattaa kysyä &mdash; paluukyydillä hinta on
            usein edullisempi kuin erikseen ajettuna.</p>

            <h2>Hinnasto</h2>
            {price_rows(muutto_prices)}
            <p class="price-note">Hintoihin lisätään arvonlisävero {SITE['vat']} %.
            Opiskelijamuuttojen hintaan lisätään polttoaineet. Pidemmistä tai poikkeuksellisen
            suurista muutoista sovitaan hinta erikseen etukäteen.</p>
            {cta_buttons()}
          </div>

          {aside_contact("Pyydä muuttotarjous",
                        "Kerro muuton lähtö- ja kohdeosoite, arvioitu tavaramäärä ja toivottu "
                        "ajankohta. Saat hinta-arvion nopeasti.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # PALVELU 2: MÖKKITALKKARI
    # ======================================================================

    mokki_prices = [
        ("Pihatyöt ja yleinen siisteys", "Mökkipihan yleiset ylläpitotyöt.", "18 €/h"),
        ("Nurmikon leikkuu mökkipihoilla", "Kertaleikkuu mökkipihalla.", "35 € / piha"),
        ("Lumityöt mökeillä", "Lumen luonti ja pihan aukaisu talvella.", "15 €/h"),
        ("Kulkuväylien aukaiseminen", "Tien ja kulkuväylien avaus mökille.", "Sopimuksen mukaan"),
        ("Haravointi ja lehtien siivoaminen", "Syyssiivous pihalla.", "Sopimuksen mukaan"),
        ("Omakotitalojen nurmikonleikkuu", "Tavallisen omakotitalon piha.", "35 €"),
        ("Isommat pihat", "Isompien pihojen nurmikon ajo.", "Hinnasta sovitaan erikseen"),
    ]

    pages.append({
        "path": "/palvelut/mokkitalkkari-palvelut/",
        "priority": "0.9",
        "title": "Mökkitalkkari Savitaipale – pihatyöt ja lumityöt | Pakuavuksi",
        "og_title": "Mökkitalkkaripalvelut – Tmi Jarno ja pakuavuksi",
        "description": (
            "Mökkitalkkaripalvelut viikonloppuisin: pihatyöt 18 €/h, nurmikonleikkuu 35 €/piha, "
            "lumityöt 15 €/h ja kulkuväylien aukaisu. Savitaipale ja Etelä-Karjala."
        ),
        "trail": [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
                  ("Mökkitalkkaripalvelut", "/palvelut/mokkitalkkari-palvelut/")],
        "schema": [service_schema(
            "Mökkitalkkaripalvelut",
            "Mökin pihatyöt, nurmikonleikkuu, lumityöt, kulkuväylien aukaisu ja haravointi "
            "viikonloppuisin Savitaipaleen ja Etelä-Karjalan alueella.",
            "/palvelut/mokkitalkkari-palvelut/",
            offers=[
                {"name": "Pihatyöt ja yleinen siisteys", "price": "18", "desc": "Tuntihinta"},
                {"name": "Nurmikon leikkuu mökkipihalla", "price": "35", "desc": "Per piha"},
                {"name": "Lumityöt mökeillä", "price": "15", "desc": "Tuntihinta"},
            ],
        )],
        "body": pagehead(
            "Mökkitalkkaripalvelut",
            "Huolenpitoa mökillesi silloinkin, kun et itse pääse paikalle. Piha pysyy siistinä, "
            "kulkuväylät auki ja mökki käyttövalmiina kaikkina vuodenaikoina.",
            [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
             ("Mökkitalkkaripalvelut", "/palvelut/mokkitalkkari-palvelut/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Eikö aika riitä hoitamaan kaikkea itse?</h2>
            <p>Tarjoan viikonloppuisin monipuolisia ja luotettavia mökkitalkkaripalveluita, joiden
            avulla mökkisi pysyy siistinä, turvallisena ja käyttövalmiina ympäri vuoden. Palvelut
            sopivat erityisesti sinulle, joka et pääse mökille säännöllisesti tai haluat säästää
            aikaa ja vaivaa mökin ylläpidossa.</p>
            <p>Käytännön esimerkki: jos mökkitielle on satanut puoli metriä lunta etkä pääse
            paikalle avaamaan kulkuväylää, minä käyn avaamassa sen. Mökille pääsee heti kun tulet.</p>

            <h2>Mitä mökkitalkkari tekee</h2>
            <ul>
              <li>Pihatyöt ja pihan yleinen siisteys</li>
              <li>Nurmikon leikkuu mökkipihoilla ja omakotitaloilla</li>
              <li>Lumityöt ja lumen luonti mökeillä</li>
              <li>Kulkuväylien ja mökkitien aukaiseminen talvella</li>
              <li>Haravointi ja lehtien siivoaminen syksyllä</li>
              <li>Portaiden ja kulkureittien putsaaminen</li>
            </ul>

            <h2>Ympärivuotinen huolenpito</h2>
            <p>Mökin ylläpito on eri asia kesällä ja talvella. Kesällä työ on useimmiten nurmikkoa,
            pihan siistimistä ja pikkuhommia. Syksyllä haravointia ja lehtien pois viemistä.
            Talvella lumitöitä ja kulkuväylien pitämistä auki, jotta mökille ylipäätään pääsee.</p>
            <p>Työt voi tilata kertaluontoisesti tai sopia toistuvaksi. Kerro, kuinka usein
            haluat pihan hoidettavan, niin katsotaan sopiva rytmi.</p>

            <h2>Hinnasto</h2>
            {price_rows(mokki_prices)}
            <p class="price-note">Hintoihin lisätään arvonlisävero {SITE['vat']} %.
            Isompien pihojen nurmikon ajosta ja laajemmista kokonaisuuksista sovitaan hinta erikseen.</p>
            {cta_buttons()}
          </div>

          {aside_contact("Kysy mökkitalkkarista",
                        "Kerro missä mökki sijaitsee ja mitä pihalla pitäisi tehdä, niin annan "
                        "arvion työn kestosta ja hinnasta.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # PALVELU 3: METSURI
    # ======================================================================

    pages.append({
        "path": "/palvelut/metsuripalvelut/",
        "priority": "0.9",
        "title": "Metsuripalvelut 24 €/h – puiden kaato ja pilkkominen | Pakuavuksi",
        "og_title": "Metsuripalvelut – Tmi Jarno ja pakuavuksi",
        "description": (
            "Metsuripalvelut viikonloppuisin 24 €/h: puiden kaato, karsiminen, polttopuiden teko "
            "ja kaadon jälkeinen siistiminen. Savitaipale, Lappeenranta ja lähialueet."
        ),
        "trail": [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
                  ("Metsuripalvelut", "/palvelut/metsuripalvelut/")],
        "schema": [service_schema(
            "Metsuripalvelut",
            "Puiden kaato, karsiminen, polttopuiden teko ja pilkkominen viikonloppuisin "
            "yksityishenkilöille, mökkiläisille ja maanomistajille.",
            "/palvelut/metsuripalvelut/",
            offers=[{"name": "Metsurityö", "price": "24", "desc": "Tuntihinta"}],
        )],
        "body": pagehead(
            "Metsuripalvelut",
            "Apua puutöihin viikonloppuisin. Moottorisaha pysyy kädessä myös tiukemmassa paikassa "
            "&mdash; siellä missä puu kasvaa väärässä kohdassa pihaa.",
            [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
             ("Metsuripalvelut", "/palvelut/metsuripalvelut/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Metsuripalvelut viikonloppuisin</h2>
            <p>Tarjoan monipuolisia ja käytännönläheisiä metsuripalveluita viikonloppuisin. Palvelu
            on suunnattu yksityishenkilöille, mökkiläisille ja maanomistajille, jotka tarvitsevat
            apua puiden kaadoissa ja polttopuiden teossa mutta eivät ehdi tai halua hoitaa töitä itse.</p>

            <h3>Palveluun kuuluu</h3>
            <ul>
              <li>Apua puiden kaatoon ja pieniin kaatoihin</li>
              <li>Kaadon jälkeinen siistiminen sovitusti</li>
              <li>Polttopuiden teko ja puiden pilkkominen</li>
              <li>Puiden karsiminen</li>
            </ul>

            <h2>Kun puu kasvaa väärässä paikassa</h2>
            <p>Tyypillinen keikka on yksittäinen puu, joka on kasvanut liian lähelle rakennusta,
            sähkölinjaa tai naapurin rajaa. Tällaiset kaadot vaativat suunnittelua: puu pitää saada
            alas hallitusti oikeaan suuntaan. Käydään tilanne läpi etukäteen ja sovitaan miten
            edetään.</p>
            <p>Jos kaato on selvästi liian vaativa turvallisesti tehtäväksi &mdash; esimerkiksi
            suoraan rakennuksen tai sähkölinjan päällä &mdash; sanon sen suoraan, jotta löydät
            oikean tekijän. Turvallisuus menee aina keikan edelle.</p>

            <h2>Polttopuut valmiiksi pinoon</h2>
            <p>Polttopuiden teko on yksi yleisimmistä tilauksista. Katkon ja pilkon puut sovittuun
            mittaan, ja kaadon jälkeinen siistiminen hoituu samalla käynnillä sovitussa laajuudessa.
            Kerro tilatessa, minkä mittaista pilkettä takkasi tai kiukaasi kaipaa.</p>

            <h2>Hinnasto</h2>
            {price_rows([("Metsurityö", "Puiden kaato, karsiminen, pilkkominen ja kaadon jälkeinen siistiminen.", "24 €/h")])}
            <p class="price-note">Hintaan lisätään arvonlisävero {SITE['vat']} %. Laajemmista
            kohteista ja useamman puun kaadoista sovitaan kokonaishinta etukäteen.</p>
            {cta_buttons()}
          </div>

          {aside_contact("Kysy metsurista",
                        "Kerro montako puuta ja millaisessa paikassa ne ovat. Kuva WhatsAppilla "
                        "auttaa arvioimaan työn nopeasti.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # PALVELU 4: APUVIRTA JA RENKAAT
    # ======================================================================

    pages.append({
        "path": "/palvelut/apuvirta-paivysty-renkaiden-vaihto/",
        "priority": "0.9",
        "title": "Apuvirta 24/7 ja renkaiden vaihto 15 € | Pakuavuksi",
        "og_title": "Apuvirta ja renkaiden vaihto – Tmi Jarno ja pakuavuksi",
        "description": (
            "Renkaiden vaihto 15 € ja apuvirtapäivystys 24/7 viikonloppuisin. Kesä- ja "
            "talvirenkaiden vaihdot Savitaipaleella ja lähialueilla. Soita " + PD + "."
        ),
        "trail": [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
                  ("Apuvirta ja renkaiden vaihto", "/palvelut/apuvirta-paivysty-renkaiden-vaihto/")],
        "schema": [service_schema(
            "Apuvirta ja renkaiden vaihto",
            "Kesä- ja talvirenkaiden vaihto sekä apuvirtapäivystys 24/7 viikonloppuisin "
            "yksityisautoilijoille.",
            "/palvelut/apuvirta-paivysty-renkaiden-vaihto/",
            offers=[{"name": "Renkaiden vaihto tai apuvirta", "price": "15", "desc": "Kertahinta"}],
        )],
        "body": pagehead(
            "Apuvirta ja renkaiden vaihto",
            "Onko työkalut hukassa tai aika kortilla? Vaihdan renkaat ja tulen antamaan apuvirtaa "
            "silloin, kun tavalliset liikkeet ovat kiinni.",
            [("Etusivu", "/"), ("Palvelut", "/palvelut/"),
             ("Apuvirta ja renkaiden vaihto", "/palvelut/apuvirta-paivysty-renkaiden-vaihto/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Autopalvelua silloin kun muut ovat kiinni</h2>
            <p>Tarjoan joustavaa ja luotettavaa autopalvelua viikonloppuisin, keskittyen
            renkaanvaihtoihin sekä apuvirran antamiseen. Palvelu on suunnattu yksityisautoilijoille,
            jotka tarvitsevat apua silloin, kun perinteiset palvelut ovat kiinni.</p>
            <p>Toimin viikonloppuisin, ja apuvirta-asioissa päivystän 24/7 viikonloppujen ajan.</p>

            <h2>Renkaiden vaihto</h2>
            <p>Vaihdan sekä kesä- että talvirenkaat. Voit joko tuoda auton minulle Savitaipaleelle
            tai tilata minut paikalle &mdash; kumpi vain sopii paremmin. Renkaanvaihto on tyypillinen
            homma, joka jää tekemättä juuri silloin kun renkaanvaihtoliikkeissä on pisimmät jonot.</p>
            <ul>
              <li>Kesärenkaiden vaihto keväällä</li>
              <li>Talvirenkaiden vaihto syksyllä</li>
              <li>Vaihto joko omalla pihallasi tai minun luonani</li>
            </ul>

            <h2>Apuvirtapäivystys 24/7 viikonloppuisin</h2>
            <p>Tyhjä akku pysäyttää auton yleensä kaikkein huonoimpaan aikaan: pakkasaamuna,
            kaupan parkkipaikalla tai mökkitien päässä lauantai-iltana. Viikonloppuisin päivystän
            ympäri vuorokauden ja tulen antamaan apuvirtaa.</p>
            <p>Huomaa, että apuvirta saa auton käyntiin, mutta jos akku on tullut tiensä päähän,
            se pitää vaihtaa. Kerron paikan päällä suoraan, kummasta on kyse.</p>

            <h2>Hinnasto</h2>
            {price_rows([("Renkaiden vaihto tai apuvirta", "Kesä- ja talvirenkaiden vaihdot sekä apuvirta viikonloppuisin.", "15 €")])}
            <p class="price-note">Hintaan lisätään arvonlisävero {SITE['vat']} %. Kauempana
            sijaitseviin kohteisiin voidaan lisätä matkakulut &mdash; kerron ne aina etukäteen puhelimessa.</p>
            {cta_buttons()}
          </div>

          {aside_contact("Akku loppu juuri nyt?",
                        "Soita suoraan. Viikonloppuisin päivystän apuvirta-asioissa ympäri "
                        "vuorokauden.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # HINNASTO
    # ======================================================================

    pages.append({
        "path": "/hinnasto/",
        "priority": "0.9",
        "changefreq": "monthly",
        "title": "Hinnasto – muuttoapu, mökkitalkkari ja metsuri | Pakuavuksi",
        "description": (
            "Avoin hinnasto: muutot 45 €/h, opiskelijamuutot alk. 90 €, kuljetukset 1 €/km, "
            "metsurityöt 24 €/h, pihatyöt 18 €/h, lumityöt 15 €/h, renkaanvaihto 15 €."
        ),
        "trail": [("Etusivu", "/"), ("Hinnasto", "/hinnasto/")],
        "body": pagehead(
            "Hinnasto",
            "Hinnat ovat avoimesti näkyvissä, jotta tiedät mistä maksat jo ennen kuin soitat. "
            f"Kaikkiin hintoihin lisätään arvonlisävero {SITE['vat']} %.",
            [("Etusivu", "/"), ("Hinnasto", "/hinnasto/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Muutto- ja kuljetuspalvelut</h2>
            {price_rows(muutto_prices)}

            <h2>Mökkitalkkaripalvelut</h2>
            {price_rows(mokki_prices)}

            <h2>Metsuripalvelut</h2>
            {price_rows([("Metsurityö", "Puiden kaato, karsiminen, polttopuiden teko ja pilkkominen sekä kaadon jälkeinen siistiminen sovitusti.", "24 €/h")])}

            <h2>Apuvirta ja renkaiden vaihto</h2>
            {price_rows([("Renkaiden vaihto tai apuvirta", "Kesä- ja talvirenkaiden vaihdot sekä apuvirtapäivystys 24/7 viikonloppuisin.", "15 €")])}

            <h2>Hyvä tietää hinnoista</h2>
            <ul>
              <li>Kaikkiin hintoihin lisätään arvonlisävero {SITE['vat']} %.</li>
              <li>Opiskelijamuuttojen hintaan lisätään polttoaineet.</li>
              <li>Isommista pihoista, laajemmista metsurikeikoista ja poikkeuksellisen suurista muutoista sovitaan hinta erikseen etukäteen.</li>
              <li>Kauempana sijaitseviin kohteisiin voidaan lisätä matkakulut. Kerron ne aina ennen työn aloittamista.</li>
              <li>Turva- ja vastuuvakuutus on kunnossa ja kattaa tekemäni työt.</li>
            </ul>
            <p>Jos et ole varma, mihin palveluun tarpeesi osuu tai kauanko työ kestää, soita.
            Käydään homma läpi puhelimessa ja annan arvion, ennen kuin mitään sovitaan.</p>
            {cta_buttons()}
          </div>

          {aside_contact("Pyydä tarjous",
                        "Isommista töistä kannattaa aina kysyä kokonaishintaa. Kerro työn "
                        "laajuus, niin lasken arvion.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # TOIMINTA-ALUE (kooste)
    # ======================================================================

    pages.append({
        "path": "/toiminta-alue/",
        "priority": "0.8",
        "title": "Toiminta-alue – Savitaipale, Lappeenranta, Kouvola, Helsinki",
        "og_title": "Toiminta-alue – Tmi Jarno ja pakuavuksi",
        "description": (
            "Muutot ja kuljetukset perjantai-iltaisin ja maanantaiaamuisin välillä Savitaipale, "
            "Lappeenranta, Kouvola ja Helsinki. Mökkitalkkari- ja metsurityöt lähialueilla."
        ),
        "trail": [("Etusivu", "/"), ("Toiminta-alue", "/toiminta-alue/")],
        "body": pagehead(
            "Toiminta-alue",
            "Kotipaikka on Savitaipale, mutta muuttokeikat ulottuvat pääkaupunkiseudulle asti. "
            "Reitin varrella hinta on usein edullisempi kuin erikseen ajettuna.",
            [("Etusivu", "/"), ("Toiminta-alue", "/toiminta-alue/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Vakioreitit</h2>
            <p>Muutto- ja kuljetuskeikoissa kuljen säännöllisesti samaa väliä, ja tälle reitille
            osuvat keikat kannattaa aina kysyä.</p>
            <ul>
              <li><strong>Perjantai-iltaisin:</strong> Helsinki, Kouvola, Lappeenranta ja Savitaipale sekä näiden väliset kuljetukset.</li>
              <li><strong>Maanantaiaamuisin:</strong> Savitaipale, Lappeenranta, Kouvola ja Helsinki.</li>
            </ul>
            <p>Mökkitalkkari-, metsuri- ja renkaanvaihtopalvelut painottuvat Savitaipaleelle ja
            sen lähialueille, koska ne ovat luonteeltaan paikallisia töitä. Kysy silti rohkeasti,
            vaikka olisit vähän kauempana &mdash; jos keikka osuu muun reissun varrelle, se yleensä onnistuu.</p>

            <h2>Alueet</h2>
            <div class="grid grid--2 mt-2">
              <article class="card card--link">
                <h3>Savitaipale</h3>
                <p>Kotipaikka. Mökkitalkkarointi, metsurityöt, renkaanvaihdot ja muutot.</p>
                <a class="card__link" href="/toiminta-alue/savitaipale/">Palvelut Savitaipaleella</a>
              </article>
              <article class="card card--link">
                <h3>Lappeenranta</h3>
                <p>Kaupunkimuutot ja opiskelijamuutot, kuljetukset sekä pihatyöt.</p>
                <a class="card__link" href="/toiminta-alue/lappeenranta/">Palvelut Lappeenrannassa</a>
              </article>
              <article class="card card--link">
                <h3>Kouvola</h3>
                <p>Muutot ja tavarakuljetukset reitin varrella, myös työmaakuljetukset.</p>
                <a class="card__link" href="/toiminta-alue/kouvola/">Palvelut Kouvolassa</a>
              </article>
              <article class="card card--link">
                <h3>Helsinki</h3>
                <p>Pitkän matkan muutot pääkaupunkiseudulle ja sieltä pois.</p>
                <a class="card__link" href="/toiminta-alue/helsinki/">Palvelut Helsingissä</a>
              </article>
            </div>
          </div>

          {aside_contact("Osuuko osoitteesi reitille?",
                        "Kerro lähtö- ja kohdeosoite, niin katson sopiiko keikka viikonlopun "
                        "reitille. Silloin hinta on usein edullisempi.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # ALUESIVUT
    # ======================================================================

    areas = [
        {
            "slug": "savitaipale",
            "name": "Savitaipale",
            "inessive": "Savitaipaleella",
            "title": "Muuttoapu, mökkitalkkari ja metsuri Savitaipaleella",
            "desc": ("Savitaipaleen paikallinen apu viikonloppuisin: muutot 45 €/h, "
                     "mökkitalkkarointi, metsurityöt sekä renkaanvaihto ja apuvirta 15 €."),
            "lead": ("Savitaipale on kotipaikkani, ja täällä hoituvat kaikki palvelut &mdash; "
                     "muutoista mökkitalkkarointiin ja puiden kaadosta apuvirtaan."),
            "body": """
            <h2>Paikallinen tekijä samasta pitäjästä</h2>
            <p>Toimipaikkani on Ojastintiellä Savitaipaleella, joten täkäläisiin keikkoihin lähtö
            on nopeaa eikä matkakuluja juuri kerry. Tämä näkyy erityisesti pienissä hommissa:
            yhden puun kaadossa, renkaanvaihdossa tai lumitöissä ei ole järkeä maksaa pitkästä
            ajomatkasta.</p>

            <h2>Mökkitalkkarointi Saimaan mökeillä</h2>
            <p>Savitaipaleen seudulla on paljon vapaa-ajan asuntoja, joiden omistajat asuvat
            muualla. Juuri tähän mökkitalkkaripalvelu on tehty: pidän pihan siistinä, leikkaan
            nurmikon ja avaan talvella kulkuväylän, jotta mökille pääsee heti kun tulet paikalle.
            Jos et pääse mökillesi aukaisemaan kulkuväylää, minä käyn.</p>

            <h2>Metsurityöt ja polttopuut</h2>
            <p>Puiden kaato, karsiminen ja polttopuiden teko ovat Savitaipaleella arkipäivää.
            Hoidan yksittäiset kaadot pihapiirissä sekä polttopuiden katkomisen ja pilkkomisen
            sovittuun mittaan.</p>

            <h2>Renkaanvaihto ja apuvirta paikan päällä</h2>
            <p>Voit tuoda auton minulle renkaanvaihtoon tai tilata minut kotipihaasi.
            Viikonloppuisin päivystän apuvirta-asioissa 24/7, mikä on hyödyllistä varsinkin
            pakkasaamuina ja mökkiteiden päässä.</p>
            """,
            "services": ["muutto", "mokki", "metsuri", "apuvirta"],
        },
        {
            "slug": "lappeenranta",
            "name": "Lappeenranta",
            "inessive": "Lappeenrannassa",
            "title": "Muuttoapu Lappeenranta – opiskelijamuutot alk. 90 €",
            "desc": ("Muuttoapu ja pakettiautokuljetukset Lappeenrannassa viikonloppuisin. "
                     "Muutot 45 €/h, opiskelijamuutot alk. 90 €. Myös piha- ja metsurityöt."),
            "lead": ("Lappeenranta on vakioreitilläni sekä perjantai-iltaisin että "
                     "maanantaiaamuisin, joten muutot ja kuljetukset onnistuvat joustavasti."),
            "body": """
            <h2>Opiskelijamuutot Lappeenrannassa</h2>
            <p>Lappeenranta on opiskelijakaupunki, ja kämpänvaihto osuu usein juuri siihen
            hetkeen kun rahaa on vähiten. Opiskelijamuutot on hinnoiteltu tätä varten:
            alkaen 90&ndash;190 euroa matkasta ja tavaramäärästä riippuen, lisäksi polttoaineet.
            Nokkakärryt kulkevat mukana, joten jääkaappi ja sohva eivät jää portaisiin.</p>

            <h2>Asuntomuutot kaupungissa</h2>
            <p>Yksiöstä perheasuntoon &mdash; muutto hoituu alusta loppuun tai vain siltä osin
            kuin tarvitset. Moni tilaa pelkän auton ja kantoavun ja pakkaa itse. Sekin sopii.</p>

            <h2>Kuljetukset Lappeenrannan ja pääkaupunkiseudun välillä</h2>
            <p>Lappeenranta on Savitaipaleen ja Helsingin välisellä reitilläni, joten
            kaupunkien väliset muutot ja tavarakuljetukset ovat luontevia. Perjantai-iltaisin
            ja maanantaiaamuisin liikkeellä ollessani saman reitin keikat ovat usein
            edullisempia kuin erikseen ajettuna.</p>

            <h2>Muut palvelut Lappeenrannan suunnalla</h2>
            <p>Myös pihatyöt, nurmikonleikkuu, lumityöt ja metsurikeikat onnistuvat
            Lappeenrannan alueella. Kysy näistä erikseen, niin sovitaan sopiva ajankohta.</p>
            """,
            "services": ["muutto", "mokki", "metsuri"],
        },
        {
            "slug": "kouvola",
            "name": "Kouvola",
            "inessive": "Kouvolassa",
            "title": "Muuttoapu ja tavarakuljetukset Kouvolassa",
            "desc": ("Muuttoapu ja pakettiautokuljetukset Kouvolassa viikonloppuisin. "
                     "Muutot 45 €/h ja tavarakuljetukset 1 €/km. Myös työmaakuljetukset."),
            "lead": ("Kouvola on reittini varrella Lappeenrannan ja Helsingin välissä, joten "
                     "muutot ja tavarakuljetukset hoituvat kätevästi saman reissun yhteydessä."),
            "body": """
            <h2>Muutot Kouvolassa ja Kouvolasta</h2>
            <p>Ajan Kouvolan kautta säännöllisesti perjantai-iltaisin ja maanantaiaamuisin.
            Käytännössä tämä tarkoittaa, että muutto Kouvolasta Lappeenrantaan, Savitaipaleelle
            tai Helsinkiin osuu valmiiksi ajettavalle reitille &mdash; ja se näkyy hinnassa.</p>

            <h2>Tavara- ja pakettikuljetukset</h2>
            <p>Kaikki kuljetettava ei ole muutto. Yksittäinen huonekalu, verkkokaupasta ostettu
            iso tavara tai kuorma rakennustarviketta liikkuu pakettiautolla hintaan 1 €/km,
            lisäksi työn osuus 20 €/h.</p>

            <h2>Työmaakuljetukset viikonloppuisin</h2>
            <p>Hoidan myös työmaakuljetuksia, esimerkiksi tavaran viemistä metsäkonetyömaille.
            Viikonloppuajankohta sopii tähän usein hyvin, koska silloin työmaalla on tilaa
            eikä kuljetus häiritse muuta työtä.</p>

            <h2>Sovi kyyti etukäteen</h2>
            <p>Koska Kouvolan keikat sidotaan viikonlopun reittiin, kannattaa olla ajoissa
            liikkeellä. Ilmoita mieluiten viikkoa ennen, niin saadaan aikataulu kohdilleen.</p>
            """,
            "services": ["muutto"],
        },
        {
            "slug": "helsinki",
            "name": "Helsinki",
            "inessive": "Helsingissä",
            "title": "Muutto Helsinkiin ja Helsingistä viikonloppuisin",
            "desc": ("Pitkän matkan muutot ja kuljetukset Helsingin ja Etelä-Karjalan välillä. "
                     "Perjantai-iltaisin ja maanantaiaamuisin. Muutot 45 €/h."),
            "lead": ("Helsinki on reittini toinen pääte. Perjantai-iltaisin tulen päin "
                     "pääkaupunkiseutua ja maanantaiaamuisin suunta on jälleen Helsinkiin."),
            "body": """
            <h2>Muutot pääkaupunkiseudulle ja sieltä pois</h2>
            <p>Muutto Etelä-Karjalasta Helsinkiin tai toisin päin on tyypillisesti kallis keikka,
            koska pelkkä ajomatka syö ison osan päivästä. Minulla tämä väli tulee ajettua joka
            tapauksessa perjantai-iltaisin ja maanantaiaamuisin, joten samaan suuntaan menevä
            muutto onnistuu järkevällä hinnalla.</p>

            <h2>Opiskelijoiden ja työn perässä muuttavien reitti</h2>
            <p>Helsinki&ndash;Lappeenranta-väli on tuttu monelle opiskelijalle ja työn perässä
            muuttavalle. Opiskelijamuutot alkavat 90 eurosta, ja nokkakärryt ovat mukana.</p>

            <h2>Tavarakuljetukset Helsingin suuntaan</h2>
            <p>Myös yksittäiset isot tavarat kulkevat samalla reitillä. Jos ostit huonekalun
            Helsingistä etkä saa sitä kotiin, kysy kyytiä &mdash; usein se järjestyy seuraavan
            viikonlopun reissulla.</p>

            <h2>Varaa ajoissa</h2>
            <p>Pääkaupunkiseudun keikat kannattaa sopia hyvissä ajoin, koska ne sidotaan
            viikonlopun ajoreittiin. Kerro lähtö- ja kohdeosoite sekä arvioitu tavaramäärä,
            niin katson mille viikonlopulle keikka sopii.</p>
            """,
            "services": ["muutto"],
        },
    ]

    svc_by_key = {
        "muutto": SERVICES[0],
        "mokki": SERVICES[1],
        "metsuri": SERVICES[2],
        "apuvirta": SERVICES[3],
    }

    for a in areas:
        trail = [("Etusivu", "/"), ("Toiminta-alue", "/toiminta-alue/"),
                 (a["name"], f"/toiminta-alue/{a['slug']}/")]
        cards = "".join(
            f"""<article class="card card--link">
              <div class="card__icon">{ICONS[svc_by_key[k]['icon']]}</div>
              <h3>{svc_by_key[k]['title']}</h3>
              <p>{svc_by_key[k]['teaser']}</p>
              <div class="card__price">{svc_by_key[k]['price']}</div>
              <a class="card__link" href="{svc_by_key[k]['slug']}">Lue lisää<span class="visually-hidden"> palvelusta {svc_by_key[k]['title']}</span></a>
            </article>"""
            for k in a["services"]
        )
        grid_class = "grid--2" if len(a["services"]) <= 2 else "grid--4"

        pages.append({
            "path": f"/toiminta-alue/{a['slug']}/",
            "priority": "0.7",
            "title": a["title"] + " | Pakuavuksi",
            "og_title": a["title"],
            "description": a["desc"],
            "trail": trail,
            "body": pagehead(a["title"], a["lead"], trail) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            {a['body']}
            {cta_buttons()}
          </div>
          {aside_contact(f"Palvelut {a['inessive']}",
                         "Soita tai laita viesti, niin katsotaan sopiva ajankohta ja hinta.")}
        </div>
      </div>
    </section>

    <section class="section section--paper3">
      <div class="wrap">
        <div class="section__head">
          <h2>Palvelut {a['inessive']}</h2>
        </div>
        <div class="grid {grid_class}">{cards}</div>
      </div>
    </section>""",
        })

    # ======================================================================
    # UKK
    # ======================================================================

    faqs = [
        ("Milloin teet töitä?",
         "<p>Palvelen viikonloppuisin. Muutto- ja kuljetuskeikat hoituvat myös perjantai-iltaisin "
         "ja maanantaiaamuisin. Apuvirta-asioissa päivystän viikonloppuisin ympäri vuorokauden.</p>"),
        ("Mille alueelle tulet?",
         "<p>Muutot ja kuljetukset kattavat Savitaipaleen, Lappeenrannan, Kouvolan ja Helsingin "
         "sekä näiden väliset matkat. Mökkitalkkari-, metsuri- ja renkaanvaihtopalvelut "
         "painottuvat Savitaipaleelle ja lähialueille.</p>"),
        ("Paljonko muutto maksaa?",
         "<p>Muuttoapu maksaa 45 €/h ja opiskelijamuutot alkaen 90–190 € matkasta ja tavaramäärästä "
         "riippuen, lisäksi polttoaineet. Paketti- ja tavarakuljetukset 1 €/km, työn osuus 20 €/h. "
         f"Hintoihin lisätään arvonlisävero {SITE['vat']} %.</p>"),
        ("Saanko kokonaishinnan etukäteen?",
         "<p>Kyllä. Isommista töistä sovitaan kokonaishinta etukäteen. Kerro työn laajuus ja "
         "aikataulu puhelimessa tai WhatsAppilla, niin annan arvion ennen kuin mitään sovitaan.</p>"),
        ("Onko sinulla vakuutukset kunnossa?",
         "<p>On. Turva- ja vastuuvakuutus on kunnossa ja kattaa tekemäni palvelut.</p>"),
        ("Kuuluuko muuttoon kantoapu vai pelkkä auto?",
         "<p>Molemmat onnistuvat. Voit tilata koko muuton kantoineen tai pelkän auton ja kuljettajan. "
         "Nokkakärryt kulkevat aina mukana raskaampien tavaroiden siirtelyyn.</p>"),
        ("Hoidatko kuolinpesän tyhjennyksiä?",
         "<p>Kyllä. Kuolinpesien muutot ja tyhjennykset ovat yksi yleisimmistä keikoista. Kerro "
         "etukäteen, mitkä tavarat säilytetään, niin ne käsitellään erikseen.</p>"),
        ("Voinko saada kotitalousvähennyksen?",
         "<p>Kotitalouteen tehtävästä työstä voi tietyissä tilanteissa saada kotitalousvähennyksen. "
         "Vähennyksen edellytykset kannattaa tarkistaa Verohallinnon ohjeista, ja voit kysyä asiaa "
         "myös minulta tarjousta pyytäessäsi.</p>"),
        ("Tuletko avaamaan mökkitien talvella?",
         "<p>Tulen. Kulkuväylien aukaiseminen on osa mökkitalkkaripalvelua. Jos et itse pääse "
         "mökillesi avaamaan kulkuväylää, käyn tekemässä sen puolestasi.</p>"),
        ("Kaadatko puun, joka on lähellä rakennusta?",
         "<p>Pienet ja hallitut kaadot onnistuvat myös ahtaassa paikassa. Jos kaato on selvästi "
         "liian vaativa turvallisesti tehtäväksi, sanon sen suoraan, jotta löydät oikean tekijän.</p>"),
        ("Mitä apuvirta maksaa ja milloin sitä saa?",
         "<p>Apuvirta ja renkaiden vaihto maksavat 15 €. Apuvirtapäivystys toimii viikonloppuisin "
         "24/7. Kauempana sijaitseviin kohteisiin voidaan lisätä matkakulut, jotka kerron etukäteen.</p>"),
        ("Miten varaan ajan?",
         f"<p>Soita numeroon {PD}, laita WhatsApp-viesti samaan numeroon tai lähetä sähköpostia "
         f"osoitteeseen {MAIL}. Kerro mitä tarvitset, missä ja milloin, niin vastaan yleensä saman "
         "päivän aikana.</p>"),
    ]

    pages.append({
        "path": "/usein-kysytyt-kysymykset/",
        "priority": "0.7",
        "title": "Usein kysytyt kysymykset | Tmi Jarno ja pakuavuksi",
        "description": (
            "Vastauksia yleisimpiin kysymyksiin: aikataulut, toiminta-alue, hinnat, vakuutukset, "
            "kotitalousvähennys ja ajan varaaminen."
        ),
        "trail": [("Etusivu", "/"), ("Usein kysytyt kysymykset", "/usein-kysytyt-kysymykset/")],
        "schema": [faq_schema(faqs)],
        "body": pagehead(
            "Usein kysytyt kysymykset",
            "Tähän on koottu ne kysymykset, jotka tulevat puhelimessa vastaan useimmin. "
            "Jos et löydä vastausta, soita niin selvitetään.",
            [("Etusivu", "/"), ("Usein kysytyt kysymykset", "/usein-kysytyt-kysymykset/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div>
            {faq_block(faqs)}
          </div>
          {aside_contact("Ei löytynyt vastausta?",
                        "Soita tai laita viesti. Vastaan mieluummin puhelimessa kuin arvuuttelen "
                        "sivuilla.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # TIETOA
    # ======================================================================

    pages.append({
        "path": "/tietoa-meista/",
        "priority": "0.6",
        "title": "Tietoa – monitoimimies pakun ratissa | Pakuavuksi",
        "og_title": "Tietoa yrityksestä – Tmi Jarno ja pakuavuksi",
        "description": (
            "Tmi Jarno ja pakuavuksi on savitaipalelainen yhden miehen yritys, joka tarjoaa "
            "muutto-, mökkitalkkari-, metsuri- ja autopalveluita viikonloppuisin."
        ),
        "trail": [("Etusivu", "/"), ("Tietoa", "/tietoa-meista/")],
        "body": pagehead(
            "Monitoimimies pakun ratissa",
            "Tmi Jarno ja pakuavuksi on savitaipalelainen yhden miehen yritys. Kun soitat, "
            "puhut suoraan sen kanssa, joka työn myös tekee.",
            [("Etusivu", "/"), ("Tietoa", "/tietoa-meista/")],
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="split">
          <div class="prose">
            <h2>Yksi mies, yksi paku, monta hommaa</h2>
            <p>Olen Jarno ja pyöritän toiminimeä Savitaipaleelta käsin. Taustaltani olen kokenut
            yhdistelmäajoneuvon kuljettaja, joten pakettiauton ratissa ollaan tutuissa maisemissa
            &mdash; olipa kyseessä ahdas kaupunkipiha Lappeenrannassa tai mutkainen mökkitie
            Saimaan rannalla.</p>
            <p>Yritys on syntynyt yksinkertaisesta havainnosta: moni tarvitsee apua juuri niinä
            päivinä, kun useimmat palvelut ovat kiinni. Muutto osuu lauantaille, renkaat pitäisi
            vaihtaa sunnuntaina ja mökkitie on umpeutunut juuri ennen viikonloppua. Siksi palvelen
            viikonloppuisin.</p>

            <!-- JARNO: Tähän kohtaan kannattaa lisätä omin sanoin muutama lause siitä,
                 kuinka kauan olet alalla ollut ja mikä sinua työssä motivoi. Omalla äänellä
                 kirjoitettu esittely erottuu ja tuo luottamusta. -->

            <h2>Mitä lupaan</h2>
            <ul>
              <li><strong>Edulliset hinnat.</strong> Hinnasto on avoimesti sivuilla, ei piilokuluja.</li>
              <li><strong>Joustavat palvelut.</strong> Tilaa koko homma tai vain se osa, johon aika ei riitä.</li>
              <li><strong>Reilu asenne.</strong> Sovitut ajat pitävät ja työ tehdään loppuun asti.</li>
              <li><strong>Suora puhe.</strong> Jos jokin ei onnistu tai ei ole järkevää, sanon sen.</li>
            </ul>

            <h2>Vakuutukset ja vastuu</h2>
            <p>Turva- ja vastuuvakuutus on kunnossa ja kattaa tarjoamani palvelut. Yritys on
            merkitty kaupparekisteriin tunnuksella {SITE['ytunnus']}.</p>

            <h2>Palvelut lyhyesti</h2>
            <ul>
              <li><a href="/palvelut/muutto-ja-kuljetuspalvelut/">Muutto- ja kuljetuspalvelut</a> &mdash; muutot, kuolinpesät, tavarakuljetukset</li>
              <li><a href="/palvelut/mokkitalkkari-palvelut/">Mökkitalkkaripalvelut</a> &mdash; pihatyöt, nurmikko, lumityöt</li>
              <li><a href="/palvelut/metsuripalvelut/">Metsuripalvelut</a> &mdash; kaadot, karsiminen, polttopuut</li>
              <li><a href="/palvelut/apuvirta-paivysty-renkaiden-vaihto/">Apuvirta ja renkaanvaihto</a> &mdash; päivystys 24/7 viikonloppuisin</li>
            </ul>
            {cta_buttons()}
          </div>

          <aside class="aside-box">
            <h2>Yrityksen tiedot</h2>
            <p class="small"><strong>Nimi</strong><br>{SITE['name']}</p>
            <p class="small"><strong>Y-tunnus</strong><br>{SITE['ytunnus']}</p>
            <p class="small"><strong>Osoite</strong><br>{SITE['street']}<br>{SITE['zip']} {SITE['city']}</p>
            <p class="small"><strong>Puhelin</strong><br><a href="tel:{P}">{PD}</a></p>
            <p class="small"><strong>Sähköposti</strong><br><a href="mailto:{MAIL}">{MAIL}</a></p>
            <a class="btn btn--primary btn--wide mt-1" href="/yhteystiedot/">Ota yhteyttä</a>
          </aside>
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # YHTEYSTIEDOT
    # ======================================================================

    pages.append({
        "path": "/yhteystiedot/",
        "priority": "0.9",
        "title": "Yhteystiedot – soita 045 633 4700 | Pakuavuksi",
        "og_title": "Yhteystiedot – Tmi Jarno ja pakuavuksi",
        "description": (
            f"Tmi Jarno ja pakuavuksi, {SITE['street']}, {SITE['zip']} {SITE['city']}. "
            f"Puhelin {PD}, sähköposti {MAIL}. Palvelen viikonloppuisin."
        ),
        "trail": [("Etusivu", "/"), ("Yhteystiedot", "/yhteystiedot/")],
        "schema": [{
            "@type": "ContactPage",
            "@id": SITE["base"] + "/yhteystiedot/#sivu",
            "url": SITE["base"] + "/yhteystiedot/",
            "name": "Yhteystiedot",
            "about": {"@id": SITE["base"] + "/#yritys"},
        }],
        "body": pagehead(
            "Ota yhteyttä",
            "Nopeimmin saat minut kiinni puhelimella tai WhatsApp-viestillä. Kerro mitä "
            "tarvitset, missä ja milloin &mdash; vastaan yleensä saman päivän aikana.",
            [("Etusivu", "/"), ("Yhteystiedot", "/yhteystiedot/")],
            buttons=False,
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="grid grid--3">
          <div class="contact-card">
            <span class="contact-card__label">Puhelin</span>
            <a class="contact-card__value" href="tel:{P}">{PD}</a>
            <small>Nopein tapa. Jos en ehdi vastata, soitan takaisin.</small>
          </div>
          <div class="contact-card">
            <span class="contact-card__label">WhatsApp</span>
            <a class="contact-card__value" href="{WA}" rel="noopener">{PD}</a>
            <small>Kuvat helpottavat arviota &mdash; esimerkiksi puusta tai muuttokuormasta.</small>
          </div>
          <div class="contact-card">
            <span class="contact-card__label">Sähköposti</span>
            <a class="contact-card__value" href="mailto:{MAIL}">{MAIL}</a>
            <small>Sopii hyvin tarjouspyyntöihin ja laskutusasioihin.</small>
          </div>
        </div>

        <div class="grid grid--3 mt-2">
          <div class="contact-card">
            <span class="contact-card__label">Osoite</span>
            <span class="contact-card__value" style="font-size:1.1rem">{SITE['street']}<br>{SITE['zip']} {SITE['city']}</span>
            <small>Auton voi tuoda tänne esimerkiksi renkaanvaihtoon.</small>
          </div>
          <div class="contact-card">
            <span class="contact-card__label">Palveluajat</span>
            <span class="contact-card__value" style="font-size:1.1rem">Viikonloppuisin</span>
            <small>Muuttokeikat myös perjantai-iltaisin ja maanantaiaamuisin. Apuvirta 24/7 viikonloppuisin.</small>
          </div>
          <div class="contact-card">
            <span class="contact-card__label">Y-tunnus</span>
            <span class="contact-card__value" style="font-size:1.1rem">{SITE['ytunnus']}</span>
            <small>{SITE['name']}. Turva- ja vastuuvakuutus kunnossa.</small>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--paper3">
      <div class="wrap">
        <div class="split">
          <div>
            <span class="eyebrow">Tarjouspyyntö</span>
            <h2>Lähetä viesti</h2>
            <p class="lead mb-2">Kerro lyhyesti mistä on kyse, niin palaan asiaan hinta-arvion kanssa.</p>

            <form class="form" id="yhteydenotto" action="https://formspree.io/f/LISAA-LOMAKKEEN-OSOITE" method="post">
              <div class="field">
                <label for="nimi">Nimi</label>
                <input type="text" id="nimi" name="nimi" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="puhelin">Puhelinnumero</label>
                <input type="tel" id="puhelin" name="puhelin" autocomplete="tel" required>
              </div>
              <div class="field">
                <label for="sahkoposti">Sähköposti</label>
                <input type="email" id="sahkoposti" name="sahkoposti" autocomplete="email">
              </div>
              <div class="field">
                <label for="palvelu">Mitä palvelua tarvitset?</label>
                <select id="palvelu" name="palvelu">
                  <option>Muutto- tai kuljetuspalvelu</option>
                  <option>Mökkitalkkaripalvelut</option>
                  <option>Metsuripalvelut</option>
                  <option>Apuvirta tai renkaiden vaihto</option>
                  <option>Muu / en osaa sanoa</option>
                </select>
              </div>
              <div class="field">
                <label for="viesti">Viesti</label>
                <textarea id="viesti" name="viesti" required></textarea>
                <p class="field__hint">Kerro esimerkiksi osoite, ajankohta ja työn laajuus.</p>
              </div>

              <div class="hp-field" aria-hidden="true">
                <label for="yritys-tarkiste">Jätä tämä kenttä tyhjäksi</label>
                <input type="text" id="yritys-tarkiste" name="yritys-tarkiste" tabindex="-1" autocomplete="off">
              </div>

              <div>
                <button class="btn btn--primary" type="submit">Lähetä viesti</button>
              </div>
              <p class="form__status" id="lomake-tila" role="status" hidden></p>
            </form>
          </div>

          {aside_contact("Kiire?",
                        "Puhelin on aina nopein. Viikonloppuisin apuvirta-asioissa päivystän "
                        "ympäri vuorokauden.")}
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # TIETOSUOJA
    # ======================================================================

    pages.append({
        "path": "/tietosuoja/",
        "priority": "0.3",
        "changefreq": "yearly",
        "title": "Tietosuojaseloste | Tmi Jarno ja pakuavuksi",
        "description": (
            "Tietosuojaseloste: mitä tietoja kerätään yhteydenottolomakkeen kautta, "
            "mihin niitä käytetään ja kuinka kauan niitä säilytetään."
        ),
        "trail": [("Etusivu", "/"), ("Tietosuojaseloste", "/tietosuoja/")],
        "body": pagehead(
            "Tietosuojaseloste",
            "Miten yhteydenottojen yhteydessä annettuja tietoja käsitellään.",
            [("Etusivu", "/"), ("Tietosuojaseloste", "/tietosuoja/")],
            buttons=False,
        ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="prose" style="max-width:760px">
          <h2>Rekisterinpitäjä</h2>
          <p>{SITE['name']} (Y-tunnus {SITE['ytunnus']})<br>
          {SITE['street']}, {SITE['zip']} {SITE['city']}<br>
          Puhelin <a href="tel:{P}">{PD}</a><br>
          Sähköposti <a href="mailto:{MAIL}">{MAIL}</a></p>

          <h2>Mitä tietoja kerätään</h2>
          <p>Sivustolla kerätään henkilötietoja ainoastaan silloin, kun otat itse yhteyttä:
          yhteydenottolomakkeella, sähköpostitse, puhelimitse tai WhatsAppilla. Lomakkeella
          kysytään nimi, puhelinnumero, sähköpostiosoite sekä viestin sisältö.</p>

          <h2>Mihin tietoja käytetään</h2>
          <p>Tietoja käytetään yhteydenottoon vastaamiseen, tarjouksen tekemiseen sekä
          sovitun työn toteuttamiseen ja laskuttamiseen. Tietoja ei käytetä markkinointiin
          eikä niitä luovuteta ulkopuolisille muutoin kuin lakisääteisten velvoitteiden,
          kuten kirjanpidon, edellyttämässä laajuudessa.</p>

          <h2>Säilytysaika</h2>
          <p>Yhteydenottoihin liittyviä tietoja säilytetään niin kauan kuin asian hoitaminen
          edellyttää. Toteutuneisiin toimeksiantoihin liittyvät tiedot säilytetään
          kirjanpitolain edellyttämän ajan.</p>

          <h2>Evästeet</h2>
          <p>Sivusto ei käytä seuranta- tai mainosevästeitä eikä siihen ole upotettu
          ulkopuolisia analytiikka- tai mainospalveluita.</p>

          <h2>Omat oikeutesi</h2>
          <p>Sinulla on oikeus tarkastaa itseäsi koskevat tiedot, pyytää niiden oikaisemista
          tai poistamista. Pyynnöt voi lähettää sähköpostitse osoitteeseen
          <a href="mailto:{MAIL}">{MAIL}</a>.</p>

          <!-- JARNO: Jos otat käyttöön yhteydenottolomakkeen välityspalvelun (esim. Formspree)
               tai kävijäseurannan, lisää niiden nimet tähän selosteeseen. -->
        </div>
      </div>
    </section>""",
    })

    # ======================================================================
    # 404
    # ======================================================================

    pages.append({
        "path": "/404/",
        "title": "Sivua ei löytynyt | Tmi Jarno ja pakuavuksi",
        "description": "Etsimääsi sivua ei löytynyt. Palaa etusivulle tai katso palvelut ja yhteystiedot.",
        "body": pagehead(
            "Sivua ei löytynyt",
            "Osoite saattoi muuttua tai linkissä on kirjoitusvirhe. Alta löydät tärkeimmät sivut.",
            None,
            buttons=False,
        ) + """
    <section class="section">
      <div class="wrap">
        <div class="btn-row">
          <a class="btn btn--primary" href="/">Etusivulle</a>
          <a class="btn btn--outline" href="/palvelut/">Palvelut</a>
          <a class="btn btn--outline" href="/hinnasto/">Hinnasto</a>
          <a class="btn btn--outline" href="/yhteystiedot/">Yhteystiedot</a>
        </div>
      </div>
    </section>""",
    })

    return pages
