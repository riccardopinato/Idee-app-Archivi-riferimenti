# CAP-0111 — Anna weekly review source-backed

**Source:** riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2.

## Proprietari canonici e separazioni

- `AgendaStore.items` conserva le task personali; `AgendaItem.done` e stato booleano corrente, non timestamp completamento. Non calcolare trend temporali da uno stato senza cronologia.
- `WeekData`: `focus`, `priorities`, `bestThing`, `reflection` esistono gia; una nuova UI deve proiettare e semmai aggiornare soltanto questa struttura tramite metodi esistenti.
- `DayJournal` e `DiaryBlock` servono il diario locale, non sono trascrizioni task; non includere automatiche sezioni Vault, Password Vault, ciclo e Spazio Condiviso.

## API prototipo

`AnnaWeeklyReview.fromPrivateTasks(weekOf, entries, accountUnchanged) -> AnnaWeekReview` con `overdueTaskIds`, `pendingDatedThisWeekIds`, `completedDatedThisWeek`, `totalTasksDatedThisWeek`.

Solo ID (non i testi di task/diario), nessuna persistenza, no lettura dati shared. La denominazione `completedDatedThisWeek` e intenzionale: indica task *datate* nella settimana attualmente marcate come fatte, NON task completate in quella settimana.

Ispirazione generica [MiniAppBench](https://huggingface.co/datasets/MiniAppBench/Dataset) benchmark specifiche; non un SDK ne codice copiato.
