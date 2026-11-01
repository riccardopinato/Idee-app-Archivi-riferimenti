# CAP-0019 — Store media content addressed e GC: compatibilità Anna's Diary

**Categoria:** `EXISTING_SOURCE` — Presenza di sorgenti coerenti; non equivale a CI/device certificati.

- **Target esaminato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`, Flutter `1.0.0-rc.6+117`.
- **Fonte nell'app:** [`lib/media_asset_store.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/media_asset_store.dart).
- **Osservazione dai sorgenti:** MediaAssetStore gestisce media content-addressed e riferimenti.
- **Score prodotto:** 81/100 (non indica compatibilità).
- **Facilità integrazione Anna:** **65%** (precedente 65%); stima editoriale, non probabilità misurata.
- **Evidence ladder attuale nel catalogo:** `SOURCE_REPORTED` — stato NON promosso in questo audit.

## Contratto di riuso

Presenza di sorgenti coerenti; non equivale a CI/device certificati. Preservare Product Bible e roadmap: niente database o flusso di sincronizzazione parallelo, AI obbligatoria, condivisione implicita o nuova feature fuori scope.

**Sviluppo da fare/validare:** Non uniformare database privacy separati

**Approccio raccomandato:** riutilizzare il file `lib/media_asset_store.dart` e i modelli/stores canonici dell'app target dopo una verifica al commit esatto. Qualora il codice sorgente esistente copra già la funzione, dedicare il lavoro a QA/regressioni anziché reimplementarla. Le capability dichiarate `OUT_OF_SCOPE` restano archiviate solo come opzioni, non come approvazione.

## Test ed evidenze ancora mancanti

- Verifica documentale del file nel repository Anna: **eseguita**.
- Test unitari/Flutter dedicati a questa singola CAP in questo audit: **non eseguiti**.
- Build APK Android del nuovo codice: **non eseguita**.
- Installazione/collaudo fisico: **non verificati**.
- Qualunque nuova dipendenza/modello donor: **non copiati**, licenza/commit da verificare prima del riuso.

Le evidenze passate di test per alcune capability (p.es. parser, slot, kit Dart autonomi) non devono essere attribuite automaticamente a una build app o a tutte le 61 capability. [Registro capability](../../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json).
