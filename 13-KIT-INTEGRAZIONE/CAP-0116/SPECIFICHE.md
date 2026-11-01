# Specifiche candidate — CAP-0116

## Scopo

Duplicate Notes Cleaner: Trova note semanticamente simili e suggerisce confronto/merge mantenendo allegati, riferimenti e cestino.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Deduplicazione semantica note con merge reversibile** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

SemHash dimostra dedup di testi/dataset, non merge sicuro di note personali. Usare ID e backup canonici. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
