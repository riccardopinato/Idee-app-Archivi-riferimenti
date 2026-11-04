# Notes-Ecosistema — riconciliazione audit dei quattro siti (04/11/2026)

Stato: **AUDIT / INTAKE**, non nuova release, non certificazione dispositivo, non promozione automatica CAP/Golden. Questo documento collega nuove ipotesi alle idee esistenti e allo **stato reale del codice**; il registro canonico `REGISTRO_CAPABILITY.json` e le viste derivate richiedono una successiva riconciliazione formale con rigenerazione, senza dichiarare artificiosamente "integrata" una capability completa per un nucleo parziale.

## Origine e limiti

Fonte: audit utente `AUDIT_NOTES_ANNA_AGGIORNATO_2026-11-04(2).txt`, sezione "I quattro siti e i competitor" (04/11/2026). La ricognizione originale era **audit only**: non equivale a benchmark hardware o a scansione esaustiva dei quattro portali.

| Fonte | Evidenza/pattern effettivo | Decisione per Notes |
| --- | --- | --- |
| [AI Valley](https://aivalley.ai/category/aitools/productivity/) | Reclaim, Audio Pen, MyMind, ChatMind e Text Blaze sono esempi *job-to-be-done*, non donor di codice | Migliorare cattura → proposta → azione, ricerca e template usando motori già presenti; niente chatbot aggiuntivo |
| [Hugging Face](https://huggingface.co/intfloat/multilingual-e5-small) | Modello multilingue citato dall'audit con asset sorgente ~471 MB, oltre runtime e tokenizer | Solo ricerca differita: revisione licenza/revision, quantizzazione e test italiano/ARM64 prima di qualsiasi download opzionale, mai base APK |
| [GitHub / JSON Canvas](https://github.com/obsidianmd/jsoncanvas/blob/main/spec/1.0.md) | Specifica JSON Canvas v1 per nodi e archi, non salvataggio completo di strokes/ink proprietario | Import/export esplicito con report dei dati non trasferibili e test round-trip; non copiare codice non verificato |
| [GitLab Issue Boards](https://docs.gitlab.com/user/project/issue_board/) | Board/WIP e task blocked sono pattern UX, non dipendenza o integrazione GitLab | Semplici READY/DOING/BLOCKED/DONE, budget e prerequisiti visibili sopra i task canonici, senza duplicare planner |

## Crosswalk incrementale: funzione, codice, differenza ancora aperta

| ID intake stabile | Funzione Notes | CAP esistente (se corrispondente) | Stato verificato al 04/11/2026 | Delta e issue |
| --- | --- | --- | --- | --- |
| NOTES-AUD4-001 | Next Action Graph | CAP-0097 adiacente, CAP-0103 per blocker; **non identici** | Nucleo locale già nel codice | UX ignore/snooze e copertura dell'intero portafoglio; [Notes #51](https://github.com/riccardopinato/Notes-Ecosistema/issues/51) per dipendenze |
| NOTES-AUD4-002 | Smart Inbox Review → preview → writer | CAP-0093 per checklist; CAP-0016 è inbox categorie, **non stessa funzione** | [Notes #44](https://github.com/riccardopinato/Notes-Ecosistema/pull/44) merged: 3 card/ignore/snooze/mute; motore [#43](https://github.com/riccardopinato/Notes-Ecosistema/pull/43) | Anteprima applicazione tag/task/progetto, ricontrollo revisione fonte e permessi prima di scrivere; [issue #46](https://github.com/riccardopinato/Notes-Ecosistema/issues/46) |
| NOTES-AUD4-003 | Time Budget / WIP / dependency blockers | [CAP-0106](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0106.md), [CAP-0103](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0103.md) | [PR #45](https://github.com/riccardopinato/Notes-Ecosistema/pull/45) e [#53](https://github.com/riccardopinato/Notes-Ecosistema/pull/53) merged, diagnosi deterministica | Picker UX per dipendenze, filtri, casi limite date e performance; [issue #51](https://github.com/riccardopinato/Notes-Ecosistema/issues/51) |
| NOTES-AUD4-004 | Guided Study e provenance | CAP-0112 adiacente (flashcard), CAP-0097 per provenance, **non equivalenti** | Q/A da fonte esplicita con [PR #52](https://github.com/riccardopinato/Notes-Ecosistema/pull/52) merged | OCR/PDF source snapshot, rettifiche, quote e test di invalidazione; [issue #47](https://github.com/riccardopinato/Notes-Ecosistema/issues/47) |
| NOTES-AUD4-005 | Duplicate Review con diff, keep, merge | [CAP-0116](../12-CAPABILITY-E-IMPLEMENTAZIONI/REGISTRO_CAPABILITY/CAP-0116.md) | Proposta non implementata per intero | Rilevamento spiegabile, conflitti, anteprima, backup e nessun merge automatico; [issue #48](https://github.com/riccardopinato/Notes-Ecosistema/issues/48) |
| NOTES-AUD4-006 | JSON Canvas import/export | CAP-0029 / CAP-0028 riguardano canvas/edge, **non il codec interoperabile** | Nuova responsabilità di portabilità, senza CAP equivalente verificata | Codec v1, provenance e report lossy strokes/media; [issue #49](https://github.com/riccardopinato/Notes-Ecosistema/issues/49) |
| NOTES-AUD4-007 | Daily Note Hub opt-in | Possibili relazioni con CAP-0097/CAP-0111 ma non equivalente | Nuova proposta differita; nessuna seconda source of truth | Vista derivata da note e planner canonici; [issue #50](https://github.com/riccardopinato/Notes-Ecosistema/issues/50) |
| NOTES-AUD4-008 | Provenance First per tutte le azioni derivate | CAP-0097 adiacente; import provenance esistente copre un'altra responsabilità | Parziale: source e revisione in alcune feature | Invariante source → preview → confirm/decline → writer + undo, ACL e stale-source gate, soprattutto [#46](https://github.com/riccardopinato/Notes-Ecosistema/issues/46) |
| NOTES-AUD4-009 | Benchmark multilingue, portabilità e QA | Non è automaticamente una nuova CAP/prodotto | Fixture Factory locali [PR #62](https://github.com/riccardopinato/App-Factory-Core/pull/62), 500/5000 synthetic | Test IT/EN/ES/FR/DE/PT consumer, fonte permission-scoped e real-device; non dichiarare retention misurata |

## Gap del catalogo attuale — non confondere archivio con stato del prodotto

- Il registro corrente elenca 80 associazioni Notes; le viste riportano 74 `Da valutare`, 6 `Da verificare`, **0 `Già integrati`**. Per molte voci si tratta di snapshot obsoleto rispetto alle PR già unite; non significa assenza di tutte le funzionalità nel codice.
- Non assegnare `INTEGRATED` a CAP-0106, CAP-0103, CAP-0116 o CAP-0112 senza confrontare l'intero contratto della CAP, non soltanto l'MVP collegato.
- In un PR tecnico successivo riconciliare gli stati di ciascuna **associazione** per Notes nel JSON canonico, citare SHA/file/CI, aggiungere nuovi CAP **solo** per responsabilità distinte (in particolare JSON Canvas e Smart Inbox end-to-end) e rigenerare `scripts/build_catalog.py` + `--check`.
- Nessun nuovo modello AI o dipendenza di rete di default. Nessun merge automatico di note, nessuna esposizione di dati Shared Spaces senza permesso, nessuna nuova architettura per il planner.

## Fonti codice principali

[Notes main](https://github.com/riccardopinato/Notes-Ecosistema) · [Smart Inbox #44](https://github.com/riccardopinato/Notes-Ecosistema/pull/44) · [Workload Guard #45](https://github.com/riccardopinato/Notes-Ecosistema/pull/45) · [Dependencies #53](https://github.com/riccardopinato/Notes-Ecosistema/pull/53) · [Guided Study #52](https://github.com/riccardopinato/Notes-Ecosistema/pull/52).

**Nessun codice di Notes modificato da questa ricognizione dell'archivio.** L'audit utente precede le PR 43/44/45/52/53: la matrice sopra aggiorna lo stato in base alle PR successivamente integrate.
