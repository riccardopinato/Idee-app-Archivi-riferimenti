# Ricerca Hugging Face Notes — quarta raccolta #45–56 (conservazione integrale)

- **Data:** 2026-11-01
- **Factory baseline:** `riccardopinato/App-Factory-Core@63dd5e4f703cb23e4095a72beb253720bc1ca9a1`, Master v27.
- **Fonte di partenza:** https://huggingface.co/search/full-text?q=to+do; l'elenco dinamico non e esaustivo.
- **Stato:** sola ricerca e archivio; no implementazioni, donorship o roadmap approvate.
- **Collegamenti:** [idee #29–44](RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md) e ricerche precedenti.
- **Nota sulle capability:** #45 Notes to Slides e #55 Scientific Figure Studio condividono `CAP-0130`: due prodotti/uscite differenti ma lo stesso motore documenti -> artefatti editabili; entrambe le idee restano con schede fonte distinte in questa nota.

## Inventario completo

| Idea # | Nome | Proposta conservata | Score idea | Capability canonica | Riferimenti |
|---|---|---|---|---|---|
| 45 | **Notes to Slides** | Trasforma note selezionate in slide con titoli e impaginazione modificabili, esportando senza alterare le note. | 9,8/10 | [CAP-0130](REGISTRO_CAPABILITY/CAP-0130.md) | [paper2any](https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md) |
| 46 | **Math Ink** | Riconosce formule manoscritte o fotografate e le converte in LaTeX modificabile e verificabile. | 9,7/10 | [CAP-0131](REGISTRO_CAPABILITY/CAP-0131.md) | [math](https://huggingface.co/inYourOwnBrowser/rapid-latex-ocr-onnx) |
| 47 | **Soundscape Journal** | Associa registrazioni di suoni non verbali e suggerimenti di etichette a note e ricordi. | 9,6/10 | [CAP-0132](REGISTRO_CAPABILITY/CAP-0132.md) | [sound](https://huggingface.co/ShantyCam/audiodet-ced-mini) |
| 48 | **Smart Reading Flow** | Ricostruisce ordine di lettura, titoli e sezioni da PDF a piu colonne conservando geometrie e origine. | 9,6/10 | [CAP-0133](REGISTRO_CAPABILITY/CAP-0133.md) | [reading](https://huggingface.co/docs/transformers/model_doc/pp_doclayout_v3) |
| 49 | **Document Auto-Sorter** | Classifica documenti importati e propone destinazione senza spostarli automaticamente. | 9,5/10 | [CAP-0134](REGISTRO_CAPABILITY/CAP-0134.md) | [sorter](https://huggingface.co/vivekkaushal/DocRex) |
| 50 | **Evidence Board** | Per una tesi o affermazione raccoglie fonti a favore/contro, passaggi citati e lacune di prova. | 9,5/10 | [CAP-0135](REGISTRO_CAPABILITY/CAP-0135.md) | [evidence](https://huggingface.co/datasets/TrustworthyComp/ClaimReview2025Q4) |
| 51 | **Smart Cutout Canvas** | Scontorna oggetti da una foto creando sticker/soggetti mobili per composizioni sulla canvas. | 9,4/10 | [CAP-0136](REGISTRO_CAPABILITY/CAP-0136.md) | [cutout](https://huggingface.co/spaces/Xenova/segment-anything-webgpu) |
| 52 | **3D Memory Objects** | Da una foto produce un oggetto 3D ruotabile associato a una nota, con origine media preservata. | 9,3/10 | [CAP-0137](REGISTRO_CAPABILITY/CAP-0137.md) | [threeD](https://huggingface.co/spaces/stabilityai/stable-fast-3d) |
| 53 | **Audio-Linked Ink** | Collega ogni tratto scritto sulla canvas al timestamp della registrazione audio per navigare la lezione. | 9,3/10 | [CAP-0138](REGISTRO_CAPABILITY/CAP-0138.md) | [timestamp](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize) |
| 54 | **Motion Study Notes** | Dai video estrae pose/fotogrammi di un movimento con annotazioni affiancate nella nota. | 9,2/10 | [CAP-0139](REGISTRO_CAPABILITY/CAP-0139.md) | [pose](https://huggingface.co/spaces/animtex/AIMoCap) |
| 55 | **Scientific Figure Studio** | Crea diagrammi scientifici/figure tecniche modificabili partendo da testi e fonti, usando una pipeline visual-export comune a slide. | 9,1/10 | [CAP-0130](REGISTRO_CAPABILITY/CAP-0130.md) | [paper2any](https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md) |
| 56 | **Image Authenticity Inspector** | Visualizza aree potenzialmente manipolate di un'immagine, con incertezza e limiti della classificazione. | 9,0/10 | [CAP-0140](REGISTRO_CAPABILITY/CAP-0140.md) | [forensic](https://huggingface.co/Gertlek/DetectiveSAM) |

## Fonte, limiti e prossimo gate per idea

### 45 — Notes to Slides

- **Stato fonte:** `README_REVIEWED_DEMO_RUNTIME_ERROR` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Trasforma note selezionate in slide con titoli e impaginazione modificabili, esportando senza alterare le note.
- **Riferimenti:** [https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md](https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md).
- **Test e blocchi:** Paper2Any dichiara Paper2PPT e licenza Apache-2.0, ma la demo pubblica era in errore; il backend/AI non va importato automaticamente.
- **Riuso interno da verificare:** CAP-0037; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 46 — Math Ink

- **Stato fonte:** `MODEL_CARD_REVIEWED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Riconosce formule manoscritte o fotografate e le converte in LaTeX modificabile e verificabile.
- **Riferimenti:** [https://huggingface.co/inYourOwnBrowser/rapid-latex-ocr-onnx](https://huggingface.co/inYourOwnBrowser/rapid-latex-ocr-onnx).
- **Test e blocchi:** Re-host MIT di RapidLatexOCR, circa 179 MB ONNX: modello on-demand eventuale, non nell'APK; audit peso e accuratezza.
- **Riuso interno da verificare:** CAP-0035; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 47 — Soundscape Journal

- **Stato fonte:** `MODEL_CARD_REVIEWED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Associa registrazioni di suoni non verbali e suggerimenti di etichette a note e ricordi.
- **Riferimenti:** [https://huggingface.co/ShantyCam/audiodet-ced-mini](https://huggingface.co/ShantyCam/audiodet-ced-mini).
- **Test e blocchi:** AudioDet classifica 17 suoni in dominio specifico; accuratezza universale non dimostrata. Nessuna registrazione senza consenso/azione.
- **Riuso interno da verificare:** CAP-0031; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 48 — Smart Reading Flow

- **Stato fonte:** `OFFICIAL_DOCS_REVIEWED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Ricostruisce ordine di lettura, titoli e sezioni da PDF a piu colonne conservando geometrie e origine.
- **Riferimenti:** [https://huggingface.co/docs/transformers/model_doc/pp_doclayout_v3](https://huggingface.co/docs/transformers/model_doc/pp_doclayout_v3).
- **Test e blocchi:** La doc descrive PP-DocLayoutV3; integrarlo e inferenza/progetto distinto dall'OCR. Controllare supporto linguistico e runtime mobile.
- **Riuso interno da verificare:** CAP-0035; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 49 — Document Auto-Sorter

- **Stato fonte:** `MODEL_CARD_REVIEWED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Classifica documenti importati e propone destinazione senza spostarli automaticamente.
- **Riferimenti:** [https://huggingface.co/vivekkaushal/DocRex](https://huggingface.co/vivekkaushal/DocRex).
- **Test e blocchi:** DocRex Apache-2.0, ~5,8 MB FP32, solo bank_statement/invoice/other, int8 1,7 MB non raccomandato; serve test su documenti italiani.
- **Riuso interno da verificare:** CAP-0075; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 50 — Evidence Board

- **Stato fonte:** `ORIGINAL_LINK_UNCONFIRMED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Per una tesi o affermazione raccoglie fonti a favore/contro, passaggi citati e lacune di prova.
- **Riferimenti:** [https://huggingface.co/datasets/TrustworthyComp/ClaimReview2025Q4](https://huggingface.co/datasets/TrustworthyComp/ClaimReview2025Q4).
- **Test e blocchi:** Dataset ClaimReview2025Q4 non risolto nel controllo: conservare il riferimento originale e cercare alternative verificabili prima di donorship.
- **Riuso interno da verificare:** CAP-0097; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 51 — Smart Cutout Canvas

- **Stato fonte:** `SPACE_PRESENT_DEMO_UNTESTED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Scontorna oggetti da una foto creando sticker/soggetti mobili per composizioni sulla canvas.
- **Riferimenti:** [https://huggingface.co/spaces/Xenova/segment-anything-webgpu](https://huggingface.co/spaces/Xenova/segment-anything-webgpu).
- **Test e blocchi:** Segment Anything WebGPU demo esiste; runtime Android/offline, peso del modello e licenza degli asset da verificare.
- **Riuso interno da verificare:** CAP-0029; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 52 — 3D Memory Objects

- **Stato fonte:** `SPACE_PRESENT_DEMO_UNTESTED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Da una foto produce un oggetto 3D ruotabile associato a una nota, con origine media preservata.
- **Riferimenti:** [https://huggingface.co/spaces/stabilityai/stable-fast-3d](https://huggingface.co/spaces/stabilityai/stable-fast-3d).
- **Test e blocchi:** Stable Fast 3D Space esiste, ma infrastruttura, licenze commerciali e risorse GPU necessitano gate; non promettere offline.
- **Riuso interno da verificare:** CAP-0019; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 53 — Audio-Linked Ink

- **Stato fonte:** `MODEL_CARD_REVIEWED_IDEA_DERIVED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Collega ogni tratto scritto sulla canvas al timestamp della registrazione audio per navigare la lezione.
- **Riferimenti:** [https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize).
- **Test e blocchi:** MOSS supporta ASR con timestamp; la sincronizzazione stroke-audio puo essere deterministica ed e proposta indipendente. Consenso registrazione obbligatorio.
- **Riuso interno da verificare:** CAP-0029, CAP-0031; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 54 — Motion Study Notes

- **Stato fonte:** `SPACE_PRESENT_DEMO_UNTESTED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Dai video estrae pose/fotogrammi di un movimento con annotazioni affiancate nella nota.
- **Riferimenti:** [https://huggingface.co/spaces/animtex/AIMoCap](https://huggingface.co/spaces/animtex/AIMoCap).
- **Test e blocchi:** AIMoCap demo esiste; accuratezza tecnica e scientifica, privacy dei soggetti e permessi video da testare; non diagnosi medica.
- **Riuso interno da verificare:** CAP-0031; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 55 — Scientific Figure Studio

- **Stato fonte:** `README_REVIEWED_DEMO_RUNTIME_ERROR` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Crea diagrammi scientifici/figure tecniche modificabili partendo da testi e fonti, usando una pipeline visual-export comune a slide.
- **Riferimenti:** [https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md](https://huggingface.co/spaces/Viraag/Paper2Any/blob/main/README_EN.md).
- **Test e blocchi:** Paper2Any dichiara Paper2Figure e Paper2PPT nella stessa codebase; registrata come modalita dello stesso CAP di Notes-to-Slides.
- **Riuso interno da verificare:** CAP-0037; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

### 56 — Image Authenticity Inspector

- **Stato fonte:** `MODEL_CARD_REVIEWED_LICENSE_RESTRICTED` — documento/dimostrazione esterna, non test nell'app.
- **Risultato proposto:** Visualizza aree potenzialmente manipolate di un'immagine, con incertezza e limiti della classificazione.
- **Riferimenti:** [https://huggingface.co/Gertlek/DetectiveSAM](https://huggingface.co/Gertlek/DetectiveSAM).
- **Test e blocchi:** DetectiveSAM ha licenza dichiarata other; non importare/copiare senza chiarimento. Le evidenze di manipolazione non certificano originalita o intenzione.
- **Riuso interno da verificare:** CAP-0039; nuovo modulo solo dopo audit codice e conferma di prodotto.
- **Stato prodotto:** `PROPOSTA`, nessuna incorporazione del codice o dei pesi.

## Decisione archivio

- 12 idee distinte conservate, 11 nuove responsabilita capability e una estensione esplicita al motore slide+figure. Nessuna idea persa nel dedup.
- Preferire modello scaricabile opzionale ad asset binari molto pesanti: Tadpole GGUF minimo 529MB + encoder 205MB; Math Ink ONNX circa 179MB. Due riferimenti particolarmente interessanti come confronto, non da bundled APK.
- DocRex modello Apache-2.0 FP32 ~5,8MB e promettente per triage, ma limitato a tre classi; non usare la variante quantizzata INT8 come default dato il calo di accuratezza riportato.
- Paper2Any: README e codice disponibili, Space attualmente con errore di runtime; non confondere progetto documentato con servizio funzionante.
- DetectiveSAM: licenza `other`; vietato trattarlo come risorsa commerciale riusabile senza verifica contrattuale.
- Nessun codice/app repository modificato, nessun release/test fisico inferito.
