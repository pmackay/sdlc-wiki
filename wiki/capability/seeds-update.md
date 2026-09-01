---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd update

`sd update <id>` — mutate an existing issue in place: `--status`, `--title`, `--priority`, `--assignee`, `--description`, `--extensions`, `--clear-extensions`.

Its load-bearing use is the **claim**. The framework's own agent workflow puts `sd update <id> --status in_progress` immediately after `sd ready` *"before you start, so parallel agents don't double-book"* — the whole coordination protocol between concurrent agents is this one state transition plus git's union merge, with no lock server and no assignment queue. Status is reopenable (`--status open` walks a closed seed back), so the lifecycle is a cycle rather than a funnel.

`--extensions` takes a JSON object and **shallow-merges** it into the issue's opaque `extensions` bag, one level deep; `--clear-extensions` drops the field entirely. Seeds validates nothing inside it beyond "must be a plain object" — consumers namespace their keys (`warren_role`, `warren_scheduledFor`, `warren_lastRunId`) and keep them flat, because a nested patch overwrites the whole sub-object. Two branches updating `extensions` on the same issue collapse via the usual `merge=union` + dedup-on-read, last occurrence winning.

Maps to **no canonical SDLC stage** — recording that implementation is in progress is not implementing.

## See Also
- [[seeds-ready]] — supplies the id to claim.
- [[seeds-close]] — the terminal transition.
- [[warren]] — the runtime that writes scheduling state into `extensions`.
- [[seeds-doctor]] — flags non-object `extensions` values and drops them under `--fix`.
