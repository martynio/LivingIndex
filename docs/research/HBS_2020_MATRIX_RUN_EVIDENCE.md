# LI-005B — HBS 2020 complete division matrix: hosted run evidence

**Date:** 2026-11-27 · **Verdict:** retrieval and research normalization PASS; production eligibility remains false.

## Run and provenance

- Operator manually dispatched [run 46032585277](https://github.com/martynio/LivingIndex/actions/runs/46032585277) at 16:19:10 UTC on main `b5af5cfbbd438eb6363d724819ccdcccdf072c40`. Both jobs completed successfully.
- Offline job 140619857782 logs: 17 tests, OK; live job 140619915597 logs: OBSERVATIONS_RETRIEVED_REVIEW_REQUIRED. Artifact 15215615718, li-002-hbs-2020-division-matrix, 1138 bytes, expiry 2026-12-04 16:19:25 UTC.
- Source: [Eurostat hbs_exp_t121](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en), DOI 10.2908/hbs_exp_t121; dataset updated 2025-10-15T23:00:00+0200 as reported; retrieval 2026-11-27T16:19:25.696389+00:00, HTTP 200.
- Exact query: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hbs_exp_t121?lang=EN&freq=A&time=2020&unit=PPS_HH&geo=PL&geo=NL&coicop=CP01&coicop=CP02&coicop=CP03&coicop=CP04&coicop=CP05&coicop=CP06&coicop=CP07&coicop=CP08&coicop=CP09&coicop=CP10&coicop=CP11&coicop=CP12
- Downloaded ZIP independently hashed: `533cd6d815c83bfae6d6e4dc39b4cff2731edbc4436a3f0f921c15f52a1ea204`, identical to GitHub metadata and job log. Single archive entry hbs-2020-matrix.json, extracted SHA-256 `c3f7c8385af0eb0930ec8c2859021c0f5452d8df8666924ac97d0335fc9ae661`.
- Original API body SHA-256 as reported by runner: `bf9ca169a1954ad1f733ac747139b6831a765f3f210fdf485ca8f57550f8dfc5`. Original bytes not retained; independently verifying the response hash remains impossible from this artifact.
- Named axes freq/coicop/unit/geo/time, sizes 1/12/1/2/1; A, CP01–CP12, PPS_HH, NL index 0 and PL index 1, 2020. 24 expected, 24 present, zero missing; every source_flag null (no flag in report, not a quality certificate).

## Observations

Source: Eurostat hbs_exp_t121, 2020 annual mean consumption expenditure per household, PPS_HH; accessed 2026-11-27. ECOICOP 2013 divisions. Verbatim numeric observations transcribed into a research evidence table, short descriptive labels only; no value transformations. Not approved production inputs.

| Division | Short description | PL | NL |
| --- | --- | ---: | ---: |
| CP01 | Food and non-alcoholic beverages | 4234 | 3835 |
| CP02 | Alcoholic beverages and tobacco | 440 | 1025 |
| CP03 | Clothing and footwear | 633 | 1203 |
| CP04 | Housing, water, electricity, gas and other fuels | 5612 | 10156 |
| CP05 | Furnishings and household maintenance | 875 | 1969 |
| CP06 | Health | 810 | 497 |
| CP07 | Transport | 1349 | 3426 |
| CP08 | Communication | 752 | 1057 |
| CP09 | Recreation and culture | 879 | 2549 |
| CP10 | Education | 155 | 378 |
| CP11 | Restaurants and hotels | 588 | 1430 |
| CP12 | Miscellaneous goods and services | 852 | 5607 |

Do not sum these rows into an asserted official total; see [national budget evidence](LI-005B-NATIONAL-BUDGET-EVIDENCE.md). PPS is neither a cash amount nor the price of a fixed basket. Housing expenditure may include imputed rent; [Eurostat HBS information](https://ec.europa.eu/eurostat/en/web/household-budget-surveys/information-data) and [metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm) document harmonization limits. 2020 pandemic context applies. Eurostat's [reuse notice](https://ec.europa.eu/eurostat/help/copyright-notice) generally permits reuse of published statistical aggregates with attribution subject to exceptions; production review stays open. Eurostat does not endorse this project.

## Independent replay

- Local adapter and tests matched accepted Git blob IDs a8f13e701a8a6ea62d033d1528c6c20207e01594 and da2bc4c8bdd39fd85421e6a6e0a0893d0e8d9176. Command: python -m unittest discover -s tests -p 'test_economic_research.py' -v; 13/13 PASS.
- Actual archived matrix report replay via scripts/economic_research.py with its independently computed report digest returned 24 records, all observed, production_eligible=false, coordinate_evidence=report_axes, all review states pending. Local normalized JSON SHA-256 `53397d56f266a167c8f6de6c3133780f8830aae69f6056504f2328007c7d0349`. No normalized or raw JSON committed.
- Independently hashed earlier CP01 archive and JSON against [first run evidence](HBS_2020_RUN_002_EVIDENCE.md). Both values and flags agree exactly.
- [Secondary compilation](https://fgeerolf.com/data/eurostat/hbs_exp_t121.html), compiled 22 November 2026 as displayed, independently corroborates NL CP01, CP04, CP07 and CP09. Four of 24 values corroborated through a secondary source; not a second official extraction. Official Data Browser cell-level verification still unavailable to reviewer.

## Gate

HBS-2020-01 PARTIAL (artifact and timestamp verified, API body not retained); HBS-2020-02 PASS for all 24 research-report coordinates and values; HBS-2020-03 OPEN (partial secondary corroboration only); HBS-2020-04/05/06 OPEN (methodology, production reuse/approval, aligned income and paid hours). Next review exact national budget definitions, approve a bounded scenario contract and synchronize registry/catalogue status in a separately scoped change. No calculations, UI edits, production promotion or stage closure.
