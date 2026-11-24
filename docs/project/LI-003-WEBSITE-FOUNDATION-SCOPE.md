# LI-003 — Website Foundation: proposed scope and acceptance gates

**Document:** LI-003-SCOPE-001 · **Date:** 2026-11-24 · **Status:** PROPOSED / separate implementation approval required.

## CURRENT STATE

- [ADR-0002](../decisions/ADR-0002-PARALLEL-SHELL-RESEARCH.md) accepted with [PR #8](https://github.com/martynio/LivingIndex/pull/8); verified merge [`c8124808c8d57b3973c17362593922b6826e3713`](https://github.com/martynio/LivingIndex/commit/c8124808c8d57b3973c17362593922b6826e3713). This allows branch-only non-data website work in parallel with LI-002, not automatic implementation or publication.
- Existing [web scaffold](../../web/README.md) contains README files and empty asset directories; no index.html or application runtime at this checkpoint. The [project proposal](LI-PP-001-PROJECT-PROPOSAL-v1.0.md) specifies static semantic HTML, Bootstrap 5+, Pinegrow, lightweight JavaScript and EN/PL/NL.
- GitHub Pages deployment activity is visible (including [run 45442944807](https://github.com/martynio/LivingIndex/actions/runs/45442944807)); the connected repository API cannot read actual Pages configuration. Published branch, source directory, hostname, custom domain, DNS and HTTPS are **unconfirmed**. No setting has been changed.
- [Legal research](../research/LEGAL_RESEARCH.md) is preliminary, not a publishable notice. No approved datasets or statistical dashboard. The 24-cell HBS run is still pending.

## OBJECTIVE

Create a professional, accessible, multilingual static website foundation suitable for later Living Index sections, with truthful research-stage messaging and a reviewed publication gate. Deliver this through three independently reviewed work packages.

| Package | Deliverable | Completion / dependency |
| --- | --- | --- |
| LI-003A — Static shell | Shared layout, local assets, navigation, EN/PL/NL landing/about and clearly marked future-section routes, legal-page layout only | Branch-only implementation; preview and tests accepted. No deployment or public merge. |
| LI-003B — Legal and hosting readiness | Actual hosting/processing inventory, reviewed localized legal text, deployment mapping and dependency notices | Requires A evidence and confirmed operator/host facts; remains non-public until accepted. |
| LI-003C — Release gate | Verify final assembled shell and legal pages, domain/base-path/HTTPS configuration, approval of publication | Separate operator decision; no deployment by A or B. |

Packages B and C are planned only. Package A requires its own execution authorization. If A must be accepted before B, retain an immutable branch checkpoint; do not merge deployable pages into a publishing branch merely to satisfy checkpoint policy.

## IN SCOPE — first implementation (LI-003A)

- Build under existing `web/` with semantic HTML and a reusable Bootstrap 5+ layout compatible with Pinegrow. Use locally served, version-pinned Bootstrap distribution assets and any required license notices; inspect the actual release before implementation. Lightweight vanilla JavaScript only where needed.
- Define a restrained, readable visual system: typography, spacing, responsive containers, navigation, buttons, source/status components, focus states, footer. Proposed editorial direction: neutral light surfaces, dark navy text, restrained teal accent. Text wordmark only; branding choices are provisional.
- Static EN/PL/NL localized page sets with explicit language switching, matching routes and document lang. Proposed English default at root, Polish and Dutch under `pl/` and `nl/`; use relative paths that work on localhost and a repository subpath. No browser storage necessary for this first version.
- Landing page communicates project purpose and research status without statistics. About explains scope and transparent methodology commitments. Sources and methodology routes may be honest explanatory placeholders, with no unreviewed dataset cards. Privacy, cookie information, terms/disclaimer and data-policy routes may be clearly marked **DRAFT / NOT FOR PUBLICATION** page layouts; no invented legal terms or controller details. Contact route/details deferred until confirmed.
- Shared visual design across translations and functional navigation. Local preview instructions and repeatable browser checks. Update WORK_LOG and HANDOFF and create an isolated PR.

## OUT OF SCOPE

- Production charts, country/year filters, figures, calculators, budget imports, data APIs, published source cards (LI-004) or backend/accounts.
- Analytics, tracking, forms, remote fonts, external scripts, embedded services, local storage, cookie-consent banner by default, service workers.
- Custom logo production, additional languages, CMS or new build system. No legal-compliance certification.
- GitHub Pages/source configuration, domain/DNS/HTTPS changes, publishable policy text, merge to a deployment branch or live release.

## CONSTRAINTS

- Use existing repository architecture, Bootstrap 5+, Pinegrow and semantic HTML. Do not use transform:scale() for effects; equal cards within .row > .col where applicable. No unnecessary animation; respect reduced-motion preference.
- Static previews must not send third-party requests. Prefer local CSS, scripts and system fonts. Avoid hard-coded domain and root-absolute internal URLs. Do not commit font binaries unless separately approved and licensed.
- Keep no personal user data or actual operator details in draft pages. No claims of tracking-free hosting before inspecting the host's logs and processors.
- No false indicators of data coverage or functionality. Every linked route exists; unimplemented features are visibly described rather than simulated.
- Technical documentation English; interface content human-readable in EN/PL/NL. Separate code license (still to be decided) from dependency and data rights.
- Branch-only acceptance: do not merge the deployable shell to main until the publication gate is explicitly cleared.

## ACCEPTANCE CRITERIA — LI-003A

1. All three locale variants have coherent landing, about, placeholder routes and draft legal layouts; no dead internal links; language switch preserves the equivalent page.
2. Mobile/tablet/desktop layout, navigation, keyboard operation and visible focus work without clipping or horizontal overflow at 320, 768 and 1440 CSS pixels. Test at 200% zoom; sensible landmarks, headings, labels, skip link, contrast and reduced motion. Aim for WCAG 2.2 AA; tests are evidence, not certification.
3. A local static preview works under both root and a nested path; no browser console errors or failed local asset requests. Network/storage checks find no third-party calls, cookies or local/session-storage writes caused by the shell.
4. All content is factual, localized, and clearly marks unavailable research/features and draft legal layouts. No numeric economic observations or unreviewed policy claims.
5. Record exact dependency version, local asset provenance and applicable notices; scope/diff, browser evidence, screenshots, test commands and results, work log, handoff and immutable branch commit available for review.

## REQUIRED TESTS

- HTML/link/asset/locale-route validation (including relative paths).
- Browser preview at 320, 768, 1440 px; keyboard and zoom tests; automated accessibility scan plus manual focus/contrast/landmark checks.
- Browser network, console, storage and cookie inspection; local-only preview with no third-party requests. Capture representative desktop and mobile screenshots.
- Run existing research regression unchanged: `python3 -m unittest discover -s tests -p 'test_hbs*.py' -v`.
- Verify Git scope and no deployment settings/workflow, research script or raw/curated data changes. Mark tests that cannot be executed NOT RUN and do not claim acceptance.

## STOP CONDITIONS

Stop on unexpected deployment activity caused by a shell change, missing rights to dependency assets, unapproved legal details or external processing, incomplete locale routes, failing tests or unresolved accessibility issues. Do not substitute fabricated data or publish drafts. If a branch preview is publicly accessible, stop and obtain a preview/privacy decision.

## LI-003B/C publication prerequisites (not implementation authorization)

- Operator confirms hosting provider, Pages branch/source path or release mechanism, domain/hostname, HTTPS, actual project/operator status, contact and controller details where applicable. Do not invent personal details or assume commercial status.
- Inspect actual site requests, host access logs/processors, retention, international transfers, cookies/terminal storage and rights-request channel as applicable. Recheck current EU/NL requirements against the actual setup.
- Prepare and review English, Polish and Dutch Privacy Notice, Cookie Information as applicable, Terms of Use/Disclaimer and Data Policy/Methodology overview. Separate source attribution from copyright/trademark and code licensing. No unnecessary cookie banner.
- Test final deployed-path behavior in a safe preview; legal and source claims require evidence. Confirm which changes cause auto-deployment before merging public HTML.
- Operator explicitly approves release; validate published URL/HTTPS, response, routing, network/storage behavior and displayed legal pages; record release SHA and evidence. LI-002 statistical gates continue independently.

**Next decision:** approve LI-003A only, revise proposed visual/route defaults if needed, and implement on an isolated branch. No execution has occurred under this scope document.
