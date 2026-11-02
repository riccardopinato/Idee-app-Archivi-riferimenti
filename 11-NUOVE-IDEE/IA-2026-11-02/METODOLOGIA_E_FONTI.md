# Metodologia, provenienza e fonti — lotto IA 02/11/2026

## Autorità e limiti
**Source of truth del progetto:** App-Factory-Core `CURRENT.yaml`: Master v27, Golden Index v23. Il repository idee è archivio/ricerca, non il codice delle app. Rispetto del lifecycle `PROPOSTA → ANALISI → VALIDAZIONE → APPROVATA/RINVIATA/SCARTATA`. Le 100 idee sono tutte **IDEA / ANALISI NON APPROVATA**. Nessuna promozione automatica in `01-PORTAFOGLIO`.

**Fonte primaria:** conversazione con un'altra IA consegnata dall'utente il 02/11/2026. I primi #1–#23 sono ripresi da `Markdown incollato (2)(1).md` (SHA256 `afc37b59d4849cf83808606b8394d4426cbc053a9412e907d252afdf6585e2ab`); #24–#100 da `Testo incollato (3)(1).txt` (SHA256 `eb3c600cd834b2c338fa66d7c6903f1a05b17c3eaedbad557acd7fb4c4963e5c`); fusioni finali da `Testo incollato (4)(1).txt` (SHA256 `8187ecdc187db919601a19baed13d4d1906abbee3c702681b66051b3db0560c4`). Altre proposte senza numeri, scambi sui Ghost WiFi e articoli sono conservati nella conversazione originaria. Il repository contiene riassunti critici, non copia integrale degli allegati originali.

## Valutazione per ogni idea
- **U (utilità)**: intensità del bisogno, 1–10.
- **D (domanda ipotizzata)**: ampiezza raggiungibile del problema, non volumi ASO verificati, 1–10.
- **V (viralità)**: probabilità qualitativa di uso condivisibile; non fattore K misurato, 1–10.
- **M (monetizzabilità)**: ipotesi sulla disponibilità a pagare/mercato, non ricavi, 1–10.
- **F (facilità)**: un MVP pubblicabile con Codex e test device, NON la brevità del codice, 1–10.
- **S (sinergia)**: riuso dei prodotti/Golden esistenti o maggiore fit Factory, 1–10.
- **R (rischio)**: API/permissi, dati, safety, licenze, privacy/ToS, maggiore = peggio, 1–10.

**Score (0–100):** `round(2.4U + 2D + 1.2V + 1.8M + 1.6F + S - 2×max(0,R-5))`, clamp 0–100. Differisce dallo score storico dei prodotti già in codice: **non confrontare i due ordinamenti come se fossero la stessa metrica**. Le classifiche sono viste derivate dalla stessa matrice di 100 record; non aggiungere ID app nuovi senza controllo collisione.

## Legenda decisioni
- **S** candidata standalone; **F** feature-first verso app esistente; **C** fusione candidata; **R** riprogettare promessa; **H** rinviare finché gate bloccante; **B** valida solo come business B2B candidato. Un'app esistente citata è **correlazione da verificare**, non feature implementata.

## Fonti esterne effettivamente consultate
- [Google Play — policy subscriptions](https://support.google.com/googleplay/android-developer/answer/18265346): l'abbonamento richiede valore continuativo.
- [Android — Wi-Fi scanning](https://developer.android.com/develop/connectivity/wifi/wifi-scan): throttling e permessi.
- [Android — privacy e clipboard](https://developer.android.com/about/versions/10/privacy/changes): limitazioni accesso clipboard da altre app.
- [Android — full-screen intents](https://source.android.com/docs/core/permissions/fsi-limits): limitazioni per false chiamate.
- [Plugin connectivity_plus](https://pub.dev/packages/connectivity_plus): tipi di connessione, non scansione access point.
- [home_widget](https://pub.dev/packages/home_widget): Flutter necessita configurazioni widget native.
- [Open Food Facts Dart](https://github.com/openfoodfacts/openfoodfacts-dart): API wrapper; dati alimentari non garantiscono copertura/accuratezza per allergie.
- [flutter_map](https://pub.dev/packages/flutter_map), [mobile_scanner](https://pub.dev/packages/mobile_scanner), [supabase_flutter](https://pub.dev/packages/supabase_flutter), [speech_to_text](https://pub.dev/documentation/speech_to_text/latest/), [flutter_local_notifications](https://pub.dev/packages/flutter_local_notifications): fonti package, NON licenza/compatibilità commerciale certificata per ogni idea.

**Non verificato:** concorrenza completa per 100 idee, trend reali, recensioni App Store, tutti i repository OSS/problemi licensing, dati di conversione, test fisici, costi cloud e fatturato. Un nome di libreria suggerito dall'altra IA non è un link verificato né autorizzazione a copiare codice.
