---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: "[[stage-plan]]"
produces: ["[[artifact-issue]]"]
applies: ["[[pattern-scale-adaptive-planning]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd create

`sd create --title <text>` — file one tracked unit of work. Flags set `--type` (`task | bug | feature | epic`), `--priority` (0 critical … 4 backlog, default 2), `--description`, and `--assignee`; the command prints the generated id (`{project}-{4hex}`, e.g. `seeds-a1b2`) or the `{ "success": true, "command": "create", "id": … }` envelope under `--json`.

It is the **low-ceremony half of the framework's planning dial**: *"for small, well-scoped tasks just `sd create` directly"*, against [[seeds-plan-prompt]] for work *"large or ambiguous enough that an LLM benefits from decomposing it"*. Two tiers, chosen by the author of the work — a fixed, explicit instance of [[pattern-scale-adaptive-planning]] rather than a dial an agent negotiates.

A bare `create` produces an unwired seed; the dependency edges that decide whether it is *ready* come from [[seeds-dep]] and [[seeds-block]], and the labels from [[seeds-label]].

## How it differs from the decomposers

No `equivalent_to` edge is stored here, deliberately: [[mp-to-tickets]] and [[speckit-taskstoissues]] both *decompose or export a plan* into many issues, which is [[seeds-plan-submit]]'s job, not this one. `sd create` files exactly one. What it shares with them is the destination, and there seeds is the odd one out in *where* the issue lands: not on a hosted tracker but in a JSONL file inside the repo, on the same branch as the code, merged by git. That is what makes it usable by an agent with no network and no tracker credentials — and what makes the issue state a reviewable part of the diff.

## See Also
- [[seeds-plan-submit]] — the high-ceremony path; spawns these same seeds one per plan step.
- [[seeds-ready]] — where a created seed surfaces once nothing blocks it.
- [[seeds-update]] · [[seeds-close]] — its lifecycle.
- [[artifact-issue]] — what it produces.
- [[stage-plan]] — the canonical stage this implements.
