---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: []
produces: "[[artifact-diataxis-docs]]"
applies: ["[[pattern-source-grounding]]"]
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /document-generate

`/document-generate` — the **Documentation Author**. Generates missing docs **from scratch** using the **Diataxis** framework: researches the codebase first, then writes reference / how-to / tutorial / explanation docs that actually match the code ([[artifact-diataxis-docs]]). Invokable standalone or chained from [[gstack-document-release]] when its coverage map finds gaps.

The from-scratch half of gstack's documentation pair (the update-what-drifted half is [[gstack-document-release]]). Researches before writing ([[pattern-source-grounding]]). Relates to Addy's [[addy-documentation]] and BMAD's [[bmad-tech-writer]]; distinctive for enforcing the four-quadrant Diataxis taxonomy.

## See Also
- [[gstack-document-release]] — chains this to fill coverage gaps at release time.
- [[addy-documentation]] · [[bmad-tech-writer]] — documentation-skill relatives.
- [[stage-release]] — the canonical stage this implements (docs sub-activity).
