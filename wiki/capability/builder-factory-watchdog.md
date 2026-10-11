---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-action-gating]]", "[[pattern-autonomous-loop]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-watchdog

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. It monitors **explicitly authorized delivery handoffs** and reports stalled ones. *"A task title, branch, PR, green check, or agent summary is not authorization."*

Find candidates through the configured host and read enough user-authored history to confirm the original request and any later cancellation or scope change. Skip active work, explicit waits, finished or cancelled tasks, unclear ownership, and anything without configured delivery authorization. For stalled work, find its task-owned PR, branch, or worktree and check live state immediately before acting.

**Notify only on a verified next step.** Send a reminder only when the notification policy allows it and live evidence shows a concrete step is due, after checking task history for an identical earlier reminder. Otherwise report `DONT_NOTIFY`. *"If target or state cannot be proven, do not message."* The task owner stays responsible for merge, post-merge verification, and cleanup unless the config assigns them elsewhere.

Off-stage supervision. The explicit silent outcome (`DONT_NOTIFY`) is what keeps a scheduled monitor from generating noise.

## See Also
- [[builder-factory-recover]] — the sibling that resumes interrupted runs instead of nudging them.
- [[builder-agent-watchdog]] — the general cross-agent audit; the guide says it does not replace this.
- [[builder-factory]] — where the notify policy is set.
