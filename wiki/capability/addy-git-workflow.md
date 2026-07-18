---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]", "[[artifact-changelog]]"]
applies: ["[[pattern-trunk-based-development]]"]
equivalent_to: ["[[ce-commit]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-04
---

# Git Workflow & Versioning

Treats git as the safety net that keeps agent-generated change manageable: commits as save
points, branches as sandboxes, history as documentation. It applies
[[pattern-trunk-based-development]] — keep `main` deployable, work in short-lived branches that
merge within 1-3 days, and prefer feature flags over long branches — and enforces atomic
commits (one logical thing each, an [[artifact-atomic-commit]]), descriptive messages that
explain the *why*, and change sizing (~100 lines, split above ~1000).

The versioning half is the consumer-facing contract: semantic `MAJOR.MINOR.PATCH` bumps where
the number is a promise, immutable tags as the source of truth for a release, and a curated
[[artifact-changelog]] grouped by impact (Added / Changed / Fixed / Deprecated / Removed /
Security) written with the change while its impact is fresh — never reconstructed at release
time from commit archaeology.

## See Also
- [[pattern-trunk-based-development]] — the branching discipline it applies.
- [[artifact-atomic-commit]] — the commit unit it produces.
- [[artifact-changelog]] — the consumer-facing release record it produces.
- [[stage-release]] — the canonical stage this implements.
