---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-deep-modules]]"]
equivalent_to: []
sources: "Matt Pocock — Skills for Real Engineers (2026)"
raw: ["../../raw/matt-pocock-skills/2026-06-28-skills-for-real-engineers.md"]
updated: 2026-07-05
---

# improve-codebase-architecture

`/improve-codebase-architecture` — a user-invoked engineering skill that scans a codebase for **architectural improvements** and presents them as visual HTML reports. The review/ maintenance answer to failure mode #4 (ball of mud): surface entropy so it can be paid down deliberately, steering modules back toward [[pattern-deep-modules]].

Implements [[stage-review]] in the maintenance sense — auditing built code — rather than feature UAT.

## See Also
- [[mp-codebase-design]] — the forward-looking design discipline this audits against.
- [[gsd-verify-work]] — GSD's verification counterpart.
- [[stage-review]] — the canonical stage this implements.
