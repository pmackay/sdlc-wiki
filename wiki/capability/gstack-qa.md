---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: "[[artifact-atomic-commit]]"
applies: ["[[pattern-autonomous-loop]]", "[[pattern-test-driven-development]]"]
equivalent_to: ["[[ce-test-browser]]", "[[addy-browser-testing]]", "[[ce-dogfood]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /qa

`/qa` — the **QA Lead**. Opens a **real browser** ([[gstack-browse]]), clicks through flows, finds
bugs, **fixes them with atomic commits, re-verifies, and auto-generates a regression test for every
fix**. "The agent has eyes now" — Garry Tan credits `/qa` with taking him "from 6 to 12 parallel
workers." Claude "saying *I SEE THE ISSUE* and then actually fixing it" is the unlock.

gstack's member of the cross-framework **browser-testing** cluster — alongside [[ce-test-browser]],
[[addy-browser-testing]], and the autonomous [[ce-dogfood]]. It is a self-fixing find→fix→verify
loop ([[pattern-autonomous-loop]]) that leaves regression tests behind ([[pattern-test-driven-development]]).
In gstack's sprint it anchors the distinct **Test** phase, separate from the **Review** phase
([[gstack-review]]). Report-only variant: [[gstack-qa-only]].

## See Also
- [[gstack-qa-only]] — the report-only sibling (no code changes).
- [[gstack-review]] — the code-**Review**-phase sibling.
- [[gstack-browse]] — the browser daemon that gives it eyes.
- [[ce-test-browser]] · [[addy-browser-testing]] · [[ce-dogfood]] — browser-testing-cluster counterparts.
- [[stage-validate]] — the canonical stage this implements (Test side).
