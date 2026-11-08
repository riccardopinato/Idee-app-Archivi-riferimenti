# CAP-0177 — Specifiche E0

## Ambito
Tracciamento attività IDE tramite plugin opt-in

Delta circoscritto a Tracciamento attività IDE tramite plugin opt-in. Non duplicare la responsabilita delle CAP CAP-0108. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0108, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Solo eventi editor autorizzati e aggregati
