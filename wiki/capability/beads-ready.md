---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-autonomous-loop]]"]
equivalent_to: ["[[seeds-ready]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd ready

`bd ready` — **the claimable frontier of the work graph**, and the single computation the whole product is built around. The docs define it precisely: *"open beads with no open blockers, excluding anything in progress, blocked, deferred, or held by a gate. Agents never scan the whole tracker; they ask for the frontier and claim atomically."*

```bash
bd ready --json            # the claimable frontier, machine-readable
bd ready --claim --json    # atomically claim the first match
bd ready --mol <mol-id>    # which steps of one molecule can run right now
```

The frontier is **derived, never stored**, so it is correct the instant a blocker closes — *"closing `bd-a1b2` makes `bd-c3d4` ready; nothing needs re-planning."* That is the sentence that makes this a [store](../store/index.md) capability rather than an orchestration one: the graph answers "what next?" without anybody scheduling, which is exactly the split beads' charter draws when it says the orchestration layer owns *"task assignment strategy"* and beads does not.

`--claim` matters as much as the query. It sets assignee and `in_progress` in one atomic write, so two agents polling the same frontier cannot both take the same bead. Combined with content-hash IDs (no renumbering on merge), that is the entire coordination protocol between parallel agents — no lock server, no assignment queue.

Not gating the frontier is as deliberate as gating it: only `blocks` and workflow edges hold work back, while `discovered-from` and `related` record meaning without hiding anything ([[beads-dep]]).

Maps to **no canonical SDLC stage** — it advances nothing; it decides what may be advanced next.

## Cross-store equivalent

[[seeds-ready]] computes the same predicate over a JSONL file, and the convergence is the strongest signal the [store layer](../store/index.md) produces: two tools built independently for the same job both landed on *the unblocked frontier as the dispatch primitive*. They differ at the edges — beads excludes gated and deferred beads and can scope to a molecule; seeds adds `--respect-schedule` for warren's parked/scheduled keys.

## See Also
- [[beads-update]] — the claim, if not done inline with `--claim`.
- [[beads-dep]] · [[beads-gate]] — what holds a bead back from this frontier.
- [[warren]] · [[bernstein]] — the orchestration layer that consumes a frontier like this one.
- [[pattern-autonomous-loop]] — the pattern this feeds.
