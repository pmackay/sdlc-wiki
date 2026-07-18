---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-spec-md]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-spec (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-spec

**`bmad-spec`** — "Distill any intent input into the SPEC kernel + companions — the canonical, preservation-validated machine contract for downstream work." A cross-phase core skill that produces a tight five-field `SPEC.md` (Problem, Capabilities, Constraints, Non-goals, Success signal) → [[artifact-spec-md]]. It is the **lightweight spec** used on the [[bmad-quick-dev|Quick-Flow]] path when a full [[bmad-prd|PRD]] is more ceremony than the work warrants — BMAD's [[pattern-scale-adaptive-planning|scale-adaptive]] bottom rung of the specify stage.

## See Also
- [[bmad]] — the framework.
- [[bmad-prd]] — the heavyweight spec for larger work; `bmad-spec` is its Quick-Flow alternative.
- [[artifact-spec-md]] — the SPEC document (shared with Addy `SPEC.md` and SpecKit `spec.md`).
- [[stage-specify]] — the canonical stage.
