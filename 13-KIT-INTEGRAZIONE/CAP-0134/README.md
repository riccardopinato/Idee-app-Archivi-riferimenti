# CAP-0134 — Document Auto-Sorter / DocRex

**Stato: CONTRACT_PROTOTYPE — componenti Dart originali preparati, non integrati in app.**

## Cosa abbiamo estratto dalla fonte reale

- [DocRex model card](https://huggingface.co/vivekkaushal/DocRex), licenza dichiarata Apache-2.0, MobileNetV3-Small, ONNX opset 18, classificazione *solo* `bank_statement` / `invoice` / `other`.
- Input: immagine RGB 256×256, center-crop 224×224, normalizzazione ImageNet, NCHW float32; output `logits` nell'ordine del file `labels.json`.
- Peso dichiarato FP32: 6.084.524 byte; SHA-256 pubblicato nel model card: `bbe9997671953145206939291c592dc937c6c523202234bba66e8a589cc643db`.
- **INT8 NON USARE:** accuratezza pubblicata dal donor 58,85%; 98,35% FP32 e solo sul test set del donor (243 immagini).

## Codice preparato e test

- [lib/document_triage.dart](lib/document_triage.dart): crop/normalizzazione dei byte RGB, softmax stabile, soglia/ambiguita e suggerimento **mai applicato automaticamente**.
- [test/document_triage_test.dart](test/document_triage_test.dart): validazione forma input, normalizzazione per canale, centro, label order, casi `other`, confidenza, logits invalidi.
- [CI Dart](../../.github/workflows/kit-dart-compat.yml) — una PR deve passare il test automatizzato.

**Mancano:** decodifica immagini Flutter/Android, inferenza ONNX nel progetto Notes, modello binario, benchmark dataset italiano, tests Flutter/APK/device. Nessun peso distribuito nel repository.

## Compatibilita con Notes — audit di struttura

App `riccardopinato/Notes-Ecosistema@3fd9b0df5ab3b7470c65721b4bad7f3fd8c59e6c`, Flutter `0.56.3+74`, Dart >=3.4. Esistono `lib/src/domain/attachments.dart`, `lib/src/domain/documents.dart`, `lib/src/data/document_store.dart` e `lib/src/state/document_controller.dart`. Il `pubspec.yaml` **non** include ONNX; il CAP puo essere un motore opzionale che ritorna una preview, non una nuova source of truth. Evitare l'assunzione che il modello gestisca PDF direttamente: convertire **localmente** la pagina in immagine soltanto dopo controllo autorizzazioni/memoria.

[Specifiche](SPECIFICHE.md) · [Provenienza](CODICE_RIFERIMENTO.txt) · [Piano Flutter](INTEGRAZIONE_FLUTTER.md) · [Licenze](LICENZE_E_DIPENDENZE.md) · [Test](TEST_E_VALIDAZIONE.md)

**Per-app ease (dopo audit):** Notes 70%, Anna 55%, PDF-Unifier 65%. Stime revisionate per modello e nuovo runtime, non misure runtime.
