# Living Index — current project status

**Updated:** 2026-11-13 · **Status scope:** public GitHub repository `martynio/LivingIndex`

## Current snapshot

- **Product stage:** planning / research preparation; no deployed application.
- **LI-001 — Governance & Roadmap:** **ACCEPTED / GATE CLOSED** by explicit operator decision on 2026-11-09.
- **Verified accepted merge checkpoint:** [`2192e95f331aaafab8ee2a10adb217cc7ae2f85b`](https://github.com/martynio/LivingIndex/commit/2192e95f331aaafab8ee2a10adb217cc7ae2f85b) on `main`, via [merged PR #1](https://github.com/martynio/LivingIndex/pull/1).
- **Closure audit:** this status, the roadmap, `WORK_LOG`, `HANDOFF` and ADR-0001 were updated in a separate, reviewable documentation-only closeout change. Consult `main` HEAD and PR history for the subsequent closeout commit; the accepted LI-001 implementation baseline is the merge SHA above.
- **Current stage:** **LI-002 — Source Registry & Legal Research**. The first official-source discovery tranche was accepted and merged through [PR #3](https://github.com/martynio/LivingIndex/pull/3), with verified `main` checkpoint [`229062bf`](https://github.com/martynio/LivingIndex/commit/229062bfbd7183399ec10f1762680b5a550d25c9). **The full LI-002 numerical-feasibility and operator gate remains open.**
- **Project Proposal:** [LI-PP-001 v1.0](LI-PP-001-PROJECT-PROPOSAL-v1.0.md) remains a project proposal; accepting governance does not automatically authorize product implementation.
- **Application code:** none; web directories remain placeholders.
- **LI-002 HBS proof and runner:** [PR #4](https://github.com/martynio/LivingIndex/pull/4) established the proof contract. [PR #5](https://github.com/martynio/LivingIndex/pull/5) was explicitly approved and merged as [`74ac245`](https://github.com/martynio/LivingIndex/commit/74ac245412c9df800720e34875affd7209bd9f2c). The manual workflow file exists on `main`; the **HBS job has not been executed**.
- **Validated economic datasets:** none. The 2020 HBS PL/NL observation-proof run remains **BLOCKED** due to unavailable API response; see [HBS proof gate](../research/HBS_2020_PROOF_GATE.md). First-pass publisher metadata and source leads do **not** constitute validated dataset observations.
- **Automated CI / application tests:** no application test suite. The manual HBS workflow and eight synthetic research-unit tests are merged; **8/8 tests were previously reported locally**, but there is **no GitHub-hosted HBS run result yet**. The GitHub connector cannot dispatch a new workflow run.

## Gate register

| Gate | State | Evidence / next requirement |
| --- | --- | --- |
| LI-001 documentation quality | **PASS** | Verified 14 PR files; post-review link/path checks passed; proposal unchanged |
| LI-001 operator approval and merge | **CLOSED / ACCEPTED** | Explicit operator approval, [PR #1 merged](https://github.com/martynio/LivingIndex/pull/1), `main` HEAD verified at `2192e95` following merge |
| LI-001 closure documentation | **RECORDED** | `ROADMAP`, `PROJECT_STATUS`, `WORK_LOG`, `HANDOFF`, ADR-0001 updated in a dedicated closeout |
| LI-002 initial metadata/rights research | **ACCEPTED / CHECKPOINTED** | [PR #3](https://github.com/martynio/LivingIndex/pull/3), merge `229062bf`; 11 source leads, no accepted numeric observations |
| LI-002 manual HBS probe | **MERGED / MANUAL RUN PENDING** | [PR #5](https://github.com/martynio/LivingIndex/pull/5) accepted; `workflow_dispatch` present on default branch; manual UI registration/dispatch not independently tested |
| LI-002 numerical feasibility | **BLOCKED / RESEARCH CONTINUES** | No verified Eurostat HBS API values; run [HBS research automation](../research/HBS_PROBE_AUTOMATION.md), review artifact, flags, units and rights |
| GitHub Actions activity | **PAGES ONLY / NOT HBS** | [Run 43428015863](https://github.com/martynio/LivingIndex/actions/runs/43428015863) succeeded for the GitHub Pages build/deployment workflow; no `LI-002 Eurostat HBS research probe` run was found in the checked action-run list |
| Publication/legal readiness | **NOT ESTABLISHED** | Verify hosting, data processing, telemetry, source rights and attribution before any public policy claims |

## Handoff

Read [AGENTS.md](../../AGENTS.md), [ROADMAP](ROADMAP.md), [WORK_LOG](../logs/WORK_LOG.md) and the [latest handoff](../logs/HANDOFF.md). Before each iteration, independently verify Git HEAD, relevant PRs, current files and open gates.

**Acceptance of LI-001 closes only the governance stage.** It authorizes no LI-003 website implementation, legal-policy publication or numerical data import. LI-002 first-pass registry research is accepted, but LI-002 is **not** complete; no LI-003 website work or numerical economic claims have been approved.
