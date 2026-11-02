# Specifiche candidate — CAP-0145

## Responsabilità distinta

Vista aggregata calendar-heatmap delle attività realmente annotate, con dati mancanti distinti da zeri e senza inferenze psicologiche.

## MVP delimitato

Griglia locale per eventi/diario/task esistenti; eventuale mood/gratitudine solo con input esplicito e consenso.

## Vincoli architetturali

- Derived view su store canonico di diario e task, nessun nuovo profiler né IA e nessuna telemetria obbligatoria.
- REUSE FIRST: un solo owner per stato e scritture, adapter per OS/piattaforma, nessuna migrazione distruttiva.
- Non introdurre IA, cloud/login obbligatori o un altro database senza Product Bible e approvazione.
- UX privacy-by-default, preview prima di divulgazione, accessibilità e lingue supportate.

## Gate di sicurezza / business

No health/diagnostic claims, no dati ciclo/Vault in UI ordinaria, no esempi +40% spacciati per risultati; test missingness e permessi.

**Non costituisce uno scope di sviluppo approvato.** Definire payload, API, upgrade e criteri finali dopo decisione prodotto.
