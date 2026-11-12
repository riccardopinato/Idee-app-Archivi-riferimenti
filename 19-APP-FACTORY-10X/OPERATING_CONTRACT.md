# App Factory 10x — contratto di continuità controllata

## 1. Source of truth e ordine
1. `App-Factory-Core/CURRENT.yaml` risolto una volta per sessione di Factory.
2. Master v27, Golden Index/Registry e Golden pertinenti.
3. Product Bible e roadmap **del repository di destinazione**.
4. Questo programma approvato: `PROGRAM_QUEUE.json`, semantica e dipendenze; non sostituisce Product Bible.
5. PR, commit esatto, test, provider/device/store receipts come prove. Chat memory non è evidence.

## 2. Stati e completamento
`PLANNED → IN_PROGRESS → VERIFIED` soltanto dopo esecuzione reale, review e fonte.
`PLANNED/IN_PROGRESS → BLOCKED` con motivo e percorso di recovery; mai falsi PASS.
`DEFERRED` se rinviato per capacità o business, conservando storico.
Una task `VERIFIED` richiede `gate_reviewed: true`, almeno una receipt `{kind, url, source_sha}` e **tutti i prerequisiti VERIFIED**. Il validatore impedisce stati strutturalmente infondati; link string validi non sostituiscono una review umana del loro contenuto.

## 3. Router per ogni esecuzione
- Leggi una sola volta la Factory baseline e la coda corrente da `main`.
- Verifica stati nuovi su GitHub; non riusare una vecchia promessa/risposta come test.
- Esegui `--check`, quindi `--next`; raggruppa per owner e permessi.
- Su `READ_ONLY` usa ricerca e auditing verificabili; genera dossier PR solo dove autorizzato.
- Su `PR_GATED` verifica Product Bible, file protetti, repo default SHA; branch singolo, test focalizzati, CI exact-head, review, merge se permesso e nessun gate bloccante.
- Su `HUMAN_GATE` registra blocco e continua su una lane indipendente. Non importare dati Windows, credenziali provider, billing o release senza ulteriori controlli.
- Per ogni lavoro completato registra task ID, source SHA, PR/run URL, gate, limiti, tempo **misurabile** e prossimo task pronto. Senza prova stato invariato.
- Prima di finire una tornata, esegui di nuovo `--next` sulla **nuova main aggiornata**; i successori sono già nel JSON.

## 4. Meccanismi realmente attivi
- **GitHub Actions read-only**: workflow schedulato controlla integrità e pubblica i successori nel Job Summary. Non scrive codice, non apre PR, non tocca altri repo.
- **ChatGPT Automations (task esistente)**: check periodico che può avviare un nuovo run Chat per completare un passaggio con i tool correnti; lo scheduling non mantiene questa conversazione viva in background e non elimina i limiti di esecuzione.
- **Agente Windows**: futuro worker reale e separato; solo dopo acquisizione sorgente e isolamento/QA potrà fare code execution persistente, soggetto a disponibilità PC/runner.

Non dichiarare mai `continuous_code_execution` sulla sola base del job read-only di GitHub. Distingui `SCHEDULE_INSTALLED` da `SCHEDULE_RUNTIME_VERIFIED` dopo il primo run.

## 5. Parallelismo e resilienza
- **Nessun limite numerico artificiale ai task paralleli**: selezionare TUTTI i task READY compatibili nel DAG. La capacità reale di runner, tool, token, rate-limit e risorse determina quanti si eseguono simultaneamente, non una regola `max_parallel=3`. I task READ_ONLY possono lavorare contemporaneamente anche sullo stesso repository.
- Due task `PR_GATED` sullo stesso repository possono lavorare simultaneamente solo quando `write_paths` è esplicito e non sovrapposto, `scope_reviewed=true` in entrambi e i branch sono distinti. Senza prove di isolamento si coordinano i writer, mai due PR che si sovrascrivono o merge senza verifica exact-head.
- **Rimpiazzo immediato del blocco:** task `BLOCKED` non riserva slot né lock di scrittura; registrare motivo e prova, rilanciare `--next` e avviare tutti i nuovi ready indipendenti. Una task `IN_PROGRESS` riserva invece il suo eventuale write-scope. Nessun busy wait in presenza di gate umani.
- Ogni ramo ha budget di scope; in caso di fail, retry limitato e motivato, non loop infinito. Non fare force-push, delete token/branch, override protections o modifiche non reversibili.
- Tutte le lane indipendenti proseguono quando una è bloccata da un gate umano; non mascherare un blocco di sicurezza.
- Per failure di Actions: conservare last known good, distinguere PR bot denied da snapshot dato riuscito e dalla sola CI, registrare URL reale.

## 6. Loop senza fine della roadmap
- Quando W7 si avvicina alla chiusura, proporre una **nuova ondata W8** basata su metriche, nuovi feedback e backlog non completato; aggiungere task con nuovi ID senza rinumerare o cancellare precedenti.
- Fermare automaticamente le azioni che richiedono gate umano, privilegi, costi nuovi o pubblicazioni; non fermare letture/controlli indipendenti.
- Nessun criterio permette di dichiarare verificata una riduzione di dieci volte senza baseline e confronto sufficientemente controllato.
- Storia durable in Git con PR: niente memoria di chat come unica fonte di avanzamento.

## 7. Comandi
```sh
python3 scripts/factory_10x_queue.py --check
python3 scripts/factory_10x_queue.py --next
python3 scripts/factory_10x_queue.py --next --json
python3 -m unittest discover -s tests -p 'factory_10x_queue_test.py' -v
```
