---
type: artifact
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# Artifact: Diataxis documentation

A set of project documentation organized by the **Diataxis** framework's four quadrants —
**tutorial, how-to, reference, explanation** — generated to match the code and tracked against a
**coverage map** so gaps are visible (surfaced in the PR body at release time). gstack produces this
via two skills: [[gstack-document-generate]] writes missing docs from scratch (researching the
codebase first), and [[gstack-document-release]] updates whatever drifted after a ship and reports
remaining coverage gaps.

Distinctive for enforcing the **four-quadrant taxonomy** and a coverage map, rather than a single
free-form README. It is the release-stage documentation output; a broader, structured relative of
Addy's [[addy-documentation]] outputs ([[artifact-adr]] + inline docs) and BMAD's tech-writer docs
([[bmad-tech-writer]]).

## Produced by (backlinks)
- [[gstack-document-generate]] — generates missing tutorial/how-to/reference/explanation docs from code.
- [[gstack-document-release]] — updates drifted docs and reports the Diataxis coverage map at release.

## See Also
- [[artifact-adr]] — a narrower, decision-record documentation artifact ([[addy-documentation]]).
- [[artifact-changelog]] — the what-shipped record, versus this how-to-use documentation.
- [[stage-release]] — the stage this artifact is produced in.
