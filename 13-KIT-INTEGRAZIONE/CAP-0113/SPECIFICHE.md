# Specifiche candidate — CAP-0113

## Scopo

Creare una bozza modificabile di ricordo da un appuntamento privato passato, con conferma, identita deterministica anti-duplicato e rispetto del Cestino.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Da appuntamento passato a ricordo privato** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Collaudo fisico APK +116 V116-03…V116-05: annulla senza scrivere, anti-duplicato, Trash/restore e privacy; valutare riuso Wonderlog senza duplicare il diario.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
