---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: ["[[pattern-worktree-isolation]]"]
equivalent_to: ["[[sp-using-git-worktrees]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-worktree

`/ce-worktree` — "Ensure work happens in an isolated git worktree with native harness detection and fallback support." An execution-infrastructure skill: it guarantees each unit of work runs in a **dedicated git worktree** so parallel and experimental work never corrupts the mainline, detecting native harness worktree support and falling back gracefully where absent.

It is the mechanism behind [[pattern-worktree-isolation]] and underpins [[ce-work]] and the autonomous [[lfg]] loop (which can run units concurrently). It implements [[stage-implement]] as an enabling capability rather than a code-writing one. Its one cross-framework counterpart is Superpowers' [[sp-using-git-worktrees]] — the two frameworks that make worktree isolation an explicit, first-class skill (Superpowers adds a harness-native-tool-first policy and a clean-baseline check); other frameworks use worktrees ad hoc.

## See Also
- [[sp-using-git-worktrees]] — the cross-framework counterpart (Superpowers' first-class worktree skill).
- [[ce-work]] · [[lfg]] — the capabilities that run inside worktree isolation.
- [[pattern-worktree-isolation]] — the technique.
- [[pattern-fresh-context-subagents]] — the context-isolation cousin (isolate context vs isolate the filesystem).
- [[stage-implement]] — the canonical stage this implements.
