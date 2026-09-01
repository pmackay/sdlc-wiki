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

# sd plan adopt

`sd plan adopt <plan-id> <seed-id…> [--step <i>] [--at <i> | --before <seed> | --after <seed>]` — link one or more already-open seeds into an existing plan.

Adoption is **link-only**, and the guarantee is the point: the adopted seed's `status`, `assignee`, `labels`, `priority`, `type`, and `title` are never mutated. What changes is the plan link (`plan_id`, and `plan_step_index` when `--step` anchors it to a 1-based blueprint step), the blocking edges to the parent seed, the plan's `children` and `adoptedChildren` arrays, and a marker-delimited `seeds:plan-backref` block prepended to the seed's description — applied in place, so manual notes wrapping the markers survive. The plan's `revision` bumps once per command call.

Three surfaces stage an adoption: a step declaring `existing_seed:` at [[seeds-plan-submit]] time, this command loosely (no step anchor — the backref reads *"Adopted into plan pl-…"*), or this command with `--step`. Positioning within `plan.children` is controlled by the mutually exclusive `--at` / `--before` / `--after`, or appended by default.

Rejections are fail-fast and pre-write: a seed that is closed, missing, attached to a *different* plan, or equal to the plan's own parent; the same seed listed twice; a step setting both `existing_seed` and `plan_template`. Reassigning a seed across plans is deliberately two explicit steps — [[seeds-plan-release]] from the old plan first, then adopt.

Implements [[stage-plan]] — it is how ad-hoc work gets folded into a sequenced plan instead of competing with it.

## See Also
- [[seeds-plan-release]] — the exact inverse.
- [[seeds-plan-create]] — the adopt-only plan this was built for.
- [[seeds-plan-reorder]] — fixes the order after a batch of adoptions.
- [[stage-plan]] — the canonical stage this implements.
