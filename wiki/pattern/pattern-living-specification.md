---
type: pattern
sources: "Fission-AI/OpenSpec — concepts.md (2026); pstack v0.15.2 — Lauren Tan (2026)"
updated: 2026-09-11
---

# Pattern: Living specification (spec-as-source-of-truth + deltas)

Keep a **permanent specification that describes how the system currently behaves**, and express every change as a **delta against it** rather than as a throwaway per-change spec. On completion the delta is merged back in, so the spec is continuously maintained as the durable source of truth.

Two coupled moves:

1. **Living spec as source of truth.** A standing spec (`openspec/specs/`, organized by domain, written as RFC-2119 requirements + Given/When/Then scenarios) always reflects *current* behavior — not a per-feature document abandoned after the feature ships.
2. **Change-as-delta.** Each change is a [[artifact-spec-delta]] with ADDED / MODIFIED / REMOVED / RENAMED sections. Deltas are small, avoid rewriting the whole spec, prevent merge conflicts across parallel changes, and make the approach **brownfield-first**. On archive the delta is applied (RENAMED → REMOVED → MODIFIED → ADDED) and folded into the living spec.

The full cycle: current specs → propose deltas → implement → archive merges deltas → specs describe new behavior → repeat.

## Why it's distinctive

This is the axis on which OpenSpec differs from every other framework in the wiki. GSD, Matt Pocock, and Addy all drive from [[pattern-spec-driven-development]] too — but their spec/PRD/plan is a **per-change artifact** written, executed, and left behind ([[artifact-prd]], [[artifact-spec-md]], [[artifact-plan-md]]). Only OpenSpec keeps the spec **permanent and self-updating**, which is also why its "release" step is spec-maintenance ([[openspec-sync]]) rather than deployment.

## Applied by (backlinks)

OpenSpec:

- [[openspec-propose]] — authors changes as deltas against the living spec.
- [[openspec-sync]] — merges a delta into the living spec.
- [[openspec-archive]] — finalizes the change, folding its delta in.

pstack — applied to a **verification** artifact rather than a requirements one:

- [[pstack-maintain-verification-skill]] — *"a feature map rots the moment the app changes."* A scheduled pass reconciles the map against the app with one read-only subagent per feature plus one live pass, shipping at most one PR of proven corrections. Its key rule forces the fork the pattern always faces: a behavior the map describes that the app no longer does is either **doc drift** (fix the map) or a **product regression** (report it, do not paper over it in docs).

## See Also
- [[pattern-spec-driven-development]] — the broader pattern this specializes.
- [[artifact-spec-delta]] — the delta artifact this pattern is built on.
- [[openspec]] — the framework built around this pattern.
