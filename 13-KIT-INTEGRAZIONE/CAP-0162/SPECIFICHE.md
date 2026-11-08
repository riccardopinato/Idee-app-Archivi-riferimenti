# CAP-0162 — Specifiche E0

## Ambito
Wikilink, backlink e rinomina dei link con riparazione

Delta circoscritto a Wikilink, backlink e rinomina dei link con riparazione. Non duplicare la responsabilita delle CAP CAP-0013, CAP-0112, CAP-0098. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0013, CAP-0112, CAP-0098, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Riconciliare con Knowledge Graph e link stabili già implementati
