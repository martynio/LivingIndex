# LI-006C — GUS descriptive data candidate

**Date:** 2026-11-27 · **State:** review ready; operator acceptance required. No production calculation approval.

## Accepted baseline

Operator explicitly approved PR #17 and CBS version cbs-86272ned-nl-2020-v1 for descriptive display only; approval recorded in commit 731a36cc2b0195e667b1e305f2586bdd368c81eb, manifest, registry and three locale views. Verified [merge](https://github.com/martynio/LivingIndex/commit/09e3f4e2a23f57d8ea349cd87eff7f285dd915f6) and main, parents 2c23e25fbba129513f7ebd7419b75b142cdf7673 and 731a36cc2b0195e667b1e305f2586bdd368c81eb. [Pages run 46045974842](https://github.com/martynio/LivingIndex/actions/runs/46045974842) completed success. Original CBS values unchanged. Operator authorized LI-006C.

## Scope and evidence

Three descriptive aggregate values for Poland 2020, monthly mean per household member, households total. [GUS annual report](https://stat.gov.pl/files/gfx/portalinformacyjny/pl/defaultaktualnosci/5486/9/15/1/budzety_gospodarstw_domowych_w_2020.pdf), Warsaw, August 2021, printed p.18, Synteza/Wstęp opening paragraph; [earlier information release](https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5486/3/20/1/sytuacja_gospodarstw_domowych_w_2020_w_swietle_wynikow_badania_budzetow_gospodarstw_domowych.pdf), 31 May 2021, printed p.1. Both publisher text extracts agree at the reported whole-PLN precision.

| Measure | Value (PLN/person/month) |
| --- | ---: |
| Mean disposable income | 1919 |
| Mean total expenditure | 1210 |
| Mean consumption expenditure | 1165 |

These are published rounded headline values, not transcription of unrounded detailed tables. Same underlying survey in two publications, not independent samples. The report documents pandemic disruption including a switch from in-person to telephone collection. [GUS definition](https://stat.gov.pl/metainformacje/slownik-pojec/pojecia-stosowane-w-statystyce-publicznej/63%2Cpojecie.html) includes monetary and nonmonetary disposable income. Consumption is part of total expenditure; do not add them together. CBS annual household means differ in basis, period, currency and coverage. No comparison, subtraction, savings, income-share or paid-hours calculation authorized.

## Rights

The [GUS BIP reuse notice PDF](https://bip.stat.gov.pl/kontakt/ponowne-wykorzystywanie-informacji-sektora-publicznego/?pdf=1), checked 27 November 2026, describes the public-sector reuse regime under the 11 August 2021 open-data law. Indicate source, creation/acquisition date and processing; GUS disclaims responsibility for reuse processing results. The annual report also requests source acknowledgment. The selected public aggregate facts are transcribed with dates, page references, source and notice links; labels translated, no numerical transformations. No CC BY license asserted for GUS, no copied images or restricted data. This is limited review for these three facts, not a general legal clearance.

PDF extracted text was accessible; screenshot attempts for both data PDFs and rights PDF timed out. No visual page inspection or raw PDF bytes/hash retained. HTML landing page and BIP HTML timed out; PDF text provides the evidence. No claim of independent survey or full table validation.

## Implementation and verification

[Snapshot](../../data/curated/gus-hbs-pl-2020-v1.json), Git blob 2ed02e2f9ca412ef6f57cb9420695e9650b67e6b. [Manifest](../../data/curated/manifest.json) retains the accepted CBS descriptive version and one pending GUS candidate. approved_versions empty; both calculation_eligible and production_eligible false. LI-SRC-016 added to CSV/Markdown and three source catalogues, separate fixed Poland section in each dashboard, no connection to hypothetical inputs. Static HTML derived from snapshot in authoring; no runtime external requests or calculation changes. Existing shell verifier extended.

Code checkpoint `7dcd12b5396bb546a8c87e0140dab9d763b39981`. Static read-back PASS: 15/15 displayed values (9 GUS, 6 CBS), 45/45 source cards/links/country scopes across 3 locales, 16 registry entries/15 eligible, correct snapshot contexts and no input/script/form inside descriptive sections. Initial authoring script syntax error corrected before successful commit; no unintended ref update. Full Python verifier, browser and arithmetic/HBS regressions NOT RUN in this tranche. No candidate deployment claimed.

## Gate / next

Explicit operator acceptance of exact GUS descriptive version required before merge and status change. Keep both statistical panels separate, calculation inventory empty. Next LI-006D: source-specific PPS evidence and reuse/methodology review, not automatic promotion. No stage closure, production release, or new time-work model.
