---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /ios-sync

`/ios-sync` — regenerate the iOS **debug bridge** and its typed `@Observable` accessors against the
latest upstream gstack templates, keeping [[gstack-ios-qa]] working as the app and templates evolve.

An **enabling** capability for iOS QA rather than a lifecycle step itself (like [[ce-worktree]] under
implement): it maintains the machinery [[gstack-ios-qa]] / [[gstack-ios-fix]] depend on. The
teardown counterpart is [[gstack-ios-clean]].

## See Also
- [[gstack-ios-qa]] — the QA harness this keeps current.
- [[gstack-ios-clean]] — strips the debug bridge before a Release build.
- [[stage-validate]] — the stage this enables.
