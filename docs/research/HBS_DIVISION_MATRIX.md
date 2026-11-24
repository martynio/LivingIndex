# LI-002 — HBS division matrix and income/time feasibility

**Date:** 2026-11-24 · **Status:** implementation accepted via [PR #8](https://github.com/martynio/LivingIndex/pull/8); hosted regression 17/17 PASS; live matrix retrieval NOT RUN.

## Scope contract

- Baseline: accepted evidence [PR #7](https://github.com/martynio/LivingIndex/pull/7), main merge `e389573c34c88c3772b0c56701360bedf979a148`. Original CP01 probe and its eight regression tests remain unchanged.
- Objective: establish coverage of 12 expenditure divisions for PL/NL in the same Eurostat 2020 survey wave; identify candidate income/time sources and their compatibility requirements.
- In scope: one fixed, bounded API request, 24 expected observations (12 divisions × 2 countries), explicit annual frequency, JSON-stat 2.0 coordinate checks, missingness, flags and response checksum. Synthetic offline tests on pull requests; live retrieval only after manual dispatch.
- Out of scope: raw-response publication, local-currency conversions, totals, price baskets, calculations of money remaining or work hours, new website or production data, automatic scheduling, changes to the existing CP01 workflow.
- Acceptance: nine matrix unit tests pass, regression suite remains compatible, new workflow permissions/trigger reviewed, and code and local test hashes match. Hosted numerical evidence is a separate gate.
- Stop conditions: ambiguous dimensions, invalid schema, HTTP failure, or incomplete cells produce non-successful retrieval status; preserve missing cells as null rather than estimate.

## Execute the research probe

With PR #8 now merged, manually run **LI-002 Eurostat HBS division matrix** from [Actions](https://github.com/martynio/LivingIndex/actions), branch main. The offline job runs both synthetic test suites; the network job only runs on workflow_dispatch after tests succeed. The artifact `li-002-hbs-2020-division-matrix` contains the research report, expires after seven days, and is not production data. The original response body is not uploaded; its SHA-256 is recorded by the runner but cannot be independently recomputed from the report alone.

- [Matrix script](../../scripts/hbs_matrix_probe.py)
- [Matrix tests](../../tests/test_hbs_matrix_probe.py)
- [Workflow](../../.github/workflows/li-002-hbs-matrix.yml)
- [Eurostat HBS table hbs_exp_t121](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en)
- [Eurostat HBS metadata and division definitions](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm)

Fixed query: freq=A, year=2020, unit=PPS_HH, geo=PL and NL, coicop=CP01–CP12. No additional years or countries are requested. These are 2020 HBS divisions, not the newer COICOP 2018 classification. CP04 includes housing-related expenditures and must not be labeled actual cash rent without methodological review.

A full report is `OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED`. A partial report is `INCOMPLETE_REVIEW_REQUIRED` and fails the live job. Invalid responses or transport failures yield `BLOCKED`. Even a full report is not accepted as a statistically comparable household budget. Compare CP01 to [run #2 evidence](HBS_2020_RUN_002_EVIDENCE.md); different values require revision/date investigation, not forced replacement. Independently reconcile selected cells with the official browser before production use.

## Income and time source candidates

| ID | Official dataset | What it measures | Compatibility risk / required decision |
| --- | --- | --- | --- |
| LI-SRC-012 | [earn_nt_net](https://ec.europa.eu/eurostat/databrowser/view/earn_nt_net/default/table?lang=en) | Annual modelled net earnings for specified earnings and family cases; EUR, national currencies, PPS as available | Select exact family/earner case and income concept; not the observed mean household disposable income of HBS participants |
| LI-SRC-013 | [lfsa_ewhais](https://ec.europa.eu/eurostat/web/products-datasets/-/lfsa_ewhais) | Actual weekly hours worked in the main job, labour force survey | Actual reference-week hours are not contractual or annual paid hours; full-time/part-time, age, worker population and breaks require alignment |
| LI-SRC-014 | [ilc_di03](https://ec.europa.eu/eurostat/databrowser/product/view/ILC_DI03?category=livcon.ilc.ilc_ip.ilc_di&lang=en) | Mean/median equivalised disposable income by age and sex, EU-SILC | Equivalised person-level indicator is not gross household income; income reference period can differ from survey year |

Primary metadata: [net earnings and tax rates](https://ec.europa.eu/eurostat/cache/metadata/en/earn_net_esms.htm), [Eurostat labour market earnings](https://ec.europa.eu/eurostat/en/web/labour-market/information-data/earnings), [actual weekly hours definition](https://ec.europa.eu/eurostat/en/web/products-eurostat-news/w/ddn-20260527-1), [EU-SILC methodology](https://ec.europa.eu/eurostat/web/income-and-living-conditions/methodology). No candidate numeric observations retrieved in this iteration. PL/NL 2020 coverage and precise dimension codes remain to be verified before a separate extraction.

## Analytical contract before calculation

Separate the observed HBS average household from an explicitly hypothetical worker/household case. Do not combine household mean spending and individual model earnings as a measured average remainder; do not divide annual earnings by 52 times a reference-week average and call it measured net paid-hour pay. A future scenario must identify household composition and earners, reference periods, units and price concept, taxes/benefits, paid-hour denominator, housing treatment, population match and source-specific rights. If these cannot be aligned, display distinct indicators or explicitly label scenario assumptions; seek operator approval rather than silently mixing them.

## Verification

Local Python command: `python -m unittest discover -s tests -p 'test_hbs_matrix_probe.py' -v` — **9/9 PASS**. Syntax compilation of both new Python files passed. GitHub blob SHA-1 matches locally hashed matrix script and test file: `e852ee49913ef19e596fb019ca49cf0970a982e8` and `64796df06553b74d46e934bc68f070c9babd159d`. Pinned checkout v5 and upload-artifact v6 action manifests verified to use Node.js 24; the prior single-cell workflow is unchanged. Hosted PR regression and manual live retrieval must be assessed separately. No new Eurostat values were obtained during local synthetic tests.

## Accepted hosted regression — 2026-11-24

[Run 45439673111](https://github.com/martynio/LivingIndex/actions/runs/45439673111) checked the PR merge test ref against the accepted base and head; offline job succeeded, logs explicitly show 17 tests and OK. Manual-observation-matrix was skipped as designed. Operator accepted PR #8; [merge c812480](https://github.com/martynio/LivingIndex/commit/c8124808c8d57b3973c17362593922b6826e3713) verified on main. No new matrix observations have been retrieved.
