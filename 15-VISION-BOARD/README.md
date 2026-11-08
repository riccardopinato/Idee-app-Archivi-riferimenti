# Vision Board — ricerca, donor, Golden candidati e capability

Sezione tematica **esclusivamente dedicata alle Vision Board**: bacheche visive di aspirazioni, obiettivi, ispirazioni, immagini, ricordi e progetti. Comprende moodboard e collage soltanto quando utili al caso d'uso. **Non è** un catalogo generico di tutte le whiteboard, una nuova app o una seconda source of truth delle capability.

**Stato dopo lotto 2 (08/11/2026):** **40 segnalazioni, 39 riferimenti unici**: 28 repo E1 SHA, 10 directory Topics E0 con URL e 1 alias non verificato; 1 input duplicato. **28 estrazioni candidate**, prossimo VBR-0040. Nessuna CAP/Golden ufficiale o app modificata.

## Destinazioni principali
1. **Notes-Ecosistema (priorità di ricerca primaria):** Vision Board progettuali e creative con immagini, sticky notes, obiettivi, milestone, riferimenti e connessioni a note/task/progetti **canonici**. Preferire estensione della lavagna/Visual Workspace già esistente, senza creare un secondo editor o database.
2. **Anna's Diary (priorità di ricerca primaria, UX distinta):** Vision Board personali, sogni, obiettivi di vita e ricordi; collegamenti facoltativi a diario, foto, ricordi e calendario. Esperienza emozionale, semplice, privata e reversibile, non un clone di Notes o un planning professionale.
3. **Altre app, solo se emerge un caso concreto:** per esempio FrameLab (palette/reference board fotografica), Wonderlog (ispirazione viaggi), o altre app della Factory. Nessuna roadmap è modificata implicitamente.

## Indice operativo
- [Inbox cumulativa 39 record](INBOX_REPOSITORY.md): 28 repo E1 e 11 fonti di discovery E0.
- [Lotto 2: 20 input e deduplicazione](LOTTO_2_20_RIFERIMENTI_2026-11-08.md): 19 nuove schede e proprietari canonici corretti.
- [Audit comparativo lotto 2](AUDIT_20_RIFERIMENTI_VB_LOTTO_2_2026-11-08.md): verifica licenze, codice e priorità.
- [Audit comparativo primo lotto](AUDIT_20_RIFERIMENTI_VB_2026-11-08.md): confronti, licenze, priorità Notes/Anna.
- [Registro fonti JSON](REGISTRO_FONTI_VB.json): inventario canonico delle **fonti Vision Board** e delle estrazioni candidate; non sostituisce la CAP registry.
- [Protocollo di audit](PROTOCOLLO_AUDIT_VB.md): regole di lettura, licenze, confronto, benchmark e admission.
- [Template per singolo repository](TEMPLATE_SCHEDA_REPOSITORY.md): scheda `SCHEDE/VBR-XXXX.md` da creare dopo l'intake.
- [28 estrazioni candidate](ESTRAZIONI_CANDIDATE.md): donor/pattern/Golden/CAP, nessuna certificazione.
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
