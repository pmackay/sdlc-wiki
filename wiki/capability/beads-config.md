---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: []
equivalent_to: ["[[seeds-config]]"]
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd config

`bd config get|set|list|show|unset|set-many|validate|apply|drift` — configuration, with three subcommands that are unusual enough to note.

- **`bd config show`** prints *"all effective configuration **with provenance**"* — which value won, and from where. In a tool with per-repo config, git config, environment variables, and CLI flags, "why is this setting what it is?" is a real question and most tools cannot answer it.
- **`bd config drift`** detects *"config-vs-reality inconsistencies"*, and **`bd config apply`** *"reconciles system state to match configuration"*. That is a declarative-convergence loop — the config is the desired state, drift reports divergence, apply fixes it — which is infrastructure-tool thinking applied to a CLI's own setup.

`bd context` (effective backend identity and repository context), `bd info` (database information, including `--whats-new`), `bd ping` (connectivity), `bd version`, and `bd metrics` (anonymous usage metrics: on/off/example, honouring `DO_NOT_TRACK`) round out the introspection surface.

Compare [[seeds-config]], which publishes a **JSON Schema** for its config so an external UI can render a form. Beads goes the other direction — richer imperative surface, provenance and drift instead of a machine-readable contract. Both are reasonable; the schema is easier to integrate against, the drift loop is easier to operate.

Maps to **no canonical SDLC stage**.

## See Also
- [[beads-doctor]] — the health command drift feeds.
- [[beads-repo]] — the `routing.*` keys.
- [[seeds-config]] — the cross-store counterpart and its contrasting posture.
