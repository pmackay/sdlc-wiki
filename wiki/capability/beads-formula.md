---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd formula

`bd formula list|show|convert` — manage **formulas**, the declarative source of a repeatable workflow: *"a TOML/JSON file defining a DAG of steps"*, with variable definitions (defaults and validation), `needs` dependencies between steps, composition rules for bonding formulas together, inheritance via `extends`, and optional `[steps.gate]` blocks that park a step on an async condition ([[beads-gate]]).

A formula can declare a `phase` — `vapor` recommends ephemeral instantiation as a wisp, and pouring a vapor formula persistently warns.

This is the front of beads' three-phase pipeline (formula → proto → molecule, see [[beads-cook]] and [[beads-mol]]), and the reason it belongs to a store rather than a framework is where the line falls: **a formula declares the shape of work and nothing about who does it.** No agent, no model, no retry policy, no scheduling — those are the *"workflow semantics"* and *"orchestration policy"* beads' charter explicitly assigns to the layer above. A formula is a reusable graph template; an orchestrator decides how to run it.

Its [[pattern-knowledge-compounding]] edge is the durable-artifact kind rather than the lesson kind: a release checklist or review pipeline that worked is captured once as a file on a search path and stamped out identically thereafter, and `bd mol distill` ([[beads-mol]]) extracts a formula *from an epic that already happened* — turning a completed body of work into a template for the next one. That is the same move as [[gstack-skillify]] and [[sp-writing-skills]], one layer down: what compounds is a work graph rather than a skill.

Maps to **no canonical SDLC stage** — authoring a template performs no lifecycle step. The instantiation does; see [[beads-mol]].

## See Also
- [[beads-cook]] — compiles a formula into a proto.
- [[beads-mol]] — instantiates the proto as real work; `distill` goes the other way.
- [[beads-gate]] — the async waits a formula step can declare.
- [[artifact-plan-record]] — [[seeds]]' single validated plan; a formula is the reusable-template generalization.
