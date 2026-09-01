---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-autonomous-loop]]"]
equivalent_to: []
sources: "gastownhall/beads — docs/workflows + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd gate

`bd gate create|list|show|check|resolve|add-waiter|discover` — **async coordination expressed as work items**, and the sharpest single idea on this page.

Some steps cannot proceed on code alone: *"a release needs CI to go green, a deploy needs a human sign-off, a cleanup should wait 24 hours."* A gate is **a bead representing that wait**. It blocks its waiters through an ordinary dependency edge, so the waiting step simply leaves the [[beads-ready|ready frontier]] until the gate closes — *"so agents never need to poll or spin."*

| Gate type | Waits for | Closed by |
|---|---|---|
| `human` | a person's decision | `bd gate resolve` only |
| `timer` | a duration (Go syntax: `30m`, `24h` — no `d` unit) | `bd gate check` once elapsed |
| `gh:run` | a GitHub Actions run to succeed | `bd gate check` (via `gh run view`) |
| `gh:pr` | a pull request to merge | `bd gate check` (via `gh pr view`) |
| `bead` | a bead in another rig to close | manual resolve — multi-rig routing was removed |

`bd gate check` evaluates open timer and GitHub gates against the real world and closes the satisfied ones (`--dry-run` reports without closing); `bd gate discover` resolves the `await_id` for `gh:run` gates. Formula steps declare gates inline with a `[steps.gate]` block, so a release pipeline's CI wait is part of the template ([[beads-formula]]).

**Why this belongs to the state layer.** A passive store has no way to make an agent wait — but it does not need one, because it controls what the agent is *offered*. Encoding the wait as a blocker means the store coordinates without scheduling: no daemon, no polling loop, no orchestration policy. That is beads' charter drawn with a single mechanism, and it is the wiki's first instance of **synchronization primitives as work items**. Its sibling [[beads-merge-slot]] applies the identical trick to mutual exclusion.

Compare the alternatives elsewhere: [[warren]] gates a plan-run's next child on the previous PR merging (the runtime holds the loop open), and [[lfg]] watches CI until green (the agent burns turns polling). Beads makes the wait a graph property, and the cost is a `bd gate check` someone has to run.

Maps to **no canonical SDLC stage** — it suspends work rather than performing any.

## See Also
- [[beads-merge-slot]] — mutual exclusion by the same mechanism.
- [[beads-mol]] — `bd mol ready` finds molecules ready for gate-resume dispatch.
- [[beads-human]] — the human-decision channel a `human` gate waits on.
- [[pattern-autonomous-loop]] — an unattended loop can park indefinitely without spinning.
