/* Mobiilivalikko + yhteydenottolomakkeen käsittely. Ei riippuvuuksia. */
(function () {
  "use strict";

  /* ---- Mobiilivalikko ---- */
  var toggle = document.querySelector(".nav__toggle");
  var menu = document.getElementById("paavalikko");

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.classList.contains("is-open")) {
        menu.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---- Yhteydenottolomake ----
     Staattinen sivusto ei voi itse lähettää sähköpostia. Lomake toimii vasta
     kun sille on asetettu vastaanottava osoite (esim. Formspree tai Netlify
     Forms) — ohjeet README.md-tiedostossa. Siihen asti lomake ei häviä
     hiljaisesti, vaan ohjaa asiakkaan puhelimeen ja sähköpostiin. */
  var form = document.getElementById("yhteydenotto");
  if (!form) return;

  var status = document.getElementById("lomake-tila");
  var PLACEHOLDER = "LISAA-LOMAKKEEN-OSOITE";

  function show(msg) {
    if (!status) return;
    status.textContent = msg;
    status.hidden = false;
  }

  form.addEventListener("submit", function (e) {
    var action = form.getAttribute("action") || "";

    if (action.indexOf(PLACEHOLDER) !== -1) {
      e.preventDefault();
      show(
        "Lomakkeen lähetys ei ole vielä käytössä. Soita 045 633 4700, " +
          "laita WhatsApp-viesti tai sähköpostia osoitteeseen pakuavuksi@hotmail.com."
      );
      return;
    }

    if (form.querySelector(".hp-field input").value !== "") {
      e.preventDefault();
      return;
    }

    e.preventDefault();
    var btn = form.querySelector('button[type="submit"]');
    if (btn) {
      btn.disabled = true;
      btn.textContent = "Lähetetään…";
    }

    fetch(action, {
      method: "POST",
      body: new FormData(form),
      headers: { Accept: "application/json" }
    })
      .then(function (res) {
        if (!res.ok) throw new Error("virhe");
        form.reset();
        show("Kiitos viestistä. Vastaan yleensä saman päivän aikana.");
      })
      .catch(function () {
        show(
          "Viestin lähetys ei onnistunut. Soita 045 633 4700 tai lähetä " +
            "sähköpostia osoitteeseen pakuavuksi@hotmail.com."
        );
      })
      .then(function () {
        if (btn) {
          btn.disabled = false;
          btn.textContent = "Lähetä viesti";
        }
      });
  });
})();
