---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]"]
equivalent_to: ["[[ce-test-xcode]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /ios-qa

`/ios-qa` — **live-device iOS QA** for SwiftUI apps (v1.43.0.0+). Drives a **real iPhone over a USB CoreDevice tunnel** via an embedded `StateServer` in the app: reads Swift source, codegens typed `@Observable` accessors, then runs the agent QA loop. An optional `--tailnet` flag exposes the device over Tailscale so remote agents (OpenClaw, any HTTP-capable agent) can run iOS QA without touching the hardware, gated by a capability-tier allowlist (observe/interact/mutate/restore), per-device session lock, and audit log. Companion Mac-side CLIs: `gstack-ios-qa-daemon` and `gstack-ios-qa-mint`.

gstack's iOS validator; the cross-framework counterpart to Compound Engineering's simulator-based [[ce-test-xcode]] — but gstack drives **real hardware** (and can share it over a tailnet), where CE uses the simulator. Its autonomous fix sibling is [[gstack-ios-fix]]; accessor regeneration is [[gstack-ios-sync]].

## See Also
- [[gstack-ios-fix]] · [[gstack-ios-design-review]] · [[gstack-ios-sync]] · [[gstack-ios-clean]] — the rest of the iOS suite.
- [[ce-test-xcode]] — the simulator-based iOS validator counterpart.
- [[stage-validate]] — the canonical stage this implements (Test side).
