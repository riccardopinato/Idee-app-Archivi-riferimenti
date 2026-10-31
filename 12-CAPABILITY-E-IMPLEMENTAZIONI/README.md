# Catalogo centrale capability — App Factory

**82 capability individuali, 39 app/idee beneficarie e 212 associazioni app-capability**, audit iniziale 01/11/2026.

- [Classifica globale](CLASSIFICA_PRIORITA.md)
- [Matrice per app](MATRICE_APP.md)
- [Stato implementazioni](STATO_IMPLEMENTAZIONI.md)
- [Schede individuali](REGISTRO_CAPABILITY/)
- [JSON canonico](REGISTRO_CAPABILITY.json)
- [Audit fonti e copertura](AUDIT_TRASVERSALE_2026-11-01.md)
- [Automazione incrementale](AUTOMAZIONE_E_REGOLE.md)

## Regole

**Una capability = un ID stabile.** Una stessa capability puo essere esistente in un'app e solo candidata in un'altra; registrare sempre `app_states` distinti. In caso di feature assente dal coding repository, non dedurre una mancanza dalle sole parole della roadmap.

**Nuova app**: registrarla in 01-PORTAFOGLIO / 11-NUOVE-IDEE secondo lo stato, poi aggiungere l'ID repository come consumer delle capability esistenti; creare CAP nuovo solo per una responsabilita realmente distinta. Non duplicare schede o cambiare gli ID. Le nuove app NON ereditano automaticamente dati, permessi, acquisti o componenti proprietari.

**Stato**: SOURCE_REPORTED non e SOURCE_VERIFIED, CI PASS non e device PASS. Per promuovere occorrono SHA, path, test e in presenza di native/device il risultato fisico. Le dichiarazioni storiche non prevalgono sulla roadmap/codice corrente.

**Scoring**: valore 35%, riuso 25%, fattibilita 20%, evidenza 10%, rischio basso 10% (fattori 1-5). Le classi P1/P2/P3 sono indicative e separate dalla severity bug P0-P3 del Factory Master.

**Licenze**: ogni API/repo/modello esterno richiede licenza ToS costi footprint privacy e commercial-use gate al momento dell'integrazione; solo ispirazione se non copiable. Questo archivio non autorizza alcuna nuova AI o backend.

## Aggiornamento e verifica

`python3 scripts/generate_capability_views.py` genera pagine e schede. 
`python3 scripts/generate_capability_views.py --check` controlla che nulla derivi da un JSON obsoleto.
Le PR sono validate tramite GitHub Actions. Il monitoraggio inter-repository usa un task ChatGPT con accesso GitHub esplicitamente autorizzato: il token `GITHUB_TOKEN` di questo repository **non ha** accesso ai repository privati altrui. Aggiornamento programmato = differito al prossimo controllo, non webhook istantaneo.
