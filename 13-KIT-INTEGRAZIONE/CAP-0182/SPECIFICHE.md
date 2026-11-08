# CAP-0182 — Specifiche E0

## Ambito
Finestre sticky giornaliere/settimanali per desktop

Delta circoscritto a Finestre sticky giornaliere/settimanali per desktop. Non duplicare la responsabilita delle CAP CAP-0144, CAP-0001, CAP-0004. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0144, CAP-0001, CAP-0004, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Separare dal widget Android CAP-0144
