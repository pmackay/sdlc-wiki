---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-review]]"
delegates_to: []
produces: "[[artifact-review-report]]"
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /devex-review

`/devex-review` — the **DX Tester**. A live developer-experience audit that actually tests your onboarding: navigates the docs, tries the getting-started flow, **times TTHW** (time-to-hello-world), and screenshots errors. Compares the measured reality against the scores from [[gstack-plan-devex-review]] — "the boomerang that shows if your plan matched reality."

The live-audit counterpart of [[gstack-plan-devex-review]], in gstack's **Review** phase ([[stage-review]]). Distinctive in this wiki: no other framework ships a dedicated developer-experience validator.

## See Also
- [[gstack-plan-devex-review]] — the plan-time review this boomerangs from.
- [[gstack-design-review]] — the end-user-facing sibling live audit.
- [[stage-review]] — the canonical stage this implements (Review side).
