---
type: capability
subtype: command
belongs_to: "[[gsd]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: "[[artifact-uat-md]]"
applies: "[[pattern-spec-driven-development]]"
equivalent_to: ["[[openspec-verify]]"]
sources: "Open GSD docs — workflow-commands (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-06-27
---

# /gsd-verify-work

`/gsd-verify-work N` — Phase 4. "Validate built features through conversational UAT with auto-diagnosis." Runs user acceptance testing, tracks results, diagnoses root causes when issues surface, produces fix plans, and queues them for re-execution by [[gsd-execute-phase]] before the phase is declared done.

**Produces:** [[artifact-uat-md]] (`{phase}-UAT.md` — test results and diagnosed gaps) plus auto-generated fix plans when issues are found.

Distinct from `/gsd-execute-phase`'s post-execution [[gsd-verifier]] (a goal-backward code check): `/gsd-verify-work` is human-in-the-loop UAT on the running feature.

## See Also
- [[gsd-execute-phase]] — re-runs queued fix plans.
- [[gsd-ship]] — runs once verification passes.
- [[openspec-verify]] — OpenSpec's counterpart; checks implementation vs spec artifacts (completeness/correctness/coherence).
- [[stage-validate]] — the canonical stage this implements.
