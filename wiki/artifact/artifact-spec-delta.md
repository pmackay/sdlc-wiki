---
type: artifact
sources: "Fission-AI/OpenSpec — concepts.md (2026)"
raw: ["../../raw/openspec/2026-07-04-openspec-framework.md"]
updated: 2026-07-04
---

# Artifact: spec delta

OpenSpec's **signature artifact** — `openspec/changes/<name>/specs/<domain>/spec.md`. Rather
than rewrite the whole product spec for a change, a delta describes only **what is changing**
relative to the living spec (`openspec/specs/`), under three sections:

```markdown
## ADDED Requirements
### Requirement: <new behavior>          # appended to main spec on merge

## MODIFIED Requirements
### Requirement: <changed behavior>       # replaces the existing requirement
[updated text] (Previously: <old text>)

## REMOVED Requirements
### Requirement: <deprecated behavior>    # deleted from main spec
(Reason for removal)
```

Each requirement is a single behavioral statement using **RFC 2119** keywords (MUST/SHALL,
SHOULD, MAY) and carries **Given/When/Then scenarios** as concrete, testable examples:

```markdown
#### Scenario: <case>
- GIVEN <precondition>
- WHEN <action>
- THEN <observable result>
```

On [[openspec-sync]] / [[openspec-archive]] the sections are applied in strict order —
**RENAMED → REMOVED → MODIFIED → ADDED** — and merged into the living spec, which then again
describes current behavior. Deltas keep changes small, prevent merge conflicts across
parallel changes, and make the framework **brownfield-first**.

The living `openspec/specs/` is the durable source of truth this delta targets; the delta
itself is temporary, discarded (into `archive/`) once merged. This is the mechanism behind
[[pattern-living-specification]].

## Produced by (backlinks)
- [[openspec-propose]] — authors the delta as part of the one-step proposal.
- [[openspec-sync]] — merges the delta into the living spec (its consumer).

## See Also
- [[artifact-proposal-md]] — the why/what that accompanies the delta in a change folder.
- [[artifact-spec-md]] · [[artifact-prd]] — whole-spec counterparts from other frameworks (rewritten, not delta'd).
- [[pattern-living-specification]] — the pattern this artifact realizes.
- [[stage-specify]] — the stage that produces it.
