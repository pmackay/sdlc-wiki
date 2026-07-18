---
type: capability
subtype: skill
belongs_to: "[[addy-agent-skills]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: ["[[mp-ask-matt]]", "[[gstack-router]]", "[[sp-using-superpowers]]"]
sources: "Addy Osmani — Agent Skills (2026)"
raw: ["../../raw/addy-agent-skills/2026-07-04-agent-skills.md"]
updated: 2026-07-09
---

# Using Agent Skills

The **meta-skill router** for the pack: when a task arrives it identifies the
development phase and dispatches to the matching skill — [[addy-interview-me]] when
the ask is underspecified, [[addy-spec-driven-development]] for a new feature,
[[addy-tdd]] when writing tests, and so on down a decision tree. It governs no single
stage because it governs all of them.

It also fixes the **shared operating rules** every other skill inherits: surface
assumptions, manage confusion actively, push back rather than yes-machine, enforce
simplicity, keep scope discipline, and never call a task done without verification.
It is the model-invoked counterpart to a routing entrypoint — the thing the agent
consults first to decide which workflow to run.

## See Also
- [[addy-agent-skills]] — the framework this skill indexes.
- [[addy-spec-driven-development]] — the default entry when a non-trivial task has no spec.
- [[addy-interview-me]] — where it routes an ask that isn't yet understood.
