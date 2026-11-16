# App e concept senza repository GitHub attuale verificato — audit CAP-only

**Perimetro:** 24 etichette/prodotti presenti nel registro delle 199 capability, ma **senza un repository con lo stesso nome fra i 35 repository GitHub visibili**. Non significa che non esistano file locali, app installate o repo con alias. Il loro stato qui è **CAP_ONLY** e non un audit di codice. Gli stati riportati derivano dai valori `app_states` del registro, per lo più `PROPOSTA` o `ROADMAP_STORICA`.

**P** priorità di prodotto (0–100); **F** fattibilità ipotetica sulla base del perimetro CAP (0–100), **confidenza inferiore** rispetto alle app con repository ispezionato. Le stelle sono fonti di idee, non prove di implementazione. Se emergono repo/alias, rivalutare scores sulla base del codice e test reali.

## App-Profiles
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0058/0088. **Stato:** CAP-only PROPOSTA; nessun repository corrente verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Profili Android che espongono on/off rotazione e capability di desktop mode, senza override occulto | **83** | **77** | CAP-0058/0088 | Verificare permission/capability OS |
| GATE | Separare App-Profiles, EdgeDock e DeskPilot: una policy condivisa, prodotti solo se differenziati | **87** | **84** | CAP-0088 | Nessuna nuova app per un alias |
| MIGLIORIA | Preset locali esportabili e ripristino precedente non distruttivo | **75** | **82** | CAP-0088 | No auto-apply senza consenso |

## BeerClass AI
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0034/0035/0036. **Stato:** CAP solo PROPOSTA; sorgente non trovato nell'elenco GitHub accessibile.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Scansione etichetta birra senza barcode con OCR on-device e conferma marca/stile | **91** | **71** | CAP-0036 | Non inventare match catalogo assenti |
| MIGLIORIA | Diario assaggi rapido, profilo gusto e ricerca locale con dati realmente registrati | **84** | **81** | CAP-0035 | Verificare se implementato sul codice prima di costruirlo |
| GATE | Provenienza etichette/immagini e data integrity su note salvate | **80** | **83** | CAP-0035 | Non usare immagini commerciali senza permesso |

## CashMate AI
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0034. **Stato:** CAP solo PROPOSTA; nessun repo corrente verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | OCR scontrini con bozza spesa, importo e data da correggere manualmente | **92** | **73** | CAP-0034 | Non acquisire spese silenziosamente |
| GATE | Valute, separatori numerici, errori OCR, backup cifrato e non duplicazione transazioni | **96** | **79** | CAP-0034 | Finanza personale: correttezza prima di grafici |
| NUOVA | Categorie ricorrenti e budget su dati canonici locali con spiegazione del calcolo | **80** | **85** | CAP-0034 | No account/cloud obbligatorio |

## CleanOS
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0059. **Stato:** CAP solo PROPOSTA; possibile overlap con Easy-Debloat.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Decidere CleanOS vs Easy-Debloat e fonte unica per il core debloat | **95** | **89** | CAP-0059 | Evita app duplicata |
| RIUSO | Interfaccia reversibile per disable/re-enable pacchetti tramite Shizuku/ADB | **93** | **70** | CAP-0059 | Nessun comando irreversibile senza backup/recovery |

## CmdPocket
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0084/0177/0178/0179/0180/0193/0194/0199. **Stato:** 8 CAP in stato PROPOSTA; repo non disponibile.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Command palette locale per snippet, trasformazioni testo e copia con rollback | **91** | **84** | CAP-0084/0180/0194 | Compatibile con workflow Flutter/web se definito |
| MIGLIORIA | Espansione testo confinata all'editor; livello OS solo con policy Android verificata | **80** | **70** | CAP-0178/0179 | Evita accessibility abuse |
| RICERCA | MCP locale read-only su task/agenda con ACL e consenso | **70** | **61** | CAP-0199 | Esporre dati personali solo autorizzati |

## DeskPilot
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0088. **Stato:** CAP solo PROPOSTA; overlap con EdgeDock e Deskland.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Prova realistica launcher e multi-window capability con recupero layout stock | **91** | **56** | CAP-0088 | Dipendenze OEM e desktop mode |
| RIUSO | Preset workspace derivato dall'engine Deskland solo dopo test e licenze | **77** | **67** | CAP-0088 | Non copiare GPL upstream |

## DevPocket Tools
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0084. **Stato:** CAP solo PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| NUOVA | Suite offline testo/JSON/QR/hash/conversioni come strumenti indipendenti | **85** | **91** | CAP-0084 | Poca superficie permessi, testing deterministico |
| MIGLIORIA | Clipboard su richiesta, cronologia opt-in e dati sensibili cancellabili | **79** | **89** | CAP-0084 | Non raccogliere clipboard in background |

## Downloads Butler
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0083. **Stato:** CAP solo PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Treemap storage e raggruppamento file con review-only, donor Omni Cleaner | **90** | **78** | CAP-0083 | Mutazioni sempre con conferma e snapshot revalidation |
| MIGLIORIA | Filtri file vecchi/grandi e suggerimento archiviazione locale | **79** | **84** | CAP-0083 | No cancellazioni automatiche |

## Easy Debloat
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0059. **Stato:** ROADMAP_STORICA, nessuna sorgente GitHub verificata; stato dispositivo Shizuku non verificato in questo audit.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Whitelisting pacchetti critici e backup lista enabled/disabled con ripristino completo | **98** | **71** | CAP-0059 | Disabilitare componenti sistema può rendere telefono inutilizzabile |
| RIUSO | Procedura assistita Shizuku/ADB e report dry-run con rollback | **94** | **76** | CAP-0059 | Nessun root o rimozione permanente predefinita |
| GATE | Unificare decisione di prodotto con CleanOS | **89** | **90** | CAP-0059 | Evitare manutenzione doppia |

## EdgeDock
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0088. **Stato:** CAP solo PROPOSTA; parte della stessa famiglia DeskPilot/App-Profiles.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Dock Android che non prende il ruolo Home senza opt-in e ripristino immediato | **93** | **63** | CAP-0088 | P0 launcher/OEM |
| RIUSO | Pattern OpenTaskbar/LumaBar/OpenWidget solo UX; touch target/gestures Android nativi | **79** | **77** | CAP-0023/0088 | Nessun Win32/WPF port |

## GrillBoss
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0052. **Stato:** CAP solo PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| NUOVA | Meteo/grigliate con finestre favorevoli e avvisi meteo a fonte/timezone visibile | **83** | **73** | CAP-0052 | Provider attuale non verificato |
| MIGLIORIA | Checklist cottura/equipaggiamento e timer offline non alimentare automatico | **77** | **89** | CAP-0052 | Gestione semplicissima senza account |

## Home Assets Passport
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0080. **Stato:** CAP solo PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| NUOVA | Schede oggetti con garanzia, seriale facoltativo e scadenze documenti | **88** | **85** | CAP-0080 | Storage locale con export e backup |
| GATE | Protezione allegati personali, cancellazione completa e permessi per import | **92** | **78** | CAP-0080 | Dati sensibili e reminder opt-in |

## MealMate
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0044/0045/0155. **Stato:** 3 CAP PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Menu settimanale da ricette canoniche e spesa derivata da ingredienti verificati | **89** | **77** | CAP-0044/0045 | Sfruttare TasteAI come donor non duplicato |
| MIGLIORIA | Sostituzioni ingredienti e anti-spreco con provenienza e cautela allergeni | **87** | **70** | CAP-0155 | Non inferire sicurezza alimentare |
| GATE | Confrontare MealMate vs TasteAI: prodotti distinti solo con user journey differente | **84** | **88** | CAP-0044 | Evita duplicare ricerca ricette |

## PDF Pocket Tools
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0037/0038. **Stato:** CAP PROPOSTA e ROADMAP_STORICA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Toolkit split/rotate/merge/lock con preview e salvataggio sicuro | **88** | **79** | CAP-0037 | Valutare se incorporare invece in PDF-Unifier |
| GATE | Evita due copie dello stesso engine PDF e convalida output | **95** | **84** | CAP-0038 | Decisione prodotto prima di nuovo repo |

## SafeShare
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0039. **Stato:** CAP solo PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| RIUSO | Condivisione di copie media senza geotag/EXIF con anteprima prima/dopo | **94** | **82** | CAP-0039 | Donor EXIF di Omni Cleaner, non originali alterati |
| GATE | Prova su HEIC/JPEG, MediaStore/SAF, copia e cancellazione metadati effettiva | **92** | **66** | CAP-0039 | No claim 'privacy completa' non testato |

## SleepMax Coach
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0062/0064/0154. **Stato:** Roadmap storica + CAP proposte, repo non disponibile per prova live.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Verifica persistenza routine, reminder e notifiche dopo riavvio/Doze | **96** | **78** | CAP-0064 | Comportamento Android reale non attestato |
| RIUSO | Best Conditions descrittive da FocuSense, senza causalità sonno-sensori | **78** | **72** | CAP-0062 | No diagnosi cliniche |
| NUOVA | Proposte routine predittive Markov opt-in con correzione manuale e privacy | **61** | **53** | CAP-0154 | Algoritmo complesso e valore incerto |

## WEB-002
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0054. **Stato:** Web-utility candidata, CAP PROPOSTA; fonte/provider non verificati.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Comparatore prezzi carburante con fonti pubbliche, timestamp e schema normalizzato | **94** | **69** | CAP-0054 | No dati non licenziati o vecchi |
| MIGLIORIA | Filtri area/carburante e costo percorso solo da dati misurati | **82** | **79** | CAP-0054 | Frequenza aggiornamenti esplicita |

## WEB-004
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0079. **Stato:** Web-utility candidata, CAP PROPOSTA.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Report stipendi/fisco con paese, anno fiscale, fonti normative e disclaimer chiari | **95** | **61** | CAP-0079 | Normativa locale e test di formule |
| MIGLIORIA | Calcolo scenari verificabili con input simulati e nessun dato finanziario persistito per default | **87** | **81** | CAP-0079 | Non rilasciare come consulenza fiscale |

## WEB-008
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0078. **Stato:** Web-utility candidata, CAP PROPOSTA.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Definire specifico provider/location market e campo data freshness prima del prodotto | **90** | **67** | CAP-0078 | CAP troppo generica per un MVP senza scope |
| MIGLIORIA | Adapter multi-provider con fallback e rate limit espliciti | **79** | **72** | CAP-0078 | Non assumere API gratis |

## WEB-009
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0054/0078. **Stato:** Web-utility candidata; prezzi carburanti + provider location.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Deduplicare WEB-002 e WEB-009: servizio prezzi vs interfaccia location | **94** | **88** | CAP-0054/0078 | Un solo source owner del feed |
| MIGLIORIA | Mappa prezzi con geolocation consenso esplicito e fallback lista | **82** | **75** | CAP-0078 | Nessuna posizione obbligatoria |

## WEB-012
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0053/0078. **Stato:** Web-utility candidata; Sun/Moon locale + location provider.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| NUOVA | Calcolo sole/luna offline per coordinate/timezone con test date DST e alte latitudini | **91** | **80** | CAP-0053 | Algoritmo e fonti testabili senza provider cloud |
| MIGLIORIA | Usabilità senza GPS: città manuale, accessibilità e fonte precisione | **78** | **89** | CAP-0078 | Mappa opzionale |

## WEB-014
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0078/0087. **Stato:** Web-utility candidata; layer geografici pubblici.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| GATE | Source freshness, incident status e fallback nel caso feed assente | **96** | **72** | CAP-0087 | Non presentare allerta non ufficiale come live |
| MIGLIORIA | Layer volontari e fonte evento visibile con differenziazione da routing GPS | **79** | **75** | CAP-0087 | Non duplicare TrailPath |

## WEB-UTILITY
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0084. **Stato:** Categoria suite utility, non singola app rilasciata.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| NUOVA | Raggruppare convertitori/QR e tool client-side privacy-first sotto un hub | **80** | **90** | CAP-0084 | Dedup con DevPocket e CmdPocket |
| GATE | Separare prodotti stand-alone da template riutilizzabili | **82** | **91** | CAP-0084 | Niente web utility clone non necessario |

## Work-Time-Keeper
**Evidenza:** [CAP registry](../REGISTRO_CAPABILITY.json) · CAP-0079/0176/0177/0195. **Stato:** 4 CAP PROPOSTA; nessun repo verificato.

| Tipo | Opportunità | P | F | CAP | Gate |
|---|---|---:|---:|---|---|
| NUOVA | Timesheet per task e progetto esportabile con arrotondamenti e audit delle modifiche | **92** | **80** | CAP-0195 | Local-first e data owner chiaro |
| RIUSO | Timeline attività e AFK opt-in da ActivityWatch/WakaTime; rilevare solo dati consentiti | **87** | **60** | CAP-0176/0177 | Differenze piattaforma Windows/Android |
| GATE | Report fiscale/per ore paese specifico, privacy e confine con FIN agent | **83** | **65** | CAP-0079 | No consulenza normativa automatica |

