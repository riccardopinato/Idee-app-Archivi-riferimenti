# Specifiche candidate — CAP-0119

## Scopo

Citation Integrity Checker: Controlla esistenza e metadati di citazioni e bibliografie, segnalandone anomalie senza dichiarare falsi positivi come inventati.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Audit citazioni bibliografiche e fonti** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

La demo CiteAudit ha runtime error al controllo; verificare Crossref/DOI/ISBN prima di ogni integrazione; offline limitato. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
