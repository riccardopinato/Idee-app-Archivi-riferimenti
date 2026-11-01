# Specifiche candidate — CAP-0107

## Scopo

Leggere Markdown/README scelti dall'utente e proporre task, fasi, dipendenze e stime collegate al documento sorgente.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Import blueprint progetto Markdown in bozze task** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Riutilizzare CAP-0093 e Import Center CAP-0075; parsers lightweight locali prima di AI; nessun accesso a file esterni implicito; Yuga richiama Nebius e Timefold, licenze e costi da auditare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
