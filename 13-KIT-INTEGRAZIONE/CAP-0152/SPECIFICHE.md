# CAP-0152 — Ricerca fuzzy offline per refusi e alias

MVP read-only: Distanza Levenshtein/Jaro-Winkler solo su candidati autorizzati, Unicode-aware.

Confini: Top-K bounded, grapheme, token di 1 carattere, soglie false-match, 500/5000 record e nessuna fuga da Shared Spaces.

- Input: dati canonicali visible/permission-scoped e revision delle fonti.
- Output: proposta con reason code e fallback; nessun writer, notifiche o upload involontario.
- Dipendenze: CAP-0015, CAP-0032. No nuovo database o sync cross-app.
- Esempi contrari e casi limiti da aggiungere nei test prima di produrre feature reali.
