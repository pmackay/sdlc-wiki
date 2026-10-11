---
type: capability
subtype: skill
belongs_to: "[[matt-pocock-skills]]"
implements: "[[stage-implement]]"
delegates_to: ["[[mp-tdd]]", "[[mp-code-review]]"]
produces: ["[[artifact-atomic-commit]]", "[[artifact-pull-request]]"]
applies: ["[[pattern-wave-parallelism]]", "[[pattern-worktree-isolation]]", "[[pattern-fresh-context-subagents]]", "[[pattern-test-driven-development]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[gsd-execute-phase]]", "[[sp-subagent-driven-development]]", "[[pstack-swarm]]"]
docs_url: "https://www.aihero.dev/skills-implement-spec"
sources: "Matt Pocock — Skills for Real Engineers v1.3.1 (2026-10-04)"
raw: ["../../raw/matt-pocock-skills/2026-10-04-skills-v1.3.1-update.md"]
updated: 2026-10-11
---

# implement-spec

`/implement-spec` — a user-invoked engineering skill that **implements a whole spec in one run**: "Implement the result of /to-spec and /to-tickets in code." It is the parallel alternative to running [[mp-implement]] once per ticket.

It is the toolkit's orchestrated execute path; the sequential one is one [[mp-implement]] per ticket, `/clear`ing context between each. Per [[mp-ask-matt]]: reach for it "when you'd rather orchestrate the build than drive each ticket yourself."

## How it works

The tickets from [[mp-to-tickets]] are read "not [as] a list of steps" but as a **task graph** with blocking relationships, "so there is always a **frontier** of tickets which are ready to be grabbed." That is the same leading word [[mp-grilling]] uses for its question rounds.

1. Read the spec and tickets to understand the task graph.
2. *(optional)* An **exploration subagent** does the codebase/docs exploration up front and saves Markdown notes **outside the repo** where every later subagent can reach them, "so implementer subagents focus on implementation rather than exploration."
3. Create one **integration branch**. A draft PR opens only if the issue tracker closes work through PRs or the user asks, and only after the first merge, since "a branch with no commits ahead of main can't open one" → [[artifact-pull-request]].
4. **Implementer subagents** each take one ticket in **their own worktree on their own branch** ([[pattern-worktree-isolation]]). Each confirms its worktree is based on the integration branch, builds the ticket by calling [[mp-tdd]], and merges the integration tip into its own branch before reporting done, so every merge is a fast-forward.
5. A **merger subagent** lands each finished branch on the integration branch.
6. When a merge opens new tickets on the frontier, more implementers launch: "maximum concurrency" ([[pattern-wave-parallelism]]).
7. Once every ticket is done, one [[mp-code-review]] runs over the whole integration branch, and a single implementer fixes everything it raises.
8. Mark the draft PR ready, or close each ticket the way the tracker closes work, and report the branch.
9. Clean up the worktrees.

Communication with subagents is "sparse", carried by **context pointers** (to the spec, tickets, research notes, previous commits) rather than restated content ([[pattern-context-engineering]]; the term is defined in [[mp-writing-for-agents]]).

## Where it sits in the cluster

It joins the **parallel-execute** sub-cluster of [[stage-implement]]. Like [[gsd-execute-phase]], it fans independent work out across fresh-context workers. Like [[sp-subagent-driven-development]], it runs one implementer subagent per unit with a review at the end. Like [[pstack-swarm]], it drains parallel workers into one result. The thing it does differently is the **ready frontier**: it works off the tracker's blocking edges instead of pre-computed waves, so new work starts as soon as a merge unblocks it, not when a whole wave finishes.

## See Also
- [[mp-implement]] — the sequential, per-ticket sibling; `/implement` runs tdd + code-review per ticket, `/implement-spec` runs one code-review over the integration branch.
- [[mp-to-tickets]] — produces the task graph (tickets with blocking edges) this walks.
- [[mp-tdd]] · [[mp-code-review]] — the skills each implementer and the close-out call.
- [[sandcastle]] — Matt Pocock's own runtime library for the same shape (sandboxed agents on branches, merged back) one layer down.
- [[gsd-execute-phase]] · [[sp-subagent-driven-development]] · [[pstack-swarm]] — parallel-execute counterparts.
- [[stage-implement]] — the canonical stage this implements.

## Version history

- **Added in v1.3.0 (2026-10-04)**, graduated from `in-progress/` into `engineering/`. Before this, the only execute path was the sequential one: one [[mp-implement]] per ticket. Ahead of graduating, the goal became the integration branch rather than a PR, it points at the configured issue tracker instead of defaulting to `gh`, and each implementer confirms its worktree base, builds with [[mp-tdd]], and merges the integration tip before reporting done.
