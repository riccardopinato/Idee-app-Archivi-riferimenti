# CAP-0153 — Previsione prudente di completamento studio e progetti

MVP read-only: Media robusta o regressione locale con intervallo e fallback senza previsione.

Confini: Minimo storico, anomalie, weekend e pause, intervallo di confidenza onesto, mai date certe da campioni scarsi.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0108, CAP-0104, CAP-0102. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
