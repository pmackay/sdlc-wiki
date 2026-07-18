---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: []
applies: ["[[pattern-persona-agents]]", "[[pattern-plan-verification-loop]]"]
equivalent_to: ["[[gsd-plan-checker]]", "[[speckit-analyze]]", "[[bmad-check-implementation-readiness]]", "[[ce-doc-review]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /plan-eng-review

`/plan-eng-review` — the **Eng Manager** persona in gstack's plan-review panel. Locks in
architecture, data flow, edge cases, and tests; forces hidden assumptions into the open with ASCII
diagrams for data flow / state machines / error paths, a test matrix, failure modes, and security
concerns. Writes a test plan that [[gstack-qa]] later picks up.

This is gstack's member of the **plan-verification** cluster ([[pattern-plan-verification-loop]]) —
gating the plan on engineering rigor before execution — alongside [[gsd-plan-checker]],
[[speckit-analyze]], and BMAD's [[bmad-check-implementation-readiness]]. As one of the
`plan-*-review` persona reviews it also clusters with [[ce-doc-review]].

## See Also
- [[gstack-autoplan]] — runs this review as part of the panel.
- [[gstack-qa]] — consumes the test plan this review writes.
- [[gsd-plan-checker]] · [[speckit-analyze]] · [[bmad-check-implementation-readiness]] — plan-verification counterparts.
- [[stage-plan]] — the canonical stage this implements.
