# CAP-0191 — Specifiche E0

## Ambito
Editor multipannello con due note e split sincronizzato

Delta circoscritto a Editor multipannello con due note e split sincronizzato. Non duplicare la responsabilita delle CAP CAP-0018, CAP-0032. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0018, CAP-0032, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Non duplicare i writer e testare gestione conflitti
