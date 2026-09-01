---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-wave-parallelism]]"]
equivalent_to: []
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd swarm

`bd swarm create|list|status|validate` — *"swarm management for structured epics"*, where *"a swarm is a structured body of work defined by an epic and its children, with dependencies forming a DAG."*

`bd swarm create <epic-id>` builds a **swarm molecule** that links to the epic, carries `mol_type=swarm` for discovery, optionally names a coordinator address, and *"can be picked up by any coordinator agent"*. A single non-epic issue is auto-wrapped in an epic first. `bd swarm validate` checks an epic's structure is swarmable before anyone tries; `bd swarm status` and `list` report progress and active workers.

This is the closest beads comes to its own charter's boundary, and it stays on the right side of it in an instructive way. The swarm molecule **declares** that a body of work is parallelizable and marks a slot for whoever coordinates it; it does not do the coordinating — no agent is spawned, no model chosen, no retry planned. Those are the *"orchestration policy"* the charter assigns to schedulers and swarms built on top. So the store's contribution to [[pattern-wave-parallelism]] is the *shape* of the wave, discoverable by a coordinator that beads knows nothing about.

Compare [[bernstein]], which batches a task DAG topologically in deterministic Python, and [[gsd-execute-phase]], which reasons its waves out in the plan. Beads sits between: the DAG is declared data, and the batching is somebody else's job.

Maps to **no canonical SDLC stage** — it structures work for parallel execution without executing any.

## See Also
- [[beads-epic]] — the structure a swarm is built from.
- [[beads-mol]] — swarms are molecules; the general machinery lives there.
- [[beads-merge-slot]] — the serialization primitive parallel workers need at merge time.
- [[pattern-wave-parallelism]] — the pattern this shapes.
