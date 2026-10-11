---
type: capability
subtype: skill
belongs_to: "[[pstack]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-worktree-isolation]]"]
equivalent_to: []
sources: "pstack v0.15.2 — Lauren Tan (2026)"
raw: ["../../raw/pstack/2026-09-11-pstack-plugin.md"]
updated: 2026-09-11
---

# principle-separate-before-serializing-shared-state

**Architecture principle.** Eliminate the sharing first; serialize structurally only when one shared writer is a real invariant.

Applies when concurrent actors might write to the same file, branch, key, or state object. This is the principle that makes pstack's parallelism safe rather than merely fast, and it is cited by name wherever the framework fans out: [[pstack-arena]] gives each candidate its own worktree or output path, [[pstack-swarm]] gives each worker its own writable output, and [[pstack-figure-it-out]] parallelizes only across seams.

## See Also
- [[pstack-poteto-mode]] — indexes this principle inline and reads the index at task start.
- [[pstack]] — the twenty-three-principle set this belongs to.
