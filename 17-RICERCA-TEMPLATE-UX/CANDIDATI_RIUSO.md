# Candidati di riuso — senza nuova CAP o Golden

| ID locale ricerca | Pattern | Ownership tecnico suggerito | Consumer | Stato e prova necessaria |
|---|---|---|---|---|
| TPLUX-001 | Catalogo e preview di template guidati | Estendere `PersonalTemplates`/editor canonico; Anna `diaryTemplatePresets` | Notes, Anna | **PROPOSTA**; verificare UX e dati originali dei template |
| TPLUX-002 | Vision Board come preset canvas | Notes `WhiteboardDocument`; Anna sketchbook/memories, scope per tipo di record | Notes, Anna | **PROPOSTA**; fare riferimento a `15-VISION-BOARD`, niente doppio motore |
| TPLUX-003 | Card Home/preset visuali | Notes UI5, Anna DS6 / `AgendaPreferences` | Notes, Anna | **PROPOSTA**; visual gate Notes #85 e custom colors compatibilità |
| TPLUX-004 | Obiettivi e review contestuale | Note/Task del planner; Anna rituali e weekly review esistenti | Notes, Anna | **PROPOSTA**; solo contatori derivati e interazione opt-in |
| TPLUX-005 | Mini-planner condiviso limitato | Anna `Noi ♡` / issue #225 | Anna | **PROPOSTA**; permessi espliciti e authorizations reali |
| TPLUX-006 | Second Brain / area-resource views | Notes Knowledge Graph/Project Workspace | Notes | **PROPOSTA**; non duplicare store né importare CRM in Anna |
| TPLUX-007 | Ricerca studio e review su Web | Notes Study Core / issue #47 | Notes | **PROPOSTA**; QA parity e prova origine del contenuto |
| TPLUX-008 | Review giorno con durata/buffer | Anna `realistic_day_advice.dart` / issue #226; Notes Planner | Notes, Anna | **PROPOSTA**; durata deve essere registrata, no inferenza dal task count |

Prima di creare qualunque CAP nuova o segnare 'già integrato' eseguire deduplicazione rispetto a `12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json` e controllo consumer esatto. Gli ID `TPLUX` non sono CAP.
