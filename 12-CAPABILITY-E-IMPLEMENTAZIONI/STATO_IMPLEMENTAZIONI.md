# Stato delle implementazioni — audit 2026-11-01

Gli stati sono **per app**, non globali. `SOURCE_REPORTED` indica fonte repo/audit consultata, non esecuzione del codice ne CI/DEVICE PASS verificati in questa sessione.

| Stato | Associamenti app-capability | Interpretazione |
| --- | --- | --- |
| PROPOSTA | 170 | Idea non approvata / nessun codice verificato qui |
| ROADMAP_STORICA | 16 | Indicata in roadmap o decisione storica; richiede verifica live |
| SOURCE_REPORTED | 85 | Roadmap/audit dichiara sorgente presente; non provato runtime in questo audit |
| DONOR_REPORTED | 2 | Repo donor documentato; riuso non ancora validato |
| SOURCE_CONFIRMED | 2 | Implementazione verificata con riferimento puntuale a codice e commit |
| CI_VERIFIED | 0 | CI exact-head verde per questa capability nel repository autorevole |
| DEVICE_VERIFIED | 0 | Test su dispositivo con artifact e SHA identificati |
| RELEASE | 0 | Distribuzione verificata nel canale dichiarato, non inferita dalla build |
| BLOCKED | 0 | Blocco concreto con causa e riferimento; mantenere l'idea nel catalogo |

| Capability con donor o sorgente documentata | App | Prova |
| --- | --- | --- |
| CAP-0003 Preparazione contestuale appuntamento | Agenda-per-Anna (SOURCE_CONFIRMED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/event_preparation.dart |
| CAP-0004 Overlay calendari esterni read-only | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0006 Lista della spesa privata e condivisa | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0007 Scheda workout e storico multisport | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0008 Import foto PDF delle schede workout | PDF-Unifier (DONOR_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0009 Ricordi mappa geolocalizzata | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0010 Ricordi Then and Now | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0011 Life Threads narrativi | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0012 Year in Review deterministico | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0013 Collection e ricerca locale | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0015 Ricerca globale ordinabile e un carattere | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md |
| CAP-0016 Inbox con categorie modificabili | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md |
| CAP-0017 Universal Delete Trash e lifecycle audit | Agenda-per-Anna (SOURCE_REPORTED), Notes-Ecosistema (SOURCE_REPORTED) | Backlog idee app.txt |
| CAP-0018 Backup restore con staging e rollback | Agenda-per-Anna (SOURCE_REPORTED), Notes-Ecosistema (SOURCE_REPORTED), CamperBoss (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0019 Store media content addressed e GC | Agenda-per-Anna (SOURCE_REPORTED), Notes-Ecosistema (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0020 Shared Ecosystem Bridge COPY LINK | Agenda-per-Anna (SOURCE_REPORTED), Wonderlog (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0021 QR inviti condivisi 24 ore | Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md |
| CAP-0022 Localizzazione cinque o piu lingue | Agenda-per-Anna (SOURCE_REPORTED), World-Days (SOURCE_REPORTED), app-fotografia (SOURCE_REPORTED), In-Cucina-con-gli-Anime (SOURCE_REPORTED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md |
| CAP-0023 Design System Flutter token-first | Design-App (SOURCE_REPORTED), Agenda-per-Anna (SOURCE_REPORTED), Wonderlog (SOURCE_REPORTED) | https://github.com/riccardopinato/Design-App/blob/main/registry/DESIGN_REGISTRY.yaml |
| CAP-0024 Motion reduced-motion e microinterazioni | Design-App (SOURCE_REPORTED), Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Design-App/blob/main/registry/DESIGN_REGISTRY.yaml |
| CAP-0025 Schermate responsive rail e split view | Design-App (SOURCE_REPORTED), Agenda-per-Anna (SOURCE_REPORTED), app-fotografia (SOURCE_REPORTED) | https://github.com/riccardopinato/Design-App/blob/main/registry/DESIGN_REGISTRY.yaml |
| CAP-0026 Sound feedback semantico opzionale | Design-App (SOURCE_REPORTED) | https://github.com/riccardopinato/Design-App/blob/main/registry/DESIGN_REGISTRY.yaml |
| CAP-0029 Canvas ibrida sketch sotto note | Notes-Ecosistema (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0033 Modello Needle 3 on demand Plus | Notes-Ecosistema (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0035 OCR immagini e documenti on device | PDF-Unifier (SOURCE_REPORTED), Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0037 Operazioni PDF split merge rotate lock | PDF-Unifier (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0038 PDF Pocket Tools packaging standalone | PDF-Unifier (DONOR_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0039 EXIF privacy safe copy | Android-Omni-Cleaner (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0040 Deduplicazione foto per hash percettivo | Android-Omni-Cleaner (SOURCE_REPORTED) | https://github.com/riccardopinato/Android-Omni-Cleaner/blob/main/ROADMAP.md |
| CAP-0042 Catalogo editoriale multilingua offline | app-fotografia (SOURCE_REPORTED), World-Days (SOURCE_REPORTED), In-Cucina-con-gli-Anime (SOURCE_REPORTED) | https://github.com/riccardopinato/app-fotografia/blob/main/ROADMAP.md |
| CAP-0043 Raccolta fonti contenuti e audit artwork | In-Cucina-con-gli-Anime (SOURCE_REPORTED), World-Days (SOURCE_REPORTED), app-fotografia (SOURCE_REPORTED) | https://github.com/riccardopinato/In-Cucina-con-gli-Anime/blob/main/ROADMAP.md |
| CAP-0044 Ricette anti-spreco da ingredienti | TasteAI (SOURCE_REPORTED) | https://github.com/riccardopinato/TasteAI/blob/main/docs/ROADMAP.md |
| CAP-0048 Routing sentieri trace snap affidabile | TrailPath (SOURCE_REPORTED) | https://github.com/riccardopinato/TrailPath/blob/main/docs/ROADMAP.md |
| CAP-0049 Offline map engine e routing camper | TrailPath (SOURCE_REPORTED) | https://github.com/riccardopinato/CamperBoss/blob/main/ROADMAP.md |
| CAP-0051 Mappe luoghi ricordi condivisi con ponte | Wonderlog (SOURCE_REPORTED), Agenda-per-Anna (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0055 Notifiche affidabili e diagnostics truth | Agenda-per-Anna (SOURCE_REPORTED), World-Days (SOURCE_REPORTED), Notification-Control (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0056 Notification listener multi-modulo | Notification-Control (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0057 Allarme protezione Table Pocket Bag Journey | Phone-Guard (SOURCE_REPORTED), Pocket-Guard (SOURCE_REPORTED), Tabletop-Motion-Alarm (SOURCE_REPORTED) | https://github.com/riccardopinato/Phone-Guard/blob/main/ROADMAP.md |
| CAP-0058 Quick settings overlay rotazione 180 | 180FlipCharge (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0060 Protezione batteria avvisi e sessioni | Battery_Guard (SOURCE_REPORTED) | https://github.com/riccardopinato/Battery_Guard/blob/main/ROADMAP.md |
| CAP-0061 Smart ETA e idle drain batteria | Battery_Guard (SOURCE_REPORTED) | https://github.com/riccardopinato/Battery_Guard/blob/main/ROADMAP.md |
| CAP-0062 Best Conditions Engine sensori | FocuSense (SOURCE_REPORTED) | https://github.com/riccardopinato/FocuSense/blob/main/ROADMAP.md |
| CAP-0066 Trasferimento LAN QR HTTPS fidato | Send-to-pc (SOURCE_REPORTED) | https://github.com/riccardopinato/Send-to-pc/blob/main/ROADMAP.md |
| CAP-0067 Release Android firmato artifact provenance | Agenda-per-Anna (SOURCE_REPORTED), AppLab (SOURCE_REPORTED), Battery_Guard (SOURCE_REPORTED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md |
| CAP-0068 AppLab evidence ladder exact SHA | AppLab (SOURCE_REPORTED), Agenda-per-Anna (SOURCE_REPORTED), CamperBoss (SOURCE_REPORTED) | https://github.com/riccardopinato/AppLab/blob/main/ROADMAP.md |
| CAP-0069 Automated screenshot visual regression | Design-App (SOURCE_REPORTED), AppLab (SOURCE_REPORTED) | https://github.com/riccardopinato/Design-App/blob/main/registry/DESIGN_REGISTRY.yaml |
| CAP-0070 AppLab autonomous bounded repair | AppLab (SOURCE_REPORTED) | https://github.com/riccardopinato/AppLab/blob/main/ROADMAP.md |
| CAP-0071 Offline content packs incremental sync | World-Days (SOURCE_REPORTED), CamperBoss (SOURCE_REPORTED), Notes-Ecosistema (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0072 Entitlement RevenueCat provider truth | Agenda-per-Anna (SOURCE_REPORTED), TasteAI (SOURCE_REPORTED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/main/docs/ROADMAP.md |
| CAP-0073 AdMob UMP consent gating | World-Days (SOURCE_REPORTED), In-Cucina-con-gli-Anime (SOURCE_REPORTED), Battery_Guard (SOURCE_REPORTED) | https://github.com/riccardopinato/World-Days/blob/main/ROADMAP.md |
| CAP-0077 Health check permessi nativi per-capability | Phone-Guard (SOURCE_REPORTED), Battery_Guard (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md |
| CAP-0080 Document expiry and asset passport | CamperBoss (SOURCE_REPORTED) | https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/blob/main/01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md |
| CAP-0081 Phone protection sensitivity adviser | Phone-Guard (SOURCE_REPORTED) | https://github.com/riccardopinato/Phone-Guard/blob/main/ROADMAP.md |
| CAP-0082 Deterministic UI design artwork | World-Days (SOURCE_REPORTED) | https://github.com/riccardopinato/Design-App/blob/main/registry/DESIGN_REGISTRY.yaml |
| CAP-0113 Da appuntamento passato a ricordo privato | Agenda-per-Anna (SOURCE_CONFIRMED) | https://github.com/riccardopinato/Agenda-per-Anna/blob/88efdfa9a688f35585cf2760d131f7a6b0b9deb2/lib/src/event_memory_capture.dart |

Non promuovere a `CI_VERIFIED`, `DEVICE_VERIFIED` o `RELEASE` senza evidence esatta del repo e della build pertinente.
