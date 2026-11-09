# ADR-0001 — Documentation-first project sequence

- **Date:** 2026-11-09
- **Status:** Accepted by operator on 2026-11-09; merged via [PR #1](https://github.com/martynio/LivingIndex/pull/1) at [2192e95](https://github.com/martynio/LivingIndex/commit/2192e95f331aaafab8ee2a10adb217cc7ae2f85b)
- **Decision owner:** Living Index repository operator
- **Context:** The project is public, depends on potentially inconsistent historical economic data, and may be worked on by different humans and AI models.

## Decision accepted

Adopt documented project gates, contributor work logs and handoffs **before** building the public website. Verify the internal source registry before displaying sources to visitors. Create the lightweight website shell and accurately grounded legal pages before implementing the public Sources Explorer. Defer charts until data provenance and calculations can be verified.

## Options considered

- Start with charts/template and document later — faster visual output but creates avoidable evidence and coordination risks.
- Build an elaborate backend/CMS first — unnecessary for the proposed initial static product.
- **Chosen direction:** documentation and source evidence first; then minimal static presentation, followed by verified economic functionality.

## Consequences

- Every substantive person/agent contribution has an auditable artifact, a verifiable checkpoint and an explicit handoff.
- Public source cards must not imply that every historical year or metric is approved.
- This ADR does not choose a license, vendor-specific deployment, legal position, or detailed product architecture.
- Any later change to the order requires an explicit, recorded operator decision.
