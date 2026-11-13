# Living Index — latest contributor handoff

**Updated:** 2026-11-13 · **Phase:** LI-002 / manual HBS API validation · **Status:** PR #4 merged; new automation PR under review; economic-data gate **BLOCKED**.

## Grounded baseline

- Repo: `martynio/LivingIndex`; `main` verified at [`e9fcb1cb6c953e356a06e4b2910f99a183180a7f`](https://github.com/martynio/LivingIndex/commit/e9fcb1cb6c953e356a06e4b2910f99a183180a7f).
- [PR #4](https://github.com/martynio/LivingIndex/pull/4) merged; HBS 2020 proof contract is on `main`.
- A **new** manual-only workflow, research probe and synthetic-unit tests are prepared on branch `research/li-002-hbs-action-probe`. Query GitHub for the exact latest PR and SHA.

## Read first

[AGENTS.md](../../AGENTS.md), [project status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [research automation instructions](../research/HBS_PROBE_AUTOMATION.md), [HBS proof contract](../research/HBS_2020_PROOF_GATE.md), [work log](WORK_LOG.md).

## Verification recorded

- Repo scope is research tooling and documentation, **not** product frontend or downloaded statistical datasets.
- Local Python 3.13, `unittest`: **8/8 PASS** against synthetic JSON-stat fixtures. `py_compile`: **PASS**. GitHub file blob hashes matched locally tested artifacts.
- Local live query: **BLOCKED due to DNS**; a JSON error report was generated.
- **NOT RUN:** GitHub Actions network probe (workflow not yet in `main`), numeric source cross-check, legal rights sign-off, methodology approval.
- Existing source registration: 11 candidates, not all publication-ready.

## Next gate

1. Review new automation PR, merge only on explicit operator acceptance.
2. Open GitHub Actions and manually run **LI-002 Eurostat HBS research probe** from `main`; domain or GitHub Pages setup **not required**.
3. Inspect the report and the GitHub run status, then write an audit log entry with actual run URL, timestamp, checksum, numerical values and flags (if retrieved), or failure details.
4. Cross-check cells and PPS/household methodology; **do not close LI-002** until both country scenarios and rights are independently validated.

Do not implement LI-003, deploy website pages, copy API responses into `data/`, or treat research probe PASS as a validated cost-of-living calculation.
