---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: []
applies: ["[[pattern-vertical-slice]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd dep

`sd dep add <issue> <depends-on>` · `sd dep remove` · `sd dep list <issue>` — maintain the dependency edges between seeds. Each edge is stored twice, on both endpoints: the dependent seed gains the blocker in `blockedBy`, the blocker gains the dependent in `blocks`, so traversal is cheap from either direction.

The edges are the framework's *plan*, in the sense that matters — a decomposition with no ordering is a list, and [[seeds-ready]] reads exactly this graph to decide what an agent may pick up. The skill that teaches the command is blunt about the cost of over-wiring: *"Add dependencies for real ordering only — every unnecessary `sd dep add` hides the work from `sd ready`."* Declaring a false dependency does not merely mislabel the graph; it removes work from the queue.

Implements [[stage-plan]]: sequencing decomposed units is planning, and it is the step [[seeds-plan-submit]] automates by translating a plan step's `blocks: [i]` indices into these same edges.

## See Also
- [[seeds-block]] — the imperative surface over the same underlying edges.
- [[seeds-plan-submit]] — wires them wholesale from a plan.
- [[seeds-ready]] — the query the graph feeds.
- [[mp-to-tickets]] — the cross-framework counterpart that also has tickets declare their blocking edges.
- [[stage-plan]] — the canonical stage this implements.
