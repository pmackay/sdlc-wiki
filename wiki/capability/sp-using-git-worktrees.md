---
type: capability
subtype: skill
belongs_to: "[[superpowers]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-worktree-isolation]]"]
equivalent_to: ["[[ce-worktree]]"]
sources: "Superpowers v6.1.1 (2026)"
raw: ["../../raw/superpowers/2026-07-17-superpowers.md"]
updated: 2026-07-17
---

# using-git-worktrees

An execution-infrastructure skill: ensure work happens in an **isolated workspace** before implementing a plan ([[pattern-worktree-isolation]]). *"Detect existing isolation first. Then use native tools. Then fall back to git. Never fight the harness."*

The decision order is its whole point: **Step 0** detects whether the agent is *already* in a linked worktree (`git-dir ≠ git-common-dir`, with a submodule guard) and skips creation if so; **Step 1a** prefers the harness's **native** worktree tool (e.g. `EnterWorktree`) — using `git worktree add` when a native tool exists is called out as *"the #1 mistake"* because it creates phantom state the harness can't manage; **Step 1b** falls back to a manual `git worktree` under `.worktrees/` (verified git-ignored first), with a sandbox fallback to working in place. It then runs project setup (auto-detected: npm/cargo/pip/poetry/go) and **verifies a clean test baseline** before reporting ready — so a failing baseline can't later be mistaken for a new bug.

It is the direct counterpart to [[ce-worktree]] — both make worktree isolation a **first-class, explicit skill** rather than something done ad hoc, and both underpin their framework's autonomous/ parallel execution. Superpowers' version adds the harness-native-tool-first policy (portability across its many supported agents). Together they make [[pattern-worktree-isolation]] a two-framework pattern.

## See Also
- [[ce-worktree]] — the counterpart; the other framework that treats worktree isolation as a first-class skill.
- [[sp-executing-plans]] · [[sp-subagent-driven-development]] — the executors that run inside the isolated workspace.
- [[sp-finishing-a-development-branch]] — cleans up the worktree this skill created.
- [[pattern-worktree-isolation]] — the technique; [[pattern-fresh-context-subagents]] — the context-isolation cousin.
- [[stage-implement]] — the canonical stage this implements (as enabling infrastructure).
