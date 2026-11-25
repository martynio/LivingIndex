# Living Index — latest contributor handoff

**Updated:** 2026-11-24 · **State on LI-003A feature branch:** implemented / static PASS / browser verification BLOCKED. Main remains at accepted scope checkpoint `16c611794ca32a0a53fafd205aebab29749ecc43`.

- Operator approved LI-003A branch-only work. Code commit `eb65f71d438c38d9a6c79b6737e5e5686582b7f2` on `feat/li-003a-static-website-shell`; 24 EN/PL/NL pages and local Bootstrap CSS/notice, no runtime JavaScript, data, tracking or publication.
- [Verification record](../project/LI-003A-VERIFICATION.md): 372 static references, 27 code blob matches, 17/17 HBS tests. Chromium navigation blocked by environment. No browser screenshots, rendered acceptance or complete accessibility audit.
- [Preview instructions](../../web/README.md), [test instructions](../../tests/README.md), [scope](../project/LI-003-WEBSITE-FOUNDATION-SCOPE.md). Verify current Git state before edits.
- Do not merge to main or issue a production release. Operator now permits non-promoted public GitHub Pages preview; see the dated preview decision in the verification record. Obtain browser evidence (root/subpath, 320/768/1440, keyboard, accessibility scan, zoom, console/network/storage) and branch-only operator acceptance. LI-003B/C are not authorized. Pages settings still unconfirmed.
- Independent LI-002 research: manually dispatch matrix workflow on main; no production data accepted. Preserve existing research code and statistical/rights gates.

## Preview decision — 2026-11-25

The operator authorized use of the existing, non-promoted GitHub Pages address for review previews of LI-003A. This is permission for a development preview, not acceptance of LI-003A, approval of legal drafts, or authorization to merge to main or issue a production release. GitHub Pages on a public repository remains publicly accessible; noindex is not access control.

The [existing Pages run 45443305037](https://github.com/martynio/LivingIndex/actions/runs/45443305037) build log shows source `.` at main commit `16c611794ca32a0a53fafd205aebab29749ecc43`; deployment log records `https://martynio.github.io/LivingIndex/`. Actual Pages settings cannot be read or modified by the available GitHub connector. No settings, site code, main or deployment changed in this decision record.

Preferred preview: operator selects `feat/li-003a-static-website-shell` and `/(root)` in Settings → Pages → Deploy from a branch. After a successful deployment the expected shell URL is `https://martynio.github.io/LivingIndex/web/`. Verify deployed branch and commit before browser acceptance. All existing draft/noindex markers remain in place. Do not treat the public preview as approved legal content or the release gate as closed.
