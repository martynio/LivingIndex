# Research — source feasibility

**Status: not started.** The first research deliverable is `LI-RESEARCH-001`: a **PL / NL Data Feasibility Matrix**.

## Questions to answer

For every proposed indicator and country:

- What is the **primary source** and exact dataset or table ID?
- Which **years** actually exist, at what frequency and geographical granularity?
- What population, unit, statistical measure, and revisions does it represent?
- Is it nominal/real, gross/net, worker/household, mean/median, observed/derived?
- Which transformations are required to compare it with other indicators?
- Can data be downloaded, processed, cached, and redistributed under its terms?
- Are there historical discontinuities or contextual warnings?

## Matrix fields (proposed, not populated)

`country | indicator | source_id | source_url | coverage_start | coverage_end | frequency | unit | population | measure | quality_status | comparability | license_status | checked_on | notes`

**Do not fill the matrix with inferred coverage.** Historical CPI availability alone does not establish comparable housing budgets, net hourly wages, or life-satisfaction series.

## Gate out of research

At least one genuinely source-supported, internally consistent baseline scenario for **each** of Poland and the Netherlands, with explicit limits and coverage gaps. The operator then decides the implementable MVP.

See [methodology](../methodology/README.md) and [proposal](../project/LI-PP-001-PROJECT-PROPOSAL-v1.0.md).
