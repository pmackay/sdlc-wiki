---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-align]]"
applies: "[[pattern-grilling]]"
equivalent_to: ["[[gsd-discuss-phase]]", "[[mp-grill-me]]", "[[addy-interview-me]]", "[[ce-brainstorm]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-clarify

**`/speckit.clarify`** — "Clarify underspecified areas." Through iterative dialogue the AI
asks clarifying questions while research agents investigate technical context, maturing the
vague specification: edge cases and boundary conditions, acceptance-criteria precision,
**removal of the `[NEEDS CLARIFICATION]` markers** left by [[speckit-specify]], and
identification of organizational constraints (database standards, auth requirements,
deployment policies). It creates **no distinct artifact** — `spec.md` evolves in place.

## The ordering inversion

`clarify` is Spec Kit's node in the wiki's **grilling cluster** ([[pattern-grilling]]) —
interrogate the human until decisions resolve — alongside:

- [[gsd-discuss-phase]] — adaptive questioning that locks decisions into CONTEXT.md.
- [[mp-grill-me]] — comprehensive interview until decisions resolve.
- [[addy-interview-me]] — one-question-at-a-time to ~95% intent confidence.

Note the ordering difference: those frameworks grill *before* producing the spec, whereas
Spec Kit drafts the spec first ([[speckit-specify]]) with ambiguities flagged, then grills
to resolve them. Same generic activity ([[stage-align]]), spec-first sequencing.

## See Also
- [[speckit]] — the framework.
- [[speckit-specify]] — produces the spec (and the markers) this command clarifies.
- [[stage-align]] — the canonical stage.
