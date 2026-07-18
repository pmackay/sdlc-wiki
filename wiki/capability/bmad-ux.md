---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-design-md]]"]
applies: []
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-ux (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-ux

**`bmad-ux`** — "Plan UX patterns and design specifications." The Planning-phase workflow owned
by [[bmad-ux-designer]] (Sally). It produces a **two-spine design spec** → [[artifact-design-md]]:

- `DESIGN.md` — visual identity (the *look*).
- `EXPERIENCE.md` — behavioral logic and information architecture (the *feel*).

Splitting visual identity from interaction logic "replaces the legacy approach" of one
monolithic UX spec, and both feed the architect and developer downstream.

## See Also
- [[bmad]] — the framework.
- [[artifact-design-md]] — the design specification produced here (shared with OpenSpec/SpecKit design docs).
- [[addy-frontend-ui]] — the build-time UI counterpart; this specifies UX before implementation.
- [[stage-specify]] — the canonical stage.
