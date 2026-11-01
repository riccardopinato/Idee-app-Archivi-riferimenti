# CAP-0102 — piano integrazione Anna Flutter

1. Rileggere Product Bible/roadmap e fissare il target SHA (audit riccardopinato/Agenda-per-Anna@88efdfa9a688f35585cf2760d131f7a6b0b9deb2). Questa capability e PROPOSTA, non in roadmap.
2. Riprendere la funzione esistente `visibleEntriesForCalendarFreeSlots` e `findCalendarFreeSlots` dal `lib/src/calendar_free_slots.dart`; **non implementare un secondo calendario**, ne cambiare il comportamento conservativo di appuntamenti non temporizzati.
3. Operare solo sul task privato `AgendaItem`, non su `UnifiedAgendaEntry.shared/external`; bloccare task ricorrenti finche non esista un gate per l'intera serie.
4. Chiedere durata esplicita e mostrare preview a fianco dell'editor esistente; verificare account/agenda revision e coverage prima di qualunque conferma. Il writer rimane l'API `AgendaStore` attuale; nessun backend aggiunto.
5. Test Flutter su account switch, overlay revocato, shared filter, timezone/DST, notifiche, backup e undo; QA fisico prima della promozione di stato.

**Codice preparato:** solo pure Dart, non patch direttamente applicata al codice `part of '../main.dart'`.
