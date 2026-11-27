# Living Index — current project status

**Updated:** 2026-11-27 · **Status scope:** public GitHub repository `martynio/LivingIndex`

## Current snapshot

- **Product stage:** LI-003A static shell authorized for main-based development preview on 2026-11-27; 24 pages plus root entry; operator reported preview satisfactory; full browser acceptance and production release pending. LI-003B preview transparency accepted and merged via PR #11 at `2ee65ee727c0c5f54ffaec8ec97c60212d9b6607`; LI-004A catalogue implemented on review branch.
- **LI-001 — Governance & Roadmap:** **ACCEPTED / GATE CLOSED** by explicit operator decision on 2026-11-09.
- **Verified accepted merge checkpoint:** [`2192e95f331aaafab8ee2a10adb217cc7ae2f85b`](https://github.com/martynio/LivingIndex/commit/2192e95f331aaafab8ee2a10adb217cc7ae2f85b) on `main`, via [merged PR #1](https://github.com/martynio/LivingIndex/pull/1).
- **Closure audit:** this status, the roadmap, `WORK_LOG`, `HANDOFF` and ADR-0001 were updated in a separate, reviewable documentation-only closeout change. Consult `main` HEAD and PR history for the subsequent closeout commit; the accepted LI-001 implementation baseline is the merge SHA above.
- **Current stage:** **LI-002 — Source Registry & Legal Research**. The first official-source discovery tranche was accepted and merged through [PR #3](https://github.com/martynio/LivingIndex/pull/3), with verified `main` checkpoint [`229062bf`](https://github.com/martynio/LivingIndex/commit/229062bfbd7183399ec10f1762680b5a550d25c9). **The full LI-002 numerical-feasibility and operator gate remains open.**
- **Project Proposal:** [LI-PP-001 v1.0](LI-PP-001-PROJECT-PROPOSAL-v1.0.md) remains a project proposal; accepting governance does not automatically authorize product implementation.
- **Application code:** static HTML/CSS shell with root preview entry; LI-004A review branch adds one local filter script. No backend or data engine.
- **LI-002 HBS proof and runner:** [PR #4](https://github.com/martynio/LivingIndex/pull/4) established the proof contract. [PR #5](https://github.com/martynio/LivingIndex/pull/5) was explicitly approved and merged as [`74ac245`](https://github.com/martynio/LivingIndex/commit/74ac245412c9df800720e34875affd7209bd9f2c). The manual HBS workflow successfully executed on 2026-11-24; [run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068).
- **Accepted research checkpoint:** [PR #7](https://github.com/martynio/LivingIndex/pull/7) merged, verified main `e389573c34c88c3772b0c56701360bedf979a148`. Research-only pair accepted as evidence, not production data.
- **Accepted matrix checkpoint:** [PR #8](https://github.com/martynio/LivingIndex/pull/8) merged at [`c812480`](https://github.com/martynio/LivingIndex/commit/c8124808c8d57b3973c17362593922b6826e3713). [Hosted regression](https://github.com/martynio/LivingIndex/actions/runs/45439673111): 17/17 PASS; 24-cell manual retrieval NOT RUN. Fourteen source candidates registered; production methodology and rights remain open.
- **Accepted website dependency decision:** [ADR-0002](../decisions/ADR-0002-PARALLEL-SHELL-RESEARCH.md). [LI-003 Website Foundation scope](LI-003-WEBSITE-FOUNDATION-SCOPE.md) is approved for LI-003A development preview on main under the 2026-11-27 operator amendment; legal approval and production release are not authorized. Pages run records confirm the existing github.io address; current settings cannot be edited through the connector.
- **Validated production datasets:** none. First research-only PL/NL CP01/PPS_HH observations retrieved via HTTP 200; [run evidence](../research/HBS_2020_RUN_002_EVIDENCE.md). Network blocker resolved on hosted runner; methodological and independent cell verification remain open.
- **Automated CI / application tests:** local shell verifier added; static pass, browser gate unresolved. No new workflow. Both HBS research suites passed **17/17** in [PR #8 hosted regression](https://github.com/martynio/LivingIndex/actions/runs/45439673111). Earlier CP01 manual run succeeded; matrix live retrieval has not run.

## Gate register

| Gate | State | Evidence / next requirement |
| --- | --- | --- |
| LI-001 documentation quality | **PASS** | Verified 14 PR files; post-review link/path checks passed; proposal unchanged |
| LI-001 operator approval and merge | **CLOSED / ACCEPTED** | Explicit operator approval, [PR #1 merged](https://github.com/martynio/LivingIndex/pull/1), `main` HEAD verified at `2192e95` following merge |
| LI-001 closure documentation | **RECORDED** | `ROADMAP`, `PROJECT_STATUS`, `WORK_LOG`, `HANDOFF`, ADR-0001 updated in a dedicated closeout |
| LI-002 initial metadata/rights research | **ACCEPTED / CHECKPOINTED** | [PR #3](https://github.com/martynio/LivingIndex/pull/3), merge `229062bf`; 11 source leads, no accepted numeric observations |
| LI-002 manual HBS probe | **PASS / ACCEPTED EVIDENCE** | [Run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068) completed successfully; artifact digest verified; [PR #7](https://github.com/martynio/LivingIndex/pull/7) merged at `e389573` |
| LI-002 matrix implementation | **ACCEPTED / CHECKPOINTED** | PR #8, merge `c812480`; 17/17 hosted tests; live matrix job intentionally skipped on PR |
| LI-003 non-data shell | **IMPLEMENTED / MAIN PREVIEW AUTHORIZED; BROWSER REVIEW OPEN** | [LI-003A verification](LI-003A-VERIFICATION.md); operator acceptance, browser evidence and publication remain separate gates |
| LI-002 numerical feasibility | **PARTIAL EVIDENCE / OPEN** | One CP01 research pair retrieved; [evidence](../research/HBS_2020_RUN_002_EVIDENCE.md); official browser reconciliation, household definitions, production rights and compatible income/hours remain open |
| GitHub Actions activity | **HBS SUCCESS** | [Run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068); Node.js 20 action deprecation warning recorded for future maintenance; unrelated Pages runs do not establish statistical validation |
| LI-004A source metadata explorer | **IMPLEMENTED / REVIEW OPEN** | [LI-004A review](LI-004A-SOURCES-EXPLORER.md); 13 eligible source cards per language; browser test pending |
| Publication/legal readiness | **PARTIAL / REVIEW OPEN** | [LI-003B preview transparency](LI-003B-PREVIEW-TRANSPARENCY.md); PR #11 accepted as preview information; controller/contact and observed browser processing still open |

## Handoff

Read [AGENTS.md](../../AGENTS.md), [ROADMAP](ROADMAP.md), [WORK_LOG](../logs/WORK_LOG.md) and the [latest handoff](../logs/HANDOFF.md). Before each iteration, independently verify Git HEAD, relevant PRs, current files and open gates.

**Operator amendment (2026-11-27):** merge LI-003A shell into main for development preview, without treating the merge as completion of browser acceptance or production release. LI-002 remains open; no legal-policy approval or numerical economic claims. See [verification](LI-003A-VERIFICATION.md).
