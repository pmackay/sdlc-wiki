---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-test-xcode

`/ce-test-xcode` — "Build and test iOS apps on simulator using XcodeBuildMCP with screenshots
and logs." The native-mobile counterpart to [[ce-test-browser]]: builds the iOS app and runs it
on the simulator via **XcodeBuildMCP**, capturing screenshots and logs as runtime evidence.

It implements [[stage-validate]] on the functional side for iOS targets. No cross-framework
counterpart is paged — it is the wiki's only native-iOS validation capability, and reflects
Compound Engineering's use at Every to run multiple products including native apps (per the
essay's "MCP-simulate-actual-usage" technique).

## See Also
- [[ce-test-browser]] — the web sibling (agent-browser); [[ce-dogfood]] — hands-off browser QA.
- [[stage-validate]] — the canonical stage this implements.
