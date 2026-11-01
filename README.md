# Idee app — archivio e riferimenti

**Archivio organizzato** per idee app, classifiche, descrizioni cliente, suite, micro-utility, fonti dati, librerie, repository, commercializzazione e aggiornamenti. Il repository non contiene il codice delle app.

## Navigazione

| Cartella | Trovi qui |
|---|---|
| [00-GUIDA](00-GUIDA/COME_AGGIORNARE.md) | Come cercare, aggiungere e verificare informazioni |
| [01-PORTAFOGLIO](01-PORTAFOGLIO/CATALOGO_APP.md) | App già registrate e [classifica Chat/GitHub](01-PORTAFOGLIO/CLASSIFICA_2026-10-30.md) e [audit opportunità](01-PORTAFOGLIO/AUDIT_OPPORTUNITA_2026-10-30.md) e [audit](01-PORTAFOGLIO/AUDIT_CHAT_GITHUB_2026-10-30.md) |
| [02-SUITE-E-MICROAPP](02-SUITE-E-MICROAPP/SUITE_E_COMPONENTI.md) | Composizione suite, componenti, vendita standalone e combinata |
| [03-WEB-UTILITY](03-WEB-UTILITY/CATALOGO_WEB_001_016.md) | 16 idee SEO, [ranking](03-WEB-UTILITY/CLASSIFICA.md), multi-market |
| [04-FONTI-DATI](04-FONTI-DATI/REGISTRO_FONTI_API.md) | [POI/mappe](04-FONTI-DATI/POI_MAPPE.md), [meteo](04-FONTI-DATI/METEO_CLIMA.md), [mobilità](04-FONTI-DATI/MOBILITA.md), [dati vari](04-FONTI-DATI/ALTRI_DATASET.md) |
| [05-REPOSITORY-E-LIBRERIE](05-REPOSITORY-E-LIBRERIE/LIBRERIE_DONOR.md) | Librerie OSS, repo di riferimento e [link centrali](05-REPOSITORY-E-LIBRERIE/REPOS_CENTRALI.md) |
| [06-SINERGIE-E-INTEGRAZIONI](06-SINERGIE-E-INTEGRAZIONI/APP_VERSO_FONTI.md) | Quali fonti/librerie possono migliorare quali app; [matrice riuso 30/10](06-SINERGIE-E-INTEGRAZIONI/OPPORTUNITA_RIUSO_2026-10-30.md) |
| [07-DESCRIZIONI-CLIENTI](07-DESCRIZIONI-CLIENTI/INDICE.md) | Descrizioni orientate agli utenti finali, in bozza |
| [08-MONETIZZAZIONE](08-MONETIZZAZIONE/MODELLI.md) | AdMob, Lifetime, micro-app + suite, SEO |
| [09-AGGIORNAMENTI](09-AGGIORNAMENTI/CHANGELOG.md) | Cronologia modifiche e decisioni |
| [10-MODELLI](10-MODELLI/SCHEDA_APP.md) | Modelli standard per app, provider e librerie |
| [11-NUOVE-IDEE](11-NUOVE-IDEE/README.md) | **Nuove proposte**, [inbox](11-NUOVE-IDEE/INBOX_IDEE.md), [audit nuove idee](11-NUOVE-IDEE/CANDIDATI_AUDIT_2026-10-30.md) e candidati non ancora promossi al portafoglio |
| [12-CAPABILITY-E-IMPLEMENTAZIONI](12-CAPABILITY-E-IMPLEMENTAZIONI/README.md) | **140 capability trasversali**, [ranking](12-CAPABILITY-E-IMPLEMENTAZIONI/CLASSIFICA_PRIORITA.md), [matrice app](12-CAPABILITY-E-IMPLEMENTAZIONI/MATRICE_APP.md), [schede per app](12-CAPABILITY-E-IMPLEMENTAZIONI/PER_APP/), [stati](12-CAPABILITY-E-IMPLEMENTAZIONI/STATO_IMPLEMENTAZIONI.md), audit e inventario per aggiornamenti futuri |
| [90-STORICO](90-STORICO/REGISTRO_MASTER_2026-10-30.txt) | Registro integrale originale, immutato |

## Versioni centrali: snapshot letto il 30 ottobre 2026

- [App-Factory-Core](https://github.com/riccardopinato/App-Factory-Core): CURRENT.yaml seleziona Master **v27**, Golden Index **v23**; commit letto: e9507056601c4a6751510da4c5d1f61601a5dc25.
- [AppLab](https://github.com/riccardopinato/AppLab): linea **v6.3**, commit main letto: 46816a1786820eb7c0edab7500ca950b10c7718c.
- Per nuovi task, risolvere di nuovo le versioni correnti solo quando richiesto dalla governance. Questi SHA sono **traccia storica**, non baseline eternamente valida.

## Convenzioni essenziali

Ogni nuova idea entra prima in **11-NUOVE-IDEE**; dopo valutazione può essere promossa in **01-PORTAFOGLIO**, senza cancellare lo storico. Non eliminare idee o riutilizzare ID storici. Separare informazioni **verificate**, **storiche** e **candidate**. Le licenze/ToS e i costi dei dati vanno verificati prima dell'integrazione commerciale. App e suite hanno prodotti e package separati, ma possono riusare capability. Le schede clienti non devono promettere funzioni non testate. Aggiornare il [changelog](09-AGGIORNAMENTI/CHANGELOG.md).

La Factory centrale governa **regole e Golden**; AppLab governa **QA/orchestrazione**; ogni repo app governa **codice, roadmap, certificazione**; questo repo è **archivio portfolio/ricerca**.

## Nuove fonti community
- [Ricerca r/BestGitHubRepos — 1 novembre 2026](12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_REDDIT_BESTGITHUBREPOS_2026-11-01.md) — componenti concreti, donor con commit/licenze, nuove app candidate e limiti.

## Ricerca Hugging Face per le app delle note

- [12 idee «to do» per Notes-Ecosistema e Anna's Diary](12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_NOTE_2026-11-01.md), in proposta: CAP-0092…CAP-0101 e collegamento ai CAP esistenti, senza cambiamenti alle roadmap delle app.
- [Seconda ricerca: altre 16 idee «to do» (#13–28)](12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_TODO_SECONDA_RICERCA_2026-11-01.md), in proposta: CAP-0102…CAP-0112 e riuso di capability gia catalogate. Totale idee Hugging Face: 28.

- [Terza e quarta ricerca: idee #29–56](12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_29_44_2026-11-01.md) ([segue #45–56](12-CAPABILITY-E-IMPLEMENTAZIONI/RICERCA_HUGGINGFACE_NOTE_IDEE_45_56_2026-11-01.md)): catalogo complessivo di **56 idee**, con CAP-0114…CAP-0140 e fonte e stato distinti.

## Capability e nuovi repository (dal 1 novembre 2026)

Le **idee di nuove app** continuano a entrare in `11-NUOVE-IDEE`; i **miglioramenti o motori riusabili** entrano in `12-CAPABILITY-E-IMPLEMENTAZIONI` con ID CAP stabile, fonte e stato *per app*. L'inventario dei repo è aggiornabile automaticamente da un controllo periodico ChatGPT/GitHub autorizzato; non è una sincronizzazione istantanea o un'autorizzazione a modificare i singoli prodotti.
