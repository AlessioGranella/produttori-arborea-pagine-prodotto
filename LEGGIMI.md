# Pagine prodotto Primoverde e Meridoro

Due pagine statiche che fanno da **modello esecutivo** per la ricostruzione in
Elementor su produttoriarborea.it.

- `primoverde-prodotti.html` — i prodotti Primoverde (linea del fresco + quarta gamma)
- `meridoro-prodotti.html` — il catalogo del Mangimificio Meridoro

Si aprono a doppio clic, senza server. Tutto ci&ograve; che serve sta in `assets/`.

---

## Regola di costruzione

Ogni blocco delle due pagine corrisponde a un **widget Elementor nativo**. Non ci sono
componenti su misura, filtri JavaScript, drawer o comparatori: si ricostruisce tutto
dall&rsquo;editor, senza plugin aggiuntivi.

| Blocco nelle pagine | Widget Elementor |
|---|---|
| `section.pa-hero` / `.pa-due` | Contenitore a 2 colonne + Titolo + Editor di testo + Immagine + Pulsante |
| `.pa-chip` | Editor di testo con sfondo e bordo arrotondato (o widget Titolo con stile) |
| `.pa-numeri` | 4 widget **Contatore** in un contenitore a 4 colonne |
| `.pa-griglia` + `.pa-scheda` | Contenitore con griglia + widget **Image box** (immagine circolare, titolo, descrizione) |
| `.pa-scheda__mix` | Icon list orizzontale, oppure testo con tag `<li>` stilizzati |
| `.pa-passi` | 4 widget **Icon box** in riga |
| `.pa-acc` (`<details>`) | Widget **Fisarmonica**: un elemento per prodotto |
| `.pa-dati` dentro la fisarmonica | Contenitore a 3 colonne con **Icon list** (valori, ingredienti, formati) |
| `.pa-formati` | Widget **Image box** in griglia |
| `.pa-pdv` | Contenitore a griglia con **Icon list** (uno per punto vendita) |
| `.pa-scarica` | Widget **Pulsante** con icona, link al PDF caricato in Media |
| Header e footer | **Non vanno ricostruiti**: sono i template header/footer gi&agrave; in linea. Qui sono replicati solo per far vedere la pagina intera. |

### Nota sulla fisarmonica
Il titolo di ogni elemento contiene immagine + nome + sottotitolo. In Elementor il widget
Fisarmonica accetta solo testo nel titolo: si risolve usando un **contenitore per ogni
prodotto** con Image box + Toggle, oppure abilitando il titolo HTML della Fisarmonica.
Se si preferisce la strada pi&ugrave; semplice, basta mettere l&rsquo;immagine dentro il corpo
dell&rsquo;elemento e lasciare nel titolo solo nome e sottotitolo.

---

## Stile

`assets/pa.css` riprende i token del sito live (kit Elementor 1101) e del brandbook:

- **Colori** — campagna `#004928`, carne `#8D1926`, ferro `#535A60`, foglia `#95C11F`,
  arancio `#F18700`, oro `#D7B46A`, oro scuro `#957C46`, pomodoro `#D20A11`,
  sabbia `#FFF7F1`, argento `#B6C0C6`, legno `#3A2828`, notte `#000E1E`.
  **Il fondo pagina &egrave; sabbia, non bianco.**
- **Caratteri** — Fredoka per i titoli e la navigazione (18px, peso 400),
  Roboto Flex per il testo. Sono gli stessi che il sito carica da Google Fonts.
- **Pulsanti** — maiuscolo, peso 700, bordo 3px, raggio 50px: come il kit del sito.
- **Contenitore** — 1140px, come il kit del sito.

---

## Da dove vengono i contenuti

### Primoverde
Cataloghi **&laquo;Linea del fresco&raquo;** e **&laquo;Quarta gamma&raquo;** del 16 marzo 2026
(`../Asset/PRIMOVERDE - *.pdf`). Descrizioni trascritte alla lettera.
I testi della filiera corta e della sostenibilit&agrave; vengono dalla pagina Primoverde
gi&agrave; in linea.

- I **pack** sono i mockup ufficiali scontornati della cartella `PRIMOVERDE (2)`,
  rifilati sull&rsquo;ingombro effettivo e portati a 600&times;600 px trasparenti
  (`assets/img/pv-*.png`). Stanno liberi sulla scheda, senza cerchio e senza bordo,
  cos&igrave; non vengono mai tagliati.
- **Insalata saporita** &egrave; l&rsquo;unico prodotto senza mockup: usa l&rsquo;illustrazione del
  design system. Quando arriver&agrave; il pack, basta sostituire l&rsquo;immagine e togliere la
  classe `pa-scheda__figura--ill`.
- Nella cartella dei mockup ci sono anche **patate rosse**, **patate novelle inverno**
  e **anguria sugar**, che il catalogo non elenca come prodotti a s&eacute;: non sono in
  pagina, si aggiungono quando serve.

### Meridoro
Cataloghi **Bovini, Ovini, Caprini, Equini e Biologico** (`../Asset/MERIDORO *.pdf`).
Denominazioni, valori nutrizionali, ingredienti, formati e dosi sono trascritti dai PDF.
I PDF sono immagini appiattite, senza testo selezionabile: la trascrizione &egrave; stata
fatta a vista, quindi **va ricontrollata dal cliente prima della pubblicazione**, in
particolare sulle percentuali.

- I **cerchi con il primo piano del mangime** e le **foto degli animali** sono ritagliati
  dalle schede dei cataloghi, che hanno un impaginato fisso.
- I **pack** sono i mockup ufficiali della cartella `Meridoro Mockup Sacchi`
  (ridotti per il web in `assets/img/pack-*.jpg`). Sono mockup, non fotografie di
  prodotto: vanno usati come tali.
- La **curva di lattazione** (`assets/img/md-curva-lattazione.svg`) &egrave; ridisegnata dal
  grafico di pagina 16 del catalogo Ovini. In Elementor si carica come immagine.
- Punti vendita e recapiti vengono dalla pagina Meridoro gi&agrave; in linea e dalla pagina
  di contatto dei cataloghi.

---

## Le brochure scaricabili

Ogni categoria ha il pulsante **Scarica la brochure**, che punta al catalogo di quella
sezione in `assets/brochure/`. Sono i PDF originali **ricompressi per il web**
(pagine a 150 dpi, JPEG qualit&agrave; 80): da 130 MB complessivi a 16 MB, restando
perfettamente leggibili. Gli originali non sono stati toccati e restano in `../Asset/`.

| Pulsante | File | Peso |
|---|---|---|
| Primoverde &middot; Linea del fresco | `primoverde-linea-del-fresco.pdf` | 2,5 MB |
| Primoverde &middot; Quarta gamma | `primoverde-quarta-gamma.pdf` | 1,9 MB |
| Meridoro &middot; Bovini | `meridoro-bovini.pdf` | 2,8 MB |
| Meridoro &middot; Ovini | `meridoro-ovini.pdf` | 3,2 MB |
| Meridoro &middot; Caprini | `meridoro-caprini.pdf` | 2,9 MB |
| Meridoro &middot; Equini | `meridoro-equini.pdf` | 1,3 MB |
| Meridoro &middot; Biologico | `meridoro-biologico.pdf` | 1,5 MB |

In Elementor si caricano in Libreria media e si collegano al pulsante.
La sezione &laquo;Insilati e materie prime&raquo; non ha un pulsante: quei contenuti stanno
dentro i cataloghi Bovini e Ovini, non hanno una brochure propria.

---

## Punti aperti

1. **Verifica dei dati tecnici Meridoro** con il mangimificio (valori, formati, dosi).
2. **HumiFEED Asciutta** compare identico nel catalogo Bovini e in quello Ovini: qui
   &egrave; una scheda sola, nella sezione Bovini. Da decidere se duplicarla anche fra
   ovini e caprini.
3. **Pack di Insalata saporita** Primoverde: manca il mockup.
4. **Ortueri** &egrave; l&rsquo;unico punto vendita senza telefono ed e-mail nelle fonti.
5. Il numero **&laquo;oltre 160.000 capi alimentati con FiberFeed&raquo;** sta sulla pagina
   FiberFEED in linea: non &egrave; stato ripreso qui, ma si pu&ograve; aggiungere ai contatori.

---

## Struttura della cartella

```
sito/
├─ primoverde-prodotti.html
├─ meridoro-prodotti.html
├─ LEGGIMI.md
└─ assets/
   ├─ pa.css                      stile delle due pagine
   ├─ pa.js                       solo menu e «torna su» (in produzione non serve:
   │                              li gestisce il tema)
   ├─ img/                        foto e pack pronti per il web
   ├─ brochure/                   i PDF scaricabili, alleggeriti per il web
   ├─ ill/                        illustrazioni del design system
   ├─ PRIMOVERDE (2)/             i mockup originali dei prodotti Primoverde (sorgenti)
   ├─ loghi/                      loghi ufficiali
   └─ Meridoro Mockup Sacchi/     i mockup originali del cliente (sorgenti, PSD compresi)
```

---

# Trova il punto vendita (Meridoro)

`punti-vendita.html` — mappa dei punti vendita agro-zootecnici con ricerca per comune,
«Vicino a me», filtro per provincia, distanze e pulsante «Indicazioni» (apre Google Maps).

**Questa è l'unica eccezione alla regola «solo widget nativi»**: una mappa con ricerca non
si fa con i widget di Elementor. È un blocco unico autosufficiente, al posto di un plugin
come Agile Store Locator (Pro da $49/anno).

## Come si mette in Elementor
1. Aprire la pagina in Elementor, aggiungere un widget **HTML**.
2. Incollare **tutto** il contenuto di `elementor/widget-punti-vendita.html`.
3. Salvare. Non serve nessun plugin né chiave API.

Il blocco porta con sé CSS (classi `pv-*`, token propri) e JavaScript. Usa
**Leaflet 1.9.4** da cdnjs e le mappe **OpenStreetMap** (gratuite, con attribuzione).
I caratteri Fredoka e Roboto Flex li carica già il sito.

## Come si aggiornano i punti vendita
I dati stanno nell'elenco `PUNTI` in `src/widget-punti-vendita.html`. Dopo la modifica:

    python3 src/build-punti-vendita.py

rigenera sia `elementor/widget-punti-vendita.html` sia la pagina di anteprima. Poi si
ri-incolla il blocco nel widget HTML.

## Da dove vengono i dati
- **Indirizzi, telefoni, email**: pagina Meridoro di produttoriarborea.it (11/11/2026).
- **Pattada**: c'è nel Report di Sostenibilità ma non sul sito, mancano indirizzo e
  contatti. In pagina compare con la nota «Indirizzo e contatti in aggiornamento».
  **Ortueri** non c'è più (sostituito da Pattada, 04/11/2026).
- **Coordinate**: OpenStreetMap (Nominatim). Precise sulla via o località per Arborea,
  Guspini, Dolianova, Suni, Bolotana (zona industriale di Ottana); sul centro del
  comune per Bassacutena, Muros, Thiesi, Pattada, Fonni, Domusnovas. **Lula** è stata
  agganciata a «Riu Sologo»: va verificata. Prima di pubblicare conviene chiedere al
  cliente le coordinate esatte (basta un link Google Maps per punto vendita).
- **Comuni per la ricerca**: i 377 comuni sardi con il centro geografico, calcolato dai
  confini ISTAT di openpolis (`src/comuni-sardegna.json`). La ricerca non usa servizi
  esterni; il CAP non è supportato.
