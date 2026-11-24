# ADR-0002 — Separate website-shell development from numerical feasibility

**Date:** 2026-11-24 · **Status:** proposed for operator acceptance in this PR. No website implementation or deployment authorized by this record alone.

## Context

The first HBS probe now works ([run #2](https://github.com/martynio/LivingIndex/actions/runs/45436731068)), but evidence for a complete comparable budget and a net paid-hour denominator remains open. The original documentation-first sequence unnecessarily tied *all* LI-003 work to completion of those numerical checks. The public repository has GitHub Pages activity; an approved merge must not accidentally publish unfinished legal text or unreviewed data.

## Decision proposed

Keep LI-002 statistical research open. Permit separate scoping and branch-only development of LI-003's non-data website shell after acceptance of this ADR and an explicit LI-003 work scope. The initial shell may contain navigation, responsive layout, EN/PL/NL structure, accessibility and research-status placeholders; it must contain no fabricated statistics, calculated outputs or unverified dataset claims. No analytics or other new third-party data flows by default.

Keep a distinct **publication gate**: inspect actual Pages/source directory, hostname/domain, hosting and real data flows; verify required privacy, cookie, terms and operator information and applicable rights. No merge of publicly deployable pages or deployment-setting changes before that review and operator approval. LI-004 public source cards require approved metadata and attribution; LI-005/006 numerical results still require compatible data and methodological gates. The LI-002 legal/source research deliverables are not waived.

## Alternatives and consequences

Keeping strict serial execution delays safe interface work unnecessarily. Unrestricted parallel production risks misrepresentation and unintended publication. Bounded branch-only shell work lets design progress while preserving the statistical and publication gates. This amends only the LI-002 → LI-003 development dependency in ADR-0001; all other approval, logging and evidence rules remain in force.

## Evidence and approval

Accepted prior baseline: [PR #7](https://github.com/martynio/LivingIndex/pull/7) merged at `e389573c34c88c3772b0c56701360bedf979a148`. Review this decision and corresponding roadmap changes before treating the new dependency as accepted. A later shell PR needs a separately defined scope and approval; this PR contains no website code.
