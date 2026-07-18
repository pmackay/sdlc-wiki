---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-implement]]"
applies: "[[pattern-test-driven-development]]"
equivalent_to: ["[[gsd-execute-phase]]", "[[openspec-apply]]", "[[addy-incremental-implementation]]", "[[bmad-dev-story]]", "[[ce-work]]", "[[mp-implement]]", "[[sp-executing-plans]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-09
---

# speckit-implement

**`/speckit.implement`** — "Execute all tasks to build the feature according to the plan."
Works through `tasks.md`, translating the specification into implementation. Its defining
constraint: **Test-Driven Development is "NON-NEGOTIABLE"** — tests must be written and must
fail before any implementation code. The loop: generate unit tests from acceptance criteria
→ get test approval → confirm tests fail (Red) → implement code to pass (Green).

## Cross-framework cluster (execute)

Spec Kit's node in the wiki's execute cluster — the frameworks that turn the task list into
working code:

- [[gsd-execute-phase]] — wave-based parallel execution via fresh-context executors.
- [[openspec-apply]] — implement the `tasks.md` checklist sequentially, resuming from checkpoints.
- [[addy-incremental-implementation]] — thin vertical slices: implement, test, verify, commit.
- [[bmad-dev-story]] — implement one fully-contexted story at a time in a fresh context.

Spec Kit is the cluster's strictest on test-first: TDD is mandated by [[artifact-constitution|the
constitution]], not merely encouraged — see [[pattern-test-driven-development]].

## See Also
- [[speckit]] — the framework.
- [[speckit-tasks]] — the task list this command executes.
- [[speckit-converge]] — assesses the resulting code against the spec and re-plans the gap.
- [[stage-implement]] — the canonical stage.
