---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-review]]"
delegates_to: []
produces: []
applies: ["[[pattern-deep-modules]]"]
equivalent_to: ["[[addy-code-simplification]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-05
---

# /ce-simplify-code

`/ce-simplify-code` — "Refine recently changed code for reuse, quality, and efficiency while
preserving behavior." Step 4 of the loop, run on freshly-written code *before* review: reduce
complexity, extract reuse, tighten interfaces — all **behavior-preserving**. Running it before
[[ce-code-review]] means reviewers spend their budget on substance, not on cleanups the author
could have made.

It implements [[stage-review]] (the quality side) and is a **direct** counterpart to Addy's
[[addy-code-simplification]].

## Cross-framework equivalents
`ce-simplify-code` ↔ [[addy-code-simplification]] (`equivalent_to`) — both reduce complexity
while preserving exact behavior. Compound Engineering's twist is *placement*: a dedicated loop
step between writing and review, feeding cleaner code into the persona fan-out.

## See Also
- [[addy-code-simplification]] — the direct counterpart (Chesterton's Fence, Rule of 500).
- [[ce-code-review]] — the next loop step, which reviews the simplified code.
- [[stage-review]] — the canonical stage this implements.
