# LI-005B — National budget evidence and compatibility review

**Date:** 2026-11-27 · **Verdict:** PARTIAL EVIDENCE / matrix retrieval remains open. No approved production inputs.

## Scope and accepted baseline

Operator accepted [PR #13](https://github.com/martynio/LivingIndex/pull/13) and requested continuation of LI-005B. Verified main `b5af5cfbbd438eb6363d724819ccdcccdf072c40`, expected merge parents 9c30a8f8989d0ca439ce33451c6cfb75821c937c and c789134fe7becc1c39c2148dfc60e093a90a96b1. [Pages run 46027307728](https://github.com/martynio/LivingIndex/actions/runs/46027307728) completed successfully at this SHA.

Rechecked 13/13 local adapter unit tests and exact tested Git blob identities. Archived CP01 ZIP SHA-256 and report digest matched accepted evidence; replay returned two research-only records. The approved-data inventory is still empty.

This tranche reviews official source evidence for 2020 national-currency household income and expenditure, HBS methodology and reuse, and denominator compatibility. No new runtime, production import, calculation code, source registry or website edits. New candidate source references below are not assigned canonical IDs until their registry/catalogue changes are separately reviewed together.

## 1. HBS retrieval and method

The GitHub run list contains the successful PR regression for the matrix but no manual workflow_dispatch execution of the live matrix job. Direct API access failed through the browser tool, including a PL/NL annual query and alternate webgate endpoint; local curl returned DNS resolution failure. The official Data Browser product could not be read at cell level. These are access limitations, not evidence of missing source values. The Eurostat copyright page also advertised maintenance on 27 November 16:00–19:00; this notice does not establish the cause of our access failure.

The earlier [CP01 evidence](HBS_2020_RUN_002_EVIDENCE.md) remains the sole retrieved Eurostat PL/NL pair. A [secondary compilation](https://fgeerolf.com/data/eurostat/hbs_exp_t121.html) independently displays the same NL CP01 2020 value of 3835, but not the PL cell in its displayed subset. This is secondary corroboration, not second official extraction. The [DBnomics dataset metadata](https://db.nomics.world/Eurostat/hbs_exp_t121) lists one unit, consistent with the [Eurostat product](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en) reporting PPS_HH. Do not assume NAC_HH or EUR_HH are available in this specific table merely because the HBS collection supports national currency, euros and PPS across its tables.

Official [HBS metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm), sections 4, 5, 12.3, 15 and 18.6, confirms the annual survey reference period, 12 ECOICOP-2013 divisions, incomplete harmonisation and use of household final-consumption PPP. Published aggregates can differ from the sum of component categories. Neither a 12-division sum nor PPS converted with a market exchange rate is a cash budget. [HBS comparability guidance](https://ec.europa.eu/eurostat/en/web/household-budget-surveys/information-data) identifies imputed owner-occupier rent as an important comparability issue. In the 2020 wave, metadata identifies Czechia and Malta as countries without such imputation; this does not establish the exact national housing treatment or cash component of the PL/NL cells.

## 2. Official national-budget observations (research evidence only)

All values below are directly transcribed at the published precision, not modelled, rounded further, converted or approved as calculation inputs. Access date 2026-11-27. No raw snapshot or normalized numeric dataset is committed. Publisher HTML text was inspected; no byte-level snapshot/hash or final-source parity is claimed.

| Local evidence key | Publisher / period / population | Measure | Published value and unit |
| --- | --- | --- | --- |
| PL-GUS-2020-INCOME | GUS, 2020, household members, monthly per person | Mean disposable income | 1919 PLN/person/month, rounded to 1 PLN by publisher |
| PL-GUS-2020-EXP | Same GUS release | Mean total expenditure | 1210 PLN/person/month, published rounded |
| PL-GUS-2020-CONS | Same GUS release | Mean consumption goods and services expenditure | 1165 PLN/person/month, published rounded |
| NL-CBS-2020-INCOME | CBS 86272NED, 2020, private households with income, annual household mean | Disposable income | 46.4 thousand EUR/household/year |
| NL-CBS-2020-CONS | Same CBS table and row | Consumption expenditure | 35.2 thousand EUR/household/year |

**PL:** [GUS release, 31 May 2021, Sytuacja gospodarstw domowych w 2020 r.](https://stat.gov.pl/obszary-tematyczne/warunki-zycia/dochody-wydatki-i-warunki-zycia-ludnosci/sytuacja-gospodarstw-domowych-w-2020-r-w-swietle-badania-budzetow-gospodarstw-domowych%2C3%2C20.html?contrast=black-yellow). Title and release date confirmed in page body; tool title incorrectly referred to 2025. Full [GUS 2020 budget publication landing page](https://stat.gov.pl/obszary-tematyczne/warunki-zycia/dochody-wydatki-i-warunki-zycia-ludnosci/budzety-gospodarstw-domowych-w-2020-roku%2C9%2C15.html?contrast=black-white) identified, but exact full table and final revision/definitions still to be inspected. This is related to LI-SRC-006, not the 2025 report itself. GUS explicitly distinguishes total spending from consumption spending.

**NL:** [CBS 86272NED, Welvaart van particuliere huishoudens; kerncijfers](https://www.cbs.nl/nl-nl/cijfers/detail/86272NED), modified 25 November 2026; year 2020 row under Particuliere huishoudens. Table identifies 2011–2024 figures as final. Mean disposable income and mean consumption spending are distinct columns; table population is private households with income on 1 January of reporting year. [Discontinued predecessor 83739NED](https://www.cbs.nl/nl-nl/cijfers/detail/83739NED) shows matching 2020 values. [CBS 85419NED](https://www.cbs.nl/nl-nl/cijfers/detail/85419NED), final 2015 and 2020, confirms annual household consumption total 35.2 thousand EUR in category 000000 and food category 010000 at 4.5 thousand EUR. The earlier [CBS 2022 article](https://www.cbs.nl/nl-nl/nieuws/2022/06/coronacrisis-drukt-bestedingen-buitenshuis-meer-uitgaven-voor-thuis) reported 35.3 thousand EUR. Retain this revision distinction rather than mixing values or silently replacing historical evidence LI-SRC-011. The CBS category table includes extra national categories; do not assume one-to-one equivalence with all Eurostat divisions. Check spending survey weights/population, imputed rent, insurance and exclusions before treating the difference of means as a cash remainder.

Both national sources describe COVID-related changes in consumption. Neither represents a normal-year fixed price basket.

## 3. Rights review (not production approval)

- Eurostat [reuse notice](https://ec.europa.eu/eurostat/help/copyright-notice): published statistical data and metadata generally reusable with source credit, subject to individual conditions and exceptions. The selected PL/NL aggregate table is identified as Eurostat data. No relevant exception was identified in the reviewed notice. For any future public extract use dataset DOI 10.2908/hbs_exp_t121 and access date, disclose transformations and non-endorsement; inspect exact release and rights at approval. No restricted microdata.
- [CBS copyright](https://www.cbs.nl/en-gb/over-ons/website/copyright): general CC BY 4.0 unless indicated otherwise; credit CBS, disclose changes, avoid endorsement and protected logos/images. The inspected statistical tables identify CBS as source; no special restriction visible. For future numeric release record exact table/row, date and license; no blanket approval of all CBS content.
- [GUS reuse conditions](https://bip.stat.gov.pl/kontakt/ponowne-wykorzystywanie-informacji-sektora-publicznego/) and [English information](https://bip.stat.gov.pl/en/contact-with-the-office/reuse-of-public-sector-information/): public-sector information reuse rules apply; source and creation/acquisition time attribution identified in official search result. Full conditions page could not be consistently fetched. Retain rights review pending for production, including modification disclosure and any publication-specific conditions. Limited attributed reporting of published facts here is research evidence, not redistribution of the report or permission to republish a dataset.

## 4. Recommended distinct analytical views (proposal, not accepted contract)

| View | Evidence | Decision / required work |
| --- | --- | --- |
| National budget | GUS 2020 per person/month and CBS 2020 per household/year | Feasible starting points for separately labelled national panels after exact definitions, complete categories, revision and rights review. Do not directly compare amounts or mechanically multiply by average household size. Need matching income and expense population/basis, explicit cash vs imputed items and harmonised categories. |
| Harmonised expenditure | HBS CP01 research pair; matrix pending | PPS household consumption, not prices or money remaining. Independent cell check, flags and methodology remain necessary. |
| Modelled earnings | [Eurostat earn_net metadata](https://ec.europa.eu/eurostat/cache/metadata/en/earn_net_esms.htm) / LI-SRC-012 | Select explicit family/earnings scenario. Includes taxes, social contributions and applicable allowances; not observed mean HBS household income. |
| Working time | LI-SRC-013 LFS actual reference-week hours; [SES metadata](https://ec.europa.eu/eurostat/cache/metadata/en/earn_ses_main_esms.htm) offers gross earnings and paid hours, four-year survey | Actual hours and paid hours differ. SES gross-based time cannot be labeled net. No matching net paid-hours denominator for 2020 established. Do not annualize LFS by a fixed multiplier and claim observed paid hours. |
| Equivalised income | LI-SRC-014 / [EU-SILC methodology](https://ec.europa.eu/eurostat/web/income-and-living-conditions/methodology) | Distinct welfare measure, not household total. Align survey and income reference periods. |

Recommendation: develop country-specific budget evidence first, and reserve cross-country comparison and paid-hour views for genuinely matched measures. Do not force a single all-purpose denominator.

## 5. Gate and immediate next action

- LI-005A accepted, code tests 13/13 re-executed and actual CP01 replay verified; no production versions.
- LI-005B national source discovery: partial PASS. Matrix retrieval/validation NOT RUN, official direct CP01 reconciliation OPEN, production rights/methodology OPEN, matched income/hours OPEN.
- Run existing [HBS division matrix workflow](https://github.com/martynio/LivingIndex/actions/workflows/li-002-hbs-matrix.yml) manually on main. Connector cannot initiate workflow_dispatch. Public repo artifacts are not private; the report contains selected aggregate observations, not raw source bytes. Eurostat general aggregate reuse notice reviewed above; artifact is research-only and expires after seven days. Preserve actual report and independently verify its digest; pass the verified report to the accepted adapter without committing output.
- Review this evidence, then separately scope exact GUS/CBS extraction and scenario eligibility; synchronize candidate registry and catalogue only after source review. No new calculation engine, chart, dataset approval or closure of LI-002/LI-005 in this tranche.
