# Verifica documentale licenze dei 26 OSS95 senza SPDX automatico — 08/11/2026

**Baseline:** App-Factory-Core@85ecbb19aeb02da1b9d04348e043f69bab77bcb9.  
**Sorgente centrale:** [Atlas OSS95 aggiornato](AUDIT_OSS95_CAPABILITY_ATLAS_2026-11-08.json).  
**Campione:** 26/26 progetti con metadato REST GitHub `NOASSERTION` oppure `UNKNOWN`.  
**Estrazione capability:** **TUTTI inclusi**, senza esclusioni basate sulla licenza; queste 26 fonti generano **90 occorrenze repository–funzionalità**, già comprese nelle 329 dell'audit precedente, non aggiuntive.
**Nuove CAP numeriche:** 0 da questo controllo. Restano 39 famiglie E0 da ammettere solo con verifica separata; 47 CAP esistenti con match tematico.

## Decisione metodologica

- Il metadato GitHub `NOASSERTION` significa **licenza non riconosciuta automaticamente**: non è una dichiarazione di pubblico dominio, MIT, Apache o libertà incondizionata.
- **Analisi funzionale senza restrizioni:** lettura di README, struttura, features e contratti; comparazione e riclassificazione per Notes, Anna e altre app. Nessun blocco dell'audit per la sola tipologia della licenza.
- **Copia/embedding del codice NON implicitamente autorizzati**: applicare l'effettiva licenza del singolo file e i vincoli commerciali/copyleft. L'utente vuole valutare potenziali app monetizzate; il confine è materialmente importante.
- I file di licenza e i README sono stati letti come evidenza documentale delle condizioni dichiarate, non come parere legale o esecuzione dei test donor. La fonte resta E0/E1 research.
- Questa PR NON modifica codice di alcuna app, roadmap, decisioni prodotto, stelle GitHub o Golden e non muta i gate Notes #60 e catalogo #41.

## Esito quantitativo

| Classe dalla licenza effettivamente letta | Repository | Uso per l'estrazione capability |
|---|---:|---|
| Permissiva, in parte con componenti separati | 7 | Sì |
| Copyleft (GPL/AGPL/LGPL) o multilicenza | 8 | Sì |
| Source-available/licenze restrittive | 8 | Sì |
| Repository senza codice applicativo, documentazione | 1 | Sì, solo come riferimento di prodotto |
| Indice/aggregatore con condizioni per componente | 2 | Sì, componenti da studiare separatamente |
| **Totale** | **26** | **26/26 analizzati** |

## Evidenze e condizioni specifiche

| Repository | Valutazione reale | File di prova | Facet già estratti | Licenza originale |
|---|---|---:|---:|---|
| [mattermost-community/focalboard](https://github.com/mattermost-community/focalboard) | Copyleft/mista | AGPL-3.0 per il sorgente; alcune cartelle Apache-2.0; distribuzioni compilate Mattermost con MIT; opzione commerciale | 4 | [LICENSE.txt](https://github.com/mattermost-community/focalboard/blob/HEAD/LICENSE.txt) |
| [toeverything/AFFiNE](https://github.com/toeverything/AFFiNE) | Permissiva (con scope) | MIT per molte aree; backend EE con licenza separata e componenti CE/client MPL-2.0 secondo i termini specifici | 5 | [LICENSE](https://github.com/toeverything/AFFiNE/blob/HEAD/LICENSE), [LICENSE-MIT](https://github.com/toeverything/AFFiNE/blob/HEAD/LICENSE-MIT), [packages/backend/server/LICENSE](https://github.com/toeverything/AFFiNE/blob/HEAD/packages/backend/server/LICENSE) |
| [outline/outline](https://github.com/outline/outline) | Source-available/restrittiva | Business Source License 1.1; divieto Document Service; conversione prevista ad Apache-2.0 il 2030-10-23 | 4 | [LICENSE](https://github.com/outline/outline/blob/HEAD/LICENSE) |
| [AppFlowy-IO/appflowy-editor](https://github.com/AppFlowy-IO/appflowy-editor) | Copyleft/mista | Dual license AGPL-3.0 o MPL-2.0 | 3 | [LICENSE](https://github.com/AppFlowy-IO/appflowy-editor/blob/HEAD/LICENSE) |
| [foambubble/foam](https://github.com/foambubble/foam) | Permissiva (con scope) | MIT; alcuni componenti e copyright di terzi sotto condizioni proprie | 3 | [LICENSE](https://github.com/foambubble/foam/blob/HEAD/LICENSE) |
| [anyproto/anytype-ts](https://github.com/anyproto/anytype-ts) | Source-available/restrittiva | Any Source Available License 1.0: uso non commerciale o commercialità limitata alle Allowed Networks | 5 | [LICENSE.md](https://github.com/anyproto/anytype-ts/blob/HEAD/LICENSE.md) |
| [laurent22/joplin](https://github.com/laurent22/joplin) | Copyleft/mista | AGPL-3.0-or-later come default, con eccezioni nelle sottocartelle; loghi protetti | 4 | [LICENSE](https://github.com/laurent22/joplin/blob/HEAD/LICENSE) |
| [HabitRPG/habitica](https://github.com/HabitRPG/habitica) | Copyleft/mista | Codice GPL-3.0; asset CC-BY-SA o CC-BY-NC-SA | 3 | [LICENSE](https://github.com/HabitRPG/habitica/blob/HEAD/LICENSE) |
| [taskade/taskade](https://github.com/taskade/taskade) | Solo documentazione | Repository di documentazione e press kit, senza codice del prodotto; testi consultabili/citabili con attribuzione, media e marchio protetti | 4 | [LICENSE](https://github.com/taskade/taskade/blob/HEAD/LICENSE) |
| [linagora/twake-workplace](https://github.com/linagora/twake-workplace) | Indice/componenti con licenze separate | Repository di indice ecosistema, nessuna licenza dichiarata nel root; i componenti sono in repository distinti | 2 | [README.md](https://github.com/linagora/twake-workplace/blob/HEAD/README.md) |
| [nocodb/nocodb](https://github.com/nocodb/nocodb) | Source-available/restrittiva | Sustainable Use License v1.0 con limiti su distribuzione commerciale e prodotti ospitati | 4 | [LICENSE.md](https://github.com/nocodb/nocodb/blob/HEAD/LICENSE.md) |
| [shuaiplus/inkstone](https://github.com/shuaiplus/inkstone) | Copyleft/mista | LGPL-3.0 | 4 | [LICENSE](https://github.com/shuaiplus/inkstone/blob/HEAD/LICENSE) |
| [regisdantas/gamify-tasks](https://github.com/regisdantas/gamify-tasks) | Source-available/restrittiva | Open Source Non-Commercial License: vietato uso commerciale diretto e indiretto | 2 | [LICENSE](https://github.com/regisdantas/gamify-tasks/blob/HEAD/LICENSE) |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | Source-available/restrittiva | Licenza tldraw custom: uso development; deploy produzione richiede licenza trial/commerciale specifica | 4 | [LICENSE.md](https://github.com/tldraw/tldraw/blob/HEAD/LICENSE.md) |
| [sorenwacker/nodus](https://github.com/sorenwacker/nodus) | Source-available/restrittiva | Nodus License: uso personale o commerciale interno, redistribuzione vietata senza autorizzazione | 4 | [LICENSE](https://github.com/sorenwacker/nodus/blob/HEAD/LICENSE) |
| [plankanban/planka](https://github.com/plankanban/planka) | Source-available/restrittiva | PLANKA Community Fair Use con limiti a hosting commerciale e moduli Pro/Enterprise esclusi | 3 | [LICENSE.md](https://github.com/plankanban/planka/blob/HEAD/LICENSE.md), [LICENSES/PLANKA License Guide EN.md](https://github.com/plankanban/planka/blob/HEAD/LICENSES/PLANKA%20License%20Guide%20EN.md) |
| [ankitects/anki](https://github.com/ankitects/anki) | Copyleft/mista | AGPL-3.0-or-later; parti vendorizzate sotto licenze varie | 2 | [LICENSE](https://github.com/ankitects/anki/blob/HEAD/LICENSE) |
| [Pikos-App/pikos](https://github.com/Pikos-App/pikos) | Source-available/restrittiva | Business Source License 1.1; vietata distribuzione come prodotto commerciale, convertibile ad Apache-2.0 secondo change-date per versione | 5 | [LICENSE](https://github.com/Pikos-App/pikos/blob/HEAD/LICENSE) |
| [vimwiki/vimwiki](https://github.com/vimwiki/vimwiki) | Permissiva (con scope) | MIT | 3 | [LICENSE.md](https://github.com/vimwiki/vimwiki/blob/HEAD/LICENSE.md) |
| [audreyt/ethercalc](https://github.com/audreyt/ethercalc) | Copyleft/mista | CPAL-1.0 e Artistic-2.0 per componenti storici; dipendenze e riscritture con licenze proprie | 3 | [LICENSE.txt](https://github.com/audreyt/ethercalc/blob/HEAD/LICENSE.txt) |
| [baserow/baserow](https://github.com/baserow/baserow) | Permissiva (con scope) | MIT per Open Source Edition; docs CC-BY-SA; premium/enterprise con licenze separate | 4 | [LICENSE](https://github.com/baserow/baserow/blob/HEAD/LICENSE) |
| [seatable/seatable](https://github.com/seatable/seatable) | Indice/componenti con licenze separate | README descrive dtable-web ed eventi Apache-2.0, seaf-server AGPL-3.0, dtable-server proprietario; repository indice senza license root | 3 | [Readme.md](https://github.com/seatable/seatable/blob/HEAD/Readme.md) |
| [amark/gun](https://github.com/amark/gun) | Permissiva (con scope) | Testo LICENSE.md include licenze permissive di componenti, fra cui MIT e Apache-2.0 | 3 | [LICENSE.md](https://github.com/amark/gun/blob/HEAD/LICENSE.md) |
| [yjs/yjs](https://github.com/yjs/yjs) | Permissiva (con scope) | MIT | 3 | [LICENSE](https://github.com/yjs/yjs/blob/HEAD/LICENSE) |
| [berty/berty](https://github.com/berty/berty) | Permissiva (con scope) | MIT e Apache-2.0 incluse, da verificare per ciascun componente | 3 | [LICENSE-MIT](https://github.com/berty/berty/blob/HEAD/LICENSE-MIT), [LICENSE-APACHE](https://github.com/berty/berty/blob/HEAD/LICENSE-APACHE), [COPYRIGHT](https://github.com/berty/berty/blob/HEAD/COPYRIGHT) |
| [zotero/zotero](https://github.com/zotero/zotero) | Copyleft/mista | AGPL-3.0, componenti terzi e marchi distinti | 3 | [COPYING](https://github.com/zotero/zotero/blob/HEAD/COPYING) |

## Controlli particolari

- **AFFiNE:** il file root è in prevalenza MIT, ma il file backend enterprise distingue EE/CE e parti MPL; nessun import del backend senza selezione dello scope.
- **Focalboard:** la licenza MIT dei binari Mattermost non coincide con la AGPL prevista per molto codice sorgente.
- **Outline, NocoDB, Pikos, Nodus, tldraw, gamify-tasks, PLANKA e Anytype:** non si possono dichiarare universalmente open-source permissivi; includerli nei candidati funzionali, richiedere autorizzazione/alternativa per eventuale copia commerciale.
- **Taskade:** il repository collegato è documentazione/promozione, non contiene il codice del prodotto; rimane utile per il benchmarking dell'esperienza.
- **Twake Workplace e SeaTable:** index/aggregator: la licenza di ciascun modulo va ricercata nel repository specifico. Il README SeaTable elenca anche `dtable-server` proprietario.
- **Habitica:** distinguere codice GPL-3.0 da artwork/asset non commerciali.
- **Yjs, Foam, Vimwiki:** codice sotto MIT, salvo componenti esterni e obblighi notice.

## Gate successivo

1. Per ogni nuova CAP candidata della [riconciliazione OSS95](AUDIT_COMPLETO_OSS95_CAPABILITY_2026-11-08.md), scegliere responsabilità non duplicata ed esatta destinazione per-app.
2. Verificare source path, source SHA, licenza **del file preciso** soltanto se si decide di riutilizzare codice, con test E2/E3 e modello legale adatto a un'app pubblicabile.
3. Mantenere `39` candidate E0 e `47` match CAP invariati nella ricerca. Non generare false `CI_VERIFIED` o `DEVICE_VERIFIED`.
4. Conservare i riferimenti OSS aperti alla valutazione anche se lo sviluppo diretto via copia codice è soggetto a licenze più severe.

