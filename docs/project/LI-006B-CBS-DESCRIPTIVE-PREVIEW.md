# LI-006B — First verified descriptive data candidate

**Date:** 2026-11-27 · **Decision:** READY FOR OPERATOR REVIEW — descriptive display only; not a production calculation input.

## CURRENT STATE

Operator explicitly accepted [PR #16](https://github.com/martynio/LivingIndex/pull/16) as development preview and authorized verification and admission of first real economic data. Main verified at `2c23e25fbba129513f7ebd7419b75b142cdf7673`, parents 7271543950ef610e9c663cbd67758bd19c90173e and 496153ef375c5ee275023c45b7d5fc20ac555d01. [Pages run 46044174341](https://github.com/martynio/LivingIndex/actions/runs/46044174341) completed successfully at that SHA. Exact previously tested dashboard JS, test and parity blobs checked before merge; earlier test counts are historical, not rerun in this tranche. Full rendered verification remains open.

## OBJECTIVE AND SCOPE

First source-traceable descriptive statistical slice on the dashboard. Prefer directly inspectable primary-source cells to forcing unresolved HBS or incompatible cash calculations. Two final 2020 CBS means, NL private households with income, annual household basis. Register LI-SRC-015, retain versioned two-cell snapshot and display in the budget mode as a fixed, clearly separated Netherlands statistics section in EN/PL/NL. Existing hypothetical inputs remain blank and independent; selecting scenario country does not change this fixed NL panel. No numeric PL or PPS results admitted. Synchronize LI-SRC-009 status with actual 24-cell research evidence.

## Source and rights evidence

| Measure | CBS 86272NED 2020 | Corroboration |
| --- | --- | --- |
| Gemiddeld besteedbaar inkomen | 46.4 thousand EUR per household/year | CBS 83739NED, same population and year, 46.4 |
| Gemiddeld besteed bedrag | 35.2 thousand EUR per household/year | CBS 83739NED, 35.2; CBS 85419NED, category 000000, Particuliere huishoudens, 2020, 35.2 |

- [CBS 86272NED](https://www.cbs.nl/nl-nl/cijfers/detail/86272NED), Welvaart van particuliere huishoudens; kerncijfers, modified 25 November 2026 06:30 as displayed, accessed 27 November 2026. Row Particuliere huishoudens / 2020; two columns as above; the table states years 2011–2024 final and 2025 provisional. Only the two selected 2020 values verified for this slice. Population: private households with income, as of 1 January of reporting year. Income definition deducts income transfers, specified insurance premiums and income/wealth taxes from gross income; expenditure covers goods/services for direct needs. These definitions do not establish a cash income/expenditure pair.
- [CBS predecessor 83739NED](https://www.cbs.nl/nl-nl/cijfers/detail/83739NED), stopped 6 February 2026; same row and columns, 2020 final. [CBS 85419NED](https://www.cbs.nl/nl-nl/cijfers/detail/85419NED), modified 10 March 2023, total consumption expenditure corroborates 35.2. Corroboration across official published tables, not independent survey measurements.
- [CBS copyright notice](https://www.cbs.nl/en-gb/over-ons/website/copyright), checked 27 November: general CC BY 4.0 unless otherwise specified; attribution mandatory, no implied endorsement. No exception identified on the selected primary table in reviewed HTML. No CBS logo, design or protected images reused. The dashboard credits CBS, table identifier, access date, rights notice and nonendorsement; labels translated, numerical values unchanged. This is a narrow source-specific review, not final legal advice or blanket rights approval.
- [Eurostat reuse notice](https://ec.europa.eu/eurostat/help/copyright-notice) and [HBS metadata](https://ec.europa.eu/eurostat/cache/metadata/en/hbs_esms.htm) reviewed again. Direct official API cell query remains inaccessible through review tool; maintenance notice for 27 November 16:00–19:00 was visible, but causation is not established. Full PPS matrix stays research-only pending existing independent-cell and methodology gates. CBS OData metadata endpoint also inaccessible; HTML table, not API bytes, is the verified source of this tranche.

## Version and admission contract

[Snapshot](../../data/curated/cbs-86272ned-nl-2020-v1.json) is a manual transcription of two source cells in the published unit, decimal strings. No conversion or raw byte retention. Source dates, original labels, corroboration, rights and review state retained. Git blob d8fd20b8f2ba4a840ce869cc92d0bf97caf0c971. [Manifest](../../data/curated/manifest.json) retains empty approved_versions and lists one descriptive_preview_candidates record. Candidate is not approved until explicit operator decision; calculation_eligible and production_eligible remain false. Static HTML is generated from the same snapshot at authoring time; no runtime data requests. A subsequent explicit acceptance must record the accepted descriptive version and update visible status before/with merge. No promotion to the production calculation inventory. Public review branch is not confidential; only public aggregate cells are staged.

## OUT OF SCOPE / STOP CONDITIONS

No cash savings, subtraction, expenditure share, PL/NL comparison, PPS conversion, worker-hour estimate, additional years, source-wide approval, hypothetical prefill or production release. No changes to JS calculation or Python economic engine. No new dependencies, hosting changes or final legal approval. Stop on mismatched source values, units, population, rights, unexpected calculation integration, or premature approved status.

## ACCEPTANCE CRITERIA AND OBSERVED VERIFICATION

- Exactly two cells from selected official table, both corroborated in predecessor and expenditure additionally in category table: PASS, manual publisher HTML read-back. Published precision retained (thousands of EUR, one decimal).
- Committed snapshot and manifest inspected; 6/6 localized displayed values match the exact snapshot, fixed NL/2020 context, source and rights links, credit, no input/script/form in descriptive section: PASS.
- Registry has 15 records, 14 eligible after excluding LI-SRC-007. Three localized catalogues: 42/42 cards, publisher links and country scope match registry, initial 14/14 count; LI-SRC-009 coverage updated: PASS.
- Existing shell verifier extended to assert snapshot/manifest and exact rendered values and allow two user-activated CBS links only in descriptive section. Full Python verifier and browser regression NOT RUN; earlier dashboard arithmetic and HBS tests not rerun. Static committed-source checks are not browser testing or a source byte hash. No live deployment of candidate branch claimed.

## NEXT GATE

Approve this exact descriptive version and dashboard display only, record the operator decision and merge to main. Then check rendered Pages preview. Continue GUS exact source definitions/rights and PPS official-cell reconciliation; national cash and paid-hours calculation gates remain closed. No full LI-005/006 closure.
