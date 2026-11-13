# LI-002 — Source Registry & Legal Research: scoped research tranche

**Date:** 2026-11-10 · **Status:** **RESEARCH IN PROGRESS / OPERATOR REVIEW PENDING**.

## Objective

Create a credible, traceable first-pass **Poland / Netherlands** primary-source registry, identify historical-coverage gaps and specific reuse / legal-preparation requirements before any public Sources Explorer or living-cost graph is implemented.

## In scope (this tranche)

- Discover public, official candidate sources covering CPI, wages, household expenditures, and survey-reported life satisfaction.
- Record precise source URLs/IDs, publisher-reported coverage, measure, historical caveats and separate reuse/compatibility statuses.
- Form an explicit PL/NL feasibility matrix and next evidence needed to demonstrate a single valid scenario.
- Record official-source legal research for hosting, cookies, privacy notice, terms and data licensing.
- Update work log, status and next-contributor handoff.

## Out of scope

- Importing or transforming numerical observations, raw data redistribution, automated scraping.
- Declaring country-to-country household budgets comparable or net hourly wage available.
- App/frontend template, UI source cards, live site, forms, cookies, legal-policy publication.
- Additional countries, composites, generational indices, commuting estimates or custom AI functionality.
- LI-002 completion/approval, LI-003 implementation or merge to `main` without operator gate.

## Acceptance criteria for this research tranche

- At least one candidate official source for each of CPI, wage, household spending and life satisfaction.
- Country evidence and source-access/reuse qualifications recorded without implying a data import.
- Explicit metadata/rights/comparability states with no fake observations or years.
- Legal requirements expressed conditionally on future host and real data flows.
- A reviewable PR, corrected documentation links, work-log entry, handoff and tested branch integrity.

## Full LI-002 stage exit (not yet satisfied)

- Using verified public HBS IDs `hbs_exp_t121` and `hbs_str_t224`, retrieve actual PL/NL 2020 observations, units, flags and harmonization details.
- Verify one complete, consistent scenario **per country**, or revise proposed MVP scope.
- Resolve dataset-specific reuse and attribution decisions for proposed public cards.
- Confirm actual hosting/data-flow decisions needed for LI-003 policy writing.
- Obtain operator approval and commit gate before dependent website work.

This document distinguishes **first-pass research** from the final LI-002 decision gate.
