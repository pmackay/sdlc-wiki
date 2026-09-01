---
type: artifact
sources: "Open GSD docs (2026); Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); jayminwest/seeds (2026)"
updated: 2026-08-31
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

Seeds:

- [[seeds-sync]] — stages and commits the `.seeds/` tracker state. The odd one out in this roster: it commits *work-item state*, not a change to the product — which is also why seeds has no audit trail of its own (*"Git IS the audit trail"*).

## See Also
- [[artifact-pull-request]] — aggregates these commits at ship time.
