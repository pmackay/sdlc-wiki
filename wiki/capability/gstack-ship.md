---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: ["[[gstack-document-release]]"]
produces: ["[[artifact-pull-request]]", "[[artifact-changelog]]", "[[artifact-atomic-commit]]"]
applies: ["[[pattern-trunk-based-development]]", "[[pattern-parallel-persona-review]]"]
equivalent_to: ["[[gsd-ship]]", "[[addy-shipping]]", "[[openspec-archive]]", "[[ce-commit-push-pr]]", "[[sp-finishing-a-development-branch]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /ship

`/ship` — the **Release Engineer**. Detects and merges the base branch, runs tests (bootstrapping a test framework from scratch if the project has none), reviews the diff, bumps `VERSION`, updates the `CHANGELOG`, commits, pushes, and opens a **PR**. Workspace-aware version queue; filter-squashes `WIP:` checkpoint commits so bisect stays clean; every run produces a **coverage audit**; **auto-invokes** [[gstack-document-release]] so docs stay current; and auto-closes the source issue from [[gstack-spec]] on merge. **Smart review routing** decides which reviews are appropriate before shipping.

gstack's member of the cross-framework **finalize / close-out** cluster — alongside [[gsd-ship]], [[addy-shipping]], [[openspec-archive]], and [[ce-commit-push-pr]]. Produces the PR, changelog, and commits ([[pattern-trunk-based-development]]). Unlike GSD/CE/OpenSpec, gstack continues past the PR into a genuine **deploy** step ([[gstack-land-and-deploy]]) and post-deploy **monitoring** ([[gstack-canary]]).

## See Also
- [[gstack-land-and-deploy]] — merges and deploys the PR this opens.
- [[gstack-landing-report]] — dashboard for the ship queue.
- [[gstack-document-release]] — auto-invoked to keep docs current.
- [[gsd-ship]] · [[addy-shipping]] · [[ce-commit-push-pr]] · [[openspec-archive]] — finalize-cluster counterparts.
- [[stage-release]] — the canonical stage this implements.
