# Anna's Diary — Step 3: riconciliazione delle capability (7 novembre 2026)

**Tipologia:** evidenza incrementale auditabile. Non è una certificazione dei 74 elementi e non promuove stati, score, Golden o release.

## Baseline e fonte della verità
- Factory: App-Factory-Core@989c5123c62c07d1dd85a3c520f0d04b7fe3f543; CURRENT Master v27, Golden Index v28, Registry v2.
- Anna: Agenda-per-Anna@dc601002c3308b6579c30945867638b84ad35de9; Flutter Web / PWA live dopo workflow #42402256546; Development CI #42402256538 PASS.
- Catalogo: Idee-app-Archivi-riferimenti@1a57e3393b2c74fa61f815864220d4a71f9a6777, 160 CAP, 74 associazioni Anna.
- Stato della roadmap: Step 2 UI/Performance aperto; Step 3 riconciliazione in corso; Step 4 solo audit backend read-only. Step 1 Web-first accettato, non certificato su hardware nativo.

## Rilievi puntuali e delta residui
| CAP | Stato attuale | Prova corrente e limite |
| --- | --- | --- |
| CAP-0152 Fuzzy | PROPOSTA | [Sorgente](https://github.com/riccardopinato/Agenda-per-Anna/blob/dc601002c3308b6579c30945867638b84ad35de9/lib/src/approved_search_policy.dart), [test](https://github.com/riccardopinato/Agenda-per-Anna/blob/dc601002c3308b6579c30945867638b84ad35de9/test/cap0152_fuzzy_fallback_test.dart): fallback locale bounded implementato e CI verde, ma Unicode/grapheme, alias/luoghi e due-account ACL ancora da validare; perimetro FULL non completato |
| CAP-0160 TF-IDF | PROPOSTA | [Sorgente](https://github.com/riccardopinato/Agenda-per-Anna/blob/dc601002c3308b6579c30945867638b84ad35de9/lib/src/cap0160_offline_tags.dart), [test](https://github.com/riccardopinato/Agenda-per-Anna/blob/dc601002c3308b6579c30945867638b84ad35de9/test/cap0160_offline_tags_test.dart): engine local e chip/save guardati, cinque lingue IT/EN/ES/FR/PT; DE della CAP generale escluso; QA Web reale da eseguire |
| CAP-0015 Cerca | SOURCE_REPORTED | [Bugfix e test ricerca vuota](https://github.com/riccardopinato/Agenda-per-Anna/blob/dc601002c3308b6579c30945867638b84ad35de9/test/approved_search_policy_test.dart) dopo [PR #270](https://github.com/riccardopinato/Agenda-per-Anna/pull/270); CI corrente PASS, tap reale PWA non certificato |
| CAP-0025 Responsive | SOURCE_REPORTED | [Test real Flutter multi-width](https://github.com/riccardopinato/Agenda-per-Anna/blob/dc601002c3308b6579c30945867638b84ad35de9/test/ds6_web_first_step2_responsive_test.dart) per 5 larghezze; tablet/split screen e screenshot reali pendenti |
| CAP-0069 Visual QA | CI_VERIFIED | Comparatore e matrice in sorgente; 70 baseline + 70 candidate PNG reali non approvate; no VISUAL_PASS |
| CAP-0067 Release | SOURCE_REPORTED | Web attuale su dc601002 e Pages #42402256546; APK firmato +129 antecedente, non si può affermare parità nativa |

## Classificazione corretta fino alla rigenerazione
Le due proposte CAP-0152 e CAP-0160 hanno componenti già implementati ma NON soddisfano ancora l'intero contratto trasversale. Conservare la coda di prodotto per il delta FULL, documentando separatamente la SOURCE_PARTIAL verificata. Non duplicare il motore locale. Non alterare score, facilità, consumer Notes/Wonderlog o Golden per effetto di questo audit.

La fonte canonica è REGISTRO_CAPABILITY.json e le pagine PER_APP, STATO_IMPLEMENTAZIONI, schede CAP, CSV e matrici sono generate. Non modificarle manualmente. Al completamento della revisione stato/evidenze, aggiornare il registro e rigenerare con scripts/build_catalog.py e scripts/build_status_views.py, poi eseguire --check e CI. Fino a quel passaggio i numeri operativi restano quelli correnti.

## Prossimi controlli Step 3 (ordine)
1. Ricomporre nel registro per Anna prova SOURCE_PARTIAL e delta FULL per CAP-0152/0160, senza promuovere CI a DEVICE.
2. Verificare e rigenerare i derivati canonici con i due generatori; cardinalità Anna sempre 74.
3. Riallineare README e roadmap Anna alla PWA Web-first e all'ultimo SHA; conservare gli storici.
4. Mantenere aperti test visivi Step 2 e audit sicurezza Step 4; nessuna modifica backend o nuovo APK.

## Inventario degli stati canonici di partenza — 74 associazioni
Il rilievo INVENTORY_ONLY significa che questo passaggio non ha ripetuto una verifica puntuale di quella CAP.

| CAP | Capability | Stato canonico | Rilievo Step 3 |
| --- | --- | --- | --- |
| [CAP-0093](REGISTRO_CAPABILITY/CAP-0093.md) | Da note a checklist strutturate | PROPOSTA | INVENTORY_ONLY |
| [CAP-0152](REGISTRO_CAPABILITY/CAP-0152.md) | Ricerca fuzzy offline per refusi e alias | PROPOSTA | PARTIAL_SOURCE_AND_CI |
| [CAP-0015](REGISTRO_CAPABILITY/CAP-0015.md) | Ricerca globale ordinabile e un carattere | SOURCE_REPORTED | SOURCE_CI_ON_CURRENT_MAIN |
| [CAP-0017](REGISTRO_CAPABILITY/CAP-0017.md) | Universal Delete Trash e lifecycle audit | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0022](REGISTRO_CAPABILITY/CAP-0022.md) | Localizzazione cinque o piu lingue | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0055](REGISTRO_CAPABILITY/CAP-0055.md) | Notifiche affidabili e diagnostics truth | SOURCE_CONFIRMED | SOURCE_PENDING_DELIVERY |
| [CAP-0067](REGISTRO_CAPABILITY/CAP-0067.md) | Release Android firmato artifact provenance | SOURCE_REPORTED | WEB_PASS_APK_OLDER |
| [CAP-0077](REGISTRO_CAPABILITY/CAP-0077.md) | Health check permessi nativi per-capability | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0001](REGISTRO_CAPABILITY/CAP-0001.md) | Pianificazione di slot liberi | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0035](REGISTRO_CAPABILITY/CAP-0035.md) | OCR immagini e documenti on device | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0102](REGISTRO_CAPABILITY/CAP-0102.md) | Ripianificazione assistita e confronto piani alternativi | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0111](REGISTRO_CAPABILITY/CAP-0111.md) | Weekly Review con proposte di pulizia e ripianificazione | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0160](REGISTRO_CAPABILITY/CAP-0160.md) | Estrazione TF-IDF di parole chiave e tag suggeriti | PROPOSTA | PARTIAL_SOURCE_AND_CI |
| [CAP-0018](REGISTRO_CAPABILITY/CAP-0018.md) | Backup restore con staging e rollback | SOURCE_REPORTED | SOURCE_PENDING_RESTORE |
| [CAP-0027](REGISTRO_CAPABILITY/CAP-0027.md) | Cattura universale condividi link testo immagine | SOURCE_CONFIRMED | INVENTORY_ONLY |
| [CAP-0068](REGISTRO_CAPABILITY/CAP-0068.md) | AppLab evidence ladder exact SHA | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0092](REGISTRO_CAPABILITY/CAP-0092.md) | Cattura task da linguaggio naturale e note | PROPOSTA | INVENTORY_ONLY |
| [CAP-0023](REGISTRO_CAPABILITY/CAP-0023.md) | Design System Flutter token-first | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0025](REGISTRO_CAPABILITY/CAP-0025.md) | Schermate responsive rail e split view | SOURCE_REPORTED | SOURCE_CI_MULTI_WIDTH |
| [CAP-0002](REGISTRO_CAPABILITY/CAP-0002.md) | Creazione eventi da linguaggio naturale | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0013](REGISTRO_CAPABILITY/CAP-0013.md) | Collection e ricerca locale | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0016](REGISTRO_CAPABILITY/CAP-0016.md) | Inbox con categorie modificabili | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0020](REGISTRO_CAPABILITY/CAP-0020.md) | Shared Ecosystem Bridge COPY LINK | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0072](REGISTRO_CAPABILITY/CAP-0072.md) | Entitlement RevenueCat provider truth | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0144](REGISTRO_CAPABILITY/CAP-0144.md) | Widget contestuali privacy-safe per agenda e contenuti condivisi | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0004](REGISTRO_CAPABILITY/CAP-0004.md) | Overlay calendari esterni read-only | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0005](REGISTRO_CAPABILITY/CAP-0005.md) | Esportazione esplicita eventi verso calendario | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0024](REGISTRO_CAPABILITY/CAP-0024.md) | Motion reduced-motion e microinterazioni | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0106](REGISTRO_CAPABILITY/CAP-0106.md) | Rilevamento sovraccarico e heatmap riunioni | PROPOSTA | INVENTORY_ONLY |
| [CAP-0031](REGISTRO_CAPABILITY/CAP-0031.md) | Trascrizione vocale offline opzionale | PROPOSTA | INVENTORY_ONLY |
| [CAP-0105](REGISTRO_CAPABILITY/CAP-0105.md) | Prioritizzazione trasparente e matrice Eisenhower | PROPOSTA | INVENTORY_ONLY |
| [CAP-0114](REGISTRO_CAPABILITY/CAP-0114.md) | Redazione PII e privacy copy di note e PDF | PROPOSTA | INVENTORY_ONLY |
| [CAP-0151](REGISTRO_CAPABILITY/CAP-0151.md) | Riassunti estrattivi di note con TextRank e citazioni | PROPOSTA | INVENTORY_ONLY |
| [CAP-0159](REGISTRO_CAPABILITY/CAP-0159.md) | Clustering spaziale privacy-safe per ricordi e POI | PROPOSTA | INVENTORY_ONLY |
| [CAP-0101](REGISTRO_CAPABILITY/CAP-0101.md) | Dashboard produttivita locale da task canoniche | PROPOSTA | INVENTORY_ONLY |
| [CAP-0134](REGISTRO_CAPABILITY/CAP-0134.md) | Triage e categorizzazione documenti importati | PROPOSTA | INVENTORY_ONLY |
| [CAP-0006](REGISTRO_CAPABILITY/CAP-0006.md) | Lista della spesa privata e condivisa | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0010](REGISTRO_CAPABILITY/CAP-0010.md) | Ricordi Then and Now | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0011](REGISTRO_CAPABILITY/CAP-0011.md) | Life Threads narrativi | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0045](REGISTRO_CAPABILITY/CAP-0045.md) | Meal plan e spesa derivata | PROPOSTA | INVENTORY_ONLY |
| [CAP-0003](REGISTRO_CAPABILITY/CAP-0003.md) | Preparazione contestuale appuntamento | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0019](REGISTRO_CAPABILITY/CAP-0019.md) | Store media content addressed e GC | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0069](REGISTRO_CAPABILITY/CAP-0069.md) | Automated screenshot visual regression | CI_VERIFIED | COMPARATOR_CI_ONLY |
| [CAP-0113](REGISTRO_CAPABILITY/CAP-0113.md) | Da appuntamento passato a ricordo privato | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0120](REGISTRO_CAPABILITY/CAP-0120.md) | Testi alternativi accessibili per immagini delle note | PROPOSTA | INVENTORY_ONLY |
| [CAP-0121](REGISTRO_CAPABILITY/CAP-0121.md) | Lettura semplificata con originale affiancato | PROPOSTA | INVENTORY_ONLY |
| [CAP-0129](REGISTRO_CAPABILITY/CAP-0129.md) | Aggiornamento controllato dei fatti con storia e fonti | PROPOSTA | INVENTORY_ONLY |
| [CAP-0145](REGISTRO_CAPABILITY/CAP-0145.md) | Heatmap locale di ricordi, attività e abitudini volontarie | PROPOSTA | INVENTORY_ONLY |
| [CAP-0147](REGISTRO_CAPABILITY/CAP-0147.md) | Home modulare riordinabile con preferenze locali | PROPOSTA | INVENTORY_ONLY |
| [CAP-0051](REGISTRO_CAPABILITY/CAP-0051.md) | Mappe luoghi ricordi condivisi con ponte | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0062](REGISTRO_CAPABILITY/CAP-0062.md) | Best Conditions Engine sensori | PROPOSTA | INVENTORY_ONLY |
| [CAP-0063](REGISTRO_CAPABILITY/CAP-0063.md) | Momenti ideali per focus in calendario | PROPOSTA | INVENTORY_ONLY |
| [CAP-0096](REGISTRO_CAPABILITY/CAP-0096.md) | Gerarchie task ricorrenze e relazioni alle note | PROPOSTA | INVENTORY_ONLY |
| [CAP-0153](REGISTRO_CAPABILITY/CAP-0153.md) | Previsione prudente di completamento studio e progetti | PROPOSTA | INVENTORY_ONLY |
| [CAP-0012](REGISTRO_CAPABILITY/CAP-0012.md) | Year in Review deterministico | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0032](REGISTRO_CAPABILITY/CAP-0032.md) | Indicizzazione ricerca semantica locale | PROPOSTA | INVENTORY_ONLY |
| [CAP-0082](REGISTRO_CAPABILITY/CAP-0082.md) | Deterministic UI design artwork | PROPOSTA | INVENTORY_ONLY |
| [CAP-0141](REGISTRO_CAPABILITY/CAP-0141.md) | Rituali collaborativi con risposta e rivelazione reciproca | PROPOSTA | INVENTORY_ONLY |
| [CAP-0076](REGISTRO_CAPABILITY/CAP-0076.md) | Web Clip sicuro con provenienza | PROPOSTA | INVENTORY_ONLY |
| [CAP-0007](REGISTRO_CAPABILITY/CAP-0007.md) | Scheda workout e storico multisport | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0009](REGISTRO_CAPABILITY/CAP-0009.md) | Ricordi mappa geolocalizzata | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0142](REGISTRO_CAPABILITY/CAP-0142.md) | Capsule e lettere a apertura programmata | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0008](REGISTRO_CAPABILITY/CAP-0008.md) | Import foto PDF delle schede workout | ROADMAP_STORICA | INVENTORY_ONLY |
| [CAP-0014](REGISTRO_CAPABILITY/CAP-0014.md) | Cattura rapida contestuale da calendario | CI_VERIFIED | INVENTORY_ONLY |
| [CAP-0021](REGISTRO_CAPABILITY/CAP-0021.md) | QR inviti condivisi 24 ore | SOURCE_REPORTED | INVENTORY_ONLY |
| [CAP-0075](REGISTRO_CAPABILITY/CAP-0075.md) | Import Center per migrazioni utenti | ROADMAP_STORICA | INVENTORY_ONLY |
| [CAP-0123](REGISTRO_CAPABILITY/CAP-0123.md) | Lettura bilingue sincronizzata di note e PDF | PROPOSTA | INVENTORY_ONLY |
| [CAP-0064](REGISTRO_CAPABILITY/CAP-0064.md) | Sonno routine e reminder adattivi | PROPOSTA | INVENTORY_ONLY |
| [CAP-0154](REGISTRO_CAPABILITY/CAP-0154.md) | Routine predittive con Markov solo opt-in | PROPOSTA | INVENTORY_ONLY |
| [CAP-0085](REGISTRO_CAPABILITY/CAP-0085.md) | Diarizzazione vocale locale per appunti riunioni | PROPOSTA | INVENTORY_ONLY |
| [CAP-0146](REGISTRO_CAPABILITY/CAP-0146.md) | Allegati documentali cifrati per Vault privato | PROPOSTA | INVENTORY_ONLY |
| [CAP-0074](REGISTRO_CAPABILITY/CAP-0074.md) | Companion voice note organizer | PROPOSTA | INVENTORY_ONLY |
| [CAP-0132](REGISTRO_CAPABILITY/CAP-0132.md) | Diario sonoro e classificazione eventi acustici | PROPOSTA | INVENTORY_ONLY |
| [CAP-0143](REGISTRO_CAPABILITY/CAP-0143.md) | Biglietti ricordo con QR e accesso revocabile | PROPOSTA | INVENTORY_ONLY |

**Cardinalità:** 74; stati {"CI_VERIFIED":10,"SOURCE_REPORTED":26,"ROADMAP_STORICA":2,"SOURCE_CONFIRMED":2,"PROPOSTA":34}. Nessuna implementazione è implicitamente autorizzata da questo documento.
