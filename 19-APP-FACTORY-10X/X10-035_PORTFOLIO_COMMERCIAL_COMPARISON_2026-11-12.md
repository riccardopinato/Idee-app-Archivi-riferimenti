# X10-035 — Confronto trasversale commerciale; tetto 100 €, nessuna spesa automatica

**Data rilevazione:** 12/11/2026. **Baseline Factory** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` (Master v27, Golden Index v29). **Stato:** confronto di decisione, NON approvazione prodotti, NON autorizzazione a pagare/pubblicare. [Proposta decisione in JSON](X10-035_OWNER_DECISION_PROPOSAL.json).

## Decisione owner: confermata soltanto la soglia economica

- **Budget massimo TOTALE** per gli esperimenti commerciali: **100 EUR**.
- **Nessuna spesa automatica autorizzata**: l'autorizzazione operativa di spesa è **0 EUR** e ogni pagamento richiede autorizzazione esplicita separata. Non dichiariamo la spesa effettivamente sostenuta esternamente, non osservabile.
- **Non selezionati ancora** i 2–3 prodotti: il proprietario ha chiesto questo confronto *prima* di confermare app, go/no-go, eventuali investimenti.
- `X10-035` resta `PLANNED` nel registro finché non sono scelti prodotti e budget e superati i gate. `X10-036` non è attivato nelle app, nessun billing, Play, ads o analytics SDK modificato.

## Metodo e limiti

L'archivio [classifica 37 voci 30/10](../01-PORTAFOGLIO/CLASSIFICA_2026-10-30.md) contiene SCORE **soggettivi/storici**, non ricavi. Questo confronto li **non** tratta come performance, rilegge le prove repository al 12/11 e incorpora [ricerca competitor X10-034](EVIDENCE_X10-034_MARKET_COMPETITORS_2026-11-12.md) oltre a comparatori pubblici. **MANCANTI:** impression/download Play propri, vendite, conversioni, retention misurate, volume keyword, costo supporto, valore organico e CAC. **Non** derivare forecast da download concorrenti.

Per ogni candidato si valutano: rapidità del test, estensione delle verifiche fisiche/provider ancora richieste, monetizzazione incrementale compatibile, domanda PROXY da competitor e sostenibilità di gestione. Valutazione qualitativa, non punteggio quantitativo né TAM.

## Graduatoria di priorità per test COMMERCIALI (NON ordine assoluto di valore delle app)

| Fascia | Prodotto / SHA principale consultato | Pro e readiness osservati | Rischio/perché non avanti | Verdetto proposto, non approvato |
| --- | --- | --- | --- | --- |
| 1 | [Rotate 180°](https://github.com/riccardopinato/180FlipCharge/tree/05bc1e2a13f37563ec1ee52874855a8b52d168b1) | v0.8.3, size budget, firma INTERNAL, modello upfront €4,99 no ads; proposta leggibile e demo economica | OEM, overlay/FGS/Usage, device + Play NO-GO; numerose alternative gratuite, prezzo non validato | **PILOTA RAPIDO DI PREZZO**, non prova di domanda |
| 1 | [Android Omni Cleaner](https://github.com/riccardopinato/Android-Omni-Cleaner/tree/984474d9af62d8b7e17b975a31332161f24f2df7) | v1.0 RC1, premium lifetime, demo ampia, README registra prima physical performance pass | Store signing/consenso/ads e affidabilità cleanup/permessi da verificare; Files by Google gratuito molto forte | **SFIDANTE PRINCIPALE**, shortlist da portare a scelta |
| 1 | [Battery Guard](https://github.com/riccardopinato/Battery_Guard/tree/1343f09d21ace8adf3976b3fd347183f38e5ab68) | Flutter v1.8.1+27, Free + Pro lifetime, INTERNAL firmato, prodotto maturo a livello source | backend trusted purchaseToken/refund NON implementato; Samsung+Redmi device, OEM behavior, AdMob/Play; AccuBattery competitor affermato | **SFIDANTE PRINCIPALE**, valore/retention da verificare |
| 2 | [Send to PC](https://github.com/riccardopinato/Send-to-pc/tree/723a13dfc144669589e0a9127d3577433a61677e) | Kotlin, signed Store Candidate v1.27 riportato in RELEASE, utile QR LAN browser senza install PC | LocalSend già gratuito/cross-platform e Google Quick Share; TLS self-signed warning, test cross-device; valore ads modesto per azioni sporadiche | **RISERVA**, tester qualitativi gratuiti |
| 2 | [Phone Guard](https://github.com/riccardopinato/Phone-Guard/tree/0586b41ef439b4ac20a834ac74c9c3d8186fa82a) | v0.9.7 6 modalità, privacy locale, valore immediato | false positive, sensori/Doze/FGS, 3 OEM & affidabilità critica; nessuna monetizzazione attiva nel README | **RISERVA** device/prodotto |
| 2 | [PDF-Unifier](https://github.com/riccardopinato/PDF-Unifier/tree/03acc73ad8122a8aac4ee1c728f9875791bb4c49) | base Android in codice, categoria user-task chiara | README non certifica attuale breadth o release; build.gradle mostra versionCode 1; PDFgear gratuito ricco | **RICERCA**, prima audit source/release |
| 2 | [FocuSense](https://github.com/riccardopinato/FocuSense/tree/99cce9e78963238854e3bbf4fb9c3f6e5e79d6ed) | RC1, focus+ambiente, one-time Pro | sensori/real device + billing/ad consent; Forest/Focus To-Do molto affermati | **RISERVA** |
| 3 | [World Days](https://github.com/riccardopinato/World-Days/tree/36f9ba28d621d374679132fd9cf93b4d012e1399) | 1.111 ricorrenze in catalogo, pipeline fonti/storie per retention e social | README segnala 218 origini IT/EN researched **dopo merge** di 155 storie registrate: 893 mancanti; human review multi-lingua e Store/ads non attestati; Dayfeed competitor | **SVILUPPO ORGANICO EDITORIALE**, non pilot paid ads immediato |
| 3 | [TasteAI](https://github.com/riccardopinato/TasteAI/tree/8e880be68d74686c6c6b7e6a992a5fdc6fa6c384) | 111 ricette offline, Anti-Waste/Plus in sorgente | store sandbox/entitlement e distribuzione, mercato ricette ampio | **RIMANDARE** commerciale |
| 3 | [Cooking Anime](https://github.com/riccardopinato/In-Cucina-con-gli-Anime/tree/fb4c8cf5d7b0e8de0ada7649a1ef8b7e981ed465) | concept condivisibile e catalogo editoriale; 20 ricette con artwork audited secondo README | diritti, 6 lingue, catalogo completo, monetizzazione e asset/copyright; non inferire ready dalla Play Console | **RIMANDARE** fino editorial/compliance |
| 3 | [Notification Control](https://github.com/riccardopinato/Notification-Control/tree/3a38648f730fff591a85e48b5f4757073adc4663) | suite 6 moduli molto evoluta e Premium | NotificationListener/private data, billing ricorrente e Play/OEM più complessi, real device non attestato | **RIMANDARE** primo esperimento |
| 3 | [Notes-Ecosistema](https://github.com/riccardopinato/Notes-Ecosistema/tree/22892b336e4587dc2daa1e8df970b873e72e41d7) / [Anna's Diary](https://github.com/riccardopinato/Agenda-per-Anna/tree/6004677f6e1a4e04abe4147a3a706a8a35a7a94b) | app mature come progetti, differenziazione di UX/privacy | sicurezza e recovery multi-device, polish, prezzo non validato; Anna è prodotto personale con confini sensibili | **CORSIA PRODOTTO/QUALITÀ**, non commercial-first |
| 3 | [CamperBoss](https://github.com/riccardopinato/CamperBoss/tree/fe3b10d435e120cc952a90cd6bc06c66b6b2521a) / [TrailPath](https://github.com/riccardopinato/TrailPath/tree/74a5cf87d0be55900d9be318af53972643eebd32) / [Wonderlog](https://github.com/riccardopinato/Wonderlog/tree/85a6fbcc914224b6753d9e405cc8fbc2e4d40cc6) | viaggi/outdoor e possibile monetizzazione futura | maggiore surface QA GPS/routing/offline/sync; CamperBoss roadmap STEP16 bloccata | **POSTICIPARE** test con 100€ |
| Alternativa strategica | [WEB-012 Sun & Moon](../03-WEB-UTILITY/CLASSIFICA.md) | Web locale SSR SEO, potenziale costo operativo basso senza API commerciali | IDEA senza consumer implementato né traffico/monetizzazione misurata; SEO non immediato e forte concorrenza | **PROTOTIPO ORGANICO ZERO-ADS**, separato dal Play pilot |

## Trade-off commerciale e differenze rispetto alla prima shortlist

- **Rotate** conserva la precedenza per **velocità di falsificazione**, non per mercato maggiore. €4,99 è il prezzo già in README, non disponibilità a pagare. [Rotation Control](https://play.google.com/store/apps/details?id=org.crape.rotationcontrol) presenta 10M+ installazioni da Google Play e include reverse portrait, quindi serve testare una ragione specifica per pagare.
- **Android Omni Cleaner** entra come sfidante **al posto di World Days nella coorte di test a breve**: physical performance primaria già riportata nel README, Pro one-time e ampia base funzionale; ma [Files by Google](https://play.google.com/store/apps/details?id=com.google.android.apps.nbu.files) è gratis e copre duplicate cleanup e altre funzioni, quindi non assumere capacità di acquisizione pagante.
- **Battery Guard** è ottimo test Free→Pro lifetime; [AccuBattery](https://play.google.com/store/apps/details?id=com.digibites.accubattery) è competitor molto strutturato, e trusted Google Billing/Refund esterno non è completato.
- **Send-to-PC** tecnicamente interessante ma [LocalSend](https://localsend.org/) è 100% free, local network, cross-platform, no ads. Per venderlo occorre mostrare un vantaggio effettivo oltre la comodità di browser/QR senza client PC.
- **PDF-Unifier** potenzialmente monetizzabile ma [PDFgear](https://play.google.com/store/apps/details?id=com.pdfeditor.pdfeditorandriod) fornisce molte operazioni gratis e il repository non ha lo stesso release-evidence livello degli altri.
- **World Days** può essere rilevante per crescita organica e cross-promo a tempo, ma la qualità editoriale è un investimento di lavoro *non* riducibile a 100€ in ads; le storie researched non sono automaticamente human-reviewed o pubblicate.
- **FocusSense** incontra alternative mature come [Forest](https://play.google.com/store/apps/details?id=cc.forestapp) e [Focus To-Do](https://play.google.com/store/apps/details?id=com.superelement.pomodoro).

## Piano di verifica entro il plafond, senza spesa automatica

**Fase A (€0):** test di installabilità e QA device, confronto screenshot/feature gap e 2 value propositions per candidate, landing/eventuali contenuti organici, raccolta di feedback volontari senza SDK nuovi. Qualunque test fisico può consumare tempo e dispositivi propri, ma NON implica spesa monetaria autorizzata.

**Fase B (da autorizzare per ogni singola voce, MAX totale €100):** dopo almeno un'app con release gate pronto, eseguire uno/due piccoli test di creatività / distribuzione solo se metriche e tracking/consenso pertinenti sono disponibili e l'owner approva voce per voce. Nessun importo allocato o impegnato ora.

## Decisione richiesta per chiudere X10-035

Proposta **non approvata** da confermare separatamente: **Rotate 180° (MVP prezzo), Android Omni Cleaner (lifetime e utilità ampia), Battery Guard (Free→Pro lifetime)**. **World Days** entra nella corsia editoriale organica e diventa sostituta soltanto dopo ulteriore certificazione di fonte, qualità e retention. Una scelta della prima coorte non autorizza deploy, Play, SDK, annunci, campagne, prezzo né altre spese.

L'ordinamento è un'euristica di velocità/risorsa disponibile, **non una previsione di ricavi**. L'analisi del 30/10 è storica; i repository qui sono source snapshots puntuali del 12/11 e non prove Store, ricavo o domanda reale.
