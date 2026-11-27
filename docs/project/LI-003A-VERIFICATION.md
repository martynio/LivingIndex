# LI-003A — implementation and verification record

**Date:** 2026-11-24 · **Verdict:** IMPLEMENTED ON FEATURE BRANCH / STATIC PASS / BROWSER GATE BLOCKED. Not accepted or published.

## Authorization and checkpoint

Operator explicitly approved LI-003A branch-only implementation after [PR #9](https://github.com/martynio/LivingIndex/pull/9). Baseline main `16c611794ca32a0a53fafd205aebab29749ecc43`, code checkpoint [`eb65f71d438c38d9a6c79b6737e5e5686582b7f2`](https://github.com/martynio/LivingIndex/commit/eb65f71d438c38d9a6c79b6737e5e5686582b7f2), branch `feat/li-003a-static-website-shell`. No merge, hosting, workflow, data or research script changes authorized. LI-003B and C remain separate. The shell files are in a public Git repository branch, not a public website release.

## Delivered

- 24 static HTML pages (eight routes in each EN/PL/NL), translated navigation, footer, equivalent language links and landmarks.
- Local Bootstrap CSS 5.3.6 from [official v5.3.6 tag](https://github.com/twbs/bootstrap/tree/v5.3.6), exact Git blob `27d4921cd5ae65045e3c0d6e3ee070f260725271`; MIT license blob `fa7c00bc4ebd5dc9c0b1e7f8c4b6a202fd9fa816`. Version chosen for exact available official distribution match. Custom CSS and provisional text wordmark/navy/teal palette; system fonts; no JS, CDN, remote images, tracking, forms, cookie banner or data simulation.
- Draft privacy, cookies, terms and data policy layouts: no real operator or legal assertions. Sources and methodology are factual introduction placeholders, not published datasets.
- Local verifier and instructions in [tests](../../tests/README.md) and [web](../../web/README.md). No new CI or deployment configuration.

## Observed verification

| Check | Result | Evidence |
| --- | --- | --- |
| Exact code identity | PASS | 27 local HTML/CSS/license blobs matched the remote code commit, including all 24 HTML routes |
| Static page/asset/locale checks | PASS | `python tests/verify_web_shell.py evidence/li-003a --static-only`: 24 pages, 372 relative references resolved; locale parity, main/header/footer, single H1, skip-link target, noindex, draft marker and no script/form/iframe/img |
| CSS syntax | PASS (static) | tinycss2 parsed 44 top-level custom CSS rules; no top-level parse errors |
| Selected text contrast | PASS (static) | Nine representative foreground/background pairs computed using WCAG relative luminance, minimum 5.54:1; not a comprehensive rendered audit |
| Existing research regression | PASS | `python -m unittest discover -s tests -p 'test_hbs*.py' -v`: 17 tests OK; four local research/test Git blobs matched main, no research files changed |
| Browser execution | BLOCKED | Chromium local navigation attempt failed with `ERR_BLOCKED_BY_ADMINISTRATOR` in the execution environment; no rendered evidence obtained |
| Browser responsive/accessibility/network/storage/zoom tests and screenshots | NOT RUN / unverified | Verifier prepared; native browser zoom and full accessibility scan still require additional checks |
| Publication | NOT AUTHORIZED | Main unchanged; no branch-specific deployment observed in inspected Actions runs before documentation commit; Pages configuration remains unconfirmed |

No visual screenshot was fabricated. The static shell is not accepted as responsive or fully accessible solely on the basis of source inspection. No WCAG certification or claims about real host data processing are made. Preserve the exact code checkpoint; do not begin LI-003B until A is accepted.

## Next permitted action

Check out this isolated branch and run the local preview plus full verifier in a browser-enabled environment. Review visual hierarchy, mobile/desktop layout, all focus states, actual 200% browser zoom, an automated accessibility scan, console/network/storage behavior and screenshots. Record actual evidence and address failures within LI-003A. Publication remains blocked until B/C and explicit operator approval. LI-002 research proceeds independently.

## Preview decision — 2026-11-25

The operator authorized use of the existing, non-promoted GitHub Pages address for review previews of LI-003A. This is permission for a development preview, not acceptance of LI-003A, approval of legal drafts, or authorization to merge to main or issue a production release. GitHub Pages on a public repository remains publicly accessible; noindex is not access control.

The [existing Pages run 45443305037](https://github.com/martynio/LivingIndex/actions/runs/45443305037) build log shows source `.` at main commit `16c611794ca32a0a53fafd205aebab29749ecc43`; deployment log records `https://martynio.github.io/LivingIndex/`. Actual Pages settings cannot be read or modified by the available GitHub connector. No settings, site code, main or deployment changed in this decision record.

Preferred preview: operator selects `feat/li-003a-static-website-shell` and `/(root)` in Settings → Pages → Deploy from a branch. After a successful deployment the expected shell URL is `https://martynio.github.io/LivingIndex/web/`. Verify deployed branch and commit before browser acceptance. All existing draft/noindex markers remain in place. Do not treat the public preview as approved legal content or the release gate as closed.

## Operator amendment — 2026-11-27: main-based development preview

The operator explicitly requested that the development shell be merged into main and visible through GitHub Pages so work can continue. This supersedes the previous branch-only preview restriction for the non-data LI-003A shell. It does not accept unresolved browser tests, approve draft policies, authorize statistical results, or close the production-release gate. Main may host a visibly marked development preview; review branches and logged checkpoints remain the normal workflow. Noindex is not access control.

Observed Pages run [45654489328](https://github.com/martynio/LivingIndex/actions/runs/45654489328) succeeded for the feature branch on 2026-11-25; [46018763155](https://github.com/martynio/LivingIndex/actions/runs/46018763155) was running for the old main checkpoint at the start of this change. The repository root lacked index.html. Add a root entry redirect with a visible fallback link to web/index.html; preserve the 24 original shell pages and local assets unchanged. Expected public preview: https://martynio.github.io/LivingIndex/ (direct route: https://martynio.github.io/LivingIndex/web/). Verify new main deployment and HTTP/rendered behavior separately; the connector cannot modify Pages settings.

The previously observed static checks are retained; browser verification and final LI-003A acceptance remain open. Legal readiness and final release remain separate. No further dependency on a feature-branch Pages configuration.

## Main preview observation — 2026-11-27

[Pages run 46019041001](https://github.com/martynio/LivingIndex/actions/runs/46019041001) completed successfully at `38f4caa2000462173f992890982c09d2e4089f71`. The operator reported that the preview was satisfactory and requested continued work. This is sufficient to proceed with the bounded LI-003B information tranche, not evidence of the full browser acceptance suite. See [LI-003B review](LI-003B-PREVIEW-TRANSPARENCY.md).
