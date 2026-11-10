# Living Index — latest contributor handoff

**Updated:** 2026-11-10 · **Work item:** LI-002 / source and legal discovery · **State:** first-pass research **IN REVIEW**, full LI-002 gate **OPEN**.

## Start here

- [Project status](../project/PROJECT_STATUS.md)
- [Roadmap](../project/ROADMAP.md)
- [AGENTS.md](../../AGENTS.md)
- [Work protocol](../governance/WORK_PROTOCOL.md)
- [Research scope](../research/LI-002-SCOPE-AND-GATE.md)
- [Source registry](../research/SOURCE_REGISTRY.md) / [CSV](../research/SOURCE_REGISTRY.csv)
- [Feasibility matrix](../research/FEASIBILITY_MATRIX.md)
- [Legal research](../research/LEGAL_RESEARCH.md)
- [Work log](WORK_LOG.md)

## Verified baseline

- Repository `martynio/LivingIndex`; accepted LI-001 main checkpoint: `af9362d71f11c65f16532ca568372e003fb0c0ee`.
- Before LI-002, `main` had no open PRs and there was no implemented application/data-ingestion test suite.
- This LI-002 research tranche is on branch `research/li-002-source-and-legal-discovery`; query Git for exact current head and PR state.

## Research delivered for review

- Official publisher metadata for CPI, wages, household budgets and life satisfaction, registered with stable IDs (now including HBS dataset codes `hbs_exp_t121` and `hbs_str_t224` plus a public CBS 2020 reference).
- PL/NL coverage and comparability gap assessment (especially the proposed 2020 HBS scenario).
- Separate source reuse and methodological suitability statuses.
- Preliminary official-source legal requirements for cookies/privacy/operator identity/hosting/terms and data attribution.
- No values downloaded, no application implemented, and no public legal pages created.

## Verification and blockers

- Public primary source pages reviewed on 2026-11-10; see exact links in research documents.
- **NOT RUN:** numeric cross-country validation, app tests/CI (none exist), a deployed-site request/cookie audit, legal counsel review.
- **CRITICAL BLOCKER:** PL/NL 2020 HBS country/wave presence is confirmed, but individual selected **value cells/flags and comparability** remain unverified; no demonstrated compatible net paid-hours denominator.
- Rights conditions must be confirmed per actual data table and output; CBS microdata cannot be treated as open redistribution material.

## Next permitted action

Review this research PR and decide whether to accept the **discovery tranche**, continue detailed LI-002 dataset checks, and which sources deserve numerical proof. **Do not begin LI-003 or close LI-002 merely because the registry exists.**
