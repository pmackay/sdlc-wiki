---
type: capability
subtype: skill
belongs_to: "[[bm-skills]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-design-md]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: ["[[addy-frontend-ui]]"]
sources: "Brian Casel (Builder Methods) — BM Skills (2026)"
raw: ["../../raw/bm-skills/2026-07-09-bm-skills.md"]
updated: 2026-07-09
---

# Design System Builder (bm-design-system)

`bm-design-system` — a skill that **scaffolds a complete, opinionated design system into a React + Tailwind v4 codebase**: a single-page reference at `/admin/design-system` that previews and documents every primitive, a small set of reusable shadcn-style components, and instructions appended to `AGENTS.md`/`CLAUDE.md` so **future agents defer to the design system instead of drifting** ([[pattern-context-engineering]]). It detects the framework (Vite / Next app or pages router / Rails+Inertia / react-on-rails), ships **locked default** colors and fonts (no decision asked), and stays opinionated-not-exhaustive.

A build-time capability that produces a working design foundation ([[artifact-design-md]]) as real component code plus its living reference page — filed under [[stage-implement]]. Its closest counterpart is Addy's [[addy-frontend-ui]] (production UI + design systems + accessibility); it also parallels [[gstack-design-consultation]] (which builds a `DESIGN.md` design system) and BMAD's [[bmad-ux]] design spec, but bm-design-system uniquely scaffolds **runnable code + agent guardrails** rather than a spec document. Hard requirements: React + Tailwind v4 (it stops if either is absent).

## See Also
- [[addy-frontend-ui]] — the cross-framework counterpart (production UI + design systems).
- [[gstack-design-consultation]] · [[bmad-ux]] — design-system / UX-spec relatives.
- [[artifact-design-md]] — the design-system output.
- [[stage-implement]] — the canonical stage this implements.
