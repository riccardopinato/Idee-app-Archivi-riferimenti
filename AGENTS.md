# AGENTS.md — contratto operativo di archivio

- Questo repo è la source of truth di idee, classifiche e riferimenti, NON delle policy App Factory, dei test AppLab o dello stato dei sorgenti app.
- Per task che dipendono dalla Factory: risolvere una volta CURRENT.yaml di App-Factory-Core, Master, Golden Index e Registry e solo Golden pertinenti; non usare README come policy autoritativa.
- Per AppLab o una app specifica: leggere repository/ref correnti solo quando il task lo richiede, senza assumere che la memoria sia aggiornata.
- Leggere solo la cartella pertinente; registrare **tutte le nuove idee in 11-NUOVE-IDEE/INBOX_IDEE.md**, non direttamente nel catalogo app già registrate. Se un'idea viene promossa, aggiornare 01-PORTAFOGLIO lasciando un link al record originale in 11. Mantenere ID stabile e fonte/data senza cancellare lo storico.
- Stato app: IDEA / IN_ROADMAP / IN_CODICE / TESTATO / RELEASE / NON_VERIFICATO; non convertire BUILD SUCCESS in RELEASE.
- Stato provider: CANDIDATE / REVIEWED / APPROVED_FOR_SCOPED_USE / BLOCKED; includere licenza, attribution, rate limit, uso commerciale, costi, privacy, geografia e freshness.
- Repository OSS: annotare licenza per repo/file, commit, modalità reference/riuso e test; nessuna copia se licenza assente, dubbia o incompatibile.
- Prodotto finale e donor possono convivere: standalone + suite senza doppia architettura e senza promesse di entitlement cross-app implicito.
- Descrizioni marketing sempre marcate DRAFT finché non verificate dal prodotto reale.
- Ogni modifica sostanziale aggiorna indice e CHANGELOG, conserva storia, segue branch/PR e gate appropriati.
- Una nuova categoria ricorrente può aggiungere cartella e link nella home; Git non salva cartelle vuote.
