# Template program — Parallel four-lane execution receipt

**Date:** 2026-11-09. **Factory baseline:** `d4ed1185d36d419228fba6b57a979cde308bd321`.

| Lane | Actual action | Evidence / current boundary | Next gate |
|---|---|---|---|
| P1 Wonderlog Web deploy | **Retry requested** for failed GitHub Pages deploy job `129449160230` on [run #42701619452](https://github.com/riccardopinato/Wonderlog/actions/runs/42701619452), initial failure caused by `syncing_files` status until `actions/deploy-pages@v4` timeout. Exactly the original `c238afd82ca93699d0e0d5d4e3e3a9a0d6d1d9ee` head. | GitHub accepted retry; inspect **attempt 2** conclusion separately. No workflow change, no fabricated deploy success | PASS only after GitHub Pages deploy success + reachable URL on exact SHA. If timeout again, diagnose hosting state/cancel-in-progress/Pages service; open targeted workflow PR only if evidence warrants |
| P1 real template QA | Three independent source regressions and manual matrices: [Notes PR #98](https://github.com/riccardopinato/Notes-Ecosistema/pull/98), [Anna PR #293](https://github.com/riccardopinato/Agenda-per-Anna/pull/293), [Wonderlog PR #27](https://github.com/riccardopinato/Wonderlog/pull/27) | New tests are **in PR, not necessarily merged/passed**; existing Step3/4 CI passes source-only. True account switch, backup on device, notifications and store are NOT VERIFIED | Exact-head CI per app → nonblocking review → merge → main CI. Manual physical evidence remains external/device-dependent |
| P2 donor/Golden | [Provenance ledger](STEP5_DONOR_PROVENANCE_2026-11-09.md) pinning 3 app source SHAs and bounded tests/CI; internal donor mapping, no duplicated store engine | E3 **SCOPED CI**, not E5 consumer. No new CAP, Golden, general cross-app SDK, registry status promotion | Consumer independent proof and artifact/device gates before future Golden extraction/promotion |
| P3 original commercial packs | [Four pack blueprint proposals](BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md): two Notes + two Anna, namespaced IDs, real owner, writer/ACL and test gates | `DESIGN CANDIDATE`, no purchased rights, no SKU, no billing, no premium content app code. €3,99 is merely a price hypothesis | Product + UX review, original asset licensing, adapter proof, store provider sandbox approval separately |

## Exit criteria

- Source/CI closure can be certified without physical proof **only if source checks are exact-HEAD PASS** and code merged.
- Wonderlog Pages retry attempt must not be reported as recovered until server delivery is confirmed; if blocked by hosting, record failure rather than pushing a false code fix.
- Risky manual app-state tests must run on disposable profiles/backup copies, never on the user's real diaries or account.
- The archive is coordinating provenance and roadmap, not inventing a shared purchase/license service. All premium design work is non-shipping.

## Esito verificato — source integration e deploy GitHub Pages

- **Notes:** [PR #98](https://github.com/riccardopinato/Notes-Ecosistema/pull/98) **MERGED** `main@cf9f9c515a87f438ab0112e7efd4a0ce0471fbd6` da PR HEAD `1200e6938933e52e514aa95b72137d6e32d61378`. `verify`, `verify-web`, `build-web` SUCCESS sul PR HEAD. Il test nuovo ha intercettato il `TextEditingController` disposed durante l'uscita dal dialogo Book Tracker: **corretto il codice produzione** usando `TextFormField` gestito dal widget. CI `main` post-merge separata, non inferita.
- **Anna:** [PR #293](https://github.com/riccardopinato/Agenda-per-Anna/pull/293) **MERGED** `main@260dd753a3f7d1b7cd501ce38cf6e4a78ea773b3` da HEAD `55c8ff2f23c7342ed5b8877f331fef1ba5546f9a`; `check` e `UI5 source and visual-flow contracts` SUCCESS esatti. Branch riallineato con il main Vision Board prima della CI/merge. Test UI dialogo Back→Use. I gate di rilascio indipendenti restano separati.
- **Wonderlog:** [PR #27](https://github.com/riccardopinato/Wonderlog/pull/27) **MERGED** `main@f045588dd5dbd668541fec380f184f3ebcd8bb6f`, HEAD `b53daafee5f6b66cc12b69d78a2b5a20d887619d`, `verify`, `apple-build`, `legacy-contract` SUCCESS. Il Pages [run #42701619452](https://github.com/riccardopinato/Wonderlog/actions/runs/42701619452) è fallito in due tentativi (`syncing_files`/timeout). **RIPRISTINO WORKFLOW**: la nuova [run #42710542583](https://github.com/riccardopinato/Wonderlog/actions/runs/42710542583) su `main@f045588d` ha `build=SUCCESS`, `deploy=SUCCESS` e run SUCCESS. Il contenuto HTTP pubblico e l'effettivo stato PWA/OAuth non sono stati verificati indipendentemente in browser. [Issue #28](https://github.com/riccardopinato/Wonderlog/issues/28) documenta recovery e gate live residuo.
- **Donor/Golden:** il ledger E3 resta **SCOPED SOURCE/CI**, nessun E5 indipendente e nessuna promozione Golden/CAP; i merge QA rafforzano l'evidenza dei tre repo, non attestano dispositivi, provider o riuso di uno stesso pacchetto.
- **Premium:** quattro blueprint su [pagina dedicata](BLUEPRINT_PREMIUM_ORIGINALI_2026-11-09.md) sono `DESIGN CANDIDATE`, non `PRODUCT_APPROVED`; nessun acquisto, SKU, checkout, RevenueCat/PlayStore update né installazioni commerciali.

**BLOCCO RESIDUO FINALE:** scenari manuali account/backup/permessi, real-device e verifica browser Pages pubblico **NOT_VERIFIED**. I lavori sorgente e la documentazione sono **MERGED**; i controlli main post-merge richiedono conferma distinta se ancora in corso.
