---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-spec-md]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-deep-modules]]"]
equivalent_to: ["[[addy-spec-driven-development]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[bmad-prd]]", "[[gstack-spec]]", "[[bm-prd-creator]]", "[[nano-spec-create]]"]
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026)"
raw: ["../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-07-09
---

# to-spec

`/to-spec` — a user-invoked engineering skill that synthesizes the current conversation (and
codebase understanding) into a **spec** — "you may know this document as a PRD" — and publishes it
to the configured issue tracker with the `ready-for-agent` triage label. Deliberately **no
interview**: it just synthesizes what has already been discussed (do the interview first with
[[mp-grill-with-docs]] / [[mp-grill-me]]). Before writing, it **sketches the testing seams**
(preferring existing seams, the highest and fewest possible) and confirms them with the user — the
"daily design investment" answer to failure mode #4 (ball of mud).

> **Renamed from `/to-prd` (v1.1, 2026-07-09).** "Spec" is now Matt Pocock's single through-line
> term for this document. The output is therefore paged as [[artifact-spec-md]], not
> [[artifact-prd]] — though the skill still opens "you may know this as a PRD" for discoverability,
> and its template leads with a Problem Statement.

MP's member of the multi-framework **specify** cluster ([[pattern-spec-driven-development]]) — write
the durable spec before code. With Addy's [[addy-spec-driven-development]] it was the **original
pair** whose distinct treatment of spec authoring promoted [[stage-specify]] out of [[stage-plan]].
Its seam-sketching applies deep-module thinking ([[pattern-deep-modules]]). Feeds
[[mp-to-tickets]], which slices the spec into tickets.

## See Also
- [[mp-to-tickets]] — breaks this spec into tracer-bullet tickets ([[stage-plan]]).
- [[mp-grill-with-docs]] · [[mp-grill-me]] — the interview that precedes synthesis (this skill does no interview of its own).
- [[addy-spec-driven-development]] — Addy's spec-first counterpart (`SPEC.md`); the original specify pair.
- [[speckit-specify]] · [[openspec-propose]] · [[bmad-prd]] · [[gstack-spec]] — specify-cluster counterparts.
- [[stage-specify]] — the canonical stage this implements.
