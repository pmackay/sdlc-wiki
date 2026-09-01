---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd block

`sd block <id> --by <blocker-id>` · `sd unblock <id> --from <blocker-id>` (or `--all`) · `sd blocked` — the imperative, blocker-first surface over the dependency graph [[seeds-dep]] maintains declaratively.

The split is ergonomic rather than semantic. `sd dep add A B` reads as *A depends on B*; `sd block A --by B` reads as *A is blocked by B*; both write the same pair of `blockedBy` / `blocks` edges. `sd unblock --all` clears every blocker on a seed at once — the escape hatch when a decomposition turns out to have been over-sequenced.

`sd blocked` lists everything currently held up, which is the complement of [[seeds-ready]] and the first place to look when the ready queue is empty but work remains open. Since v0.5.15 it renders the plan-membership suffix that `list` and `ready` already showed, so a blocked seed belonging to an approved plan says so.

Implements [[stage-plan]] for the same reason [[seeds-dep]] does: it is where execution order is decided.

## See Also
- [[seeds-dep]] — the declarative surface over the same edges.
- [[seeds-ready]] — the complementary query.
- [[seeds-plan-submit]] — spawns children with these edges pre-wired.
- [[stage-plan]] — the canonical stage this implements.
