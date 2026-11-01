# CAP-0003 — Preparazione contestuale appuntamento: compatibilità Anna's Diary

**Categoria:** `EXISTING_SOURCE` — Presenza di sorgenti coerenti; non equivale a CI/device certificati.

- **Target esaminato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`, Flutter `1.0.0-rc.6+117`.
- **Fonte nell'app:** [`lib/src/event_preparation.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/event_preparation.dart).
- **Osservazione dai sorgenti:** EventPreparationDraft e saveEventPreparation gestiscono note/checklist per appuntamento.
- **Score prodotto:** 81/100 (non indica compatibilità).
- **Facilità integrazione Anna:** **95%** (precedente 95%); stima editoriale, non probabilità misurata.
- **Evidence ladder attuale nel catalogo:** `SOURCE_CONFIRMED` — stato NON promosso in questo audit.

## Contratto di riuso

Presenza di sorgenti coerenti; non equivale a CI/device certificati. Preservare Product Bible e roadmap: niente database o flusso di sincronizzazione parallelo, AI obbligatoria, condivisione implicita o nuova feature fuori scope.

**Sviluppo da fare/validare:** Collaudo fisico +116 V116-06…V116-10 e V116-12: note, checklist, conflitti, Trash, offline e lingue; CI e APK firmato non equivalgono a DEVICE_PASS.

**Approccio raccomandato:** riutilizzare il file `lib/src/event_preparation.dart` e i modelli/stores canonici dell'app target dopo una verifica al commit esatto. Qualora il codice sorgente esistente copra già la funzione, dedicare il lavoro a QA/regressioni anziché reimplementarla. Le capability dichiarate `OUT_OF_SCOPE` restano archiviate solo come opzioni, non come approvazione.

## Test ed evidenze ancora mancanti

- Verifica documentale del file nel repository Anna: **eseguita**.
- Test unitari/Flutter dedicati a questa singola CAP in questo audit: **non eseguiti**.
- Build APK Android del nuovo codice: **non eseguita**.
- Installazione/collaudo fisico: **non verificati**.
- Qualunque nuova dipendenza/modello donor: **non copiati**, licenza/commit da verificare prima del riuso.

Le evidenze passate di test per alcune capability (p.es. parser, slot, kit Dart autonomi) non devono essere attribuite automaticamente a una build app o a tutte le 61 capability. [Registro capability](../../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json).
