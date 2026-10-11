---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-action-gating]]", "[[pattern-evidence-before-claims]]", "[[pattern-autonomous-loop]]"]
equivalent_to: ["[[pstack-benny-triage]]", "[[mp-triage]]", "[[ce-sweep]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-collect

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. It collects only the sources named by `workflows.collect.sources`.

**Collect and verify coverage.** Resolve each source ID to the connected read tool and exact scope. Follow pagination to the end and record filters, range, cursor/page coverage, and source counts. *"Keep `empty`, `unavailable`, and `truncated` distinct. A missing connector, partial page, or failed query is not an empty source."* For telemetry, report the metric and aggregation window, and distinguish event counts from unique users unless the source has a reliable identity definition.

**Triage and act.** Classify each item as a verified defect, repeated symptom, feature request, subjective feedback, duplicate, out of scope, or needing more evidence. Group related reports while keeping each source record and reporter. Implement only when `workflows.collect.implement` allows it, and verify with the configured checks plus a representative reproduction. Reply, close, and everything downstream have separate gates. *"Publish, approve, merge, or deploy: requires its own workflow authorization; collection does not grant it."*

**The follow-up loop.** When one missing detail blocks triage and the reply policy allows it, ask **one targeted question**. If replies are disabled, put the question in the report for a person to send. Later runs check for an answer, re-triage the original report with it, and apply the fix rules again. *"Receiving an answer does not itself authorize a fix or external action."*

This is the intake flavor of [[stage-align]], the same slot as [[pstack-benny-triage]], [[mp-triage]], and [[ce-sweep]]. The inputs are production feedback, telemetry, and errors rather than a developer's prompt, and it runs as a scheduled workflow with nobody watching.

## See Also
- [[builder-factory-lookback]] — the cross-time complement; collect handles current items, lookback handles recurrence.
- [[builder-factory-human-digest]] — where held items surface for a person.
- [[pstack-benny-triage]] · [[ce-sweep]] · [[mp-triage]] — the other intake capabilities.
- [[stage-align]] — the canonical stage this implements.
