# LI-004A — Sources Explorer implementation and review

**Date:** 2026-11-27 · **State:** implemented on review branch; static audit PASS; browser verification OPEN.

## CURRENT STATE

Operator explicitly accepted PR #11 as development-preview information and authorized its merge, checkpoint and commencement of LI-004. [PR #11](https://github.com/martynio/LivingIndex/pull/11) merged at `2ee65ee727c0c5f54ffaec8ec97c60212d9b6607`, verified on main with both expected parents. Final legal and production gates remain open; LI-002 numerical research continues independently.

## OBJECTIVE / IN SCOPE

Make the existing Sources route a useful EN/PL/NL catalogue of official source metadata. Present dataset identifier, institution, research country scope, topic, period, measure, evidence status, reuse conditions, comparison readiness, limitation and publisher link. Add local country and category filters, result count, reset and empty state. Render all cards in HTML so the catalogue remains readable without JavaScript.

## OUT OF SCOPE / CONSTRAINTS

No new datasets, economic figures, calculations, live source API requests, backend, analytics, storage, external scripts, policy approval or deployment configuration changes. Use existing Bootstrap/Pinegrow-compatible layout; equal-height cards within row/col. No data-source ranking. Use the canonical [source registry CSV](../research/SOURCE_REGISTRY.csv), checked metadata as recorded, not claims of current live coverage. Country filters mean research scope, not confirmed national observations; table periods do not imply continuous national data. Each card has one primary topic; working-hours-related source LI-SRC-004 is grouped with earnings and explicitly mentions hours. Only one source has a checked dataset-specific CC BY 4.0 license (LI-SRC-001); all remaining reuse conditions retain source-specific qualifications. All cards explicitly reject production calculation readiness.

**Eligibility decision:** exclude LI-SRC-007 because its registry status is RESEARCH_LEAD_NOT_FOR_PUBLICATION and redistribution is not approved. The remaining 13 source records are shown in each language, including LI-SRC-009 with its limited retrieved-pair evidence, without displaying numeric observations. Metadata display is not redistribution of source data. Registry unchanged.

## ACCEPTANCE CRITERIA / REQUIRED TESTS

- Exactly 13 distinct eligible IDs per locale; publisher URLs and research country scope match the registry; localized explanations preserve measure, evidence and rights limitations.
- Country/category controls, reset, empty state, result count and no-JS fallback; local script only, no network or browser storage from filtering.
- Preserve locale navigation, semantic headings, noindex, draft status, existing legal pages and research code.
- Static card/registry audit, all 18 filter combinations per locale, predicate tests, scope and documentation audit. Run existing Python shell verifier and HBS regression, then actual browser checks at 320/768/1440, keyboard, accessibility, zoom, storage and network.
- Stop on unknown source rights, invented source values/coverage, missing locale cards, unapproved external assets or failed verification.

## Observed implementation and evidence

Code checkpoint `948497d0049dd15c64de1d8be9edf9ee7c6109f4`. Three existing Sources pages, one local script, shared CSS extension and updated existing verifier. No additional runtime dependency.

| Check | Result |
| --- | --- |
| Registry parity | PASS — 39 cards (13 × 3), all 39 publisher links and country codes matched canonical registry |
| Filter predicate | PASS — seven synthetic predicate cases executed in authoring runtime; same function serialized into the local script |
| Filter data matrix | PASS — 18 combinations per locale checked from committed HTML; identical counts across locales; PL and NL each match 10 research candidates |
| Static source review | PASS — unique IDs, local deferred script, noindex and draft research message; no fetch, XHR, storage, cookie writes or innerHTML in script |
| Python verifier and HBS regression | NOT RUN in this tranche; HBS implementation/tests unchanged |
| Browser rendering and interactive filter tests | NOT RUN; existing execution-environment limitation remains unresolved |
| Publication | NOT RUN for LI-004A; review PR requires approval before merge to main |

The existing Python verifier now checks exact eligible IDs and links, allows only local sources-explorer.js on the Sources route and approved publisher anchors, and adds browser filter/reset checks. This verifier has not yet been executed in this tranche. The static review is not a full browser or accessibility test. No fresh external source retrieval was attempted; claims are based on the already reviewed registry.

## Next

Review the catalogue as a development-preview feature, obtain operator acceptance and checkpoint; inspect deployed visuals and controls before full LI-004 completion. Preserve independent data rights, numerical feasibility, legal and production release gates.
