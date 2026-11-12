# X10-045 — recurrent failure → donor candidate feedback, SOURCE+CI evidence

Factory baseline `App-Factory-Core@c5adc147046beb7024629466d10eeb799c3c2619` (Master 27 / Golden Index 29).

[AppLab PR #229](https://github.com/riccardopinato/AppLab/pull/229) squash MERGED `0888d71e3ce163db4af94d9694c34f18b4041ec3`; exact head `e6c1e2e1c1bbc066c3a8f6b4f91e45aeb0f6c6b2`. Seven required workflows completed SUCCESS, independent Codex exact-head review clean, past P1/P2 review discussions resolved.

Code: `scripts/x10_failure_donor_loop.py`, `backend/tests/test_x10_failure_donor_loop.py`, `integration/agent_core/X10-045_FAILURE_DONOR_REPLAY.md`. Thin facade to existing AppLab `pattern3_discovery_v57c` and `factory_feedback_packager_v58d`. Requires at least 3 independently verified distinct run/evidence receipts with same failure signature; binds exact repository/source SHA, test key, category, error code, digest and workflow run; normalizes GitHub repo casing before Pattern-3 classification. Output `PROPOSAL_ONLY`, replay plan `NOT_EXECUTED`, no donor auto-certification or Golden admission.

**BOUNDARY:** unit fixtures + CI validate the contract, NOT real reproduced consumer failures, replay execution, cross-app piloting or verified donor promotion. Live trusted verifier must be injected; any promotion remains a separate gated decision.
