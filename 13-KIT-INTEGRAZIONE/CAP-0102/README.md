# CAP-0102 — Smart Rescheduler / Anna's Diary

**Stato: CONTRACT_PROTOTYPE — specifiche di sorgente Anna esaminate e codice originale Dart con test; NON integrato nell'app.**

## Materiale esistente osservato

- [Anna CalendarFreeSlots](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/calendar_free_slots.dart): `CalendarFreeSlot(start,end)`, `findCalendarFreeSlots()`, controllo di intervalli occupati con appuntamenti privati/condivisi visibili e overlay esterno opzionale. Un appuntamento privo di orario blocca il giorno, privo di fine blocca fino a mezzanotte. Task NON occupano tempo: non dedurre disponibilita da essi.
- [UnifiedAgendaEntry](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/unified_agenda.dart): campi `type`, `isPrivate/isShared/isExternal`, `start/end`; [AgendaItem](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/domain_models.dart) con `id`, `date`, `done`, `recurrenceRule`, `start/end`, `ItemType.task`. **Non possiede un campo canonico durata del task**: il prototipo richiede una durata indicata dall'utente.
- [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/docs/PRODUCT_BIBLE.md): agenda personale leggera, no project manager, no spostamenti o condivisione impliciti.

## Componenti riutilizzabili

- [lib/anna_reschedule_preview.dart](lib/anna_reschedule_preview.dart) — codice originale senza pacchetti, seleziona solo proposte temporali per task private, mobili, non ricorrenti, incomplete. Fail-closed se calendario parziale/account cambiato. Rispetta deadline e selezione manuale.
- [test/anna_reschedule_preview_test.dart](test/anna_reschedule_preview_test.dart) — contratto deterministico; verifica durata, deadline, dedup, slot fissi, account/visibilita, nessuna scrittura.

**Limitazioni:** non sposta un record, non modifica notifiche o cloud, non calcola slot da solo, non supporta prioritizzazione, alternative planning avanzato o multi-task. Solo preview di un singolo task.

**Gate di prodotto:** Nessuna nuova funzione e approvata nella roadmap corrente; questo e un kit per futuri esperimenti, non una modifica all'app o ai dati. Gli stati app restano PROPOSTA.

[Specifiche](SPECIFICHE.md) · [Codice e provenienza](CODICE_RIFERIMENTO.txt) · [Integrazione Flutter](INTEGRAZIONE_FLUTTER.md) · [Licenze](LICENZE_E_DIPENDENZE.md) · [Test](TEST_E_VALIDAZIONE.md)
