---
type: pattern
sources: "Open GSD docs (2026); obra/superpowers (2026); mattpocock/sandcastle (2026); sipyourdrink-ltd/bernstein (2026)"
updated: 2026-08-31
---

# Pattern: Wave parallelism

Discover task dependencies, group independent tasks into **waves**, and run each wave's tasks concurrently (one subagent per task) before advancing to the next wave. Maximizes parallelism while respecting dependency order. In GSD, [[gsd-execute-phase]] spawns a [[gsd-executor]] per task per wave; `--wave N` runs a single wave for staged rollout.

## Applied by (backlinks)

GSD:

- [[gsd-execute-phase]] — groups tasks into dependency-ordered waves.
- [[gsd-executor]] — runs one task per wave slot.

Superpowers (the concurrent-dispatch half, without GSD's dependency-ordered waves):

- [[sp-dispatching-parallel-agents]] — one focused subagent per *independent* problem domain, all dispatched in a single response so they run concurrently; explicitly *not* for related/shared-state work.

## Enabled by (infrastructure)

- [[sandcastle]] (library) — the [execution layer](../runtime/index.md)'s concurrent-dispatch substrate: parallel AFK `run()`s across isolated worktrees plus session **forking** for fan-out. Its `parallel-planner` template identifies parallelizable work and runs it concurrently, merging back. This is the concurrent-dispatch half (like [[sp-dispatching-parallel-agents]]), without GSD's dependency-ordered waves.
- [[bernstein]] (platform) — the fullest infra realization: a **declarative task DAG** (`[P]` parallel-safe markers, `-> T###` dependency arrows, `[US<n>]` rollback slices) that `topological_iter_with_parallel` batches into waves — all ready `[P]` tasks form one concurrent batch, a serial task runs alone. Parallel-safety is *declared by the plan*, not inferred from file overlap or reasoned out by a planning agent, and an **adaptive-parallelism controller** throttles the effective `max_agents` on observed error rate and CPU load. This is the dependency-ordered-wave half that Sandcastle leaves to your script — the infra counterpart to [[gsd-execute-phase]]'s waves rather than to plain fan-out.

## See Also
- [[pattern-fresh-context-subagents]] — each wave task runs in clean context.
- [[stage-implement]] — the stage where this applies.
- [[sandcastle]] · [[bernstein]] — the runtimes that supply parallel isolated agent execution (Sandcastle as fan-out you script; Bernstein as a scheduled, dependency-ordered task DAG).
