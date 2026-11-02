# Audit delle 14 fusioni suggerite dalla fonte — 02/11/2026

Le fusioni sono mantenute integralmente. Lo **score di coerenza (0–100)** valuta compatibilità di utente, dati e prodotto, **non** fattibilità verificata né pronostico ricavi. Una fusione respinta resta consultabile; i singoli # continuano a esistere nelle 100 schede.

| Fusione proposta | Descrizione | Coerenza | Esito | Ragione / destinazione |
|---|---|---:|---|---|
| [#1](SCHEDE/IA26-001.md) + [#41](SCHEDE/IA26-041.md) + [#52](SCHEDE/IA26-052.md) | Soundboard meme + suoni casa + scuse ambientali | **34** | SEPARARE | Target e diritti diversi: intrattenimento, genitorialità, telefonate; condividere solo motore audio. |
| [#2](SCHEDE/IA26-002.md) | Diario successi invisibili | **80** | MANTENERE | Singola app coerente; confrontare habit tracker già diffusi. |
| [#3](SCHEDE/IA26-003.md) + [#38](SCHEDE/IA26-038.md) | Kit viaggio offline + tempo in denaro | **39** | SEPARARE | Convertire il prezzo in ore lavorate non risolve un bisogno di viaggio; #38 con #4. |
| [#4](SCHEDE/IA26-004.md) + [#24](SCHEDE/IA26-024.md) | Pausa acquisti + carrello supermercato | **79** | FUSIONE CONDIZIONALE | Logica risparmio e budget comune, ma barcode non offre prezzo di negozio; partire da #4. |
| [#9](SCHEDE/IA26-009.md) + [#40](SCHEDE/IA26-040.md) | Diario corpo/umore + coerenza sonno | **72** | FEATURE FIRST | App Health/diary: considerare SleepMax Coach, Anna's Diary, FocusSense; evitare inferenze mediche. |
| [#6](SCHEDE/IA26-006.md) + [#39](SCHEDE/IA26-039.md) + [#42](SCHEDE/IA26-042.md) + [#72](SCHEDE/IA26-072.md) | Biglietti QR + diario finto + capsule + polaroid | **36** | SEPARARE | La privacy cifrata non è un tema grafico. Biglietti/Polaroid/Capsule possono condividere export, non vault. |
| [#5](SCHEDE/IA26-005.md) + [#11](SCHEDE/IA26-011.md) + [#25](SCHEDE/IA26-025.md) | Ricordi casuali + amicizie e cerchio dei cinque | **65** | DUE MODULI | Ricordi famiglia (#5) distinti da cura amicizie (#11/#25); collaborazione opzionale. |
| [#46](SCHEDE/IA26-046.md) + [#48](SCHEDE/IA26-048.md) + [#62](SCHEDE/IA26-062.md) | Sveglia shake + gioco tavolo + allarme anti-touch | **55** | DONOR COMUNE | Stessi sensori ma journey differenti; #62 riuso Phone Guard; #46 segue SleepMax; #48 party game. |
| [#10](SCHEDE/IA26-010.md) + [#27](SCHEDE/IA26-027.md) + [#31](SCHEDE/IA26-031.md) | Tempo qualità + idee congelate + decisione di pancia | **56** | SEPARARE CON RIUSO | Proposta tempo libero vs progetti vs scelte; #27 candidato a Notes. |
| [#43](SCHEDE/IA26-043.md) + [#88](SCHEDE/IA26-088.md) | Contatore ripetizioni + velocità parole | **81** | FUSIONE CONSIGLIATA | Integrare anche #32 in un coach public speaking a sessione esplicita. |
| [#13](SCHEDE/IA26-013.md) + [#33](SCHEDE/IA26-033.md) + [#71](SCHEDE/IA26-071.md) | Vocabolario bimbi + oggetti perduti condominio + batteria sociale | **21** | NON FONDERE | Condividono cloud ma né destinatari né dati né modello commerciale. |
| [#74](SCHEDE/IA26-074.md) + [#79](SCHEDE/IA26-079.md) + [#99](SCHEDE/IA26-099.md) | Risposte a discussioni + finanza ironica + recensioni B2B | **26** | NON FONDERE | Privacy, tono e mercati incompatibili; #99 B2B distinta. |
| [#75](SCHEDE/IA26-075.md) + [#82](SCHEDE/IA26-082.md) | Sogni in arte + fiabe personalizzate | **52** | SOLO RIUSO TECNICO | Motori AI generativi comuni, ma pubblici, contenuti e moderazione per minori diversi. |
| [#19](SCHEDE/IA26-019.md) + [#92](SCHEDE/IA26-092.md) + [#97](SCHEDE/IA26-097.md) | Scanner alimenti trasparente + etichette tessili | **41** | SEPARARE | Food/allergeni e tessuti hanno fonti e safety differenti; #92 con TasteAI, #97 con CuraVestiti. |

## Riuso rispetto al portafoglio esistente

| App/suite già censita | Idee candidate da verificare (non implementazioni dichiarate) | Prossimo controllo |
|---|---|---|
| [Battery Guard](https://github.com/riccardopinato/Battery_Guard) | #44, #67 (solo componente battery) | Stesso contratto batteria, notifiche e test Doze |
| [Phone Guard](https://github.com/riccardopinato/Phone-Guard) | #48, #50, #62, #73 (solo studio sensori) | Non creare una seconda sirena; valutare policy e calibrazione |
| [Anna's Diary](https://github.com/riccardopinato/Agenda-per-Anna) | #5, #9, #26, #37, #39, #61, #69, #71, #95 | Product Bible, dati Noi/Private, Map e Vault |
| [Notes-Ecosistema](https://github.com/riccardopinato/Notes-Ecosistema) | #27, #93, extra E04 | No doppione note; sicurezza memoria, backup e voce |
| [TasteAI](https://github.com/riccardopinato/TasteAI) | #12, #19, #92 | Anti-waste già esistente; catalogo alimentare e safety |
| [CamperBoss](https://github.com/riccardopinato/CamperBoss) | #3, #90 | Offline content e release non confusi con dati valutari in tempo reale |
| [Wonderlog](https://github.com/riccardopinato/Wonderlog) | #17, #36, #37, #90 | Dataset film/storia e diritti immagini prima di mappe |
| [FrameLab](https://github.com/riccardopinato/app-fotografia) | #23, #35, #72, #96 | Motore foto/palette, vincoli export e monetizzazione |
| SleepMax Coach | #29, #40, #41, #46, #70, #87 | Repository da verificare, audio background e sveglie |
| FocusSense / Focus Kingdom | #8, #27, #45, #66, #81, #85, #93 | Non duplicare motori focus/gamification |
| CashMate AI | #4, #24, #38, #49, #79 | MVP #4 potenzialmente standalone solo se diverso da budgeting |
| CuraVestiti | #97 | Feature etichette tessili, non scanner allergeni |
| ReelForge/ClipForge | extra E05 | Lip-sync video avanzato solo come ricerca tecnica |

Tutti gli stati sono **analisi / idee**. Licenze, API, Product Bible, repo e SHA richiedono audit mirati prima di qualsiasi implementazione.
