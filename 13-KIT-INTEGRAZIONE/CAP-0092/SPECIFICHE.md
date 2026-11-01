# Specifiche candidate — CAP-0092

## Scopo

Convertire testo o trascrizioni volontarie in bozze editabili di task, date, priorita e reminder; origine e ambiguita conservate.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Cattura task da linguaggio naturale e note** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Verificare capture/task canonici prima di aggiungere parser IT/EN locale; preview, timezone, consenso prima di scheduler, AI solo pack opzionale e niente download automatici.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
