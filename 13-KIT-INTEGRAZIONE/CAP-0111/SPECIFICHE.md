# Specifiche candidate — CAP-0111

## Scopo

Revisione settimanale di task scadute, avanzamenti e impegni con azioni esplicite di conferma/skip e storico.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Weekly Review con proposte di pulizia e ripianificazione** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Riutilizzare dashboard CAP-0101, scheduler esistente e lifecycle; nessuna cancellazione o ripianificazione automatica; Anna in forma Today/diario non PM suite.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
