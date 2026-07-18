---
type: pattern
sources: "Open GSD docs (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Wave parallelism

Discover task dependencies, group independent tasks into **waves**, and run each wave's
tasks concurrently (one subagent per task) before advancing to the next wave. Maximizes
parallelism while respecting dependency order. In GSD, [[gsd-execute-phase]] spawns a
[[gsd-executor]] per task per wave; `--wave N` runs a single wave for staged rollout.

## Applied by (backlinks)

GSD:

- [[gsd-execute-phase]] — groups tasks into dependency-ordered waves.
- [[gsd-executor]] — runs one task per wave slot.

Superpowers (the concurrent-dispatch half, without GSD's dependency-ordered waves):

- [[sp-dispatching-parallel-agents]] — one focused subagent per *independent* problem domain, all dispatched in a single response so they run concurrently; explicitly *not* for related/shared-state work.

## See Also
- [[pattern-fresh-context-subagents]] — each wave task runs in clean context.
- [[stage-implement]] — the stage where this applies.
