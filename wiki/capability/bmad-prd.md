---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-prd]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-grilling]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[mp-to-spec]]", "[[addy-spec-driven-development]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[bm-prd-creator]]", "[[nano-spec-create]]"]
sources: "bmad-code-org/BMAD-METHOD — bmad-prd (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-09
---

# bmad-prd

**`bmad-prd`** — "Create, update, or validate a PRD." BMAD's central spec-authoring workflow, owned by [[bmad-pm]]. A consolidated three-intent skill (superseding the deprecated create/edit/validate skills) offering a **Fast or Coaching path**, a Decision-Log pattern, and a `.memlog.md` "append-only memory and audit trail — every decision, change, and override" — BMAD's [[pattern-context-engineering|context-engineering]] applied to the spec itself. Output: `prd.md` + `addendum.md` (→ [[artifact-prd]]). Length "scales with stakes" ([[pattern-scale-adaptive-planning]]). It synthesizes whatever align-stage inputs exist — briefs, PRFAQ, research, brainstorming — into structured requirements.

## Cross-framework cluster (specify)
The fifth framework in the wiki's spec-authoring cluster — write the durable spec before code:

- [[mp-to-spec]] — synthesize a conversation into a PRD.
- [[addy-spec-driven-development]] — a six-area `SPEC.md` before code.
- [[openspec-propose]] — the spec as ADDED/MODIFIED/REMOVED deltas.
- [[speckit-specify]] — `spec.md` with user stories + `[NEEDS CLARIFICATION]` markers.

BMAD is the cluster's most **facilitated**: the PM coaches the human to each requirement rather than drafting the doc ([[pattern-grilling]]).

## See Also
- [[bmad]] — the framework.
- [[bmad-spec]] — the lightweight `SPEC.md` kernel used on the Quick-Flow path instead of a full PRD.
- [[bmad-create-epics-and-stories]] — decomposes this PRD into epics and stories.
- [[stage-specify]] — the canonical stage.
