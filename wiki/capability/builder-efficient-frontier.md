---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-model-tiering]]", "[[pattern-fresh-context-subagents]]", "[[pattern-wave-parallelism]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: ["[[builder-efficient-fable]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /efficient-frontier

The same orchestration as [[builder-efficient-fable]] for **any high-cost frontier model**: *"Use the expensive frontier model where its marginal judgment matters. Push repeatable, bounded, or token-heavy work to cheaper/faster subagents."*

Frontier-only decisions are architecture, prioritization, ambiguity resolution, risk, synthesis, and final review. Delegable work is research scans, repository inventory, docs extraction, browser and testing passes, log reduction, test-failure clustering, narrow coding, and mechanical edits. Useful stop conditions for delegates: the live code does not match the handoff's assumption; a verification command fails twice; the work needs files outside the assigned scope; the agent cannot produce concrete evidence for its claim.

Its guardrails are the rules most often broken in practice: *"Do not delegate the immediate blocker if your next step depends on it. Do not ask multiple agents to edit the same files at the same time… Do not claim universal savings."*

Off-stage. It is the general form of [[pattern-model-tiering]].

## See Also
- [[builder-efficient-fable]] — the Fable-specific original.
- [[pstack-setup-pstack]] — mapping roles to models as configuration instead of as an orchestration habit.
- [[pattern-model-tiering]] — the pattern.
