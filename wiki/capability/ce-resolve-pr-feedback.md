---
type: capability
subtype: skill
belongs_to: "[[compound-engineering]]"
implements: "[[stage-release]]"
delegates_to: ["[[ce-pr-comment-resolver]]"]
produces: []
applies: ["[[pattern-parallel-persona-review]]"]
equivalent_to: []
sources: "Compound Engineering — EveryInc/compound-engineering-plugin (2026)"
raw: ["../../raw/compound-engineering/2026-07-04-compound-engineering-every.md", "../../raw/compound-engineering/2026-07-04-compound-engineering-plugin.md"]
updated: 2026-07-04
---

# /ce-resolve-pr-feedback

`/ce-resolve-pr-feedback` — "Evaluate, fix, and reply to PR review feedback in parallel including
nitpicks." Once a PR is open ([[ce-commit-push-pr]]), this triages each review comment,
implements the fixes **in parallel**, and posts replies — handling nitpicks as well as
substantive changes — to drive the PR to merge-ready.

It implements [[stage-release]] as the **pre-merge resolution** step: distinct from
[[ce-code-review]] (which *generates* internal findings in [[stage-review]]) — this one
*responds to external human reviewers'* findings on the open PR. No cross-framework counterpart
is paged; it is a distinctive release-side capability reflecting a PR-centric team workflow.

## See Also
- [[ce-commit-push-pr]] — opens the PR this resolves feedback on.
- [[ce-code-review]] — internal review that precedes external PR review.
- [[stage-release]] — the canonical stage this implements.
