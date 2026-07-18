---
type: capability
subtype: command
belongs_to: "[[gsd]]"
implements: "[[stage-release]]"
delegates_to: []
produces: "[[artifact-pull-request]]"
applies: "[[pattern-spec-driven-development]]"
equivalent_to: ["[[addy-shipping]]", "[[openspec-archive]]", "[[ce-commit-push-pr]]", "[[gstack-ship]]", "[[sp-finishing-a-development-branch]]"]
sources: "Open GSD docs — workflow-commands (2026)"
raw: ["../../raw/gsd/2026-06-27-gsd-core-framework.md"]
updated: 2026-07-04
---

# /gsd-ship

`/gsd-ship N` — Phase 5. "Create a pull request and prepare the phase for merge." Pushes
the phase branch, creates a PR with an auto-generated summary, triggers optional review
(e.g. `/gsd-review` cross-AI feedback), tracks merge completion, then archives the phase
so the loop proceeds to the next one.

**Produces:** [[artifact-pull-request]] on the remote repository.

**Flags:** `--draft` (open PR as draft, not ready-for-review). Branch granularity follows
the configured Git branching strategy (none / phase / milestone).

## See Also
- [[gsd-verify-work]] — must pass before shipping.
- [[addy-shipping]] — Addy's shipping skill; same PR-and-merge release step.
- [[openspec-archive]] — OpenSpec's finalize step; closes the iteration via spec-merge + archive rather than a PR.
- [[stage-release]] — the canonical stage this implements.
