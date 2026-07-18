---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: []
produces: []
applies: ["[[pattern-autonomous-loop]]"]
equivalent_to: ["[[ce-product-pulse]]"]
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /canary

`/canary` — the **SRE**. A **post-deploy monitoring loop** (via the browse daemon) that watches for
console errors, performance regressions, and page failures after a release.

gstack's operate/monitor capability — the counterpart to Compound Engineering's post-release
[[ce-product-pulse]] and adjacent to Addy's [[addy-observability]]. Together with
[[gstack-land-and-deploy]] it gives gstack a genuine deploy→operate arc, the evidence behind the
[[stage-release]] `stage-operate` split candidate. Runs as a watching loop
([[pattern-autonomous-loop]]).

## See Also
- [[gstack-land-and-deploy]] — the deploy step this monitors.
- [[ce-product-pulse]] — the post-release monitoring counterpart.
- [[addy-observability]] — the observability/alerting relative.
- [[stage-release]] — the canonical stage this implements (operate/monitor sub-activity).
