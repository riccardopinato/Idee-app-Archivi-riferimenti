# GitHub Projects — mirror operativo App Factory (solo lettura dalla Factory)

## Decisione e fonte canonica

- **Source of truth intatta:** `12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json`, schede `PER_APP/`, kit, README, source repo e roadmap.
- **GitHub Project:** un solo progetto personale, intitolato **App Factory — Capability Dashboard**, con un record per associazione **(app, CAP ID)**. Non creare 48 Projects separati.
- **Stato:** implementazione del sincronizzatore e collaudo offline; la creazione **reale** del Project richiede il segreto `APP_FACTORY_PROJECT_TOKEN`, non disponibile dalla connessione GitHub del solo Chat. Non dichiarare creato un Project finché l'Actions run live non mostra `PROJECT_CREATED`/`PROJECT_REUSED`, `PILOT_PASS` e `FULL_SYNC_PASS` con URL.
- **Assenza di operazioni distruttive:** nessuna cancellazione di file, issue o item, nessuna archiviazione, nessuna modifica ai repository app, nessuna variazione di visibilità e nessuna scrittura di stati nel registro canonico.

## Snapshot catalogo 04/11/2026

- Registro canonico ricalibrato: **150 CAP / 48 app / 346 associazioni**; le 342 associazioni menzionate nello storico sotto sono il precedente snapshot, non un limite del sync.
- Il mirror ricalcola i campi dai dati canonicali: non elimina gli item legacy, non promuove uno stato app in base al solo CI e non interpreta facilità come probabilità.
- Un precedente Pilot/Batch/Full PASS per 342 righe **non certifica** la presenza di tutte le 346 righe: serve una nuova lettura remota dopo il cambio catalogo.

## Campi e viste

Campi: `App` (testo), `Priorità` (numero 0–100), `Facilità` (numero 0–100), `Fase` (menu: Da valutare, Già integrati, Da verificare). Il titolo del draft include CAP + app + descrizione.

Viste iniziali in layout **Table**: `Tutte le capability`, `Da valutare`, `Già integrati`, `Da verificare`. I filtri sulle viste sono salvati tramite GraphQL. I campi sono visibili; per ordinamento multiplo scegliere **View → Sort**, selezionare `Priorità` discendente e `Facilità` discendente, quindi **Save changes**. La creazione programmata delle viste non pretende di aver configurato il loro ordinamento, poiché le mutation pubbliche verificate espongono filter e campi visibili ma non il salvataggio sort-by.

Le 48 app si consultano filtrando il campo `App`; non creare 48 pannelli permanenti. Lo stesso CAP in due app ha **due elementi distinti**, con stati indipendenti.

## Test pilota e promozione automatica

`scripts/projects_sync.py` offre quattro modalità:
- `--mode dry-run` (default): legge tutti i CSV derivati per app, incrocia ID, nomi, punteggi e facilità contro il JSON canonico; **non necessita token** e non chiama GitHub.
- `--mode pilot`: crea/recupera il Project, assicura campi/viste, importa **6 associazioni** che coprono le tre categorie, rileggendo da API Project i valori e fallendo se non corrispondono.
- `--mode bootstrap`: esegue lo stesso pilota e, **solo dopo PILOT_PASS**, avvia un batch di massimo **180 associazioni** da aggiungere/aggiornare. A import incompleto stampa `BATCH_SYNC_PASS ... REMAINING N`; i run successivi riprendono automaticamente dalle chiavi stabili. `FULL_SYNC_PASS` compare solo al completamento effettivo di tutte le associazioni e della rilettura API.
- `--mode full`: sincronizzazione incrementale di un batch di massimo 180 righe, consentita soltanto dopo un pilot già verificato; non elimina elementi non più presenti nell'archivio.

Il parser usa soltanto `PER_APP/<app>/TABELLA.csv` già generato da `scripts/build_catalog.py` e prima richiede `--check`; nessun punteggio minimo arbitrario (85/85 non è un criterio automatico).

Stato al momento della prima implementazione: **147 CAP**, **48 app**, **342 associazioni** (**214 da valutare / 8 confermate / 120 da verificare**). Sono valori snapshot, non quote fisse del sincronizzatore; i futuri record vengono letti dinamicamente.

## Attivazione GitHub con credenziali appropriate

1. Su GitHub creare un **personal access token (classic)** con scope `project` oppure un token GitHub App con autorizzazione Projects scrittura. Meglio privilegi minimi compatibili; NON inserire il token nel repository o in chat.
2. Nel repository `riccardopinato/Idee-app-Archivi-riferimenti`, aprire **Settings → Secrets and variables → Actions → New repository secret**, nome `APP_FACTORY_PROJECT_TOKEN`, valore del token.
3. Aprire **Actions → App Factory Project mirror (non-destructive) → Run workflow**, modalità `bootstrap`; in alternativa il cron/push attiva automaticamente `bootstrap` quando il segreto esiste. Il primo passaggio può essere soltanto parziale per rispettare i limiti di GitHub; senza interventi ulteriori, il cron riprende dal batch precedente.
4. Verificare l'URL del Project nel log di Actions e `PILOT_PASS`; `BATCH_SYNC_PASS ... REMAINING N` indica un import ancora **parziale**. Solo `FULL_SYNC_PASS` e `REMOTE_VERIFIED` su tutte le righe attestano completamento. Se l'API è bloccata, il processo termina senza fingere un import eseguito.

La connessione GitHub integrata in ChatGPT espone repo/PR/file/Actions, **non le mutation GitHub Projects V2**: non può creare il Project senza credenziali addizionali. Il token rimane solo nei Secrets GitHub Actions.

## Automatismi e sicurezza

- Workflow: `.github/workflows/app-factory-project-sync.yml`.
- Trigger: **push su main** che modifica il registro o i CSV per-app, **cron ogni quattro ore al minuto 20 UTC**, o **workflow_dispatch**. Non è un processo ChatGPT in background; è un workflow GitHub Actions realmente configurato.
- Nessuna chiamata API su PR non fidate o senza segreto. I test CI eseguono solo modalità dry-run e fake API.
- Limite di sicurezza: al massimo **180 associazioni** per run, pause di almeno 1,3 secondi tra mutation GraphQL, per ridurre il rischio di secondary rate limit GitHub (80 richieste che creano contenuti/min, 500/ora secondo la documentazione; limiti soggetti a modifiche). La sincronizzazione di 342 coppie può richiedere più run: nessun dato è perso e nessun elemento viene cancellato.
- Interruzione: il successivo run recupera i draft già importati dal marker `<!-- APP_FACTORY_CAP_PAIR:<app>|<CAP> -->` senza duplicare.
- Nessuna mutation di eliminazione/archiviazione; gli item estranei senza marker non vengono mai modificati; i campi di altre persone non vengono aggiornati.
- Schema/campo ambiguo, ID duplicati, dati incompleti, errori GraphQL o controllo live fallito: **fail closed** e niente fase successiva.
- Lo stato `GIA_INTEGRATI` richiede la prova già definita nel registro; la Project UI non promuove unilateralmente una feature a integrata.
- Il workflow non modifica il registro JSON, i file Markdown, i CSV o il codice delle app.

Riferimenti ufficiali:
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects
- https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-table-layout
- https://docs.github.com/en/graphql/reference/projects

**Nota sul costo:** GitHub Projects è disponibile su GitHub Free; le Actions e gli eventuali componenti associati rimangono soggetti alle normali quote e condizioni del piano GitHub. Nessun servizio cloud a pagamento viene introdotto dallo script.
