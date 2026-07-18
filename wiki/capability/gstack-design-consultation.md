---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-plan]]"
delegates_to: []
produces: "[[artifact-design-md]]"
applies: ["[[pattern-source-grounding]]"]
equivalent_to: ["[[bmad-ux]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /design-consultation

`/design-consultation` — the **Design Partner**. Builds a **complete design system from scratch**: understands your product, researches the design landscape, proposes creative risks, and specifies aesthetic, typography, color, layout, spacing, and motion, generating font + color previews and realistic product mockups. Output is written as `DESIGN.md` ([[artifact-design-md]]).

"Design is at the heart" of gstack's parallel-sprint story: this skill seeds the design system that the [[gstack-design-shotgun]] → [[gstack-design-html]] pipeline then explores and realizes. It enacts *Search Before Building* ([[pattern-source-grounding]]) by researching the landscape first. Its cross-framework counterpart is BMAD's [[bmad-ux]] (the two-spine UX/design spec).

## See Also
- [[gstack-design-shotgun]] — explores mockup variants against this system.
- [[gstack-design-html]] — turns an approved mockup into production HTML.
- [[bmad-ux]] — BMAD's design-spec counterpart → [[artifact-design-md]].
- [[stage-plan]] — the canonical stage this implements.
