# CAP-0102 — Anna: specifiche derivate dai sorgenti

**App target:** riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2 — `pubspec.yaml` Flutter/Dart >=3.10, `1.0.0-rc.6+117`.

## Data contracts rilevati

- `CalendarFreeSlot`: coppia DateTime inizio/fine; `findCalendarFreeSlots` deriva gap da eventi visibili e autorizzati, non da task; disponibilita esterna dipende da `ExternalCalendarService`/permission/coverage.
- `AgendaItem`: `ItemType.task`, `done`, `id`, `date`, `start/end`, `recurrenceRule`; **nessun campo `plannedMinutes` o `duration` universale**; chiedere `requestedMinutes` prima di proporre.
- `AgendaStore`: owner delle modifiche, account attivo e revisioni; il kit non possiede alcun writer, modalita solo lettura.

## Adapter originale

`AnnaReschedulePreview.suggest(taskId, requestedMinutes, now, freeWindows, isPrivateTask, completed, recurring, fixedAppointment, calendarCoverageComplete, accountUnchanged, deadline?, previousStart?) -> List<AnnaMoveProposal>`.

**Invarianti:** nessuna proposta su shared/external/fixed/ricorrente; deadline hard; ordinamento deterministico, dedup dello stesso start; niente commit o notifica automatica; calendario parziale/account cambiato = zero proposte. Nessun inferenza AI. DateTime timezone e DST dovranno essere verificate nella UI e su device prima del riuso.

**Fonte di ispirazione**: [Plan My Day, dataset sperimentale Apache-2.0](https://huggingface.co/datasets/burtenshaw/plan-my-day-results) usa imprevisti e preferenze, ma non fornisce un modulo Dart pronto né prove su utenti reali. NESSUN codice/peso/dato donor copiato.
