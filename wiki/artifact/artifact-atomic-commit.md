---
type: artifact
sources: "Open GSD docs (2026); Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026)"
updated: 2026-07-05
---

# Artifact: Atomic commit

One atomic git commit **per completed task**, created by [[gsd-executor]] during [[gsd-execute-phase]]. Because the executor is the only Edit-capable agent and commits one task at a time, history stays granular and each change maps back to a planned task in [[artifact-plan-md]].

## Produced by (backlinks)

GSD:

- [[gsd-execute-phase]] — orchestrates the waves that yield commits.
- [[gsd-executor]] — makes one atomic commit per completed task.

Addy Osmani — Agent Skills:

- [[addy-incremental-implementation]] — one commit per slice.
- [[addy-git-workflow]] — atomic commits, trunk-based.

BMAD:

- [[bmad-dev-story]] — implements one story to completion, producing working, tested, committed code.

Compound Engineering:

- [[ce-work]] — produces committed code from the guardrailed plan.
- [[ce-commit]] — crafts one convention-aware atomic commit (file-level splitting).
- [[gstack-ship]] · [[gstack-qa]] · [[gstack-design-review]] — atomic commits at ship time / per QA fix / per design fix (gstack).

## See Also
- [[artifact-pull-request]] — aggregates these commits at ship time.
