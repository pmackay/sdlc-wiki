---
type: pattern
sources: "Matt Pocock — Skills for Real Engineers (2026); John Ousterhout"
updated: 2026-07-04
---

# Pattern: Deep modules

John Ousterhout's principle: a good module provides "a lot of functionality accessed through
a simple interface." Maximize the ratio of capability to interface surface, and place module
boundaries at clean seams — the antidote to architectural entropy ("ball of mud").

## Applied by (backlinks)

Matt Pocock — Skills for Real Engineers:

- [[mp-codebase-design]] — design discipline for deep modules with small interfaces.
- [[mp-improve-codebase-architecture]] — audits existing code toward this shape.

Addy Osmani — Agent Skills:

- [[addy-api-design]] — designs small interfaces over rich functionality.

Compound Engineering:

- [[ce-simplify-code]] — reduce complexity / extract reuse behind simpler interfaces, behavior-preserving.
- [[ce-architecture-strategist]] — reviews module boundaries / service boundaries for integrity.

## See Also
- [[stage-plan]] — where forward-looking design applies.
- [[stage-review]] — where the architecture audit applies.
