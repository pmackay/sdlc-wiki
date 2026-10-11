---
type: artifact
sources: "Open GSD docs (2026); pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
updated: 2026-10-11
---

# Artifact: Pull request

The pull request created on the remote at [[gsd-ship]]: the phase branch is pushed and a PR opened with an auto-generated summary, optional cross-AI review triggered, and merge tracked. Aggregates the phase's [[artifact-atomic-commit]] history. `--draft` opens it as a draft.

## Produced by (backlinks)
- [[gsd-ship]]

- [[ce-commit-push-pr]] — Compound Engineering: working changes → open PR with adaptive description.
- [[lfg]] — the autonomous loop opens the PR as its terminal step (then watches CI to green).
- [[mp-pr]] — Matt Pocock: model-invoked PR-body template (smallest-visual Summary, before/after Evidence, one-/two-way-door Merge Danger); body only, no push/merge (v1.3.0).
- [[mp-implement-spec]] — Matt Pocock: opens a draft PR on the integration branch after the first merge, only when the tracker closes work through PRs or the user asks.
- [[gstack-ship]] — gstack's Release Engineer opens the PR (bumps VERSION + CHANGELOG, filter-squashes WIP commits).

pstack:

- [[pstack-poteto-mode]] — the *Opening a PR* playbook, invoked at the end of every other playbook: small ordered commits, a conventional-commits title, and a briefing-style body. Its *Shipping* playbook lands only the contiguous verified run from the root, bottom-up.
- [[pstack-benny-reproduce-and-fix]] — a **bounded draft** PR opened unattended, only after before-and-after proof through the real UI.
- [[pstack-maintain-verification-skill]] — at most one PR per run, carrying only proven corrections.

builder-skills (every PR write separately gated):

- [[builder-factory-collect]] — a fix for a verified defect, only when `workflows.collect.implement` allows it.
- [[builder-factory-ship]] — open or update only when publishing is enabled, with configured title, body, draft status, and labels, and no tagging unless enabled.
- [[builder-factory-babysit-pr]] — pushes in-scope fixes to one authorized PR; never force-pushes or overwrites a concurrent update.
- [[builder-factory-lookback]] — the systemic fix, when lookback implementation is enabled (manual by default).

## See Also
- [[artifact-atomic-commit]] — the commits this PR bundles.
