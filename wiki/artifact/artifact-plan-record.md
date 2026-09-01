---
type: artifact
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md (MIT, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# Artifact: Plan record

A **plan as structured, schema-validated data** rather than as a document — one JSON object on one line of `.seeds/plans.jsonl`, with its own `pl-{4hex}` id space, bidirectionally linked to the seed that owns it and the child seeds it spawned.

It is the wiki's only non-prose plan artifact, and it exists because [[seeds]] set out to make one: *"Structured data, not prose. Plans are JSONL rows with validated fields. **No markdown plan documents anywhere in the artifact path.** The plan is queryable, validatable, mechanically traversable."* Every other framework here produces [[artifact-plan-md]] — a `plan.md` or `tasks.md` that a later step re-reads and re-interprets.

## Shape

```json
{"id":"pl-a1b2","seed":"seeds-9c4d","template":"feature","status":"approved","revision":1,
 "sections":{"context":"…","approach":"…","alternatives":[{"name":"…","rejected_because":"…"}],
   "steps":[{"title":"Add OAuth provider config","type":"task","priority":2,"blocks":[2],"labels":["auth"]}],
   "risks":["Token refresh race (mx-902)"],"acceptance":["Login flow completes end-to-end"]},
 "children":["seeds-aa01","seeds-aa02"],"adoptedChildren":["seeds-aa05"],
 "outcome":null,"reviewedBy":null,"createdAt":"…","updatedAt":"…"}
```

- **`sections`** is template-shaped, not fixed. Which sections exist, which are required, and what validation applies come from the template declared in `.seeds/config.yaml`; an AJV schema is generated from that declaration and enforced by [[seeds-plan-submit]].
- **`steps`** is the executable part: each entry spawns one child seed, and its 1-based `blocks: [j]` indices are translated into real `blockedBy` edges on the spawned ids. A step may instead adopt an existing seed (`existing_seed`) or require its own sub-plan (`plan_template`).
- **`status`** is derived, not set: `draft` on prompt, `approved` on successful submit, `active` as soon as any child is `in_progress`, `done` when all children close.
- **`revision`** increments on every mutation. Revisions are not kept as rows — *"Git history of `plans.jsonl` is the audit trail"* — which is the same argument [[seeds]] makes for having no audit trail of its own.

## Why the data form matters

Three consequences a markdown plan cannot offer:

- **It is enforceable.** The plan and the work queue are the same object graph, so "step 3 depends on step 1" is a `blockedBy` edge that hides step 3 from [[seeds-ready]], not a sentence an agent is asked to honour.
- **It is consumable by other layers.** [[warren]]'s serial plan-run walks `plan.children` verbatim (`seq = index + 1`), one agent run per child, gated on the previous PR merging — which is why [[seeds-plan-reorder]] exists as a first-class command with a permutation check. The ordering *is* the schedule.
- **It is re-checkable.** [[seeds-plan-validate]] re-runs a plan against the *current* template, so tightening a rule after a failure ([[seeds-config]]) applies retroactively to plans already in flight.

The cost is symmetrical and worth stating: a schema checks shape, never quality. The gate notices a missing `risks` array; it cannot notice that the approach is wrong.

## Produced by (backlinks)
- [[seeds-plan-submit]] — validates the filled plan, spawns children, writes the row.
- [[seeds-plan-create]] — writes an adopt-only row with zero spawned children, for release trains.

## See Also
- [[artifact-plan-md]] — the prose counterpart every other framework produces; the direct contrast.
- [[artifact-issue]] — what a plan's steps become, one child seed per step.
- [[artifact-story]] — BMAD's richer unit, the other artifact here that carries plan context down to the implementer; a story inlines the context as prose, a plan record links to it as data.
- [[pattern-plan-verification-loop]] — the gate applied to this artifact before its children exist.
- [[seeds]] — the framework that produces it.
