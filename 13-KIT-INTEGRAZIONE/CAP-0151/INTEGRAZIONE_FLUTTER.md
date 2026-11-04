# CAP-0151 — Riassunti estrattivi di note con TextRank e citazioni

1. Risolvere la Product Bible e lo SHA dei repo app al momento dell'implementazione.
2. Selezionare la piu piccola fonte Golden E3 pertinenti, senza promuovere l'intero motore in automatico.
3. Adapter puro Dart (o Kotlin nativo se richiesto) per LEXICAL_TEXT; nessuna rete o modello predefinito.
4. Data filtering e ACL prima degli algoritmi; no source mutation e idempotenza per conferme ripetute.
5. Test proprietà/determinismo e negative/fuzz; analisi Dart/Flutter, CI exact-head, hardware se coinvolti sensori/batteria.
6. E3 donor dopo direct tests+CI; E5 solo dopo consumer indipendente e prove scope.

GATE: Segmentazione multilingua, citazioni/negazioni, source-revision, test di frasi non inventate, fallback a estratto lineare.
