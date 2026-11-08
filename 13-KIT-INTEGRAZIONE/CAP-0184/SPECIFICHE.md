# CAP-0184 — Specifiche E0

## Ambito
Serie abitudini e obiettivi di continuità con storico

Delta circoscritto a Serie abitudini e obiettivi di continuità con storico. Non duplicare la responsabilita delle CAP CAP-0112, CAP-0145, CAP-0101. Ogni dubbio di sovrapposizione richiede confronto di test/contratti prima di introdurre codice.

## Input
Entita canoniche visibili, revision, scope/ACL, consenso, dati user-selected.

## Output
Preview leggibile con reason code e undo/rollback se la funzione scrive; nessuna mutazione autonoma o doppio storage.

## Invarianti
Identita stabile; privacy, account switch e visibilita prima di ogni lookup; niente export automatico; implementazione non inferita dalle fonti OSS.

## Esclusioni
Non sostituire CAP-0112, CAP-0145, CAP-0101, non introdurre cloud, AI o plugin obbligatori per il solo catalogo.

## Acceptance gate
Distinguere dalla heatmap CAP-0145
