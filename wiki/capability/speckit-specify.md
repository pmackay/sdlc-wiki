---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-specify]]"
produces: "[[artifact-spec-md]]"
applies: "[[pattern-spec-driven-development]]"
equivalent_to: ["[[openspec-propose]]", "[[mp-to-spec]]", "[[addy-spec-driven-development]]", "[[bmad-prd]]", "[[bm-prd-creator]]", "[[nano-spec-create]]"]
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-09
---

# speckit-specify

**`/speckit.specify`** — "Define what you want to build (requirements and user stories)." The heart of the workflow: it transforms a vague idea into a structured feature specification. It auto-assigns a sequential feature number (001, 002…), creates a semantic branch name, and generates `specs/[branch-name]/spec.md` from a template.

The output [[artifact-spec-md]] captures **user stories, acceptance criteria, and explicit `[NEEDS CLARIFICATION]` markers** for ambiguities — deliberately deferring resolution to [[speckit-clarify]]. It focuses on **"WHAT users need and WHY," not implementation details**, which are pushed to [[speckit-plan]].

## Cross-framework cluster (specify)

This is Spec Kit's node in the wiki's specify cluster — the frameworks that write a durable spec before code:

- [[openspec-propose]] — generates proposal + spec deltas + design + tasks in one shot.
- [[mp-to-spec]] — synthesizes a conversation into a PRD.
- [[addy-spec-driven-development]] — writes a six-area `SPEC.md` before code.
- [[bmad-prd]] — a facilitated, stakes-calibrated PRD (fifth framework in the cluster).

Spec Kit's distinctive touches: the `[NEEDS CLARIFICATION]` markers (an explicit ambiguity backlog) and automated branch/feature-number scaffolding.

## See Also
- [[speckit]] — the framework.
- [[speckit-clarify]] — resolves the `[NEEDS CLARIFICATION]` markers this command leaves.
- [[speckit-checklist]] — quality-checks the resulting requirements.
- [[stage-specify]] — the canonical stage.
