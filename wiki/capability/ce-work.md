---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-implement]]"
delegates_to: ["[[ce-figma-design-sync]]"]
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-worktree-isolation]]", "[[pattern-vertical-slice]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[openspec-apply]]", "[[addy-incremental-implementation]]", "[[speckit-implement]]", "[[bmad-dev-story]]", "[[mp-implement]]", "[[sp-executing-plans]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-09
---

# /ce-work

`/ce-work` — "Execute against implementation-ready guardrails, figure out HOW with code, ship through quality gates." Step 3 of the loop and the "20%" of the effort split. It takes the guardrailed [[artifact-plan-md|plan]] from [[ce-plan]] and implements it in code — the plan owns the WHAT, `ce-work` owns the HOW — running inside an isolated git worktree ([[pattern-worktree-isolation]], via [[ce-worktree]]) and using MCP tooling (e.g. Playwright, XcodeBuildMCP) to simulate real usage while building.

It implements [[stage-implement]] and is the seventh member of the wiki's **execute** cluster.

## Cross-framework equivalents
Execute cluster (now seven frameworks): `ce-work` ↔ [[gsd-execute-phase]] ↔ [[openspec-apply]] ↔ [[addy-incremental-implementation]] ↔ [[speckit-implement]] ↔ [[bmad-dev-story]] — turn a plan into working code. `ce-work`'s distinctive constraints: **guardrails from the plan bound it**, and it runs in worktree isolation with live-usage simulation.

## See Also
- [[gsd-execute-phase]] · [[openspec-apply]] · [[addy-incremental-implementation]] · [[speckit-implement]] · [[bmad-dev-story]] — execute-cluster counterparts.
- [[ce-worktree]] — the isolation it runs inside; [[ce-plan]] — supplies its guardrails.
- [[ce-simplify-code]] · [[ce-code-review]] — the next loop steps that gate its output.
- [[stage-implement]] — the canonical stage this implements.
