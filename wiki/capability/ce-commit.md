---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-release]]"
delegates_to: []
produces: ["[[artifact-atomic-commit]]"]
applies: ["[[pattern-trunk-based-development]]"]
equivalent_to: ["[[addy-git-workflow]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-commit

`/ce-commit` — "Create a single, well-crafted git commit with convention awareness and logical file-level splitting." Detects the repo's commit conventions, groups changes into a coherent atomic unit (splitting at the file level when the diff spans unrelated concerns), and writes a well-formed message → [[artifact-atomic-commit]].

It implements [[stage-release]] (finalize) on the ship-to-prod side and clusters with Addy's [[addy-git-workflow]] on atomic commits ([[pattern-trunk-based-development]]). It is the narrowest of Compound Engineering's release skills — one commit — feeding [[ce-commit-push-pr]].

## Cross-framework equivalents
`ce-commit` ↔ [[addy-git-workflow]] (`equivalent_to`, atomic-commit axis) — both produce clean atomic commits on a trunk-based flow. `ce-commit` is commit-only; Addy's skill also carries semver + changelogs.

## See Also
- [[addy-git-workflow]] — the atomic-commit counterpart.
- [[ce-commit-push-pr]] — the push-and-PR escalation of this skill.
- [[stage-release]] — the canonical stage this implements.
