---
type: capability
subtype: command
belongs_to: "[[openspec]]"
implements: "[[stage-release]]"
produces: ["[[artifact-spec-delta]]"]
applies: ["[[pattern-living-specification]]", "[[pattern-spec-driven-development]]"]
sources: "Fission-AI/OpenSpec docs — commands.md, concepts.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-04
---

# /opsx:sync

`/opsx:sync` — "Merge delta specs from a change into main specs." It intelligently
integrates a change's [[artifact-spec-delta]] into the living `openspec/specs/`, applying the
delta sections in strict operation order — **RENAMED → REMOVED → MODIFIED → ADDED** — so that
ADDED requirements are appended, MODIFIED requirements replace their originals, and REMOVED
requirements are deleted. "Usually invoked during archive, rarely needed manually."

This is the mechanical heart of [[pattern-living-specification]]: the step that turns a
temporary change back into permanent, source-of-truth spec. It is unique in this wiki — no
other framework maintains a durable spec that changes are merged *into*.

## A release step, OpenSpec-style

`sync` (with [[openspec-archive]]) is OpenSpec's finalization, so it `implements:`
[[stage-release]] — but its flavor is **spec-maintenance, not deployment**. Where GSD's
[[gsd-ship]] opens a PR and Addy's [[addy-shipping]] runs a launch checklist, OpenSpec's
"release" simply folds the delta into the living spec so the spec once again describes
current behavior. There is no deploy / CI / observability analogue.

## See Also
- [[openspec-archive]] — normally triggers sync as part of finalizing a change.
- [[artifact-spec-delta]] — the input; the living spec is its merge target.
- [[pattern-living-specification]] — the pattern this step realizes.
- [[stage-release]] — the canonical stage this implements.
