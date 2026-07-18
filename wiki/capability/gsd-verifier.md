---
type: capability
subtype: sub-agent
belongs_to: "[[gsd]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[openspec-verify]]"]
sources: "Open GSD docs — agents (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-06-27
---

# gsd-verifier

Specialist sub-agent run sequentially after execution by [[gsd-execute-phase]]. "Performs a
goal-backward analysis" — working back from the phase goal to confirm the built code
actually satisfies its requirements.

Distinct from [[gsd-verify-work]], the human-in-the-loop UAT command: gsd-verifier is an
automated code-level check inside the Execute phase, whereas `/gsd-verify-work` is
conversational acceptance testing on the running feature.

## See Also
- [[gsd-executor]] — produces the code this verifies.
- [[gsd-verify-work]] — the UAT-stage counterpart.
- [[openspec-verify]] — OpenSpec's spec-backward validator; nearest cross-framework analogue.
