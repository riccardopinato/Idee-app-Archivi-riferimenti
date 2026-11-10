# Step 7 — Prototipi interattivi originali Notes / Anna

**Data:** 10/11/2026. **Factory baseline pin:** `App-Factory-Core@2953e9b50f5f43fbd5a1702cb41785a4235592a5`, Master v27, Golden Index v29. Tutte le fonti sono interne ai repository e nessun contenuto Notion di terzi è copiato.

## Risultati realmente integrati

| Consumer | Prototipo navigabile (HTML standalone) | Specifica UX e privacy | PR / commit main | Evidenza e confini |
|---|---|---|---|---|
| Notes-Ecosistema | [Study Sprint Studio](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/docs/TEMPLATE_NOTION/UX_STEP7/PROTOTIPO_STUDY_SPRINT_STUDIO.html) | [UX draft e gate](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/docs/TEMPLATE_NOTION/UX_STEP7/README_STUDY_SPRINT_STUDIO.md) | [PR #100](https://github.com/riccardopinato/Notes-Ecosistema/pull/100) MERGED, `main@09fbd28728178078fa281f5a0010b50ca1eb5375` | Documento + HTML statico navigabile: fonte manuale, argomenti, preview, conferma simulata. Nessun writer, AI, store, pagamento, runtime CI specifico di questa UX. |
| Anna's Diary | [Dodici settimane che contano](https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/TEMPLATE_NOTION/UX_STEP7/PROTOTIPO_DODICI_SETTIMANE.html) | [UX draft e gate](https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/TEMPLATE_NOTION/UX_STEP7/README_DODICI_SETTIMANE.md) | [PR #298](https://github.com/riccardopinato/Agenda-per-Anna/pull/298) MERGED, `main@8bfb4bcd58e820c995bd913e2c8f08c223c2b45d`; HEAD `f32ef532bf7b4f9882c2122aa895b2de09f1dcfe` | `check` e `UI5 source and visual-flow contracts` SUCCESS su HEAD. HTML simulato non integrato nel diario, no data/device QA. |

**Decisione di prodotto:** entrambi i manifest Core restano `research_candidate`. I mockup sono `UX_DRAFT_PENDING_APPROVAL`: il merge della documentazione non implica approvazione UX/commerciale né autorizza checkout, SKU, RevenueCat product o Cloud. L'applicazione Flutter richiede una decisione prodotto separata e un adapter ai writer canonici per ogni app.

## Contesto Free verificato

- Notes [PR #99](https://github.com/riccardopinato/Notes-Ecosistema/pull/99) MERGED `main@b119180e4eca578f055dd55d75cfb0d7d6d806f5`, PR HEAD `a7366b6b2ddb5756a464124261f5d9c6876a58c8`. I check `verify`, `verify-web`, `build-web` sono SUCCESS; [Deploy Web preview #42808861763](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/42808861763) SUCCESS a questo commit (non prova di test manuale del browser). Il codice rimuove `\\n` letterali e applica ricerca a tutti i preset gratuiti.
- Anna galleria dei sei template gratuiti già in main, invariata dalla PR #298.
- Wonderlog Trip Planner gratuito già in main, invariato. Google/cloud sospesi secondo decisione utente.

## Come valutare i due prototipi

Gli HTML sono interattivi ma **GitHub mostra normalmente il sorgente**: il tester può aprire il file nel repository, usare **Raw/Download** e aprire la copia `.html` in un browser. Nessuna API, backend, credential, localStorage o account richiesto. Il comportamento simulato non prova il rendering nella reale app Flutter.

**Domande decisionali UX (senza riformulare lo Store):** preferire un percorso Studio assistito a una nota unica o un multi-writer confermato? Per Anna, navigazione per capitoli o timeline? La data di inizio è opzionale? Le domande settimanali sono adatte all'identità del diario? Solo dopo approvazione esplicita: valutare un adapter **limitato e non-billing**, in PR separata, con idempotency receipt, rollback, private owner e test.

## Evidence ladder

- Manifest statici JSON di quattro pack originali: Core PR #90, schema/static CI **PASS**; nessun adapter.
- UX clickable draft HTML: **SOURCE MERGED** nei due repo; su Anna anche PR CI **PASS**. L'esecuzione manuale nel browser del tester rimane **NOT VERIFIED**.
- Product/UX approval: **PENDING**; Flutter runtime, esercizio utenti, acquisti, restore, physical QA: **NOT IMPLEMENTED / NOT VERIFIED**.
- Nessuna promozione Donor/Golden, SKU o CAP. Nessun cambiamento a Master, Registry, Supabase o repository Wonderlog.

La roadmap [Step6](STEP6_MANIFEST_ORIGINALI_2026-11-10.md) rimane valida: dopo approval UX, primo adapter Notes e poi Anna, sempre con le verifiche e i vincoli proprietari di ciascuna app.
