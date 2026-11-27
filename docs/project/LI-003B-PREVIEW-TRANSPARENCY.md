# LI-003B — Development-preview transparency and hosting review

**Date:** 2026-11-27 · **Status:** implementation for review; final legal readiness remains OPEN.

## Scope and evidence

Operator reported the main preview was satisfactory and requested continued work. LI-003A checkpoint `38f4caa2000462173f992890982c09d2e4089f71` is the baseline. GitHub [Pages run 46019041001](https://github.com/martynio/LivingIndex/actions/runs/46019041001) finished successfully on that SHA; build, deploy and report-build-status jobs succeeded. Operator visual acceptance of the preview is not the complete responsive/accessibility test suite.

This tranche upgrades the twelve existing legal-information placeholders (EN, PL, NL × privacy, cookies, terms and data policy) to factual, visibly provisional development-preview information. It does not assert that a final privacy policy, legal basis, controller arrangement or production release has been approved. All original navigation and noindex markers remain. No analytics, forms, scripts, remote assets, storage, data or deployment configuration added.

## Hosting and processing inventory

| Item | Evidence and conclusion |
| --- | --- |
| Host / address | GitHub Pages, https://martynio.github.io/LivingIndex/; successful deployment confirmed by GitHub Actions; web shell at web/ |
| Project frontend | Source inspection of 25 HTML pages (24 localized + root), local Bootstrap and custom CSS. No scripts, forms, embedded media or automatic external resource URLs found. Bootstrap's 23 CSS url() references are data URLs; no CSS imports or font-face declarations in either stylesheet. |
| Browser storage | No project script writes storage or cookies in inspected source. Actual host response headers, browser cookie/storage and request capture remain NOT RUN; absence of source scripts does not establish zero personal-data processing. |
| External navigation | Nine user-activated anchors on privacy/cookie pages to two official GitHub documentation URLs; rel=noreferrer. No external resource loading introduced. |
| Host logs | GitHub's Pages documentation confirms visitor IP logging and storage for security, regardless of sign-in. GitHub's general privacy statement describes its own processing, rights, transfers and retention; project-specific roles and access arrangements are not inferred. |
| Other activities | No visitor account, budget entry, payment, marketing form or project analytics feature found. GitHub repository interaction is separate; do not invite personal data via public issues. |
| Operator facts | Controller identity, project organization, private rights contact, applicable legal bases, actual access to logs, retention and transfer arrangements still need confirmation. No personal details invented or committed. |

## Official sources checked 2026-11-27

- [GitHub Pages — data collection](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection): IP logging for security.
- [GitHub General Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement): effective 2026-04-27; general provider processing. Do not treat this as the project's notice or as proof of a particular contractual role.
- [GDPR — Article 13 and related provisions](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/): transparency requirements, including controller/contact, purpose/legal basis, recipients, retention, applicable rights and transfers.
- [Netherlands Enterprise Agency — cookies](https://business.gov.nl/regulations/cookies/): information and consent obligations depend on actual technologies and their impact; do not add a banner without checking the deployment.
- [Existing source rights research](../research/LEGAL_RESEARCH.md): dataset-specific attribution and reuse gates remain open. No new data license or project code license chosen.

## Verification and limits

PASS: deployment metadata for the previous checkpoint; static read-back audit of 12 changed pages, 180 relative references, nine allowlisted user-activated external anchors, language parity, single H1, three content H2, draft/noindex markers, no embedded/active elements; unchanged CSS blobs checked. Earlier 17/17 HBS regression is historical evidence, not rerun here; research scripts and tests are untouched. The existing Python verifier was narrowly amended to accept only the two approved external anchor destinations on privacy/cookie routes. Its full execution is NOT RUN in this tranche. Direct live HTTP probe failed with DNS resolution error; web access also could not retrieve the live preview. No browser rendering, cookie/response header inspection, accessibility certification or final legal approval is claimed.

## Next gate

Review this PR as development-preview content only. Confirm operator/controller and private contact, hosting arrangements and observed browser behavior before final LI-003B acceptance. Keep LI-003C and official release separate; LI-002 remains open. Do not invent legal identity or convert provisional information into a final policy.
