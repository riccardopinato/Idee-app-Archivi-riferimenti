# CAP-0183 — Piano integrazione Flutter

1. Leggere Product Bible e roadmap attuali. Lo stato PROPOSTA non autorizza implementazione.
2. Audit dell'owner canonico e delle CAP parent: CAP-0145, CAP-0096, CAP-0101.
3. Definire DTO, puro Dart adapter ove possibile; permessi/API native solo con gate esplicito.
4. Filtrare ACL e revision prima di calcoli, export, notifiche o suggerimenti.
5. Implementare preview, conferma, idempotenza, errori/undo e rollback.
6. Test unitari e di integrazione; CI exact-head e QA reale device/provider se pertinente.
7. Misurare differenza dimensione APK, RAM, batteria e latenza prima di adottare dipendenze.

Gate: Opt-in, nessuna pressione/comportamento patologizzante
