---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[addy-browser-testing]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-test-browser

`/ce-test-browser` — "End-to-end browser tests on PR/branch-affected pages using agent-browser exclusively." Scopes tests to the pages actually touched by the current PR/branch diff and drives a real browser (agent-browser) to exercise them end-to-end, gathering live runtime behavior rather than trusting unit tests alone.

It implements [[stage-validate]] on the **functional** side (does it work) and clusters with Addy's [[addy-browser-testing]]. Its diff-scoping is what makes it cheap enough to run every loop; the fully-autonomous variant is [[ce-dogfood]].

## Cross-framework equivalents
`ce-test-browser` ↔ [[addy-browser-testing]] (`equivalent_to`) — both gather live runtime data via a real browser. `ce-test-browser` adds **diff-scoping** (only PR-affected pages).

## See Also
- [[addy-browser-testing]] — the live-runtime counterpart (Chrome DevTools MCP).
- [[ce-dogfood]] — the hands-off, self-fixing variant; [[ce-test-xcode]] — the iOS-simulator sibling.
- [[stage-validate]] — the canonical stage this implements.
