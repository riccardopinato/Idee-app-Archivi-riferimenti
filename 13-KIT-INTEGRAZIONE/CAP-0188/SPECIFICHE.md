# CAP-0188 — Specifiche E0

## Ambito
Pubblicazione controllata Markdown/wiki con redazione

Delta circoscritto a Pubblicazione controllata Markdown/wiki con redazione. Non duplicare la responsabilita delle CAP CAP-0013, CAP-0100, CAP-0014. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0013, CAP-0100, CAP-0014, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Mai esporre contenuti privati o condivisi per default
