---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-wave-parallelism]]", "[[pattern-vertical-slice]]"]
equivalent_to: ["[[seeds-tpl-pour]]"]
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd mol

`bd mol pour|wisp|show|current|progress|ready|bond|squash|burn|distill|seed|stale|last-activity` — **molecules**: the instantiation half of beads' workflow engine, and the one place in the tool that does genuine lifecycle work.

`bd mol pour <proto> --var version=1.2.0` turns a template into **real, dependency-ordered beads that flow through [[beads-ready]] like any other work** (liquid phase). That is the [[stage-plan]] edge: a multi-step body of work is decomposed into ordered units with their blocking edges wired, which is what [[seeds-tpl-pour]], [[speckit-tasks]], and [[mp-to-tickets]] each do by their own means. Beads' distinction is that the decomposition is *stamped from a reusable template* rather than reasoned out per task — closer to a macro than to planning, which is exactly why the charter is comfortable with it.

**The phase model is the distinctive contribution.** Beads is the only tool here that distinguishes work worth keeping from work worth forgetting at the data level:

| Phase | Command | Persistence |
|---|---|---|
| solid — proto | [[beads-cook]] | a template, not live work |
| liquid — molecule | `bd mol pour` | permanent, synced like any bead |
| vapor — wisp | `bd mol wisp` | ephemeral: excluded from federation push, deleted by `bd purge` |

Wisps exist because *"operational workflows — release checklists, health patrols, diagnostics — create beads that are worthless the moment they close."* And the phase is not a one-way door: `bd mol squash` compresses a molecule's execution into a digest and **promotes** a wisp that turned out to matter; `bd mol burn` deletes one that did not, irreversibly and without a digest. The docs' own rule is *"squash before you delete."*

The rest of the family is operational surface over live molecules: `bd mol ready` finds molecules ready for gate-resume dispatch, `current` and `progress` report position, `stale` detects *"complete-but-unclosed"* molecules, `bond` combines two molecules or protos (with phase overrides — `bd mol bond mol-critical-bug wisp-patrol --pour` persists a bug found during a throwaway patrol), and **`bd mol distill` extracts a formula from an existing epic**, turning work that already happened into a template for next time.

## Cross-tool comparison

[[seeds-tpl-pour]] does the same serial instantiation from a stored checklist; beads' version adds a real DAG (`needs`), variable substitution, gates, an ephemeral phase, and bonding. Against the process-layer decomposers ([[sp-writing-plans]], [[speckit-tasks]]) the difference is reuse: they decompose *this* piece of work by reasoning about it, beads replays a decomposition that was validated by having worked before.

## See Also
- [[beads-formula]] · [[beads-cook]] — the two phases before this one; `distill` closes the loop back to a formula.
- [[beads-gate]] — parks a molecule step on an external condition.
- [[beads-swarm]] — a molecule subtype for parallel epic dispatch.
- [[beads-delete]] — `bd purge`, the wisp reaper.
- [[stage-plan]] — the canonical stage this implements.
