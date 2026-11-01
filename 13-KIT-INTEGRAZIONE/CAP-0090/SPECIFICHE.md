# Specifiche candidate — CAP-0090

## Scopo

Segnalare file e comportamenti fuori dallo scope autorizzato prima del merge.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Controllo scope creep e dipendenze nelle PR** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Verificare se AppLab copre gia la stessa responsabilita: solo gate advisory a diff bounded confrontato con PR scope, niente agente ulteriore o trigger duplicati. Controllare licenza di ogni skill e le sue dipendenze.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
