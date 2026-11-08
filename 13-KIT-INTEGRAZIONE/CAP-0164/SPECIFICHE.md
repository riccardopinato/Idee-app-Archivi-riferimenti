# CAP-0164 — Specifiche E0

## Ambito
Query e scripting locale su note e knowledge base

Delta circoscritto a Query e scripting locale su note e knowledge base. Non duplicare la responsabilita delle CAP CAP-0013, CAP-0032, CAP-0112. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0013, CAP-0032, CAP-0112, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Sandbox, privacy, limiti di esecuzione e tipizzazione
