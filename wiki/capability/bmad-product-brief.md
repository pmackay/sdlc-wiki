---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-product-brief]]"]
applies: ["[[pattern-grilling]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-product-brief (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-product-brief

**`bmad-product-brief`** — "Create, update, or validate a product brief." Dispatched by [[bmad-analyst]] (menu `CB`), it produces the [[artifact-product-brief|product brief]] (`brief.md` + `addendum.md`) — the **pre-PRD scoping document** that captures the problem, audience, and boundaries of a prospective project. The brief is one of the inputs the [[bmad-prd]] workflow synthesizes into structured requirements.

## See Also
- [[bmad]] — the framework.
- [[bmad-prfaq]] — the sibling working-backwards variant of the same align-stage scoping.
- [[artifact-proposal-md]] — OpenSpec's comparable why/what + scope rationale layer.
- [[bmad-prd]] — the downstream spec the brief feeds.
- [[stage-align]] — the canonical stage.
