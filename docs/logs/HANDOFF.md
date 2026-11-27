# Living Index — latest contributor handoff

**Updated:** 2026-11-27 · CBS accepted on main; GUS candidate ready for review.

- PR #17 merge verified at `09e3f4e2a23f57d8ea349cd87eff7f285dd915f6`; Pages run 46045974842 success. One accepted descriptive version, zero approved calculation versions.
- LI-006C branch `feat/li-006c-gus-descriptive-preview`, implementation `7dcd12b5396bb546a8c87e0140dab9d763b39981`. [GUS contract](../project/LI-006C-GUS-DESCRIPTIVE-PREVIEW.md), [snapshot](../../data/curated/gus-hbs-pl-2020-v1.json). Three published rounded national monthly per-person means; GUS rights conditions reviewed. 15/15 displayed values and 45/45 source cards pass static read-back. PDF screenshots timed out; full browser and regression NOT RUN.
- Next: explicitly accept exact GUS descriptive version, record metadata/labels and merge. Then separate LI-006D PPS admission review; no direct PL/NL cash comparison or paid-hour model. Read [status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [work log](WORK_LOG.md).

- Continuation recheck (LI-LOG-0036): existing PR #18 head `37d689ae7b26cb31b756e459cb644c3936917ee6` independently read back; 3/3 precise-table rounding matches, 15/15 values, 45/45 cards, engines and CBS snapshot unchanged, empty calculation inventory. Precise table values recorded as research only; retain rounded v1 pending acceptance. Screenshot/DNS failures and full test gaps remain. See [review](../project/LI-006C-GUS-DESCRIPTIVE-PREVIEW.md).
