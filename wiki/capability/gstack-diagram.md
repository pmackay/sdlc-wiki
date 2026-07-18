---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /diagram

`/diagram` — the **Diagram Maker**. English (or mermaid source) in, an editable **diagram triplet** out: mermaid source, a hand-drawn-style `.excalidraw` file you can open and edit on excalidraw.com, and a rendered SVG/PNG. Zero network. Embed the source in markdown and [[gstack-make-pdf]] renders it.

A **cross-cutting utility** with no single lifecycle stage — used wherever a diagram helps (e.g. [[gstack-plan-eng-review]]'s data-flow/state-machine diagrams, or documentation). No `implements:` edge; it supports many stages rather than realizing one.

## See Also
- [[gstack-make-pdf]] — renders the diagram source into a publication PDF.
- [[gstack-plan-eng-review]] — a frequent consumer (architecture diagrams).
