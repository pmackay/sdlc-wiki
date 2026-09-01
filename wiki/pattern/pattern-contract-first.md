---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); GitHub/spec-kit (2026); jayminwest/seeds (2026); disler/super-simple-software-factory (2026)"
updated: 2026-08-31
---

# Pattern: Contract-first interface design

Design the **contract** — the API shape, types, error semantics, and boundary validation — before the implementation, and treat every observable behavior as a commitment. Governed by **Hyrum's Law** (with enough users, every observable behavior gets depended on, documented or not) and the **One-Version Rule**. Implications: expose intentionally, don't leak implementation details, validate at boundaries, and plan for deprecation at design time.

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-api-design]] — contract-first, Hyrum's Law, One-Version Rule, error semantics.

Spec Kit:

- [[speckit-plan]] — authors `contracts/` (REST endpoints, WebSocket events) during planning, before implementation.

This second framework promotes contract-first from an Addy-only technique to a **two-framework** pattern. Emphasis differs: Addy grounds it in Hyrum's Law and interface stability, whereas Spec Kit treats the `contracts/` directory as a *planning artifact* that [[speckit-tasks]] then derives contract-tests-first tasks from.

Seeds:

- [[seeds-config]] — publishes a JSON Schema for its own config file so an external UI ([[warren]]'s per-tool config editor) renders a form and writes back through per-knob commands, with no bespoke integration either side. The pattern applied to a config file: the schema is the interface, CLI and UI are both clients.

## Enabled by (infrastructure)

The [execution layer](../runtime/index.md) applies the pattern to a different interface — not an API between two programs, but the **seam between two agents**:

- [[sssf]] (library) — every agent call declares a concrete Pydantic `output_type`, and the agent's final JSON response is parsed against exactly that type; a response that does not validate re-prompts the *same session* with a correction naming the missing fields, so the contract is enforced rather than hoped for. Deterministic results are adapted into the same shape (`quality.as_envelope`, `changes.as_envelope`) so *"the consuming agent cannot tell the difference"* between a code result and an agent report. The contract is defined as a **synced triad** — the type in `data_types.py`, the JSON example in that agent's `user.md` `## Report` section, and `output_type=` at the call site — which must change in one edit, on the grounds that drift between the three is paid for on every call in correction rounds. Contract-first applied to agent-to-agent handoff: *"Context transfers in code, not in conversation."*

## See Also
- [[pattern-deep-modules]] — Ousterhout's complement: rich behavior behind a small, stable interface.
- [[addy-deprecation]] — how to retire a contract once users depend on it.
- [[stage-implement]] — where interfaces are designed and built.
