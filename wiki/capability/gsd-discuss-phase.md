---
type: capability
subtype: command
belongs_to: "[[gsd]]"
implements: "[[stage-align]]"
delegates_to: []
produces: "[[artifact-phase-context]]"
applies: ["[[pattern-spec-driven-development]]", "[[pattern-grilling]]"]
equivalent_to: ["[[addy-interview-me]]", "[[openspec-explore]]", "[[speckit-clarify]]", "[[ce-brainstorm]]", "[[gstack-office-hours]]", "[[sp-brainstorming]]"]
sources: "Open GSD docs — workflow-commands (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-04
---

# /gsd-discuss-phase

`/gsd-discuss-phase N` — Phase 1 of the GSD loop. "Gather phase context through adaptive questioning before planning." Loads project history, scouts the codebase for reusable components, identifies unresolved decisions, and guides the user through deep-dives on areas of uncertainty. The output locks decisions so that [[gsd-plan-phase]] plans against a settled scope.

**Produces:** [[artifact-phase-context]] (`{phase}-CONTEXT.md` — locked decisions + scope).

**Flags:** `--all` (discuss all gray areas at once), `--batch` (group related areas), `--power` (extended questioning protocol). An assumptions mode delegates to the gsd-assumptions-analyzer sub-agent (confidence + consequence mapping).

Its "adaptive questioning" is GSD's take on [[pattern-grilling]] — the cross-framework counterpart of Matt Pocock's [[mp-grill-me]] / [[mp-grill-with-docs]].

## See Also
- [[gsd-plan-phase]] — consumes the locked context.
- [[mp-grill-me]] — the equivalent elicitation skill in the other framework.
- [[addy-interview-me]] — Addy's interview skill; same adaptive elicitation before planning.
- [[openspec-explore]] — OpenSpec's align entry; investigates the codebase/approaches rather than interrogating the human.
- [[speckit-clarify]] — Spec Kit's grilling step; resolves `[NEEDS CLARIFICATION]` markers after the spec is drafted.
- [[stage-align]] — the canonical stage this implements.
