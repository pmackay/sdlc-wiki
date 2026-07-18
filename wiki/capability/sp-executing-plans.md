---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-implement]]"
delegates_to: ["[[sp-test-driven-development]]", "[[sp-using-git-worktrees]]", "[[sp-finishing-a-development-branch]]"]
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-test-driven-development]]"]
equivalent_to: ["[[openspec-apply]]", "[[addy-incremental-implementation]]", "[[gsd-execute-phase]]", "[[speckit-implement]]", "[[ce-work]]", "[[bmad-dev-story]]", "[[mp-implement]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# executing-plans

The **parallel-session** alternative to [[sp-subagent-driven-development]]: load the plan, review it critically for concerns, create todos, then execute every task in order — following each bite-sized step exactly and running its verifications — with human review at natural checkpoints. When all tasks pass, it hands off to [[sp-finishing-a-development-branch]].

The skill is explicit that it is the **fallback**: *"Superpowers works much better with access to subagents… if subagents are available, use [[sp-subagent-driven-development]] instead."* It is for harnesses without subagent support, or for running the plan in a separate session from the one that wrote it. Guardrails: **stop and ask** on any blocker rather than guessing; never start implementation on `main`/`master` without explicit consent; return to plan review if the approach needs rethinking. Executors follow [[sp-test-driven-development]] per task → [[artifact-atomic-commit]].

It is the seventh-plus member of the cross-framework **execute cluster** — [[openspec-apply]] ↔ [[addy-incremental-implementation]] ↔ [[gsd-execute-phase]] ↔ [[speckit-implement]] ↔ [[ce-work]] ↔ [[bmad-dev-story]] ↔ [[mp-implement]] — the "walk the plan task-by-task" loop; its distinctive flavor is **batch execution with human checkpoints** (vs subagent-driven's continuous autonomous run).

## See Also
- [[sp-subagent-driven-development]] — the recommended same-session alternative (use when subagents exist).
- [[sp-writing-plans]] — produces the plan; [[sp-using-git-worktrees]] — ensures the workspace; [[sp-finishing-a-development-branch]] — the close-out.
- [[openspec-apply]] · [[addy-incremental-implementation]] · [[gsd-execute-phase]] · [[speckit-implement]] · [[ce-work]] · [[bmad-dev-story]] · [[mp-implement]] — the execute cluster.
- [[stage-implement]] — the canonical stage this implements.
