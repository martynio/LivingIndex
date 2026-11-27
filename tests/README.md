# Verification

Existing synthetic HBS regression tests remain unchanged. Run from the repository root:

```sh
python -m unittest discover -s tests -p 'test_hbs*.py' -v
```

LI-003A adds a separate local verifier. Install test dependencies in an isolated Python environment if needed:

```sh
python -m pip install beautifulsoup4 playwright
python -m playwright install chromium
python tests/verify_web_shell.py evidence/li-003a --static-only
python tests/verify_web_shell.py evidence/li-003a
```

The first command with the verifier checks static markup/relative paths/locale parity. The second launches a loopback-only server and browser, covering root and repository subpath navigation at 320, 768 and 1440 CSS pixels, accessibility-tree landmarks, keyboard skip/focus, storage/cookie/network/console checks and CSS 200% zoom proxy; it writes screenshots and JSON to the chosen local directory. Set CHROMIUM_PATH to a local installed Chromium executable if appropriate. Browser checks require an environment that permits loopback navigation. A CSS zoom proxy and AX tree checks are not equivalent to browser zoom or a full automated accessibility audit: also verify native 200% zoom, all keyboard focus paths, contrast and an accessibility scan manually/with an appropriate tool before accepting LI-003A. Do not publish test screenshots or the site without approval.

See [LI-003A verification](../docs/project/LI-003A-VERIFICATION.md) for observed results. Future data, calculation, source and scenario tests require separate authorized work.

## LI-003B external navigation

The verifier permits exactly two GitHub documentation URLs as user-activated anchors on privacy and cookies routes, with noreferrer. Other external references remain disallowed. This is not permission for embedded external assets. Full verifier execution remains required; see [LI-003B evidence](../docs/project/LI-003B-PREVIEW-TRANSPARENCY.md).

## LI-004A source catalogue checks

The existing verifier checks eligible registry IDs, publisher anchor URLs, country scope, local deferred filter script and browser filter/reset behavior. Source metadata is not a production dataset. See [LI-004A review](../docs/project/LI-004A-SOURCES-EXPLORER.md) for actual checks and remaining browser evidence.

## LI-005A

Run `python -m unittest discover -s tests -p 'test_economic_research.py' -v`. The adapter uses only Python standard-library modules; the tests use synthetic fixtures. To validate an actual archived report (outside the repository), run `python scripts/economic_research.py /path/to/report.json --sha256 REPORT_SHA256` using the independently recorded report hash. Optional --output must be a new file outside the repository. See [contract and observed verification](../docs/project/LI-005A-RESEARCH-DATA-CONTRACT.md). No production promotion.

## LI-005C

Run `python -m unittest discover -s tests -p 'test_economic*.py' -v` for engine and adapter regression. For actual PPS replay, call `pps_comparison` from `scripts/economic_engine.py` with the original report bytes and independently recorded digest for each CP01–CP12. Do not commit outputs. See [contract and verification](../docs/project/LI-005C-ECONOMIC-ENGINE.md). Monetary/time inputs are hypothetical only.

## LI-006A

Run `node tests/test_dashboard.cjs` for arithmetic and mock-DOM checks; run `python tests/verify_dashboard_parity.py` for 500 synthetic cross-language arithmetic cases (Node and Python required, no external dependencies). The existing shell verifier now covers 27 locale pages and dashboard browser interactions. See [observed verification](../docs/project/LI-006A-DASHBOARD-PREVIEW.md). Mock-DOM and static results do not substitute for real browser checks.

## LI-006B

The shell verifier now checks the CBS descriptive candidate manifest, snapshot and static localized values, with source/rights anchor allowlist. Run the existing static-only and browser commands before claiming full verification. Observed committed-source read-back evidence and limits: [LI-006B review](../docs/project/LI-006B-CBS-DESCRIPTIVE-PREVIEW.md).
