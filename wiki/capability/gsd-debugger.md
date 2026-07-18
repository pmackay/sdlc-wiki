---
type: capability
subtype: sub-agent
belongs_to: "[[gsd]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]", "[[pattern-fresh-context-subagents]]"]
equivalent_to: ["[[mp-diagnosing-bugs]]", "[[addy-debugging]]", "[[ce-debug]]", "[[gstack-investigate]]", "[[sp-systematic-debugging]]"]
sources: "Open GSD docs — agents (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-04
---

# gsd-debugger

Specialist sub-agent invoked by `/gsd-debug` that "investigates bugs with persistent session state tracking hypotheses and evidence." State persists to `.planning/debug/`, so a debugging investigation survives across turns and sessions. Applies [[pattern-systematic-debugging]].

Its cross-framework counterpart is Matt Pocock's [[mp-diagnosing-bugs]] skill — both run a disciplined, evidence-tracking debugging loop rather than guess-and-check (see `equivalent_to`).

## See Also
- [[mp-diagnosing-bugs]] — the equivalent skill in the other framework.
- [[gsd-executor]] — applies the fixes the debugger identifies.
- [[addy-debugging]] — Addy's debugging skill; same disciplined hypothesis-and-evidence loop.
- [[stage-implement]] — the canonical stage this implements.
