---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: "[[artifact-atomic-commit]]"
applies: ["[[pattern-autonomous-loop]]", "[[pattern-systematic-debugging]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /ios-fix

`/ios-fix` — an **autonomous iOS bug fixer** with regression-snapshot capture. Drives the app on a real device ([[gstack-ios-qa]]), reproduces the bug, fixes it, and captures a snapshot so the fix is guarded against regression.

The iOS analogue of gstack's self-fixing loop: [[gstack-qa]] for web, `/ios-fix` for native. Applies [[pattern-autonomous-loop]] and the no-fix-without-investigation discipline of [[gstack-investigate]] ([[pattern-systematic-debugging]]).

## See Also
- [[gstack-ios-qa]] — the live-device QA harness it drives.
- [[gstack-qa]] — the web-side self-fixing loop.
- [[gstack-investigate]] — the debugging discipline it shares.
- [[stage-validate]] — the canonical stage this implements.
