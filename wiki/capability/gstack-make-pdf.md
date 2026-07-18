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

# /make-pdf

`/make-pdf` — the **Publisher**. Turns any markdown file into a **publication-quality document**:
mermaid and excalidraw fences render as vector diagrams (fully offline), images scale to the page
and never truncate, wide diagrams get their own landscape page. `--to html` emits one self-contained
file; `--to docx` a Word doc.

A **cross-cutting utility** with no single lifecycle stage — an output/export tool used across the
lifecycle (specs, plans, reports, docs). No `implements:` edge. Pairs with [[gstack-diagram]] for
diagram rendering.

## See Also
- [[gstack-diagram]] — produces the diagram sources this renders.
- [[gstack-document-generate]] — a frequent source of the markdown it publishes.
