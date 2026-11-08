# CAP-0178 — Specifiche E0

## Ambito
Espansione abbreviazioni solo nell'editor corrente

Delta circoscritto a Espansione abbreviazioni solo nell'editor corrente. Non duplicare la responsabilita delle CAP CAP-0093. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0093, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Riusa i template esistenti e permette undo
