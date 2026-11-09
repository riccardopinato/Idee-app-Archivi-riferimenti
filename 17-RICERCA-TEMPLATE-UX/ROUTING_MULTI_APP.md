# Protocollo Template Notion — tutte le app App Factory

**Decisione utente 09/11/2026**: catalogo `Template Notion` **separato in ogni repository di app**, non soltanto Notes e Anna. Nuovi export: inventario centrale unico, assegnazione per affinità prodotto, indici locali specifici.

## Template Engine Standard v1 — contratto tecnico (Maxi-step 1)

La classificazione di questo archivio si collega al [contratto v1 condiviso di App-Factory-Core](https://github.com/riccardopinato/App-Factory-Core/tree/main/contracts/template_engine_v1) (Core PR #89, SHA `d4ed1185d36d419228fba6b57a979cde308bd321`). Il contratto definisce identità, localizzazioni, preview, compatibilità, opzioni e installazione reversibile; è stato staticamente validato con CI della PR. **Non** è installato nelle app e non converte o distribuisce template Notion. Le schede `TPLUX-REF` rimangono ricerca; eventuali manifest app-specifici devono essere originali e passare Product Bible, licenze, adattatore e QA propri.

## Architettura di proprietà
1. Questo repository conserva `TPLUX-REF-NNNN`: fonte, evidenza, limiti, rischi di licenza e deduplicazione.
2. **Ogni app** conserva `docs/TEMPLATE_NOTION/README.md` e `CATALOGO.json`. Le app senza candidati hanno `entries: []`, senza filler.
3. Uno stesso template può interessare più app, ma mantiene **un solo ID centrale**. Le voci locali identificano il tipo di riuso; non duplicano contenuti o inventano nuovi SKU.
4. Per template trasversali, l'app primaria riceve il caso d'uso più completo; le secondarie solo sottoinsiemi compatibili con le rispettive Product Bible.
5. Repository centrali/factory, donor, upstream di terzi e archivi non-app **non sono app consumer**: possono ricevere link al catalogo, non cataloghi locali obbligatori.
6. Se l'app candidata non ha repository disponibile, conservare `UNASSIGNED_REVIEW` nel registro centrale; non assegnare a un prodotto sbagliato.

## Qualità, privacy e licenze
- E0 titolo, E1 marketing pubblico, E2 export Markdown/CSV effettivamente ispezionato, E3 codice donor con licenza verificata e prove. E2 **non** prova formule/automation/layout.
- Nessun export privato, dati di clientela, contatti, prezzi individuali, immagini o ZIP nei GitHub pubblici. I documenti riportano soltanto schema, numero di righe/elementi e pattern generali.
- Sempre **originale e su misura per l'app**, non copy/paste Notion. Nessuna promessa di IAP/Store o rilascio.
- Le voci sono **ricerca** e non alterano la roadmap; per iniziare lo sviluppo servono PR specifica, Product Bible, test, privacy/ACL e UI approval.
- Per l'idea store `€3,99`: prezzo ipotetico, vendita una tantum e billing da validare. Niente acquisti attivi da questo catalogo.

## Contratto JSON locale minimo
```json
{
  "schema_version": 1,
  "application": "Nome App",
  "catalogue_type": "public_research_index",
  "updated_at": "2026-11-09",
  "master_reference": "riccardopinato/Idee-app-Archivi-riferimenti/17-RICERCA-TEMPLATE-UX",
  "entries": [],
  "notes": "Inspiration only; not installed templates"
}
```

## Gate di chiusura
Verificare la creazione fisica dei due file su `main`, gli ID univoci, la coerenza per-app e l'eventuale CI. **Non** considerare una PR aperta come catalogo già attivo su `main`. Non forzare merge contrari alle regole locali (es. repo con approvazione merge esplicita). Non riscrivere README o roadmap delle app se non strettamente necessario alla discoverability.
