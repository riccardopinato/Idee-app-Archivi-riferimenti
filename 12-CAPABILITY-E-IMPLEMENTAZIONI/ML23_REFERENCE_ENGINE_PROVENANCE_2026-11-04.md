# ML23 — source ledger dei tre motori riusabili (4 novembre 2026)

- App Factory Core versione fonte: [`ae76e4267b67fe0e913d650d8e89a010dd235a5c`](https://github.com/riccardopinato/App-Factory-Core/commit/ae76e4267b67fe0e913d650d8e89a010dd235a5c)
- Libreria: [`reference_engines/lib/src/on_device_algorithms.dart`](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/lib/src/on_device_algorithms.dart)
- Vettori di test: [`reference_engines/test/on_device_algorithms_test.dart`](https://github.com/riccardopinato/App-Factory-Core/blob/ae76e4267b67fe0e913d650d8e89a010dd235a5c/reference_engines/test/on_device_algorithms_test.dart)
- Verifica eseguita: [reference-dart post-merge PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145600) + [Factory validate PASS](https://github.com/riccardopinato/App-Factory-Core/actions/runs/41814145585)
- Governance: [issue #68 — Golden admission / E5](https://github.com/riccardopinato/App-Factory-Core/issues/68)

| CAP | Motore verificato in Core | Cosa resta da dimostrare |
| --- | --- | --- |
| CAP-0152 | Levenshtein, ricerca fuzzy limitata e filtraggio visible/deleted su input | Tokeni Unicode grapheme, ACL reale, shortlist Notes/Wonderlog e nuove revisioni |
| CAP-0160 | Tokenizzazione Unicode e TF-IDF lessicale sparse | Corpus e stopword 6 locale, ACL app, writer tag confermato e prova consumer |
| CAP-0158 | EWMA con isteresi e debounce su sequenze sintetiche | Adattatore sensori, foreground/lifecycle, batteria e test multi-OEM |

**Regola:** il CI dimostra un *source reference testato*, non E5 su un'app consumatrice, non hardware e non release. Queste tre CAP restano `PROPOSTA` a livello applicativo, il Golden Index v28 rimane la baseline letta dell'audit precedente. Nessun pacchetto ML, API esterna o permesso nativo è stato introdotto da questo aggiornamento.

## Consumer effettivi — integrazioni del 4 novembre 2026

Questa sezione distingue i motori **E3 testati in Core** dalle implementazioni effettivamente integrate nelle app e dalle prove **ancora mancanti**.

| CAP | App consumatrice | Codice e risultato verificato | Gate ancora aperto |
| --- | --- | --- | --- |
| CAP-0152 — fuzzy | [Notes-Ecosistema PR #56](https://github.com/riccardopinato/Notes-Ecosistema/pull/56), main `cb2cbb9a7a4e5070e10ddd6809765ba132fecc85` | Fallback typo limitato su note attive, nella ricerca unificata; filtro ID già trovati applicato prima del limite; [Flutter CI head SUCCESS](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41821096456) | ACL effettiva, cambio account, replay/revisione, prestazioni reali, QA dispositivo |
| CAP-0160 — TF-IDF | Stessa PR #56 / commit Notes | Proposte di tag in dialogo editor, `compute` per snapshot limitati, scelta esplicita prima del salvataggio canonico; test unitari e [CI head SUCCESS](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41821096456) | Validazione writer al salvataggio, ACL, revisione, qualità tag su corpus reali, estensione diretta alla Smart Inbox |
| CAP-0158 — EWMA | [Pocket-Guard PR #6](https://github.com/riccardopinato/Pocket-Guard/pull/6), main `1b10e39801190c3356cc5077973b2c6c96b9c8e0` | Port Kotlin dello stato matematico; campioni motion reali osservati in **shadow mode**, senza influenzare allarmi; [CI postmerge SUCCESS](https://github.com/riccardopinato/Pocket-Guard/actions/runs/41819397260) | Test OEM multipli, falsi positivi, consumo, FGS/lifecycle e nuova revisione se il segnale diventa decisionale |

**Smart Inbox — collegamento vicino ma distinto:** [Notes PR #54](https://github.com/riccardopinato/Notes-Ecosistema/pull/54), merged `ab254e7a8927778498bc3035d1b97bf21d323fcc`, aggiunge anteprima source-backed dei candidati espliciti e apertura dell'editor canonico; non costituisce un writer TF-IDF Smart Inbox completo né applica automaticamente tag. La verifica sull'unione effettiva #56 + #54 è la [CI di main](https://github.com/riccardopinato/Notes-Ecosistema/actions/runs/41822558551), il cui risultato va verificato indipendentemente dai due CI di PR.

**Pocket hardware:** la [PR #7](https://github.com/riccardopinato/Pocket-Guard/pull/7), main `dcec7d82e374e955f1e06c2c8d0a9143c418b6d7`, ha aggiunto un [protocollo di QA fisico con 15 scenari](https://github.com/riccardopinato/Pocket-Guard/blob/main/docs/CAP0158_PHYSICAL_SENSOR_QA_2026-11-04.md), con [CI postmerge SUCCESS](https://github.com/riccardopinato/Pocket-Guard/actions/runs/41822147632). Il protocollo **non** è esecuzione fisica.

**Ledger centrale:** [App-Factory-Core PR #69](https://github.com/riccardopinato/App-Factory-Core/pull/69), merged `0ce46d07993287711edf5156bdfe48ea98296871`; [registro delle prove](https://github.com/riccardopinato/App-Factory-Core/blob/main/evidence/ML23_CONSUMER_EVIDENCE_LEDGER_2026-11-04.md). [Issue #68](https://github.com/riccardopinato/App-Factory-Core/issues/68) mantiene i gate E5, fisici e di promozione.

**Stati invariati:** le tre CAP rimangono `PROPOSTA` a livello app, finché la validazione specifica richiesta non è completa. Nessuna promozione Golden, nessuna modifica di punteggi, delle 160 CAP, delle 385 associazioni o del Golden Index v28.
