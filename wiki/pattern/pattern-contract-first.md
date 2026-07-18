---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); GitHub/spec-kit (2026)"
updated: 2026-07-04
---

# Pattern: Contract-first interface design

Design the **contract** — the API shape, types, error semantics, and boundary validation — before the implementation, and treat every observable behavior as a commitment. Governed by **Hyrum's Law** (with enough users, every observable behavior gets depended on, documented or not) and the **One-Version Rule**. Implications: expose intentionally, don't leak implementation details, validate at boundaries, and plan for deprecation at design time.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-api-design]] — contract-first, Hyrum's Law, One-Version Rule, error semantics.

Spec Kit:

- [[speckit-plan]] — authors `contracts/` (REST endpoints, WebSocket events) during planning, before implementation.

This second framework promotes contract-first from an Addy-only technique to a **two-framework** pattern. Emphasis differs: Addy grounds it in Hyrum's Law and interface stability, whereas Spec Kit treats the `contracts/` directory as a *planning artifact* that [[speckit-tasks]] then derives contract-tests-first tasks from.

## See Also
- [[pattern-deep-modules]] — Ousterhout's complement: rich behavior behind a small, stable interface.
- [[addy-deprecation]] — how to retire a contract once users depend on it.
- [[stage-implement]] — where interfaces are designed and built.
