---
type: artifact
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# Artifact: constitution

Spec Kit's **signature artifact** — `.specify/memory/constitution.md`, a set of **immutable,
project-wide governing principles** written once and treated as "the architectural DNA of
the system." Structured as numbered **articles**:

- **Articles I–III** — universal: library-first design, CLI interfaces, test-driven development.
- **Articles IV–VI** — project-defined: teams encode domain-specific governance.
- **Articles VII–IX** — simplicity, anti-abstraction, and integration-first testing.

What makes it distinctive is not *having* principles — every framework here has opinions —
but **externalizing them into one durable, versioned document that later phases are
mechanically gated against**. [[speckit-plan]] validates its technology choices against the
constitution through "Phase -1" gates (enforcing simplicity ≤3 projects, framework-direct
usage, integration-first tests), and [[speckit-analyze]] audits every artifact for
constitutional compliance. GSD, Matt Pocock, and Addy instead embed principles *inside*
individual skills; OpenSpec has no equivalent.

Unlike a per-change spec/plan, the constitution is **not consumed and discarded** — it
persists across all features and is updated only deliberately (via [[speckit-constitution]]).

## Produced by (backlinks)
- [[speckit-constitution]] — creates and updates it.

## See Also
- [[pattern-project-constitution]] — the technique this artifact realizes.
- [[speckit-analyze]] — the gate that enforces it across all planning artifacts.
- [[artifact-adr]] — a narrower, per-decision governance record (Addy/MP), versus this project-wide charter.
- [[stage-align]] — the stage this artifact supports.
