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

# /setup-browser-cookies

`/setup-browser-cookies` — the **Session Manager**. Imports cookies from your real browser (Chrome, Arc, Brave, Edge) into the headless [[gstack-browse]] session so the agent can test **authenticated pages**. Cookies are decrypted in-process (never written to disk in plaintext), the browser DB is opened read-only, and first import triggers a Keychain approval dialog.

An **enabling** capability for authenticated live testing ([[stage-validate]]); one-time setup that makes [[gstack-qa]] / [[gstack-design-review]] work behind login walls.

## See Also
- [[gstack-browse]] — the session cookies are imported into.
- [[gstack-qa]] — the testing skill that benefits from authenticated sessions.
- [[stage-validate]] — the stage this enables.
