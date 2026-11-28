# Living Index — latest contributor handoff

**Updated:** 2026-11-28 · CBS and GUS descriptive versions accepted by operator.

- PR #17 merge verified at `09e3f4e2a23f57d8ea349cd87eff7f285dd915f6`; Pages run 46045974842 success. One accepted descriptive version, zero approved calculation versions.
- LI-006C branch `feat/li-006c-gus-descriptive-preview`, implementation `7dcd12b5396bb546a8c87e0140dab9d763b39981`. [GUS contract](../project/LI-006C-GUS-DESCRIPTIVE-PREVIEW.md), [snapshot](../../data/curated/gus-hbs-pl-2020-v1.json). Three published rounded national monthly per-person means; GUS rights conditions reviewed. 15/15 displayed values and 45/45 source cards pass static read-back. PDF screenshots timed out; full browser and regression NOT RUN.
- Next: verify acceptance metadata/labels and merge PR #18, then verify main. Then separate LI-006D PPS admission review; no direct PL/NL cash comparison or paid-hour model. Read [status](../project/PROJECT_STATUS.md), [roadmap](../project/ROADMAP.md), [work log](WORK_LOG.md).

- Continuation recheck (LI-LOG-0036): existing PR #18 head `37d689ae7b26cb31b756e459cb644c3936917ee6` independently read back; 3/3 precise-table rounding matches, 15/15 values, 45/45 cards, engines and CBS snapshot unchanged, empty calculation inventory. Precise table values recorded as research only; rounded v1 accepted by operator on 2026-11-28. Screenshot/DNS failures and full test gaps remain. See [review](../project/LI-006C-GUS-DESCRIPTIVE-PREVIEW.md).

- LI-LOG-0037: operator accepted exact reviewed PR #18 head `a1e9fb5e6fa00c0854694a205890f6fd14e276d1` and authorized merge; GUS descriptive only, no calculation input. LI-006D next after verified merge.
