# Crosswalk tecnico: pattern UX, sorgenti e gap

**Data**: 09/11/2026. Audit dei sorgenti alle revisioni appuntate nel [README](README.md). `SOURCE CONFIRMED` significa classe/funzione presente; NON prova la parità Web, l'integrazione end-to-end, i test fisici o un'esperienza visiva approvata.

| Pattern | Notes: sorgente verificata | Anna: sorgente verificata / confine | Delta proposto, non ancora deciso | Gate |
|---|---|---|---|---|
| Template contestuali / catalogo | `flutter_app/lib/src/domain/templates.dart` contiene `PersonalTemplates`, `PageTemplates`, `TemplateContent` | Diario e rituali riusano template canonici (`lib/src/daily_rituals.dart`) | Metadati di preset, anteprima, setup opzionale, localizzazione; NON nuovo owner dati | Snapshot preview, undo, import validato, scadenze visuali |
| Second Brain / PARA | Knowledge, Project Workspace e Knowledge Graph già presenti; non dichiarare PARAfied UX completa | Product Bible esclude clone di Notion, CRM e gestione professionale | Notes: relazioni tra Aree/Progetti/Risorse come viste derivate; Anna: raccolte personali soltanto se pertinenti | Provenienza, dati canonici, no duplicazione |
| Inbox → next action | `smart_inbox_source_preview.dart`, `smart_inbox_project_action.dart`, Planner; **#46 aperta**, multi-store non serializzato | `Unified Capture` come unica cattura; evitare GTD professionale | Notes: completare percorso affidabile senza attivare codice QA in production | #46, transaction coordinator, revoca permessi, account switch, fault injection |
| Planner settimanale / time-block | `planner.dart` ha `PlannerView`, `TimeBlock`; Workspace progetti | `realistic_day_advice.dart`, `weekly_review.dart`; **#226 aperta** | Durata canonica, buffer e vista settimanale con azioni reversibili | Nessun "task count = durata"; rispetto calendario, turni, locale |
| Studio / ripasso | `study.dart` definisce `LearningItem`, `StudyScheduler` e queue; Web parziale | Studio professionale fuori Product Bible | Notes: surface Study Web, risorse, source-linked flashcards e stato consistente | #47, Web functional tests, provenance fonti |
| Habits / Goals | Planner + workflow automation esistenti; owner habit generale da verificare | `v1.01` preset moduli, Daily Rituals e review; funzionalità già presenti | Obiettivi collegati a task/rituali, con riuso senza second DB | Nessuna streak inventata; preferenze account e backup |
| Diario, riflessioni, ricordi | Diario opzionale; rischio duplicazione rispetto ad Anna | DiaryBlock, ritmi, ricordi, Life Threads; **#224 aperta** | Anna: prompt editoriali opzionali e richiamo fonte; Notes: solo bisogno professionale/creativo specifico | Privacy First, Vault invariato, opt-in, provenance |
| Vision board | `visual_documents.dart`: WhiteboardDocument, BoardNode sticky/noteLink/taskLink | Sketchbook, foto, ricordi; non certifica Vision Board | Preset **sugli editor esistenti**, consumer distinti; riusare ricerca in `15-VISION-BOARD` | Privato vs Noi ♡, media rights, export, no secondo canvas |
| Temi / Home modulare | Home UI5/Nav hanno implementazioni ma **#85** visual/default-on gate aperta | UI DS6/HSV e `AgendaPreferences` con personalizzazione reversibile | Migliorare token/card/preset, non sostituire UI approvata | 320–1280dp, a11y, scale text, backup e visual approval |
| Planner condiviso di coppia | Non necessario al core Notes | `Noi ♡` e **#225** mini-planner autorizzato da definire | Solo eventi e task esplicitamente condivisi, senza schema professionale | ACL owner/member, scope, revoca, account switch |

## Ordine di sviluppo consigliato
1. Chiudere sicurezza della persistenza Web Notes prima di grandi importazioni: Step 1 corrente è **snapshot browser localStorage**, non IndexedDB.
2. Per Notes mantenere la roadmap esistente: **Smart Inbox #46 → Project Intelligence #51 → UI5 #85 / Study #47**, evitando nuove implementazioni che si sovrappongano.
3. Per Anna valorizzare prima **Realistic Day #226**, **Noi mini-planner #225** e ricordi spiegabili **#224** con decisioni per privacy e UI.
4. Vision Board e template sono **esperimenti UX** finché non c'è preview verificata e decisione prodotto.
5. Nessuna promozione Donor/Golden per un semplice riferimento esterno: usare il **Provenance Reuse Ledger** e i gate App Factory.

## Stato esplicito
**Audit sorgente campionato** su file canonici e issue aperte. Non eseguiti test nuovi né aperta la libreria commerciale privata. I gap sono ipotesi verificabili, non ticket implementativi approvati automaticamente.
