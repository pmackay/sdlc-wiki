---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-learn]]"
delegates_to: []
produces: ["[[artifact-retrospective]]", "[[artifact-pull-request]]"]
applies: ["[[pattern-systematic-debugging]]", "[[pattern-knowledge-compounding]]", "[[pattern-evidence-before-claims]]", "[[pattern-action-gating]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-lookback

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. Its purpose is *"to find patterns that normal item-by-item flows keep missing or fixing only temporarily."*

**Build a bounded evidence set.** Enumerate the full configured window and an optional comparison baseline across feedback, telemetry, runtime errors, recurring CI or review failures, repeated recovery attempts, replies to earlier information requests, and prior fixes marked shipped. Cluster records *"by underlying symptom and affected boundary, not wording alone."* Keep event counts, affected users, versions, and distinct source links separate.

**Find the systemic cause.** Trace representative reports back to their source and to prior dispositions, commits, tests, and release evidence. Check whether the symptom *"recurred after a claimed fix, appeared through a sibling caller, or escaped because the normal workflow lacked a signal, owner, verification step, or recovery path."* Reproduce a current case where possible. *"Prefer one verified correction at that boundary over a pile of caller-specific patches."* Separate confirmed causes from hypotheses, and state what evidence would disprove each hypothesis. This is [[pattern-systematic-debugging]] applied to a population of reports instead of to one bug.

**Change and verify.** `workflows.lookback.implement` decides between recommending only, preparing a fix, and publishing. The guide recommends keeping this manual until its queries and fix criteria are proven. *"A recurring pattern is evidence for investigation, not automatic permission to edit code."* After a fix, inspect the same signals again: *"A test, merge, or 'fixed' label alone does not prove that the live recurrence stopped."*

Filed under [[stage-learn]] as a **third flavor** of that stage. The other two fold lessons into an agent corpus or a team retrospective; this one learns from the product's own recurrence signal and writes the lesson back as a structural fix. It has no `equivalent_to:`. [[ce-product-pulse]] also reports post-release signal but does not look for causes.

## See Also
- [[builder-factory-collect]] — current intake; lookback reads its follow-up threads.
- [[ce-product-pulse]] · [[gstack-retro]] — the nearest production-signal report and team retrospective.
- [[stage-learn]] — the canonical stage this implements.
