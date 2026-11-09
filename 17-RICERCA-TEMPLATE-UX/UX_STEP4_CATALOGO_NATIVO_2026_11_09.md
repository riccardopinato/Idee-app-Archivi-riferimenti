# Maxi-step 4 — Catalogo native free-first (Notes / Anna)

**Decisione:** autorizzato il 09/11/2026 il passo successivo dopo le integrazioni native gratuite Step3. La proposta di `Template Store` a pagamento rimane **BACKLOG DI PRODOTTO**: nessuno SKU, prezzo attivo, checkout, acquisto/ripristino o entitlements cross-app sono stati autorizzati in questo passaggio.

| App | PR sorgente | Implementazione nativa | Evidenza GitHub / gate residui |
|---|---|---|---|
| Notes-Ecosistema | [#97](https://github.com/riccardopinato/Notes-Ecosistema/pull/97) | `TemplatesScreen`: sezioni "Catalogo" di preset gratuiti e "I miei" modelli derivati solo da `PersonalTemplates.catalog` | **MERGED** `f057c81c92532cd22b504116c14ccef8a2ad6612`; PR head `ae93ff2a09284a34d15118a0a896b567b075ff0b`: `verify`, `verify-web`, `build-web` **SUCCESS**; account/backup/device **NOT VERIFIED** |
| Anna's Diary | [#291](https://github.com/riccardopinato/Agenda-per-Anna/pull/291) | `showDiaryTemplatePicker`: sei `DiaryTemplatePreset` originali gratuiti, preview seedText/mediaHint e consenso "Usa nel diario", poi editor canonico | **MERGED** `2c77c764ecf9982817aee8fc6ecc31ee75b741f9`; PR head `6316a4cfea97cefefbad899447a8fd655e10e463`: `check`, `build-web`, `UI5 source and visual-flow contracts` **SUCCESS**; device e account/privacy **NOT VERIFIED** |
| Wonderlog | [Step3 #26](https://github.com/riccardopinato/Wonderlog/pull/26) | Pilota Trip Planner già integrato, **non nello scope dello store Notes/Anna** | La CI Step3 non costituisce QA device |

**Separazione di evidenza:** progetto UX approvato → codice in branch/PR → CI head PASS → merged `main` → runtime/device PASS → Store READY. Gli stati non si implicano a vicenda. I tre writer canonici non sono stati duplicati. I merge Step4 Notes e Anna sono confermati sopra; CI del commit `main`/Web dopo merge, dispositivi, backup/account e Store sono evidenze distinte dalla CI sul PR head.

**Confini:** nessun file ZIP, template, media, formula o copy Notion commerciale redistribuito. Nessun Catalog DB, install tracker, account/billing, patch Vault/Noi, Golden o CAP promossi. I preset FREE non vengono monetizzati retroattivamente. Il prezzo di €3,99 è una sola ipotesi di prodotto per template premium **nuovi, originali, di valore aggiunto**, che necessitano approvazione, design UX e validazione acquisto/revoca/ripristino separata.

**Esito Step4:** sviluppo e merge delle due PR native completati, test e build Web sul PR head verificati. **Prossimi gate:** verificare separatamente i workflow post-merge su `main`, QA su device e backup/account, definire veri premium pack originali e raccogliere approvazione prodotto/design prima di una UX di commercio.

Factory baseline fissata: App-Factory-Core `d4ed1185d36d419228fba6b57a979cde308bd321` (Master v27, Golden Index v29).
