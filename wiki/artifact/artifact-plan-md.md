---
type: artifact
sources: "Open GSD docs (2026); GitHub/spec-kit (2026); Builder Methods — BM Skills (2026); tao-hpu/nano-spec (2025)"
updated: 2026-07-13
---

# Artifact: PLAN.md (executable plan)

`{phase}-PLAN.md` — the phase plan as a set of **executable task prompts**, written by
[[gsd-planner]] under [[gsd-plan-phase]] and gated by [[gsd-plan-checker]] before
execution. Each task becomes a unit of work for a [[gsd-executor]] in an execution wave.
In MVP mode on Phase 1 a `SKELETON.md` is produced alongside it.

## Produced by (backlinks)

GSD:

- [[gsd-plan-phase]] — orchestrates planning and gating.
- [[gsd-planner]] — authors the executable task prompts.

Addy Osmani — Agent Skills:

- [[addy-planning]] — writes `tasks/plan.md` + `tasks/todo.md`.

OpenSpec:

- [[openspec-propose]] — emits `tasks.md`, a hierarchically numbered (1.1, 1.2, …) checklist with checkboxes, as the last of its four planning artifacts.
- [[openspec-apply]] — walks and checks off that checklist (its resumable progress ledger).

Spec Kit:

- [[speckit-tasks]] — emits `tasks.md`: an ordered list with `[P]` markers on independently parallelizable tasks, sequenced test-first (contract → integration → unit).
- [[speckit-converge]] — *appends* new tasks to the list from the codebase-vs-spec gap.

Compound Engineering:

- [[ce-plan]] — enriches requirements into `docs/plans/` guardrail plans (U-IDs + test scenarios, WHAT-not-HOW).

Builder Methods — BM Skills:

- [[bm-prd-creator]] — emits a sequence of **milestone prompt files** (`milestones/N-{slug}/prompt.md`) alongside the PRD — ready-to-build prompts that drive a coding agent through implementation (a specify→plan bridge for non-technical builders).

nano-spec:

- [[nano-spec-create]] — the pack's `todo.md`: research/implementation/verification checklists + Must/Nice/Out acceptance criteria (part of the [[artifact-nano-spec-pack]]).

## See Also
- [[artifact-research-md]] — research feeding the plan.
- [[artifact-atomic-commit]] — what executing each task produces.
- [[artifact-design-md]] — OpenSpec's design record that `tasks.md` is derived from.
