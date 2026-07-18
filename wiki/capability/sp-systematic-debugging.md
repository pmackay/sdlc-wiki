---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-implement]]"
delegates_to: ["[[sp-test-driven-development]]", "[[sp-verification-before-completion]]"]
produces: []
applies: ["[[pattern-systematic-debugging]]", "[[pattern-anti-rationalization]]"]
equivalent_to: ["[[gsd-debugger]]", "[[mp-diagnosing-bugs]]", "[[addy-debugging]]", "[[ce-debug]]", "[[gstack-investigate]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# systematic-debugging

The "something's broken" entry point: find the **root cause before attempting any fix**
([[pattern-systematic-debugging]]). Four phases, each a prerequisite for the next — **(1) Root-Cause
Investigation** (read errors fully, reproduce consistently, check recent changes, add diagnostic
instrumentation at each component boundary in multi-layer systems, trace the bad value backward to
its source); **(2) Pattern Analysis** (find working examples, read reference implementations
completely, list every difference); **(3) Hypothesis & Testing** (one hypothesis, smallest possible
test, one variable at a time); **(4) Implementation** (write a failing test via
[[sp-test-driven-development]], one fix, verify).

> **The Iron Law:** *"NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST."* And a distinctive escalation:
> **after 3 failed fixes, STOP and question the architecture** — repeated failures that each surface a
> new problem elsewhere signal a wrong architecture, not a wrong hypothesis. Discuss before fix #4.

Like the other Superpowers skills it is heavily armored with [[pattern-anti-rationalization]] — a
Red-Flags list ("quick fix for now", "just try changing X", "one more fix attempt") and an
excuse→reality table ("emergency, no time for process" → systematic is *faster* than thrashing) — plus
a section reading the human partner's frustration signals ("stop guessing", "ultra-think this") as
cues to return to Phase 1. Companion techniques ship alongside: `root-cause-tracing.md`,
`defense-in-depth.md`, `condition-based-waiting.md`.

Its tightest cross-framework counterpart is [[gstack-investigate]] — both enforce an **Iron-Law "no
fix without investigation"** and a stop-after-3 rule — within the broader debugging cluster
[[gsd-debugger]] ↔ [[mp-diagnosing-bugs]] ↔ [[addy-debugging]] ↔ [[ce-debug]].

## See Also
- [[sp-test-driven-development]] — writes the Phase-4 failing test that proves the fix.
- [[sp-verification-before-completion]] — confirms the fix actually worked before any "fixed" claim.
- [[gstack-investigate]] — the tightest counterpart (shared Iron Law + stop-after-3).
- [[gsd-debugger]] · [[mp-diagnosing-bugs]] · [[addy-debugging]] · [[ce-debug]] — the debugging cluster.
- [[pattern-systematic-debugging]] · [[pattern-anti-rationalization]] — the techniques applied.
- [[stage-implement]] — the canonical stage this implements.
