# Web interface

**Status: LI-003A development shell — branch review only. Development preview only; no production release.**

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

See [LI-003A verification](../docs/project/LI-003A-VERIFICATION.md) and [test instructions](../tests/README.md). This shell has no approved legal policy, no analytics and no production data. The noindex directive is not access control. Operator-authorized GitHub Pages development preview is permitted as recorded below; production release is not authorized. Code licensing for the project itself remains a separate decision.

## Preview decision — 2026-11-25

The operator authorized use of the existing, non-promoted GitHub Pages address for review previews of LI-003A. This is permission for a development preview, not acceptance of LI-003A, approval of legal drafts, or authorization to merge to main or issue a production release. GitHub Pages on a public repository remains publicly accessible; noindex is not access control.

The [existing Pages run 45443305037](https://github.com/martynio/LivingIndex/actions/runs/45443305037) build log shows source `.` at main commit `16c611794ca32a0a53fafd205aebab29749ecc43`; deployment log records `https://martynio.github.io/LivingIndex/`. Actual Pages settings cannot be read or modified by the available GitHub connector. No settings, site code, main or deployment changed in this decision record.

Preferred preview: operator selects `feat/li-003a-static-website-shell` and `/(root)` in Settings → Pages → Deploy from a branch. After a successful deployment the expected shell URL is `https://martynio.github.io/LivingIndex/web/`. Verify deployed branch and commit before browser acceptance. All existing draft/noindex markers remain in place. Do not treat the public preview as approved legal content or the release gate as closed.
