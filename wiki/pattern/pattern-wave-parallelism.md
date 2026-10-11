---
type: pattern
sources: "Open GSD docs (2026); obra/superpowers (2026); mattpocock/sandcastle (2026); sipyourdrink-ltd/bernstein (2026); gastownhall/beads (2026); pstack v0.15.2 — Lauren Tan (2026); Tessl docs (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-10-11
---

# Pattern: Wave parallelism

Discover task dependencies, group independent tasks into **waves**, and run each wave's tasks concurrently (one subagent per task) before advancing to the next wave. Maximizes parallelism while respecting dependency order. In GSD, [[gsd-execute-phase]] spawns a [[gsd-executor]] per task per wave; `--wave N` runs a single wave for staged rollout.

## Applied by (backlinks)

GSD:

- [[gsd-execute-phase]] — groups tasks into dependency-ordered waves.
- [[gsd-executor]] — runs one task per wave slot.

Superpowers (the concurrent-dispatch half, without GSD's dependency-ordered waves):

- [[sp-dispatching-parallel-agents]] — one focused subagent per *independent* problem domain, all dispatched in a single response so they run concurrently; explicitly *not* for related/shared-state work.

Beads — the wave *declared* as data, with the batching left to whoever coordinates:

- [[beads-swarm]] — validate an epic's DAG and mint a swarm molecule that *"can be picked up by any coordinator agent"*; beads marks the coordinator slot and spawns nothing, because its charter assigns *"task assignment strategy"* to the layer above.
- [[beads-mol]] — a poured molecule's unblocked steps *are* the current wave, by construction of [[beads-ready]].

pstack — **the framework whose whole thesis is that rigor is what makes parallelism safe**: *"when you can go deep on one agent and trust it to write good, verifiable code, you can truly parallelize with confidence."*

- [[pstack-swarm]] — N workers across slices or races, **cloud-default** (`environment: "cloud"`), each brief standing alone, one aggregated report.
- [[pstack-arena]] — N candidates at the same artifact, then base selection and grafting ([[pattern-candidate-grafting]]).
- [[pstack-how]] — two to four exploration angles spawned in a single message, then one synthesizer.
- [[pstack-reflect]] — three review lenses in parallel, then a synthesizer.
- [[pstack-maintain-verification-skill]] — one read-only source subagent per feature file, launched concurrently.
- [[pstack-recall]] · [[pstack-automate-me]] — parallel miners across slices of transcript history.

Tessl:

- [[tessl-change-verify]] — fans LLM-judge verifiers across changed files at a default concurrency of 48, capped by a call ceiling that refuses broad runs outright.

builder-skills:

- [[builder-stay-within-limits]] — bounded waves (at most 3 parallel subagents by default) with a usage check between waves; in-flight subagents are never interrupted to save budget.
- [[builder-efficient-frontier]] — parallel slices with clear file ownership, and *"do not ask multiple agents to edit the same files at the same time."*

Matt Pocock — Skills for Real Engineers:

- [[mp-implement-spec]] — implementer subagents launched across the ready **frontier** of a ticket task graph; each merge that unblocks tickets launches more ("maximum concurrency"). A frontier rather than pre-computed waves (v1.3.0).

## Enabled by (infrastructure)

- [[sandcastle]] (library) — the [execution layer](../runtime/index.md)'s concurrent-dispatch substrate: parallel AFK `run()`s across isolated worktrees plus session **forking** for fan-out. Its `parallel-planner` template identifies parallelizable work and runs it concurrently, merging back. This is the concurrent-dispatch half (like [[sp-dispatching-parallel-agents]]), without GSD's dependency-ordered waves.
- [[bernstein]] (platform) — the fullest infra realization: a **declarative task DAG** (`[P]` parallel-safe markers, `-> T###` dependency arrows, `[US<n>]` rollback slices) that `topological_iter_with_parallel` batches into waves — all ready `[P]` tasks form one concurrent batch, a serial task runs alone. Parallel-safety is *declared by the plan*, not inferred from file overlap or reasoned out by a planning agent, and an **adaptive-parallelism controller** throttles the effective `max_agents` on observed error rate and CPU load. This is the dependency-ordered-wave half that Sandcastle leaves to your script — the infra counterpart to [[gsd-execute-phase]]'s waves rather than to plain fan-out.

## Persisted by (store)

- [[beads]] — [[beads-swarm]] validates an epic's DAG and mints a swarm molecule that *"can be picked up by any coordinator agent"*; the wave is **declared as data** and the batching is deliberately somebody else's job, since beads' charter assigns *"task assignment strategy"* to the layer above. A molecule's unblocked steps are the current wave by construction ([[beads-mol]], [[beads-ready]]).

Three positions on the same pattern are now visible: the process layer *reasons* the waves out ([[gsd-execute-phase]]), the store *declares* them, and the execution layer *schedules* them ([[bernstein]]'s topological batching).

## See Also
- [[pattern-fresh-context-subagents]] — each wave task runs in clean context.
- [[stage-implement]] — the stage where this applies.
- [[sandcastle]] · [[bernstein]] — the runtimes that supply parallel isolated agent execution (Sandcastle as fan-out you script; Bernstein as a scheduled, dependency-ordered task DAG).
