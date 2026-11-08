# CAP-0196 — Specifiche E0

## Ambito
Archivio documenti indicizzato con classificazione e retention

Delta circoscritto a Archivio documenti indicizzato con classificazione e retention. Non duplicare la responsabilita delle CAP CAP-0035, CAP-0134. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0035, CAP-0134, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Distinguere OCR CAP-0035, triage CAP-0134 e vault documenti
