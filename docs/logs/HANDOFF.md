# Living Index — latest contributor handoff

**Updated:** 2026-11-13 · **Phase:** LI-002 / HBS 2020 API probe · **State:** Automation merged; manual run pending; full LI-002 data gate **OPEN**.

## Accepted and verified checkpoint

- Repository: public `martynio/LivingIndex`.
- Operator-approved [PR #5](https://github.com/martynio/LivingIndex/pull/5): **MERGED / CLOSED**.
- `main` merge checkpoint: [`74ac245412c9df800720e34875affd7209bd9f2c`](https://github.com/martynio/LivingIndex/commit/74ac245412c9df800720e34875affd7209bd9f2c), with both Git parents verified.
- Workflow `.github/workflows/li-002-hbs-probe.yml` exists on `main`, with `workflow_dispatch` and read-only `contents` permission.
- A documentation-only closeout commit may follow that baseline; inspect current Git HEAD instead of assuming the merge SHA is latest.

## What is and is not verified

- **PASS:** PR #5 merge, workflow file and manual trigger configuration. Previous synthetic Python unit tests: **8/8 PASS** (as recorded in LI-LOG-0010).
- **NOT RUN:** real Eurostat HBS 2020 PL/NL API probe, observations, source flags, response checksum, official data-browser reconciliation, and methodology/legal acceptance.
- **TOOL LIMIT:** current GitHub connection can read workflow runs but cannot invoke `workflow_dispatch` or verify the Actions UI button.
- **UNRELATED RUN:** [GitHub Pages run 43428015863](https://github.com/martynio/LivingIndex/actions/runs/43428015863) was successful for **Pages build/deployment**, not the Eurostat workflow. The first real Living Index website is not an accepted product release.

## Next operator action

1. Open [repository Actions](https://github.com/martynio/LivingIndex/actions).
2. Choose **LI-002 Eurostat HBS research probe** and click **Run workflow** for `main`.
3. Share the resulting run URL; the research job should upload `li-002-hbs-2020-probe-report` even when the API request fails, and the report is retained for 7 days.
4. Inspect the run's actual logs, report timestamp, SHA-256, data coordinates/flags, and any errors. Record a new `LI-LOG-0012` or later entry based only on observed evidence.

## Research constraints

Read [AGENTS.md](../../AGENTS.md), [current status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [HBS automation guide](../research/HBS_PROBE_AUTOMATION.md), [HBS proof contract](../research/HBS_2020_PROOF_GATE.md), and [WORK_LOG](WORK_LOG.md).

No numeric observations or validated budget model have been committed. HBS `PPS_HH` does **not** represent monthly PLN/EUR cash spending; net working-hours and housing methodology remain separate gates. **Do not begin LI-003 or publish statistical claims based only on this workflow.**
