# Specifiche candidate — CAP-0115

## Scopo

Contradiction Finder: Evidenzia frasi potenzialmente in conflitto tra note, senza scegliere quale versione sia vera.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Segnalazione contraddizioni testuali con provenance** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

NLI e segnalazione probabilistica, necessita prova sulle negazioni, numeri, date e citazioni; nessuna correzione automatica. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
