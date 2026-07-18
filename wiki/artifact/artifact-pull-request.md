---
type: artifact
sources: "Open GSD docs (2026)"
updated: 2026-07-05
---

# Artifact: Pull request

The pull request created on the remote at [[gsd-ship]]: the phase branch is pushed and a
PR opened with an auto-generated summary, optional cross-AI review triggered, and merge
tracked. Aggregates the phase's [[artifact-atomic-commit]] history. `--draft` opens it as a
draft.

## Produced by (backlinks)
- [[gsd-ship]]

- [[ce-commit-push-pr]] — Compound Engineering: working changes → open PR with adaptive description.
- [[lfg]] — the autonomous loop opens the PR as its terminal step (then watches CI to green).
- [[gstack-ship]] — gstack's Release Engineer opens the PR (bumps VERSION + CHANGELOG, filter-squashes WIP commits).

## See Also
- [[artifact-atomic-commit]] — the commits this PR bundles.
