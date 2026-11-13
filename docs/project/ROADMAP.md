# Living Index — project roadmap

**Document:** LI-RM-001 · **Created:** 2026-11-09 · **Status:** Active governance roadmap (LI-001 operator-approved and checkpointed); future stages require independent operator authorization.

This roadmap organizes work; it does **not** promise dates or data availability. The [Project Proposal](LI-PP-001-PROJECT-PROPOSAL-v1.0.md) remains the definition of product goals. Stage labels below are independent of code releases.

## Phase sequence

| ID | Stage | Deliverables | Stage exit (operator gate) | Current state |
| --- | --- | --- | --- | --- |
| LI-000 | Public repository foundation | Initial README, proposal, scaffold, contribution guidance | Repository tree and proposal verified | **CHECKPOINTED** — [67ccc38](https://github.com/martynio/LivingIndex/commit/67ccc38d8a29f9300d741e49351d1f65a765f3a7) |
| LI-001 | Governance, roadmap & logs | `AGENTS.md`, work protocol, status, roadmap, append-only log and handoff, PR traceability | Documents cross-linked, consistent; operator approves governance PR | **ACCEPTED / CHECKPOINTED** — [PR #1](https://github.com/martynio/LivingIndex/pull/1), [merge 2192e95](https://github.com/martynio/LivingIndex/commit/2192e95f331aaafab8ee2a10adb217cc7ae2f85b) |
| LI-002 | Source registry & legal requirements research | Internal source catalog, licenses/redistribution/attribution review, PL/NL coverage matrix, privacy/cookie/hosting requirements assessment | Source claims and legal assumptions evidenced; publishable sources identified; gaps documented | **RESEARCH IN PROGRESS** — [initial source research PR #3 merged](https://github.com/martynio/LivingIndex/pull/3); numerical verification pending, full stage gate open |
| LI-003 | Website foundation | Responsive Bootstrap 5+ / Pinegrow-compatible template, navigation, EN/PL/NL shells, accessibility baseline, reviewed legal information pages | Functional shell tested on mobile/desktop; legal pages match **actual** data processing | **PLANNED — BLOCKED by LI-002 decision gate** |
| LI-004 | Public sources explorer | Transparent source cards, definitions, dataset coverage, warnings, method/attribution links; no unverified series | Displayed source metadata reconciled with approved registry; usable without app charts | **PLANNED** |
| LI-005 | Economic data foundation | Approved PL/NL snapshots and curated, versioned JSON, documented calculations and regression tests | Reproducible evidence-backed scenario per country; comparison limits and licenses clear | **PLANNED — research dependent** |
| LI-006 | First economic dashboard | Country/year selection, money/work-hour view, warning links and source traceability | Accepted MVP slice on verified datasets; accessibility, calculations and regression gates pass | **PLANNED** |

**LI-003 and LI-004 are presentation phases, not permission to manufacture data.** The source registry starts *before* its public presentation. LI-005 must close its evidence gate before a dashboard can claim real results.

## Scope boundaries by phase

- LI-001: documentation and templates only. **No** runtime, website template, datasets, legal-policy drafts, or source-data imports.
- LI-002: research and source eligibility; no live site, no implied universal 1980–present coverage.
- LI-003: honest website shell; privacy, cookie, terms and legal text must be checked against chosen hosting, analytics, data flows and applicable law. Do not generate a cookie banner by default.
- LI-004: cards for inspected sources with explicit status; display of an institution does not imply all of its data has been accepted.
- LI-005/006: build only the actually feasible and operator-approved slice; do not convert a survey mean into a percent satisfied or gross pay into net purchasing hours.

## Required exit evidence for every stage

1. Operator-approved scope, acceptance criteria and exclusions.
2. Repo check: branch, HEAD, change status, relevant implementation, prior checkpoint, tests.
3. Documented work and evidence in [WORK_LOG](../logs/WORK_LOG.md) and [HANDOFF](../logs/HANDOFF.md).
4. Applicable tests/checks with verifiable outcome, honest `NOT RUN` where appropriate.
5. Isolated branch, traceable commit(s), PR, operator decision recorded.
6. `PROJECT_STATUS.md` updated only when a transition is actually accepted.

## Future (not in initial sequence)

Comparisons with more countries, historical age/household segments, extended time accounting, survey life-satisfaction visualizations where available, and optional experimental composite indexes follow separate feasibility and scope decisions. No artificial deadlines.
