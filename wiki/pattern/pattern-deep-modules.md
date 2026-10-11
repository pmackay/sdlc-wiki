---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); John Ousterhout; pstack v0.15.2 — Lauren Tan (2026)"
updated: 2026-09-11
---

# Pattern: Deep modules

John Ousterhout's principle: a good module provides "a lot of functionality accessed through a simple interface." Maximize the ratio of capability to interface surface, and place module boundaries at clean seams — the antidote to architectural entropy ("ball of mud").

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-codebase-design]] — design discipline for deep modules with small interfaces.
- [[mp-improve-codebase-architecture]] — audits existing code toward this shape.

Addy Osmani — Agent Skills:

- [[addy-api-design]] — designs small interfaces over rich functionality.

Compound Engineering:

- [[ce-simplify-code]] — reduce complexity / extract reuse behind simpler interfaces, behavior-preserving.
- [[ce-architecture-strategist]] — reviews module boundaries / service boundaries for integrity.

pstack:

- [[pstack-architect]] — screens every design candidate against a shipped red-flag list (**shallow modules, information leakage, temporal decomposition, pass-through methods**) before synthesis, and compares survivors on **interface depth**: prefer the design that hides more complexity behind a smaller, simpler public surface.
- [[pstack-principle-minimize-reader-load]] — count the layers between question and answer and the hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.
- [[pstack-principle-laziness-protocol]] — the tie-break when two candidates score level: prefer the cleaner boundary or smaller API.

## See Also
- [[stage-plan]] — where forward-looking design applies.
- [[stage-review]] — where the architecture audit applies.
