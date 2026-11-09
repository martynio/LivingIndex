# Living Index — continuity and audit records

| Document | Purpose |
| --- | --- |
| [WORK_LOG.md](WORK_LOG.md) | Append-only historical record of substantive human and AI changes, tests, decisions, checkpoints |
| [HANDOFF.md](HANDOFF.md) | Short, overwriteable **latest** operating state for the next contributor |

## How to use

1. Read [PROJECT_STATUS](../project/PROJECT_STATUS.md) and verify it against the current branch and PRs.
2. Read [HANDOFF](HANDOFF.md) for immediate constraints and next action.
3. Consult [WORK_LOG](WORK_LOG.md) only when historical evidence is needed.
4. After each iteration, append a verified entry to the log and update the handoff.
5. Link a commit and PR whenever one exists. Mark pending approvals and checks honestly.

Logging is required for substantive work, **not** routine conversation or each terminal command. Never store secrets or private chain-of-thought. See [WORK_PROTOCOL](../governance/WORK_PROTOCOL.md).
