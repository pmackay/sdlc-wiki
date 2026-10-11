---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-supply-chain-scanning]]", "[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl install

The package manager proper: `install`, `uninstall`, `list`, `outdated`, and `update`. The command family that makes *"context as code"* literal, and the reason the [supply layer](../registry/index.md) reads as a package manager rather than a catalogue.

Four install sources, which is what keeps it usable before anything is published: the **registry** (`tessl install tessl/skill-optimizer`), the **filesystem** (any directory containing a `.tessl-plugin/plugin.json`, so you can test before publishing), a **GitHub repo** (including shorthand, a specific branch and path, interactive skill selection from a multi-skill repo, and named skills), and **a specific commit** — the last one noted in the docs as useful *"when the registry shows security results for that commit"*, which is [[pattern-supply-chain-scanning]] leaking into the install syntax.

Scope is per-repository by default with a `--global` flag for skills you want everywhere. `outdated` and `update` carry the rest of the dependency vocabulary — interactive or unattended updates, a single named plugin, and an explicit opt-in for breaking changes. Skills are linked into the agent's own directories (directory junctions rather than symlinks on Windows, where moving the project folder requires a re-run).

The thing worth noticing is what this command *does not* do. There is no notion of "the framework you adopted": each bundle is an independently versioned dependency, addressable and pinnable on its own. That is the framework coming apart into parts, expressed as a CLI.

## See Also
- [[tessl-search]] — finds the thing this installs.
- [[tessl-plugin]] — produces [[artifact-capability-bundle]], the unit this consumes.
- [[tessl-init]] — configures the harnesses these installs land in.
- [[tessl]] — the registry this belongs to.
