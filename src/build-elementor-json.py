"""Template Elementor (.json) della sottopagina «Dove trovare Rossopregio».

Uscita: elementor/rossopregio-punti-vendita.json
Import: WordPress > Template > Libreria template > Importa template.
Poi nella pagina: icona cartella «Aggiungi template» > I miei template > Inserisci.

Il sito usa Elementor 4.3.6 con i Contenitori ed Elementor Pro (verificato 20/11/2026).
I colori sono collegati ai Colori globali del kit 1101:
  primary #004928 · secondary #8D1926 (carne) · text #535A60 · f929e7e #FFF7F1 (sabbia)

Uso:  python3 src/build-elementor-json.py   (dalla cartella sito/, DOPO build-rossopregio.py)
"""
import json
import secrets
from pathlib import Path

SITO = Path(__file__).resolve().parent.parent
BASE = "https://alessiogranella.github.io/produttori-arborea-pagine-prodotto/assets/"
WIDGET = (SITO / "elementor/widget-punti-vendita-rossopregio.html").read_text(encoding="utf-8")

CARNE_SCURO = "#6B121C"
G = lambda chiave, colore: {chiave: f"globals/colors?id={colore}"}


def uid():
    return secrets.token_hex(4)[:7]


def px(v):
    return {"unit": "px", "size": v, "sizes": []}


def box(t, r, b, l, unit="px"):
    return {"unit": unit, "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


def tipo(famiglia, peso, size, size_m=None, lh=None, prefix="typography"):
    s = {f"{prefix}_typography": "custom", f"{prefix}_font_family": famiglia,
         f"{prefix}_font_weight": str(peso), f"{prefix}_font_size": px(size)}
    if size_m:
        s[f"{prefix}_font_size_tablet"] = px(round((size + size_m) / 2))
        s[f"{prefix}_font_size_mobile"] = px(size_m)
    if lh:
        s[f"{prefix}_line_height"] = {"unit": "em", "size": lh, "sizes": []}
    return s


def widget(tipo_w, settings):
    return {"id": uid(), "elType": "widget", "widgetType": tipo_w, "settings": settings, "elements": []}


def contenitore(figli, settings=None, inner=False):
    return {"id": uid(), "elType": "container", "isInner": inner, "settings": settings or {}, "elements": figli}


def sezione(figli, sfondo=None, glob=None, riga=False):
    s = {
        "content_width": "boxed", "boxed_width": px(1140),
        "flex_direction": "row" if riga else "column",
        "flex_direction_tablet": "column" if riga else "column",
        "flex_direction_mobile": "column",
        "flex_align_items": "center" if riga else "stretch",
        "flex_gap": {"unit": "px", "size": 56, "column": "56", "row": "32", "isLinked": False},
        "padding": box(88, 24, 88, 24), "padding_tablet": box(64, 32, 64, 32),
        "padding_mobile": box(48, 16, 48, 16),
        "flex_gap_tablet": {"unit": "px", "size": 32, "column": "32", "row": "32", "isLinked": True},
    }
    if sfondo:
        s.update({"background_background": "classic", "background_color": sfondo})
    if glob:
        s["__globals__"] = glob
    return contenitore(figli, s)


def colonna(figli, larghezza=50):
    return contenitore(figli, {
        "content_width": "full", "width": {"unit": "%", "size": larghezza, "sizes": []},
        "width_tablet": {"unit": "%", "size": 100, "sizes": []},
        "width_mobile": {"unit": "%", "size": 100, "sizes": []},
        "flex_direction": "column", "flex_gap": {"unit": "px", "size": 16, "column": "16", "row": "16", "isLinked": True},
        "padding": box(0, 0, 0, 0),
    }, inner=True)


def titolo(testo, tag, size, size_m, colore="secondary", hex_colore=None):
    s = {"title": testo, "header_size": tag, **tipo("Fredoka", 600, size, size_m, 1.15)}
    if hex_colore:
        s["title_color"] = hex_colore
    else:
        s["title_color"] = "#8D1926"
        s["__globals__"] = G("title_color", colore)
    return widget("heading", s)


def sottotitolo(testo, colore=CARNE_SCURO):
    return widget("heading", {"title": testo, "header_size": "p", "title_color": colore,
                              **tipo("Fredoka", 500, 22, 19, 1.3)})


def testo(html, colore=None, glob="text", centrato=False):
    s = {"editor": html, **tipo("Roboto Flex", 400, 17, 16, 1.6)}
    if colore:
        s["text_color"] = colore
    else:
        s["text_color"] = "#535A60"
        s["__globals__"] = G("text_color", glob)
    if centrato:
        s["align"] = "center"
    return widget("text-editor", s)


def immagine(file, larghezza=None, alt=""):
    s = {"image": {"url": BASE + file, "id": "", "size": "", "alt": alt, "source": "library"}, "image_size": "full"}
    if larghezza:
        s["width"] = px(larghezza)
        s["align"] = "left"
        s["align_mobile"] = "left"
    else:
        s["width"] = {"unit": "%", "size": 100, "sizes": []}
        s["width_tablet"] = {"unit": "%", "size": 70, "sizes": []}
        s["width_mobile"] = {"unit": "%", "size": 100, "sizes": []}
        s["align_tablet"] = "center"
    return widget("image", s)


def p(*righe):
    return "".join(f"<p>{r}</p>" for r in righe)


# ---------------------------------------------------------------- 1. HERO
hero = sezione([
    colonna([
        testo('<p><a href="https://www.produttoriarborea.it/">Home</a> &nbsp;/&nbsp; '
              '<a href="https://www.produttoriarborea.it/rossopregio/">Rossopregio</a> &nbsp;/&nbsp; Dove trovare Rossopregio</p>',
              colore="#8D1926") | {},
        immagine("loghi/rp-lockup.png", 200, "Rossopregio — Produttori Arborea"),
        titolo("DOVE TROVARE ROSSOPREGIO", "h1", 56, 36),
        sottotitolo("La qualità della carne nata e allevata in Sardegna, vicino a te."),
        testo(p("La carne Rossopregio arriva ai consumatori attraverso una rete di macellerie e punti vendita.",
                "Una presenza che permette di trovare la qualità della carne Rossopregio in tutto il territorio, "
                "portando fino al banco il lavoro di una filiera che nasce e si sviluppa in Sardegna.",
                "Vuoi sapere dove acquistare Rossopregio? Consulta la mappa e trova il punto vendita più vicino a te.")),
    ], 52),
    colonna([immagine("ill/rp-limousine-carne.png", alt="")], 48),
], sfondo="#FFF7F1", glob=G("background_color", "f929e7e"), riga=True)

# le briciole: maiuscolo piccolo in Fredoka
briciole = hero["elements"][0]["elements"][0]["settings"]
briciole.update(tipo("Fredoka", 400, 13, 12, 1.4))
briciole.update({"typography_text_transform": "uppercase",
                 "typography_letter_spacing": px(1), "text_color": "#8D1926",
                 "__globals__": G("text_color", "secondary")})

# ---------------------------------------------------------------- 2. MAPPA
mappa = sezione([
    titolo("TROVA IL PUNTO VENDITA ROSSOPREGIO PIÙ VICINO A TE", "h2", 38, 28),
    sottotitolo("Cerchi una macelleria o un punto vendita dove acquistare la carne Rossopregio?"),
    testo(p("Con la nostra mappa interattiva puoi individuare facilmente i punti vendita che propongono "
            "Rossopregio e scoprire dove trovare la nostra carne nella tua zona.",
            "Inserisci una città, una provincia o un CAP oppure utilizza la geolocalizzazione per trovare "
            "il punto vendita più vicino a te.")),
    widget("html", {"html": WIDGET, "_margin": box(16, 0, 0, 0)}),
], sfondo="#FFFFFF")
mappa["settings"]["flex_gap"] = {"unit": "px", "size": 16, "column": "16", "row": "16", "isLinked": True}

# ---------------------------------------------------------------- 3. QUALITÀ
qualita = sezione([
    colonna([immagine("ill/rp-stalle-e-mucche-carne.png", alt="")], 46),
    colonna([
        titolo("LA QUALITÀ DELLA CARNE ROSSOPREGIO", "h2", 38, 28),
        sottotitolo("Quando scegli Rossopregio, scegli il risultato di un lavoro che inizia molto prima di "
                    "arrivare al banco della tua macelleria."),
        testo(p("La filiera della Cooperativa Produttori Arborea coinvolge circa 200 allevatori associati e segue "
                "diverse fasi della produzione: dalla scelta degli animali all’alimentazione, dall’allevamento alla "
                "lavorazione, fino alla distribuzione.",
                "Ogni fase contribuisce a costruire il percorso della carne Rossopregio, attraverso "
                "un’organizzazione che unisce persone, competenze e strutture in Sardegna.",
                "Oggi questa filiera arriva al consumatore anche grazie a una rete di circa 300 macellerie "
                "fidelizzate in Sardegna.",
                "Una storia che nasce in Sardegna e arriva fino al banco.")),
    ], 54),
], sfondo="#FFF7F1", glob=G("background_color", "f929e7e"), riga=True)

# ---------------------------------------------------------------- 4. CONTATTI
contatti = sezione([
    titolo("NON TROVI ROSSOPREGIO NELLA TUA ZONA?", "h2", 38, 28, hex_colore="#FFF7F1"),
    testo(p("Le macellerie sono il collegamento tra il lavoro della filiera e chi ogni giorno sceglie la nostra carne.",
            "Se non hai trovato un punto vendita vicino a te o desideri ricevere maggiori informazioni sulla "
            "disponibilità di Rossopregio nella tua zona, contattaci."), colore="#FFF7F1", centrato=True),
    widget("button", {
        "text": "Contattaci", "align": "center",
        "link": {"url": "https://www.produttoriarborea.it/contatti/", "is_external": "", "nofollow": "", "custom_attributes": ""},
        "button_text_color": "#FFF7F1", "background_color": "#8D1926",
        "border_border": "solid", "border_width": box(3, 3, 3, 3) | {"isLinked": True}, "border_color": "#FFF7F1",
        "border_radius": box(50, 50, 50, 50) | {"isLinked": True},
        "hover_color": "#8D1926", "button_background_hover_color": "#FFF7F1", "button_hover_border_color": "#FFF7F1",
        **tipo("Fredoka", 700, 14, None, 1.0),
        "typography_text_transform": "uppercase",
        "text_padding": box(15, 28, 15, 28),
        "_margin": box(12, 0, 0, 0),
    }),
], sfondo="#8D1926", glob=G("background_color", "secondary"))
contatti["settings"]["flex_align_items"] = "center"
contatti["settings"]["flex_gap"] = {"unit": "px", "size": 16, "column": "16", "row": "16", "isLinked": True}
contatti["elements"][0]["settings"]["align"] = "center"

modello = {
    "version": "0.4",
    "title": "Rossopregio — Dove trovare Rossopregio",
    "type": "page",
    "page_settings": {},
    "content": [hero, mappa, qualita, contatti],
}
out = SITO / "elementor/rossopregio-punti-vendita.json"
out.write_text(json.dumps(modello, ensure_ascii=False, indent=1), encoding="utf-8")
print("ok:", out.name, out.stat().st_size // 1024, "KB")
