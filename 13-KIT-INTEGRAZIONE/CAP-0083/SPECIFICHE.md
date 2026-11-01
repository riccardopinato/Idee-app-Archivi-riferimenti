# Specifiche candidate — CAP-0083

## Scopo

Usare visualizzazione a rettangoli proporzionali per mostrare cosa occupa lo storage senza cancellazioni implicite.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Treemap interattiva dello spazio e selezione sicura** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Scansione progressiva read-only, treemap per dimensione, selezione esplicita, conferma eliminazione o esportazione e rollback ove disponibile. Non replicare accesso MFT/NTFS nel sandbox Android.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
