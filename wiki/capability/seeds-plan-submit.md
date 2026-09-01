---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-plan-record]]", "[[artifact-issue]]"]
applies: ["[[pattern-plan-verification-loop]]", "[[pattern-deterministic-gates]]", "[[pattern-vertical-slice]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[mp-to-tickets]]", "[[gsd-plan-phase]]", "[[speckit-tasks]]", "[[addy-planning]]", "[[sp-writing-plans]]"]
sources: "Jaymin West — jayminwest/seeds PLAN_SPEC.md + README.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd plan submit

`sd plan submit <seed-id> --plan <file>` — the framework's centre of gravity. It validates a filled plan against its template, spawns one child seed per step, wires the dependency edges between them, writes the [[artifact-plan-record|plan row]] to `.seeds/plans.jsonl` with status `approved`, and blocks the parent seed on its children. Flags: `--overwrite` to replace an existing non-draft plan, `--name` for a human-readable label, `--record-decision` to write the chosen approach back to mulch, `--domain` to pin domain inference.

```
✓ plan pl-a1b2 created (status: approved)
✓ spawned 4 child seeds: seeds-aa01, seeds-aa02, seeds-aa03, seeds-aa04
✓ seeds-9c4d now blocked by 4 children
```

## The gate

Validation is an **AJV schema generated from the template config**, not a prompt: required sections present and non-empty, `min_length` on text, `min` on lists and steps, every `steps[].blocks` index inside `1..steps.length` with self-references rejected, each step declaring either a `title` (fresh spawn) or an `existing_seed` (adoption), object-spec fields matching their declared `kind`, and the `template` name resolving. Failure is **fail-fast and pre-write** — both JSONL files are untouched — and stderr carries a patchable partial-state diff:

```json
{ "errors": [ { "path": "sections.steps", "code": "min", "fix": "add at least 1 more step entry" } ],
  "current": { "…plan-as-submitted…" } }
```

so the agent patches and resubmits without re-running [[seeds-plan-prompt]]. That is [[pattern-plan-verification-loop]] with the checker replaced by a program: the cluster's other five gates ([[gsd-plan-checker]], [[speckit-analyze]], [[bmad-check-implementation-readiness]], [[ce-doc-review]], [[gstack-plan-eng-review]]) are all models asked to judge a plan and can be argued with; this one exits non-zero ([[pattern-deterministic-gates]]). The trade is equally sharp — it checks *shape*, never *quality*. Nothing here notices that an approach is wrong, only that the approach field is under fifty characters.

## The spawn

Each `steps[]` entry becomes a child seed carrying the step's `title`, `type`, `priority`, and normalized `labels`; a step's 1-based `blocks: [j]` means *this step blocks step j*, translated on submit into real ids on both endpoints' `blocks` / `blockedBy`. The template's own instruction for the section — *"Decompose into ordered, independent implementation steps"* — is the [[pattern-vertical-slice]] edge. A step may instead declare `plan_template:` to spawn a child requiring its own sub-plan (`requires_plan: true`, hidden from [[seeds-ready]] until that plan is approved), or `existing_seed:` to adopt an already-open seed at that index rather than duplicating it.

`--overwrite` re-plans in place: the row is replaced atomically, `revision` increments, and new steps are diffed against current children **id-first** (`existing_seed`), then by title, then spawned fresh. Children whose step is gone are reported as *obsolete* with a suggested close command but are **never auto-closed** — *"the LLM has the context to decide whether the existing work is still useful."*

## Cross-framework equivalents

The decomposition cluster spans six frameworks: [[gsd-plan-phase]], [[speckit-tasks]], [[addy-planning]], [[sp-writing-plans]], [[mp-to-tickets]], and this. Five of them write markdown a later step re-reads; seeds writes a validated record and spawns the work items itself in the same call, so there is no gap between "the plan says step 3 depends on step 1" and the queue enforcing it.

## See Also
- [[seeds-plan-prompt]] — produces the request this consumes.
- [[seeds-plan-edit]] · [[seeds-plan-adopt]] · [[seeds-plan-reorder]] — post-submit surgery on what this creates.
- [[seeds-ready]] — where the spawned children surface, in dependency order.
- [[artifact-plan-record]] · [[artifact-issue]] — what it produces.
- [[stage-plan]] — the canonical stage this implements.
