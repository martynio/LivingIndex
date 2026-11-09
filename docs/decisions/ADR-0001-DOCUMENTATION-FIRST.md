# ADR-0001 — Documentation-first project sequence

- **Date:** 2026-11-09
- **Status:** Proposed for operator acceptance with LI-001 (not merged policy)
- **Decision owner:** Living Index repository operator
- **Context:** The project is public, depends on potentially inconsistent historical economic data, and may be worked on by different humans and AI models.

## Decision proposed

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
