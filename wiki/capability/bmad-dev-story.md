---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-test-driven-development]]", "[[pattern-context-engineering]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[openspec-apply]]", "[[addy-incremental-implementation]]", "[[speckit-implement]]", "[[ce-work]]", "[[mp-implement]]", "[[sp-executing-plans]]", "[[sp-subagent-driven-development]]"]
sources: "bmad-code-org/BMAD-METHOD — bmad-dev-story (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-09
---

# bmad-dev-story

**`bmad-dev-story`** — "Execute story implementation following a context filled story spec
file." BMAD's core implementation loop, owned by [[bmad-dev]] (Amelia). It reads a
[[artifact-story|story file]], implements test-first ([[pattern-test-driven-development]]), and
updates only the story's own regions (Dev Agent Record, File List, Change Log, Status). Its
discipline is strict: "Execute ALL steps in exact order," and "Continue in a single execution
until the story is COMPLETE … UNLESS a HALT condition is triggered."

Because the story file carries all context ([[pattern-context-engineering]]), each story runs
in a [[pattern-fresh-context-subagents|fresh context]].

## Cross-framework cluster (execute)
The **sixth framework** in the wiki's execute cluster — walk the plan into working code:

- [[gsd-execute-phase]] — wave-based parallel execution.
- [[openspec-apply]] — resumable sequential pass over `tasks.md`.
- [[addy-incremental-implementation]] — thin vertical slices.
- [[speckit-implement]] — test-first, TDD mandated by the constitution.

They differ in the unit of work: GSD parallelizes into waves, Addy cuts vertical slices, and
BMAD drives from a single fully-contexted story at a time.

## See Also
- [[bmad]] — the framework.
- [[bmad-create-story]] — produces the story file this executes.
- [[bmad-code-review]] — reviews the result adversarially in a fresh context.
- [[stage-implement]] — the canonical stage.
