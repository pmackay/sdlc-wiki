---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: ["[[seeds-doctor]]"]
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd doctor

`bd doctor [--fix]` — *"check and fix beads installation health (start here)"*, and the single place beads consolidates every remediation. Its own CLI-design rule explains why: *"Recovery/fix operations → `bd doctor --fix`. Don't create separate commands like `bd recover` or `bd repair`. Doctor already detects problems — let `--fix` handle remediation. This keeps all health-related operations in one discoverable place."*

Two checks are worth naming:

- **Orphan detection** cross-references open beads against git history to find *"work that was committed but the issue wasn't closed"*, keyed off the `(bd-abc)` commit convention. A tracker-versus-repository consistency check that only a store living in the repo can run.
- **Divergence and drift** — hook format drift ([[beads-hooks]]), config-vs-reality drift ([[beads-config]]), and an explicit `<!-- bd-doctor-divergence: ok -->` marker convention so a project can declare an intentional difference between `AGENTS.md` and `CLAUDE.md` and stop it being flagged. That marker is a small, well-judged idea: the checker distinguishes *unnoticed* drift from *decided* difference.

A pure [[pattern-deterministic-gates]] instance at the tooling level — program-decided verdicts with an exit code, no model involved — and one that is being widened conservatively: embedded-mode support is *"enabled one subcommand at a time, each human-vetted."*

Maps to **no canonical SDLC stage**: it audits the store and its installation, not the product. (Contrast [[gstack-health]], which runs the same kind of check over the *codebase* and therefore does implement [[stage-review]].)

## See Also
- [[beads-lint]] · [[beads-graph]] · [[beads-preflight]] — the other three self-checks, on issue content, graph integrity, and the working tree.
- [[beads-hooks]] · [[beads-config]] — the drift this detects.
- [[seeds-doctor]] — the cross-store counterpart.
