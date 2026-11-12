# X10-034 — Ricerca domanda, competitor e canali organici per la shortlist 10x

**Data consultazione:** 12 novembre 2026. **Factory baseline:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`. **Precondizione:** [X10-002 shortlist SOURCE](EVIDENCE_X10-002_COMMERCIAL_SHORTLIST_2026-11-12.md). **Metodo:** pagine prodotto pubbliche di Google Play e sito ufficiale concorrente; dati pubblicati **dai rispettivi provider**, non dati proprietari della nostra Play Console. Il campione è esplorativo, non censuario: ranking delle query, volumi keyword e prezzi effettivi per paese possono variare.

## 1. Battery Guard — domanda plausibile, concorrenza affollata

| Evidenza pubblica | Implicazione verificabile | Limite |
|---|---|---|
| [AccuBattery](https://play.google.com/store/apps/details?id=com.digibites.accubattery): Google Play indica 10M+ installazioni, ~603K recensioni, ads/IAP, allarme ricarica e salute/capacità batteria | Forte alternativa di larga scala; soglia di differenziazione alta | Installazioni storiche altrui **non** predicono conversioni alla nostra app |
| [Battery Guru](https://play.google.com/store/apps/details?id=com.paget96.batteryguru): allarmi di carica/scarica, temperatura, sessioni, UI e funzioni Pro | Le funzioni base e avanzate sono già offerte nel mercato | Nessun dato validato sulla nostra willingness-to-pay o qualità OEM |
| [Battery Full Charge Alarm](https://play.google.com/store/apps/details?id=com.battery.fullchargealarm): Google Play indica 1M+ installazioni, ads/IAP e allarmi di carica/scarica | C'è pubblico per utility semplici con alert personalizzabili | Recensioni riportano anche interruzioni: casi aneddotici, non prevalenza misurata |
| [Full Battery Charge Alarm / Syrupy](https://play.google.com/store/apps/details?id=apps.syrupy.fullbatterychargealarm): avverte delle restrizioni di Xiaomi/Huawei/OnePlus | L'affidabilità con gli OEM è un problema competitivo verificabile da test reali | Non dimostra che Battery Guard lo risolva meglio |

**Ipotesi differenziante da testare:** semplice affidabilità di alert su Xiaomi/Redmi e Samsung, privacy/assenza sorprese, spiegazioni trasparenti dei dati, **Pro lifetime** con valore dimostrabile. Il rischio centrale è l'equivalenza funzionale con strumenti gratuiti e pagamenti già presenti altrove. **Canali organici candidati:** video dimostrativi di soglie/alert, keyword long-tail italiane/inglesi Play, guida troubleshooting per OEM, comparativa pubblica con limiti Android descritti onestamente.

## 2. Rotate 180° — nicchia dimostrabile, disponibilità a pagare incerta

| Evidenza pubblica | Implicazione verificabile | Limite |
|---|---|---|
| [Rotation Control / CrapeMyrtle](https://play.google.com/store/apps/details?id=org.crape.rotationcontrol): Google Play indica 10M+ installazioni, reverse portrait, notifiche | La rotazione inversa è già una funzione offerta da competitor popolari | Grande base installata non implica che il nostro prodotto possa sostenere €4,99 |
| [Rotation Control / CloudEx](https://play.google.com/store/apps/details?id=jp.snowlife01.android.rotationcontrol): Google Play indica 1M+ installazioni, **2 giorni di prova gratuita poi singolo acquisto permanente**, Quick Settings, profili per app e condizioni | Esiste un benchmark pubblico di monetizzazione una tantum, più ricco del semplice switch 180° | Il prezzo non è stato verificato per l'Italia e nessuna conversione è pubblica |
| [Rotation Control / plus infotech](https://play.google.com/store/apps/details?id=com.plus.rotationcontrol): Google Play indica 500K+ download, annunci/IAP e reverse portrait | Alternativa freemium già presente con modalità avanzate | Su alcuni dispositivi le modalità forzate non funzionano o deformano le app |
| [Screen Orientation Control](https://play.google.com/store/apps/details?id=net.mm2d.android.orientationfaker): 14 orientamenti, limitazioni Android 16+ grandi schermi, overlay e ottimizzazione batteria | La compatibilità tecnica/OEM deve essere spiegata prima dell'acquisto | Le limitazioni variano per device e targetSdk |

**Ipotesi da falsificare:** un gesto/Quick Settings tile estremamente veloce per invertire il telefono in carica o sul supporto può giustificare un prezzo upfront solo se supera in usabilità le alternative gratuite. Il `€4,99` della Product Bible è un'**ipotesi**, non un prezzo market-cleared. **Canali:** clip brevi con confronto prima/dopo, community Android/accessibilità/dock e scheda Play focalizzata su reverse-portrait; test fisici sulle versioni Android e OEM realmente supportate, senza promessa “funziona sempre”.

## 3. World Days — opportunità editoriale, concorrente diretto già articolato

| Evidenza pubblica | Implicazione verificabile | Limite |
|---|---|---|
| [Dayfeed](https://www.dayfeed.app/it/): il sito ufficiale **dichiara** 1.600+ giornate in 17 lingue, fonti, widget, promemoria, poster personalizzabili e Free+Pro | Forte sovrapposizione con contenuti, social sharing e monetizzazione; non bastano catalogo o poster come differenziazione | Numeri dichiarati dal provider, non audit indipendente di qualità/coverage |
| [DayVerse](https://play.google.com/store/apps/details?id=com.dayverse.app): descrive 195+ paesi, calendario culturale e awareness, approfondimenti, preferiti/notifiche, senza abbonamento | Offerta ampia gratuita, quindi premium basato solo sul catalogo fragile | Dati per l'app concorrente non garantiscono ricavo/retention nostra |
| [Today: International Days 2026](https://play.google.com/store/apps/details?id=net.smartlogic.three65days): contenuti su ricorrenze/giorni nazionali, storia, promemoria e filtri | Alcuni bisogni di learning e reminder sono già coperti | Nessuna misurazione di ritorno giornaliero disponibile |
| [World Days / SZIS](https://play.google.com/store/apps/details?id=com.szis.vilagnap): elenco descrittivo/search/TTS; [WhatDay](https://play.google.com/store/apps/details?id=com.ozekstudio.whatday): mini-task e mood | Segmenti alternativi: archivio, lettura, micro-azioni quotidiane | Non confondere presenza concorrenza con dimostrazione di audience raggiungibile |

**Baseline PROPRIA** al commit [World-Days@d84976e](https://github.com/riccardopinato/World-Days/commit/d84976e1f9f210a4748fa193feae169e78de625f): 1.111 ricorrenze in catalogo, 46 origini singolarmente ricercate IT/EN e 1.065 nel backlog di quel momento; un job incrementale può aver modificato il main dopo la snapshot. Il prodotto dovrà differenziarsi tramite qualità attribuita delle fonti, spiegazioni editoriali ricche, accuratezza delle date mobili e utilità senza pubblicità invasive. Non promettere “la più completa” senza audit delle fonti rispetto a Dayfeed.

**Canali organici candidati:** Pinterest/Instagram contenuti giornalieri citati, SEO long-tail `giornata mondiale + data + storia`, condivisione di card senza attribuzione falsa; link alle fonti ufficiali ONU/UNESCO/OMS/FAO verificati singolarmente. Evitare materiale grafico e testi di terzi senza licenza.

## 4. Evidenza di domanda vs osservazioni mancanti

**Segnali verificabili oggi:** concorrenti reali, funzioni ricorrenti, modelli Free/ads/IAP/lifetime esposti nelle schede, alcune installazioni Play aggregate e presenza di pagine/editori. **Non disponibili/NOT_MEASURED:** volume query per paese/lingua, impressioni Play, tasso clic/install, retention D1/D7/D30, conversione Pro, revenue, eCPM netto, costi di acquisizione, margine supporto, recensioni rappresentative, valore lifetime rispetto agli OEM. Le installazioni concorrenti sono soglie cumulative dichiarate da Play, **non** domanda incrementale nostra. Non stimare TAM o ricavi da conteggi Play.

## 5. Esperimenti ordinati a costo minimo prima di X10-035

1. **Verifica di proposta:** 2 varianti di store copy/screenshot per utility, landing/campagna organica per Word Days; traccia solo click/impressioni attribuibili quando realmente disponibili. Nessuna spesa pubblicitaria senza budget approvato.
2. **Qualità di prodotto prima dell'acquisizione:** Battery Guard prova OEM, alert/restore/consent/billing server; Rotate prova reverse portrait su target OS/OEM, tile, gestione blocchi; World Days audit di lotti editoriali e revisione indipendente delle fonti/traduzioni. NON release-ready finché i rispettivi release gate non passano.
3. **Metriche da strumentare con consenso:** visite allo store, conversioni install, first useful action, D1/D7, crash/ANR e richiesta Pro; per World Days frequenza apertura/salvataggio/condivisione e contenuti effettivamente letti. Registrare `NOT_MEASURED` prima del dato reale, anonimizzare e rispettare privacy/consenso.
4. **Scelta umana X10-035:** confrontare le evidenze effettive dei tre piloti (e dell'alternativa Cooking Anime se necessario); concordare budget, target e soglie **prima** di autorizzare esperimenti a pagamento, SDK aggiuntivi, billing in produzione o store.

**Stato del dossier:** `PUBLIC_COMPETITOR_RESEARCH` con fonti datate. Può soddisfare lo scope **READ_ONLY** di raccolta X10-034 dopo PR/CI/review, **non** è `BUSINESS_MEASURED`, domanda pagante verificata o approvazione del gate umano X10-035. **Conclusione provvisoria:** non esiste ancora evidenza sufficiente per preferire finanziariamente uno dei tre; Rotate è il test di proposta più semplice, Battery ha il problema d'affidabilità più chiaro ma mercato affollato, World Days richiede una strategia contenuti più costosa per competere con Dayfeed.
