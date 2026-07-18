---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /open-gstack-browser

`/open-gstack-browser` — launch **GStack Browser**: an AI-controlled visible Chromium with the
**sidebar extension** baked in, **anti-bot stealth** (Google/NYTimes work without CAPTCHAs), custom
branding, one-click cookie import, and **auto model routing** (Sonnet for fast actions, Opus for
reading/analysis). The sidebar runs a child Claude instance in an isolated session; a layered
**prompt-injection defense** protects it. `$B disconnect` returns to headless.

The headed counterpart to the [[gstack-browse]] daemon — enabling infrastructure for the
**Test/Review** stages ([[stage-validate]] / [[stage-review]]). Powers cross-agent coordination via
[[gstack-pair-agent]].

## See Also
- [[gstack-browse]] — the headless daemon this makes visible.
- [[gstack-pair-agent]] — shares this browser across agents.
- [[gstack-setup-browser-cookies]] — cookie import for authenticated sessions.
- [[stage-validate]] — the stage this enables.
