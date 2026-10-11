---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: "[[stage-review]]"
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-action-gating]]", "[[pattern-deterministic-gates]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: ["[[ce-code-review]]", "[[addy-code-review]]", "[[mp-code-review]]", "[[gstack-review]]", "[[sp-requesting-code-review]]", "[[bmad-code-review]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /factory-review-prs

Part of the experimental **Factory** suite of [[builder-skills]]. Reads `.agent-factory/config.yaml` ([[artifact-autonomy-policy]]) and its own optional `skill_prompts` overlay, which adds project guidance but cannot grant permission. It reviews a **filtered queue** of PRs. For one long-lived PR the Factory uses [[builder-factory-babysit-pr]] instead.

For each candidate: read live state from the configured host, excluding drafts, PRs outside the filters, and PRs that already have a current review unless policy asks for re-review. Inspect the diff, linked issues, required checks, review threads, author eligibility, and the **exact head revision**. *"Treat bot findings as leads and preserve human review direction unless source evidence disproves it."* Report actionable findings with file, line, impact, and a concrete fix. *"If none exist, record that outcome without inventing a comment."*

Review is one of four separately gated actions. The others are reply or other PR write, approve, and merge. *"Host-level mergeability, one green check, or a bot approval does not prove all gates passed. Re-read the exact head and live state immediately before an approval or merge. Restart a configured soak if the head or a gate changes."* Unavailable or partial state counts as unknown, never as clean.

In the wiki's [[stage-review]] code-review cluster, this is the only member designed for **a queue of other people's PRs on a schedule**. The others review the agent's own diff.

## See Also
- [[builder-factory-babysit-pr]] — the one-PR counterpart.
- [[ce-code-review]] · [[gstack-review]] · [[mp-code-review]] — the code-review cluster.
- [[stage-review]] — the canonical stage this implements.
