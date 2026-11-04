# CAP-0158 — Soglie adattive con isteresi per luce e prossimità

MVP read-only: EWMA e debounce per segnali rumorosi, impossibile inferire contesto da un solo campione.

Confini: Sensor availability/health, luce coperta, prossimità binaria, calibrazione, consumo e verifica real-device OEM.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0057, CAP-0062. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
