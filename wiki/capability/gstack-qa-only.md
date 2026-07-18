---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[gstack-qa]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /qa-only

`/qa-only` — the **QA Reporter**. Same live-browser testing methodology as [[gstack-qa]] but **report-only**: a pure bug report with no code changes. Use it when you want the findings without the agent touching the code (e.g. reviewing someone else's branch, or a read-only sweep).

The non-mutating sibling of [[gstack-qa]] in gstack's **Test** phase ([[stage-validate]]). Its report-vs-fix relationship mirrors the way OpenSpec's verify is advisory-only.

## See Also
- [[gstack-qa]] — the fix-and-verify sibling.
- [[stage-validate]] — the canonical stage this implements (Test side).
