"""Monta la sottopagina «Dove trovare Rossopregio» e il suo widget.

Uscite:
  elementor/widget-punti-vendita-rossopregio.html -> da incollare nel widget HTML di Elementor
  rossopregio-punti-vendita.html                  -> mockup della pagina con nav e footer del sito

Dati:
  src/punti-rossopregio.json      -> i punti vendita (ORA SONO DI ESEMPIO: da sostituire con l'elenco vero)
  src/comuni-sardegna-cap.json    -> 377 comuni: [nome, provincia, lat, lng, [CAP]]

Uso:  python3 src/build-rossopregio.py   (dalla cartella sito/)
"""
import json
from pathlib import Path

SITO = Path(__file__).resolve().parent.parent
punti = json.loads((SITO / "src/punti-rossopregio.json").read_text(encoding="utf-8"))
comuni = (SITO / "src/comuni-sardegna-cap.json").read_text(encoding="utf-8").strip()
DI_ESEMPIO = any("esempio" in p["nome"].lower() for p in punti)

widget = ((SITO / "src/widget-punti-vendita-rossopregio.html").read_text(encoding="utf-8")
          .replace("/*PUNTI*/[]", json.dumps(punti, ensure_ascii=False, separators=(",", ":")))
          .replace("/*COMUNI*/[]", comuni))

(SITO / "elementor").mkdir(exist_ok=True)
(SITO / "elementor/widget-punti-vendita-rossopregio.html").write_text(widget, encoding="utf-8")

# nav e footer: quelli della pagina Meridoro (replica del sito live), adattati a Rossopregio
base = (SITO / "meridoro-prodotti.html").read_text(encoding="utf-8")
testa = base[: base.index('<main id="contenuto">')]
coda = base[base.index("</main>"):]

i = testa.index('<meta name="description"')
testa = (testa
  .replace('class="theme-agrozoo"', 'class="theme-carni"')
  .replace("<title>I prodotti Meridoro &mdash; Produttori Arborea</title>",
           "<title>Dove trovare Rossopregio &mdash; Produttori Arborea</title>")
  .replace(testa[i:testa.index('>', i) + 1],
           '<meta name="description" content="Trova la macelleria o il punto vendita Rossopregio più vicino a te: la carne nata e allevata in Sardegna.">')
  .replace('<a href="https://www.produttoriarborea.it/rossopregio/">Rossopregio</a>',
           '<a href="https://www.produttoriarborea.it/rossopregio/" aria-current="page">Rossopregio</a>')
  .replace('<a href="https://www.produttoriarborea.it/meridoro/" aria-current="page">Meridoro</a>',
           '<a href="https://www.produttoriarborea.it/meridoro/">Meridoro</a>'))

# footer Rossopregio: social e due sedi come sul sito live (/rossopregio/)
ICO_TEL = coda[coda.index('<svg viewBox="0 0 512 512" aria-hidden="true"><path d="M497.39'):]
ICO_TEL = ICO_TEL[: ICO_TEL.index("</svg>") + 6]
ICO_MAIL = coda[coda.index('<svg viewBox="0 0 512 512" aria-hidden="true"><path d="M464 64H48'):]
ICO_MAIL = ICO_MAIL[: ICO_MAIL.index("</svg>") + 6]
ICO_PIN = coda[coda.index('<svg viewBox="0 0 384 512"'):]
ICO_PIN = ICO_PIN[: ICO_PIN.index("</svg>") + 6]

def sede(titolo, tel, tel_txt, indirizzo):
    return f'''<div>
          <h4>{titolo}</h4>
          <ul>
            <li>{ICO_TEL}<a href="tel:{tel}">{tel_txt}</a></li>
            <li>{ICO_MAIL}<a href="mailto:info@produttoriarborea.it">info@produttoriarborea.it</a></li>
            <li>{ICO_PIN}<span>{indirizzo}</span></li>
          </ul>
        </div>'''

a = coda.index('<div class="pa-footer__contatti">')
b = coda.index('<div class="pa-footer__legale">')
contatti = f'''<div class="pa-footer__contatti pa-footer__contatti--due">
        <img src="assets/loghi/produttori-arborea-cerchio.png" alt="Produttori Arborea">
        {sede("Centro lavorazione carni Rossopregio", "+390783802074", "(+39) 0783 802074", "Strada 19 Est - 09092 Arborea (OR)")}
        {sede("Centro di allevamento Rossopregio", "+390783800788", "(+39) 0783 800788", "Strada 20 Est - 09092 Arborea (OR)")}
      </div>
    </div>
  </div>

  '''
coda = (coda[:a] + contatti + coda[b:]) \
  .replace("https://www.facebook.com/meridoroproduttoriarborea", "https://www.facebook.com/rossopregioproduttoriarborea") \
  .replace("https://www.instagram.com/meridoro_produttoriarborea/", "https://www.instagram.com/rossopregio_produttoriarborea/")

avviso = '''
<!-- Solo mockup: in produzione questa riga non esiste. -->
<p class="rp-avviso">Mockup &middot; i punti vendita sulla mappa sono <b>dati di esempio</b>, da sostituire con l&rsquo;elenco delle macellerie.</p>
''' if DI_ESEMPIO else ""

corpo = f'''<main id="contenuto">
{avviso}
<!-- ====== 1. DOVE TROVARE ROSSOPREGIO · contenitore 2 colonne: titolo + testo | immagine ====== -->
<section class="pa-hero">
  <div class="container pa-due">
    <div>
      <p class="pa-hero__briciole">
        <a href="https://www.produttoriarborea.it/">Home</a> &nbsp;/&nbsp;
        <a href="https://www.produttoriarborea.it/rossopregio/">Rossopregio</a> &nbsp;/&nbsp; Dove trovare Rossopregio
      </p>
      <div class="rp-lockup">
        <img class="rp-lockup__marchio" src="assets/loghi/rossopregio.svg" alt="Rossopregio">
        <img class="rp-lockup__endorser" src="assets/loghi/produttori-arborea.svg" alt="Produttori Arborea">
      </div>
      <h1>DOVE TROVARE ROSSOPREGIO</h1>
      <p class="rp-sottotitolo">La qualit&agrave; della carne nata e allevata in Sardegna, vicino a te.</p>
      <p class="testo-largo">La carne Rossopregio arriva ai consumatori attraverso una rete di macellerie e punti vendita.</p>
      <p class="testo-largo">Una presenza che permette di trovare la qualit&agrave; della carne Rossopregio in tutto il territorio, portando fino al banco il lavoro di una filiera che nasce e si sviluppa in Sardegna.</p>
      <p class="testo-largo">Vuoi sapere dove acquistare Rossopregio? Consulta la mappa e trova il punto vendita pi&ugrave; vicino a te.</p>
    </div>
    <figure class="pa-due__figura rp-ill" style="margin:0">
      <img class="rp-ill__img" src="assets/ill/rp-limousine-carne.png" width="1585" height="1024" alt="">
    </figure>
  </div>
</section>

<!-- ====== 2. TROVA IL PUNTO VENDITA · titolo + testo + widget HTML di Elementor ====== -->
<section class="fascia fascia--bianca" id="mappa">
  <div class="container">
    <div class="rp-intro">
      <h2>TROVA IL PUNTO VENDITA ROSSOPREGIO PI&Ugrave; VICINO A TE</h2>
      <p class="rp-sottotitolo">Cerchi una macelleria o un punto vendita dove acquistare la carne Rossopregio?</p>
      <p class="testo-largo">Con la nostra mappa interattiva puoi individuare facilmente i punti vendita che propongono Rossopregio e scoprire dove trovare la nostra carne nella tua zona.</p>
      <p class="testo-largo">Inserisci una citt&agrave;, una provincia o un CAP oppure utilizza la geolocalizzazione per trovare il punto vendita pi&ugrave; vicino a te.</p>
    </div>
<!-- INIZIO WIDGET HTML ELEMENTOR -->
{widget}
<!-- FINE WIDGET HTML ELEMENTOR -->
  </div>
</section>

<!-- ====== 3. LA QUALITÀ DELLA CARNE · contenitore 2 colonne: titolo + testo | immagine ====== -->
<section class="fascia">
  <div class="container pa-due pa-due--inverso">
    <div>
      <h2>LA QUALIT&Agrave; DELLA CARNE ROSSOPREGIO</h2>
      <p class="rp-sottotitolo">Quando scegli Rossopregio, scegli il risultato di un lavoro che inizia molto prima di arrivare al banco della tua macelleria.</p>
      <p class="testo-largo">La filiera della Cooperativa Produttori Arborea coinvolge circa 200 allevatori associati e segue diverse fasi della produzione: dalla scelta degli animali all&rsquo;alimentazione, dall&rsquo;allevamento alla lavorazione, fino alla distribuzione.</p>
      <p class="testo-largo">Ogni fase contribuisce a costruire il percorso della carne Rossopregio, attraverso un&rsquo;organizzazione che unisce persone, competenze e strutture in Sardegna.</p>
      <p class="testo-largo">Oggi questa filiera arriva al consumatore anche grazie a una rete di circa 300 macellerie fidelizzate in Sardegna.</p>
      <p class="testo-largo">Una storia che nasce in Sardegna e arriva fino al banco.</p>
    </div>
    <figure class="pa-due__figura rp-ill" style="margin:0">
      <img class="rp-ill__img" src="assets/ill/rp-stalle-e-mucche-carne.png" width="1800" height="980" alt="" loading="lazy">
    </figure>
  </div>
</section>

<!-- ====== 4. NON TROVI ROSSOPREGIO · titolo + testo + pulsante su fondo carne ====== -->
<section class="fascia rp-fascia-carne" id="contatti">
  <div class="container centrato">
    <h2>NON TROVI ROSSOPREGIO NELLA TUA ZONA?</h2>
    <p class="testo-largo">Le macellerie sono il collegamento tra il lavoro della filiera e chi ogni giorno sceglie la nostra carne.</p>
    <p class="testo-largo">Se non hai trovato un punto vendita vicino a te o desideri ricevere maggiori informazioni sulla disponibilit&agrave; di Rossopregio nella tua zona, contattaci.</p>
    <p style="margin-top:28px"><a class="pa-btn pa-btn--chiaro" href="https://www.produttoriarborea.it/contatti/">Contattaci</a></p>
  </div>
</section>

'''
(SITO / "rossopregio-punti-vendita.html").write_text(testa + corpo + coda, encoding="utf-8")
print("ok:", len(widget) // 1024, "KB widget,", len(punti), "punti", "(DI ESEMPIO)" if DI_ESEMPIO else "")
