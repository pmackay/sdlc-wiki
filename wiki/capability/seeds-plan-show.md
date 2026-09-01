---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan show

`sd plan show <pl-id>` — render a plan: its filled sections, status, revision, and the children in order, recursing through nested sub-plans up to `max_plan_depth` (default 3). It accepts either a `pl-*` id or the parent seed id, as the whole planning surface does.

Adopted children are tagged with a muted `(adopted)` suffix in human output, and `--json` sets `adopted: true` on each child listed in `plan.adoptedChildren`. A step's `type`, `priority`, `labels`, and `existing_seed` render as dim sub-lines when present, and adoption-only steps show as `(adopt <seed>)`.

It also carries the framework's only review nudge: when a plan is `approved` or `active` with no reviewer recorded, `show` prints a *"review suggested"* hint. Suggested, never gating — see [[seeds-plan-review]].

A pure **read** command; maps to **no canonical SDLC stage**.

## See Also
- [[seeds-plan-list]] — the multi-plan view.
- [[seeds-plan-review]] — the hint's target.
- [[seeds-show]] — the issue-side counterpart, which surfaces plan children inline.
