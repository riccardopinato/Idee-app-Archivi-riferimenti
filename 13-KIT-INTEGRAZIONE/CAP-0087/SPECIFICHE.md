# Specifiche candidate — CAP-0087

## Scopo

Overlay opt-in su mappa per terremoti, incendi o altri dati pubblici con data e confidenza esplicite.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Layer geografici pubblici con freshness e fallback** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Per ogni feed dichiarare API, diritti commerciali, refresh, intervalli, limiti, simulazioni e disponibilita; nessuna navigazione operativa o allerta emergenza da data feed incompleti. Repo metadata NOASSERTION: verify license per file.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
