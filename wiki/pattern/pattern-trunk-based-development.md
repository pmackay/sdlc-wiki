---
type: pattern
sources: "Addy Osmani — Agent Skills (2026); obra/superpowers (2026)"
updated: 2026-07-17
---

# Pattern: Trunk-based development

Integrate into a single shared trunk continuously via short-lived branches and small, atomic
commits (~100 lines of change), keeping the trunk always releasable. Each commit is a
save-point that can be reverted cleanly; unfinished work hides behind [[pattern-feature-flags]]
rather than long-lived branches. Small changes are faster to review and safer to ship, which
is the same "faster is safer" logic behind [[pattern-shift-left]].

## Applied by (backlinks)

Addy Osmani — Agent Skills:

- [[addy-git-workflow]] — trunk-based development, atomic commits, commit-as-save-point.
- [[addy-ci-cd]] — pipelines that keep the trunk green.

Compound Engineering:

- [[ce-commit]] — convention-aware atomic commits; [[ce-commit-push-pr]] — short-lived branch → PR.

gstack:

- [[gstack-ship]] — atomic commits, short branches, PR flow; filter-squashes WIP checkpoint commits so bisect stays clean.

Superpowers:

- [[sp-finishing-a-development-branch]] — short-lived feature branch → merge-or-PR decision menu, with per-choice worktree cleanup keeping the trunk clean.

## See Also
- [[pattern-feature-flags]] — how in-progress work stays on trunk without shipping.
- [[artifact-atomic-commit]] — the unit of integration.
- [[stage-release]] — the stage this pattern serves.
