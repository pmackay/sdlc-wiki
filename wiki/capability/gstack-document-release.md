---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-release]]"
delegates_to: ["[[gstack-document-generate]]"]
produces: "[[artifact-diataxis-docs]]"
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /document-release

`/document-release` — the **Technical Writer**. Post-ship, it reads every doc file, cross-references
the diff, and **updates everything that drifted** — README, ARCHITECTURE, CONTRIBUTING, CLAUDE.md,
TODOS. Builds a **Diataxis coverage map** (reference / how-to / tutorial / explanation) so gaps show
in the PR body, and chains [[gstack-document-generate]] to fill them. Auto-invoked by
[[gstack-ship]] so docs stay current without an extra command.

gstack's docs-stay-current release capability, producing [[artifact-diataxis-docs]]. It is the
maintenance half (update what drifted); the from-scratch half is [[gstack-document-generate]].
Relates to Addy's [[addy-documentation]] and BMAD's [[bmad-tech-writer]], but is uniquely
**diff-driven and release-triggered**.

## See Also
- [[gstack-document-generate]] — generates the missing docs the coverage map finds.
- [[gstack-ship]] — auto-invokes this at release time.
- [[addy-documentation]] — the documentation-skill relative.
- [[stage-release]] — the canonical stage this implements (docs sub-activity).
