# CAP-0157 — Gesti volontari locali tramite Dynamic Time Warping

1. Risolvere la Product Bible e lo SHA dei repo app al momento dell'implementazione.
2. Selezionare la piu piccola fonte Golden E3 pertinenti, senza promuovere l'intero motore in automatico.
3. Adapter puro Dart (o Kotlin nativo se richiesto) per SENSOR_SIGNAL; nessuna rete o modello predefinito.
4. Data filtering e ACL prima degli algoritmi; no source mutation e idempotenza per conferme ripetute.
5. Test proprietà/determinismo e negative/fuzz; analisi Dart/Flutter, CI exact-head, hardware se coinvolti sensori/batteria.
6. E3 donor dopo direct tests+CI; E5 solo dopo consumer indipendente e prove scope.

GATE: Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita.
