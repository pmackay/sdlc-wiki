---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[gstack-upgrade]]"]
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd upgrade

`sd upgrade [--check]` — self-update to the latest `@os-eco/seeds-cli` from npm; `--check` reports whether a newer version exists without installing it.

A self-maintenance utility, mapping to **no canonical SDLC stage** — the direct counterpart of [[gstack-upgrade]], and for the same reason: a tool an agent invokes daily is a tool whose version drift the agent should be able to notice and fix without a human. Seeds pins its version in two places (`package.json` and `src/version.ts`), kept in sync by a `version:bump` script and verified in CI, so `--check` compares against a single authoritative constant.

## See Also
- [[gstack-upgrade]] — the equivalent self-updater in another framework.
- [[seeds-doctor]] — the other maintenance command, for data rather than code.
