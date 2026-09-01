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

# sd plan release

`sd plan release <plan-id> <seed-id…>` — detach one or more seeds from a plan **without closing them**. The inverse of [[seeds-plan-adopt]], and inverse in the strict sense: it clears `plan_id` and `plan_step_index`, strips only the `seeds:plan-backref` marker block from the description (collapsing whitespace at the new boundary, and dropping the field entirely if nothing remained), removes the parent-seed blocking edges in both directions, drops the id from `children` and `adoptedChildren` — removing `adoptedChildren` altogether when it empties — and bumps `revision`.

It exists for the case where scope was wrong rather than where work was wrong: *"realize the CSRF bug should ship separately"*. The seed comes back out open, unblocked, and fully queryable, having lost nothing but its membership. Releasing a seed that is not attached to the named plan, or that is the plan's own parent, is rejected pre-write.

Implements [[stage-plan]] as the corrective half of plan composition.

## See Also
- [[seeds-plan-adopt]] — the operation this reverses.
- [[seeds-plan-submit]] — `--overwrite`, the heavier re-planning path.
- [[stage-plan]] — the canonical stage this implements.
