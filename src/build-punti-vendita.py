"""Monta il widget «Trova il punto vendita».

Uscite:
  elementor/widget-punti-vendita.html  -> da incollare nel widget HTML di Elementor
  punti-vendita.html                   -> anteprima con nav e footer del sito

Uso:  python3 src/build-punti-vendita.py   (dalla cartella sito/)
"""
from pathlib import Path

SITO = Path(__file__).resolve().parent.parent
src = (SITO / "src/widget-punti-vendita.html").read_text(encoding="utf-8")
comuni = (SITO / "src/comuni-sardegna.json").read_text(encoding="utf-8").strip()
widget = src.replace("/*COMUNI*/[]", comuni)

(SITO / "elementor").mkdir(exist_ok=True)
(SITO / "elementor/widget-punti-vendita.html").write_text(widget, encoding="utf-8")

# nav e footer: gli stessi della pagina prodotti Meridoro (replica del sito live)
base = (SITO / "meridoro-prodotti.html").read_text(encoding="utf-8")
testa = base[: base.index('<main id="contenuto">')]
coda = base[base.index("</main>"):]

testa = (testa
  .replace("<title>I prodotti Meridoro &mdash; Produttori Arborea</title>",
           "<title>Punti vendita Meridoro &mdash; Produttori Arborea</title>")
  .replace(testa[testa.index('<meta name="description"'):testa.index('>', testa.index('<meta name="description"')) + 1],
           '<meta name="description" content="Trova il punto vendita agro-zootecnico Meridoro più vicino: mangimi, sementi, concimi in tutta la Sardegna.">'))

corpo = f'''<main id="contenuto">

<!-- ====== 1. INTESTAZIONE · contenitore + titolo + testo =============== -->
<section class="pa-hero" style="padding-bottom:clamp(24px,3vw,36px)">
  <div class="container">
    <p class="pa-hero__briciole">
      <a href="https://www.produttoriarborea.it/">Home</a> &nbsp;/&nbsp;
      <a href="https://www.produttoriarborea.it/meridoro/">Meridoro</a> &nbsp;/&nbsp; Punti vendita
    </p>
    <div class="pa-lockup">
      <img class="pa-lockup__marchio" src="assets/loghi/meridoro.svg" alt="Meridoro">
    </div>
    <h1>Trova il punto vendita pi&ugrave; vicino</h1>
    <p class="testo-largo">
      Puoi visitare uno dei nostri punti vendita agro-zootecnici, in Sardegna, per scoprire
      la gamma completa di prodotti e servizi. Trova il punto vendita pi&ugrave; vicino o
      contattaci direttamente per maggiori informazioni.
    </p>
  </div>
</section>

<!-- ====== 2. TROVA IL PUNTO VENDITA · widget HTML di Elementor ========= -->
<section class="fascia" style="padding-top:0">
  <div class="container">
<!-- INIZIO WIDGET HTML ELEMENTOR -->
{widget}
<!-- FINE WIDGET HTML ELEMENTOR -->
  </div>
</section>

<!-- ====== 3. CONTATTI ================================================ -->
<section class="fascia fascia--scura" id="contatti">
  <div class="container centrato">
    <h2>Ufficio commerciale del Mangimificio</h2>
    <p class="testo-largo">Puoi rivolgerti al nostro ufficio commerciale per ordinare e avere maggiori informazioni.</p>
    <p style="font-size:1.15rem;line-height:2">
      <a href="tel:+3907831818087">0783 1818087</a> &nbsp;&middot;&nbsp;
      <a href="https://wa.me/393467902333">Whatsapp 346 7902333</a><br>
      <a href="mailto:mangimificio@produttoriarborea.it">mangimificio@produttoriarborea.it</a>
    </p>
  </div>
</section>

'''
(SITO / "punti-vendita.html").write_text(testa + corpo + coda, encoding="utf-8")
print("ok:", len(widget) // 1024, "KB widget")
