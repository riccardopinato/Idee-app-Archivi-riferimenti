# CAP-0111 — Weekly Review leggero per Anna's Diary

**Stato: CONTRACT_PROTOTYPE — source compatibility documentata, Dart originale, non integrato in Anna.**

## Sorgenti realmente osservati

- [AgendaItem](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/domain_models.dart): ID, data, `ItemType.task`, `done`; `AgendaStore.items` e il contenitore privato canonico ([agenda_store.dart](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/agenda_store.dart)).
- [WeekData](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/domain_models.dart) contiene gia `focus`, `priorities`, `bestThing`, `reflection`. **Riusare questa rappresentazione**, non creare un secondo diario della settimana.
- [Daily rituals](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/daily_rituals.dart) conserva contenuti nel DayJournal, non richiede un engine alternativo.
- [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/docs/PRODUCT_BIBLE.md): diario personale, non strumento professionale per progetti e task.

## Contratto preparato

- [lib/anna_weekly_review.dart](lib/anna_weekly_review.dart): proiezione in sola lettura sulle sole task private, settimana lunedi-domenica, elenco ID scaduti prima della settimana, task pianificate e completate **con data nella settimana**. Non afferma di conoscere la data effettiva del completamento, che non e registrata in `AgendaItem.done`.
- [test/anna_weekly_review_test.dart](test/anna_weekly_review_test.dart): confini, de-duplicazione ID, esclusione shared/appuntamenti, account switch, limiti e input immutati.

**Mancano:** UI riepilogo, dati storici completamento puntuali, salvataggio conferme/skip su store canonico, backup/sync, device QA. Questo kit **non** e una weekly review automaticizzata.

**Gate di prodotto:** Nessuna nuova funzione e approvata nella roadmap corrente; questo e un kit per futuri esperimenti, non una modifica all'app o ai dati. Gli stati app restano PROPOSTA.

[Specifiche](SPECIFICHE.md) · [Codice](CODICE_RIFERIMENTO.txt) · [Piano](INTEGRAZIONE_FLUTTER.md) · [Licenze](LICENZE_E_DIPENDENZE.md) · [Test](TEST_E_VALIDAZIONE.md)
