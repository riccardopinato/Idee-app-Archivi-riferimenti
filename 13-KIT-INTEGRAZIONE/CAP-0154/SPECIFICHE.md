# CAP-0154 — Routine predittive con Markov solo opt-in

MVP read-only: Transizioni tra stati locali e frequenze smussate per suggerimenti reversibili.

Confini: Opt-in, minimal retention, cancellazione, min-sample, divieto inferenze sensibili e zero notifiche automatiche.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0111, CAP-0148. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
