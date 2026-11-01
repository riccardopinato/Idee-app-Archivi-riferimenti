# CAP-0005 — Esportazione esplicita eventi verso calendario: compatibilità Anna's Diary

**Categoria:** `PARTIAL_REUSE` — Esiste un fondamento riusabile, non la capability completa.

- **Target esaminato:** `riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2`, Flutter `1.0.0-rc.6+117`.
- **Fonte nell'app:** [`lib/src/android_calendar_sync.dart`](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/android_calendar_sync.dart).
- **Osservazione dai sorgenti:** Sync/export Android Calendar Provider presente, ma non esportazione generica cross-platform.
- **Score prodotto:** 87/100 (non indica compatibilità).
- **Facilità integrazione Anna:** **75%** (precedente 85%); stima editoriale, non probabilità misurata.
- **Evidence ladder attuale nel catalogo:** `ROADMAP_STORICA` — stato NON promosso in questo audit.

## Contratto di riuso

Esiste un fondamento riusabile, non la capability completa. Preservare Product Bible e roadmap: niente database o flusso di sincronizzazione parallelo, AI obbligatoria, condivisione implicita o nuova feature fuori scope.

**Sviluppo da fare/validare:** Verificare provider permessi e intent senza sync bidirezionale

**Approccio raccomandato:** riutilizzare il file `lib/src/android_calendar_sync.dart` e i modelli/stores canonici dell'app target dopo una verifica al commit esatto. Qualora il codice sorgente esistente copra già la funzione, dedicare il lavoro a QA/regressioni anziché reimplementarla. Le capability dichiarate `OUT_OF_SCOPE` restano archiviate solo come opzioni, non come approvazione.

## Test ed evidenze ancora mancanti

- Verifica documentale del file nel repository Anna: **eseguita**.
- Test unitari/Flutter dedicati a questa singola CAP in questo audit: **non eseguiti**.
- Build APK Android del nuovo codice: **non eseguita**.
- Installazione/collaudo fisico: **non verificati**.
- Qualunque nuova dipendenza/modello donor: **non copiati**, licenza/commit da verificare prima del riuso.

Le evidenze passate di test per alcune capability (p.es. parser, slot, kit Dart autonomi) non devono essere attribuite automaticamente a una build app o a tutte le 61 capability. [Registro capability](../../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json).
