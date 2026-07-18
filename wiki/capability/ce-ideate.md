---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-align]]"
delegates_to: ["[[ce-issue-intelligence-analyst]]", "[[ce-learnings-researcher]]", "[[ce-web-researcher]]"]
produces: []
applies: ["[[pattern-source-grounding]]", "[[pattern-adversarial-review]]", "[[pattern-context-engineering]]"]
equivalent_to: ["[[bmad-brainstorming]]", "[[addy-idea-refine]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-ideate

`/ce-ideate` — "Discover strong, qualified directions worth exploring with conceptual frames
and adversarial filtering." It diverges into candidate directions using conceptual frames, then
**adversarially filters** them ([[pattern-adversarial-review]]) so only qualified ideas survive,
grounding the search in repo + web evidence and the [[artifact-strategy-md|strategy]] and
compound corpus ([[pattern-source-grounding]]).

It is the **ideation** flavor of [[stage-align]], clustering with BMAD's [[bmad-brainstorming]]
and Addy's [[addy-idea-refine]] (diverge-then-converge). Compound Engineering's twist is the
explicit adversarial cut and grounding pass before an idea is allowed forward.

## Cross-framework equivalents
Ideation cluster: `ce-ideate` ↔ [[bmad-brainstorming]] ↔ [[addy-idea-refine]] — all turn a vague
space into a small set of qualified directions. BMAD's [[bmad-forge-idea]] pressure-tests a
*single* idea; `ce-ideate`'s adversarial filter is the multi-candidate analogue.

## See Also
- [[bmad-brainstorming]] · [[addy-idea-refine]] — ideation-cluster counterparts.
- [[bmad-forge-idea]] — single-idea adversarial pressure-test.
- [[ce-pov]] — the decisive-verdict sibling; [[ce-brainstorm]] — the requirements sibling.
- [[stage-align]] — the canonical stage this implements.
