# App Factory 10x — Six-step parallel execution checkpoint

Date: 12 November 2026. Factory baseline `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`, Master v27 / Index v29.

## Actual technical artifacts and remaining gates

| Task | Current execution artifact | Boundary / reason not marked VERIFIED |
| --- | --- | --- |
| **X10-026** two Flutter consumers | [Anna's Diary PR #307](https://github.com/riccardopinato/Agenda-per-Anna/pull/307); [CamperBoss PR #33](https://github.com/riccardopinato/CamperBoss/pull/33) **DRAFT** | Source-level kit profile v0.1.0 pinned to `Idee-app-Archivi-riferimenti@1d1a8628e25f58b788b013cf6955763d00363cdc`. Anna uses Git dependency; CamperBoss preserves strict hosted-only supply-chain policy and uses a pinned internal source copy. Both tests are consumers of the actual Dart module, but no live UI/store integration, real rollback, device validation or Golden admission. Do not merge CamperBoss before its blocked STEP16 roadmap gate is resolved. |
| **X10-032** physical / Play | [AppLab #230](https://github.com/riccardopinato/AppLab/pull/230) | PLAN_ONLY scenario contract bound to source, APK SHA, signer, version and prior-version baseline; no device attached or Play evidence obtained. Reuse canonical AppLab physical_evidence.py; HUMAN_GATE remains open. |
| **X10-035** 2–3 product + budget decision | [owner decision JSON](X10-035_OWNER_DECISION_PROPOSAL.json) and [documented shortlist](X10-035_036_DECISION_AND_ANALYTICS_PROPOSAL.md) | Battery Guard + Rotate 180° suggested, World Days conditional; `owner_approved=false` and `approved_budget_eur=null`. No spending, product decision, release or price change. Owner must expressly select 2–3 products and budget. |
| **X10-036** privacy-first analytics | [privacy_metrics Dart kit](flutter_kits/privacy_metrics/README.md), merged via [archive #147](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti/pull/147) | Prototype opt-in in-memory counters, zero network/identifiers; no actual retention, unique users, attributable conversion, hosted provider, app integration or independent consent/legal approval. X10-035 decision is prerequisite. |
| **X10-046** feature A real agent pilot | [Agent Core #23](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/23) | Merged source gate for provenance / draft PR / QA. Agent Windows source X10-008 remains unavailable; no real worker run or human product approval. AppLab SELF_CANARY is the proposed safe first target only. |
| **X10-047** feature B other repo pilot | same Agent Core #23 plus [two-repo handoff](https://github.com/riccardopinato/App-Factory-Agent-Core/blob/main/docs/X10-046_047_TWO_REPO_PILOT_HANDOFF.md) | Must use a different authorized repository after actual feature-A accepted, with real independent worker/PR tests and recovery. World-Days is only a proposed second target, not yet authorized for agent rollout. |

## Required sequence and independent lanes
1. **Consumer lane** — finish exact-head CI/Codex on Anna #307 and CamperBoss #33; keep latter DRAFT while its roadmap blocks. Capture full dependency supply-chain and rollback evidence before X10-026 promotion.
2. **QA lane** — merge AppLab #230 only after its seven required workflows and Codex review; then obtain actual same-APK physical hub and Play Console Internal Testing evidence. No fake physical PASS.
3. **Commercial lane** — ask owner to approve product IDs / budget, then record a separate gated decision PR. Only then enable an actual consent-first analytics design in selected products; the current kit does not satisfy full retention/attribution.
4. **Agent lane** — acquire sanitized Windows source/approval X10-008, perform authenticated local X10-015 runner recovery proof; run A and B actual bounded draft-PR tasks with independent review and separate human acceptance.

## Honest progress accounting
**Do not promote these six tasks to VERIFIED merely because the source preparation PRs are green.** Release/device gates, investor/budget owner decision, real pilot outcomes and signed artifact verification are outside synthetic CI. Preserve 34/57 existing source+CI verified counts unless subsequent genuine task-specific admission gates are passed.
