# Maxi-step 4 — Catalogo native free-first (Notes / Anna)

**Decisione:** autorizzato il 09/11/2026 il passo successivo dopo le integrazioni native gratuite Step3. La proposta di `Template Store` a pagamento rimane **BACKLOG DI PRODOTTO**: nessuno SKU, prezzo attivo, checkout, acquisto/ripristino o entitlements cross-app sono stati autorizzati in questo passaggio.

| App | PR sorgente | Integrazione prevista | Evidenza valida |
|---|---|---|---|
| Notes-Ecosistema | [#97](https://github.com/riccardopinato/Notes-Ecosistema/pull/97) | `TemplatesScreen`: sezioni "Catalogo" di preset gratuiti e "I miei" modelli derivati solo da `PersonalTemplates.catalog` | Da verificare sul commit esatto: analyze/test/build Web e schermate, account/backup su device |
| Anna's Diary | [#291](https://github.com/riccardopinato/Agenda-per-Anna/pull/291) | `showDiaryTemplatePicker`: sei `DiaryTemplatePreset` originali gratuiti, preview seedText/mediaHint e consenso "Usa nel diario", poi editor canonico | Da verificare sul commit esatto: Development/Web/UI5 gate e privatizzazione/account/device |
| Wonderlog | [Step3 #26](https://github.com/riccardopinato/Wonderlog/pull/26) | Pilota Trip Planner già integrato, **non nello scope dello store Notes/Anna** | La CI Step3 non costituisce QA device |

**Separazione di evidenza:** progetto UX approvato → codice in branch/PR → CI head PASS → merged `main` → runtime/device PASS → Store READY. Gli stati non si implicano a vicenda. I link PR sono la fonte dinamica finché i merge non sono confermati.

**Confini:** nessun file ZIP, template, media, formula o copy Notion commerciale redistribuito. Nessun Catalog DB, install tracker, account/billing, patch Vault/Noi, Golden o CAP promossi. I preset FREE non vengono monetizzati retroattivamente. Il prezzo di €3,99 è una sola ipotesi di prodotto per template premium **nuovi, originali, di valore aggiunto**, che necessitano approvazione, design UX e validazione acquisto/revoca/ripristino separata.

**Prossimi gate:** concludere e verificare PR #97 e #291, QA su device e backup/account, specificare i veri premium pack originali e ottenere approvazione di prodotto/design prima di un'eventuale UX di commercio.

Factory baseline fissata: App-Factory-Core `d4ed1185d36d419228fba6b57a979cde308bd321` (Master v27, Golden Index v29).
