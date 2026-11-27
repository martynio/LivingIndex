# LI-005A — Research data contract and HBS normalization

**Date:** 2026-11-27 · **State:** implementation and local verification on review branch; not a production data release.

## CURRENT STATE

Operator explicitly accepted [PR #12](https://github.com/martynio/LivingIndex/pull/12) as development preview and authorized LI-005. Main verified at `9c30a8f8989d0ca439ce33451c6cfb75821c937c`, with expected merge parents. Pages run 46023013236: completed/success, head 9c30a8f8989d0ca439ce33451c6cfb75821c937c. No approved production dataset. Existing [CP01 evidence](../research/HBS_2020_RUN_002_EVIDENCE.md) records two research observations from the 2020 PL/NL HBS, but lacks independently verified API response bytes, explicit legacy category axes, second official cell reconciliation and full methodology/rights approval. [Matrix](../research/HBS_DIVISION_MATRIX.md) manual retrieval remains pending.

## OBJECTIVE

Introduce versioned, machine-readable research observations and strict scope validation so later approved inputs cannot silently inherit incorrect units or research-only status. This is the first bounded foundation package, not a complete economic model.

## IN SCOPE

- Standard-library Python adapter [economic_research.py](../../scripts/economic_research.py) for the existing legacy CP01 and 24-cell matrix report formats, only hbs_exp_t121, PL/NL, reference year 2020, PPS_HH.
- Validate separately recorded report SHA-256, endpoint/query, successful HTTP status, dimensions, observation keys, numeric values, missingness, flags, offsets, counts and report status. Matrix named-axis coordinates must agree with offsets. Legacy report has only query/shape evidence, not category indices; preserve that limitation.
- Normalize into JSON contract 1.0.0, with research-only status and explicit pending review fields. The local CLI can validate without writing values or produce a new private file outside the repository. Empty approved-data manifest.
- Test synthetic cases and reprocess the previously archived real CP01 report locally.

## OUT OF SCOPE / CONSTRAINTS

No new retrieval, raw or normalized values committed, dataset promotion, chart, income conversion, actual cash budget, working-hour calculation, UI change or backend. Do not import any restricted data or commit a local research output. Input digests must come from independently recorded evidence: matching a caller-supplied digest verifies identity, not publisher authenticity. This is a bounded adapter, not a general JSON-stat parser, full legal validator or access control system. The public Pages root may serve repository content; never store private or unapproved data there. No fabricated economic series; synthetic numbers occur only in test code.

## Contract 1.0.0

| Field | Meaning |
| --- | --- |
| schema_version / kind | 1.0.0 / research_observations |
| production_eligible | Always false in this adapter; input flags cannot override it |
| source_id / dataset | LI-SRC-009 / hbs_exp_t121 |
| measure / unit / population | mean_consumption_expenditure / PPS_HH / survey_households |
| frequency / statistic | annual / mean; not monthly cash or identical-basket prices |
| provenance | Query, report-created timestamp, retrieved timestamp if available, source revision as reported, actual report digest, runner-reported API digest, independent API-byte check=false, coordinate evidence level |
| review | Rights, methodology, independent cell check and operator approval all pending |
| observations | Country, reference year, category, value, source flag, source flat index, observed/missing |
| approved manifest | [manifest.json](../../data/curated/manifest.json) has empty approved_versions, NO_APPROVED_DATASETS |

A null value is missing, not zero. A null flag means absent report flag, not a quality certificate. Duplicate or out-of-scope coordinates, invalid offsets, non-finite or negative expenditure, wrong units and digest mismatch reject the report. A matrix missing an actual coordinate retains null value and null offset; a present coordinate may have missing value and a flag. No interpolation. Frequency and legacy category labels are inferred from the documented query and publisher metadata, not independently proven by the legacy report. Source revision is carried as reported, not a separate verified version identifier.

## ACCEPTANCE CRITERIA / REQUIRED TESTS / STOP CONDITIONS

Accept only this research adapter after code identity, regression tests for its fixed scope, replay of the archived report and empty-manifest verification. Stop on changed input hashes, new dimension codes, incompatible unit, unresolved reuse conditions for publication or any attempt to treat research data as approved inputs. Existing HBS scripts and web shell must remain unchanged.

### Observed verification

- Local Python: `python -m unittest discover -s tests -p 'test_economic_research.py' -v` — **13/13 PASS** (synthetic tests). Tested blobs match GitHub: script `a8f13e701a8a6ea62d033d1528c6c20207e01594`, tests `da2bc4c8bdd39fd85421e6a6e0a0893d0e8d9176`. Code checkpoint `82f4446218c49232c113ca08f6da2466f0e92701`.
- Archived real CP01 ZIP hash independently recomputed, matching `9eae192f964daa90dfc0301a4ee9e857d4da3639008b5b7efc3ce6a90ff0b4e5`. Extracted JSON hash `373fc61e2fa5356c6e74ef82489aa819ef8a725af127be58a4cc280eac0fc15c` matched accepted evidence. Normalization returned exactly two original country values and research-only status, with legacy coordinate limitation. No normalized numbers committed.
- Manifest contains zero approved versions. Matrix report real replay NOT RUN (no hosted matrix run observed). Existing HBS regression and browser tests NOT RUN in this iteration; previous test results are historical. No new source retrieval or independent primary-source reconciliation.

## Next packages (not yet executed)

1. LI-005B: obtain actual matrix artifact by manual workflow, validate report, reconcile source cells/rights and assess local currency and matching household/worker data. Do not sum incomplete or incompatible divisions.
2. LI-005C: choose one clearly defined country/year/population scenario per country with compatible income and expenses; independently review actual net employment income and paid hours. Define transformation lineage and approved version records; implement arithmetic and rejection tests only after those contracts are accepted.
3. LI-006: consume approved version records, not research artifacts. No budget remainder or paid-hour equivalent until appropriate definitions and source rights clear. This adapter does not close LI-002 or LI-005.
