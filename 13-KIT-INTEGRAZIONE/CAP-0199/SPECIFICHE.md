# CAP-0199 — Specifiche E0

## Ambito
Interfaccia MCP/API locale per lettura controllata di agenda e task

Delta circoscritto a Interfaccia MCP/API locale per lettura controllata di agenda e task. Non duplicare la responsabilita delle CAP CAP-0004, CAP-0002. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0004, CAP-0002, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Sandbox, autorizzazioni, no accesso al Vault o chiavi
