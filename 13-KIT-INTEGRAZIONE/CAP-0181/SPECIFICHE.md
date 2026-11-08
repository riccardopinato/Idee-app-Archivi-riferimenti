# CAP-0181 — Specifiche E0

## Ambito
Import/export lossless di todo.txt, Org e TaskPaper

Delta circoscritto a Import/export lossless di todo.txt, Org e TaskPaper. Non duplicare la responsabilita delle CAP CAP-0096, CAP-0075, CAP-0105. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0096, CAP-0075, CAP-0105, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Parser delimitato, anteprima, semantica recurrence e rollback
