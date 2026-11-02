# Anna's Diary / NotebookLM — 15 idee -> capability canoniche

**Registrazione 02/11/2026.** Factory baseline `cf931f8031ca973cb0a5467a8e83c865cd1e9def`, Anna source osservata `827bb61620960d8867eb03e453d142013aada786`. Le priorità idee restano 4 P1 e 11 P2, separate dal ranking CAP ufficiale. Nessun codice Anna, billing o Privacy #215 modificati.

## Matrice formale, senza duplicati

| ID idea | Decisione | CAP canonica | Ambito distinto | Priorità idea |
|---|---|---|---|---|
| AD-NL26-01 | **NUOVA** | CAP-0141 | Rituale con due risposte | P1 |
| AD-NL26-02 | **NUOVA** | CAP-0142 | Capsula coppia (stesso contratto lettera) | P1 |
| AD-NL26-03 | **NUOVA** | CAP-0142 | Lettera personale (stesso time-release) | P1 |
| AD-NL26-04 | **NUOVA** | CAP-0143 | QR e ricordi con revoca | P2 |
| AD-NL26-05 | **NUOVA** | CAP-0144 | Countdown evento selezionato | P2 |
| AD-NL26-06 | **NUOVA** | CAP-0144 | Foto partner opt-in, variante bloccata | P2 |
| AD-NL26-07 | **NUOVA** | CAP-0145 | Heatmap diario/abitudini descrittive | P2 |
| AD-NL26-09 | **NUOVA** | CAP-0146 | PDF in Vault cifrato, threat model | P2 |
| AD-NL26-11 | **NUOVA** | CAP-0144 | Widget Oggi + Crea | P1 |
| AD-NL26-12 | **ESTENDI** | CAP-0055 | Action notifiche, non nuovo scheduler | P2 |
| AD-NL26-13 | **ESTENDI** | CAP-0024 | Haptics nelle microinterazioni, opzionali | P2 |
| AD-NL26-14 | **ESTENDI** | CAP-0023 | Preset tema Dark Velvet, stesso engine | P2 |
| AD-NL26-15 | **PRESERVA** | CAP-0023 / CAP-0069 | UI5 Manrope/Lora + QA visiva | P2 |
| AD-NL26-16 | **NUOVA** | CAP-0147 | Riordino card e preferenze Home | P2 |
| AD-NL26-17 | **ESTENDI** | CAP-0072 | Entitlement e pricing da validare, non nuovi SKU | P2 |

**Risultato:** 7 CAP aggiunte (`CAP-0141…CAP-0147`) per 10 idee; 5 idee collegate a CAP esistenti (`CAP-0023/0024/0055/0069/0072`). Un ID di idea può fare riferimento a una CAP già condivisa con più varianti.

## Scoring e stati

| Nuova CAP | Score canonico | Classe CAP | App base (stato) | Gate principale |
|---|---:|---|---|---|
| [CAP-0141](REGISTRO_CAPABILITY/CAP-0141.md) | 79/100 | P2 | Agenda-per-Anna: PROPOSTA | Non approvata in roadmap. Prima validare con due account/device, disclosure in cache/push/feed, revoca e privacy #215 ON HOLD; nessuna E2EE implicita. |
| [CAP-0142](REGISTRO_CAPABILITY/CAP-0142.md) | 75/100 | P3 | Agenda-per-Anna: PROPOSTA | Nessuna garanzia crittografica del blocco temporale. QA date/fusi/offline/orologio, backup e sync due device; shared dopo Privacy #215. |
| [CAP-0143](REGISTRO_CAPABILITY/CAP-0143.md) | 62/100 | P3 | Agenda-per-Anna: PROPOSTA | Blocco disclosure pubblica: mai pubblicare contenuto privato automaticamente. Security review token/noindex/EXIF/URL leak/revoca, termini hosting e Privacy #215. |
| [CAP-0144](REGISTRO_CAPABILITY/CAP-0144.md) | 86/100 | P2 | Agenda-per-Anna: PROPOSTA | Android launcher e iOS WidgetKit diversi; no claim real-time. PIN/biometria e contenuti riservati su lockscreen richiedono QA fisico; Privacy #215 congelata. |
| [CAP-0145](REGISTRO_CAPABILITY/CAP-0145.md) | 81/100 | P2 | Agenda-per-Anna: PROPOSTA | No health/diagnostic claims, no dati ciclo/Vault in UI ordinaria, no esempi +40% spacciati per risultati; test missingness e permessi. |
| [CAP-0146](REGISTRO_CAPABILITY/CAP-0146.md) | 69/100 | P3 | Agenda-per-Anna: PROPOSTA | Security HIGH: plaintext temporanei/thumbnail/indici, backup/cloud, perdita chiavi, iOS/Web, memoria; Privacy #215 ON HOLD; no claim Keystore universale. |
| [CAP-0147](REGISTRO_CAPABILITY/CAP-0147.md) | 81/100 | P2 | Agenda-per-Anna: PROPOSTA | No secondo dashboard/data store; screenshot matrix su UI5, contrasto, semantica, performance, account switch e fallback small screen. |

**Attenzione alle due scale:** score idea NotebookLM U/D/V/M/F/S/R e score CAP `35% valore + 25% riuso + 20% fattibilità + 10% evidenza + 10% rischio basso` sono diversi. Una CAP tecnica P3 non reinserisce nessuna delle due idee P3 già scartate: indica solo bassa fattibilità/evidenza attuale per una delle quindici idee P1/P2 mantenute.

## Riuso / Golden

- CAP-0055: scheduler/diagnostica già catalogati; quick action come estensione candidata senza claim OEM/OS.
- CAP-0024: motion e microfeedback; haptic mirato senza nuova architettura.
- CAP-0023: temi tipografici/HSV; Dark Velvet e Manrope/Lora UI5 sono rifinitura non nuova CAP.
- CAP-0069: visual regression, 70+70 screenshot reali ancora da acquisire/approvare.
- CAP-0072: provider-agnostic entitlement e RevenueCat; prezzo Free/Premium/Lifetime resta test business non integrazione Store.
- Golden di riferimento: `GOLDEN_ENTITLEMENT_CONTRACT_FLUTTER_v1`, `GOLDEN_CAPABILITY_HARVEST_ASSEMBLY_v1_DRAFT`; **nessun nuovo Golden promosso**.

## Errori di riferimento della fonte esterna

NotebookLM assegnava nomi a codici già usati: CAP-0041 = palette foto, non E2EE; CAP-0052 = meteo outdoor, non Lockscreen Widget; CAP-0038 = PDF Pocket Tools, non Time Lock; CAP-0012 = Year in Review, non QR; CAP-0015 = ricerca globale, non Stats; CAP-0042 = catalogo editoriale, non Vault; CAP-0084 = toolbox conversioni, non Fake PIN; CAP-0022 = localizzazione, non cattura; CAP-0063 = focus, non notifiche. Questi codici canonici NON sono stati riutilizzati scorrettamente. Le due idee P3 scartate restano fuori dal registro.

## Authority e prossimi gate

La PR di questo archivio è **catalogazione soltanto**: non implica Product Bible, roadmap approvata o runtime. Privacy #215 rimane DRAFT/ON HOLD. Le 7 schede `ANNA_SOURCE_COMPATIBILITA.md` certificano solo la presenza di file storici, NON l'implementazione. I sette kit sono livello 1, senza codice donor copiato. Prima di uno sviluppo: approvazione del proprietario, audit source al nuovo SHA, scope, test e QA fisica appropriata.
