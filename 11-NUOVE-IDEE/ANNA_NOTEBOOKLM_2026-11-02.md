# Anna's Diary — 15 proposte NotebookLM (02/11/2026)

**PROPOSTE / ANALISI NON APPROVATA**. Esclusa IA per l'agenda, nessuna modifica alla roadmap o a RevenueCat. Fonte: "Nuovo Documento di testo (4).txt", 113 righe, SHA-256 0ac109c023523b466f71cfefe53232733d5450b7fb1164da02f560220a6c5613. Nessun link alle affermazioni di mercato nell'originale.

Confronto con Anna's Diary main 827bb61620960d8867eb03e453d142013aada786 (Product Bible, roadmap, UI5, widget bridge, Vault, Weekly Review, RevenueCat). Factory Core cf931f8031ca973cb0a5467a8e83c865cd1e9def, Master 27 / Golden Index 23. Privacy #215 resta Draft **ON HOLD**.

## Mappatura capability formalizzata

[Apri la matrice canonica delle 15 idee](../12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_ANNA_NOTEBOOKLM_2026-11-02.md): 7 CAP nuove (0141…0147), 5 estensioni di CAP esistenti. Identificativi editoriali AD-NL26 e priorità originali conservati; nessuna idea P3 esclusa reinserita. Le nuove CAP possono ricevere priorità tecnica diversa secondo lo score ufficiale.

## Classifica e categorie

Score editoriale 0–100: U=utilità, D=domanda ipotizzata, V=viralità, M=monetizzabilità, F=fattibilità, S=sinergia, R=rischio (10=alto). Assi 1–10; formula della raccolta IA 02/11: round(2.4U + 2D + 1.2V + 1.8M + 1.6F + S − 2 max(0,R−5)). Classi **solo per questo lotto** P1 >=75; P2 60–74. La classifica attiva comprende soltanto P1 e P2. Non confrontare con gli score delle CAP, né usare P1 come autorizzazione.

| Rang | ID idea | Sezione | Proposta | U/D/V/M/F/S/R | Score | Priorità | Esito |
|---:|---|---|---|---|---:|---|---|
| 1 | AD-NL26-01 | Noi ♡ | Domanda del giorno con doppia rivelazione | 9/8/8/8/8/9/5 | 83 | P1 | MVP candidato |
| 2 | AD-NL26-03 | Ricordi | Lettera al me futuro | 8/8/7/7/8/9/5 | 78 | P1 | MVP candidato |
| 3 | AD-NL26-02 | Noi ♡ | Capsula condivisa a scadenza | 9/8/9/8/6/9/7 | 77 | P1 | Dipende da privacy e sync |
| 4 | AD-NL26-11 | Agenda/widget | Widget Oggi e Crea in 1 tap | 9/9/5/7/7/9/6 | 76 | P1 | Android-first |
| 5 | AD-NL26-05 | Noi/widget | Countdown prossimo evento di coppia | 9/8/7/7/6/8/6 | 74 | P2 | Dopo widget Oggi |
| 6 | AD-NL26-12 | Agenda/notifiche | Fatto / 10 min / 1 ora | 9/8/3/8/7/9/6 | 74 | P2 | QA native |
| 7 | AD-NL26-14 | UI | Preset Dark Velvet | 7/8/6/6/8/10/3 | 74 | P2 | Estendere tema esistente |
| 8 | AD-NL26-15 | UI | Tipografia editoriale Manrope/Lora | 7/8/5/6/9/10/3 | 74 | P2 | Già presente, solo audit |
| 9 | AD-NL26-07 | Analytics | Heatmap attività/abitudini e mood opt-in | 8/7/6/7/8/8/6 | 72 | P2 | Statistiche descrittive |
| 10 | AD-NL26-04 | Ricordi/share | Biglietti con QR e pagina Web | 8/7/9/8/6/8/8 | 70 | P2 | Gate divulgazione |
| 11 | AD-NL26-13 | UI | Haptics semantici | 7/7/3/6/9/10/3 | 70 | P2 | Quick win |
| 12 | AD-NL26-16 | UI/Home | Dynamic cards riordinabili | 8/8/5/7/6/9/6 | 70 | P2 | Solo riuso Home attuale |
| 13 | AD-NL26-17 | Monetizzazione | Freemium, abbonamenti e lifetime | 8/7/4/9/7/9/7 | 70 | P2 | Business test, non attivare |
| 14 | AD-NL26-06 | Noi/widget | Foto quotidiana del partner | 7/8/9/7/5/8/8 | 66 | P2 | Rinvio: privacy/consenso |
| 15 | AD-NL26-09 | Vault | Documenti PDF cifrati | 8/7/4/8/5/8/8 | 62 | P2 | Rinvio: threat model |

## Valutazione e MVP di ogni idea

**AD-NL26-01 Domanda Noi ♡:** il miglior differenziatore quotidiano. Catalogo locale di domande, risposta nascosta fino a quando entrambi hanno inviato, nessuna notifica spoiler, disconnessione e account switch, consenso/revoca. L'obiettivo non è pressione sul partner o streak obbligatori; validare con utenti reali la frequenza di ritorno.

**AD-NL26-02 Capsula coppia:** testo e singola foto, data concordata, reveal esplicito sincronizzato. Riutilizzare ricordi/media canonici. Fuso, manomissione orologio, offline, backup, partner rimosso e problemi cross-device vietano claim di blocco crittografico assoluto. Privacy #215 sospesa blocca nuove superfici private.

**AD-NL26-03 Lettera futura:** feature personale senza nuovo server: testo+data+promemoria, recupero backup, possibilità di annullare/aprire anticipatamente con conferma. Piccolo costo, buona occasione di ritorno in app.

**AD-NL26-04 Biglietto QR:** prima PNG/PDF stampabile in locale; solo successivamente pagina Web/PWA se opt-in con token non indovinabile, revoca, scadenza, preview anonima, noindex e EXIF safe. **Mai** pubblicare in automatico diario e ricordi riservati.

**AD-NL26-05 Countdown Noi:** evento condiviso autorizzato, widget Home/lockscreen con etichetta neutra quando serve. Aggiornamenti OS non garantiti in tempo reale. Android e iOS necessitano adapter nativi e QA separati.

**AD-NL26-06 Foto del partner widget:** media privati in launcher/lockscreen rischiano leak anche senza aprire l'app. Ogni immagine opt-in, possibilità di revoca e invalidazione cache su due device. Rinviare prima del gate #215.

**AD-NL26-07 Heatmap:** visualizzare solo task/diario/gratitudine realmente tracciati, distinguendo nessun dato da valore zero. Mood solo se inserito volontariamente. Nessun dato ciclo del Vault in analytics aperta.


**AD-NL26-09 PDF Vault:** ambito potenzialmente vendibile ma ad alto rischio: file temporanei in chiaro, thumbnail, stream decryption, backup/recovery, Web/iOS, limiti file, perdita chiavi e sicurezza locale. Non promettere cifratura hardware per ogni dato.


**AD-NL26-11 Widget Oggi/Crea:** timeline, cattura e widget bridge già esistono; riusare prossimo evento e un deeplink per cattura, senza replicare tutta timeline 00–24. Dati privati sempre mascherati, test idempotenza e launcher.

**AD-NL26-12 Notifiche:** azione Fatto e ritardo 10 min come MVP, poi 1 h; write canonici, niente doppia esecuzione, test background/killed, OEM, timezone, account, notifiche sensibili.

**AD-NL26-13 Haptic:** lightImpact solo per cattura, task completato, conferma sblocco; NON per ogni tab. Configurabile e disabilitabile, accessibilità, Free polish.

**AD-NL26-14 Dark Velvet:** palette candidata #0D0D12 / #E2A9B8 entro temi Rose/HSV già previsti, non nuovo motore. Verifica contrasto testo, 70 screenshot baseline/candidati e tema scuro.

**AD-NL26-15 Editoriale:** Manrope/Lora e linguaggio Journal già approvati/implementati UI5. Non avviare redesign duplicato; soltanto audit font scale, spacing, shadow, screenshot, accessibilità.

**AD-NL26-16 Home riordinabile:** esistono già card Oggi e Weekly Review. Prototipo con riordino di 2–3 card canoniche prima di nuova griglia; niente nuovo database. Card meteo richiede provider/licenza commerciale.

**AD-NL26-17 Prezzi:** NotebookLM ipotizza €2,99/mese, €19,99/anno, €49,99 lifetime e trial 7 giorni; **non configurati né approvati**. Sconto annuale 44,3% vs mensile. Il lifetime può non coprire storage cloud continuo. Free deve tutelare accesso e recupero dei dati; misurare funnel e costi.

## Errori e fonti critiche

Il documento attribuisce nomi ERRATI ai CAP: 0041 è palette foto (non E2EE); 0052 meteo outdoor (non lockscreen widget); 0038 PDF Pocket Tools (non Time Lock); 0012 Year in Review (non QR Generator); 0015 ricerca globale (non charts); 0042 catalogo offline (non Vault); 0022 localizzazione (non Unified Capture); 0063 focus calendar (non notifiche interattive). La mappatura corretta è nel dossier di sezione 12.

RevenueCat [State of Subscription Apps 2026](https://www.revenuecat.com/state-of-subscription-apps) dà benchmark aggregati, NON prova che Paired/Between/Locket convertano più di altre categorie o che Anna avrà tali tassi. [Android widget](https://developer.android.com/develop/ui/views/appwidgets/advanced) aggiorna periodicamente non sotto 30 minuti con updatePeriodMillis; [WidgetKit](https://developer.apple.com/documentation/widgetkit/keeping-a-widget-up-to-date) ha budget OS. [Google Play](https://support.google.com/googleplay/android-developer/answer/18265346) e [Apple](https://developer.apple.com/app-store/review/guidelines/) richiedono per abbonamenti valore continuativo, trasparenza e restore.

## Prossime decisioni, senza avvio sviluppo

Validare con 8–12 coppie come esplorazione qualitativa rituale Noi, lettera futura e widget Oggi; metriche future D7/D30, pairing/active duo, uso feature, trial->paid e costi cloud, non KPI già osservati. Preservare Privacy #215 Draft ON HOLD e le 70+70 baseline visive non ancora approvate. Le 17 sigle AD-NL26 sono ID editoriali **non CAP nuovi**; creare CAP canonici soltanto dopo dedup, approvazione, aggiornamento JSON e rigenerazione di tutte le viste.
