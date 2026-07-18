---
type: capability
subtype: skill
belongs_to: "[[bm-skills]]"
implements: []
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "Brian Casel (Builder Methods) — BM Skills (2026)"
raw: ["../../raw/bm-skills/2026-07-09-bm-skills.md"]
updated: 2026-07-09
---

# Favicon Creator (bm-favicon-creator)

`bm-favicon-creator` — a skill that generates a complete, cross-device **favicon set** (a rounded
square with a centered icon on a solid background) from a **Lucide icon** (default), another icon
library, an existing SVG, or a described icon, then writes `favicon.ico`, `icon.svg`, `icon.png`,
and `apple-touch-icon.png` to `public/` and wires the favicon meta tags into the layout. Requires
`rsvg-convert` + ImageMagick's `magick`.

A pure **asset/branding utility** — it carries **no `implements:` edge** and belongs to no lifecycle
stage (like gstack's [[gstack-make-pdf]] / [[gstack-diagram]] utilities). Catalogued for
completeness of the [[bm-skills]] ingest.

## See Also
- [[bm-skills]] — the marketplace this belongs to.
- [[bm-design-system]] — the sibling front-end scaffolding skill.
