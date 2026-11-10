# Step 6 — Quattro template originali: manifest di ricerca e riuso nativo

Data: 10 novembre 2026. Factory baseline della sessione: App-Factory-Core@d4ed1185d36d419228fba6b57a979cde308bd321, Master v27, Golden Index v29. La baseline operativa non è ricaricata dopo il merge dello step.

## Cosa è stato realmente integrato

[Core PR #90](https://github.com/riccardopinato/App-Factory-Core/pull/90) MERGED su main@2953e9b50f5f43fbd5a1702cb41785a4235592a5; source-head 6cd1bd151d72112e4176976b0462a45cf988fbed con check validate PASS.

Quattro file JSON nuovi nel percorso Core contracts/template_engine_v1/examples:

- notes_project_launch_studio_research.json — Notes Project Launch Studio
- notes_study_sprint_studio_research.json — Notes Study Sprint Studio
- anna_memory_atlas_research.json — Anna Atlante dei ricordi
- anna_twelve_week_reflection_research.json — Anna Dodici settimane che contano

Ogni manifest è research_candidate, con cinque/sei traduzioni, compatibilità dichiarativa, configurazioni limitate, preview synthetic generated_in_app, scope private, conferma esplicita e removal detach_keep_user_data. Il campo paid_once è un'ipotesi di commercializzazione, l'entitlement_key è un nome logico e NON uno SKU.

Il validatore centrale verifica solo schema/dati e anti-regressione. Gli adapter dichiarati sono NOMI DI CONTRATTO NON IMPLEMENTATI. Non esiste un'app Store Premium, né quattro prodotti installabili. Non dichiarare product_approved, paid entitlement, consumer runtime, E5 Golden o disponibilità Web/iOS/Android senza nuovi test e gate. Nessuna copia di testi/asset Notion.

## Cataloghi gratuiti e Wonderlog

- Notes-Ecosistema [PR #99](https://github.com/riccardopinato/Notes-Ecosistema/pull/99): corregge la ricerca del catalogo e newline letterali nei quattro modelli Free e nel Daily. È un cambio sorgente con test; verificare l'esito finale CI/merge/deploy separatamente, senza inventare PASS.
- Anna's Diary: sei template di diario gratuiti e preview nativa già in main, invariati; confini privato/Vault/Noi preservati.
- Wonderlog: pilota Trip Planner già in main, invariato. Bug Web risolto in PR #29, Pages [run #42719570479](https://github.com/riccardopinato/Wonderlog/actions/runs/42719570479) build/deploy/live assets PASS. Login Google/cloud resta SOSPESO per decisione utente.

## Prossimi 5 maxi-step

1. UX approvazione mirata: primo concept Notes Study Sprint Studio, primo Anna Dodici settimane che contano. Preview e diff su dati sintetici, valutazione UX e Product Bible; nessuna mutazione dati.
2. Adapter Notes pilota, con Note/Task canonici, receipt durevole idempotente, staged validation, failure rollback e test di backup. Niente nuova base dati o clone Notion.
3. Adapter Anna pilota, con DiaryBlock privati, date opt-in, nessun reminder automatico, nessun Vault/Noi o cross-account scope. Test Annulla e ripetizione.
4. QA runtime Web + browser, dispositivo, profilo/account isolato, restore e verifiche privacy; separare CI da accettazione reale.
5. Valutazione commerciale distinta: soltanto con approvazione esplicita, UX soddisfacente, diritti e proof si implementeranno billing e Store. Prezzo 3,99 euro ancora ipotetico.

Registro precedente: [4 priorità eseguite](EXECUTION_4_PRIORITIES_2026-11-09.md) e [blueprint dei 4 pack](BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md). Non promuovere Golden/CAP da semplici manifest.
