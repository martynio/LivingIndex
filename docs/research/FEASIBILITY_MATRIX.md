# LI-002 — Initial PL/NL data feasibility matrix

**Checked:** 2026-11-10 · **Stage:** DISCOVERY / evidence audit, **not a validated economic dataset**.

## Verified availability vs missing integrations

| Question | Poland | Netherlands | What is still missing |
| --- | --- | --- | --- |
| Annual consumer price changes since 1980? | **Candidate YES**: GUS annual CPI table 1950–2025 (LI-SRC-002) | **Candidate YES**: CBS linked CPI table 1900–2025 (LI-SRC-001) | Definitions, breaks, index conversion and whether methodological base can be harmonized |
| Historical average wages? | **Candidate YES**: GUS monthly mean wages 1950–2025 (LI-SRC-003) | **Partial**: CBS employment gross wages / working hours 2009–2025 (LI-SRC-004) | Matching populations and gross-to-net rules per historical period |
| Comparable household spending categories? | GUS household-budget 2025 and earlier editions exist (LI-SRC-006) | Eurostat HBS 2020 PL/NL wave participation **verified**; exact tables `hbs_exp_t121` (LI-SRC-009) and `hbs_str_t224` (LI-SRC-010) identified; CBS restricted microdata (LI-SRC-007) | **CRITICAL**: **actual selected numeric cells**, COICOP mapping, owner-occupied imputed rent, sample/method differences and source-specific license |
| Net earnings per paid hour? | **NO VERIFIED MATCHED SERIES** | **NO VERIFIED MATCHED SERIES** | Income definition, tax/benefit treatment, paid hours, worker vs household basis |
| Life satisfaction observations? | Eurostat 2022 survey indicator `ilc_pw01` (LI-SRC-008) | Same indicator / year (LI-SRC-008) | Download and check comparable years, age breakdown, survey responses and confidence |
| Housing ownership, rent, age cohorts, commuting, queues? | Not researched sufficiently | Not researched sufficiently | Separate research tasks; **out of MVP assumptions** |

The word **candidate** means the primary publisher describes the measure or series; it does **not** mean values were retrieved, validated, or approved. A CPI index cannot directly show a euro/PLN monthly spending budget.

## 2020 evaluation hypothesis — not an accepted comparison

2020 is a stronger **research anchor**: Eurostat's [country/year metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm) explicitly confirms **both Poland and the Netherlands** in the 2020 HBS wave, and public dataset codes [`hbs_exp_t121`](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en) and [`hbs_str_t224`](https://ec.europa.eu/eurostat/databrowser/view/hbs_str_t224/default/table?category=livcon.hbs.hbs_struc&lang=en) are identified. But **selected numerical cells**, their flags, compatible net income, and paid hours have **not** been checked.

**Do not publish a PL/NL 'money left' or 'hours needed' comparison yet.**

To close the data-feasibility portion of LI-002:

1. Use the now-identified HBS table IDs to **retrieve and verify selected PL/NL 2020 values and flags**, units, reference period, owner-occupier imputed rent handling and categories.
2. Review at least one compatible alternative national source per country for 2020.
3. Identify coherent earnings denominator(s): country-specific net income and paid hours for the same population and period, or explicitly postpone net-hour calculations.
4. Build a provenance matrix with source URLs, dataset IDs, retrieval dates, revisions and source-specific usage conditions.
5. Design a provisional harmonization mapping with **missing/incomparable** states; do not invent backfill.
6. Review feasibility independently before accepting **one real scenario per country**.

## Non-negotiable methodology

- Historical Poland has currency redenomination and major market/availability discontinuities; do not compare unadjusted pre-1995 nominal PLN with modern PLN.
- Historical CPI and wages support **trend analysis**, not automatically exact cost-of-living reconstruction.
- Distinguish family vs per-person, renting vs owner-occupancy, household disposable income vs worker wages.
- Do not equate EU-SILC life satisfaction 7.7 / 10 with '77% satisfied'.
- Actual commuting/queue time requires separate directly relevant sources. No inferred daily-hour scores.

See [SOURCE_REGISTRY.md](SOURCE_REGISTRY.md), [LEGAL_RESEARCH.md](LEGAL_RESEARCH.md), and [methodology](../methodology/README.md).

## Additional 2020 context (not a calculated result)

The [CBS 2020 budget summary](https://www.cbs.nl/item?sc_itemid=f6a7ad70-31b4-47bd-a7cf-bca7a7e58978&sc_lang=nl-nl) provides a public 2020 reference for household income, spending and savings and marks the initial 2020 values as provisional. COVID-19 restrictions changed the 2020 spending pattern; that year must carry an explicit context warning in any future public comparison. NL evidence is **not** a substitute for a matching PL measure.
