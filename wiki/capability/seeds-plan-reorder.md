---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan reorder

`sd plan reorder <plan-id> <seed-id…>` — set the exact order of `plan.children`. The argument list must be a **permutation** of the current children: no adds, no drops, no duplicates (use [[seeds-plan-adopt]] and [[seeds-plan-release]] for those). It bumps `revision` and changes nothing else.

The command exists because of a consumer one layer down. **Warren's plan-run walks `plan.children` verbatim, `seq = index + 1`**, dispatching one agent run per child and gating each on the previous PR merging — so the array's order *is* the execution schedule, and `reorder` is the surface for guaranteeing that, say, the cut-release seed runs last.

That makes this the most concrete instance in the wiki of the [[artifact-plan-record|plan-as-data]] argument paying off. A markdown plan's step order is a hint a later agent is asked to respect; here it is an array a runtime indexes into, which is why it needed a first-class command with a permutation check rather than a note in a template.

Implements [[stage-plan]].

## See Also
- [[warren]] — the runtime that consumes this ordering.
- [[seeds-plan-create]] — release trains, the case this was built for.
- [[artifact-plan-record]] — the record whose ordering this pins.
- [[stage-plan]] — the canonical stage this implements.
