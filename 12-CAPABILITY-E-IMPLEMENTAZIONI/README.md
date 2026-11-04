# Catalogo centrale capability — App Factory

## GitHub Projects — dashboard interattiva

[Sincronizzazione unidirezionale, test pilota e procedura di attivazione](GITHUB_PROJECTS_MIRROR.md). Script `scripts/projects_sync.py`: verifica tutte le 48 app, primo test su 6 associazioni, estensione automatica all'intero catalogo soltanto dopo riscontro live e credenziali Projects autorizzate. Le schede e tutti i dati originali restano invariati.

## Priorità da fare vs già integrate

**[DA_VALUTARE.md](../DA_VALUTARE.md)** separa le capability ancora proposte da quelle da verificare e mostra **tutte le associazioni app-capability non integrate**, ordinate per Score di priorità e, a parità, per facilità. **Nessuna soglia 85/85 fissa:** valori diversi sono sempre inclusi; le soglie sono filtri applicabili solo su richiesta. **[GIA_INTEGRATI.md](../GIA_INTEGRATI.md)** elenca le implementazioni con prova puntuale (SHA/PR/CI dove disponibile). Il ranking globale qui rimane *storico/analitico* e non va usato per creare una coda di lavoro senza il filtro stati.

La rigenerazione è inclusa in `python3 scripts/build_catalog.py`; `--check` controlla che i due file non siano obsoleti.


**160 capability individuali, 48 app/idee beneficiarie e 385 associazioni app-capability**, ri-audit 04/11/2026 (audit iniziale + ricerche incrementali).

- [Classifica globale](CLASSIFICA_PRIORITA.md)
- [Matrice per app](MATRICE_APP.md)
- [Schede per singola app](PER_APP/) — tre tabelle operative per app: **Da valutare**, **Già integrati**, **Da verificare**, più **CSV** ricercabile su GitHub e ordinabile in Excel. Lo storico `PER_APP/<app>.md` rimane consultabile.
- [Stato implementazioni](STATO_IMPLEMENTAZIONI.md)
- [Schede individuali](REGISTRO_CAPABILITY/)
- [JSON canonico](REGISTRO_CAPABILITY.json)
- [160 kit tecnici](../13-KIT-INTEGRAZIONE/README.md) e [indice](../13-KIT-INTEGRAZIONE/INDICE.md)
- [Metodologia percentuali facilità](../13-KIT-INTEGRAZIONE/METODOLOGIA_FACILITA.md)
- [Audit fonti e copertura](AUDIT_TRASVERSALE_2026-11-01.md)
- [Ricerca r/BestGitHubRepos 01/11](RICERCA_REDDIT_BESTGITHUBREPOS_2026-11-01.md)
- [Hugging Face «to do»: 12 proposte Notes/Anna 01/11](RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md)
- [Seconda ricerca Hugging Face: altre 16 idee, #13–28](RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md)
- [Terza ricerca Hugging Face: idee #29–44](RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md)
- [Quarta ricerca Hugging Face: idee #45–56](RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md)
- [Automazione incrementale](AUTOMAZIONE_E_REGOLE.md)
- [Anna NotebookLM: 15 idee -> 7 CAP nuove + 5 estensioni](RICERCA_ANNA_NOTEBOOKLM_2026-11-02.md)

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

## Estensione NotebookLM 02/11/2026

Le sette nuove CAP sono **PROPOSTA**, non integrazioni. La classifica originale di 15 idee conserva priorità editoriali P1/P2; il ranking tecnico CAP impiega un'altra formula e può assegnare P3 a proposte con rischi o scarsa evidenza. La vecchia matrice 61/61 di Anna è uno **snapshot storico**, non include le nuove candidature.

## Audit Anna's Diary — 03/11/2026

[Stati CAP riconciliati con evidenze e Factory Golden Index v26](AUDIT_ANNA_CAP_2026-11-03.md). Fonte autonoma del prodotto: Anna Product Bible, Roadmap, commit e CI. Non equivale a QA su dispositivo o release.

## Score Golden v28 — 04/11/2026

[Rapporto audit completo](AUDIT_RIPRIORITIZZAZIONE_GOLDEN_V28_2026-11-04.md); due CSV includono ogni CAP e associazione, anche invariata.

## Audit ML23 / Golden reuse — 04/11/2026

[23 algoritmi mappati a 160 CAP](./AUDIT_GOLDEN_ML_23_ALGORITMI_2026-11-04.md) e [grafo dipendenze](CATENE_MOTORI_ML_2026-11-04.json). Questa e catalogazione E0, non codice certificato.

## Audit ML10 secondo lotto — 04/11/2026

[Audit profondo di 10 famiglie on-device, crosswalk CAP e percorsi Donor/Golden](ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md). Nessuna CAP duplicata: i modelli sono tecniche alternative/estensioni per capability già censite. [Core PR #71](https://github.com/riccardopinato/App-Factory-Core/pull/71) ha integrato due reference engine pure Dart: [Dart CI main SUCCESS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41833497699). Sono verificati in Core, **non** donor di un'app consumatrice né Golden. [Gate E5/Golden #72](https://github.com/riccardopinato/App-Factory-Core/issues/72). Il registro 160 CAP / 385 associazioni resta invariato.

## Full-scope ML10 capability re-audit — 04/11/2026

[Audit ricalcolato di tutte le 160 CAP e 385 associazioni per 48 app](AUDIT_COMPLETO_ML10_2026-11-04.md) con [CSV integrale per capability](AUDIT_COMPLETO_CAP_ML10_2026-11-04.csv), [CSV integrale per app](AUDIT_COMPLETO_APP_ML10_2026-11-04.csv), motivazione individuale nel registro canonico e viste per-app rigenerate. Le variazioni sono evidence-gated, non automatiche né probabilità di successo. [Core P1–P3 #73](https://github.com/riccardopinato/App-Factory-Core/pull/73) matematici PASS; modelli Vision/Audio ancora bloccati su diritti, modello e QA. Golden v28 non promosso.

## ML10: implementazioni consumer e P3 model gate — 04/11/2026

- [Ammissione scoped postmerge Notes #57 e TasteAI #2](ML10_CONSUMER_POSTMERGE_2026-11-04.md). Il registro canonico conserva 160 capability e 385 associazioni; CAP-0116 Notes ora SOURCE_REPORTED con stima di facilità 85%, ma merge reversibile e dispositivi non sono certificati.
- [Analisi dei modelli Vision/Audio (EfficientNet-Lite0 e YAMNet)](ML10_MODEL_SCREENING_2026-11-04.md): ricerca P3 con fonti provider, **non** modello licenziato/distribuito.
- [Audit completo con delta prima/dopo](AUDIT_COMPLETO_ML10_2026-11-04.md) e [secondo lotto tecnico](ML10_AUDIT_DONOR_GOLDEN_2026-11-04.md). Ogni stato per app deve restare distinto dal grado di evidenza E3/E4/E5.

## Anna's Diary — Audit delle 58 voci DA_VERIFICARE (04/11/2026)

[Audit trasversale su 58 capability e decisione individuale](AUDIT_ANNA_58_DA_VERIFICARE_2026-11-04.md), basato su [Anna main@ab5360b78187a643e2b101be21e6951441406059](https://github.com/riccardopinato/Agenda-per-Anna/tree/ab5360b78187a643e2b101be21e6951441406059), Core Master v27 / Golden Index v28 @8052b45b771bf3c5694fc6dd8d037bd83233b37a e fonti Donor/Golden pertinenti. Sei sole candidature `PROPOSTA / PARTIAL_REUSE` ammesse **alla valutazione di prodotto** (CAP-0092, 0093, 0101, 0120, 0145, 0147); 52 rimangono da verificare, otto restano integrate. [Da valutare Anna](PER_APP/Agenda-per-Anna/DA_VALUTARE.md) · [Da verificare Anna](PER_APP/Agenda-per-Anna/DA_VERIFICARE.md). Nessuna modifica alla roadmap/prodotto, punteggi, stati tecnici, codice app o Golden.
