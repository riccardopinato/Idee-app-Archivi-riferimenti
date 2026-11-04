# CAP-0151 — Riassunti estrattivi di note con TextRank e citazioni

MVP read-only: Ranking di frasi originali con offset e fonte; sintesi estrattiva non generativa.

Confini: Segmentazione multilingua, citazioni/negazioni, source-revision, test di frasi non inventate, fallback a estratto lineare.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0032, CAP-0097, CAP-0148. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
