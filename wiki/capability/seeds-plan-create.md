---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-plan-record]]"]
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan create

`sd plan create <seed-id> [--name <text>] [--template <name>]` — create an **adopt-only** plan: status `approved`, zero spawned children, an empty steps blueprint, to be assembled entirely from seeds that already exist.

It answers a case ordinary planning handles badly. A *release train* — run this set of already-filed seeds serially, ending with a cut-release step — needs ordering and a container, but spawning fresh children for work that is already tracked would duplicate it. `plan create` gives you the container; [[seeds-plan-adopt]] fills it; [[seeds-plan-reorder]] pins the sequence.

It rejects a pre-existing non-draft plan for the seed, so it cannot silently orphan an approved decomposition.

Implements [[stage-plan]]: composing and sequencing existing units of work is planning even when nothing new is decomposed.

## See Also
- [[seeds-plan-adopt]] — populates it.
- [[seeds-plan-reorder]] — pins the execution order warren's plan-run consumes.
- [[seeds-plan-submit]] — the spawning alternative.
- [[stage-plan]] — the canonical stage this implements.
