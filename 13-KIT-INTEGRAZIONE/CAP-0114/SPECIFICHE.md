# CAP-0114 — specifiche sorgente vs implementazione disponibile

- Il donor Redact descrive classificazione PII multilingue (nomi, indirizzi, email, IBAN ecc.), runtime browser/Android con componente modello ~24.5MB e licenza propria. La demo non certifica una pipeline PDF senza dati residui.
- Il nostro codice originale `PrivacyPreview.detect` copre **soltanto email sintattiche e IBAN con checksum MOD 97**. Non riconosce nomi, indirizzi, telefono, targhe, metadata, immagini, PDF testo nascosto, OCR o record secondari.
- `mask(text, selected)` verifica corrispondenza originale e offset, restituisce una **nuova stringa** senza mutare l'originale, non esporta PDF e non ha selezione automatica di tutti i dati.
- Un prodotto di redazione deve fallire chiuso quando non puo garantire l'assenza di dati recuperabili: per PDF serve riscrittura e verifica del file esportato, non un rettangolo sopra il testo.

**Gate:** privacy specialist review, licenze/termini del donor, performance e test sulle categorie PII italiane, verificate sull'APK reale e audit metadata/export.
