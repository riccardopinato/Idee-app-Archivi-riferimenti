# Specifiche candidate — CAP-0094

## Scopo

Una stessa attivita appare su post-it, Kanban, checklist e planner con ID/ownership unici, drag-and-drop e stati sincronizzati.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Sticky Kanban con task canoniche su canvas e planner** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Verificare modelli e canvas attuali, riusare post-it/task, garantire update unico, undo e sync; non usare come donor il link MiniMax-M1 non pertinente.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
