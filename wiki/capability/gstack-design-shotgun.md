---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: "[[artifact-design-mockup]]"
applies: ["[[pattern-throwaway-prototype]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /design-shotgun

`/design-shotgun` — the **Design Explorer**. "Show me options." Generates **4-6 AI mockup variants**
(GPT Image), opens a comparison board in your browser, collects structured feedback ("more
whitespace", "bolder headline"), and iterates in rounds. **Taste memory** kicks in after a few
rounds so it biases toward what you actually pick (persisted per-project via `gstack-taste-update`,
decays 5%/week). Repeat until you love something, then hand it to [[gstack-design-html]].

Visual exploration before committing to code — the throwaway-prototype technique
([[pattern-throwaway-prototype]]) applied to UI — producing [[artifact-design-mockup|mockup variants]]
rather than shippable code. The taste memory is a small [[pattern-knowledge-compounding]] loop
(the tool learns your design preferences). No cross-framework counterpart: gstack is the only
framework here with an image-generation design-exploration loop.

## See Also
- [[gstack-design-consultation]] — supplies the design system the variants explore.
- [[gstack-design-html]] — turns the chosen mockup into production HTML.
- [[stage-implement]] — the canonical stage this implements.
