---
type: capability
subtype: command
belongs_to: "[[gsd]]"
implements: "[[stage-implement]]"
delegates_to: ["[[gsd-executor]]", "[[gsd-verifier]]"]
produces: "[[artifact-atomic-commit]]"
applies: ["[[pattern-wave-parallelism]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[addy-incremental-implementation]]", "[[openspec-apply]]", "[[speckit-implement]]", "[[bmad-dev-story]]", "[[ce-work]]", "[[mp-implement]]", "[[sp-executing-plans]]", "[[sp-subagent-driven-development]]"]
sources: "Open GSD docs — workflow-commands (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-09
---

# /gsd-execute-phase

`/gsd-execute-phase N` — Phase 3. "Execute all plans in a phase with wave-based
parallelization." Discovers task dependencies, groups them into parallel execution waves
(see [[pattern-wave-parallelism]]), spawns a [[gsd-executor]] subagent per task in a wave
— each in a clean ~200k-token context ([[pattern-fresh-context-subagents]]) — and collects
results. [[gsd-verifier]] runs a goal-backward analysis afterward.

**Produces:** [[artifact-atomic-commit]] — one atomic git commit per completed task
(gsd-executor is the only agent with Edit tool access).

**Flags:** `--wave N` (execute only Wave N; staged rollout), `--interactive` (sequential
inline execution with user checkpoints).

## See Also
- [[gsd-plan-phase]] — produces the plan this executes.
- [[gsd-verify-work]] — conversational UAT after execution.
- [[addy-incremental-implementation]] — Addy's counterpart; same task-by-task execution with a commit per slice.
- [[openspec-apply]] — OpenSpec's counterpart; walks the `tasks.md` checklist (sequential, resumable).
- [[speckit-implement]] — Spec Kit's counterpart; executes `tasks.md` with TDD mandated (tests fail before code).
- [[bmad-dev-story]] — BMAD's counterpart; implements one fully-contexted story at a time in a fresh context.
- [[stage-implement]] — the canonical stage this implements.
