# CAP-0156 — Semplificazione reversibile di tracce e polilinee GPX

MVP read-only: Ramer–Douglas–Peucker parametrizzato in metri, originale immutato.

Confini: Lat/lon finiti, antimeridiano e poli, endpoint/waypoint protetti, errore massimo verificato, nessuna mutazione dello storico.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0048, CAP-0049, CAP-0050. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
