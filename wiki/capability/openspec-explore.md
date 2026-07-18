---
type: capability
subtype: command
belongs_to: "[[openspec]]"
implements: "[[stage-align]]"
applies: ["[[pattern-spec-driven-development]]"]
equivalent_to: ["[[gsd-discuss-phase]]", "[[addy-idea-refine]]", "[[bmad-document-project]]"]
sources: "Fission-AI/OpenSpec docs — commands.md, concepts.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-04
---

# /opsx:explore

`/opsx:explore` — "Think through ideas, investigate problems, and clarify requirements before committing to a change." Opens an **exploratory conversation without creating any structure**: it investigates the codebase, compares candidate approaches, and clarifies requirements, then transitions to [[openspec-propose]] once the path is clear.

This is OpenSpec's **brownfield-first** entry point — the discovery phase that lets the framework be adopted on an existing codebase rather than only greenfield work. It produces no artifact; its output is a clarified, agreed technical direction that `propose` then turns into a change.

## Alignment flavor — investigate, don't only interrogate

OpenSpec aligns primarily by **investigating the codebase and comparing approaches**, where [[gsd-discuss-phase]] and [[mp-grill-me]] align by *interrogating the human*. Both close the same pre-build alignment gap ([[stage-align]]); explore is the *explore* substep of the `explore → shape → execute` arc, the counterpart to Addy's [[addy-idea-refine]]. BMAD's [[bmad-document-project]] shares the codebase-investigation flavor most directly.

## See Also
- [[openspec-propose]] — the change this discovery feeds into.
- [[gsd-discuss-phase]] — GSD's alignment phase (interrogation-led).
- [[addy-idea-refine]] — Addy's divergent/convergent exploration substep.
- [[bmad-document-project]] — BMAD's brownfield codebase-investigation counterpart.
- [[stage-align]] — the canonical stage this implements.
