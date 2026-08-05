---
type: capability
subtype: command
belongs_to: "[[nano-spec]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-nano-spec-pack]]", "[[artifact-plan-md]]", "[[artifact-adr]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[bm-prd-creator]]", "[[mp-to-spec]]", "[[addy-spec-driven-development]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[bmad-prd]]", "[[gstack-spec]]", "[[agent-os-shape-spec]]"]
sources: "Tao An — nano-spec (2025)"
raw: ["../../raw/nano-spec/2025-12-01-nano-spec.md"]
updated: 2026-08-05
---

# nano-spec create

`/nano-spec create <task-name> "<description>"` — the defining capability of [[nano-spec]]. From a one-line task description it generates the [[artifact-nano-spec-pack|4-document pack]] into `tasks/<task-name>/` (or the project root if no `tasks/` dir exists): **README.md** (background, goals, in/out scope, dependencies), **todo.md** (research/implementation/verification checklists + Must-Have/Nice-to-Have/Out-of-Scope acceptance criteria), **doc.md** (summary, key decisions with options·chosen·rationale, schemas, open questions), and **log.md** (initialized dev log). It then prints a one-line summary and hands back to the user to review and refine.

This is [[nano-spec]]'s member of the cross-framework **specify** cluster ([[pattern-spec-driven-development]]) — *author the durable spec before code* — the **eighth** alongside [[bm-prd-creator]], [[mp-to-spec]], [[addy-spec-driven-development]], [[openspec-propose]], [[speckit-specify]], [[bmad-prd]], and [[gstack-spec]].

**Distinctive in the specify cluster:**
- **Minimalism as the whole point** — four short markdown files, ~10-minute setup, no bespoke tooling. Where [[speckit-specify]] adds a checklist gate and [[gstack-spec]] a cross-model quality gate, nano-spec *subtracts*: the ceremony is fixed at the smallest useful amount ([[pattern-scale-adaptive-planning]]).
- **Not a facilitated interview** — unlike [[bm-prd-creator]] / [[bmad-prd]], `create` generates the pack in one shot from the description; refinement happens by editing (or [[nano-spec-update]]), not a grilling loop.
- **Tool-agnostic** — the same generation runs as a Claude Code skill/slash-command or as a natural-language prompt across nine other agents; the output pack is identical.
- **Explicit out-of-scope lists** in both README.md and todo.md — scope-creep prevention is a first-class field, not an afterthought.

Its output splits across the pack's files onto existing artifacts: **todo.md** is a task list + acceptance criteria ([[artifact-plan-md]]); **doc.md**'s Key Decisions are ADR-style records ([[artifact-adr]]); README.md (context/scope) and log.md (journey) live inside the [[artifact-nano-spec-pack]] itself.

## See Also
- [[bm-prd-creator]] — the closest counterpart: the other minimalist, non-full-SDLC specify entry (but a facilitated interview → visual HTML PRD).
- [[mp-to-spec]] · [[speckit-specify]] · [[openspec-propose]] · [[gstack-spec]] — other specify-cluster members.
- [[nano-spec-update]] — maintains the pack after creation; [[nano-spec-status]] — reports on it.
- [[artifact-nano-spec-pack]] — the primary output; [[artifact-plan-md]] (todo.md) · [[artifact-adr]] (doc.md) — its components.
- [[stage-specify]] — the canonical stage this implements. </content>
