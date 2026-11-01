# CAP-0134 — specifiche estratte: DocRex e contratto candidato

| Voce | Dato verificato sul model card |
|---|---|
| Model | MobileNetV3-Small, ONNX FP32 opset 18 |
|---|---|
| Input | RGB, resize 256×256, center crop 224×224, NCHW float32 |
|---|---|
| Mean | 0.485, 0.456, 0.406 |
|---|---|
| Std | 0.229, 0.224, 0.225 |
|---|---|
| Output | 3 logits, softmax locale |
|---|---|
| Label order | bank_statement, invoice, other |
|---|---|
| Modello FP32 | 6.084.524 byte, SHA pubblicato nel README |
|---|---|
| Quantizzato INT8 | Experimental, non raccomandato |

**Non dedurre dal model card:** supporto PDF nativo, estrazione testo, classificazione ricevute separata, altre lingue o performance su fatture italiane. La soglia 0,85 e il margin 0,10 del codice originale sono **decisioni di sicurezza del prototipo**, non parametri certificati del donor.

## API proposta

`DocRexContract.normalizeCenterCrop(Uint8List rgb256) -> Float32List` e `DocRexContract.evaluate(List<double> logits) -> TriageDecision` (suggerimento non esecutivo).

Il renderer dell'app ospite deve generare RGB 256x256 tramite un adattatore Flutter; il runtime ONNX (plugin) e un'eventuale distribuzione on-demand del modello sono da valutare con audit Android/iOS.

**Accettazione prodotto:** file originali immutati, preview manuale, fallback `other`/bassa confidenza senza classificazione forzata, niente rete implicita, report del benchmark italiano e no secondi datastore.
