# Audit stelle GitHub 750 — delta autentico, idee per app e deduplica CAP (16 novembre 2026)

## Scope e fonte verificabile

- L’utente riferisce 750 stelle nel profilo. GitHub API pubblica ha enumerato **737 repository**, su 8 pagine [100,100,100,100,100,100,100,37]. Le altre 13 non sono identificabili dal connettore pubblico.
- Snapshot storico di ottobre: **632** repo. Intersezione 627; **110 nuove nel confronto insiemistico**; 5 vecchie non più presenti nel set pubblico. Assenze non equiparabili a rimozione stella accertata.
- **110 README letti/estratti** con commit HEAD e blob README quando possibile. Questo è inventario E0, non audit integrale codice/test/licenza per file.
- **89 delle 110** erano già nell'audit OSS95 dell'8 novembre 2026. Di queste, 70 README conservano hash identico e 19 hanno hash diverso o precedente mancante. 4 ulteriori fonti avevano audit separato: GBrain, Deskland, OpenTaskbar, LumaBar.
- **17 fonti non risultavano in quei precedenti dossier**; non nasce per questo automaticamente alcuna nuova CAP, roadmap, Golden, app o donor certificato.

Fonti: [censimento 110](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/audit/stars-750-20261116/research/STARS_INCREMENTAL_2026-11-16.md), [classifica curata 110](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/audit/stars-750-20261116/research/CLASSIFICA_CURATA_110_2026-11-16.md), [classifica 737](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/audit/stars-750-20261116/research/STARS_ALL_2026-11-16.md), [crosswalk OSS95](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github/blob/audit/stars-750-20261116/research/INCROCIO_OSS95_2026-11-16.md). Baseline Factory `c5adc147046beb7024629466d10eeb799c3c2619`; registro canonicale esaminato: **199 CAP / 48 nomi app**.

## Le 17 fonti veramente non classificate nei precedenti dossier controllati

| Repository | Score opportunità | Dominio | Consumer candidato | Licenza GitHub (metadato) | Stato |
|---|---:|---|---|---|---|
| [MobSF/Mobile-Security-Framework-MobSF](https://github.com/MobSF/Mobile-Security-Framework-MobSF) | 98 | QA e sicurezza | AppLab | GPL-3.0 | E0/DA_VALUTARE |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | 97 | QA e sicurezza | AppLab | Apache-2.0 | E0/DA_VALUTARE |
| [github/codeql](https://github.com/github/codeql) | 96 | QA e sicurezza | AppLab | MIT | E0/DA_VALUTARE |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | 95 | QA e sicurezza | AppLab | LGPL-2.1 | E0/DA_VALUTARE |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | 94 | Agenti e App Factory | App-Factory-Agent-Core | MIT | E0/DA_VALUTARE |
| [alztrk/OpenWidget](https://github.com/alztrk/OpenWidget) | 89 | Desktop e widget | App Factory Control Center | MIT | E0/DA_VALUTARE |
| [zaproxy/zaproxy](https://github.com/zaproxy/zaproxy) | 84 | QA e sicurezza | AppLab | Apache-2.0 | E0/DA_VALUTARE |
| [ai-boost/awesome-image-video-prompts](https://github.com/ai-boost/awesome-image-video-prompts) | 81 | Design e workflow visuale | Notes-Ecosistema | GPL-3.0 | E0/DA_VALUTARE |
| [tonhowtf/omniget](https://github.com/tonhowtf/omniget) | 81 | Agenti e App Factory | App-Factory-Agent-Core | GPL-3.0 | E0/DA_VALUTARE |
| [greenbone/openvas-scanner](https://github.com/greenbone/openvas-scanner) | 75 | QA e sicurezza | AppLab | GPL-2.0 | E0/DA_VALUTARE |
| [onmyway133/Promptberry](https://github.com/onmyway133/Promptberry) | 75 | Agenti e App Factory | App-Factory-Agent-Core | MIT | E0/DA_VALUTARE |
| [SonarSource/sonarqube](https://github.com/SonarSource/sonarqube) | 74 | QA e sicurezza | AppLab | LGPL-3.0 | E0/DA_VALUTARE |
| [exo-explore/exo](https://github.com/exo-explore/exo) | 71 | Agenti e App Factory | App-Factory-Agent-Core | Apache-2.0 | E0/DA_VALUTARE |
| [PaoloJN/recap](https://github.com/PaoloJN/recap) | 65 | Produttivita e privacy | FocuSense | MIT | E0/DA_VALUTARE |
| [SunshineStream/Sunshine](https://github.com/SunshineStream/Sunshine) | 55 | Desktop e widget | Send-to-PC | GPL-3.0 | E0/DA_VALUTARE |
| [20220402jp-coder/attendance-management-system](https://github.com/20220402jp-coder/attendance-management-system) | 40 | Non pertinente | Nessuna | NOASSERTION | E0/DA_VALUTARE |
| [Cracked5pider/Ekko](https://github.com/Cracked5pider/Ekko) | 10 | Non pertinente | Nessuna | NOASSERTION | E0/DA_VALUTARE |

**Score /100:** giudizio qualitativo di priorità relativa, NON probabilità di integrazione. Le fonti GPL/AGPL/LGPL e quelle senza licenza verificata restano referenze prima di qualunque riuso. Fonti con codice pubblicato non equivalgono a componenti copiabili o già testati.

## Mappa per applicazione: nuovi spunti vs CAP già esistenti

| Consumer | Priorità | Fonti | CAP / stato attuale | Raccomandazione audit (non decisione approvata) |
|---|---|---|---|---|
| AppLab | P1 | MobSF + Trivy + CodeQL + Semgrep | CAP-0068 (evidence ladder) | Aggiungere un lane di sicurezza report-only su APK/AAB, CVE/SBOM, secrets e analisi statica, con triage falsi positivi. Non integrare motori GPL nel prodotto senza licenza; non dichiarare certificazione Android senza device. |
| App-Factory-Agent-Core | P1 | OpenHands / Agent Canvas | Catalogo governance Agenti e donor già esistenti | Confrontare controllo agenti multi-backend, isolamento Docker/VM, autorizzazioni e code di job; non sostituire l’agente né GBrain senza piano di migrazione. |
| App Factory Control Center | P1 | alztrk/OpenWidget e xyflow/xyflow | CAP-0023/0024; dashboard e provenance esistenti | Surface desktop con widget stato PR/CI e un grafo di dipendenze, aggiornamenti pull-based e dati GitHub autorizzati; evitare nuova source-of-truth. |
| Notes-Ecosistema | P1 | AppFlowy Editor, AFFiNE, Nodus, Memry, tldraw, Excalidraw | CAP-0028, CAP-0029, CAP-0094, CAP-0098, CAP-0149, CAP-0161, CAP-0167 | Canvas ibrida, blocchi su canvas, elementi vivi con ID canonici, export roundtrip. Il motore già implementato va esteso, non duplicato; tldraw SDK e AGPL/MPL soggetti a licensing. |
| Notes-Ecosistema | P1 | whisper.cpp, Prismical, Meetily, NoteGen | CAP-0031, CAP-0074, CAP-0085, CAP-0095 | Voice-to-note opzionale, diarizzazione e action-items controllati; modelli distribuiti separatamente per evitare APK grandi e privilegiare consenso/privacy. |
| Agenda-per-Anna | P1 | andstatus/todoagenda, Orange Schedule, Pikos | CAP-0144, CAP-0182, CAP-0002, CAP-0175 | Widget Android per prossimi eventi e filtri, sticky giornalieri desktop dove applicabile, quick capture e timeboxing senza doppio calendario; usare privacy mask. |
| Notes-Ecosistema | P2 | AnkiDroid e Anki | CAP-0112 | Ripasso dilazionato legato alle note originali, con ID e fonte; non copiare GPL e non creare un secondo database flashcard se già presente. |
| FocuSense | P2 | ActivityWatch, WakaTime CLI, projecthamster | CAP-0176, CAP-0177, CAP-0109 | Statistiche locali focus/app time con consenso esplicito, granularità minima, senza monitoraggio invasivo; prima audit permessi/OS. |
| Design-App | P2 | tldraw, Excalidraw, Markmap, xyflow, OpenWidget | CAP-0023, CAP-0024; Design-App registry | Reference per canvas, motion, grafi, preview, HUD e icone. Conservare provenienza; nessun codice cross-platform copiato senza file-level license. |
| FrameLab | P3 | ai-boost/awesome-image-video-prompts | CAP-0082 o ricerca editoriale | Catalogo di idee prompt come ispirazione, NON motore AI/API né dipendenza. Priorità sotto bug/runtime esistenti. |
| Send-to-PC | P3 | SunshineStream/Sunshine | Nessuna implementazione approvata | Streaming desktop a bassa latenza come concetto distinto dal trasferimento file: non introdurre nelle release attuali. |
| TrailPath / CamperBoss / Wonderlog | FUORI_SCOPE_PER_QUESTO_LOTTO | Nessuna nuova fonte di routing verificata | CAP-0048, CAP-0087, ecc. | Il ranking automatico associava erroneamente OpenProject/Markmap a mappe; nessun nuovo motore GPS certificato da queste stelle. |

## Azioni da NON eseguire automaticamente

- NON promuovere CAP-0031 o CAP-0112 a 'nuove': voice offline e flashcard sono già catalogate. Stesso per CAP-0098 mind map, CAP-0144 widget, CAP-0161 editor, CAP-0167 CRDT, CAP-0182 sticky calendar.
- NON importare AppFlowy AGPL, Saber GPL, MobSF GPL o upstream Deskland GPL come codice commerciale senza valutazione legale; appflowy-editor README dichiara doppia AGPL/MPL. Repo lumabar proprietario non fornisce codice OSS.
- NON lanciare scanning web/reti su host terzi; non installare motori agent o nuovi backend senza richiesta specifica, privacy e sicurezza.
- NON editare direttamente source code, roadmap, Golden o product decision delle app durante questa ricerca.

## Prossimo gate di ammissione reale

Le proposte per AppLab (security scan stack) e agent self-hosted OpenHands possono giustificare una **nuova responsabilità CAP** solo dopo anti-dedup semantico di tutto il registro e kit a sei file con codice/ref/licenza/test. I visual pattern per Notes, Anna e Design-App vanno invece prima accorpati agli ID esistenti e collaudati per delta, evitando architetture parallele. Il catalogo resta a 199 CAP fino a evidenza/approvazione.
