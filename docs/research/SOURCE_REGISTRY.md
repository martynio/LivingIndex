# LI-002 — Source registry (research candidates)

**Checked:** 2026-11-10 · **Status:** first-pass source discovery, **not** publication approval.

The canonical machine-readable index is [SOURCE_REGISTRY.csv](SOURCE_REGISTRY.csv). IDs are stable references, not ranking scores. Every registered claim is backed by the linked **primary publisher** webpage. **No statistical observations have been downloaded, validated or committed.**

## Source inventory

| ID | Provider | Measure | Evidence checked | Readiness |
| --- | --- | --- | --- | --- |
| LI-SRC-001 | CBS (NL) | CPI, linked historic series | Table `71905ned` metadata: 1900–2025, annual, estimated by joining series; dataset explicitly marks CC BY 4.0 | Metadata verified; **not** a household-cost series |
| LI-SRC-002 | GUS (PL) | Annual CPI change | Official GUS annual index table: 1950–2025, previous year = 100 | Metadata verified; not directly comparable to CBS base |
| LI-SRC-003 | GUS (PL) | Average monthly wage | Official GUS historical wage table: 1950–2025 | National mean, **not** net household income |
| LI-SRC-004 | CBS (NL) | Employment wages and working hours | CBS `81432ENG`: available since 2009; published 2009–2025 figures final | Contains **gross** wages; not net purchasing hours |
| LI-SRC-005 | Eurostat | HBS expenditure waves | Official HBS information: waves 2015 and 2020, generally five-year collection; methodological differences remain | Country/indicator cells and direct comparison **unverified** |
| LI-SRC-006 | GUS (PL) | Household income and spending | 2025 household-budget publication and publicly linked historical archive | Single publication checked; historical harmonization **unverified** |
| LI-SRC-007 | CBS (NL) | Household expenditure microdata | CBS microdata listing 1978–2004, 2012, 2013, 2015, 2020 | **Not approved for redistribution**; avoid using as public data |
| LI-SRC-008 | Eurostat | Life satisfaction survey | EU-SILC indicator `ilc_pw01`, 2022 wave, score 0–10 | Candidate, not % respondents satisfied |
| LI-SRC-009 | Eurostat | HBS household mean expenditure | Exact table `hbs_exp_t121`, 1988–2020 table coverage; PL/NL 2020 country wave confirmed in official metadata | **Dataset identified; cell values / flags still unchecked** |
| LI-SRC-010 | Eurostat | HBS expenditure structure by household type | Exact table `hbs_str_t224`, 1988–2020; per-mille proportions | **Not equivalent to absolute expenditure** |
| LI-SRC-011 | CBS (NL) | 2020 household income / expenditure public summary | CBS article cites annual disposable income, expenditure and savings for 2015/2020 | 2020 publication flags preliminary figures; COVID spending anomaly |

## Publisher sources

- [CBS `71905ned` official dataset page](https://dataportal.cbs.nl/detail/CBS/71905ned) — includes OData/CSV links, latest revision and dataset-specific CC BY 4.0.
- [GUS annual CPI indices](https://stat.gov.pl/obszary-tematyczne/ceny-handel/wskazniki-cen/wskazniki-cen-towarow-i-uslug-konsumpcyjnych-pot-inflacja-/roczne-wskazniki-cen-towarow-i-uslug-konsumpcyjnych/).
- [GUS average monthly earnings 1950–2025](https://stat.gov.pl/obszary-tematyczne/rynek-pracy/pracujacy-zatrudnieni-wynagrodzenia-koszty-pracy/przecietne-miesieczne-wynagrodzenie-w-gospodarce-narodowej-w-latach-1950-2025%2C2%2C1.html).
- [CBS `81432ENG` earnings / hours](https://www.cbs.nl/en-gb/figures/detail/81432ENG).
- [Eurostat HBS — information on data](https://ec.europa.eu/eurostat/en/web/household-budget-surveys/information-data).
- [Eurostat official HBS country/year metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm) — NL and PL both marked as participating in 2020.
- [Eurostat `hbs_exp_t121` expenditure table](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en) — DOI `10.2908/hbs_exp_t121`, 1988–2020 reported table coverage.
- [Eurostat `hbs_str_t224` structure by household type](https://ec.europa.eu/eurostat/databrowser/view/hbs_str_t224/default/table?category=livcon.hbs.hbs_struc&lang=en) — DOI `10.2908/hbs_str_t224`, 1988–2020 table coverage.
- [CBS 2020 budget/income public summary](https://www.cbs.nl/item?sc_itemid=f6a7ad70-31b4-47bd-a7cf-bca7a7e58978&sc_lang=nl-nl) — 2020 observations described as provisional in the original publication.
- [GUS 2025 household budget report](https://stat.gov.pl/obszary-tematyczne/warunki-zycia/dochody-wydatki-i-warunki-zycia-ludnosci/budzety-gospodarstw-domowych-w-2025-r-%2C9%2C24.html).
- [CBS budget survey microdata listing](https://www.cbs.nl/nl-nl/onze-diensten/maatwerk-en-microdata/microdata-zelf-onderzoek-doen/microdatabestanden/budgetonderzoek-bestedingen-particuliere-huishoudens).
- [Eurostat life satisfaction indicator `ilc_pw01`](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20240115-1).

## Two independent approval axes

**Rights to reuse are not the same as scientific comparability.**

1. **Reuse clearance:** dataset-specific license/terms, attribution wording, third-party exceptions, transformations and any redistribution limits.
2. **Analytical clearance:** population, units, period, mean/median, gross/net, deflation, currency regime, household composition, survey differences, and uncertainty.

A public source card may be built from independently verifiable metadata after review; it must never imply that underlying figures have been accepted for a calculation.

## Reading the CSV

- `verified_start_year` / `verified_end_year` refer to **publisher metadata available in this discovery**, not checked numeric observation completeness; empty means not verified.
- `metadata_state` describes only checked page-level facts.
- `reuse_state` is NOT permission to copy except where explicitly checked at dataset level. `CBS_GENERAL_CC_BY_4_0_VERIFY_DATASET` and `EUROSTAT_GENERAL_REUSE_EXCEPTIONS_CHECK` require source-level review.
- `comparison_readiness` is an independent analytical gate; no row is accepted as production-ready.
- `source_url` is a stable publisher reference where possible; exact data exports and timestamps remain future work.

For feasibility and blockers, see [FEASIBILITY_MATRIX.md](FEASIBILITY_MATRIX.md). For rights and site requirements, see [LEGAL_RESEARCH.md](LEGAL_RESEARCH.md).

## 2020 discovery addendum (2026-11-10)

Eurostat's [HBS metadata table](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm) lists both **Netherlands and Poland** as 2020 wave participants. The source reports historical wave participation (NL from 1988; PL from 1999), but participation does **not** prove that every category x household-type x unit cell is non-missing. The next task is to inspect actual selected observations and flags in `hbs_exp_t121` and `hbs_str_t224`.

This improves confidence in the 2020 research anchor but **does not** establish a complete comparable household budget or net-hourly economic model.
