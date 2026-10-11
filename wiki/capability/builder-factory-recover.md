---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-idempotent-operations]]", "[[pattern-session-handoff]]", "[[pattern-action-gating]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-recover

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. It finds and resumes interrupted coding runs, typically after a host restart or an interrupted automation. *"Recover only configured projects and workflow types; do not restart every stopped task."*

For each candidate run: read the original user request and later messages, *"not only the title or summary."* Skip work that is active, cancelled, intentionally paused, blocked on a person, complete, ambiguous, or out of scope. Confirm the worktree still belongs to the run, and *"never reset, clean, stash, or attach another task's branch."* **Recheck external state before retrying an uncertain action**, and *"do not repeat completed writes, replies, approvals, merges, or deployments."* If the original authorization does not cover the next step, leave the run stopped and state the decision needed.

This is [[pattern-idempotent-operations]] from the other side. The Factory cannot assume its own steps are safe to re-run, so recovery checks for each write whether it already happened. The prompt overlay *"cannot restore canceled work or grant new authorization."* Off-stage, and the counterpart of the session-resumption capabilities ([[pstack-recall]], [[gstack-context-restore]]) for unattended runs.

## See Also
- [[builder-factory-watchdog]] — the stalled-work notifier.
- [[pattern-idempotent-operations]] · [[pattern-session-handoff]] — the patterns this depends on.
- [[pstack-recall]] — resumption for an interactive session.
