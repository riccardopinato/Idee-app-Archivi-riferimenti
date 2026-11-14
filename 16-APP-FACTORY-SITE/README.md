# App Factory Control Center — snapshot derivato

La dashboard HTML locale usa il JSON in `data/snapshot.json` come input pubblico **read-only**. Non è il catalogo canonico e non contiene credenziali. L'archivio autorevole resta nei repository App-Factory-Core e Idee-app-Archivi-riferimenti; le decisioni per-app rimangono nelle rispettive Product Bible e roadmap.

**Aggiornamento:** l'attività ChatGPT esistente «App Factory v27 — Tempo reale» alle 09:30 Europe/Rome è configurata per proporre aggiornamenti incrementali del JSON tramite PR, senza altre automazioni. Se non può scrivere o validare, deve dichiarare esplicitamente il blocco: non esiste una sincronizzazione implicita della pagina né del browser.

## Workflow Context Sync (11/11/2026)

Il [registro separato `data/context_fleet.json`](data/context_fleet.json) copre 35 slot, espone soltanto i 32 repo pubblici e anonimizza gli altri tre. La vista **Repository** nel file [src/index.html](src/index.html) mostra lo stato workflow, HEAD osservato, run e PR bot con filtri; i dati manuali `localStorage` e la snapshot precedente non sono modificati. [`scripts/context_fleet.py`](../scripts/context_fleet.py) applica validazione offline e riconciliazione **solo da ricevute reali con URL**, preservando la cronologia append-only. `python3 -m unittest discover -s tests -p context_fleet_test.py -v` è in CI.

**Non è aggiornamento real-time:** dati della fotografia osservata, nessun cron di refresh aggiuntivo, nessuna attivazione remota del Site/Vercel dimostrata. L'eventuale deploy segue controlli separati. **Non sostituisce** `data/snapshot.json` né il catalogo CAP.

**Schema:** `schemaVersion: 1`, `generatedAt`, `sourceRepository`, `catalog_source_sha`, `factoryBaseline`, `completeness`, `data`. Ogni record supportato mantiene origine URL, SHA, orario di consultazione, stato di evidenza. `data.capabilityCounts` rappresenta **associazioni app×CAP**, non il numero di capability uniche. `data.repoObservations` registra veri commit GitHub osservati; main HEAD non certifica comportamenti o release.

**Regola di prova:** SOURCE_REPORTED non significa implementato; SOURCE_CONFIRMED non significa CI; CI non significa device PASS; device PASS non significa Store Ready. Non dedurre certificazioni senza prove puntuali e separate. La versione iniziale dichiara copertura CAP parziale; per copertura integrale usare il registro canonico JSON, non inventare record.

**Protezione dati manuali:** il Site sovrappone ai record sorgente le proprie modifiche locali e conserva il registro delle modifiche. Le sovrascritture GitHub non si propagano nei dati manuali. I dati locali restano nel browser e possono essere esportati con backup JSON; non sono sincronizzati fra dispositivi.

**Consegne/policy:** solo Chat, mai Work; Flutter come default nuovi progetti mobile; codice completo e APK quando applicabile; branch/PR, exact-head CI e gate di verifica rispettati.

**Riservatezza:** questo repository è pubblico. Non aggiungere informazioni private, segreti, token o dati sensibili al JSON. Se una fonte non è condivisibile pubblicamente, registrare solo metadati non sensibili o bloccare l'esportazione.


## Donor & Golden — Site v2 · 8 novembre 2026

Il sorgente HTML della pagina ora è versionato in [src/index.html](src/index.html), invece di vivere soltanto in un deployment Vercel senza Git link. Il dataset pubblico [data/snapshot.json](data/snapshot.json) si basa su Factory Golden Index **v29** al commit `5a34d12f826d0de8cef223036cc074b9dbdaff4d`.

La sezione Donor & Golden presenta **61 Golden ufficiali (inclusi draft/processi)** e **20 Passport per capability** da **17 donor**; **9** Passport E3 nuovi, **2** Golden E5 a perimetro ristretto. Nel catalogo CAP sono conservate **199 CAP e 441 associazioni su 48 app/idee**. Il loro stato non equivale a dispositivo/test release.

**Storico e dati manuali:** la chiave localStorage `appfactory-control-center-v1` non cambia. `syncGitHub` importa i record Golden/Capability e i Passport in sola lettura; i record protetti manualmente continuano a prevalere. Evitare reset dello storage e sostituzioni distruttive. I donor fanno parte della snapshot pubblica; nessuna chiave GitHub/Vercel nel browser. Filtri client-side senza round-trip verso GitHub.

**Gate:** `python3 -m unittest discover -s tests -p site_snapshot_test.py -v`; workflow [App Factory Site snapshot](../../.github/workflows/app-factory-site-snapshot.yml). Deploy Vercel tramite HTML statico (attuale progetto senza Git repository collegato) dopo la PR/CI, con check del dominio produttivo.


## Certificazioni E3 incrementali (08/11/2026)

[Sei donor storici verificati](SYNC_DONOR_E3_2026-11-08.md) da App-Factory-Core PR #87; la snapshot ora contiene 15 E3 puntuali. È sufficiente la sincronizzazione dati GitHub, senza nuovo deploy HTML né reset dello storico manuale.

## Gateway MCP: registro sorgente read-only · 14 novembre 2026

La pagina [src/index.html](src/index.html) contiene la vista «Gateway MCP» con ricerca, filtro e collegamenti alle nove PR #25–#33 di Agent Core; legge unicamente il nuovo [data/gateway_progress.json](data/gateway_progress.json). Le informazioni riportano lo SHA dei commit osservati, esiti CI pubblici, dipendenze, bozze e gate ancora aperti. Questo dataset è **puntuale, non real-time**: non deve aggiornare automaticamente `data/snapshot.json` né gli stati manuali in `localStorage`.

Il CI esegue `tests/gateway_site_test.py` per controllare SHA, URL delle workflow run, assenza di false approvazioni o certificazioni, preservazione dello storage e sintassi JS. I dati GitHub non attestano review formali `APPROVED`, né disponibilità di un servizio MCP remoto. Nessun deploy o refresh schedulato è dichiarato. La cronologia delle modifiche è in [CHANGELOG.md](CHANGELOG.md).
