---
type: capability
subtype: command
belongs_to: "[[agent-os]]"
implements: "[[stage-align]]"
delegates_to: []
produces: ["[[artifact-product-docs]]"]
applies: ["[[pattern-grilling]]", "[[pattern-scale-adaptive-planning]]"]
equivalent_to: ["[[ce-strategy]]"]
sources: "Agent OS v3.0.0 — plan-product (2026)"
raw: ["../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Agent OS: plan-product

`/plan-product` — establish the **foundational product docs** through an interactive conversation, creating [[artifact-product-docs|mission.md, roadmap.md, and tech-stack.md]] in `agent-os/product/`. Six steps: check for existing docs (fresh / update-specific / cancel) → gather **vision** (problem, audience, differentiator) → gather **roadmap** (MVP must-haves + post-launch) → establish **tech stack** (reuse a global tech-stack standard if present, else ask) → generate the three files → confirm. It uses the host tool's **AskUserQuestion** tool exclusively, **one question at a time**, and keeps the docs deliberately lightweight.

This is Agent OS's [[stage-align]] capability: it establishes the durable *product-direction* context read by every later [[agent-os-shape-spec|shape-spec]]. Its closest cross-framework counterpart is Compound Engineering's [[ce-strategy]] — both maintain a standing, upstream anchor document (there `STRATEGY.md`, here the `product/` trio) that downstream planning defers to, and both are *read as context* rather than *mechanically gated* (the property that keeps them in align rather than a `stage-govern`). It differs from a heavyweight PRD by design: one-question interviews and lightweight docs, sized to the project ([[pattern-scale-adaptive-planning]]).

## See Also
- [[ce-strategy]] — the counterpart standing product-direction anchor (STRATEGY.md).
- [[agent-os-shape-spec]] — reads these product docs when shaping each spec.
- [[bmad-product-brief]] · [[bmad-prd]] — heavier product-planning artifacts in a full-SDLC framework.
- [[artifact-product-docs]] — the mission/roadmap/tech-stack trio this produces.
- [[stage-align]] — the canonical stage this implements (strategy/product-direction flavor).
