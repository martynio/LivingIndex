# LI-002 — Manual Eurostat HBS API probe (GitHub Actions)

**Status (2026-11-13):** **PR #5 ACCEPTED / MERGED** into `main` at [`74ac245`](https://github.com/martynio/LivingIndex/commit/74ac245412c9df800720e34875affd7209bd9f2c). The workflow file is present on the default branch; the **Eurostat network probe has NOT BEEN RUN**.
**Purpose:** get reproducible first-party JSON-stat 2.0 evidence for a narrow 2020 PL/NL subset without deploying the website.

## Scope and operation

The job in [li-002-hbs-probe.yml](../../.github/workflows/li-002-hbs-probe.yml) is **manual only** (`workflow_dispatch`). It uses GitHub-hosted Ubuntu, standard Python 3, repository contents read-only, a 10-minute job limit, and no additional secrets or web domain. It does not create Git commits, publish site files, or upload full API response bodies.

1. With the workflow now merged into default branch `main`, open [GitHub Actions](https://github.com/martynio/LivingIndex/actions).
2. Select **LI-002 Eurostat HBS research probe** → **Run workflow** → branch **main** → Run workflow.
3. Inspect test results and the network-probe step. Download artifact `li-002-hbs-2020-probe-report` from the run; retention is **7 days**.
4. Report the run URL, commit SHA, report `created_at_utc`, source endpoint, response checksum (when available), observations/flags, and reviewer conclusions in [WORK_LOG](../logs/WORK_LOG.md). Never copy unreviewed data to `data/`.
5. Independently cross-check the two coordinates in [Eurostat Data Browser](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en), then carry out the independent methodological and reuse-rights gates in [HBS_2020_PROOF_GATE.md](HBS_2020_PROOF_GATE.md).

**Why not run on PR?** GitHub documents that manually dispatchable workflows must be present on the default branch. The workflow will therefore be runnable only after its separate review/acceptance gate. The website and domain are unrelated to this requirement.

## Fixed research query

```text
dataset = hbs_exp_t121
time = 2020
geo = PL, NL
unit = PPS_HH
coicop = CP01
```

The script uses Eurostat's official JSON-stat API endpoint; no API token is required. It has a 5 MB response limit, a request timeout, validates dimensions dynamically (never trusts hard-coded flat indices), refuses ambiguous extra dimensions, and rejects missing/null/non-finite values. No fallback data are invented.

The status meanings in the artifact are deliberately narrow:

- `OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED`: a valid paired numeric response was retrieved and the response SHA-256 was captured. This **does not mean** values have been approved for a Living Index dashboard. Any source flags and differences in definitions need review.
- `BLOCKED`: the API was unreachable, response invalid, required dimensions absent, or one of the two cells missing or invalid. The job **fails** while preserving the report if possible.
- A failing/blocked probe is **not** proof that Eurostat is down; network availability, query parameters and published category membership must be investigated.

Report values are **PPS per household** rather than PLN/EUR monthly spending. The script does not create a net-income, work-hours or owner-occupied imputed-rent comparable model.

## Verification

Run offline (uses intentionally artificial test numbers only):

```bash
python3 -m unittest discover -s tests -p 'test_hbs_probe.py' -v
python3 -m py_compile scripts/hbs_probe.py tests/test_hbs_probe.py
```

For live observation evidence, run only the manual GitHub Action. Do not commit the report as production data.

The checked local tests cover JSON-stat sparse/dense forms, array/dictionary category indices, varying dimension order, missing values, invalid extra dimensions and non-numeric observations. They are **synthetic fixtures**, not official economic data.

## Controls

- No scheduled background run, no arbitrary input URL, no credentials.
- Workflow has `permissions: contents: read`, and uploads a short **report only**, not the raw dataset.
- All acceptance decisions remain human-reviewed and recorded as a Git checkpoint.
- Official information: [Eurostat API Statistics](https://ec.europa.eu/eurostat/en/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics), [GitHub manually running workflows](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow).

**Current gate:** This automation is merged and was locally unit-tested in the previous iteration, but has not yet been run or verified on GitHub-hosted runners. Do not close LI-002 or advance to LI-003 until real PL/NL values, flags, rights, housing methods and relevant net-income/paid-hours inputs have been independently verified.

## Dispatch verification record (2026-11-13)

- **PASS:** PR #5 merged (GitHub reports `merged=true`) with commit `74ac245412c9df800720e34875affd7209bd9f2c`; `main` HEAD matched and the workflow YAML was fetched directly from `main`.
- **PASS — configuration:** the YAML contains the intended `on: workflow_dispatch` trigger, `permissions: contents: read`, a single Ubuntu job, no schedule, and a short report artifact.
- **LIMITATION:** this GitHub connection exposes workflow reads and run/job status, but **no action to dispatch a new `workflow_dispatch` event**. The workflows-list/details endpoints were also unavailable through this connection. Therefore the actual presence of the **Run workflow** UI button was not independently verified here.
- **NOT RUN:** the LI-002 HBS job itself. The repository's recent Actions list contained only [GitHub Pages build/deployment run 43428015863](https://github.com/martynio/LivingIndex/actions/runs/43428015863) (successful after merge) and its prior canceled Pages run. Neither is the HBS probe. A successful Pages deployment is not evidence that a Living Index website is ready or that the Eurostat API was contacted.

**Operator handoff:** open the [Actions tab](https://github.com/martynio/LivingIndex/actions), select **LI-002 Eurostat HBS research probe**, choose **Run workflow** on branch `main`, then share the run URL for inspection. If the workflow does not appear or the button is unavailable, record the actual UI or repository Actions policy issue without inventing a successful run.
