# Specifiche candidate — CAP-0096

## Scopo

Task principali e sottotask, dipendenze/relazioni, ricorrenze, tag e priorita con reminder coerenti e lifecycle recuperabile.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Gerarchie task ricorrenze e relazioni alle note** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Audit funzioni task e recurrence gia presenti; non introdurre secondo scheduler o storage; test eccezioni ricorrenza, delete e restore.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
