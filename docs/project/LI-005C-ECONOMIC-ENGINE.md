# LI-005C — Economic Engine: separated calculation contracts

**Date:** 2026-11-27 · **Status:** implemented on review branch; research/simulation only.

## CURRENT STATE

Operator explicitly accepted [PR #14](https://github.com/martynio/LivingIndex/pull/14) and authorized LI-005C with separate national budgets, PPS and work-time models. Verified main `3465b1eed6233e7a5979bac8118f710ee5e67090`, parents b5af5cfbbd438eb6363d724819ccdcccdf072c40 and b16a42186c5aa1d87cc8377ccbcbc9c6373efb7a. [Pages run 46033414894](https://github.com/martynio/LivingIndex/actions/runs/46033414894) completed successfully at the merge SHA. Actual HBS report replay and 13/13 adapter tests repeated before merge. [National budget research](../research/LI-005B-NATIONAL-BUDGET-EVIDENCE.md) and [matrix evidence](../research/HBS_2020_MATRIX_RUN_EVIDENCE.md) are accepted research, not production inputs. Approved manifest remains empty.

## OBJECTIVE

Implement deterministic, separate offline contracts that reject incompatible inputs, preserve provenance and missingness, and provide reusable calculation primitives without implying that real country scenarios are approved.

## IN SCOPE

Standard-library Python [economic_engine.py](../../scripts/economic_engine.py) exposes three pure functions. Each result is a JSON-compatible dictionary with schema_version 1.0.0, explicit mode/kind and production_eligible=false. No production promotion entry point.

| Mode | Function | Result |
| --- | --- | --- |
| National budget | national_budget(income, expenditure) | Hypothetical cash income, total cash expenditure, signed balance, expenditure share or null |
| PPS comparison | pps_comparison(raw_report, report_sha256, category) | Actual validated report pair for one CP01–CP12 category; original observations/flags, metadata/provenance/review, pair status |
| Work time | work_time(net_earnings, paid_hours, cost) | Hypothetical matched worker's net hourly earnings and cost-equivalent paid hours |

### National and work-time input contract

Each monetary/time input is an object with exactly scenario_id, country, year, currency, period, basis, population, kind, measure and value. All seven scenario-context fields must match across inputs. kind must be hypothetical. Country PL requires PLN, NL requires EUR; period month or year; year integer 1980–2100 is only a scenario identifier range, not a claim of historical currency validity or data coverage. Population and scenario identifiers are caller-declared assumptions, not verification of real statistical alignment. Basis person or household for budget, worker for work time. Value is a decimal string with at most 12 integer digits and six fractional digits; no floats, booleans, null, exponent notation or non-finite numbers. Currency in a paid_hours input is the common monetary scenario context, not the unit of the hours; measure identifies that its value is in hours.

National budget requires cash_disposable_income and cash_total_expenditure. Both nonnegative in this initial supported scope. Deficit remains negative. Balance = income minus expenditure. Expenditure share = 100 × expenditure / income; zero income yields null share, not zero. Cash balance is not statistical savings. No summing HBS categories or conversion of consumption including imputed rent into cash expenses. The actual GUS/CBS research figures are not connected to this function.

Work time requires net_employment_earnings, paid_hours and cash_cost. Net earnings and paid hours must be strictly positive, cost nonnegative. Net hourly earnings = net earnings / paid hours. Cost-equivalent paid hours = cost × paid hours / net earnings, with no intermediate rounding. Reject gross earnings, actual reference-week hours, PPS, other currencies and mixed worker/household bases. This is a hypothetical equivalent, not measured time, free time or a household average. No annualization or currency conversion.

Calculation uses Decimal with 50-digit local context. Cash balance retains decimal precision; shares, hourly rate and equivalent hours are returned as decimal strings rounded half-up to two decimal places. This display precision is not evidence of statistical accuracy.

### PPS input contract

Call accepted LI-005A normalize on raw report bytes and independently recorded report SHA-256; do not trust pre-normalized user flags. Restricted to existing PL/NL 2020 hbs_exp_t121 scope. Preserve original values, country, category, source flag, flat index, availability, unit PPS_HH, source_id, dataset, mean, annual frequency, population, provenance and pending reviews. Return PL then NL. Pair status missing if either value absent, otherwise flagged if any source flag is non-null, otherwise review_required. A null flag is not quality certification. No aggregate totals, ratios, conversion, cash or paid-hour calculations. Category absent in a legacy CP01 report is rejected. No independent official reconciliation is claimed.

## OUT OF SCOPE / CONSTRAINTS

No website changes, new data retrieval, real national/time calculation inputs, approval manifest edits, new datasets, derived production JSON, API, backend, dependency, deployment configuration or legal approval. No personal budget collection or persistence. Hypothetical inputs are caller assumptions and are not a synthetic national series. This tranche is a simulation/research engine, not the final production dataset or authorization layer.

## ACCEPTANCE CRITERIA / REQUIRED TESTS / STOP CONDITIONS

- Separate function outputs, version and nonproduction status; matching contexts required; no silent population/period/unit conversion.
- Correct signed cash balance, zero denominator behavior, decimal arithmetic, work-hour formula without intermediate rounding.
- Reject invalid numeric inputs, gross earnings, actual hours, missing/extra monetary fields, wrong basis, country/currency mismatch, research input promotion and invalid PPS category/hash.
- Preserve PPS missingness, flags, review and provenance. Replay all twelve categories of archived real matrix using exact accepted adapter. No output values written to repository.
- Run both economic test suites, compile new files, match exact Git blob identities, verify scope and append-only audit. Stop if any test, digest or alignment validation fails. Real production eligibility remains a separate operator-reviewed evidence gate.

## Observed verification

- Code checkpoint `0bc290902cc7f51493a30f34a25167a13d4168a2`. New engine blob `12b5eb34fd9d36adc34e3fc8e5e6b79e931c1dee`; test blob `2e588917ce6d0337b7e226dae69dba9a6fe379be`; exact locally tested bytes matched GitHub.
- `python -m unittest discover -s tests -p 'test_economic*.py' -v`: **29/29 PASS** (16 new + 13 unchanged adapter tests). Initial run revealed a duplicate keyword in a test helper, corrected before final run. Python compilation of new files PASS.
- Downloaded matrix ZIP and extracted report digest matched accepted evidence; 24/24 normalized before merge. Real report replay through pps_comparison: 12/12 category pairs PASS, all review_required and production_eligible=false. No output file created.
- Earlier 17/17 hosted HBS tests remain historical evidence from run 46032585277; not rerun in this implementation tranche. Browser tests not run; no UI changes. No live new retrieval. No new numerical source approval.

## NEXT GATE

Accept this code as the bounded engine foundation only. Then select and verify exact national scenario input definitions, approve source-specific versions and rights, and establish a genuinely aligned net-paid-hours denominator or explicitly label a simulation. A separately scoped LI-006 development dashboard may present the three distinct modes and unavailable states, but must not present unapproved numerical results as official. No full LI-005 closure.

## Accepted checkpoint — 2026-11-27

Operator approved PR #15; merge verified at `7271543950ef610e9c663cbd67758bd19c90173e` with both parents. 29/29 economic tests and 12/12 actual PPS replays rerun successfully. LI-006A separately authorized; see [dashboard preview](LI-006A-DASHBOARD-PREVIEW.md). No production input approval.
