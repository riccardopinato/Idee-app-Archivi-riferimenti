# X10-002 — Shortlist commerciale 10x (prevalidazione; non decisione di investimento)

**Audit source-only:** 12/11/2026. **Factory baseline:** [Core@c5adc147](https://github.com/riccardopinato/App-Factory-Core/commit/c5adc147046beb7024629466d10eeb799c3c2619), Master v27, Golden Index v29.
**Scope:** selezione tecnica di 2–3 candidati per la successiva market validation `X10-034` e decisione umana `X10-035`. Non sono stati consultati dati Play Console, installazioni, ricavi, keyword volume, CPC o retention. Non si dichiara nessuna monetizzazione/launch di produzione.
**Criteri:** promessa utente comprensibile, codice esistente, costo incrementale/release, monetizzazione prevista da Product Bible, differenziazione, dipendenze esterne, distanza dai gate fisici/Store. Valutazione qualitativa; **nessuno score numerico è una misura di mercato**.

## Tre prodotti selezionati per la fase di verifica

### 1. Battery Guard — pilota primario, utility Flutter
- **Snapshot:** [Battery_Guard@1343f09d](https://github.com/riccardopinato/Battery_Guard/commit/1343f09d21ace8adf3976b3fd347183f38e5ab68), [README](https://github.com/riccardopinato/Battery_Guard/blob/1343f09d21ace8adf3976b3fd347183f38e5ab68/README.md), [Product Bible](https://github.com/riccardopinato/Battery_Guard/blob/1343f09d21ace8adf3976b3fd347183f38e5ab68/PRODUCT_BIBLE.md), [Release Gate](https://github.com/riccardopinato/Battery_Guard/blob/1343f09d21ace8adf3976b3fd347183f38e5ab68/RELEASE_GATE.md).
- **Fit:** problema concreto (avvisi ricarica, telemetria spiegabile), Free utile e Pro lifetime senza abbonamento; ampia superficie riutilizzabile per signing, widget, notifications, billing consent e QA.
- **Prove software:** sorgente v1.8.1+27, artefatti INTERNAL Free e Premium Test firmati indicati dal repository; ciò NON certifica installazione, upgrade sul dispositivo, acquisti Play o distribuzione.
- **Gate aperti:** collaudo Samsung + Xiaomi/Redmi, update-in-place, verificatore server-side dei purchase token e refund lifecycle, produzione AdMob/consenso, Play Internal Testing e governance branch/release. Nessun prezzo/revenue confermato.
- **Ipotesi da falsificare in X10-034:** disponibilità a pagare lifetime per insight aggiuntivi rispetto agli strumenti OEM e retention nelle sessioni d'uso.

### 2. Rotate 180° — micro-utility Kotlin, controprova prodotto leggero
- **Snapshot:** [180FlipCharge@b60480c](https://github.com/riccardopinato/180FlipCharge/commit/b60480c0161b2063679004c178f8a89952a88f74), [README](https://github.com/riccardopinato/180FlipCharge/blob/b60480c0161b2063679004c178f8a89952a88f74/README.md).
- **Fit:** funzione puntuale e spiegabile (reverse portrait 0°/180°, tile Quick Settings, eccezioni app). Stack Android nativo esistente; buon confronto con l'utility Flutter senza aprire una nuova codebase.
- **Modello dichiarato nel repo:** acquisto upfront €4,99, senza ads; è una scelta prodotto **registrata**, non prezzo validato o autorizzazione a pubblicare.
- **Gate aperti:** firma INTERNAL configurata in GitHub Secrets e build manuale, nessuna prova qui di acquisto reale, distribuzione o test fisico; verificare policy Play per FGS/overlay/usage access, riavvio, eccezioni app e compatibilità OEM, senza promettere rotazione su ogni device.
- **Ipotesi da falsificare:** domanda sufficiente per una funzionalità specializzata, costo di supporto/compatibilità inferiore al margine di un lifetime/upfront.

### 3. World Days — pilota editoriale/retention, *condizionale*
- **Snapshot:** [World-Days@d84976e](https://github.com/riccardopinato/World-Days/commit/d84976e1f9f210a4748fa193feae169e78de625f), [README](https://github.com/riccardopinato/World-Days/blob/d84976e1f9f210a4748fa193feae169e78de625f/README.md), [Roadmap](https://github.com/riccardopinato/World-Days/blob/d84976e1f9f210a4748fa193feae169e78de625f/ROADMAP.md).
- **Fit:** caso differente dalle due utility: catalogo, contenuti di approfondimento, frequenza di ritorno e possibile inventory pubblicitaria; valida se la Factory riesce a mantenere contenuti affidabili a basso costo.
- **Prove e limite:** 1.111 ricorrenze in catalogo; 46 origini individualmente documentate IT/EN nell'attuale ledger, 1.065 ancora da ricercare con lo stesso standard. 56 contenuti editoriali preesistenti sono un conteggio distinto. ES/FR/DE/PT e revisione editoriale indipendente restano aperti.
- **Gate aperti:** qualità/fonte editoriali, QA/retention, valutazione ads e consenso, build/deploy/store reali; nessun APK o produzione affermati sulla base dei soli commit.
- **Ipotesi da falsificare:** ritorno organico, rapporto contenuto/tempo, sostenibilità delle ricerche a 100 ricorrenze per lotto, retention e ricavi pubblicitari netti.

## Alternative considerate ma non preferite nella prima coorte
- **Cooking Anime:** [repo@fb4c8cf](https://github.com/riccardopinato/In-Cucina-con-gli-Anime/commit/fb4c8cf5d7b0e8de0ada7649a1ef8b7e981ed465), [Product Bible](https://github.com/riccardopinato/In-Cucina-con-gli-Anime/blob/fb4c8cf5d7b0e8de0ada7649a1ef8b7e981ed465/docs/PRODUCT_BIBLE.md). 162 ricette con revisione IT 51–162 e traduzioni/asset da validare; interessante, ma dipende dalla certificazione contenuti e dai diritti. Mantenerla come sostituta condizionale se World Days non supera `X10-034`.
- **Notes-Ecosistema:** elevata complessità e molte capability, con Plus/Needle ancora da certificare su device e billing. Più adatta per test kit riutilizzabili che per il primo esperimento di ricavi.
- **PDF Pocket Tools:** buona idea futura ma nessun prodotto proprio verificato per un go-to-market vicino; evitare di confondere opportunità con app già pronta.

## Decisione limitata a X10-002
**Shortlist di prova:** Battery Guard, Rotate 180°, World Days (quest'ultima condizionale). Non è l'approvazione finale di investimento/launch. Non aggiorna Product Bible, roadmap delle app, prezzi, billing o release.

**Handoff obbligatorio:**
1. `X10-034` raccoglie dati comparabili e datati per domanda/competitor, keyword, distribuzione, policy, acquisizione e costi per tutti e tre i candidati (più Cooking Anime come sostituto); fonti con URL/data, niente stime spacciate per osservazioni.
2. `X10-035` richiede una scelta umana 2–3 prodotti e budget. Prima di quel gate nessun impegno a campagne, nuovi SDK analytics, pagamenti o release.
3. `X10-036/037/038/039` restano vincolati a privacy, pricing, approvazioni Play e coorti reali; il completamento della shortlist NON sblocca pubblicazione.
4. Distingui sempre `SOURCE`, `CI`, `DEVICE`, `STORE` e `BUSINESS_MEASURED`. Nessuno dei tre candidati ha `STORE_READY` attestato dal presente audit.

**Acceptance X10-002:** 3 candidati nominati con fonti pinned, trade-off e handoff ai task dipendenti. Evidenza READ_ONLY; nessun claim di validazione domanda né metriche inventate.
