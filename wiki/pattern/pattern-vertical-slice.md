---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); Open GSD docs (2026); Addy Osmani — Agent Skills (2026); bmad-code-org/BMAD-METHOD (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Vertical slice

Decompose work into units that each cut top-to-bottom through the stack (UI → API → DB) so
every unit is independently buildable, shippable, and demoable — rather than horizontal
layers that only deliver value once all are complete.

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-to-tickets]] — produces "independently-grabbable" vertical-slice issues.

GSD:

- [[gsd-plan-phase]] — `--mvp` mode plans vertical slices (UI→API→DB).

Addy Osmani — Agent Skills:

- [[addy-planning]] — breaks work into independently shippable slices.
- [[addy-incremental-implementation]] — builds one slice at a time, top-to-bottom.

BMAD:

- [[bmad-create-epics-and-stories]] — decomposes requirements into epics of independently shippable stories.
- [[bmad-create-story]] — each [[artifact-story|story]] is one self-contained, shippable slice, built one at a time.

Compound Engineering:

- [[ce-work]] — executes the guardrailed plan slice-by-slice through quality gates.

Superpowers:

- [[sp-writing-plans]] — each task is the smallest unit that carries its own test cycle and is worth a reviewer's gate — an independently testable slice.

## See Also
- [[artifact-issue]] — how Matt's skills materialize a slice.
- [[stage-plan]] — the stage where this applies.
