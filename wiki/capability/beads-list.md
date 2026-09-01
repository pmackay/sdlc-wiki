---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: ["[[seeds-list]]"]
sources: "gastownhall/beads — README + docs/core-concepts + docs/CLI_REFERENCE.md (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd list

`bd list` — the filtered listing (status, type, assignee, label, priority, `--stale`, `--mol`, limits and sorts), with `--json` for agents. Four narrow siblings live here because each is one canned filter over the same data:

- **`bd count`** — the same query, answered as a number.
- **`bd blocked`** — everything held up; the complement of [[beads-ready]] and the first place to look when the frontier is empty but work remains open.
- **`bd stale`** — beads not updated recently, the queue-rot detector.
- **`bd orphans`** — **the interesting one**: beads *referenced in a git commit message but still open*. Beads' commit convention puts the id in parentheses (`git commit -m "Fix auth validation bug (bd-abc)"`), so the store can cross-reference open beads against git history and find work that shipped but was never closed. A consistency check between the tracker and the repository, which only a store living inside the repo can perform.

The `--stale` example is also the wiki's neatest illustration of beads' own CLI-design rule: *"Prefer flags on existing commands… `bd list --stale` instead of `bd stale`"* — a discipline it states and then only partly follows, since both exist.

Maps to **no canonical SDLC stage**. Its [[pattern-context-engineering]] edge is the `--json`/limit/filter surface: with a ~109-command tracker, what an agent pulls into context is a budget decision, and every read command is built to be narrowed.

## See Also
- [[beads-ready]] — the actionable subset.
- [[beads-query]] — the expressive alternative when filters are not enough.
- [[beads-doctor]] — where `orphans`-style consistency checks are consolidated with `--fix`.
