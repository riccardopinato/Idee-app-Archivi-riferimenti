# Specifiche candidate — CAP-0088

## Scopo

Preset e ripristino layout multi finestra soltanto per device desktop realmente compatibili.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Workspace Android desktop virtuale con capability probe** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Rimandato: Dextop GPLv3, usa hidden API e runtime privilegiati; Samsung OneUI moderno prevalente, Xiaomi/HyperOS disabilitato. Vietato promettere compatibilita universale, copia solo con obblighi GPL e test Play.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
