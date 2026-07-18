---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-plan]]"
produces: "[[artifact-plan-md]]"
applies: "[[pattern-vertical-slice]]"
equivalent_to: ["[[mp-to-tickets]]", "[[addy-planning]]", "[[bmad-create-epics-and-stories]]", "[[ce-plan]]", "[[sp-writing-plans]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-tasks

**`/speckit.tasks`** — "Generate actionable task lists for implementation." Converts the
plan into an executable task list (`tasks.md`, an instance of [[artifact-plan-md]]). Inputs:
`plan.md` (required), plus optional `data-model.md`, `contracts/`, and `research.md`.

It derives concrete tasks from API contracts, entities, and test scenarios; marks
independent tasks **`[P]`** for parallelization; sequences dependent work; and prioritizes
**test-first ordering** — contract tests before integration tests before unit tests, in
keeping with the constitution's non-negotiable TDD.

## Cross-framework cluster (decompose)

Clusters with the frameworks that break a plan/spec into discrete, orderable units of work:

- [[mp-to-tickets]] — break a plan/PRD into vertical-slice issues.
- [[addy-planning]] — decompose a spec into small, verifiable, dependency-ordered tasks.
- [[bmad-create-epics-and-stories]] — decompose requirements into epics of context-rich stories.

The `[P]` parallel markers echo GSD's dependency-ordered [[pattern-wave-parallelism|wave
parallelism]], though Spec Kit expresses parallelism as per-task flags rather than explicit
waves.

## See Also
- [[speckit]] — the framework.
- [[speckit-plan]] — the plan this command decomposes.
- [[speckit-taskstoissues]] — exports the resulting tasks to GitHub issues.
- [[speckit-implement]] — executes the list.
- [[stage-plan]] — the canonical stage.
