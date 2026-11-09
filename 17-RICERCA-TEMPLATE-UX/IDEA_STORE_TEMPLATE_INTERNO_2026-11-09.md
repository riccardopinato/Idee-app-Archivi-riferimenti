# IDEA VALIDA — Store interno di template originali per Notes e Anna's Diary

**Data**: 9 novembre 2026. **Stato decisionale:** **IDEA VALIDA / BACKLOG APPROVATO COME CONCETTO**, non approvazione di sviluppo, pubblicazione, prezzo o variazione del Product Bible. **Prezzo candidato:** **€3,99 per singolo template**, da testare; non una tariffa già attiva.

## Proposta
Uno **store interno a ciascuna app** con catalogo di modelli **originali per l'app**, scheda anteprima, contenuti inclusi, pulsante Acquista, sblocco permanente, installazione **reversibile** e sezione 'I miei template'. Non creare una nuova app-store né costringere l'utente ad abbonarsi. Prevedere alcuni preset gratuiti utili, senza impoverire le funzioni base.

| Aspetto | Notes-Ecosistema | Anna's Diary |
|---|---|---|
| Tipi di template | Second Brain personalizzabile, studio, biblioteca libri, planner progetti, dashboard creativa, Vision Board | Diario guidato, routine leggere, ricordi/album, viaggio, obiettivi e Vision Board personali |
| Modalità di installazione | Istanziare `PersonalTemplates` e i writer Note/Task/Projects canonici | Istanziare preset diario/rituali/agenda canonici, con confini privato/`Noi ♡` |
| Cosa NON vendere | Altri engine duplicati o export commerciali di terzi | Privacy/Vault, attività di base, permessi condivisi o funzioni fuori dal Product Bible |

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
