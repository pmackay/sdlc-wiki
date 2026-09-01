---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-issue]]"]
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd tpl pour

`sd tpl pour <id> --prefix <text>` — instantiate a convoy template into real issues: one issue per step, `{prefix}` interpolated into each title, and **dependencies wired serially** (step *N+1* blocked by step *N*). The resulting set is a *convoy*, tracked by a shared tag on the created issues rather than by a separate data structure.

The serial wiring is the whole feature. Because [[seeds-ready]] only surfaces unblocked work, pouring a template produces a queue that hands an agent exactly one step at a time, in order, with no coordination beyond closing the previous one. It is the framework's cheapest form of process enforcement — a repeatable procedure encoded as blocking edges rather than as instructions an agent might skip.

Implements [[stage-plan]]: it decomposes a named piece of work into ordered, dependency-wired units, the same output [[seeds-plan-submit]] produces from an LLM-authored plan rather than from a stored macro.

## See Also
- [[seeds-tpl]] — authors the template this pours.
- [[seeds-tpl-status]] — reports convoy progress.
- [[seeds-plan-submit]] — the reasoning-driven counterpart producing the same shape.
- [[stage-plan]] — the canonical stage this implements.
