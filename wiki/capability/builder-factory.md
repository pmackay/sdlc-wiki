---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: ["[[builder-factory-collect]]", "[[builder-factory-lookback]]", "[[builder-factory-human-digest]]", "[[builder-factory-review-prs]]", "[[builder-factory-babysit-pr]]", "[[builder-factory-ship]]", "[[builder-factory-watchdog]]", "[[builder-factory-recover]]"]
produces: ["[[artifact-autonomy-policy]]"]
applies: ["[[pattern-action-gating]]", "[[pattern-evidence-before-claims]]", "[[pattern-autonomous-loop]]", "[[pattern-worktree-isolation]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory

The Factory's configuration and coordination skill. *"Configure the current project to turn selected product or maintenance signals into verified, reviewed changes. Factory coordinates the other modules; it does not assume a provider, repository, schedule, or autonomy level."* It writes the project's [[artifact-autonomy-policy]] and, if asked, the host automations that run the other eight modules.

The setup is seven steps. (1) Read the existing config and preserve explicit choices. (2) Show the read-capable integrations **this host** exposes, since *"there is no built-in Factory source catalog"*. (3) Set each action policy independently: implement, reply, close, review, approve, publish, merge, deploy, recover, notify. (4) Add optional per-skill prompt overlays. (5) Choose schedules, time zone, worktree ownership, runtime, and notifications only where the host supports them. (6) Write the config, never putting credentials in it. (7) Create one job per enabled workflow, then **read back** its saved schedule, target, runtime, and notification settings and report whatever the host could not honour.

The safe defaults are the core of the design. Replies, issue closure, approvals, merges, production deploys, and recovery all stay disabled unless their own policy says otherwise. Criteria-based actions must list both the conditions that allow the action and the conditions that require a human. *"Missing or unclear policy means hold. Permission to fix does not authorize publication or another external action."* The skill's closing rule, *"Never claim that a schedule, integration, merge, or deployment exists without reading back its live state"*, applies [[pattern-evidence-before-claims]] to the factory's own setup.

The skill performs no lifecycle stage. It sets policy for the modules that do, so `implements:` is empty. It is the wiki's clearest example of [[pattern-action-gating]] expressed as configuration.

## See Also
- [[builder-skills]] — the framework and the full workflow diagram.
- [[artifact-autonomy-policy]] — the document this writes.
- [[pattern-action-gating]] — the pattern the policy model instantiates.
- [[topic-software-factory]] — the prompt-owned control-plane pole this skill defines.
