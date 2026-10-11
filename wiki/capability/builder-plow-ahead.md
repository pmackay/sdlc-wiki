---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: ["[[artifact-decision-log]]", "[[artifact-handoff-doc]]"]
applies: ["[[pattern-autonomous-loop]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: ["[[pstack-principle-never-block-on-the-human]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /plow-ahead

An **explicit autonomy contract** that the user switches on with phrases like *"plow ahead"*, *"do not stop"*, or *"finish while I am away"*. The agent turns routine questions into stated assumptions, picks the smallest reversible option, keeps working through ordinary test failures and ambiguity, and *"do[es] not pause merely to ask which reasonable option the user prefers. Pick one, record why, and keep going."*

**Stop conditions are listed** instead of left to judgment: missing credentials, paid services, or private data; destructive, irreversible, or production-mutating steps; branch operations, history rewrites, force pushes, or deletions the user did not ask for; high legal, safety, privacy, or security risk; decisions the user reserved; and a verification failure that repeats after reasonable investigation, where the next fix would be speculative. When it stops, it leaves a self-contained handoff.

**Decision rules** for choosing without the user: reuse existing patterns, prefer local and low-blast-radius changes, keep scope tight, pick correctness over cleverness, validate small first, and, when options are close, *"choose the one that is easier for the user or a reviewer to understand later."* It keeps a lightweight decision log and ends with a recap under Goal, **Key decisions**, Changes, Validation, and Remaining risk. The recap is written for a human who was not watching, which is exactly the reader [[artifact-decision-log]] was minted for.

Off-stage: this sets how much autonomy the agent has without performing a lifecycle step. `equivalent_to:` [[pstack-principle-never-block-on-the-human]] (proceed on reversible work, pause for irreversible writes).

## See Also
- [[pstack-principle-never-block-on-the-human]] · [[pstack-show-me-your-work]] — the same contract and its audit trail in pstack.
- [[pattern-autonomous-loop]] — the pattern this enters.
- [[builder-quick-recap]] — the one-line status signal that ends the recap.
