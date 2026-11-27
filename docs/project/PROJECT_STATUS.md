# Living Index — current project status

**Updated:** 2026-11-27 · **Status scope:** public GitHub repository `martynio/LivingIndex`

## Current snapshot

- **Product stage:** LI-003A static shell authorized for main-based development preview on 2026-11-27; 24 pages plus root entry; operator reported preview satisfactory; full browser acceptance and production release pending. LI-003B preview transparency accepted and merged via PR #11 at `2ee65ee727c0c5f54ffaec8ec97c60212d9b6607`; LI-004A catalogue accepted as development preview and merged via [PR #12](https://github.com/martynio/LivingIndex/pull/12) at `9c30a8f8989d0ca439ce33451c6cfb75821c937c`; LI-005A accepted via PR #13 at `b5af5cfbbd438eb6363d724819ccdcccdf072c40`; LI-005B evidence accepted via PR #14 at `3465b1eed6233e7a5979bac8118f710ee5e67090`; LI-005C accepted via PR #15 at `7271543950ef610e9c663cbd67758bd19c90173e`; LI-006A dashboard accepted as development preview via PR #16 at `2c23e25fbba129513f7ebd7419b75b142cdf7673`; LI-006B descriptive CBS version accepted by operator; PR #17 acceptance checkpoint prepared.
- **LI-001 — Governance & Roadmap:** **ACCEPTED / GATE CLOSED** by explicit operator decision on 2026-11-09.
- **Verified accepted merge checkpoint:** [`2192e95f331aaafab8ee2a10adb217cc7ae2f85b`](https://github.com/martynio/LivingIndex/commit/2192e95f331aaafab8ee2a10adb217cc7ae2f85b) on `main`, via [merged PR #1](https://github.com/martynio/LivingIndex/pull/1).
- **Closure audit:** this status, the roadmap, `WORK_LOG`, `HANDOFF` and ADR-0001 were updated in a separate, reviewable documentation-only closeout change. Consult `main` HEAD and PR history for the subsequent closeout commit; the accepted LI-001 implementation baseline is the merge SHA above.
- **Current stage:** **LI-002 — Source Registry & Legal Research**. The first official-source discovery tranche was accepted and merged through [PR #3](https://github.com/martynio/LivingIndex/pull/3), with verified `main` checkpoint [`229062bf`](https://github.com/martynio/LivingIndex/commit/229062bfbd7183399ec10f1762680b5a550d25c9). **The full LI-002 numerical-feasibility and operator gate remains open.**
- **Project Proposal:** [LI-PP-001 v1.0](LI-PP-001-PROJECT-PROPOSAL-v1.0.md) remains a project proposal; accepting governance does not automatically authorize product implementation.
- **Application code:** static HTML/CSS shell with root preview entry; LI-004A adds one local filter script on main; LI-005A adds offline research adapter on main, not a production data engine. LI-005C adds offline simulation/research calculation primitives on main; LI-006A adds a local dashboard on main; LI-006B stages two source-verified descriptive values. No backend.
- **LI-002 HBS proof and runner:** [PR #4](https://github.com/martynio/LivingIndex/pull/4) established the proof contract. [PR #5](https://github.com/martynio/LivingIndex/pull/5) was explicitly approved and merged as [`74ac245`](https://github.com/martynio/LivingIndex/commit/74ac245412c9df800720e34875affd7209bd9f2c). The manual HBS workflow successfully executed on 2026-11-24; [run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068).
- **Accepted research checkpoint:** [PR #7](https://github.com/martynio/LivingIndex/pull/7) merged, verified main `e389573c34c88c3772b0c56701360bedf979a148`. Research-only pair accepted as evidence, not production data.
- **Accepted matrix checkpoint:** [PR #8](https://github.com/martynio/LivingIndex/pull/8) merged at [`c812480`](https://github.com/martynio/LivingIndex/commit/c8124808c8d57b3973c17362593922b6826e3713). [Hosted regression](https://github.com/martynio/LivingIndex/actions/runs/45439673111): 17/17 PASS; [24-cell manual retrieval](https://github.com/martynio/LivingIndex/actions/runs/46032585277) PASS; [matrix evidence](../research/HBS_2020_MATRIX_RUN_EVIDENCE.md). Fifteen source records registered; production methodology and rights remain open.
- **Accepted website dependency decision:** [ADR-0002](../decisions/ADR-0002-PARALLEL-SHELL-RESEARCH.md). [LI-003 Website Foundation scope](LI-003-WEBSITE-FOUNDATION-SCOPE.md) is approved for LI-003A development preview on main under the 2026-11-27 operator amendment; legal approval and production release are not authorized. Pages run records confirm the existing github.io address; current settings cannot be edited through the connector.
- **Validated production datasets:** none. All 24 research-only PL/NL CP01–CP12/PPS_HH observations retrieved via HTTP 200 and normalized; [matrix evidence](../research/HBS_2020_MATRIX_RUN_EVIDENCE.md). Network blocker resolved on hosted runner; methodological and independent cell verification remain open.
- **Automated CI / application tests:** local shell verifier added; static pass, browser gate unresolved. No new workflow. Both HBS research suites passed **17/17** in [PR #8 hosted regression](https://github.com/martynio/LivingIndex/actions/runs/45439673111). Latest matrix run: 17/17 hosted HBS regression PASS, 13/13 local adapter tests PASS; actual 24-cell replay PASS.

## Gate register

| Gate | State | Evidence / next requirement |
| --- | --- | --- |
| LI-001 documentation quality | **PASS** | Verified 14 PR files; post-review link/path checks passed; proposal unchanged |
| LI-001 operator approval and merge | **CLOSED / ACCEPTED** | Explicit operator approval, [PR #1 merged](https://github.com/martynio/LivingIndex/pull/1), `main` HEAD verified at `2192e95` following merge |
| LI-001 closure documentation | **RECORDED** | `ROADMAP`, `PROJECT_STATUS`, `WORK_LOG`, `HANDOFF`, ADR-0001 updated in a dedicated closeout |
| LI-002 initial metadata/rights research | **ACCEPTED / CHECKPOINTED** | [PR #3](https://github.com/martynio/LivingIndex/pull/3), merge `229062bf`; 11 source leads, no accepted numeric observations |
| LI-002 manual HBS probe | **PASS / ACCEPTED EVIDENCE** | [Run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068) completed successfully; artifact digest verified; [PR #7](https://github.com/martynio/LivingIndex/pull/7) merged at `e389573` |
| LI-002 matrix implementation | **ACCEPTED / CHECKPOINTED** | PR #8, merge `c812480`; 17/17 hosted tests; subsequent manual run 46032585277 PASS, all 24 cells present |
| LI-003 non-data shell | **IMPLEMENTED / MAIN PREVIEW AUTHORIZED; BROWSER REVIEW OPEN** | [LI-003A verification](LI-003A-VERIFICATION.md); operator acceptance, browser evidence and publication remain separate gates |
| LI-002 numerical feasibility | **PARTIAL EVIDENCE / OPEN** | 24 research cells retrieved and normalized; [matrix evidence](../research/HBS_2020_MATRIX_RUN_EVIDENCE.md); official browser reconciliation, household definitions, production rights and compatible income/hours remain open |
| GitHub Actions activity | **HBS SUCCESS** | [Run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068); Node.js 20 action deprecation warning recorded for future maintenance; unrelated Pages runs do not establish statistical validation |
| LI-004A source metadata explorer | **PREVIEW ACCEPTED / BROWSER REVIEW OPEN** | [LI-004A review](LI-004A-SOURCES-EXPLORER.md); 14 eligible source cards per language; browser test pending |
| LI-005A research data contract | **ACCEPTED / CHECKPOINTED** | [LI-005A contract](LI-005A-RESEARCH-DATA-CONTRACT.md); 13/13 local tests, real CP01 replay PASS, zero approved datasets |
| LI-005B national budget evidence | **ACCEPTED RESEARCH / PRODUCTION OPEN** | [Evidence](../research/LI-005B-NATIONAL-BUDGET-EVIDENCE.md); GUS/CBS official figures located, no compatible production inputs; HBS matrix complete; source reconciliation and production eligibility open |
| LI-005C economic engine | **ACCEPTED / CHECKPOINTED** | [Contract](LI-005C-ECONOMIC-ENGINE.md); 29/29 local tests and 12/12 actual PPS pairs; monetary/time inputs hypothetical only |
| LI-006A development dashboard | **PREVIEW ACCEPTED / BROWSER REVIEW OPEN** | [Contract](LI-006A-DASHBOARD-PREVIEW.md); 27 pages, 22 arithmetic + 39 mock-DOM assertions, 500 parity cases; browser gate open, no approved figures |
| LI-006B first descriptive dataset | **DESCRIPTIVE PREVIEW ACCEPTED** | [CBS candidate](LI-006B-CBS-DESCRIPTIVE-PREVIEW.md); two final 2020 values, three locale displays; no production calculation eligibility |
| Publication/legal readiness | **PARTIAL / REVIEW OPEN** | [LI-003B preview transparency](LI-003B-PREVIEW-TRANSPARENCY.md); PR #11 accepted as preview information; controller/contact and observed browser processing still open |

## Handoff

Read [AGENTS.md](../../AGENTS.md), [ROADMAP](ROADMAP.md), [WORK_LOG](../logs/WORK_LOG.md) and the [latest handoff](../logs/HANDOFF.md). Before each iteration, independently verify Git HEAD, relevant PRs, current files and open gates.

**Operator amendment (2026-11-27):** merge LI-003A shell into main for development preview, without treating the merge as completion of browser acceptance or production release. LI-002 remains open; no legal-policy approval or numerical economic claims. See [verification](LI-003A-VERIFICATION.md).
