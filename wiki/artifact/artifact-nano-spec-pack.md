---
type: artifact
sources: "Tao An — nano-spec (2025)"
raw: ["../../raw/nano-spec/2025-12-01-nano-spec.md"]
updated: 2026-07-13
---

# Artifact: nano-spec pack (4-document task spec)

[[nano-spec]]'s signature output: a per-task folder `tasks/{task-name}/` holding **exactly four short markdown files**, each answering one question. Minimal by design — the whole pack is meant to be set up in ~10 minutes and maintained at ~20 min/day.

```
tasks/{task-name}/
├── README.md   # Context: what & why — background, goals, in/out scope, dependencies
├── todo.md     # Plan: research/impl/verification checklists + acceptance criteria
├── doc.md      # Output: key decisions (options·chosen·rationale), schemas, open questions
└── log.md      # Journey: dated Done / In-Progress / Blocked / Notes entries
```

The fixed four-file shape *is* the distinctiveness: other frameworks materialize the spec as a single document (`SPEC.md`, `spec.md`, a PRD, an [[artifact-spec-delta]]); nano-spec splits the spec, the plan, the decision record, and the running journal into four tiny files and treats the set as a living pack maintained through the build.

Component ↔ existing-artifact mapping:
- **todo.md** — a task checklist + Must/Nice/Out acceptance criteria → an [[artifact-plan-md]]-class plan.
- **doc.md** — Key Decisions in options·chosen·rationale form → [[artifact-adr]]-class decision records (plus schemas/architecture akin to [[artifact-design-md]]).
- **README.md** — background/goals/**scope**/dependencies; the context-and-boundaries brief (narrower than a full [[artifact-prd]] or [[artifact-proposal-md]]).
- **log.md** — the dated dev journal; the [[pattern-session-handoff|handoff]] and retrospective trail.

## Produced by (backlinks)

nano-spec:

- [[nano-spec-create]] — generates all four files from a one-line task description.
- [[nano-spec-update]] — maintains the pack and appends dated `log.md` entries as work proceeds.

## See Also
- [[artifact-plan-md]] — the plan/checklist class that `todo.md` belongs to.
- [[artifact-adr]] — the decision-record class that `doc.md` belongs to.
- [[artifact-spec-md]] · [[artifact-prd]] · [[artifact-spec-delta]] — the single-document specs this fixed four-file pack is the minimalist alternative to.
- [[stage-specify]] — the stage that produces this pack. </content>
