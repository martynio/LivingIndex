# Living Index — latest contributor handoff

**Updated:** 2026-11-24 · **Phase:** LI-002 · **State:** first evidence accepted; division-matrix implementation and dependency ADR proposed; numerical gate OPEN.

- Verified main `e389573c34c88c3772b0c56701360bedf979a148` after [PR #7](https://github.com/martynio/LivingIndex/pull/7); hosted CP01 report evidence accepted.
- Proposed matrix branch `research/li-002-hbs-division-matrix`; implementation commit `a137f987e711f71428f78de5df9616d86fe13297`; nine new local tests PASS, exact tested blob hashes matched. Hosted regression/live matrix run not yet observed when this note was written.
- Read [matrix scope](../research/HBS_DIVISION_MATRIX.md), [first run evidence](../research/HBS_2020_RUN_002_EVIDENCE.md), [registry](../research/SOURCE_REGISTRY.md), [status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [work log](WORK_LOG.md), and [AGENTS.md](../../AGENTS.md).
- New candidates LI-SRC-012–014 have only metadata verified; no income/hour values obtained. Never equate PPS with local cash spending or use mismatched denominators.
- [ADR-0002](../decisions/ADR-0002-PARALLEL-SHELL-RESEARCH.md) proposes branch-only LI-003 shell work in parallel, conditional on acceptance and a separate scope. Actual Pages settings, host, operator data, legal review and publication gate still open.
- Next: check PR offline regression result; review and accept; manually dispatch **LI-002 Eurostat HBS division matrix** on main. Inspect artifact, compare CP01 and source flags, record observed results. No data/chart publication, site changes or scope expansion in this PR.
