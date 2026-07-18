---
type: capability
subtype: command
belongs_to: "[[openspec]]"
implements: "[[stage-release]]"
delegates_to: ["[[openspec-sync]]"]
applies: ["[[pattern-living-specification]]", "[[pattern-spec-driven-development]]"]
equivalent_to: ["[[gsd-ship]]", "[[addy-shipping]]", "[[ce-commit-push-pr]]", "[[gstack-ship]]", "[[sp-finishing-a-development-branch]]"]
sources: "Fission-AI/OpenSpec docs — commands.md, concepts.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-04
---

# /opsx:archive

`/opsx:archive` — "Archive a completed change." It finalizes the work: **optionally syncs** the change's delta into the living spec (via [[openspec-sync]]), then **moves the change folder to `openspec/changes/archive/` with a timestamp**, preserving an audit trail of completed work with its full context.

This is OpenSpec's close-the-loop step — the point at which a temporary change becomes permanent spec and is retired. `/opsx:bulk-archive` (expanded profile) does the same for several changes at once, resolving spec conflicts across simultaneous changes by inspecting actual implementation and archiving in chronological order; `openspec archive` is the terminal-CLI alternative.

## Cross-framework equivalents

The **ship / finalize** cluster spans three frameworks: OpenSpec's `archive` ↔ GSD's [[gsd-ship]] ↔ Addy's [[addy-shipping]] (`equivalent_to`) — each closes the iteration on a completed unit of work. But they finalize *different things*: GSD opens and tracks a PR, Addy runs a launch checklist + parallel review personas, and OpenSpec merges the spec delta and archives the change. OpenSpec's is the only one that is pure spec-maintenance with no deployment — see [[stage-release]].

## See Also
- [[openspec-sync]] — the merge step archive invokes.
- [[openspec-verify]] — advisory validation that precedes (but does not gate) archiving.
- [[gsd-ship]] · [[addy-shipping]] — finalization-cluster counterparts.
- [[stage-release]] — the canonical stage this implements.
