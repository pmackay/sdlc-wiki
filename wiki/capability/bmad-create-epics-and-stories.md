---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: ["[[artifact-story]]"]
applies: ["[[pattern-vertical-slice]]"]
equivalent_to: ["[[mp-to-tickets]]", "[[addy-planning]]", "[[speckit-tasks]]", "[[sp-writing-plans]]"]
sources: "bmad-code-org/BMAD-METHOD — bmad-create-epics-and-stories (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-create-epics-and-stories

**`bmad-create-epics-and-stories`** — "Break requirements into epics and user stories." The
Solutioning decomposition workflow owned by [[bmad-pm]], turning the PRD + architecture into an
`epics.md` of epics containing [[artifact-story|user stories]] — BMAD's decomposition into
independently shippable [[pattern-vertical-slice|vertical slices]].

## Cross-framework cluster (decompose)
- [[mp-to-tickets]] — break a plan/PRD into vertical-slice issues.
- [[addy-planning]] — decompose the spec into small, verifiable, dependency-ordered tasks.
- [[speckit-tasks]] — decompose the plan into a `[P]`-parallelizable, test-first task list.

BMAD's output is richer than a task list: each story is a self-contained context bundle (see
[[bmad-create-story]] and [[artifact-story]]).

## See Also
- [[bmad]] — the framework.
- [[bmad-create-story]] — expands one story into a fully context-filled implementation spec.
- [[stage-plan]] — the canonical stage.
