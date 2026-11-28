# LI-006D — Eurostat PPS admission review

**Date:** 2026-11-28 · **State:** research verification started; independent official reconciliation OPEN; no numeric dashboard admission.

## Accepted baseline

Operator accepted PR #18 and gus-hbs-pl-2020-v1 for descriptive display only and authorized LI-006D. Merge [ceaad53](https://github.com/martynio/LivingIndex/commit/ceaad5367c8f5b5c02f2cc516041973dfe2c2f71) verified identical to main; reviewed acceptance head 081b59f9341f4b8fcfdf3c52ce8a3367ee828921. Both descriptive versions accepted; approved calculation inventory remains empty. Deployment not independently confirmed: combined statuses and PR-triggered workflow listing empty; these do not establish a Pages failure.

## Scope and actual verification

- Fixed dataset Eurostat hbs_exp_t121, DOI 10.2908/hbs_exp_t121, annual mean consumption expenditure per private household, PPS_HH, 2020, CP01–CP12 (ECOICOP 2013), PL/NL only. See [existing matrix evidence](../research/HBS_2020_MATRIX_RUN_EVIDENCE.md).
- Downloaded original Actions artifact 15215615718 again from [run 46032585277](https://github.com/martynio/LivingIndex/actions/runs/46032585277); ZIP 1138 bytes, SHA-256 533cd6d815c83bfae6d6e4dc39b4cff2731edbc4436a3f0f921c15f52a1ea204; sole report hbs-2020-matrix.json SHA-256 c3f7c8385af0eb0930ec8c2859021c0f5452d8df8666924ac97d0335fc9ae661. Both independently recomputed locally and match prior evidence. Artifact expires 2026-12-04 16:19:25 UTC. Raw API body not retained.
- Local standard-library Python assertions on downloaded report: 24/24 unique expected country/category pairs, integer values, flat indices agree with declared axes (NL=0, PL=1), all flags null and no missing cells. Four NL values agree with [secondary compilation](https://fgeerolf.com/data/eurostat/hbs_exp_t121.html), CP01/04/07/09, respectively 3835/10156/3426/2549. This is not an independent official export or quality certification. Earlier 12/12 engine replay and 29/29 regression are historical, not rerun here.
- Official [Data Browser product](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en) identifies annual PPS per household; direct view returned only navigation shell. Exact original JSON-stat query, single PL CP01 query, alternate SDMX-CSV request and TSV request were inaccessible via reviewer web access. DBnomics series/API requests also inaccessible. Local git ls-remote failed DNS. No inference that Eurostat itself is down. HBS-2020-03 remains OPEN.

## Methodology and reuse

[Official HBS metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm), sections 3, 13, 15, 18 and 19, and [HBS information](https://ec.europa.eu/eurostat/en/web/household-budget-surveys/information-data) reviewed 2026-11-28. Private households (institutional/collective households generally excluded); weighted sample estimates. Annual household mean is not a fixed household composition or per-person measure. PPS adjustment uses the average household final consumption PPP, not category-specific price parity; country survey differences persist. Owner-occupier imputed rent affects housing, and both PL/NL are outside the two 2020 non-imputing countries listed in metadata; do not assume identical national treatment. Aggregates may differ from component sums, and the pandemic affected expenditure and collection. No price, affordability, cash balance, ratio, total, currency conversion, paid-hours or cross-wave claim.

[Eurostat reuse notice](https://ec.europa.eu/eurostat/help/copyright-notice) reviewed 2026-11-28: statistical aggregates generally reusable with source acknowledgment subject to individual exceptions; distinguish this from editorial CC BY 4.0. PL/NL EU data identified as Eurostat; no relevant exception identified in reviewed product metadata, no logos/microdata. If admitted, credit Eurostat, DOI/table, source update and retrieval date, indicate translated labels/no numerical transformation and disclaimer of Eurostat responsibility for transformations. No blanket legal or production approval.

## Independent export gate — operator action

1. Open [official table](https://ec.europa.eu/eurostat/databrowser/view/hbs_exp_t121/default/table?lang=en) in a normal browser.
2. Download **full dataset TSV** (or filtered SDMX-CSV with codes and observation flags) via Download. Official [download guide](https://ec.europa.eu/eurostat/en/web/user-guides/data-browser/download-data/download-datasets) and [TSV format](https://ec.europa.eu/eurostat/en/web/user-guides/data-browser/api-data-access/api-faq/tsv-format). Alternatively obtain [official TSV endpoint](https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/hbs_exp_t121?format=TSV) as a raw export. Keep the unedited file (including gzip if served) and record retrieval UTC and URL. Do not manually copy a screen or regenerate a file from our own matrix.
3. Upload that original export for independent comparison. Check dimension codes and annual 2020 column, all 24 pairs, flags/missingness, calculate raw file digest and compare to accepted archived report. Stop on discrepancies; investigate dataset revisions rather than overwriting.
4. Only after successful reconciliation stage a versioned PPS descriptive matrix with source attribution, limitations and explicit candidate state, three localized views and regression checks; operator approval required before main publication. No approved calculation input. A separate gate would be needed for derived comparison ratios/production calculations.

## Result

Research review and artifact integrity PASS; independent official reconciliation OPEN. No snapshot, manifest, registry, dashboard, engine, or workflow modifications in this tranche. No full browser or regression run. This draft PR preserves the actual state and gives a specific unblock path.
