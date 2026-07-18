---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-story]]"]
applies: ["[[pattern-context-engineering]]", "[[pattern-fresh-context-subagents]]", "[[pattern-vertical-slice]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-create-story (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-create-story

**`bmad-create-story`** — "Creates a dedicated story file with all the context the agent will
need to implement it later." Owned by [[bmad-dev]] (in the absorbed Scrum-Master role), it is
the hinge between planning and implementation: it expands one backlogged story into a
self-contained [[artifact-story]] (`story-[slug].md`) carrying acceptance criteria,
tasks/subtasks, Dev Notes (architecture constraints, source-tree touch-points, testing
standards, `[Source: …]` citations), and an empty Dev Agent Record.

This front-loading is the concrete mechanism of BMAD's [[pattern-context-engineering|context
engineering]] — the story file *is* the context, so [[bmad-dev-story]] can implement in a
[[pattern-fresh-context-subagents|fresh context]] without losing the thread. A new story is
created "ONLY after previous one is 'done' to incorporate learnings."

## See Also
- [[bmad]] — the framework.
- [[artifact-story]] — the context-rich work unit this produces.
- [[bmad-dev-story]] — consumes the story file to write code.
- [[gsd-planner]] — GSD's analogue: authors an executable, acceptance-checked plan for the executor.
- [[stage-plan]] — the canonical stage.
