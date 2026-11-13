# Intake visuale App Factory — 13/11/2026

**Sorgente verificata per i file di riferimento**: [Design-App, registro JSON di 66 immagini](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/REGISTRO_RIFERIMENTI_UTENTE_2026-11-13.json), [catalogo descrittivo](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/RIFERIMENTI_UTENTE_2026-11-13.md), [matrice per app](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/MATRICE_APP_RIFERIMENTI_2026-11-13.md). Allegati utente: 77, di cui 66 SHA-256 diversi e 11 ripetizioni esatte. Introdurre come **reference**, non come codice o asset autorizzati alla distribuzione.

## Differenziale rispetto alle capability esistenti (main 13/11/2026)

Il registro canonico consultato è `12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json` (199 record, ultimo aggiornamento dichiarato 08/11/2026). Questo intake **non modifica** il registro canonico, gli stati di app, score CAP, i kit, Golden o roadmap: prima si deduplicano le responsabilità funzionali e si raccolgono prove puntuali.

| Direzione di riuso candidata | Fonte visuale (nuovi ID Design-App) | CAP esistente / gap | App da valutare | Stato/gate |
|---|---|---|---|---|
| Theme presets, scale cromatiche e semantic design tokens | UIR-0036–0048; UIR-0071–0072; UIR-0085–0093 | **CAP-0023** Design System Flutter token-first; **CAP-0041** per estrazione palette da fotografie, non equivalente all'applicazione tema | Anna's Diary, Notes, Battery Guard, World Days | RICERCA: validare leggibilità, brand e contrasto; nessuna nuova CAP per sole varianti di colore |
| Stati di focus, elevazione, accessibilità e visual regression | UIR-0049, UIR-0064–0072, UIR-0086–0088 | **CAP-0023**, **CAP-0024**, **CAP-0025**, **CAP-0069** | tutte le app Flutter | Candidato a specifiche/kit esistenti; validare test su dispositivo e regressioni |
| Rotary Input / knob con input touch+keyboard e aptica | UIR-0053–0061 | Nessuna equivalenza diretta verificata nella lista CAP; possibile nuovo contratto *solo dopo audit funzionale* | Deskland, SleepMax Coach, FocusSense | REFERENCE_ONLY, progettare stato semantico e test di gesture/48dp/reduced motion |
| Soft 3D / Neumorphic dashboard tiles | UIR-0050–0052, UIR-0066–0069, UIR-0074–0077 | **CAP-0023** e **CAP-0025** coprono fondamenta; widget OS **CAP-0144** non equivale a bento dashboard interna | Deskland, FocusSense, App Factory Dashboard | Nessuna donor di codice certificata; benchmark su telefoni/desktop |
| Modular Daily Journal (umore, abitudini, acqua, sketch) | UIR-0062 | Adiacente a memorie e widget; non assumere copertura dalla sola **CAP-0193** (CLI diario testuale) | Anna's Diary, Notes | Audit delta su Product Bible/repo prima di creare capability o roadmap; privacy e dati canonici |
| Scene backgrounds/paper cut/illustrated covers | UIR-0078–0084; UIR-0094–0101 | **CAP-0082** artwork deterministico; non copre automaticamente parallax interattivo o artwork di terzi | Deskland, Wonderlog, Cooking Anime, World Days | Sfondi originali, licenza e provenienza culturale, fallback statici; animazione solo dove funzionale |
| Layout responsive e widget ambientali contestuali | UIR-0074–0077 | **CAP-0025** responsive, **CAP-0144** widget OS, **CAP-0182** sticky desktop; responsabilità diverse | Deskland, App Factory Dashboard, CamperBoss | Test funzionali e risorse, distinguere launcher/widget interno/OS |

**Nota ID**: `UIR-0036` è il primo elemento del lotto, `UIR-0101` l'ultimo. Le famiglie UI/UX e i punteggi 0–100 nel catalogo sono euristiche estetiche: non sono i punteggi decisionali del registro CAP e non devono essere riportati come tali.

## Priorità di audit, non di implementazione

1. **P1 — Compatibilità Anna's Diary**: Vivid Journal e Lilac devono restare opzionali/di componente, preservando lo stile editoriale rose Manrope/Lora approvato. Dati e sync invariati.
2. **P1 — Deskland**: visualizzare glass dashboard, rotary/tactile controls, ambient landscape senza introdurre jank, consumi eccessivi o invasività del launcher.
3. **P1 — Factory-wide Flutter tokens**: usare CAP-0023 come contratto esistente; nuovi design system devono diventare varianti di token, non duplicati runtime.
4. **P2 — Notes**: applicare pattern decorativi solo fuori dall'area primaria di scrittura/disegno; controlli tastiera, zoom e leggibilità prima degli effetti.
5. **P2 — Cooking Anime / Wonderlog / World Days**: cover e palette editoriali pertinenti; diritti verificati, nessuna copia di opere o marchi di terzi; preservare colori World Days correnti.

## Donor, Golden e attestazioni

- **DONOR**: 0 nuovi donor di codice verificati. Immagini e Pinterest non costituiscono sorgenti importabili.
- **GOLDEN**: 0 Golden promossi o modificati; referenze non hanno CI, test UI/widget né evidenze source.
- **CAP canoniche**: 0 aggiunte o cambiate. Registro e viste generate non toccati; nessuna rigenerazione necessaria.
- **Licenze**: immagini di terzi senza evidenza di ridistribuzione autorizzata = `REFERENCE_ONLY`. Non si copiano JPG nel repo pubblico.
- **Stato**: ricerca catalogata; non è lavoro implementato né revisione delle roadmap delle app.

## Tracciabilità

Questo documento è una crosswalk tra cataloghi, non una nuova source of truth dei prodotti. Alla selezione di un componente per un'app: aprire il repo/HEAD e Product Bible relativi, verificarne il delta con i CAP già esistenti, proporre task approvati e validare CI/accessibilità/device. Evitare conteggi cumulativi che confondano i precedenti 33 visual con i nuovi 66.

## Consolidamento relazionale (12–13 novembre 2026)

L'intake del 13/11 aggiunge 66 visual distinti ai 33 già presenti in Design-App (totale 99). Consultare la [matrice trasversale di 19 app e 28 stili](MATRICE_VISUAL_APP_STILI_2026-11-13.md) e il [registro canonico delle 254 associazioni stile–app](https://github.com/riccardopinato/Design-App/blob/main/UI-UX/MATRICE_BIDIREZIONALE_APP_STILI_2026-11-13.json). Stato delle associazioni: PROPOSTA, senza automatica introduzione nel backlog CAP o nelle app.
