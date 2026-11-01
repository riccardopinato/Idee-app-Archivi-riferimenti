# Hugging Face «to do» — seconda ricerca: idee 13–28 per Notes-Ecosistema

- **Data:** 2026-11-01
- **Ricerca principale:** https://huggingface.co/search/full-text?q=to+do
- **Relazione con ricerca precedente:** [idee 1–12](RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md), mantenute intatte.
- **Classificazione:** `PROPOSTA` di prodotto, **non** implementazione, non Product Bible/roadmap approvata.
- **Factory baseline di riferimento:** `riccardopinato/App-Factory-Core@632a66dce4aa00e8e1700b0a3e4dfc7ea008197c` (Master v27).
- **Limite della ricerca:** il listing dinamico full-text non era enumerabile completamente. Le fonti esaminate sotto sono selezioni accessibili e verificabili; non sono 16 app Hugging Face installabili. Dove un abbinamento non e diretto, si dichiara esplicitamente `IDEA DERIVATA`.
- **Punteggi 8,5–9,9/10:** valutazioni editoriali gia condivise in Chat, non benchmark, metriche di business o score CAP del registro.

## Tutte le 16 idee, senza duplicazione CAP

| # | Idea | Descrizione proposta | Fit | Valore /10 | CAP collegati |
|---|---|---|---|---|---|
| 13 | **Smart Rescheduler** | Se salta un impegno, proporre di ricollocare task flessibili rispettando eventi fissi, disponibilita e scadenze; scelta esplicita dell'utente. | Notes-Ecosistema; Anna's Diary essenziale | 9,9 | CAP-0102, CAP-0001 |
| 14 | **Dependency Map** | Grafo dei prerequisiti e task bloccate, con indicazione della dipendenza che impedisce di partire. | Notes-Ecosistema | 9,8 | CAP-0103, CAP-0096, CAP-0028 |
| 15 | **Goal Timeline** | Obiettivi a 1/3 anni divisi in fasi e milestone modificabili su timeline e canvas. | Notes-Ecosistema | 9,7 | CAP-0104, CAP-0099 |
| 16 | **Smart Priority Engine** | Ranking trasparente e modificabile per urgenza, importanza, tempo stimato e vincoli, senza decisioni implicite. | Notes-Ecosistema; Anna's Diary essenziale | 9,6 | CAP-0105 |
| 17 | **Workload Guard** | Rilevare giorni o settimane con sovraccarico sulla base di eventi e ore-task, senza spostare gli impegni. | Notes-Ecosistema; Anna's Diary essenziale | 9,6 | CAP-0106, CAP-0001 |
| 18 | **Project Blueprint Import** | Importare Markdown/README di progetto e ottenere una bozza di fasi, attivita, stime e note collegate. | Notes-Ecosistema | 9,5 | CAP-0107, CAP-0093, CAP-0075 |
| 19 | **Backward Planning** | Impostare una deadline finale e costruire a ritroso milestone e attivita, mantenendo date modificabili. | Notes-Ecosistema | 9,5 | CAP-0104, CAP-0001 |
| 20 | **Task Time Accuracy** | Stimato vs effettivo per task, con suggerimenti futuri fondati su storia locale e nessuna telemetria remota. | Notes-Ecosistema | 9,4 | CAP-0108, CAP-0101 |
| 21 | **Focus Notes** | Timer Pomodoro collegato alla nota o task attiva, con sessioni, pause e minuti focus locali. | Notes-Ecosistema; potenziale riuso FocuSense | 9,3 | CAP-0109 |
| 22 | **Eisenhower Visual Board** | Vista a quattro quadranti importante/urgente applicata alle task canoniche, con drag e modifica manuale. | Notes-Ecosistema | 9,2 | CAP-0105, CAP-0094 |
| 23 | **Quick Start Mode** | Scomporre volontariamente una task complessa in un primo micro-passo e avviare una breve sessione guidata. | Notes-Ecosistema | 9,1 | CAP-0110, CAP-0109 |
| 24 | **Weekly Review** | Revisione periodica di task incompiute, impegni e priorita con proposte di azione confermabili. | Notes-Ecosistema; Anna's Diary essenziale | 9,0 | CAP-0111, CAP-0101 |
| 25 | **Learning Recall** | Generare o costruire flashcard collegate a note di studio e pianificare ripassi distanziati. | Notes-Ecosistema | 8,9 | CAP-0112, CAP-0099 |
| 26 | **Alternative Plans** | Mostrare due piani possibili per la giornata con conflitti e tempo libero, prima che l'utente ne applichi uno. | Notes-Ecosistema; Anna's Diary essenziale | 8,8 | CAP-0102, CAP-0001 |
| 27 | **Focus Protection** | Durante il timer Focus proporre controlli OS disponibili per notifiche e distrazioni, senza permessi invasivi. | Notes-Ecosistema; potenziale riuso FocuSense | 8,6 | CAP-0109, CAP-0077 |
| 28 | **Meeting Load Heatmap** | Heatmap delle ore di riunione e dei picchi settimanali con fonte e conteggi trasparenti. | Notes-Ecosistema; Anna's Diary se compatibile con calendario | 8,5 | CAP-0106, CAP-0101 |

## Tracciabilita: cosa mostrano davvero le fonti

### 13. Smart Rescheduler

- **Proposta:** Se salta un impegno, proporre di ricollocare task flessibili rispettando eventi fissi, disponibilita e scadenze; scelta esplicita dell'utente.
- **Evidenza vs proposta:** Fonte diretta: Plan My Day considera interruzioni, preferenze e correzioni; nostra proposta: integrazione nelle entita Notes.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/burtenshaw/plan-my-day-results).
- **Relazioni canoniche:** CAP-0102, CAP-0001; stato `PROPOSTA`, non confermata nel codice della app.

### 14. Dependency Map

- **Proposta:** Grafo dei prerequisiti e task bloccate, con indicazione della dipendenza che impedisce di partire.
- **Evidenza vs proposta:** Fonte diretta: Yuga dichiara dipendenze sequenziali; nostra proposta: visualizzazione interattiva e blocker espliciti.
- **Riferimenti:** [fonte 1](https://huggingface.co/spaces/Agents-MCP-Hackathon/yuga-planner/blob/main/README.md).
- **Relazioni canoniche:** CAP-0103, CAP-0096, CAP-0028; stato `PROPOSTA`, non confermata nel codice della app.

### 15. Goal Timeline

- **Proposta:** Obiettivi a 1/3 anni divisi in fasi e milestone modificabili su timeline e canvas.
- **Evidenza vs proposta:** Fonte diretta: MiniAppBench #21 descrive timeline drag-and-drop per obiettivi pluriennali; e una specifica di benchmark, non una app pronta.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset).
- **Relazioni canoniche:** CAP-0104, CAP-0099; stato `PROPOSTA`, non confermata nel codice della app.

### 16. Smart Priority Engine

- **Proposta:** Ranking trasparente e modificabile per urgenza, importanza, tempo stimato e vincoli, senza decisioni implicite.
- **Evidenza vs proposta:** Derivazione proposta: Plan My Day gestisce preferenze e vincoli ma non certifica questo specifico motore di scoring.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/burtenshaw/plan-my-day-results).
- **Relazioni canoniche:** CAP-0105; stato `PROPOSTA`, non confermata nel codice della app.

### 17. Workload Guard

- **Proposta:** Rilevare giorni o settimane con sovraccarico sulla base di eventi e ore-task, senza spostare gli impegni.
- **Evidenza vs proposta:** Fonti dirette: disponibilita e vincoli in Yuga; MiniAppBench #27 ha heatmap riunioni. Soglie overload per Notes sono una proposta.
- **Riferimenti:** [fonte 1](https://huggingface.co/spaces/Agents-MCP-Hackathon/yuga-planner/blob/main/README.md) · [fonte 2](https://huggingface.co/datasets/MiniAppBench/Dataset).
- **Relazioni canoniche:** CAP-0106, CAP-0001; stato `PROPOSTA`, non confermata nel codice della app.

### 18. Project Blueprint Import

- **Proposta:** Importare Markdown/README di progetto e ottenere una bozza di fasi, attivita, stime e note collegate.
- **Evidenza vs proposta:** Fonte diretta: Yuga fa parsing di file Markdown e composizione task tramite LLM e Nebius; implementazione Flutter locale non presente nel donor.
- **Riferimenti:** [fonte 1](https://huggingface.co/spaces/Agents-MCP-Hackathon/yuga-planner/blob/main/README.md).
- **Relazioni canoniche:** CAP-0107, CAP-0093, CAP-0075; stato `PROPOSTA`, non confermata nel codice della app.

### 19. Backward Planning

- **Proposta:** Impostare una deadline finale e costruire a ritroso milestone e attivita, mantenendo date modificabili.
- **Evidenza vs proposta:** Estensione di Goal Timeline: backward scheduling non risulta provato dal benchmark; pattern progettuale proposto.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset).
- **Relazioni canoniche:** CAP-0104, CAP-0001; stato `PROPOSTA`, non confermata nel codice della app.

### 20. Task Time Accuracy

- **Proposta:** Stimato vs effettivo per task, con suggerimenti futuri fondati su storia locale e nessuna telemetria remota.
- **Evidenza vs proposta:** Spunto generale da metriche di pianificazione del dataset sperimentale; misurazione personali durate e una proposta aggiuntiva.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/burtenshaw/plan-my-day-results).
- **Relazioni canoniche:** CAP-0108, CAP-0101; stato `PROPOSTA`, non confermata nel codice della app.

### 21. Focus Notes

- **Proposta:** Timer Pomodoro collegato alla nota o task attiva, con sessioni, pause e minuti focus locali.
- **Evidenza vs proposta:** Fonte diretta: MiniAppBench #20 definisce timer Pomodoro + task, contatori e statistiche; benchmark, non codice Flutter disponibile.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset/blob/main/query_validation_100.json).
- **Relazioni canoniche:** CAP-0109; stato `PROPOSTA`, non confermata nel codice della app.

### 22. Eisenhower Visual Board

- **Proposta:** Vista a quattro quadranti importante/urgente applicata alle task canoniche, con drag e modifica manuale.
- **Evidenza vs proposta:** Concept autonomo della seconda ricerca; MiniAppBench e solo riferimento generale alla famiglia di tool di produttivita, non conferma della vista Eisenhower.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset).
- **Relazioni canoniche:** CAP-0105, CAP-0094; stato `PROPOSTA`, non confermata nel codice della app.

### 23. Quick Start Mode

- **Proposta:** Scomporre volontariamente una task complessa in un primo micro-passo e avviare una breve sessione guidata.
- **Evidenza vs proposta:** Idea di prodotto originale combinando task/Pomodoro; il benchmark #20 non descrive micro-passi motivazionali.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset/blob/main/query_validation_100.json).
- **Relazioni canoniche:** CAP-0110, CAP-0109; stato `PROPOSTA`, non confermata nel codice della app.

### 24. Weekly Review

- **Proposta:** Revisione periodica di task incompiute, impegni e priorita con proposte di azione confermabili.
- **Evidenza vs proposta:** Adattamento del benchmark MiniAppBench #24 (check-in trimestrali/mensili su obiettivi); la revisione settimanale con task e una proposta.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset).
- **Relazioni canoniche:** CAP-0111, CAP-0101; stato `PROPOSTA`, non confermata nel codice della app.

### 25. Learning Recall

- **Proposta:** Generare o costruire flashcard collegate a note di studio e pianificare ripassi distanziati.
- **Evidenza vs proposta:** Fonte: release notes HermesAgent indicano memento-flashcards come skill di ripetizione dilazionata; nessuna compatibilita Flutter attestata.
- **Riferimenti:** [fonte 1](https://huggingface.co/spaces/abc1181/HermesAgent/blob/main/RELEASE_v0.6.0.md).
- **Relazioni canoniche:** CAP-0112, CAP-0099; stato `PROPOSTA`, non confermata nel codice della app.

### 26. Alternative Plans

- **Proposta:** Mostrare due piani possibili per la giornata con conflitti e tempo libero, prima che l'utente ne applichi uno.
- **Evidenza vs proposta:** Derivazione da pianificazione con correzioni di Plan My Day; confronto duale non descritto come feature provata.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/burtenshaw/plan-my-day-results).
- **Relazioni canoniche:** CAP-0102, CAP-0001; stato `PROPOSTA`, non confermata nel codice della app.

### 27. Focus Protection

- **Proposta:** Durante il timer Focus proporre controlli OS disponibili per notifiche e distrazioni, senza permessi invasivi.
- **Evidenza vs proposta:** Estensione concettuale del timer: il benchmark non documenta blocchi di siti o permessi Android. Richiede policy device-specific e consenso.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset/blob/main/query_validation_100.json).
- **Relazioni canoniche:** CAP-0109, CAP-0077; stato `PROPOSTA`, non confermata nel codice della app.

### 28. Meeting Load Heatmap

- **Proposta:** Heatmap delle ore di riunione e dei picchi settimanali con fonte e conteggi trasparenti.
- **Evidenza vs proposta:** Fonte diretta: MiniAppBench #27 descrive tool di durata riunioni e heatmap su dati di esempio, non un'integrazione live.
- **Riferimenti:** [fonte 1](https://huggingface.co/datasets/MiniAppBench/Dataset).
- **Relazioni canoniche:** CAP-0106, CAP-0101; stato `PROPOSTA`, non confermata nel codice della app.


## Fonti di riferimento e limiti verificati

1. **[Yuga Planner](https://huggingface.co/spaces/Agents-MCP-Hackathon/yuga-planner/blob/main/README.md)** (Space Apache-2.0): analizza documenti Markdown e README, compone task/stime e pianifica assegnazioni usando LlamaIndex, Nebius AI e Timefold. Dipendenze di progetto e disponibilita risorse sono nel README; la mappa grafica degli ostacoli e una **nostra** proposta. Nebius/Timefold e dipendenze esterne richiedono audit separato (licenze, quota, account e uso commerciale); Apache-2.0 dello Space **non** autorizza automaticamente ogni componente.
2. **[Plan My Day](https://huggingface.co/datasets/burtenshaw/plan-my-day-results)** (dataset Apache-2.0): esperimento di pianificazione giornaliera con vincoli, preferenze, evento imprevisto e correzioni; include un planner a regole e confronto sintetico fra modelli. Non dimostra efficacia su utenti reali, non addestra live dai dati del calendario e non e un motore di agenda Flutter pronto. I pesi LiquidAI hanno licenza propria, distinta dal codice/dataset. `Alternative Plans`, `Task Time Accuracy` e priorita transparenti sono estrapolazioni.
3. **[MiniAppBench Dataset](https://huggingface.co/datasets/MiniAppBench/Dataset)** (benchmark di *specifiche*, non app complete): #20 Pomodoro+task; #21 timeline obiettivi; #24 check-in trimestrali/mensili; #27 heatmap carico riunioni. Documento puntuale: [query_validation_100.json](https://huggingface.co/datasets/MiniAppBench/Dataset/blob/main/query_validation_100.json). Le funzioni proposte per Notes sono un design originale. Licenza e condizioni del dataset da verificare prima di incorporare righe/testi in prodotti commerciali.
4. **[HermesAgent release notes](https://huggingface.co/spaces/abc1181/HermesAgent/blob/main/RELEASE_v0.6.0.md)**: include la skill `memento-flashcards` per spaced repetition; reference progettuale, non modulo Flutter validato. Licenza per singola skill, eventuali dipendenze e compatibilita da verificare.

## Scelta architetturale: 16 idee, 11 nuovi CAP

- **Nuovi ID:** CAP-0102…CAP-0112 (11 responsabilita distinte).
- **Riuso senza nuova capability:** Backward Planning → CAP-0104; Eisenhower Visual Board → CAP-0105 + CAP-0094; Alternative Plans → CAP-0102; Focus Protection → CAP-0109 e permessi CAP-0077; Meeting Load Heatmap → CAP-0106 + CAP-0101.
- **Capability preesistenti collegate:** CAP-0001 (slot), CAP-0028 (connettori), CAP-0075 (import), CAP-0077 (permessi), CAP-0093 (note-to-checklist), CAP-0094 (Kanban), CAP-0096 (task/relazioni), CAP-0099 (planner studio), CAP-0101 (dashboard). Nessun nuovo ID per funzioni gia coperte.
- **Note-Ecosistema:** priorita esplorativa alta per CAP-0103, CAP-0102, CAP-0104, CAP-0108 e CAP-0109, ma ordine da confermare dopo audit del repository app.
- **Anna's Diary:** solo rescheduling di task flessibili, suggerimenti priorita semplici e riepilogo settimanale; carico/heatmap solo se i calendari canonici lo consentono. Nessuna Kanban aziendale o nuovo backend.
- **FocuSense:** possibile riuso del focus timer senza importazione automatica di dati o acquisti cross-app.

## Requisiti prima di implementare

1. **Nessun codice/roadmap app alterato:** fonte di verita dell'implementazione sono i repository app. Auditare task, reminder, timer, canvas, planner e interfacce presenti prima di aprire PR nelle app.
2. **Preservare una sola task canonica** in note, planner, timeline, Kanban, grafo e report; identificatori, relazioni, stato, reminder e lifecycle condivisi. Soft delete/restore/backup per tutti i nuovi link.
3. **Pianificazione sicura:** disponibilita, timezone, scadenze, appuntamenti fissi vs task flessibili e preferenze esplicite. Solo *proposte* con preview e consenso prima di scrivere o notificare; piano originale ripristinabile.
4. **Performance:** parsing/metriche/solver leggero locale e deterministico dove possibile. Nessun modello pesante incluso di default nell'APK, niente inferenza cloud implicita.
5. **Focus e permessi:** timer resistente a sospensione processi; notifiche/DND e restrizioni OS solo con permessi e capability probe, nessun blocco siti universale promesso.
6. **Fonti/licenze:** donor e benchmark sono riferimenti, non dipendenze approvate; conservare la distinzione Apache-2.0 del singolo progetto e licenze di librerie/modelli/dati.
7. **Verifica:** unita, accessibilita, data loss, DST/timezone, ripristino eventi, collisioni, backup, degrado offline, privacy, e test su dispositivo ove necessario.

**Decisione archivio:** idee #13–28 conservate senza promozione; 11 nuove capability canoniche, 5 idee rappresentate tramite riuso dei CAP; tutte le associazioni aggiunte con stato `PROPOSTA`.
