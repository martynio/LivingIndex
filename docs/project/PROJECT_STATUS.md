# Living Index — current project status

**Updated:** 2026-11-10 · **Status scope:** public GitHub repository `martynio/LivingIndex`

## Current snapshot

- **Product stage:** planning / research preparation; no deployed application.
- **LI-001 — Governance & Roadmap:** **ACCEPTED / GATE CLOSED** by explicit operator decision on 2026-11-09.
- **Verified accepted merge checkpoint:** [`2192e95f331aaafab8ee2a10adb217cc7ae2f85b`](https://github.com/martynio/LivingIndex/commit/2192e95f331aaafab8ee2a10adb217cc7ae2f85b) on `main`, via [merged PR #1](https://github.com/martynio/LivingIndex/pull/1).
- **Closure audit:** this status, the roadmap, `WORK_LOG`, `HANDOFF` and ADR-0001 were updated in a separate, reviewable documentation-only closeout change. Consult `main` HEAD and PR history for the subsequent closeout commit; the accepted LI-001 implementation baseline is the merge SHA above.
- **Current stage:** **LI-002 — Source Registry & Legal Research**. A narrow first-pass official-source discovery has started from the accepted LI-001 checkpoint. Its documents are proposed on a review branch; **the full LI-002 data-feasibility/decision gate remains open**.
- **Project Proposal:** [LI-PP-001 v1.0](LI-PP-001-PROJECT-PROPOSAL-v1.0.md) remains a project proposal; accepting governance does not automatically authorize product implementation.
- **Application code:** none; web directories remain placeholders.
- **Validated economic datasets:** none. First-pass publisher metadata and source leads do **not** constitute validated dataset observations.
- **Automated CI / application tests:** no configured application test suite.

## Gate register

| Gate | State | Evidence / next requirement |
| --- | --- | --- |
| LI-001 documentation quality | **PASS** | Verified 14 PR files; post-review link/path checks passed; proposal unchanged |
| LI-001 operator approval and merge | **CLOSED / ACCEPTED** | Explicit operator approval, [PR #1 merged](https://github.com/martynio/LivingIndex/pull/1), `main` HEAD verified at `2192e95` following merge |
| LI-001 closure documentation | **RECORDED** | `ROADMAP`, `PROJECT_STATUS`, `WORK_LOG`, `HANDOFF`, ADR-0001 updated in a dedicated closeout |
| LI-002 source feasibility | **IN PROGRESS / REVIEW PENDING** | Review official source registry and legal research; validate country-level datasets, matched net/hours scenario, and rights before full gate |
| Publication/legal readiness | **NOT ESTABLISHED** | Verify hosting, data processing, telemetry, source rights and attribution before any public policy claims |

## Handoff

Read [AGENTS.md](../../AGENTS.md), [ROADMAP](ROADMAP.md), [WORK_LOG](../logs/WORK_LOG.md) and the [latest handoff](../logs/HANDOFF.md). Before each iteration, independently verify Git HEAD, relevant PRs, current files and open gates.

**Acceptance of LI-001 closes only the governance stage.** It authorizes no LI-003 website implementation, legal-policy publication or numerical data import. LI-002 first-pass research is for separate review and must not be called completed.
