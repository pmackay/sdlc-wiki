---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]", "[[pattern-edit-guardrails]]"]
equivalent_to: ["[[gsd-debugger]]", "[[mp-diagnosing-bugs]]", "[[addy-debugging]]", "[[ce-debug]]", "[[sp-systematic-debugging]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /investigate

`/investigate` — the **Debugger**. Systematic root-cause debugging with an **Iron Law: no fixes without investigation.** Traces data flow, tests hypotheses one at a time, and **stops after 3 failed fixes** rather than thrashing. Auto-**freezes** edits to the module under investigation ([[pattern-edit-guardrails]], via [[gstack-freeze]]) so it cannot "fix" unrelated code.

gstack's member of the cross-framework **debugging** cluster ([[pattern-systematic-debugging]]) — reproduce → localize → hypothesize → instrument → fix — alongside [[gsd-debugger]], [[mp-diagnosing-bugs]], [[addy-debugging]], and [[ce-debug]]. Its signature twist is the auto-freeze scoping.

## See Also
- [[gstack-freeze]] — the edit-lock this auto-activates.
- [[gstack-ios-fix]] — the autonomous iOS analogue.
- [[gsd-debugger]] · [[mp-diagnosing-bugs]] · [[addy-debugging]] · [[ce-debug]] — debugging-cluster counterparts.
- [[stage-implement]] — the canonical stage this implements.
