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

# sd plan edit

`sd plan edit <id>` — targeted, field-level edits to a live plan without re-submitting the whole JSON through `--overwrite`. `--name` renames the plan; `--section <name> <text>` replaces a text section; `--step <i>` with `--title` / `--priority` / `--type` edits a step. Flags compose atomically in one invocation, `<id>` accepts a plan id or the parent seed id, and each call bumps `revision` once and refreshes `updatedAt`.

Two propagation rules make it more than a text edit. `--step` metadata **propagates to the corresponding child seed** (looked up via `plan.children[i-1]`; the flag is 1-based, matching `step.blocks`), so a plan and its spawned work cannot drift apart. And `--section approach` **refreshes the `seeds:plan-backref` block on every child**, keeping the snippet each child seed carries in its description in sync with the live plan.

Structural change — adding, removing, or reordering steps — still requires `--overwrite` or the dedicated composition commands; this is the surface for fixes, not for re-planning. Out-of-range `--step` and unknown section names exit non-zero with both JSONL files untouched, and the lock order matches the rest of the planning surface (outer `plans.jsonl`, inner `issues.jsonl`).

Implements [[stage-plan]] — keeping the plan true as understanding improves is part of planning, and the framework's alternative would be a stale plan nobody edits.

## See Also
- [[seeds-plan-submit]] — `--overwrite`, for structural change.
- [[seeds-plan-validate]] — re-check after editing.
- [[seeds-plan-reorder]] — the ordering operation this deliberately excludes.
- [[stage-plan]] — the canonical stage this implements.
