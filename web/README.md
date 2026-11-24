# Web interface

**Status: LI-003A development shell — branch review only. Do not publish.**

Static, semantic HTML and locally served CSS, compatible with a conventional Pinegrow/Bootstrap workflow. No build step, JavaScript, third-party service, or dataset is required. The neutral navy/teal palette and text wordmark are provisional.

## Local preview

From the repository root, run:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory web
```

Open `http://127.0.0.1:8000/` in your browser. For Polish and Dutch, use `/pl/` and `/nl/`. Alternatively open `web/index.html` locally (no server needed for the static navigation). Stop the server with Ctrl+C. Keep the server bound to loopback; do not deploy or use a public preview.

## Structure

English pages are at the web root; identical route names exist under `pl/` and `nl/`. Each locale includes index, sources, methodology, about, privacy, cookies, terms and data-policy HTML files. Locale links point to the same page in the target language. Shared assets are in `assets/css/`. Edit the static HTML directly in Pinegrow; preserve navigation, landmarks, locale links and draft legal notices across all variants. No new build system.

## Dependency

Bootstrap **5.3.6** CSS is the unmodified distribution from [official release v5.3.6](https://github.com/twbs/bootstrap/tree/v5.3.6). The [MIT license](assets/licenses/bootstrap-5.3.6-MIT.txt) accompanies the CSS. Version selected because exact local and upstream blob hashes matched; no Bootstrap JS is used. Source maps are not required at runtime. Custom design rules: `assets/css/living-index.css`.

See [LI-003A verification](../docs/project/LI-003A-VERIFICATION.md) and [test instructions](../tests/README.md). This shell has no approved legal policy, no analytics and no production data. The noindex directive is not access control; do not publish this branch. Code licensing for the project itself remains a separate decision.
