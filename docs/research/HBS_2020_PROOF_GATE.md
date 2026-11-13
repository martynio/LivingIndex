# LI-002 — HBS 2020 observation proof gate (Poland / Netherlands)

**Date:** 2026-11-13  
**Stage:** LI-002 research, numerical proof not yet obtained  
**Verification verdict:** **BLOCKED — no successfully retrieved PL/NL numeric observation pair**  
**Producer:** ChatGPT (GPT-6, official-publication review and GitHub repository tools)

## Question

Can Living Index reproduce at least one exact, public, well-defined **2020** household expenditure comparison between Poland (`PL`) and the Netherlands (`NL`) from **the same Eurostat table, unit, COICOP code and reference wave**, with documented flags, methodology and rights?

A source identifier and country participation are necessary, **not sufficient**.

## Primary evidence verified

| Evidence | Verified statement | Important restriction |
| --- | --- | --- |
| [Eurostat `hbs_exp_t121`](https://ec.europa.eu/eurostat/databrowser/product/view/hbs_exp_t121?lang=en) | Mean consumption expenditure **per household**, COICOP; table contains 1988–2020 waves; its displayed unit is **PPS per household** (`PPS_HH`), latest dataset update shown as 2025-10-15 | PPS is **not** directly a national-currency monthly cash budget; coverage years are global table metadata, not guaranteed cells by country/category |
| [Eurostat HBS 2020 microdata availability](https://ec.europa.eu/eurostat/web/microdata/collections-research/household-budget-survey) | Both `PL` and `NL` are listed for the 2020 HBS scientific-use-file wave | Restricted scientific microdata access is **not** permission to copy or redistribute microdata |
| [Eurostat HBS information](https://ec.europa.eu/eurostat/en/web/household-budget-surveys/information-data) | Wave 2020 exists; cross-country survey frequency, methodology and owner-occupied housing treatment can differ | Country participation alone does not imply numerical comparability |
| [Eurostat HBS metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm) | Historical HBS reference rounds include 1988, 1994, 1999, 2005, 2010, 2015, 2020; consumption expenditure may use national currency, euro, or PPS **depending on table** | Verify **actual** `unit` values in each selected dataset; do not assume the `hbs_exp_t121` table supplies PLN/EUR |
| [Eurostat API specification](https://ec.europa.eu/eurostat/en/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics) | JSON-stat 2.0 service with dimension filters is available | API schema and available positions must be inspected from its returned response; never infer observations from a URL |
| [Eurostat HBS 2020 methodology](https://ec.europa.eu/eurostat/web/household-budget-surveys/methodology) | Eurostat publishes survey documentation and 2020 quality information | The treatment of imputed rent requires a documented inclusion/exclusion decision |
| [Eurostat reuse notice](https://ec.europa.eu/eurostat/help/copyright-notice) | Statistical data generally reusable with attribution, modifications disclosure and specific exceptions | Cite exact dataset DOI `10.2908/hbs_exp_t121`, access date and modifications; check applicable exceptions |

## Reproducible API request — **prepared, not successfully executed here**

The following is a **request recipe**, not a dataset or a claim of received values. Run in an environment able to reach the Eurostat API. Do not add fabricated fixtures.

```bash
curl --fail-with-body --location --show-error \
  'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/hbs_exp_t121?lang=EN&geo=PL&geo=NL&time=2020&unit=PPS_HH&coicop=CP01' \
  --output hbs_exp_t121_PL_NL_2020_CP01.json
```

1. Record **UTC retrieval timestamp**, exact URL, response status, publisher's last update and SHA-256 of the response **before** interpretation.
2. Validate that response is genuine **JSON-stat 2.0**, not an HTML error/captcha. Verify its `id` dimensions, positions and total `size`; do **not** assume array ordering or a fixed column index.
3. Inspect `PL` and `NL`, year `2020`, `freq=A`, `coicop=CP01` (food and non-alcoholic beverages), `unit=PPS_HH`. Confirm that each exact coordinate has a **non-null** numeric `value`.
4. Preserve any source `status` or observation flags, provenance and metadata. **A null/absent cell is not a zero and must not pass.**
5. Recheck the two values against Eurostat Data Browser for the **same** filter coordinates and note any discrepancy.
6. Perform separate rights review before publishing the response or a derived subset to the public repository. A link can be recorded even when a snapshot is not redistributable.
7. Repeat with `hbs_str_t224` **only after inspecting that table's own dimensions, units and category codes**. The source is a structure/share table, not directly additive spending.

**Status of execution in this review environment:** The Eurostat API endpoint could not be retrieved by available web access; a local network probe returned DNS resolution failure. Therefore the response status, observation values, flags, hash and value-comparison checks are all **NOT RUN / UNVERIFIED**.

## Explicitly separate the outputs

- `PPS_HH`: standardized purchasing power **per household per year/reference survey measure**. It is **not** a direct PLN/EUR bill and not a personal budget.
- `hbs_str_t224`: household category **shares**, not absolute amounts. Check the exact per-mille definition and household-type filter before use.
- Net income and paid working hours: **not** supplied by the expenditure table. A net-hours chart remains **BLOCKED** until an aligned denominator exists.
- A survey score on a 0–10 life-satisfaction scale: **not** a percentage of happy respondents.
- HBS 2020 is historically exceptional because of pandemic-related consumption changes; the future UI must state the context when applicable.
- Homeownership may involve **imputed rent**, a non-cash housing service cost. Showing it as cash mortgage or rent would mislead users.

## Acceptance matrix (current result)

| Gate | Evidence required | Current |
| --- | --- | --- |
| `HBS-2020-01` | Downloaded, pinned response with hash and retrieval timestamp | **BLOCKED / NOT RUN** |
| `HBS-2020-02` | Matching `PL` / `NL` cells, values and source flags at identical dimensions | **BLOCKED / NOT RUN** |
| `HBS-2020-03` | Rechecked official browser values + units, period, category and household definition | **BLOCKED / NOT RUN** |
| `HBS-2020-04` | Imputed-rent methodology and category comparability decision recorded | **OPEN** |
| `HBS-2020-05` | Source-specific redistribution and attribution cleared | **OPEN** |
| `HBS-2020-06` | Compatible net household/worker income and paid-hour model proved | **OPEN / separate indicator research** |

**STOP CONDITION:** If either PL or NL 2020 value is missing, flagged as unsuitable, or not definitionally comparable, do **not** compute a joint budget. Record the mismatch and propose a narrower analytical slice (or different year/series) for operator decision.

## Next action

Run the documented official API probe in a network-enabled environment; attach actual response checksum and selected metadata/flags as evidence; decide `PASS` or `ISSUES` on each gate. The **full LI-002 stage must not close until an accepted reproducible scenario per country or an explicit scope change exists**.
