---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-wave-parallelism]]", "[[pattern-fresh-context-subagents]]", "[[pattern-context-engineering]]", "[[pattern-worktree-isolation]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[sp-dispatching-parallel-agents]]", "[[mp-implement-spec]]"]
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-10-11
---

# /swarm

Fans out N parallel workers, drains them, and returns **one** report. The framework's coverage-and-race primitive, sibling to [[pstack-arena]]: swarm covers separate slices or races identical briefs, arena competes on the same artifact and grafts.

Four phases. **Frame** states the done predicate and the artifact the swarm must return, then picks the shape — partition into slices, race N workers on identical briefs, or mix both — and for a race or mixed shape declares the selection rule **before spawning**: `first pass`, `rank all`, or `best-of`. **Fan out** spawns all N in one message with `environment: "cloud"` and `run_in_background: true`, dropping to `environment: "local"` only when a worker needs something on the user's computer, and passing `cloud_base_branch` when a worker must start from a non-default pushed branch. **Aggregate** reads the terminal results and applies the pre-declared rule. **Report** returns one consolidated in-chat report.

Three details carry the weight.

- **Every brief stands alone**: goal, scope, the exact slice or race arm, how to verify, and what to report. Workers report `PASS`, `ISSUES`, or `BLOCKED` with evidence, so aggregation is mechanical rather than interpretive.
- **The selection rule is declared before spawning, not after reading.** That is a deliberate guard against picking the winner you like once you have seen the results.
- ***Do not paste raw worker dumps.*** The parent returns a compact result table, one-line evidenced issues, and explicit gaps or dropouts. This is [[pattern-context-engineering]] enforced at the aggregation boundary, and the direct expression of [[pstack-principle-guard-the-context-window]].

Its **cloud-default** is worth noting against the wiki's other parallelism capabilities: where [[gsd-execute-phase]] and [[sp-dispatching-parallel-agents]] fan out local fresh-context subagents and runtimes like [[sandcastle]] provide worktree isolation as infrastructure, swarm's default worker is a remote cloud agent and local execution is the exception. N is stated as total workers, explicitly *not* the cloud concurrency limit.

## See Also
- [[pstack-arena]] — the sibling fan-out primitive, competitive rather than partitioned.
- [[pstack-maintain-verification-skill]] — runs a source wave of one worker per feature.
- [[pstack-principle-guard-the-context-window]] — the principle the no-raw-dumps rule enforces.
- [[gsd-execute-phase]] · [[sp-dispatching-parallel-agents]] — the cross-framework parallel-execution counterparts.
- [[mp-implement-spec]] — Matt Pocock: fans implementer subagents out across a ticket frontier and lands them on one integration branch.
