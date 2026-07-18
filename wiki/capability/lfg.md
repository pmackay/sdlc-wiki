---
type: capability
subtype: command
belongs_to: "[[compound-engineering]]"
implements: ["[[stage-plan]]", "[[stage-implement]]", "[[stage-review]]", "[[stage-validate]]", "[[stage-release]]"]
delegates_to: ["[[ce-plan]]", "[[ce-work]]", "[[ce-simplify-code]]", "[[ce-code-review]]", "[[ce-commit-push-pr]]"]
produces: ["[[artifact-pull-request]]"]
applies: ["[[pattern-autonomous-loop]]", "[[pattern-worktree-isolation]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /lfg

`/lfg` — "Run full hands-off engineering pipeline from planning through green PR with CI watch." Compound Engineering's **autonomous orchestrator**: after a brainstorm, it chains the whole loop without supervision — plan → work → simplify → review (with fixes) → test → commit → push → open PR → watch CI until green — and returns only when the PR is merge-ready. It runs in worktree isolation ([[pattern-worktree-isolation]]) and self-corrects on failures ([[pattern-autonomous-loop]]).

It spans [[stage-plan]] through [[stage-release]] by delegating to the loop's individual skills, so it is documented as a cross-stage orchestrator rather than owning a single stage. It is Compound Engineering's counterpart to running the human-checkpointed loop by hand — and the closest relative to Addy's `/build auto` and BMAD's [[bmad-quick-dev]] (`dev-auto`) unattended paths.

## See Also
- [[ce-plan]] · [[ce-work]] · [[ce-simplify-code]] · [[ce-code-review]] · [[ce-commit-push-pr]] — the loop steps it delegates to.
- [[pattern-autonomous-loop]] — the technique; [[bmad-quick-dev]] — BMAD's unattended fast path (nearest analogue).
- [[ce-dogfood]] — the same autonomy scoped to QA.
- [[stage-plan]] · [[stage-implement]] · [[stage-review]] · [[stage-validate]] · [[stage-release]] — the stages it orchestrates.
