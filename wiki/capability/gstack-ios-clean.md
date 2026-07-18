---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /ios-clean

`/ios-clean` — a convenience skill that **removes the DebugBridge SPM package and all `#if DEBUG` wiring** from an iOS app before a **Release build**, so the QA instrumentation ([[gstack-ios-qa]]) never ships to production.

A pre-release cleanup **enabling** capability ([[stage-release]]); the teardown counterpart to [[gstack-ios-sync]] (which installs/regenerates the bridge for QA).

## See Also
- [[gstack-ios-sync]] — installs/regenerates the debug bridge this strips.
- [[gstack-ios-qa]] — the QA harness whose instrumentation this removes for release.
- [[stage-release]] — the stage this supports (pre-release cleanup).
