# LI-002 — HBS 2020 first hosted observation evidence

**Date:** 2026-11-24 · **Evidence ID:** LI-002-HBS-RUN-002

**Verdict:** NETWORK RETRIEVAL PASS / RESEARCH OBSERVATIONS REVIEW REQUIRED. Not a validated economic budget or full LI-002 acceptance.

## Run and provenance

| Field | Observed result |
| --- | --- |
| Source | Eurostat, [hbs_exp_t121](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en), DOI 10.2908/hbs_exp_t121 |
| Exact API request | [Fixed PL/NL 2020 CP01 PPS_HH query](https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hbs_exp_t121?lang=EN&geo=PL&geo=NL&time=2020&unit=PPS_HH&coicop=CP01) |
| Run | [45436731068, run number 2](https://github.com/martynio/LivingIndex/actions/runs/45436731068); event workflow_dispatch; completed success |
| Operator | Repository owner manually initiated the workflow |
| Checked-out commit | `228e23d4897fd2365037ab19a6009355438f5f15` (main), confirmed in job logs |
| Job | 138596465703, hbs-2020-observation-probe; checkout, synthetic tests, retrieval and upload all succeeded |
| Tests | 8/8 passed on the hosted runner, as observed in job logs |
| Report timestamp UTC | 2026-11-24T16:24:26.639879+00:00 |
| HTTP | 200, as recorded by the probe |
| Dataset updated | 2025-10-15T23:00:00+0200 |
| Report state | OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED |
| Artifact | [14940134556](https://github.com/martynio/LivingIndex/actions/runs/45436731068/artifacts/14940134556), 769-byte ZIP; expiry 2026-12-01T16:24:27Z |
| Artifact ZIP SHA-256 | `9eae192f964daa90dfc0301a4ee9e857d4da3639008b5b7efc3ce6a90ff0b4e5` |
| Extracted report JSON SHA-256 | `373fc61e2fa5356c6e74ef82489aa819ef8a725af127be58a4cc280eac0fc15c` |
| API response SHA-256 (reported by probe) | `46189db6de1d1951870f90f9eefce9c5de6a2aaab46782352634760d5cff8992` |

The reviewer downloaded the artifact, independently hashed its ZIP bytes and matched the GitHub artifact digest and job log. The ZIP contains exactly one file, `hbs-2020-report.json`, which was extracted, hashed and parsed. The original API response was not uploaded by design; therefore its SHA-256 is a runner-reported value, **not independently recomputed**. The artifact expires; this research note records the selected observations and provenance, not a byte-for-byte source snapshot.

## Observations (unmodified numeric values from the report)

Dataset: mean consumption expenditure per household by COICOP consumption purpose. Category CP01 (food and non-alcoholic beverages), annual frequency A, survey reference year 2020, unit PPS_HH (purchasing power standard per household). Report dimensions: freq, coicop, unit, geo, time. Shape: 1 × 1 × 1 × 2 × 1.

| Country | Value (PPS per household) | Source flag returned | Report flat index |
| --- | ---: | --- | ---: |
| PL — Poland | 4234 | null | 1 |
| NL — Netherlands | 3835 | null | 0 |

Null flag means the report contains no flag for that observation; it is not a quality certificate. The approved script resolves named coordinates, but its report does not include singleton frequency category labels; A is supported by the publisher's table metadata, not by an explicit frequency-label check in the report.

Source: [Eurostat hbs_exp_t121](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en), accessed 2026-11-24. Subset selected and transcribed from the API report without numerical transformation. Eurostat is not responsible for Living Index interpretations. [Eurostat reuse notice](https://ec.europa.eu/eurostat/help/copyright-notice) permits reuse of statistical data with attribution subject to individual conditions and exceptions. The public table identifies Eurostat as provider; no special restriction was apparent in the inspected metadata. This note is research evidence only, not blanket redistribution approval or approval of production data.

## Independent verification and remaining gates

- Publisher table metadata confirms annual frequency, PPS per household, category and country coverage. Direct API re-fetch and official Data Browser cell reconciliation were not available through the reviewer's browsing environment; no claim of a second primary-source read.
- [Open Data Index secondary Eurostat catalogue](https://www.opendataindex.nl/en/dataset/eurostat/hbs_exp_t121) displays the matching NL value of 3835; this is partial secondary corroboration, not independent primary-source confirmation of both cells.
- Household size/composition, survey methods, imputed rent and COVID-2020 context remain relevant. PPS household spending is not local currency, the price of a fixed basket, affordability, disposable income, or working hours.
- Hosted run logs report Node.js 20 deprecation for checkout@v4 and upload-artifact@v4 (forced to Node.js 24). Run succeeded. Record as maintenance follow-up, not a reason to invalidate this run. No workflow upgrade in this scope.

| Gate | Result |
| --- | --- |
| HBS-2020-01 | PARTIAL PASS: retrieval and report checksum evidence verified; original response bytes not preserved |
| HBS-2020-02 | PASS for selected CP01/PPS_HH numeric pair and report flags only |
| HBS-2020-03 | OPEN: direct official browser value reconciliation not done |
| HBS-2020-04 | OPEN: household and housing methodology |
| HBS-2020-05 | OPEN for production: general reuse notice reviewed; final output-specific conditions/attribution review required |
| HBS-2020-06 | OPEN: compatible net income and paid hours |

## Next permitted action

Review and checkpoint this evidence PR. Reconcile the two exact cells with the official Data Browser; then define a small, separately scoped source-feasibility iteration for local-currency household budgets and matched income/time denominators, or explicitly revise the stage gate to permit website shell work independently. No production import, chart, new code or stage closure is authorized by this note.
