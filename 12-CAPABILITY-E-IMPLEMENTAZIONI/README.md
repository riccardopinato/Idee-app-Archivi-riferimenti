# Catalogo centrale capability — App Factory

**140 capability individuali, 48 app/idee beneficiarie e 324 associazioni app-capability**, stato catalogo 01/11/2026 (audit iniziale + ricerche incrementali).

- [Classifica globale](CLASSIFICA_PRIORITA.md)
- [Matrice per app](MATRICE_APP.md)
- [Schede per singola app](PER_APP/)
- [Stato implementazioni](STATO_IMPLEMENTAZIONI.md)
- [Schede individuali](REGISTRO_CAPABILITY/)
- [JSON canonico](REGISTRO_CAPABILITY.json)
- [140 kit tecnici](../13-KIT-INTEGRAZIONE/README.md) e [indice](../13-KIT-INTEGRAZIONE/INDICE.md)
- [Metodologia percentuali facilità](../13-KIT-INTEGRAZIONE/METODOLOGIA_FACILITA.md)
- [Audit fonti e copertura](AUDIT_TRASVERSALE_2026-11-01.md)
- [Ricerca r/BestGitHubRepos 01/11](RICERCA_REDDIT_BESTGITHUBREPOS_2026-11-01.md)
- [Hugging Face «to do»: 12 proposte Notes/Anna 01/11](RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md)
- [Seconda ricerca Hugging Face: altre 16 idee, #13–28](RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md)
- [Terza ricerca Hugging Face: idee #29–44](RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md)
- [Quarta ricerca Hugging Face: idee #45–56](RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md)
- [Automazione incrementale](AUTOMAZIONE_E_REGOLE.md)

## Regole

**Una capability = un ID stabile.** Una stessa capability puo essere esistente in un'app e solo candidata in un'altra; registrare sempre `app_states` distinti. In caso di feature assente dal coding repository, non dedurre una mancanza dalle sole parole della roadmap.

**Nuova app**: registrarla in 01-PORTAFOGLIO / 11-NUOVE-IDEE secondo lo stato, poi aggiungere l'ID repository come consumer delle capability esistenti; creare CAP nuovo solo per una responsabilita realmente distinta. Non duplicare schede o cambiare gli ID. Le nuove app NON ereditano automaticamente dati, permessi, acquisti o componenti proprietari.

**Stato**: SOURCE_REPORTED non e SOURCE_VERIFIED, CI PASS non e device PASS. Per promuovere occorrono SHA, path, test e in presenza di native/device il risultato fisico. Le dichiarazioni storiche non prevalgono sulla roadmap/codice corrente.

**Scoring**: valore 35%, riuso 25%, fattibilita 20%, evidenza 10%, rischio basso 10% (fattori 1-5). Le classi P1/P2/P3 (P1 >=92; P2 79-91; P3 <79) sono indicative e separate dalla severity bug P0-P3 del Factory Master.

**Licenze**: ogni API/repo/modello esterno richiede licenza ToS costi footprint privacy e commercial-use gate al momento dell'integrazione; solo ispirazione se non copiable. Questo archivio non autorizza alcuna nuova AI o backend.

## Audit totale Anna's Diary (61/61)

[Rapporto di compatibilita sorgente](../13-KIT-INTEGRAZIONE/ANNA_FULL_AUDIT_61_2026-11-01.md) con schede per ogni CAP. Nella [tabella Anna](PER_APP/Agenda-per-Anna.md) sono aggiunti Esito sorgente e Analisi compatibilita, oltre alla facilità percentuale, senza promuovere alcuna capability a runtime certificato.

## Colonne per-app

Ogni tabella delle app presenta Score, **Facilita integrazione (%)**, **Descrizione breve**, **Kit tecnico** e l'evidence ladder. Le percentuali sono stime preliminari per singola app e si aggiornano nel JSON. I kit sono al livello 1, senza codice donor copiato o licenza verificata nel kit.

## Aggiornamento e verifica

`python3 scripts/build_catalog.py` genera pagine e schede. 
`python3 scripts/build_catalog.py --check` controlla che nulla derivi da un JSON obsoleto.
Le PR sono validate tramite GitHub Actions. Il monitoraggio inter-repository usa un task ChatGPT con accesso GitHub esplicitamente autorizzato: il token `GITHUB_TOKEN` di questo repository **non ha** accesso ai repository privati altrui. Aggiornamento programmato = differito al prossimo controllo, non webhook istantaneo.
