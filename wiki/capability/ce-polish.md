---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-polish

`/ce-polish` — "Conversational UX polish — start dev server, open browser, iterate together with framework auto-detection." An interactive UI-refinement loop: it auto-detects the web framework, starts the dev server, opens a browser, and iterates on the UX **conversationally** with the developer, seeing the running app rather than guessing from code.

It implements [[stage-implement]] as a UI-refinement capability. It relates to Addy's [[addy-frontend-ui]] (production-quality UI craft) but is a distinct act — *live, conversational iteration against the running app* rather than a standing UI-quality skill — so it is not set as an `equivalent_to`. It shares the live-runtime-observation stance with the browser-testing skills ([[ce-test-browser]], [[addy-browser-testing]]), applied to *design iteration* rather than verification.

## See Also
- [[addy-frontend-ui]] — production-quality UI craft (related, not equivalent).
- [[ce-test-browser]] · [[ce-dogfood]] — the verification-side live-browser siblings.
- [[stage-implement]] — the canonical stage this implements.
