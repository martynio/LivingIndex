# LI-006A — Dashboard Development Preview

**Date:** 2026-11-27 · **State:** implemented on review branch; browser acceptance and production data gates OPEN.

## CURRENT STATE

Operator explicitly approved [PR #15](https://github.com/martynio/LivingIndex/pull/15) and authorized LI-006A with three independent modes and explicit availability status. Verified main `7271543950ef610e9c663cbd67758bd19c90173e`, merge parents 3465b1eed6233e7a5979bac8118f710ee5e67090 and ad915bd6add46303a27173726e8cba20b3073412. Before merge, reran 29/29 economic tests, exact accepted Python blob identity and all 12 actual PPS category replays against the archived report; ZIP and JSON digests matched accepted evidence. [Pages run 46034792231](https://github.com/martynio/LivingIndex/actions/runs/46034792231): completed/success, head `7271543950ef610e9c663cbd67758bd19c90173e`. No approved statistical versions; [manifest](../../data/curated/manifest.json) stays empty.

## OBJECTIVE / IN SCOPE

A multilingual static dashboard on the existing Bootstrap/Pinegrow-compatible website; EN/PL/NL dashboard route and navigation across every locale page. Three independent analysis modes with explicit research/official availability. Only hypothetical cash and paid-hour calculations; PPS research coverage and provenance without republishing unapproved values.

- National budget: choose PL/PLN or NL/EUR, month/year and person/household; enter hypothetical nonnegative cash income and total cash expenditure. Signed cash balance, share of income, undefined share for zero income. Do not call this statistical savings.
- PPS: fixed research reference year 2020, PL/NL pair, twelve ECOICOP category options, 24/24 research cells retrieved, reference LI-SRC-009 / hbs_exp_t121 / PPS_HH; link to the exact accepted research evidence. No economic values or totals on the dashboard, no PPP/FX conversions. Categories are short descriptive labels. No false year selector: only the retrieved wave is advertised.
- Work time: independent PL/NL currency and month/year context, hypothetical matched worker's net employment earnings, paid hours and cash cost. Positive earnings and hours required; cost nonnegative. Net hourly earnings and cost-equivalent paid hours; no intermediate rounding.
- Empty default inputs, explicit simulation and unavailable status, locale-specific decimal display, reset, invalid and missing states. Country/period/basis changes clear the corresponding scenario; mode changes retain independent temporary page state. No JavaScript fallback displays all three research-status sections, not inert interactive fields.
- Local JavaScript only: arithmetic mirrors the accepted Python engine using six-decimal BigInt fixed point and half-up ratios to two decimal places; equivalent cash-balance numeric precision is retained without unnecessary trailing zeros. Accept dot or comma decimals (no thousands separators) and nonnegative bounded values, a subset of the Python input representation. The browser does not execute Python or import unapproved observations. The Python contracts remain authoritative. No personal information requested; users are told to use hypothetical values only. No form submission, network call, storage, analytics, new dependency, external embedded asset or backend. Privacy/cookie preview copy updated narrowly to explain local hypothetical processing and scripts; final policy remains under review.

## OUT OF SCOPE / CONSTRAINTS

No production figures, chart of national statistics, additional research years, data fetch, manifest promotion, new source registration, code changes to Python economic engines, deployment workflow/settings, final legal or production release. No personal budgets, fabricated country series or misleading cross-country comparison. Existing source registry and HBS research remain unchanged. Maintain noindex, accessible labels and main/locale navigation, equal result cards with row/col, no transform scaling.

## ACCEPTANCE CRITERIA / REQUIRED TESTS / STOP CONDITIONS

- Three distinct panels and status messages in each locale; language switch stays on corresponding route; local links/assets resolve; no approved-data claims.
- Verify signed balance, zero income, invalid inputs, positive denominator, exact decimal arithmetic and no intermediate rounding. Run JavaScript edge tests and Python parity. Test mode isolation, category choice, currency/period reset, clear and stale-result rejection. Static no-JS status and no default numbers.
- Browser verification at 320/768/1440, root/subpath, focus, native zoom, console, storage and network, screen reader and accessibility review; do not claim full acceptance if unavailable. Stop on incorrect arithmetic, invalid source claims, unexplained network/storage, wrong currency interpretation, or broken navigation. Development-preview merge requires separate operator approval.

## Observed verification

- Implementation checkpoints 36ff7f3d1c780982e520d48980831587da94c396 (dashboard), 2fd22dc6e506958c020d4bc69535111382dbbc74 and c5bbe7ff046c695aaf1e877990415dbc041229ff (navigation/disclosure), a4da8d116c2eadc2eb9a91edff4a75d626b7e162 (tests), `ab40a70bb4847c03d6ce7a9ee99cd1191a225c0a` (navigation correction). Initial oversized connector batch rejected; no unintended ref update; smaller batches succeeded.
- `node tests/test_dashboard.cjs`: 22 arithmetic assertions + 39 mock-DOM assertions PASS. Mock DOM is not a browser.
- `python tests/verify_dashboard_parity.py`: 500 deterministic synthetic cases PASS (250 budget, 250 work-time) against the accepted Python engine. Compare exact Decimal numeric balances and formatted two-decimal ratios; no national statistical values.
- Exact locally executed Git blob identities: dashboard.js 91dac74d956ba8a5c72e662c26dcce481636f36a; test_dashboard.cjs 32d3143518f0793af2da2d9f8086e0f195e70986; verify_dashboard_parity.py 4a9bae54bd7a650ef5209d4d8f0435b58b7f100c. Accepted Python 29/29 and 12/12 actual PPS replays rerun before merge; Python engine files unchanged.
- Static read-back audit of all 27 locale HTML pages: 453 relative href/src references resolve, 51 external anchor references match registry, GitHub documentation or pinned evidence, 3 locale switches on each page; correct main menu, headings/noindex, 12 PPS categories, labeled blank inputs and local deferred script. Initial English Sources navigation insertion mistakenly affected locale navigation; corrected in `ab40a70bb4847c03d6ce7a9ee99cd1191a225c0a`, all three locale audits then passed. No actual external link fetch claimed.
- Browser loopback probe attempted with installed Chromium and Playwright; ERR_BLOCKED_BY_ADMINISTRATOR. Full browser verifier (including newly added interaction cases), real layout/keyboard/zoom/AX, storage/headers and accessibility scans NOT RUN. Existing HBS 17/17 regression historical, not rerun. Full Python shell verifier NOT RUN; separate committed-source static read-back used instead. No screenshot or deployment of this branch claimed.

## NEXT GATE

Review LI-006A and accept for main development preview only; verify actual rendered behavior. Real national input/source compatibility, approved version records, PPS methodological and rights review, aligned net-paid-hours denominator and legal/production gates remain open. No full LI-005 or LI-006 closure. Expected preview after approved merge: web/dashboard.html, web/pl/dashboard.html, web/nl/dashboard.html under the existing GitHub Pages base path.

## Operator acceptance — 2026-11-27

PR #16 accepted as development preview; verified main `2c23e25fbba129513f7ebd7419b75b142cdf7673` and both parents, Pages run 46044174341 successful. Exact previously tested blobs matched; tests not rerun in this tranche. See [first descriptive data candidate](LI-006B-CBS-DESCRIPTIVE-PREVIEW.md). Browser and production gates remain open.
