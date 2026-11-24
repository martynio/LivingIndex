# Living Index — latest contributor handoff

**Updated:** 2026-11-24 · **State:** LI-002 research continues; ADR-0002 accepted; LI-003 scope proposed, implementation not started.

## Verified accepted checkpoint

- [PR #8](https://github.com/martynio/LivingIndex/pull/8) merged/closed at [`c8124808c8d57b3973c17362593922b6826e3713`](https://github.com/martynio/LivingIndex/commit/c8124808c8d57b3973c17362593922b6826e3713), verified on main with correct parents.
- [Hosted offline run](https://github.com/martynio/LivingIndex/actions/runs/45439673111) passed 17/17 tests; live matrix job skipped as designed. No new economic observations or production data.
- [ADR-0002](../decisions/ADR-0002-PARALLEL-SHELL-RESEARCH.md) accepted. The administrative closeout may follow the merge; always read current main.
- [LI-003 Website Foundation scope](../project/LI-003-WEBSITE-FOUNDATION-SCOPE.md) proposes A: static shell, B: legal/hosting readiness, C: publication. Only scope preparation was requested; A needs separate approval. No HTML or deployment change.

## Two independent next steps

- Research: manually dispatch [LI-002 Eurostat HBS division matrix](https://github.com/martynio/LivingIndex/actions/workflows/li-002-hbs-matrix.yml) on main, inspect artifact, flags and compare CP01; record results. Income/time definitions, methodology and rights remain open.
- Website: review/approve LI-003A; branch-only implementation under web/ using local assets and EN/PL/NL. Actual Pages source path/domain/operator details are unconfirmed; connector Pages settings request unavailable. Do not merge deployable pages to publishing branch or change settings before B/C review and explicit publication approval.

Read [AGENTS](../../AGENTS.md), [status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [matrix guide](../research/HBS_DIVISION_MATRIX.md), [legal research](../research/LEGAL_RESEARCH.md), [work log](WORK_LOG.md). Never use unverified observations or legal assumptions as production facts.
