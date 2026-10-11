---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-action-gating]]", "[[pattern-deterministic-gates]]", "[[pattern-evidence-before-claims]]", "[[pattern-worktree-isolation]]"]
equivalent_to: ["[[ce-resolve-pr-feedback]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-babysit-pr

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. It follows **one explicitly authorized PR** through its delivery lifecycle. *"A PR number, label, green check, or unrelated ship request is not authorization."*

Each pass has five steps. (1) **Confirm authority and ownership**: exact host, repository, PR, the original user authorization, allowed paths and risk, and a task-owned worktree, stopping before any write if something is missing or stale. (2) **Read a complete live snapshot**: base and head, open/draft/merged state, all required checks, reviews, unresolved threads, and mergeability. *"Partial or unavailable data is unknown, not clean."* (3) **Disposition feedback**: fix only actionable findings within the authorized limits, and *"avoid speculative cleanup and larger redesigns."* (4) **Verify and re-read**: after every push, fetch the live PR again and tie all evidence to the new head. (5) **Apply action gates separately.**

The action-gate table has six rows: Fix, Publish (*"never force-push or overwrite a concurrent update"*), Reply, Approve, Merge (*only if the host can condition the merge on the checked head*), and **Soak**. For the soak, the agent must *"prove the exact head and required gates stayed unchanged for the full configured interval. Missing history does not satisfy it."* It stays host-neutral: *"Do not assume GitHub, a specific CLI, or identical conditional-merge support across hosts."*

Filed under [[stage-release]] next to [[ce-resolve-pr-feedback]], the other capability that resolves pre-merge feedback. This one runs over many passes and carries its own merge authority. pstack's page mentions Cursor's built-in `/babysit` with the same name and purpose.

## See Also
- [[builder-factory-review-prs]] — the queue-sweep counterpart.
- [[builder-factory-watchdog]] — the stalled-work monitor; does not replace this.
- [[ce-resolve-pr-feedback]] — the pre-merge feedback resolver.
- [[stage-release]] — the canonical stage this implements.
