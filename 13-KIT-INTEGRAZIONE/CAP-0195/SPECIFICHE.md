# CAP-0195 — Specifiche E0

## Ambito
Timesheet esportabili e report settimanali per progetto

Delta circoscritto a Timesheet esportabili e report settimanali per progetto. Non duplicare la responsabilita delle CAP CAP-0108, CAP-0109, CAP-0105. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0108, CAP-0109, CAP-0105, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Misure da sessioni reali, timezone e no inventare lavoro
