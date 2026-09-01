---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: []
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd completions

`sd completions <bash|zsh|fish>` — print a shell completion script for the current command surface, generated from the commander program rather than hand-maintained, so new commands and flags complete as soon as they exist.

Included for full coverage of the command surface. It is the framework's only capability aimed squarely at a **human** at a terminal rather than at an agent — agents do not tab-complete — and maps to **no canonical SDLC stage**.

## See Also
- [[seeds-list]] — where the `--format ids` mode serves the analogous shell-composability goal for agents.
- [[seeds]] — the parent framework.
