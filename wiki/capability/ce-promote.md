---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-promote

`/ce-promote` — "Draft user-facing announcement copy for shipped features across X, changelog, LinkedIn, email." The launch-communications step: turns a shipped feature into channel-tailored announcement copy (X/Twitter, changelog, LinkedIn, email).

It implements [[stage-release]] as the **announce** act — the outward-facing tail of shipping. It relates to Addy's [[addy-shipping]] (which owns launch checklists + rollout) but covers the *communications* surface Addy folds in only implicitly. No `equivalent_to` — no other framework here ships a dedicated announcement-drafting capability, reflecting Every's writing-first, product-marketing-integrated culture.

## See Also
- [[addy-shipping]] — launch orchestration (checklist/rollout); `ce-promote` is the comms tail.
- [[ce-commit-push-pr]] — ships the work `ce-promote` announces; [[ce-product-pulse]] — reports how the launch lands.
- [[stage-release]] — the canonical stage this implements.
