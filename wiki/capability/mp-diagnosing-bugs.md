---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]"]
equivalent_to: ["[[gsd-debugger]]", "[[addy-debugging]]", "[[ce-debug]]", "[[gstack-investigate]]", "[[sp-systematic-debugging]]"]
sources: "Matt Pocock — Skills for Real Engineers (2026)"
raw: ["../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-07-04
---

# diagnosing-bugs

A **model-invoked** engineering skill that runs a structured debugging loop: **reproduce → minimize → hypothesize → instrument → fix** (see [[pattern-systematic-debugging]]). A feedback-loop answer to failure mode #3: don't guess, shrink the problem and test hypotheses against evidence.

Its cross-framework counterpart is GSD's [[gsd-debugger]] sub-agent, which tracks hypotheses and evidence in persistent session state — see `equivalent_to`.

## See Also
- [[gsd-debugger]] — GSD's equivalent debugging capability.
- [[mp-tdd]] — the test-first feedback loop.
- [[addy-debugging]] — Addy's debugging skill; same evidence-driven, no-guessing loop.
- [[stage-implement]] — the canonical stage this implements.
