# Anna's Diary — Audit profondo delle 58 capability DA_VERIFICARE
**Data:** 4 novembre 2026 — **Decisione:** 6 ammesse alla valutazione; 52 mantengono il gate originario.

## Baseline / autorità e fonte
- **App Factory:** [Core main@8052b45b771bf3c5694fc6dd8d037bd83233b37a](https://github.com/riccardopinato/App-Factory-Core/tree/8052b45b771bf3c5694fc6dd8d037bd83233b37a); `CURRENT.yaml` Master **v27**, Golden Index **v28**, Registry **v2**. Non sono stati modificati.
- **Prodotto:** [Anna's Diary@ab5360b78187a643e2b101be21e6951441406059](https://github.com/riccardopinato/Agenda-per-Anna/tree/ab5360b78187a643e2b101be21e6951441406059) con [Product Bible](https://github.com/riccardopinato/Agenda-per-Anna/blob/ab5360b78187a643e2b101be21e6951441406059/docs/PRODUCT_BIBLE.md), [Roadmap](https://github.com/riccardopinato/Agenda-per-Anna/blob/ab5360b78187a643e2b101be21e6951441406059/docs/ROADMAP.md) e AGENTS. Snapshot più recente: PR #223 merged, RC +122 **non** certificato installato. Problemi aperti: [QA fisico #227](https://github.com/riccardopinato/Agenda-per-Anna/issues/227), [giornata realistica #226](https://github.com/riccardopinato/Agenda-per-Anna/issues/226), [privacy V2 #215](https://github.com/riccardopinato/Agenda-per-Anna/pull/215) DRAFT/non autorizzata al merge; Google Calendar API #199 PAUSED.
- **Catalogo:** [Idee repo@40756900473dad1b73a6ba0bc2c747e679d9f3b4](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/tree/40756900473dad1b73a6ba0bc2c747e679d9f3b4), registro **160 CAP / 385 associazioni**, **74** per Anna (**8 Da valutare / 8 Già integrati / 58 Da verificare** prima della presente decisione).
- **Metodologia:** verifica mirata del codice app HEAD, sorgenti già documentati `ANNA_SOURCE_COMPATIBILITA.md`, Product Bible, roadmap/issue, stato dei Donor/Golden e limitazioni fisiche. Le schede `ANNA_SOURCE_COMPATIBILITA.md` conservano SHA storici: NON sono prove del codice corrente. Non è stato lanciato un nuovo test Flutter né su telefono in questo audit documentale.
- **Vincolo centrale:** diario personale / agenda leggera, non Notion, CRM, sistema PM, assistente narrativo o diagnostica. Codice, privacy, backend e dati privati restano nei domini canonici. Le cinque lingue reali di Anna sono **IT/EN/ES/FR/PT** (non DE). Nessuna modifica al Product Bible/roadmap, nessuna aggiunta runtime AI/SDK/licenza.

## Esito e semantica di ammissione

**Ammesse 6** su 58, tutte `PROPOSTA / PARTIAL_REUSE`, perché l'idea residua può essere valutata con un'estensione piccola, reversibile e local-first. Il campo canonico `app_evaluation_admissions.Agenda-per-Anna` aggiunge un gate **READY_FOR_PRODUCT_EVALUATION** distinto dallo stato di implementazione `app_states` (rimane `PROPOSTA`) e dalla classificazione sorgente `anna_full_source_audit.classification` (rimane `PARTIAL_REUSE`).

**Nessuna** modifica ai punteggi 0–100, facilità stimata, certificazione Donor/Golden, permessi, dipendenze, app code o release. Non sono nuove funzionalità approvate: `DA_VALUTARE` significa soltanto «il prossimo passo è decidere se inserirle nella roadmap». Per ognuna è richiesto un giudizio UX/costo e un gate chiaro.

| Fase valutazione | CAP | Delta ristretto e motivazione | Dipendenza/gate principale |
| --- | --- | --- | --- |
| W1 · cattura | **CAP-0092** | Estrarre task privato da testo nel composer, con anteprima, riuso parser di eventi | Test ambiguità 5 lingue, account scope, no write automatico |
| W1 · cattura | **CAP-0093** | Selezionare righe elenco della nota e proporre una checklist collegata | Donor Notes `note_to_checklist.dart` da adattare senza un task database concorrente |
| W2 · accessibilità | **CAP-0120** | Alt text **manuale opzionale** per foto diario/Ricordi | Metadata in MediaAssetStore/diario, screen reader + backup/Trash |
| W2 · UX | **CAP-0147** | Ordinamento reversibile 2–3 card Home Oggi già presenti | UI5, pref `AgendaPreferences`, Golden progressive disclosure DRAFT |
| W3 · ricordi | **CAP-0145** | Griglia privata ricordi registrati, no mood/ciclo/Vault | Null vs 0, permessi, nessuna pubblicazione automatica |
| W3 · bilancio | **CAP-0101** | 2–3 indicatori nel Weekly Review attuale, non dashboard PM | Dedupe CAP-0111 e rispettare task visibili/Trash |

## Donor e Golden (valore effettivo, non promozione)

- **Note/task:** [Notes-Ecosistema `note_to_checklist.dart`](https://github.com/riccardopinato/Notes-Ecosistema/blob/main/flutter_app/lib/src/domain/note_to_checklist.dart) ha estrazione deterministica di sole righe lista e task canonico da scelta utente; il codice adotta modelli Notes, **non è direttamente copia-incollabile in Anna**. [Core Local Rules](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/data/GOLDEN_LOCAL_RULES_AUTOMATION_ENGINE_v1_DRAFT.txt) è DRAFT e non autorizza esecuzione automatica; [Core `local_ml_candidates.dart`](https://github.com/riccardopinato/App-Factory-Core/blob/main/reference_engines/lib/src/local_ml_candidates.dart) contiene Naive Bayes matematico, non un modello addestrato/testato per gli appunti Anna.
- **UX Home:** Anna è il donor della personalizzazione a preset; [Golden Progressive Disclosure](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/ui/GOLDEN_PROGRESSIVE_DISCLOSURE_MODULE_VISIBILITY_FLUTTER_v1_DRAFT.txt) e [Golden App Shell/Visual QA](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/ui/GOLDEN_APP_SHELL_RESPONSIVE_VISUAL_QA_FLUTTER_v1_DRAFT.txt) sono DRAFT. Visibilità **non** equivale a proprietà/cancellazione né a ordine card già implementato.
- **Ricordi/metriche:** [Golden Explainable Recommendation](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/data/GOLDEN_EXPLAINABLE_RECOMMENDATION_ENGINE_v1_DRAFT.txt) resta DRAFT; i contatori già presenti `WeeklyReviewSummary` e le viste dell'archivio sono la base, non prove della nuova visualizzazione. Core ML10 (kNN/logistica/HMM/PCA) non produce automaticamente insight attendibili su persone o salute.
- **Privacy/dati:** il donor Anna local storage/Trash ha E3 scoped nel [Golden Donor Catalog](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/governance/GOLDEN_SCOPED_DONOR_CAPABILITY_CATALOG_v1.txt). [Single Donor Admission](https://github.com/riccardopinato/App-Factory-Core/blob/main/golden/governance/GOLDEN_SINGLE_DONOR_CAPABILITY_ADMISSION_v1.txt) separa E1 SHA, E2 test presenti, E3 test exact-source, E4 device e E5 consumer indipendente. Nessun E4/E5 nuovo in questo audit.
- **Gate immediato della roadmap attuale:** prima non disturbare [#227 QA release +122](https://github.com/riccardopinato/Agenda-per-Anna/issues/227) e [#226 giornata realistica](https://github.com/riccardopinato/Agenda-per-Anna/issues/226). [#215 Privacy V2](https://github.com/riccardopinato/Agenda-per-Anna/pull/215) resta bloccata: nessuna promozione di funzioni condivise/secure non approvate.

## Decisione individuale su tutte le 58 voci

**Categorie:** `AMMETTERE` = passare a Da valutare; `QA_*` = codice presente, completare prove; `DELTA_ESISTENTE` = integrazione parziale già eseguita, non backlog nuovo; `BLOCCO_PRIVACY` = approvazione/security pending; `FUORI_PERIMETRO` = prodotto specialistico/PM/AI; `DUPLICATO_*` = già coperto da owner; `STORICO_VERIFICA` = source storico da riconciliare.

| CAP | Descrizione | Priorità / facilità attuale | Decisione | Motivo concreto |
| --- | --- | --- | --- | --- |
| CAP-0093 | Da note a checklist strutturate | 96/100 · 60% | AMMETTERE | Checklist su righe esplicite: donor Notes e proprietà task già disponibili, non una struttura di progetto. |
| CAP-0015 | Ricerca globale ordinabile e un carattere | 95/100 · 95% | VERIFICARE_SORGENTE | Ricerca globale già presente: smoke Android, ordinamento e isolamento, non nuova feature. |
| CAP-0055 | Notifiche affidabili e diagnostics truth | 94/100 · 85% | QA_NATIVE | Diagnostica notifiche esistente: misurare consegna effettiva e canali/OEM. |
| CAP-0017 | Universal Delete Trash e lifecycle audit | 94/100 · 80% | QA_DATI | Trash/lifecycle esistenti: regressioni restore, purge e media orfani. |
| CAP-0022 | Localizzazione cinque o piu lingue | 94/100 · 80% | QA_LOCALE | Cinque lingue già presenti: parità native push e fallback da verificare. |
| CAP-0067 | Release Android firmato artifact provenance | 94/100 · 80% | QA_RELEASE | Firma/provenance è infrastruttura: verifica di APK specifico e installazione, non roadmap prodotto. |
| CAP-0035 | OCR immagini e documenti on device | 92/100 · 80% | QA_MODELLO | OCR già presente: licenza e media lifecycle, test su device, nessun nuovo OCR. |
| CAP-0102 | Ripianificazione assistita e confronto piani alternativi | 92/100 · 76% | DELTA_ESISTENTE | Ripianificazione read-only da #217 presente: due piani alternativi non provati; prima #226 e QA. |
| CAP-0027 | Cattura universale condividi link testo immagine | 90/100 · 80% | QA_CAPTURE | Condivisione tramite ACTION_SEND già esistente: test intent, consenso, revoca. |
| CAP-0018 | Backup restore con staging e rollback | 90/100 · 65% | QA_BACKUP | Restore staging/rollback già presente: corrupt archive, import e account switching. |
| CAP-0068 | AppLab evidence ladder exact SHA | 90/100 · 65% | QA_FACTORY | Evidence ladder è processo AppLab già presente: gate SHA e device separati. |
| CAP-0092 | Cattura task da linguaggio naturale e note | 90/100 · 55% | AMMETTERE | Parser eventi e Unified Capture esistono: valutare un parser locale task con anteprima. |
| CAP-0023 | Design System Flutter token-first | 89/100 · 80% | QA_UI | Design System Flutter UI5 presente: token e visual regression, non reimplementazione. |
| CAP-0025 | Schermate responsive rail e split view | 89/100 · 75% | QA_UI | Responsive shell parziale: collaudo small/tablet/landscape, non nuova architettura. |
| CAP-0013 | Collection e ricerca locale | 88/100 · 95% | QA_RICERCA | Collezioni e ricerca già presenti: performance, ACL e provenienza dei risultati. |
| CAP-0016 | Inbox con categorie modificabili | 88/100 · 90% | QA_INBOX | Inbox e categorie già presenti: test vuoti, persistenza e multi-account. |
| CAP-0144 | Widget contestuali privacy-safe per agenda e contenuti condivisi | 88/100 · 73% | QA_PRIVACY | Home widget già corretto in #216: privacy lockscreen/cambio account e QA fisico prima di estensione. |
| CAP-0072 | Entitlement RevenueCat provider truth | 88/100 · 60% | QA_PROVIDER | Entitlement esistente: verifica RevenueCat Store e provider truth senza falsi unlock. |
| CAP-0020 | Shared Ecosystem Bridge COPY LINK | 88/100 · 58% | QA_BRIDGE | Bridge COPY/LINK esistente: roundtrip e versioni, niente nuova sincronizzazione. |
| CAP-0004 | Overlay calendari esterni read-only | 87/100 · 85% | QA_CALENDARIO | Overlay eventi esterni già previsto: test provider, permessi e isolamento. |
| CAP-0024 | Motion reduced-motion e microinterazioni | 87/100 · 80% | QA_ACCESSIBILITA | Motion/reduced motion presenti: test dinamici e preferenze accessibilità. |
| CAP-0106 | Rilevamento sovraccarico e heatmap riunioni | 87/100 · 25% | FUORI_PERIMETRO | Heatmap riunioni/workload professionale contraria al Product Bible, già covered day advice #226 per vita personale. |
| CAP-0114 | Redazione PII e privacy copy di note e PDF | 85/100 · 40% | BLOCCO_PRIVACY | Redazione PII export richiede copertura/QA sicurezza: Privacy V2 #215 non approvata. |
| CAP-0105 | Prioritizzazione trasparente e matrice Eisenhower | 85/100 · 25% | FUORI_PERIMETRO | Board Eisenhower è gestione progetto: Notes è owner, Weekly Review già fornisce priorità leggere. |
| CAP-0101 | Dashboard produttivita locale da task canoniche | 84/100 · 55% | AMMETTERE | WeeklyReviewSummary ha già contatori canonici: valutare solo 2–3 metriche personali senza nuova dashboard. |
| CAP-0134 | Triage e categorizzazione documenti importati | 84/100 · 17% | FUORI_PERIMETRO | Classificatore estratti/invoice non corrisponde al diario; modello/licenze e dati italiani non verificati. |
| CAP-0006 | Lista della spesa privata e condivisa | 83/100 · 95% | QA_SHOPPING | Lista spesa privata/condivisa già presente: isolamento e prove bidispositivo. |
| CAP-0010 | Ricordi Then and Now | 83/100 · 95% | QA_RICORDI | Then/Now già presente: media canonici e consenso di visualizzazione. |
| CAP-0011 | Life Threads narrativi | 82/100 · 85% | QA_RICORDI | Life Threads già presenti: evitare duplicazione dello storico. |
| CAP-0045 | Meal plan e spesa derivata | 82/100 · 45% | FUORI_PERIMETRO | Meal planning ricette compete con Cooking Anime/TasteAI; Anna conserva sola lista spesa. |
| CAP-0145 | Heatmap locale di ricordi, attività e abitudini volontarie | 81/100 · 70% | AMMETTERE | Archivio/Ricordi già consentono frequenze: valutare griglia locale solo dei ricordi volontari. |
| CAP-0019 | Store media content addressed e GC | 81/100 · 65% | QA_STORAGE | Content-addressed media esistente: reference GC, scope Vault separato. |
| CAP-0147 | Home modulare riordinabile con preferenze locali | 81/100 · 65% | AMMETTERE | Preset/moduli esistono: valutare ordinamento reversibile di poche card Home, no nuovo store. |
| CAP-0120 | Testi alternativi accessibili per immagini delle note | 81/100 · 45% | AMMETTERE | Accessibilità foto già richiesta: valutare descrizione manuale opzionale, no BLIP/cloud. |
| CAP-0129 | Aggiornamento controllato dei fatti con storia e fonti | 81/100 · 45% | FUORI_PERIMETRO | Memoria agentica con editing fatti/sorgenti è prodotto Notes, non diario personale. |
| CAP-0051 | Mappe luoghi ricordi condivisi con ponte | 80/100 · 65% | QA_BRIDGE | Mappa ricordi e COPY/LINK esistono: controllare trasporto e autorizzazioni. |
| CAP-0063 | Momenti ideali per focus in calendario | 80/100 · 40% | DUPLICATO_ADVICE | Focus slot sovrapposto a free slots e RealisticDayAdvisor/#226; nessuna nuova surface separata. |
| CAP-0096 | Gerarchie task ricorrenze e relazioni alle note | 80/100 · 25% | FUORI_PERIMETRO | Gerarchie task/progetti e scheduler duplicato trasformerebbero Anna in PM, contrario al Bible. |
| CAP-0062 | Best Conditions Engine sensori | 80/100 · 15% | FUORI_PERIMETRO | Scoring sensor ambientale appartiene a FocusSense; sensori e test device assenti in Anna. |
| CAP-0012 | Year in Review deterministico | 79/100 · 85% | QA_RICORDI | Year in Review deterministico già presente: filtri privacy e storico. |
| CAP-0141 | Rituali collaborativi con risposta e rivelazione reciproca | 79/100 · 65% | BLOCCO_PRIVACY | Rivelazione reciproca nuovo protocollo condiviso: Privacy #215 e test due account obbligatori. |
| CAP-0082 | Deterministic UI design artwork | 79/100 · 55% | PRIORITA_BASSA | Artwork deterministico è asset/design tool, non feature quotidiana; UI5 già definita. |
| CAP-0032 | Indicizzazione ricerca semantica locale | 79/100 · 42% | FUORI_PERIMETRO | Embedding/indice semantico pesante e knowledge workflow appartengono a Notes; ricerca locale Anna già presente. |
| CAP-0076 | Web Clip sicuro con provenienza | 78/100 · 55% | DUPLICATO_CAPTURE | Share URL/testo già presente; web archiving completo estende data ownership senza valore dimostrato. |
| CAP-0007 | Scheda workout e storico multisport | 77/100 · 85% | QA_WORKOUT | Scheda allenamento esistente: verificare single owner e progressione. |
| CAP-0009 | Ricordi mappa geolocalizzata | 77/100 · 85% | QA_RICORDI | Mappa ricordi già presente: localizzazione consenso e privacy GPS. |
| CAP-0142 | Capsule e lettere a apertura programmata | 77/100 · 77% | DELTA_ESISTENTE | Lettere personali già source-merged in #218: test fusi/backup e solo dopo shared/privacy. |
| CAP-0014 | Cattura rapida contestuale da calendario | 75/100 · 80% | QA_CAPTURE | Cattura calendario contestuale già CI: verificare import volontario e date. |
| CAP-0021 | QR inviti condivisi 24 ore | 75/100 · 75% | QA_SHARED | Inviti QR già presente: prova camera, due account e scadenza/revoca. |
| CAP-0008 | Import foto PDF delle schede workout | 75/100 · 55% | STORICO_VERIFICA | Import workout storico: chiarire delta rispetto media store e scheda attuale. |
| CAP-0075 | Import Center per migrazioni utenti | 74/100 · 55% | STORICO_VERIFICA | Import center migrazioni da validare sul restore con staging; alto rischio storico dati. |
| CAP-0123 | Lettura bilingue sincronizzata di note e PDF | 74/100 · 25% | FUORI_PERIMETRO | Lettura PDF bilingue con servizi esterni è funzione specialistica Notes e non offline garantito. |
| CAP-0064 | Sonno routine e reminder adattivi | 73/100 · 40% | FUORI_PERIMETRO | Coach sonno/routine specializzato appartiene a SleepMax; non creare diagnostica nel diario. |
| CAP-0085 | Diarizzazione vocale locale per appunti riunioni | 70/100 · 10% | FUORI_PERIMETRO | Diarizzazione speaker richiede modelli/audio/consenso non approvati; voice diary esiste. |
| CAP-0146 | Allegati documentali cifrati per Vault privato | 69/100 · 30% | BLOCCO_PRIVACY | Allegati cifrati Vault richiedono security design/keys/backup multi-platform; Privacy #215 bloccata. |
| CAP-0074 | Companion voice note organizer | 67/100 · 55% | DUPLICATO_CAPTURE | Organizer voice note duplica diario vocale e Unified Capture; nessun corpus/prodotto nuovo. |
| CAP-0132 | Diario sonoro e classificazione eventi acustici | 65/100 · 20% | FUORI_PERIMETRO | YAMNet classifica eventi acustici, non contenuti diario; licenza e hardware non certificati. |
| CAP-0143 | Biglietti ricordo con QR e accesso revocabile | 62/100 · 40% | BLOCCO_PRIVACY | Biglietti QR ricordi con revoca creano nuova condivisione sensibile; Privacy V2 #215 aperta. |

## Roadmap di **valutazione**, non roadmap approvata di sviluppo

- **Gate 0 — Source/release truth:** prima risolvere priorità già approvate #227 e #226; usare sempre SHA app/base e premere stop su account/privacy/backup incompleti. Non unire #215 o #199 implicitamente.
- **Wave 1 — Rimuovere attrito della cattura (CAP-0092, CAP-0093):** specificare due user journeys piccoli (frase→task privato, elenco→checklist), prototipi read-only, esempi IT/EN/ES/FR/PT, preview/edit/annulla, source revision, Undo. Se non superano il confronto con Unified Capture corrente, archiviare la proposta.
- **Wave 2 — Accessibilità e controllo Home (CAP-0120, CAP-0147):** UX manual alt-text con screen reader e reversibilità; layout 2–3 card con salvataggio nelle preferenze esistenti, reset e test visual 10×7, account switch. Niente ML foto, niente nuovi dati condivisi.
- **Wave 3 — Rilettura e bilancio (CAP-0145, CAP-0101):** due superfici derivate dalle entità private già possedute, filtri di sicurezza, aggregati su dati incompleti, disattivazione esplicita; test di privacy/conteggi e confronto con Year in Review/Weekly Review. Nessun nuovo sistema di statistiche comportamentali.
- **Gate 4 — Decisione utente:** per ogni CAP valutare valore, impatto UI, costo sviluppo, degrado di performance e rischio. Solo i sotto-scope esplicitamente approvati entrano poi in `docs/ROADMAP.md` del repository Anna con PR separata e CI. Le 6 candidature sono indipendenti dal release/versionCode corrente.

## Tracciabilità e integrità del catalogo

L'ammissione è registrata nel JSON canonico e derivata da `scripts/build_status_views.py`. I link `PER_APP/Agenda-per-Anna/DA_VALUTARE.md`, `DA_VERIFICARE.md`, `TABELLA.csv`, l'indice per-app e la coda globale vengono rigenerati. **Risultato atteso:** Anna **14 Da valutare, 8 Già integrati, 52 Da verificare**; totale Anna **74**, totale catalogo **160 CAP / 385 associazioni**. Nessuna voce viene cancellata e nessuno stato `PROPOSTA`, `SOURCE_REPORTED` o `CI_VERIFIED` viene falsamente promosso.

**Limite dell'audit:** la correlazione tra Donor e prodotto è una decisione architetturale/documentale; qualità UX reale, migrazioni, test con screen reader, performance e dispositivo non sono attestati da una semplice ricerca sorgente. I gate non verificati restano aperti.
