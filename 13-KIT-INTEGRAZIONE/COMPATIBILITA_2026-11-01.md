# Audit compatibilita kit 01/11/2026 — CAP-0134, CAP-0114, CAP-0138

**Factory baseline:** `riccardopinato/App-Factory-Core@63dd5e4f703cb23e4095a72beb253720bc1ca9a1` (Master v27).

**Target verificato (solo in lettura):** `riccardopinato/Notes-Ecosistema@3fd9b0df5ab3b7470c65721b4bad7f3fd8c59e6c` — `flutter_app/pubspec.yaml`: Flutter port 0.56.3+74 e Dart SDK `>=3.4.0 <4.0.0`, Riverpod, `google_mlkit_document_scanner`, `google_mlkit_text_recognition`, `record`, `sqflite` e `crypto`. Nessuna libreria ONNX nel pubspec osservato.

## Evidence ladder delle prove

| Livello | CAP-0134 DocRex | CAP-0114 Privacy | CAP-0138 Ink |
|---|---|---|---|
| Fonte esterna consultata | Model card/README, labels, preprocessing, metriche pubblicate | Model/Space Redact e condizioni licenza `other` | Model card MOSS solo riferimento facoltativo |
| Contratti nel repo Notes osservati | `domain/documents.dart`, `domain/attachments.dart`, `data/document_store.dart`, `state/document_controller.dart` | `domain/attachments.dart`, `domain/documents.dart` | `domain/visual_documents.dart` (`InkStroke.id`), `screens/whiteboard_screen.dart`, `screens/editor_screen.dart` (`AudioRecorder`) |
| Codice originale in kit | Crop/normalize RGB e softmax + preview | Parser email/IBAN e copia mascherata *parziale* | Codec/versioning e indicizzazione stroke/audio |
| Test Dart standalone | [Test](CAP-0134/test/document_triage_test.dart) | [Test](CAP-0114/test/privacy_preview_test.dart) | [Test](CAP-0138/test/audio_ink_index_test.dart) |
| Modello originale eseguito | **NO** | **NO** | **NO** (non serve al contratto) |
| Flutter build / app integration | **NON VERIFICATO** | **NON VERIFICATO** | **NON VERIFICATO** |
| Android fisico / sicurezza | **NON VERIFICATO** | **NON VERIFICATO** | **NON VERIFICATO** |

Test CLI per codice Dart puro, senza nuovi pacchetti: [workflow GitHub](../.github/workflows/kit-dart-compat.yml) con `dart analyze` e `dart path/test.dart`. **Un check verde certifica solo i contratti e gli errori rilevati nei test, non il prodotto completo.**

## Ricalibrazione percentuali

| Kit | App | Prima | Dopo | Ragione |
|---|---|---:|---:|---|
| CAP-0134 | Notes-Ecosistema | 95% | **70%** | Necessario ONNX FP32 + decoding raster/PDF, assente nel progetto |
| CAP-0134 | Agenda-per-Anna | 85% | **55%** | Solo consumer candidato, provider documenti e limiti da verificare |
| CAP-0134 | PDF-Unifier | 95% | **65%** | Dipende da rendering PDF e nuovo runtime; repo non auditato in profondita qui |
| CAP-0114 | Notes-Ecosistema | 80% | **55%** | Parser limitato e mancano sanitizzazione media/export sicuro |
| CAP-0114 | Agenda-per-Anna | 80% | **45%** | Dati privati e scope UX/permessi da valutare |
| CAP-0114 | PDF-Unifier | 75% | **40%** | La redazione sicura PDF e piu complessa di una sostituzione testuale |
| CAP-0138 | Notes-Ecosistema | 85% | **65%** | Stroke IDs presenti ma mancano UI sincronizzata, clock, storage e backup |

Percentuali **euristiche**, non probabilita misurate; Anna/PDF stimate in modo conservativo ma senza audit esatto del loro codice in questa tranche.

## Fonte originale, licenze e blocchi

- [DocRex](https://huggingface.co/vivekkaushal/DocRex): modello FP32 6.084.524 byte, 3 categorie, input 224 NCHW, dichiarazione Apache-2.0 e SHA256 `bbe9997671953145206939291c592dc937c6c523202234bba66e8a589cc643db`; nessun binario scaricato, hash **non ricalcolato**. Il 98.35% e misura donor su 243 immagini, non prova sui dati italiani. INT8 donor 58.85%, non consigliato.
- [Redact model](https://huggingface.co/desert-ant-labs/redact) e [Space](https://huggingface.co/spaces/desert-ant-labs/redact-demo/blob/main/README.md): SDK Kotlin esistente, demo client-side. Licenza `other`/condizioni commerciali specifiche; **nessun codice o peso esterno riutilizzato**. Il parser originale sviluppato qui NON garantisce assenza residua di dati identificativi.
- [MOSS Transcribe-Diarize](https://huggingface.co/OpenMOSS-Team/MOSS-Transcribe-Diarize): modello 0.9B Apache-2.0 per ASR/diarizzazione; non e necessario per l'associazione temporale deterministica. Nessun download.
- [flutter_onnxruntime](https://pub.dev/packages/flutter_onnxruntime): plugin candidato per valutazione, non incluso; la documentazione elenca requisiti Android e minimi iOS, non una prova di compatibilita con Notes.

**Provenance:** tutto il nuovo Dart e implementazione originale `NEW_IMPLEMENTATION` basata su requisiti pubblicati; codice donor copiato = zero, licenze OSS non promosse.

## Prossimi gate (non automatizzabili dal solo archivio)

1. Integrare un singolo kit in branch protetto di Notes dopo controllo Product Bible e roadmap: prima CAP-0138 (nessun modello) oppure CAP-0134 (runtime nuovo), con test Flutter reali.
2. CAP-0134: verificare binary SHA a commit modello esatto, usare fp32, benchmark immagini italiane con classi bilanciate, memoria e dimensioni APK; evitare classificazione automatica `other`.
3. CAP-0114: definire export realmente sanitizzato e test recupero testo/metadata, PII multilingue, audit sicurezza; non promuovere parser parziale.
4. CAP-0138: event stream a clock monotono con `record`, sidecar versionato incluso in backup/sync e lifecycle delete/undo, validazione fisica.
5. Mantenere stati app `PROPOSTA` finche il codice non sia nel repo app e verificato sul commit dichiarato.

**Nota test:** il risultato effettivo dei check Dart e quello della PR/CI; questo documento non simula un test gia passato.
