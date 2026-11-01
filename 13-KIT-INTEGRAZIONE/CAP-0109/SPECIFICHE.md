# Specifiche candidate — CAP-0109

## Scopo

Timer locale lavoro/pausa con attribuzione alla task o nota attiva e, se disponibile e autorizzato, controlli di riduzione distrazioni.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Sessioni Focus/Pomodoro collegate a note e protezione opzionale** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Riutilizzare eventuali timer FocusSense prima del codice; persistenza dopo app pause, gestione lifecycle e background Android, DND soltanto con permesso/azione esplicita; non promettere blocco siti.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
