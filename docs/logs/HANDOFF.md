# Living Index — latest contributor handoff

**Updated:** 2026-11-13 · **Phase:** LI-002 / HBS 2020 observation proof · **State:** discovery tranche merged; numerical retrieval **BLOCKED**, full LI-002 gate **OPEN**.

## Project baseline

- Public repository: `martynio/LivingIndex`.
- [PR #3](https://github.com/martynio/LivingIndex/pull/3) merged, verified `main` checkpoint [`229062bfbd7183399ec10f1762680b5a550d25c9`](https://github.com/martynio/LivingIndex/commit/229062bfbd7183399ec10f1762680b5a550d25c9).
- Eleven research source IDs `LI-SRC-001` through `LI-SRC-011` and legal-feasibility notes present on `main`.
- No published website, curated observations or application tests/CI.

## Read first

[AGENTS.md](../../AGENTS.md), [status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [source registry](../research/SOURCE_REGISTRY.md), [feasibility](../research/FEASIBILITY_MATRIX.md), [work log](WORK_LOG.md), and [work protocol](../governance/WORK_PROTOCOL.md).

## Accepted outcome

- Documented source discovery and reuse/cross-country limits, not a comparable living-cost calculation.
- PR #3 independently verified: 11 source IDs; 34 internal links with 0 missing; no runtime/data changes.
- **NOT RUN:** selected 2020 HBS numeric cells, harmonization of net wages and paid hours, site/host privacy scan, runtime CI.

## Latest research result

The [HBS 2020 proof gate](../research/HBS_2020_PROOF_GATE.md) defines the exact `PL/NL` 2020 API query and required cell-status checks. Actual response JSON could not be retrieved in this environment; the work deliberately records **no invented numeric observations**. Dataset `hbs_exp_t121` is displayed in **PPS per household**, not directly in local-currency monthly budgets. Owner-occupied imputed rent requires separate methodological treatment.

## Next permitted task

Run the bounded LI-002 2020 HBS API observation probe in a network-enabled environment, preserve retrieval evidence, and then evaluate matched PL/NL values and definitions. Record sources, retrieve and preserve flags, avoid interpreting PPS/household as national-currency monthly spending. No LI-003 implementation without full LI-002 decision gate.
