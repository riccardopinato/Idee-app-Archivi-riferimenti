# App Factory — M1 35-repository scan + real retry (11/11/2026)

**Status:** `35/35 STATIC_CONFIG_VERIFIED` · `5/5 LIVE_PUSH_CANARY` · `1/35 BOT_PR_CREATION_VERIFIED` · `0/35 CONTEXT_SCHEDULE_VERIFIED` · `0/35 CONTEXT_DISPATCH_VERIFIED` · `ADMIN_CHANGE_BLOCKED`.
**Factory baseline pinned:** `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619`; Master v27; Golden Index v29.
**Earlier evidence:** [first five real canaries and btrader E2E](EVIDENCE_M1_CONTEXT_SYNC_CANARY_2026-11-11.md).

## 1. Repository inventory — current default-branch workflow source
- Read live GitHub owner inventory: **35 repositories** (32 public, 3 private). None archived at audit time; all have a default branch.
- Fetched the canonical workflow on the **default branch** of every repository: `app-factory-context.yml` on 32; `context-snapshot.yml` on the original Agent/Finance/Interactive trio.
- All 35 include an enabled YAML `schedule` trigger, `workflow_dispatch`, and the declared `pull-requests: write` job or workflow permission. This is **static source inspection**, not proof that GitHub's admin permission allows the bot to create PRs.
- Queried GitHub Actions REST events `event=schedule` and `event=workflow_dispatch` for all 35 repositories, **filtering results by the exact context snapshot workflow name**. No actual context-snapshot `schedule` or `workflow_dispatch` run was found as of this audit. Other unrelated scheduled/manual workflows exist in several repos; they do not count.
- Queried open PRs targeting the context bot branch in all 35: one real GitHub Actions bot-created PR, [btrader #5](https://github.com/riccardopinato/btrader/pull/5), while the others have no bot PR open. Closed/merged historical bot PRs were not exhaustively audited.
- No runtime canary was dispatched in the **other 30** repositories: their bot-create capability and any subsequent recovery remain `NOT_VERIFIED`. Do not extrapolate the public btrader success to 35/35.

## 2. Public-repository source inventory (32 of 35)

Columns: **Cron** = configured daily local UTC scheduler specification; `schedule`/`dispatch` columns count **observed runs of the context workflow**, not all repo workflows. `PR bot` = open PR authored by `github-actions[bot]` from the expected branch. Each workflow source also has dispatch and write permission declared.

| Public repository | Workflow | Cron | Context schedule runs | Context manual runs | Open PR bot |
|---|---|---|---|---|---|
| [1000-AI-collection-tools](https://github.com/riccardopinato/1000-AI-collection-tools) | v2 | 05:09 UTC | 0 | 0 | — |
| [180FlipCharge](https://github.com/riccardopinato/180FlipCharge) | v2 | 04:13 UTC | 0 | 0 | — |
| [Adaptive-Landscape-Android](https://github.com/riccardopinato/Adaptive-Landscape-Android) | v2 | 06:22 UTC | 0 | 0 | — |
| [Agenda-per-Anna](https://github.com/riccardopinato/Agenda-per-Anna) | v2 | 07:35 UTC | 0 | 0 | — |
| [Analisi-delle-mie-stelle-github](https://github.com/riccardopinato/Analisi-delle-mie-stelle-github) | v2 | 05:48 UTC | 0 | 0 | — |
| [Android-Omni-Cleaner](https://github.com/riccardopinato/Android-Omni-Cleaner) | v2 | 07:11 UTC | 0 | 0 | — |
| [App-corpo-umano](https://github.com/riccardopinato/App-corpo-umano) | v2 | 08:22 UTC | 0 | 0 | — |
| [App-Factory-Agent-Core](https://github.com/riccardopinato/App-Factory-Agent-Core) | originale | 05:17 UTC | 0 | 0 | — |
| [App-Factory-Core](https://github.com/riccardopinato/App-Factory-Core) | v2 | 09:33 UTC | 0 | 0 | — |
| [app-fotografia](https://github.com/riccardopinato/app-fotografia) | v2 | 07:44 UTC | 0 | 0 | — |
| [AppLab](https://github.com/riccardopinato/AppLab) | v2 | 04:17 UTC | 0 | 0 | — |
| [Battery_Guard](https://github.com/riccardopinato/Battery_Guard) | v2 | 05:28 UTC | 0 | 0 | — |
| [btrader](https://github.com/riccardopinato/btrader) | v2 | 06:39 UTC | 0 | 0 | [#5](https://github.com/riccardopinato/btrader/pull/5) |
| [CamperBoss](https://github.com/riccardopinato/CamperBoss) | v2 | 04:50 UTC | 0 | 0 | — |
| [Design-App](https://github.com/riccardopinato/Design-App) | v2 | 07:26 UTC | 0 | 0 | — |
| [Finance-Intelligence-Agent](https://github.com/riccardopinato/Finance-Intelligence-Agent) | originale | 05:17 UTC | 0 | 0 | — |
| [FocuSense](https://github.com/riccardopinato/FocuSense) | v2 | 06:48 UTC | 0 | 0 | — |
| [Idee-app-Archivi-riferimenti](https://github.com/riccardopinato/Idee-app-Archivi-riferimenti) | v2 | 09:24 UTC | 0 | 0 | — |
| [In-Cucina-con-gli-Anime](https://github.com/riccardopinato/In-Cucina-con-gli-Anime) | v2 | 10:35 UTC | 0 | 0 | — |
| [Interactive-Scene-Core](https://github.com/riccardopinato/Interactive-Scene-Core) | originale | 05:17 UTC | 0 | 0 | — |
| [Neon-arcade-runner](https://github.com/riccardopinato/Neon-arcade-runner) | v2 | 08:46 UTC | 0 | 0 | — |
| [Notes-Ecosistema](https://github.com/riccardopinato/Notes-Ecosistema) | v2 | 07:21 UTC | 0 | 0 | — |
| [Notification-Control](https://github.com/riccardopinato/Notification-Control) | v2 | 08:32 UTC | 0 | 0 | — |
| [PDF-Unifier](https://github.com/riccardopinato/PDF-Unifier) | v2 | 09:43 UTC | 0 | 0 | — |
| [Phone-Guard](https://github.com/riccardopinato/Phone-Guard) | v2 | 07:54 UTC | 0 | 0 | — |
| [Pocket-Guard](https://github.com/riccardopinato/Pocket-Guard) | v2 | 05:27 UTC | 0 | 0 | — |
| [Send-to-pc](https://github.com/riccardopinato/Send-to-pc) | v2 | 06:38 UTC | 0 | 0 | — |
| [Tabletop-Motion-Alarm](https://github.com/riccardopinato/Tabletop-Motion-Alarm) | v2 | 07:49 UTC | 0 | 0 | — |
| [TasteAI](https://github.com/riccardopinato/TasteAI) | v2 | 05:02 UTC | 0 | 0 | — |
| [TrailPath](https://github.com/riccardopinato/TrailPath) | v2 | 06:33 UTC | 0 | 0 | — |
| [Wonderlog](https://github.com/riccardopinato/Wonderlog) | v2 | 07:44 UTC | 0 | 0 | — |
| [World-Days](https://github.com/riccardopinato/World-Days) | v2 | 08:55 UTC | 0 | 0 | — |

**Three private repositories:** workflow files and `schedule`/`workflow_dispatch` declarations observed on all three default branches; zero context workflow runs; no bot PR. Their names, paths and exact cron details are excluded from this **public** evidence record. One of the three was a live canary and failed PR creation due admin setting; the other two were **source-only inspected**.

## 3. Real reruns of four previously blocked canaries

| Canary | Live Actions rerun attempt=2 | Real status | Root cause |
|---|---|---|---|
| 180FlipCharge | [43040857811](https://github.com/riccardopinato/180FlipCharge/actions/runs/43040857811) | **FAIL** after branch pushed | `GraphQL: GitHub Actions is not permitted to create or approve pull requests` |
| Private test repo | Private run previously recorded; URL not published here | **FAIL** after branch pushed | Same `createPullRequest` administrative restriction |
| App-Factory-Agent-Core | [43040897071](https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/43040897071) | **FAIL** at `git merge --no-edit` | `Committer identity unknown`: bot `git config` occurred after merge |
| World-Days | [43041253853](https://github.com/riccardopinato/World-Days/actions/runs/43041253853) | **FAIL** after branch pushed | Same `createPullRequest` administrative restriction |

Reruns were triggered through authorized GitHub Actions **rerun job** controls. A rerun preserves the original run's event/commit semantics: none of these constitute actual `schedule` or `workflow_dispatch` evidence. The blocked `createPullRequest` state was not circumvented by using a user PAT or weakening branch checks.

## 4. Remediation of discovered merge-identity defect

The same bug existed in all three original workflows, even though Agent Core was the one with observed live failure. Changed only identity placement: `git config user.name` and `git config user.email` are now established **before** the first possible `git merge`.

- [App-Factory-Agent-Core PR #8](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/8) — merged, exact-head CI PASS.
- [Finance-Intelligence-Agent PR #4](https://github.com/riccardopinato/Finance-Intelligence-Agent/pull/4) — merged, exact-head CI PASS.
- [Interactive-Scene-Core PR #4](https://github.com/riccardopinato/Interactive-Scene-Core/pull/4) — merged, exact-head CI PASS.

**Post-fix runtime proof (Agent Core):** [run #43052705998](https://github.com/riccardopinato/App-Factory-Agent-Core/actions/runs/43052705998), real `push` QA canary from [PR #9](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/9). Logs: `Merge made by the 'ort' strategy.`, `CONTEXT_SNAPSHOT_WRITE_PASS`, `CONTEXT_SNAPSHOT_CHECK_PASS`, bot `automation/context-snapshot` branch advanced successfully; only `gh pr create` failed due the independent admin restriction. [PR #10](https://github.com/riccardopinato/App-Factory-Agent-Core/pull/10) then **removed the temporary push trigger** with green CI. Workflow on default branch again includes only `schedule` and `workflow_dispatch`, and the Git identity fix remains.

**Verdict:** merge-identity cause `RUNTIME_FIX_VERIFIED` in Agent Core; same source fix `CI_VERIFIED` but **runtime NOT_VERIFIED** in Finance and Interactive.

## 5. Remaining blockers and next actions

1. **Owner admin UI (unavailable through current GitHub connector):** `Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests → Save` for the four live-failing canary repositories, then confirm scope `contents: write` and `pull-requests: write` stays only in metadata job. Do not enable auto-approval/auto-merge; allowing PR creation does not waive review/check policy.
2. **Re-run after setting change** (or use UI `Actions → Context snapshot → Run workflow`). Confirm an actual bot PR from the existing automation branch, no duplicates, exact-head check pass. Three canaries failed at permissions and Agent Core now reaches the same permission error after the Git merge fix. Re-running again before the admin change only repeats the failure.
3. **Cron verification next eligible day:** scheduled times are in **UTC**; next candidate day after this afternoon deployment is **12 Nov 2026**, with the latest among public cron schedules `10:35 UTC`. GitHub warns scheduled jobs can be delayed/dropped; absence of a run after a configured cron does not imply the job ran successfully. Check after the daily window, separating `event=schedule` from other workflows.
4. **Rest of fleet:** after admin permission audit, perform real `workflow_dispatch` canaries on additional representative repositories (including private and different branch policies) without temporary push commits where a GitHub actor with Actions write can dispatch. The connected GitHub tool currently lacks `workflow_dispatch` and administration mutation.
5. **Background followup not scheduled:** a one-shot ChatGPT automation was attempted for 12 Nov but rejected with `too_many_active_automations` (5/5 active). No existing task was modified or cancelled. Until capacity/authorization changes, no future autonomous verification is promised.

## Gate decisions
- `STATIC_35_OF_35 = PASS` — observed canonical workflow source and trigger syntax.
- `REAL_PUSH_SNAPSHOT_5_OF_5 = PASS`; `BOT_PR_CREATED = PASS` on btrader alone.
- `IDENTITY_MERGE_RUNTIME = PASS` on Agent Core after fix; Finance/Scene only exact-head CI PASS.
- `PR_CREATE_PERMISSION_FLEET = BLOCKED / UNKNOWN`; four original canaries still **not** green E2E until admin UI change.
- `SCHEDULE / WORKFLOW_DISPATCH_RUNTIME = NOT_VERIFIED` on all 35 as of 11 Nov; no claim of complete autonomy, device verification, Golden certification or agent runtime.
