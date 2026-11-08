# Vision Board — ricerca, donor, Golden candidati e capability

Sezione tematica **esclusivamente dedicata alle Vision Board**: bacheche visive di aspirazioni, obiettivi, ispirazioni, immagini, ricordi e progetti. Comprende moodboard e collage soltanto quando utili al caso d'uso. **Non è** un catalogo generico di tutte le whiteboard, una nuova app o una seconda source of truth delle capability.

**Stato iniziale (08/11/2026):** infrastruttura di intake pronta; **0 repository Vision Board ricevuti e auditati**. Primo ID disponibile: `VBR-0001`. Le opportunità sotto sono ipotesi di integrazione, non feature già implementate o approvate.

## Destinazioni principali
1. **Notes-Ecosistema (priorità di ricerca primaria):** Vision Board progettuali e creative con immagini, sticky notes, obiettivi, milestone, riferimenti e connessioni a note/task/progetti **canonici**. Preferire estensione della lavagna/Visual Workspace già esistente, senza creare un secondo editor o database.
2. **Anna's Diary (priorità di ricerca primaria, UX distinta):** Vision Board personali, sogni, obiettivi di vita e ricordi; collegamenti facoltativi a diario, foto, ricordi e calendario. Esperienza emozionale, semplice, privata e reversibile, non un clone di Notes o un planning professionale.
3. **Altre app, solo se emerge un caso concreto:** per esempio FrameLab (palette/reference board fotografica), Wonderlog (ispirazione viaggi), o altre app della Factory. Nessuna roadmap è modificata implicitamente.

## Indice operativo
- [Inbox dei link VBR](INBOX_REPOSITORY.md): URL inviati, ID stabili, deduplicazione, stato e SHA.
- [Registro fonti JSON](REGISTRO_FONTI_VB.json): inventario canonico delle **fonti Vision Board** e delle estrazioni candidate; non sostituisce la CAP registry.
- [Protocollo di audit](PROTOCOLLO_AUDIT_VB.md): regole di lettura, licenze, confronto, benchmark e admission.
- [Template per singolo repository](TEMPLATE_SCHEDA_REPOSITORY.md): scheda `SCHEDE/VBR-XXXX.md` da creare dopo l'intake.
- [Estrazioni candidate](ESTRAZIONI_CANDIDATE.md): vista leggibile di donor, Golden e nuove responsabilità da valutare; nessuna certificazione per sola catalogazione.
- [Crosswalk verso CAP e Golden esistenti](CROSSWALK_CAP_GOLDEN.md): evitare duplicazioni e valorizzare i motori già presenti.
- [Matrice consumer](MATRICE_CONSUMER.md): Notes, Anna e riusi secondari, con confini di prodotto.

## Procedura per ogni repository che verrà inviato
1. Normalizzare il link, fissare `owner/repo@SHA`, verificare upstream/fork e deduplicare per URL canonico; assegnare `VBR-0001` e successivi **solo a fonti reali**.
2. Ispezionare README, codice specifico, dipendenze, test, CI e licenze **di codice, immagini, template, font, asset e dataset** separatamente. Classificare la profondità reale E0/E1/E2/E3.
3. Estrarre il **modulo minimo riusabile**: funzionalità, prova del file, limiti, costi, footprint, piattaforme, sicurezza e accessibilità.
4. Classificare separatamente `CODE_DONOR_CANDIDATE`, `PATTERN_DONOR`, `UX_REFERENCE`, `GOLDEN_CANDIDATE`, `CAPABILITY_MATCH`, `NEW_CAP_PROPOSAL`, `APP_IDEA` o `REJECTED`.
5. Verificare prima le CAP già presenti e il Golden Infinite Canvas/Ink. Una tecnica nuova non equivale automaticamente a una nuova capability.
6. Produrre un verdetto **per consumer** (Notes/Anna/altro), con beneficio, delta rispetto al codice reale, rischio, facilità euristica e gate di validazione.
7. Aggiornare Inbox, scheda, registro JSON e vista estrazioni nella stessa PR. Non inventare test o licenze; non applicare automaticamente modifiche alle app.

## Source of truth e limiti
- Factory: [App-Factory-Core/CURRENT.yaml](https://github.com/riccardopinato/App-Factory-Core/blob/main/CURRENT.yaml), risolta una volta per sessione. Baseline letta per la creazione: `c709e483d40424c88b6ba316d0c8352eec5370fe` — Master v27 / Golden Index v28.
- CAP e stati **per app**: [registro canonico](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY.json).
- Kit ammessi: [13-KIT-INTEGRAZIONE](../13-KIT-INTEGRAZIONE/README.md), dopo la normale ammissione.
- Nuove idee di prodotto: [11-NUOVE-IDEE](../11-NUOVE-IDEE/INBOX_IDEE.md).
- Policy del repository: [AGENTS.md](../AGENTS.md).

**Limite di mandato:** questa sezione è un laboratorio di ricerca. Nessuna copia di codice privo di licenza compatibile, nessuna promozione ufficiale Golden/donor, nessuna nuova CAP canonica, nessuna modifica a roadmap o sorgenti Notes/Anna senza workflow e autorizzazione separati.
