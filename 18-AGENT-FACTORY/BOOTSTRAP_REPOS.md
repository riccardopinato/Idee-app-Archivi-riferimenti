# Blueprint tecnico per i repository dedicati (non ancora creati)
Versione 1 — 2026-11-11

## App-Factory-Agent-Core — IN_ROADMAP
Struttura proposta:
- AGENTS.md — gerarchia policy, limiti e comandi reali
- PRODUCT_BIBLE.md — task engine e consumer
- ROADMAP.md — milestone, gate, dipendenze
- contracts/job.schema.json — request/response; idempotency key; approval
- src/orchestrator/ — state machine, scheduler adapter, checkpoint/retry bounded
- src/adapters/ — read-only GitHub, build/test, gated write
- src/security/ — permissions, secret indirection, allowlist, sandbox
- src/evidence/ — receipt con source SHA e log sanitizzati
- tests/ — idempotenza, crash/restart, timeout, permessi, human gate
- CHANGELOG.md; docs/PROVENANCE.md; evidence/README.md.
Stack: prima verificare il codice Windows/WSL esistente. Non scegliere TypeScript/Python/Rust a priori. Runner persistente esplicito, non una chat.

## Finance-Intelligence-Agent — IN_ROADMAP
Struttura proposta:
- AGENTS.md; PRODUCT_BIBLE.md; ROADMAP.md; CHANGELOG.md
- contracts/market-event.schema.json; contracts/portfolio-position.schema.json
- src/providers/ + providers/LICENSE_AND_FRESHNESS.md
- src/portfolio/ — posizione, operazioni, cost basis e multi-currency
- src/analytics/ — rendimenti, drawdown, allocazione, correlazione, scenario risk
- src/news/ — citations, provenance, timestamps, source quality
- src/alerts/ — threshold, idempotency, cooldown e user authorization
- src/paper/ — simulatore senza ordini reali
- tests/fixtures/synthetic/ — dataset sintetici temporali e corporate action
- docs/SECURITY_AND_REGULATION.md; evidence/.
Design: backend read-only, storage cifrato, portfolio manuale/CSV opzionale, alert con log, nessun broker token obbligatorio. API reali solo dopo audit provider. Trading LIVE DISABILITATO per default e non parte delle milestone approvate.

## Interactive-Scene-Core — CANDIDATE
Struttura proposta:
- AGENTS.md; ROADMAP.md; CHANGELOG.md
- contracts/scene.schema.json — geometria, oggetti, viewport, versionamento
- packages/scene-model/ — modello puro riusabile (valutare lingua effettiva)
- packages/flutter-scene-adapter/ — solo se consumer Flutter reale
- packages/android-scene-renderer/ — Kotlin/GLES/WallpaperService optional
- benchmarks/ — CPU, GPU, RAM, FPS, battery, resolution, frame pacing
- tests/ — coordinate, determinismo, sleep/resume, multi-DPI
- docs/LICENSE_AUDIT.md; docs/PROVENANCE.md; evidence/.
Non estrarre subito: primo step mappa dipendenze ed evidence sul codice Adaptive Landscape; staccare shader acqua da scene core generico. Originale Deskland GPL-3.0 solo reference; non copiare asset/codice.

## Template di aggiornamento obbligatorio
Date | Repo | Main SHA | PR/issue | Modulo | Stato prima/dopo | Test/CI | Device/Provider | Licenza | Consumer | Blocker | Next action.
Tutti i campi di evidenza non osservati devono dire NOT_VERIFIED, mai PASS presunto.
