# App Factory Control Center — snapshot derivato

La dashboard HTML locale usa il JSON in `data/snapshot.json` come input pubblico **read-only**. Non è il catalogo canonico e non contiene credenziali. L'archivio autorevole resta nei repository App-Factory-Core e Idee-app-Archivi-riferimenti; le decisioni per-app rimangono nelle rispettive Product Bible e roadmap.

**Aggiornamento:** l'attività ChatGPT esistente «App Factory v27 — Tempo reale» alle 09:30 Europe/Rome è configurata per proporre aggiornamenti incrementali del JSON tramite PR, senza altre automazioni. Se non può scrivere o validare, deve dichiarare esplicitamente il blocco: non esiste una sincronizzazione implicita della pagina né del browser.

**Schema:** `schemaVersion: 1`, `generatedAt`, `sourceRepository`, `catalog_source_sha`, `factoryBaseline`, `completeness`, `data`. Ogni record supportato mantiene origine URL, SHA, orario di consultazione, stato di evidenza. `data.capabilityCounts` rappresenta **associazioni app×CAP**, non il numero di capability uniche. `data.repoObservations` registra veri commit GitHub osservati; main HEAD non certifica comportamenti o release.

**Regola di prova:** SOURCE_REPORTED non significa implementato; SOURCE_CONFIRMED non significa CI; CI non significa device PASS; device PASS non significa Store Ready. Non dedurre certificazioni senza prove puntuali e separate. La versione iniziale dichiara copertura CAP parziale; per copertura integrale usare il registro canonico JSON, non inventare record.

**Protezione dati manuali:** il Site sovrappone ai record sorgente le proprie modifiche locali e conserva il registro delle modifiche. Le sovrascritture GitHub non si propagano nei dati manuali. I dati locali restano nel browser e possono essere esportati con backup JSON; non sono sincronizzati fra dispositivi.

**Consegne/policy:** solo Chat, mai Work; Flutter come default nuovi progetti mobile; codice completo e APK quando applicabile; branch/PR, exact-head CI e gate di verifica rispettati.

**Riservatezza:** questo repository è pubblico. Non aggiungere informazioni private, segreti, token o dati sensibili al JSON. Se una fonte non è condivisibile pubblicamente, registrare solo metadati non sensibili o bloccare l'esportazione.
