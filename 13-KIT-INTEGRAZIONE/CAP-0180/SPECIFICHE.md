# CAP-0180 — Specifiche E0

## Ambito
Archivio snippet di codice con linguaggi e frammenti

Delta circoscritto a Archivio snippet di codice con linguaggi e frammenti. Non duplicare la responsabilita delle CAP CAP-0013, CAP-0084. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0013, CAP-0084, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Riutilizzare note/tag/code block senza un secondo vault
