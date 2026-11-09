# Living Index (LI)

**The real cost of living — measured in money and time.**

> **Project status: Proposal / data feasibility research.** This repository does not yet contain a released application or validated cost-of-living datasets.

Living Index is an independent, public-facing project exploring how everyday expenses, wages, purchasing power, and the working time needed to afford essential goods change across countries, years, and generations.

It is designed to make historical comparisons easier to explore **without treating averages as individual experiences, estimates as observations, or missing data as zero**.

## What Living Index is designed to do

- **Explore:** select a country and year for a clear overview of living costs and earnings.
- **Understand time:** express selected expenses as an equivalent number of paid working hours when sufficiently defined net-pay and working-time data exist.
- **Compare carefully:** contrast countries or years only where measures and populations are methodologically compatible.
- **Inspect the evidence:** reveal source, period, unit, population, transformations, data quality, and limitations next to each visualization.
- **Go deeper when needed:** access more detailed household, age, housing, and time scenarios as suitable evidence becomes available.
- **Share responsibly:** generate reproducible links and annotated PNG exports.

**Initial research scope:** the Netherlands and Poland. Further countries and historical coverage depend on source availability and comparability. The ambition to examine data back to 1980 is **not** a claim that complete series already exist.

**Interface languages planned:** English, Polish, Dutch.

## Principles

1. **Evidence before narrative.** The project does not set out to prove that any country or generation had it better.
2. **Transparency over apparent precision.** Observed values, transformations, reconstructions, and unavailable measures must remain distinguishable.
3. **Money and time are separate views.** An hourly earning equivalent is not automatically a measure of actual free time.
4. **No silent gap filling.** Missing or incompatible inputs must be disclosed, not guessed.
5. **Progressive disclosure.** A simple default view can expand to a detailed, well-documented analysis.
6. **Survey outcomes are not synthetic scores.** Actual reported life satisfaction takes priority; a future model-derived index would be separate and explicitly labeled.

## Current phase

`DISCUSS → RESEARCH → DECIDE → REPO CHECK → EXECUTE → VERIFY → COMMIT / RELEASE GATE`

The [Project Proposal v1.0](docs/project/LI-PP-001-PROJECT-PROPOSAL-v1.0.md) defines intended features and boundaries; it is **not** evidence that those features have been implemented.

The next project gate is a **Poland / Netherlands data-feasibility assessment**, including coverage by indicator and year, definitions, source terms, and licensing. See [Research](docs/research/README.md).

## Repository layout

| Path | Purpose |
| --- | --- |
| [`docs/project/`](docs/project/) | Approved or proposed project artifacts and scope |
| [`docs/research/`](docs/research/) | Source discovery and data-feasibility evidence |
| [`docs/methodology/`](docs/methodology/) | Definitions, comparability and calculation contracts |
| [`docs/decisions/`](docs/decisions/) | Architecture and product decisions with rationale |
| [`data/`](data/) | Source snapshots and curated, traceable datasets (not yet populated) |
| [`web/`](web/) | Future static interface, assets, and PL/EN/NL localization |
| [`tests/`](tests/) | Future repeatable validation and regression checks |

For contributors and AI agents, start with [AGENTS.md](AGENTS.md), [current project status](docs/project/PROJECT_STATUS.md), and the [roadmap](docs/project/ROADMAP.md). All substantive changes follow the [work protocol](docs/governance/WORK_PROTOCOL.md) and are recorded in the [work log](docs/logs/WORK_LOG.md).

See the [documentation index](docs/README.md) for full navigation.

## Data integrity and licensing

No statistical series has yet been imported or approved for publication. Source availability, licensing, attribution, and transformations must be checked **before** redistribution or derived visualizations are released.

**Public repository ≠ open-source license.** A license for code and separate dataset usage terms have **not yet been selected**. Until then, repository visibility does not grant general reuse rights. Contributions are welcome as discussions and evidence; please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting changes.

## Contributing

Source leads, methodological corrections, and documented data-quality concerns are especially useful during research. Start with an issue and provide the exact source or definition involved. Do not submit fabricated sample statistics as if they were observations.

---

*Living Index is in planning and research. Its descriptions are goals, not claims of launched functionality.*
