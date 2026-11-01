# Specifiche candidate — CAP-0105

## Scopo

Ordinare task per urgenza importanza durata e vincoli con motivazioni leggibili; mostrare gli stessi dati in quadranti Eisenhower.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Prioritizzazione trasparente e matrice Eisenhower** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Controllare priorita/task preesistenti; regole deterministiche configurabili, no score opachi e drag quadranti deve aggiornare le stesse task; evitare classificazioni non richieste.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
