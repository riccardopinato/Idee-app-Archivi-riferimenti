# Specifiche candidate — CAP-0097

## Scopo

Recuperare decisioni, blocchi e storico per singolo progetto, rimandando ai documenti originali e mostrando i limiti delle risposte.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Project Memory con Q&A circoscritto e provenance** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Partire da filtri e FTS locale esistenti; ricerca semantica solo opt-in/on-device se giustificata; citazioni verificabili e isolamento tra progetti.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
