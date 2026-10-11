---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-action-gating]]", "[[pattern-evidence-before-claims]]", "[[pattern-deterministic-gates]]", "[[pattern-worktree-isolation]]"]
equivalent_to: ["[[gsd-ship]]", "[[ce-commit-push-pr]]", "[[gstack-ship]]", "[[addy-shipping]]", "[[sp-finishing-a-development-branch]]", "[[openspec-archive]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-ship

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. It publishes and completes delivery work. *"Editing code does not by itself authorize a PR update, approval, merge, or deployment."*

Six delivery steps. (1) **Confirm ownership** of the repository, task-owned worktree, branch, and complete change set, preserving unrelated changes and *"never take over a peer's checkout."* (2) **Verify** with the configured formatter, tests, and release checks, and report any that were skipped. (3) **Publish when enabled**, using the configured title, body, draft status, and labels, and tag nobody unless that is enabled. (4) **Resolve feedback** in one coherent update and rerun the affected checks. (5) **Apply merge gates** on the unchanged live head, using a head-match guard where the host supports one. (6) **Verify and close out**: confirm the merge landed in the base branch, then verify the deployment only if configured, *because "a merge is not live proof."* Close issues, rotate worktrees, and notify only at their configured proof points.

Its stop condition is that *"an inconclusive result"* is never turned *"into success."*

A member of the [[stage-release]] finalize cluster. It stands out for **treating deploy verification as a separate proof point from merge** and for leaving every sub-step off by default. Among frameworks, only [[gstack-land-and-deploy]] ships a separate deploy command.

## See Also
- [[builder-factory-babysit-pr]] — the per-PR follow-through that often precedes this.
- [[gsd-ship]] · [[ce-commit-push-pr]] · [[gstack-ship]] — the finalize cluster.
- [[stage-release]] — the canonical stage this implements.
