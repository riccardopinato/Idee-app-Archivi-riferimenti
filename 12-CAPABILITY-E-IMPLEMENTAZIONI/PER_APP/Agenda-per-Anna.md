# Agenda-per-Anna — capability e priorita

Fonte canonica: `../REGISTRO_CAPABILITY.json`. Stati di audit, non certificazioni.

| ID | Capability | Priorita | Score | Stato nell'app | Prossimo gate |
| --- | --- | --- | --- | --- | --- |
| [CAP-0015](../REGISTRO_CAPABILITY/CAP-0015.md) | Ricerca globale ordinabile e un carattere | P1 | 95 | SOURCE_REPORTED | Source gate riportati PASS ma verificare smoke Android |
| [CAP-0017](../REGISTRO_CAPABILITY/CAP-0017.md) | Universal Delete Trash e lifecycle audit | P1 | 94 | SOURCE_REPORTED | Regression entita-per-entita e file orfani; niente duplicazione lifecycle |
| [CAP-0022](../REGISTRO_CAPABILITY/CAP-0022.md) | Localizzazione cinque o piu lingue | P1 | 94 | SOURCE_REPORTED | Controllare parita lingua in native notifications |
| [CAP-0055](../REGISTRO_CAPABILITY/CAP-0055.md) | Notifiche affidabili e diagnostics truth | P1 | 94 | SOURCE_REPORTED | Permesso non equivale consegna reale |
| [CAP-0067](../REGISTRO_CAPABILITY/CAP-0067.md) | Release Android firmato artifact provenance | P1 | 94 | SOURCE_REPORTED | Artifact build non e device certification |
| [CAP-0077](../REGISTRO_CAPABILITY/CAP-0077.md) | Health check permessi nativi per-capability | P1 | 94 | PROPOSTA | Permesso concesso non prova capability operativa |
| [CAP-0035](../REGISTRO_CAPABILITY/CAP-0035.md) | OCR immagini e documenti on device | P1 | 92 | SOURCE_REPORTED | Audit licenza ML Kit e processi media originali |
| [CAP-0001](../REGISTRO_CAPABILITY/CAP-0001.md) | Pianificazione di slot liberi | P2 | 91 | PROPOSTA | Verificare conflitti e non spostare eventi fissi |
| [CAP-0018](../REGISTRO_CAPABILITY/CAP-0018.md) | Backup restore con staging e rollback | P2 | 90 | SOURCE_REPORTED | Audit formati e test corrupt archive per consumer |
| [CAP-0027](../REGISTRO_CAPABILITY/CAP-0027.md) | Cattura universale condividi link testo immagine | P2 | 90 | PROPOSTA | Android share intent e consenso senza import occulto |
| [CAP-0068](../REGISTRO_CAPABILITY/CAP-0068.md) | AppLab evidence ladder exact SHA | P2 | 90 | SOURCE_REPORTED | Mai inferire device PASS da CI |
| [CAP-0023](../REGISTRO_CAPABILITY/CAP-0023.md) | Design System Flutter token-first | P2 | 89 | SOURCE_REPORTED | Riuso pattern non diventa Golden automaticamente |
| [CAP-0025](../REGISTRO_CAPABILITY/CAP-0025.md) | Schermate responsive rail e split view | P2 | 89 | SOURCE_REPORTED | No claim desktop full prima di QA multi-width |
| [CAP-0013](../REGISTRO_CAPABILITY/CAP-0013.md) | Collection e ricerca locale | P2 | 88 | SOURCE_REPORTED | Verificare performance e origine dei risultati |
| [CAP-0016](../REGISTRO_CAPABILITY/CAP-0016.md) | Inbox con categorie modificabili | P2 | 88 | SOURCE_REPORTED | Smoke fisico categoria vuota riavvio e sync |
| [CAP-0020](../REGISTRO_CAPABILITY/CAP-0020.md) | Shared Ecosystem Bridge COPY LINK | P2 | 88 | SOURCE_REPORTED | Verificare roundtrip reale e contratti consumer per versione |
| [CAP-0072](../REGISTRO_CAPABILITY/CAP-0072.md) | Entitlement RevenueCat provider truth | P2 | 88 | SOURCE_REPORTED | IAP compliance e no premium unlocked falsely |
| [CAP-0004](../REGISTRO_CAPABILITY/CAP-0004.md) | Overlay calendari esterni read-only | P2 | 87 | SOURCE_REPORTED | Verificare Android Calendar Provider e disponibilità Notes |
| [CAP-0005](../REGISTRO_CAPABILITY/CAP-0005.md) | Esportazione esplicita eventi verso calendario | P2 | 87 | ROADMAP_STORICA | Verificare provider permessi e intent senza sync bidirezionale |
| [CAP-0024](../REGISTRO_CAPABILITY/CAP-0024.md) | Motion reduced-motion e microinterazioni | P2 | 87 | SOURCE_REPORTED | Verifica accessibilita e prestazioni su device |
| [CAP-0002](../REGISTRO_CAPABILITY/CAP-0002.md) | Creazione eventi da linguaggio naturale | P2 | 86 | PROPOSTA | Parser EN IT ES FR PT con conferma e timezone |
| [CAP-0031](../REGISTRO_CAPABILITY/CAP-0031.md) | Trascrizione vocale offline opzionale | P2 | 86 | PROPOSTA | Licenza modello footprint benchmark 5 lingue e download opt-in |
| [CAP-0006](../REGISTRO_CAPABILITY/CAP-0006.md) | Lista della spesa privata e condivisa | P2 | 83 | SOURCE_REPORTED | Verificare test v0.71 e riuso senza database condiviso |
| [CAP-0010](../REGISTRO_CAPABILITY/CAP-0010.md) | Ricordi Then and Now | P2 | 83 | SOURCE_REPORTED | Usare media canonici e consenso foto |
| [CAP-0011](../REGISTRO_CAPABILITY/CAP-0011.md) | Life Threads narrativi | P2 | 82 | SOURCE_REPORTED | Non introdurre archivio parallelo |
| [CAP-0045](../REGISTRO_CAPABILITY/CAP-0045.md) | Meal plan e spesa derivata | P2 | 82 | PROPOSTA | Lista derivata con consenso e separazione proprieta dati |
| [CAP-0019](../REGISTRO_CAPABILITY/CAP-0019.md) | Store media content addressed e GC | P2 | 81 | SOURCE_REPORTED | Non uniformare database privacy separati |
| [CAP-0069](../REGISTRO_CAPABILITY/CAP-0069.md) | Automated screenshot visual regression | P2 | 81 | PROPOSTA | Baseline screen e variant certi |
| [CAP-0051](../REGISTRO_CAPABILITY/CAP-0051.md) | Mappe luoghi ricordi condivisi con ponte | P2 | 80 | SOURCE_REPORTED | Trasporto COPY LINK esplicito e autorizzato |
| [CAP-0062](../REGISTRO_CAPABILITY/CAP-0062.md) | Best Conditions Engine sensori | P2 | 80 | PROPOSTA | Score sensori non diagnosi e test runtime |
| [CAP-0063](../REGISTRO_CAPABILITY/CAP-0063.md) | Momenti ideali per focus in calendario | P2 | 80 | PROPOSTA | Consenso e niente spostamento eventi involontario |
| [CAP-0012](../REGISTRO_CAPABILITY/CAP-0012.md) | Year in Review deterministico | P2 | 79 | SOURCE_REPORTED | Non ricostruire funzione gia integrata |
| [CAP-0082](../REGISTRO_CAPABILITY/CAP-0082.md) | Deterministic UI design artwork | P2 | 79 | PROPOSTA | Non generare asset coperti da diritti |
| [CAP-0076](../REGISTRO_CAPABILITY/CAP-0076.md) | Web Clip sicuro con provenienza | P3 | 78 | PROPOSTA | Permissions share sheet e URL originale |
| [CAP-0003](../REGISTRO_CAPABILITY/CAP-0003.md) | Preparazione contestuale appuntamento | P3 | 77 | PROPOSTA | Riutilizzare reminder e note senza nuovo scheduler |
| [CAP-0007](../REGISTRO_CAPABILITY/CAP-0007.md) | Scheda workout e storico multisport | P3 | 77 | SOURCE_REPORTED | Non creare doppio diario allenamenti |
| [CAP-0009](../REGISTRO_CAPABILITY/CAP-0009.md) | Ricordi mappa geolocalizzata | P3 | 77 | SOURCE_REPORTED | Verificare permessi e nessuna condivisione GPS implicita |
| [CAP-0008](../REGISTRO_CAPABILITY/CAP-0008.md) | Import foto PDF delle schede workout | P3 | 75 | ROADMAP_STORICA | Verificare parser e conservazione file originale |
| [CAP-0014](../REGISTRO_CAPABILITY/CAP-0014.md) | Cattura rapida contestuale da calendario | P3 | 75 | PROPOSTA | Conversione evento a ricordo sempre esplicita |
| [CAP-0021](../REGISTRO_CAPABILITY/CAP-0021.md) | QR inviti condivisi 24 ore | P3 | 75 | SOURCE_REPORTED | Serve prova camera e 2 account su device distinti |
| [CAP-0075](../REGISTRO_CAPABILITY/CAP-0075.md) | Import Center per migrazioni utenti | P3 | 74 | ROADMAP_STORICA | Import validato e non perdere storico |
| [CAP-0032](../REGISTRO_CAPABILITY/CAP-0032.md) | Indicizzazione ricerca semantica locale | P3 | 73 | PROPOSTA | Modello multilingue licenza footprint e benchmark; non inserire pack base |
| [CAP-0064](../REGISTRO_CAPABILITY/CAP-0064.md) | Sonno routine e reminder adattivi | P3 | 73 | PROPOSTA | Non formulare diagnosi mediche |
| [CAP-0085](../REGISTRO_CAPABILITY/CAP-0085.md) | Diarizzazione vocale locale per appunti riunioni | P3 | 70 | PROPOSTA | Benchmark sherpa-onnx o modello compatibile su smartphone; opt-in microfono, indicatori recording, segmenti speaker non affidabili senza validazione; non aggiungere modello grande all'APK base. |
| [CAP-0074](../REGISTRO_CAPABILITY/CAP-0074.md) | Companion voice note organizer | P3 | 67 | PROPOSTA | No duplicare trascrizione vocale offline |

**Totale associazioni:** 45. Non modificare automaticamente la roadmap del prodotto.
