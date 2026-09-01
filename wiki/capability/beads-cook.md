---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd cook

`bd cook <formula-file>` — compile a formula into a **proto**: *"a template epic with `{{variables}}`, carrying the `template` label, reusable, not yet live work"* (solid phase, in the chemistry metaphor the CLI runs with).

Two modes, and the split is more interesting than it first looks:

- **compile-time** (default) keeps `{{variable}}` placeholders intact — *"use for modeling, estimation, contractor handoff, planning."*
- **runtime** (`--mode=runtime`, or implied by any `--var`) substitutes every variable and requires them all to have values — *"use for final validation before pour, seeing exact output."*

So a cooked-but-unresolved proto is a *quotable* work graph: you can hand someone the shape of a release or a migration, with its step count and dependency structure, before committing to the specifics. That is an unusual affordance for a tracker and it only makes sense because the plan is data.

By default cook writes JSON to stdout and the proto is **ephemeral** — `pour` and `wisp` accept formula names directly and cook inline, so `--persist` (writing the proto into the database as a labelled bead with children and edges) is documented as *"legacy behavior"* for when you want to reuse the same proto repeatedly. `--dry-run` previews; `--prefix` namespaces the proto id.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-formula]] — the source this compiles.
- [[beads-mol]] — pours the proto into real beads.
- [[beads-label]] — the `template` label that identifies a persisted proto.
