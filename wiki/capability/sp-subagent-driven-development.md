---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-implement]]"
delegates_to: ["[[sp-test-driven-development]]", "[[sp-requesting-code-review]]", "[[sp-finishing-a-development-branch]]"]
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-fresh-context-subagents]]", "[[pattern-adversarial-review]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[bmad-dev-story]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# subagent-driven-development

The recommended execution engine: run a plan by dispatching a **fresh implementer subagent per task**, a **task review** after each, and a **broad whole-branch review** at the end — all in the current session, without pausing for human check-ins between tasks ([[pattern-fresh-context-subagents]]).

> **Core principle:** *fresh subagent per task + task review (spec compliance ∥ code quality) + broad final review = high quality, fast iteration.* Subagents never inherit the controller's context; the controller crafts exactly the brief each one needs, preserving its own context for coordination.

The two-stage **task review** is the [[pattern-adversarial-review]] gate: the reviewer returns both a spec-compliance verdict (nothing missing, nothing extra) *and* a code-quality verdict; Critical/ Important findings are fixed by a dispatched fix subagent and re-reviewed before the task is marked complete → [[artifact-atomic-commit]] per task. The final whole-branch review uses [[sp-requesting-code-review]]'s template, then work closes via [[sp-finishing-a-development-branch]]. Implementer subagents follow [[sp-test-driven-development]].

Sharp operational discipline distinguishes it: **explicit model selection** per role (cheapest tier for transcription-style tasks, most capable for the final review — never inherit the session model); **file handoffs** (task briefs, reports, and review packages move as files, never pasted into context); a **durable progress ledger** (`.superpowers/sdd/progress.md`) so a compaction never re-dispatches a completed task; and a strict rule against **pre-judging reviewer findings** ("do not flag X" is forbidden). It clusters with the other fresh-context executors — [[gsd-execute-phase]] (wave-based executors) and [[bmad-dev-story]] (one fully-contexted story per fresh context).

## See Also
- [[sp-writing-plans]] — produces the plan this executes; [[sp-executing-plans]] — the parallel-session alternative.
- [[sp-test-driven-development]] — the discipline implementer subagents follow.
- [[sp-requesting-code-review]] — the final whole-branch review template; [[sp-finishing-a-development-branch]] — the close-out.
- [[gsd-execute-phase]] · [[bmad-dev-story]] — the fresh-context execute cluster.
- [[pattern-fresh-context-subagents]] · [[pattern-adversarial-review]] — the techniques applied.
- [[stage-implement]] — the canonical stage this implements.
