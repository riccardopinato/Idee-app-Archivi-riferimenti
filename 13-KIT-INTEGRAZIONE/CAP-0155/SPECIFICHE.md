# CAP-0155 — Associazioni ingredienti e ricette offline con Apriori

MVP read-only: Frequent itemset e regole con supporto/confidenza, mai dedurre allergeni o causalità.

Confini: Corpus minimo, support/confidence/lift, ingredienti canonici, lingua, allergeni, nessuna aggiunta automatica a spesa.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0044, CAP-0045. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
