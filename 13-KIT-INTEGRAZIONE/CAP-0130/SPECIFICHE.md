# Specifiche candidate — CAP-0130

## Scopo

Notes to Slides: Trasforma note selezionate in slide con titoli e impaginazione modificabili, esportando senza alterare le note. Scientific Figure Studio: Crea diagrammi scientifici/figure tecniche modificabili partendo da testi e fonti, usando una pipeline visual-export comune a slide.

## Requisiti iniziali proposti (non specifiche donor verificate)

1. Selezione esplicita dell'input e identificazione della fonte.
2. Elaborazione limitata a **Generazione di slide e figure tecniche modificabili** e restituzione di un risultato chiaro o errore esplicito.
3. Preview/edit prima di ogni mutazione; nessun download, upload, sincronizzazione o cancellazione implicita.
4. Riutilizzo dei dati canonici, import/export, lifecycle e backup dell'app destinataria.
5. Offline/failure, localizzazione, accessibilità e logica permessi trattati per-app.

## Gate particolare

Paper2Any dichiara Paper2PPT e licenza Apache-2.0, ma la demo pubblica era in errore; il backend/AI non va importato automaticamente. | Paper2Any dichiara Paper2Figure e Paper2PPT nella stessa codebase; registrata come modalita dello stesso CAP di Notes-to-Slides. Verificare architettura e licensing nel Product Bible prima di integrare.

**DA COMPLETARE:** interfacce sorgente e API reali, forme dati e file target dopo audit a SHA del donor e dell'app.
