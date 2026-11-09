# Maxi-step 2 — Tre UX nativi per i template App Factory

**Stato: DESIGN DRAFT / ATTESA APPROVAZIONE UTENTE.** Le PR documentali sono state integrate. NON sono template installati, app Flutter aggiornate, Store attivi né Golden certificati.

| App | Fonte | Proposta originale | UX + demo standalone | PR | SHA main |
|---|---|---|---|---|---|
| Notes | TPLUX-REF-0004 Book Tracker | **Biblioteca di lettura gratuita**, una singola nota modificabile con sezioni | [Prototipo Notes](https://github.com/riccardopinato/Notes-Ecosistema/tree/main/docs/TEMPLATE_NOTION/UX_STEP2) | [#95](https://github.com/riccardopinato/Notes-Ecosistema/pull/95) merged | 0c5777ef9d47a8fe52dd35e126ce58c19722c655 |
| Anna's Diary | TPLUX-REF-0002 Routines Activities | **Rituali gentili** gratuiti, privacy privata, riuso rituali e DiaryBlock | [Prototipo Anna](https://github.com/riccardopinato/Agenda-per-Anna/tree/main/docs/TEMPLATE_NOTION/UX_STEP2) | [#286](https://github.com/riccardopinato/Agenda-per-Anna/pull/286) merged | f4b2baf95e062777da4ad23c0e40bbf8ed8cb6c1 |
| Wonderlog | TPLUX-REF-0011 Trip Planner | **Piano di viaggio leggero**, un Journey canonico con sezioni testuali, no routing/booking/budget reali | [Prototipo Wonderlog](https://github.com/riccardopinato/Wonderlog/tree/main/docs/TEMPLATE_NOTION/UX_STEP2) | [#25](https://github.com/riccardopinato/Wonderlog/pull/25) merged | 66c93cfb5157b84e697a089322b93f9440702b4e |

## Verifica di prodotto

- Notes: il codice attuale espone PersonalTemplates, TemplatesScreen e Note; un Books DB NON è una feature dimostrata dal materiale.
- Anna: DailyRitualKind.morning/evening, startDailyRitual e DiaryTemplatePreset esistono; nessun secondo habit tracker, streak, condivisione Noi ♡ o modifica al Vault.
- Wonderlog: JourneyRepository.createJourney prende titolo/destinazione/date e descrizione; non ci sono budget/packing di prima classe nel model Journey. Il gate Premium esistente resta vincolante.
- Tutti i prototipi HTML sono originali, con dati fittizi, senza import Notion, billing, accesso a DB o modifiche utente. Sono esempi di design, non test device Flutter.

## Decisioni e prossimo gate

1. Mostrare i tre prototipi e raccogliere **approvazione UX esplicita**, separata dallo stato GitHub MERGED.
2. Se approvati, scegliere un pilota gratuito e specificare adapter, scope, writer, idempotenza, validazione, rollback e QA in Maxi-step 3.
3. Il prezzo ipotetico €3,99 rimane riservato a template premium originali di valore aggiuntivo; non rivendere le funzioni gratuite o i file Notion di terzi.
4. App Factory Core Template Engine Standard v1 resta static-only: [contratto](https://github.com/riccardopinato/App-Factory-Core/tree/main/contracts/template_engine_v1), SHA d4ed1185d36d419228fba6b57a979cde308bd321.

**Questa matrice non promuove i template allo stato APPROVATO e non cambia la roadmap di alcuna app.**
