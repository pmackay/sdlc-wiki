---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-evidence-before-claims]]", "[[pattern-action-gating]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-human-digest

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. Experimental even within the Factory.

A **read-only decision queue**: every configured item the agent-handled flows did not resolve and a person still has to decide on. By default it covers all configured categories for the last 7 days at *balanced* detail. It can be narrowed in plain language (*"PRs only, last 30 days, detailed"*), but a filter *"cannot expand the repositories, source scopes, or tools in the project config."*

It includes PRs waiting for human review, approval, a merge decision, or product judgment; issues, feedback, or errors held for missing context, unclear intent, risk, or conflicting evidence; new answers to information requests that have not been re-triaged; and recurring incidents or delivery work that stopped with no safe authorized next step. It excludes items with a verified terminal outcome unless they reopened. *"A label or agent summary alone does not prove an item is resolved."*

Related items are grouped *"by the underlying user impact or failure pattern, not by similar words alone"*, with every source link kept and report volume separated from the number of affected people. Output is at one of three levels: brief, balanced, or detailed.

**It never acts.** *"Do not reply, approve, merge, assign, close, change status, or notify people from the digest."* Any decision is routed back through the module that owns that action and its separate policy. This is the factory anatomy's *escalation* path built as a capability. Off-stage: it tracks decisions that belong to other stages without advancing any of them.

## See Also
- [[beads]] — `bd human`, the store-layer version of a human-needed queue.
- [[topic-software-factory]] — *escalation* in the glossary; the human socket in the anatomy diagram.
- [[builder-factory]] — the policy that decides what gets held.
