# Living Index — latest contributor handoff

**Updated:** 2026-11-24 · **Phase:** LI-002 · **State:** hosted HBS retrieval PASS; research evidence in review; full stage OPEN.

## Baseline and evidence

- Repository `martynio/LivingIndex`, verified main checkpoint `228e23d4897fd2365037ab19a6009355438f5f15`; PRs #5 and #6 accepted.
- Operator manually dispatched [HBS run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068) on that checkpoint; 8/8 hosted tests and retrieval succeeded.
- Downloaded report ZIP hash matched GitHub digest. Exact provenance, CP01/PPS_HH PL/NL observations, source flags and limitations: [run evidence](../research/HBS_2020_RUN_002_EVIDENCE.md).
- No production dataset or cost-of-living calculation approved. Original API body not retained; independent official browser reconciliation open.
- Node.js 20 deprecation warning in workflow logs: maintenance follow-up, not a run failure.

## Read first

[AGENTS.md](../../AGENTS.md), [status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [source registry](../research/SOURCE_REGISTRY.md), [proof gate](../research/HBS_2020_PROOF_GATE.md), [work log](WORK_LOG.md).

## Next permitted action

Review the evidence PR and accept or request corrections. Then reconcile both exact source cells, investigate local-currency household expenditure and compatible net income and paid hours, and evaluate final rights and methodology. Do not interpret PPS as EUR/PLN or a fixed-basket price. The LI-003 dependency has not been changed; any parallel website-shell scope requires explicit operator decision. No code, deployment settings or production data modified.
