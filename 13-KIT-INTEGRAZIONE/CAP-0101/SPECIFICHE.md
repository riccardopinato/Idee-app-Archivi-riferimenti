# Specifiche candidate — CAP-0101

## Scopo

Statistiche deterministiche su completate, arretrate, priorita, progetti e intervalli, senza telemetria esterna necessaria.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Dashboard produttivita locale da task canoniche** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Verificare report gia esistenti; calcolare su task non cestinate; metriche semplici e leggibili con limiti e no analytics privacy-invasive.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
