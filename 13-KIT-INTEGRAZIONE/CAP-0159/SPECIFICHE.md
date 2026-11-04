# CAP-0159 — Clustering spaziale privacy-safe per ricordi e POI

MVP read-only: DBSCAN in metri o griglia geospaziale con source visibility.

Confini: Antimeridiano/poli, GPS nullo/non finito, raggio geodesico, permesso luoghi condivisi, dati privati non esportabili per default.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0009, CAP-0051, CAP-0048. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
