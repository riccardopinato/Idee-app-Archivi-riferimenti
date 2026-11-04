# CAP-0160 — Estrazione TF-IDF di parole chiave e tag suggeriti

MVP read-only: TF-IDF sparse per keyword e ranking, distinto da embeddings semantici.

Confini: Tokenizzazione IT/EN/ES/FR/DE/PT, stopwords, IDF stabile, shared ACL, gestione corpus piccolo, preview prima di tag writer.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0124, CAP-0148, CAP-0032. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
