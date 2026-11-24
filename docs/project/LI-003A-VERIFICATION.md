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
