# Specifiche candidate — CAP-0100

## Scopo

Assegnare task, tracciare cambi stato e filtrare per persona in workspace condivisi con ownership, ACL e cancellazione differenziata.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Kanban collaborativa task e permessi per workspace** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Non anticipare il Team roadmap; design-only finche identita/ACL/sync non sono approvati; nessuna condivisione implicita di note private; WebTestBench non e donor Kanban.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
