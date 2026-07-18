---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-trunk-based-development]]"]
equivalent_to: ["[[gsd-ship]]", "[[addy-shipping]]", "[[ce-commit-push-pr]]", "[[gstack-ship]]", "[[openspec-archive]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# finishing-a-development-branch

The close-out step: once implementation is complete, decide how to integrate the work. *"Verify tests → detect environment → present options → execute choice → clean up."*

The flow is deliberately structured to avoid open-ended "what next?" prompts: **verify tests pass** first (stop if not) → **detect the workspace** (normal repo / named-branch worktree / detached HEAD) → determine the base branch → present **exactly four options** — (1) merge locally, (2) push and open a PR → [[artifact-pull-request]], (3) keep the branch as-is, (4) discard (requires a typed "discard" confirmation) → execute, then clean up the worktree **only** for merge/discard (a PR keeps it alive for iteration). A quick-reference table and a Common-Mistakes list encode the git ordering hazards (merge before removing the worktree; `cd` to main root before `git worktree remove`; only clean up worktrees you created). [[pattern-trunk-based-development]].

It is the finalize/close-out cluster's Superpowers member — [[gsd-ship]] ↔ [[addy-shipping]] ↔ [[ce-commit-push-pr]] ↔ [[gstack-ship]] ↔ [[openspec-archive]] — each closing an iteration but finalizing different things. Superpowers' distinctive flavor is the **decision menu itself**: it doesn't assume ship-to-prod, it *asks* (merge vs PR vs keep vs discard) and handles worktree cleanup per choice. Like GSD/OpenSpec it stops at PR/merge — **no deploy step**.

## See Also
- [[sp-subagent-driven-development]] · [[sp-executing-plans]] — the executors that hand off to this close-out.
- [[sp-using-git-worktrees]] — created the worktree this skill tears down.
- [[gsd-ship]] · [[addy-shipping]] · [[ce-commit-push-pr]] · [[gstack-ship]] · [[openspec-archive]] — the finalize/close-out cluster.
- [[artifact-pull-request]] — produced by the PR option; [[pattern-trunk-based-development]] — the technique.
- [[stage-release]] — the canonical stage this implements.
