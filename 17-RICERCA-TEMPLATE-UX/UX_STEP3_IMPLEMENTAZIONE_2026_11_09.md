# Maxi-step 3 — Template nativi / tre piloti

**Decisione prodotto:** utente ha autorizzato a procedere il 09/11/2026 sulla base delle tre UX Step2 già integrate. Approvazione limitata ai template gratuiti leggeri e ai writer esistenti. Nessuna autorizzazione per billing, template marketplace, cloud o dati aggiuntivi.

| App | PR Step3 | Adapter canonico | Stato verificato / gate residuo |
|---|---|---|---|
| Notes-Ecosistema | [#96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96) | `PageTemplates.bookTracker` → `TemplatesScreen.onUse` → note writer canonico | **MERGED** `42efc5b91fc01ef6e40e9a5d61ab8d1d05f9f41c`; exact-head verify, verify-web, build-web PASS; runtime/backup/account NOT VERIFIED |
| Anna's Diary | [#290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290) | anteprima read-only `DiaryTemplatePreset` + `DailyRitualCard`; attivazione/reminder nelle impostazioni esistenti | **MERGED** `0b49de46d43f4747c5cf9425d460f2fc2c7e6cd4`; check, UI5 source, build-web PASS; device/consenso NOT VERIFIED |
| Wonderlog | [#26](https://github.com/riccardopinato/Wonderlog/pull/26) | `JourneyRepository.createJourney` con intestazioni testuali `description` | **MERGED** `c238afd82ca93699d0e0d5d4e3e3a9a0d6d1d9ee`; exact-head verify, apple-build, legacy-contract PASS; runtime premium/ciclo vita NOT VERIFIED |

**Stato aggiornato 09/11/2026:** tre PR Step3 integrate in `main`, CI exact-head superata. La conferma merge non costituisce test di dispositivo, collaudo di flussi reali, backup/account, pubblicazione Store o attivazione di pagamenti. Eventuali snapshot, report o pagamenti commerciali richiedono gate separati.

**Non cambiare:** API billing/premium, database, licenze asset Notion, sync, schemi cloud, privilegi, Vault, dei rituali, modelli libri, packing o budget strutturati.

**Factory baseline:** `d4ed1185d36d419228fba6b57a979cde308bd321` Master v27 / Golden Index v29.
