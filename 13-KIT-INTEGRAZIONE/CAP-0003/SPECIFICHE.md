# Specifiche candidate — CAP-0003

## Scopo

Editor contestuale per appuntamenti privati con note e checklist leggibili in AgendaItem.note, senza scheduler o storage aggiuntivo.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Preparazione contestuale appuntamento** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Collaudo fisico +116 V116-06…V116-10 e V116-12: note, checklist, conflitti, Trash, offline e lingue; CI e APK firmato non equivalgono a DEVICE_PASS.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
