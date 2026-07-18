---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-systematic-debugging]]"]
equivalent_to: ["[[gsd-debugger]]", "[[mp-diagnosing-bugs]]", "[[addy-debugging]]", "[[gstack-investigate]]", "[[sp-systematic-debugging]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-debug

`/ce-debug` — "Find root causes systematically through causal chains, predictions, and post-fix
polish." Reproduce the failure, build a **causal chain** to the root cause, make explicit
**predictions** to confirm the hypothesis before changing code, apply the fix, then polish
(guard against regression). The prediction step is its signature: it forces falsifiable
hypotheses rather than shotgun edits.

It implements [[stage-implement]] (diagnose-and-fix work) and joins the wiki's **debugging**
cluster via [[pattern-systematic-debugging]].

## Cross-framework equivalents
Debugging cluster: `ce-debug` ↔ [[gsd-debugger]] ↔ [[mp-diagnosing-bugs]] ↔ [[addy-debugging]] —
all systematic reproduce→localize→hypothesize→fix→guard loops. `ce-debug`'s distinctive step is
**explicit predictions** that must be confirmed before the fix lands.

## See Also
- [[gsd-debugger]] · [[mp-diagnosing-bugs]] · [[addy-debugging]] — debugging-cluster counterparts.
- [[pattern-systematic-debugging]] — the shared technique.
- [[stage-implement]] — the canonical stage this implements.
