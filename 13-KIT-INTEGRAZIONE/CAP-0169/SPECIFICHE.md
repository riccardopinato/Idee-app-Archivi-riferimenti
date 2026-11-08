# CAP-0169 — Specifiche E0

## Ambito
Sincronizzazione CalDAV bidirezionale opt-in

Delta circoscritto a Sincronizzazione CalDAV bidirezionale opt-in. Non duplicare la responsabilita delle CAP CAP-0004, CAP-0144, CAP-0100. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0004, CAP-0144, CAP-0100, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Google Calendar Direct issue #199 resta DRAFT; account e conflitti vanno verificati
