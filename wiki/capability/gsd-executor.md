---
type: capability
subtype: sub-agent
belongs_to: "[[gsd]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: "[[artifact-atomic-commit]]"
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-wave-parallelism]]"]
equivalent_to: []
sources: "Open GSD docs — agents (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-06-27
---

# gsd-executor

Specialist sub-agent invoked per task by [[gsd-execute-phase]] within each parallel wave.
"Implements plans with one atomic git commit per completed task." Runs in a fresh context
window and is **the only agent with Edit tool access** — all code changes flow through it,
which keeps writes isolated and auditable.

**Produces:** [[artifact-atomic-commit]] (one per completed task).

## See Also
- [[gsd-verifier]] — checks the executor's output goal-backward.
- [[gsd-execute-phase]] — spawns executors per wave.
