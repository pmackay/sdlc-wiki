---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd lint

`bd lint` — *"check issues for missing template sections"*: a linter for the **content of work items**, not for code.

The premise is that a bead an agent will pick up weeks later needs to actually contain what the picker will need. Beads keeps those fields structurally separate — `--description`, `--design`, `--notes`, `--acceptance` ([[beads-update]]) — and `bd lint` reports the ones left empty, so an under-specified bead is caught before it reaches the [[beads-ready|frontier]] and stalls whoever claims it.

It is the store-layer analogue of the process layer's plan gates ([[pattern-plan-verification-loop]]): [[seeds-plan-submit]] validates a plan's sections against a template with AJV, and this validates a bead's sections against a template with an exit code. The difference is scope and ambition — seeds refuses to *write* an incomplete plan, beads *reports* incomplete beads after the fact. Detective rather than preventive, in the vocabulary [[topic-harness-engineering]] uses.

One of beads' four self-checks, alongside [[beads-doctor]] (installation), [[beads-graph]] `check` (graph integrity), and [[beads-preflight]] (working tree).

Maps to **no canonical SDLC stage** — it audits work descriptions, not the product.

## See Also
- [[beads-doctor]] · [[beads-graph]] · [[beads-preflight]] — the sibling checks.
- [[seeds-plan-submit]] — the preventive version of the same idea, one layer up.
- [[pattern-deterministic-gates]] — the pattern it applies.
