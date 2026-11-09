# IDEA VALIDA — Store interno di template originali per Notes e Anna's Diary

**Data**: 9 novembre 2026. **Stato decisionale:** **IDEA VALIDA / BACKLOG APPROVATO COME CONCETTO**, non approvazione di sviluppo, pubblicazione, prezzo o variazione del Product Bible. **Prezzo candidato:** **€3,99 per singolo template**, da testare; non una tariffa già attiva.

## Maxi-step 1 — Standard tecnico condiviso integrato (09/11/2026)

- [**Template Engine Standard v1 — App-Factory-Core**](https://github.com/riccardopinato/App-Factory-Core/tree/main/contracts/template_engine_v1) è stato creato e integrato con la [PR Core #89](https://github.com/riccardopinato/App-Factory-Core/pull/89), commit `d4ed1185d36d419228fba6b57a979cde308bd321`.
- Contratto **CANDIDATE / static-only**: manifest JSON Schema v1, esempi Notes/Anna, validatore e test collegati alla CI Factory. **Non** è un engine Flutter utilizzabile, un Golden certificato, un catalogo prodotti Play/Apple o un sistema di acquisto.
- Gli step 2–5 restano separati: UX app-native → adapter reale + template gratuito → store UI → billing verificato. Lo standard non autorizza automaticamente SKU, nuove CAP, cambi Product Bible o modifiche ai repository delle app.

## Proposta
Uno **store interno a ciascuna app** con catalogo di modelli **originali per l'app**, scheda anteprima, contenuti inclusi, pulsante Acquista, sblocco permanente, installazione **reversibile** e sezione 'I miei template'. Non creare una nuova app-store né costringere l'utente ad abbonarsi. Prevedere alcuni preset gratuiti utili, senza impoverire le funzioni base.

| Aspetto | Notes-Ecosistema | Anna's Diary |
|---|---|---|
| Tipi di template | Second Brain personalizzabile, studio, biblioteca libri, planner progetti, dashboard creativa, Vision Board | Diario guidato, routine leggere, ricordi/album, viaggio, obiettivi e Vision Board personali |
| Modalità di installazione | Istanziare `PersonalTemplates` e i writer Note/Task/Projects canonici | Istanziare preset diario/rituali/agenda canonici, con confini privato/`Noi ♡` |
| Cosa NON vendere | Altri engine duplicati o export commerciali di terzi | Privacy/Vault, attività di base, permessi condivisi o funzioni fuori dal Product Bible |

## Requisito vincolante: template nativi e su misura per ciascuna app

**Decisione esplicita del proprietario (09/11/2026):** ogni template destinato allo store deve essere **progettato specificamente per l'app che lo vende**. Non basta esportare, caricare o imitare un template Notion. Notion è esclusivamente una fonte di ispirazione/ricerca; il prodotto acquistato è una configurazione o un'esperienza **originale e nativa** che funziona in Notes-Ecosistema o Anna's Diary senza dipendere da un account Notion.

- **Notes-Ecosistema**: un template deve attivare flussi concreti per note, task, progetti, collezioni, knowledge o lavagna usando **modelli, editor, writer e persistenza canonici di Notes**. Navigazione, anteprime, filtri, personalizzazione e backup devono essere coerenti con il prodotto, non un clone delle pagine Notion.
- **Anna's Diary**: un template deve essere calibrato su **agenda leggera, diario, ricordi, routine, obiettivi personali o Noi ♡**, riutilizzando editor, rituali, agenda, preferenze e permessi esistenti. Deve rispettare design **DS6/editoriale**, cinque lingue, private-by-default e confini Vault/Noi. Non aggiungere un sistema PARA/workspace professionale o una seconda source of truth.
- **Esperienza di acquisto e uso**: preview fedele a come apparirà *dentro l'app*, scelta di opzioni prima dell'applicazione, creazione di contenuto **modificabile** dall'utente nei flussi normali, installazione reversibile, nessuna perdita di dati e compatibilità esplicita per piattaforma/versione. Il template deve apportare valore reale, non un semplice cambio di colori o una pagina statica a €3,99.
- **Varianti per due app**: se lo stesso concetto è utile a entrambe, sviluppare **due adattamenti originali separati**, con UX/permessi/modello dati propri; catalogazione e titolarità commerciale rimangono per-app. Il riferimento di ricerca centrale resta unico, senza doppia copia del materiale esterno.
- **Gate di ammissione allo store**: una scheda di ricerca E1/E2 **non** è un articolo vendibile. Occorrono specifica per app, asset originali con diritti, dati sintetici per anteprima, test su editor/store canonici, backup/restore, accessibilità, permessi e acquisto/ripristino. Solo dopo tali prove si può considerare lo stato `STORE_READY`.

**Stato di questa modifica:** requisito di progettazione documentato, **NON** implementazione dello store, della UI, di template premium o dell'acquisto in-app.

## Vincolo assoluto: originalità/licenze
Gli ZIP Notion analizzati **non sono stock da rivendere**. Il Book Tracker Mindful Setups dichiara esplicitamente divieto di rivendita/redistribuzione senza autorizzazione. Anche quando una licenza non è riportata, non presumere il diritto commerciale di copiare media, formule, testi, contenuti o strutture puntuali.

L'idea monetizzabile è **creare nuovi template Flutter originali**, ispirati a esigenze e pattern generali; non vendere, reimpacchettare o rendere scaricabili i file Notion acquistati.

## Modello commerciale da testare
- Alcuni template di base sempre gratis; acquisto **una tantum** dei singoli template premium.
- **€3,99** come ipotesi iniziale per template ricco. Valutare esperimenti con preset più semplici e bundle, senza dichiarare tassi di conversione/ricavi non misurati.
- Acquisto come **non-consumable / entitlement durevole**; ripristino su reinstallazione e cambio telefono, gestione rimborsi/revoche.
- **Entitlement per-app e per-store**, salvo progetto cross-app separato esplicitamente definito; non promettere acquisto una volta e disponibilità in entrambe le app.
- Web/PWA: serve soluzione distinta e verificata; il fatto di usare Flutter non equivale a supporto del Play Billing o StoreKit nella PWA.

## Vincoli di pagamento attuali
- **Android su Google Play**: contenuti digitali in-app normalmente tramite **Google Play Billing**, salvo eccezioni/programmi territoriali applicabili. Fonte: https://support.google.com/googleplay/android-developer/answer/9858738?hl=it
- **iOS App Store**: sblocchi premium digitali normalmente con **In-App Purchase / StoreKit**, secondo linee guida ed eccezioni regionali. Fonte: https://developer.apple.com/app-store/review/guidelines/
- Per le opzioni Google Play una tantum: https://developer.android.com/google/play/billing/one-time-products
- **RevenueCat** presente in Anna come adapter entitlement, ma il collegamento di nuovi product ID richiede implementazione e prova; per Notes verificare lo stack esistente.

## Requisiti tecnici prima di codificare
1. Catalogo manifest versionato (ID per app, nome, descrizione, immagini **autorizzate**, locale, tag, compatibilità versione e migrazioni).
2. Preview reale offline, permessi espliciti, applicazione con undo/rollback e separazione template vs dati reali dell'utente.
3. Store provider e backend verify purchase/restore/refund dove necessario; controllo idempotente, no acquisti doppi; accesso consentito anche offline dopo legittimo sblocco verificato.
4. Dati creati dall'utente conservati dopo la rimozione di un template, senza delete/purge involontari. Distinguere revoca di accesso al catalogo da proprietà delle note/ricordi già creati.
5. Gate privacy (Anna + `Noi ♡`), valute localizzate e pricing, fiscalità, policy store, accessibilità, confronto Free/Premium, dimensioni download e compatibilità Web/Android/iOS.
6. Piccolo pilota: **2 template originali premium per app** più alcuni gratuiti, test reale di acquisto/ripristino/reso/assenza rete prima di estendere.

**Non eseguito**: alcun sistema di pagamento, SKU, schermata Store, nuovo database, emissione di fatture, release, acquisizione di licenze o redistribuzione di template altrui.
