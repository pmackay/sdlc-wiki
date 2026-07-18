---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-release]]"
delegates_to: ["[[ce-commit]]"]
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-trunk-based-development]]"]
equivalent_to: ["[[gsd-ship]]", "[[addy-shipping]]", "[[openspec-archive]]", "[[gstack-ship]]", "[[sp-finishing-a-development-branch]]"]
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-commit-push-pr

`/ce-commit-push-pr` — "Go from working changes to open PR with adaptive descriptions and three workflow modes." The finalize step: commit (via [[ce-commit]]), push, and open a PR whose description adapts to the change, offering three workflow modes (e.g. quick vs full). → [[artifact-pull-request]].

It implements [[stage-release]] and is Compound Engineering's member of the **finalize/ship** cluster.

## Cross-framework equivalents
Finalize cluster: `ce-commit-push-pr` ↔ [[gsd-ship]] ↔ [[addy-shipping]] ↔ [[openspec-archive]] — each closes the iteration on completed, validated work. `ce-commit-push-pr` is closest to [[gsd-ship]] (branch → PR → track); Addy's adds a launch checklist + persona fan-out, OpenSpec's merges a spec delta instead of deploying. Announcing the shipped feature is a separate step, [[ce-promote]].

## See Also
- [[gsd-ship]] · [[addy-shipping]] · [[openspec-archive]] — finalize-cluster counterparts.
- [[ce-commit]] — the commit step it delegates to; [[ce-resolve-pr-feedback]] — resolves review comments on the opened PR.
- [[ce-promote]] — announces the shipped work; [[lfg]] — runs this as its terminal step (to green CI).
- [[stage-release]] — the canonical stage this implements.
