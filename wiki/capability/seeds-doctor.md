---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-deterministic-gates]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd doctor

`sd doctor [--fix]` — check project health and data integrity, and optionally repair what it finds.

Its checks are of two kinds. **Setup drift**: it verifies all three `merge=union` lines are present in `.gitattributes` and backfills any missing one, sourcing the canonical list from [[seeds-init]] rather than a hardcoded pair — a real bug class, since a store initialized before `plans.jsonl` existed silently loses union-merge on plans. **Data shape**: the `extensions-schema` check flags any issue whose `extensions` value is not a plain object (arrays, `null`, scalars are rejected at write time by [[seeds-update]] but can arrive via a hand-edited file or a bad merge); `--fix` drops them.

A pure [[pattern-deterministic-gates]] instance at the tooling level — program-decided verdicts over the store, with an exit code, no model involved. Maps to **no canonical SDLC stage**: it audits the tracker, not the product. (Contrast [[gstack-health]], which runs the same *kind* of check over the codebase and therefore does implement [[stage-review]].)

## See Also
- [[seeds-init]] — the setup this verifies.
- [[seeds-update]] — the write-time validation this backstops.
- [[pattern-deterministic-gates]] — the pattern it applies.
