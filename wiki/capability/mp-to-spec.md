---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-specify]]"
delegates_to: []
produces: ["[[artifact-spec-md]]"]
applies: ["[[pattern-spec-driven-development]]", "[[pattern-deep-modules]]"]
equivalent_to: ["[[addy-spec-driven-development]]", "[[openspec-propose]]", "[[speckit-specify]]", "[[bmad-prd]]", "[[gstack-spec]]", "[[bm-prd-creator]]", "[[nano-spec-create]]", "[[agent-os-shape-spec]]"]
docs_url: "https://www.aihero.dev/skills-to-spec"
sources: "Matt Pocock — Skills for Real Engineers v1.1 (2026); v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md", "../../raw/matt-pocock-skills/2026-07-09-skills-v1.1-update.md"]
updated: 2026-10-11
---

# to-spec

`/to-spec` — a user-invoked engineering skill that synthesizes the current conversation (and codebase understanding) into a **spec** and publishes it to the configured issue tracker with the `ready-for-agent` triage label. "Spec" is Matt Pocock's single through-line term for this document, so the output is paged as [[artifact-spec-md]]; its template leads with a Problem Statement. Deliberately **no interview**: it just synthesizes what has already been discussed (do the interview first with [[mp-grill-with-docs]] / [[mp-grill-me]]). Before writing, it **sketches the testing seams** (preferring existing seams, the highest and fewest possible) and confirms them with the user — the "daily design investment" answer to failure mode #4 (ball of mud).

It is also where [[mp-wayfinder]] hands off: when a wayfinder map clears, `/to-spec` collapses the map's linked decisions into a buildable plan.

MP's member of the multi-framework **specify** cluster ([[pattern-spec-driven-development]]) — write the durable spec before code. With Addy's [[addy-spec-driven-development]] it was the **original pair** whose distinct treatment of spec authoring promoted [[stage-specify]] out of [[stage-plan]]. Its seam-sketching applies deep-module thinking ([[pattern-deep-modules]]). Feeds [[mp-to-tickets]], which slices the spec into tickets.

## See Also
- [[mp-to-tickets]] — breaks this spec into tracer-bullet tickets ([[stage-plan]]).
- [[mp-grill-with-docs]] · [[mp-grill-me]] — the interview that precedes synthesis (this skill does no interview of its own).
- [[addy-spec-driven-development]] — Addy's spec-first counterpart (`SPEC.md`); the original specify pair.
- [[speckit-specify]] · [[openspec-propose]] · [[bmad-prd]] · [[gstack-spec]] — specify-cluster counterparts.
- [[stage-specify]] — the canonical stage this implements.

## Version history

### v1.2.0 (2026-08-05)
- Finished the `to-prd` → `to-spec` rename: the opening "you may know this document as a PRD" was dropped from the skill and its docs page, and the tracker templates say "specs" rather than "PRDs". [[mp-ask-matt]] routes [[mp-wayfinder]]'s handoff here.

### v1.1.0 (2026-07-08; ingested 2026-07-09)
- Renamed from `/to-prd`; "spec" became the through-line term, so the output moved from [[artifact-prd]] to [[artifact-spec-md]]. The skill still opened "you may know this as a PRD" for discoverability.

### Initial ingest (2026-06-28)
- Documented as `to-prd`: synthesize the current conversation into a PRD and publish it to the issue tracker.
