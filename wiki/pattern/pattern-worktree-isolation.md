---
type: pattern
sources: "EveryInc/compound-engineering-plugin — /ce-worktree, /ce-work (2026); obra/superpowers — using-git-worktrees (2026)"
updated: 2026-07-17
---

# Pattern: Worktree isolation (each unit of work in its own git worktree)

Run each unit of work in a **dedicated git worktree** — a separate working directory on its own branch, sharing one repository — so parallel, experimental, and autonomous work never corrupts the mainline or collides with other in-flight units. When a unit is abandoned, its worktree is discarded with no trace on the trunk; when it succeeds, it merges cleanly.

**Two frameworks** make this a first-class, explicit skill. Compound Engineering ([[ce-worktree]]) runs [[ce-work]] and the autonomous [[lfg]] loop inside it; Superpowers ([[sp-using-git-worktrees]]) prefers the harness's *native* worktree tool, falls back to `git worktree`, and verifies a clean test baseline before any implementation begins. Other frameworks use worktrees ad hoc; these two foreground isolation as a reusable step.

## Why it's distinctive

This is the **filesystem** counterpart to [[pattern-fresh-context-subagents]] (which isolates an agent's *context*): worktree isolation isolates the *files*. It is the safety substrate that makes [[pattern-autonomous-loop]] non-destructive — an unattended agent can build, break, and retry without risking the developer's working tree — and it enables running multiple units concurrently (one product, five worktrees). Other frameworks use git worktrees ad hoc; Compound Engineering foregrounds isolation as an explicit, reusable step.

## Applied by (backlinks)

Compound Engineering:

- [[ce-worktree]] — ensures an isolated worktree exists (native detection + fallback).
- [[ce-work]] — executes the plan inside the isolated worktree.
- [[lfg]] — runs the whole autonomous loop in isolation.

Superpowers:

- [[sp-using-git-worktrees]] — detect existing isolation → prefer the harness's native worktree tool → fall back to `git worktree` (verified git-ignored) → verify a clean test baseline.
- [[sp-finishing-a-development-branch]] — the counterpart teardown: removes only the worktrees it created, per the merge/PR/keep/discard choice.

## See Also
- [[pattern-fresh-context-subagents]] — the context-isolation cousin (isolate the agent's memory vs the filesystem).
- [[pattern-autonomous-loop]] — the pattern this one makes safe.
- [[pattern-trunk-based-development]] — worktrees keep short-lived branches off a clean trunk.
- [[compound-engineering]] · [[superpowers]] — the frameworks applying this pattern.
