---
type: capability
subtype: command
belongs_to: "[[speckit]]"
implements: "[[stage-align]]"
produces: "[[artifact-constitution]]"
applies: "[[pattern-project-constitution]]"
sources: "GitHub/spec-kit README + spec-driven.md (2026)"
raw: ["../../raw/speckit/2026-07-04-speckit-framework.md"]
updated: 2026-07-04
---

# speckit-constitution

**`/speckit.constitution`** — "Create or update project governing principles and development guidelines." The first phase of the Spec Kit workflow: it establishes the project's **immutable architectural principles** in `.specify/memory/constitution.md` — described as nine numbered "articles" (I–III universal: library-first design, CLI interfaces, test-driven development; IV–VI project-defined; VII–IX mandating simplicity, anti-abstraction, and integration-first testing).

The constitution is "the architectural DNA of the system, ensuring that every generated implementation maintains consistency." It is not consumed and discarded like a per-change spec — it persists and is the reference every later phase is checked against: [[speckit-plan]] validates its choices against the constitution through "phase gates," and [[speckit-analyze]] audits all artifacts for constitutional compliance.

## Why it maps to align (with a caveat)

This is Spec Kit's signature capability and it has **no counterpart in any other framework** here — GSD, Matt Pocock, Addy, and OpenSpec all embed principles *inside* individual skills rather than externalizing them into one governing document. It is filed under [[stage-align]] as the most generic fit (agreeing the rules of engagement before building), but it is really a **governance-setup** activity that sits upstream of the per-change lifecycle. See the `stage-govern` split candidate parked on [[stage-align]] — it needs a second framework's evidence before it could become a canonical stage.

## See Also
- [[speckit]] — the framework.
- [[artifact-constitution]] — the document it produces.
- [[pattern-project-constitution]] — the technique it embodies.
- [[speckit-analyze]] — the gate that enforces the constitution across all artifacts.
