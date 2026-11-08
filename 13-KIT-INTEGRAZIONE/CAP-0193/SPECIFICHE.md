# CAP-0193 — Specifiche E0

## Ambito
Diario testuale portable e operazioni CLI per data

Delta circoscritto a Diario testuale portable e operazioni CLI per data. Non duplicare la responsabilita delle CAP CAP-0014, CAP-0150, CAP-0018. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0014, CAP-0150, CAP-0018, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Per Anna prodotto UI-first; CLI solo interop opzionale
