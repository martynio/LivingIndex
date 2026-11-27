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
