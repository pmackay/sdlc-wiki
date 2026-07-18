---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /setup-deploy

`/setup-deploy` — the **Deploy Configurator**. One-time setup for [[gstack-land-and-deploy]]:
detects your platform (Fly.io, Render, Vercel, …), production URL, and deploy commands.

An **enabling** capability for the release/deploy arc ([[stage-release]]) — configuration only, not
a lifecycle step itself. It supplies the config [[gstack-land-and-deploy]] and [[gstack-canary]]
consume.

## See Also
- [[gstack-land-and-deploy]] — the deploy step this configures.
- [[gstack-canary]] — the post-deploy monitor that uses the production URL.
- [[stage-release]] — the stage this enables.
