---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: "[[artifact-review-report]]"
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /ios-design-review

`/ios-design-review` — a **designer's-eye visual audit for iOS apps on real hardware**, scored
against a **10-dimension Apple HIG rubric**. The native-app sibling of the web-facing
[[gstack-design-review]].

Sits in gstack's **Review** phase ([[stage-review]]); produces a design review report. No
cross-framework counterpart — gstack is the only framework here with an iOS/HIG design auditor.

## See Also
- [[gstack-design-review]] — the web-facing design-audit sibling.
- [[gstack-ios-qa]] — the live-device harness it runs on.
- [[stage-review]] — the canonical stage this implements (Review side).
