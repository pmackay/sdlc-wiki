---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /design-html

`/design-html` — the **Design Engineer**. Turns an approved mockup (from [[gstack-design-shotgun]], a CEO plan, a design review, or a description) into **production-quality HTML/CSS** — not the kind that looks fine at one width and breaks everywhere else. Uses **Pretext computed layout** so text reflows, heights adjust to content, and layouts are dynamic (30KB, zero dependencies). Detects the framework (React / Svelte / Vue) and outputs the right format; smart API routing picks Pretext patterns per design type (landing page vs dashboard vs form vs card). "The output is shippable, not a demo."

The realization end of gstack's design pipeline ([[gstack-design-consultation]] → [[gstack-design-shotgun]] → **design-html**). It produces UI source code directly (no separate artifact page). No cross-framework counterpart — gstack is the only framework here with a dedicated mockup-to-production-frontend skill.

## See Also
- [[gstack-design-shotgun]] — supplies the approved mockup.
- [[gstack-design-review]] — audits the resulting UI after it ships.
- [[stage-implement]] — the canonical stage this implements.
