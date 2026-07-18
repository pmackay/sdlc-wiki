---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: ["[[pattern-trunk-based-development]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /land-and-deploy

`/land-and-deploy` — the **Release Engineer's** deploy step. **Merge** the PR, **wait for CI and
deploy**, then **verify production health**. "One command from 'approved' to 'verified in
production.'" Deploy configuration comes from [[gstack-setup-deploy]] (Fly.io / Render / Vercel / …).

This is what makes gstack distinctive on the delivery side: it is the **first framework here to
separate deploy from ship** — [[gstack-ship]] opens the PR; `land-and-deploy` merges and pushes it
to production and confirms it's healthy; [[gstack-canary]] then monitors. That deploy+verify+monitor
arc is the evidence strengthening the [[stage-release]] `stage-operate` split candidate. Nearest
relatives elsewhere are Addy's CI/CD ([[addy-ci-cd]]) and feature-flag rollout, but no other
framework ships an actual deploy command.

## See Also
- [[gstack-ship]] — opens the PR this merges and deploys.
- [[gstack-canary]] — monitors the deployment this verifies.
- [[gstack-setup-deploy]] — supplies the deploy configuration.
- [[addy-ci-cd]] — the nearest CI/CD relative.
- [[stage-release]] — the canonical stage this implements (deploy sub-activity).
