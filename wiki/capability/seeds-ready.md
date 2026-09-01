---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-autonomous-loop]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd ready

`sd ready` — **open issues with no unresolved blockers.** This is the framework's dispatch primitive and the reason every other command exists: a seed is ready when it is `open` and every id in its `blockedBy` list is `closed`, so the answer is derived from the dependency graph rather than stored, and it is correct the moment a blocker closes.

It takes the same filters as [[seeds-list]] (`--type`, `--assignee`, `--label`, `--label-any`, `--unlabeled`, `--priority`, `--priority-max`, `--limit`, `--sort`, `--format`) plus two behaviours of its own:

- **`--respect-schedule`** (opt-in) reads two well-known keys out of the opaque `extensions` bag so [[warren]] can park work without losing it: `extensions.queued === true` is excluded as intentionally parked, and `extensions.scheduledFor` parsing to a future ISO-8601 timestamp is excluded as not yet due. Malformed or past values fall through as if unset, and default `sd ready` is unchanged — agents still see queued items unless they ask for the schedule-aware view.
- **Planning outranks implementation.** A parent seed whose plan is still `draft` is surfaced as planning work, and a child seed created with `requires_plan: true` is *hidden* until its sub-plan reaches `approved`. That is how the framework enforces "plan before you build" — not by instructing the agent but by refusing to hand it the work ([[seeds-plan-submit]]).

Maps to **no canonical SDLC stage** — it advances nothing; it decides what to advance next. Its [[pattern-autonomous-loop]] edge is the process-layer half of a loop the runtime closes: warren's agents self-claim from `.seeds/`, and its serial plan-run walks a plan's children one run at a time.

## See Also
- [[seeds-update]] — the claim (`--status in_progress`) an agent issues immediately after picking a ready seed, so parallel agents do not double-book.
- [[seeds-block]] · [[seeds-dep]] — what makes a seed *not* ready.
- [[warren]] — the runtime that polls this queue; [[bernstein]] — the same idea implemented as an in-process task DAG.
- [[pattern-autonomous-loop]] — the pattern this feeds.
