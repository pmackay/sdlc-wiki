---
type: artifact
sources: "gstack — Garry Tan (2026)"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# Artifact: design mockup

An **AI-generated visual mockup variant** — a rendered image of a proposed UI, produced in batches
of 4-6 (via GPT Image) and displayed on a browser **comparison board** for side-by-side selection
and structured feedback. gstack's signature design-exploration output ([[gstack-design-shotgun]]):
the user picks favorites and leaves notes ("more whitespace", "lose the gradient"), the skill
generates a new round, and **taste memory** biases later rounds toward what the user actually picks.

It is a *disposable exploration* artifact ([[pattern-throwaway-prototype]]), not shippable code:
distinct from [[artifact-design-md]] (the durable design *system*) upstream and from the production
HTML ([[gstack-design-html]]) downstream. An approved mockup is the hand-off between them.

## Produced by (backlinks)
- [[gstack-design-shotgun]] — generates the variant batches, comparison board, and taste-memory iteration.

## See Also
- [[artifact-design-md]] — the durable design system the mockups explore against.
- [[gstack-design-html]] — turns an approved mockup into production HTML.
- [[pattern-throwaway-prototype]] — the build-to-learn technique this artifact embodies.
- [[stage-implement]] — the stage this artifact belongs to.
