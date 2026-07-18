---
type: capability
subtype: command
belongs_to: "[[gstack]]"
implements: "[[stage-validate]]"
delegates_to: []
produces: []
applies: []
equivalent_to: []
sources: "gstack — Garry Tan (2026); ARCHITECTURE.md"
raw: ["../../raw/gstack/2026-07-05-gstack-framework.md"]
updated: 2026-07-05
---

# /browse

`/browse` — the **QA Engineer's eyes**: a persistent **headless Chromium daemon** giving the agent real clicks, real screenshots, and real navigation at **~100-200ms per command**. A long-lived `Bun.serve()` server talks to Chromium over CDP so cookies, tabs, and login sessions **persist across commands** (first call ~3s, every call after ~100ms; 30-min idle timeout). Addresses page elements by **refs** (`@e1`, `@e2`) from an ARIA snapshot instead of CSS selectors. Includes a raw `$B cdp` escape hatch (deny-default allowlist) and browser **handoff** (`$B handoff`/`$B resume`) at CAPTCHAs/auth walls.

This is gstack's foundational **infrastructure** — "the browser is the hard part; everything else is Markdown." It is the enabling capability behind live [[gstack-qa]], [[gstack-design-review]], [[gstack-benchmark]], [[gstack-canary]], and [[gstack-scrape]]; filed under [[stage-validate]] as an enabling capability (like [[ce-worktree]] under implement). The visible variant is [[gstack-open-gstack-browser]]; authenticated testing uses [[gstack-setup-browser-cookies]].

## See Also
- [[gstack-open-gstack-browser]] — the visible GStack Browser with sidebar + stealth.
- [[gstack-setup-browser-cookies]] — import cookies for authenticated pages.
- [[gstack-qa]] · [[gstack-scrape]] · [[gstack-benchmark]] · [[gstack-canary]] — the skills it powers.
- [[stage-validate]] — the stage its testing capabilities serve.
