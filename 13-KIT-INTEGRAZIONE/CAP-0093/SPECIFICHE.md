# Specifiche candidate — CAP-0093

## Scopo

Estrarre piu attivita e sottoattivita da una nota mantenendo origine, editabilita e link canonici invece di duplicare documenti.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Da note a checklist strutturate** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Audit note/task esistenti, implementare parsing deterministico e preview multi-selezione; dataset NC reference only, test su ambiguita e nessuna creazione implicita.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
