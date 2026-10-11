---
type: artifact
sources: "EveryInc/compound-engineering-plugin — skills/ce-explain (2026); pstack v0.15.2 — Lauren Tan (2026); Builder.io — BuilderIO/skills (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-09-26
---

# Artifact: explainer

A **dense visual explainer** produced by [[ce-explain]] — a human-facing document (often HTML/Markdown with diagrams) that explains a concept, a diff, or a chunk of recent work, with optional verification of its claims against the code.

It is the **human-facing** counterpart to the agent-facing [[artifact-solution-doc]]: both are outputs of [[stage-learn]] realizing [[pattern-knowledge-compounding]], but the explainer builds *the developer's (and team's) understanding* rather than seeding future agents' grounding. It is adjacent to MP's [[artifact-handoff-doc]] (compact knowledge for a future reader), but an explainer teaches a topic rather than continuing a session.

## Produced by (backlinks)
- [[ce-explain]] — turns concepts/diffs/recent work into the explainer.
- [[ce-work-recap-scout]] — gathers the recent-work evidence the explainer is built from.

pstack — three skills produce one, at three depths:

- [[pstack-how]] — Overview / Key Concepts / How It Works / Where Things Live / Gotchas, pitched at a senior engineer onboarding onto a subsystem.
- [[pstack-why]] — a cited read on decisions and tradeoffs across seven organizational evidence sources, under an explicit epistemics contract whose hedges are **findings, not style**.
- [[pstack-teach]] — the human-facing weave of both, built up **diagram by diagram** with each figure redrawing the last and adding one part. The counterpart to [[ce-explain]].

builder-skills:

- [[builder-visual-recap]] — an interactive recap of a diff (data-model, API, file-tree, and diagram blocks) so a reviewer sees the change's overall shape before the raw lines.

## See Also
- [[artifact-solution-doc]] — the agent-facing learning sibling ([[ce-compound]]).
- [[artifact-handoff-doc]] — compact-for-a-future-reader relative (MP).
- [[pattern-knowledge-compounding]] — the technique; [[stage-learn]] — the stage this supports.
