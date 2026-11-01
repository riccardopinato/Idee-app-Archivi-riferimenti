# CAP-0123 — Lettura bilingue sincronizzata di note e PDF: compatibilità Anna's Diary

**Categoria:** `OUT_OF_SCOPE` — Non integrare senza nuova decisione del Product Bible.

- **Target esaminato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`, Flutter `1.0.0-rc.6+117`.
- **Fonte nell'app:** [`lib/src/localization.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/localization.dart).
- **Osservazione dai sorgenti:** UI multilingue non equivale a reader PDF bilingue; meglio Notes/PDF-Unifier.
- **Score prodotto:** 74/100 (non indica compatibilità).
- **Facilità integrazione Anna:** **25%** (precedente 60%); stima editoriale, non probabilità misurata.
- **Evidence ladder attuale nel catalogo:** `PROPOSTA` — stato NON promosso in questo audit.

## Contratto di riuso

Non integrare senza nuova decisione del Product Bible. Preservare Product Bible e roadmap: niente database o flusso di sincronizzazione parallelo, AI obbligatoria, condivisione implicita o nuova feature fuori scope.

**Sviluppo da fare/validare:** Il donor traduce PDF con pipeline e servizi esterni; niente invio implicito di documenti privati; licenza, quote e uso commerciale da verificare. Verificare architettura e licensing nel Product Bible prima di integrare.

**Approccio raccomandato:** riutilizzare il file `lib/src/localization.dart` e i modelli/stores canonici dell'app target dopo una verifica al commit esatto. Qualora il codice sorgente esistente copra già la funzione, dedicare il lavoro a QA/regressioni anziché reimplementarla. Le capability dichiarate `OUT_OF_SCOPE` restano archiviate solo come opzioni, non come approvazione.

## Test ed evidenze ancora mancanti

- Verifica documentale del file nel repository Anna: **eseguita**.
- Test unitari/Flutter dedicati a questa singola CAP in questo audit: **non eseguiti**.
- Build APK Android del nuovo codice: **non eseguita**.
- Installazione/collaudo fisico: **non verificati**.
- Qualunque nuova dipendenza/modello donor: **non copiati**, licenza/commit da verificare prima del riuso.

Le evidenze passate di test per alcune capability (p.es. parser, slot, kit Dart autonomi) non devono essere attribuite automaticamente a una build app o a tutte le 61 capability. [Registro capability](../../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json).
