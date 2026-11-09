# Living Index — collaboration and change-control protocol

**Document:** LI-GOV-001 · **Date:** 2026-11-09 · **Applies to:** human contributors, external collaborators, Codex and other AI agents.

This protocol defines the standard for repository work. It becomes operative on `main` **after operator approval and merge**. Proposed future stages in the [roadmap](../project/ROADMAP.md) are not authorization to implement.

## Authority and workflow

1. **DISCUSS:** record the product question, hypotheses and alternatives. Discussion alone authorizes no edits.
2. **RESEARCH:** validate claims against primary sources, define coverage and uncertainty.
3. **DECIDE:** operator authorizes one bounded outcome, acceptance criteria, exclusions and constraints; record durable decisions in `docs/decisions/` when needed.
4. **REPO CHECK:** verify actual branch and HEAD, recent relevant commits, current files, working tree, tests, and whether a prior dependent change was accepted/checkpointed.
5. **EXECUTE:** do only the agreed scope, on an isolated branch. Prefer a small, reviewable diff.
6. **VERIFY:** independently examine changed files/diff and run appropriate tests or documented manual checks. Classify `PASS`, `ISSUES`, `OUT-OF-SCOPE`, or `BLOCKED`. `NOT RUN` is not `PASS`.
7. **COMMIT / GATE:** make an immutable Git checkpoint, update the log/handoff, open or update PR, request operator acceptance. Only accepted results become a dependency for the next stage.

A report by an AI executor is a **claim**, not proof. Evidence means code/data/files that can be independently examined, a reproducible test result, or a traceable external source. Never claim implementation, testing, a merge, or publication that did not occur.

## Work authorization contract

For implementation tasks, capture: **CURRENT STATE; OBJECTIVE; IN SCOPE; OUT OF SCOPE; CONSTRAINTS; ACCEPTANCE CRITERIA; REQUIRED TESTS; STOP CONDITIONS**. If authorization or relevant definitions are missing, ask the operator before irreversible work. A research task can use a shorter written scope, but must still identify deliverables and evidence.

Do not introduce new services, backends, analytics, statistical series or branding as a side effect of a documentation-only change. `main` remains protected by workflow policy even if GitHub branch protection is not configured.

## Required public work-log record

Create an append-only entry in [WORK_LOG](../logs/WORK_LOG.md) for **every substantive contribution** — human or AI — with:

- **ID/date (ISO 8601):** a unique identifier; date or UTC datetime if verified.
- **Contributor:** human GitHub handle or actual AI provider/model/tool if known; do not invent unknown IDs.
- **Work item / phase:** approved scope reference and PR/issue link if available.
- **Purpose and changed paths:** concise factual result, not prompt history.
- **Evidence:** relevant diff, review, commands/tests, datasets, commit links, source URLs.
- **Verification:** `PASS / ISSUES / OUT-OF-SCOPE / BLOCKED`; list `NOT RUN` separately.
- **Checkpoint and approval:** exact commit SHA (or `PENDING`) and operator decision.
- **Handoff:** next permitted action, remaining risks, blockers.

**Rule:** log entries are append-only once accepted. Corrections are dated new entries referencing the old ID; do not silently rewrite history. While a PR is open, its entries may be finalized with verified commit/PR IDs before merging. Git commit history is the canonical sequence of changes; the log is a human/agent-oriented audit index, not a duplicate of every keystroke.

## Handoff standard

Update [HANDOFF](../logs/HANDOFF.md) at the end of each substantive iteration. Include: status and phase; checked SHA and branch; what actually changed; where to verify; test evidence; outstanding issues and constraints; next authorized or proposed step. A newly starting contributor first checks Git to confirm the handoff is current.

## Source and security gates

- Do not publish data without precise provenance, definitions, units, population, dates, data rights and transformation lineage.
- Flag discontinuous series, missingness, imputation, estimates, and incomparable values in text as well as visuals.
- Keep survey-reported life satisfaction distinct from any future computed index.
- Avoid publishing secrets, private conversations, personal budgets, raw unapproved datasets, or model internal reasoning.
- When a new legal information page is created, verify it against the actual hosting, processing and user-facing behavior; do not make unsupported legal compliance claims.
- Record a blocking issue if licensing or method is unknown. Public repository access does not grant third-party data reuse rights.

## Contributors and approval

- External contributors propose work through issues and PRs; they do not unilaterally expand the roadmap.
- An AI may execute an authorized task but cannot self-approve it or represent its report as operator acceptance.
- A passing test suite is necessary when appropriate, but not sufficient for methodological or legal approval.
- No dependent next-phase execution before the preceding work is **accepted and checkpointed**.
- Technical documentation is English. User-facing UI is planned for English, Polish, Dutch.
