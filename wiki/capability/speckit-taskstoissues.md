---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-plan]]"
produces: "[[artifact-issue]]"
equivalent_to: ["[[mp-to-tickets]]"]
sources: "GitHub/spec-kit README (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-taskstoissues

**`/speckit.taskstoissues`** — converts the `tasks.md` task list into **GitHub issues** for
tracking. A thin bridge from Spec Kit's planning artifacts to an external tracker, producing
[[artifact-issue]] (one issue per task). Natural given Spec Kit's GitHub provenance.

## Cross-framework cluster

Directly parallels [[mp-to-tickets]] — Matt Pocock's skill that breaks a plan/PRD into
independently-grabbable vertical-slice issues. Both materialise the plan as tracker issues;
Spec Kit's variant is a mechanical export of an already-decomposed [[speckit-tasks|task
list]] to GitHub specifically, rather than doing the decomposition itself.

## See Also
- [[speckit]] — the framework.
- [[speckit-tasks]] — produces the task list this command exports.
- [[artifact-issue]] — the output.
- [[stage-plan]] — the canonical stage.
