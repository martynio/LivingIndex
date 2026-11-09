# Living Index — instructions for human and AI contributors

> **Entry point, not autonomous permission to execute.** This file is a compact navigation and integrity contract. The authoritative state lives in Git and [PROJECT_STATUS](docs/project/PROJECT_STATUS.md).

## Read before starting work (in order)

1. [Current project status](docs/project/PROJECT_STATUS.md): active stage, approved checkpoint, blockers, and next gate.
2. [Roadmap](docs/project/ROADMAP.md): phase order, deliverables, exclusions, and criteria.
3. [Project Proposal](docs/project/LI-PP-001-PROJECT-PROPOSAL-v1.0.md): intended product scope; proposed requirements are **not** automatically implementation authorization.
4. [Work protocol](docs/governance/WORK_PROTOCOL.md): approvals, audit trail, and responsibilities.
5. [Latest handoff](docs/logs/HANDOFF.md) and [work history](docs/logs/WORK_LOG.md).
6. Relevant [methodology](docs/methodology/README.md), [research](docs/research/README.md), and [decisions](docs/decisions/).

## Non-negotiable rules

- **Conversation ≠ plan ≠ approved execution.** Do not implement a proposed idea without an explicit authorized scope and acceptance criteria.
- **Repository check before execution:** inspect HEAD, active branch, recent commits, working-tree changes, existing files, tests and unfinished dependent work. Do not overwrite uncommitted work.
- **Checkpoint gate:** a dependent phase cannot begin from an uncommitted or unaccepted iteration. Use a feature branch and a reviewable PR; do not merge to `main` without operator approval.
- **Scope discipline:** no unrelated refactors, new services, synthetic economic data, or speculative product features.
- **Statistical integrity:** trace sources, definitions, units, population, coverage, transformations, uncertainty and licensing. Missing values remain missing.
- **Truthful verification:** list actual commands, checks, diffs and outcomes; clearly say when a check was not run. An agent's self-report is not independent proof.
- **Mandatory traceability:** every substantive contributor (person or agent) updates the [WORK_LOG](docs/logs/WORK_LOG.md) and [HANDOFF](docs/logs/HANDOFF.md) with work ID, identity/actual tool used, scope, changed paths, evidence, result, blockers, PR/commit references. See [protocol](docs/governance/WORK_PROTOCOL.md).
- **No public sensitive material:** never commit personal budgets, credentials, private conversations, chain-of-thought, or unlicensed third-party data.
- **Language:** repository-level technical documentation in English. Planned UI localization: EN / PL / NL.

## Standard execution flow

`DISCUSS → RESEARCH → DECIDE → REPO CHECK → EXECUTE → VERIFY → COMMIT / GATE`

For each approved atomic change: check the repo → state scope / out-of-scope / DONE → change only approved files → run applicable checks → update work log and handoff → commit on an isolated branch → open/update PR → request operator acceptance.

Before authoring a **new Codex implementation task**, verify current available coding models from current official information, and specify **MODEL / CONTEXT (NEW WINDOW or CONTINUE CURRENT) / WHY**. This requirement does not imply a model choice for documentation-only changes.

## Current reality

As of 2026-11-09, Living Index is a documentation and data-research project. There is no released website, validated statistical dataset, application runtime, or CI test suite. Check [PROJECT_STATUS](docs/project/PROJECT_STATUS.md) for newer evidence.

**When status conflicts:** inspect Git and operator-approved decisions, record the discrepancy, and stop rather than guessing.
