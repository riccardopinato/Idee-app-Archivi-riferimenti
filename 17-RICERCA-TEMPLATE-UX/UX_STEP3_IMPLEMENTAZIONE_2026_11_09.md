# Maxi-step 3 — Template nativi / tre piloti

**Decisione prodotto:** utente ha autorizzato a procedere il 09/11/2026 sulla base delle tre UX Step2 già integrate. Approvazione limitata ai template gratuiti leggeri e ai writer esistenti. Nessuna autorizzazione per billing, template marketplace, cloud o dati aggiuntivi.

| App | PR Step3 | Adapter canonico | Gate ancora necessario |
|---|---|---|---|
| Notes-Ecosistema | [#96](https://github.com/riccardopinato/Notes-Ecosistema/pull/96) | `PageTemplates.bookTracker` → `TemplatesScreen.onUse` → note writer canonico | exact-head CI + runtime/backup/account |
| Anna's Diary | [#290](https://github.com/riccardopinato/Agenda-per-Anna/pull/290) | anteprima read-only `DiaryTemplatePreset` + `DailyRitualCard`; attivazione/reminder nelle impostazioni esistenti | exact-head Development/Web/Source Gate + device/consenso |
| Wonderlog | [#26](https://github.com/riccardopinato/Wonderlog/pull/26) | `JourneyRepository.createJourney` con intestazioni testuali `description` | analyze/test/Android/Web + premium gate e ciclo di vita |

**Stato al momento della registrazione:** branch/PR create; i merge e le verifiche finali NON sono impliciti. Guardare le PR sopra per i check sul rispettivo HEAD. Eventuali snapshot, report o pagamenti commerciali richiedono gate separati.

**Non cambiare:** API billing/premium, database, licenze asset Notion, sync, schemi cloud, privilegi, Vault, dei rituali, modelli libri, packing o budget strutturati.

**Factory baseline:** `d4ed1185d36d419228fba6b57a979cde308bd321` Master v27 / Golden Index v29.
