# CAP-0157 — Gesti volontari locali tramite Dynamic Time Warping

MVP read-only: Distanza DTW con template scelto dall'utente; cap sensori/FGS obbligatorio.

Confini: Template locali e soglia calibrata, bounded samples, falso positivo sui device, Android background/permission, no cattura audio implicita.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0057, CAP-0062. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
