---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: []
applies: ["[[pattern-worktree-isolation]]"]
equivalent_to: ["[[seeds-init]]"]
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd init

`bd init` — create `.beads/` and make the project tracked. By default it also *"creates or updates `AGENTS.md` so agents can discover the beads workflow, and installs project Claude/Codex integrations"* unless you pass `--skip-agents` or `--stealth`. Three siblings share the page: `bd bootstrap` (*"non-destructive database setup for fresh clones and recovery"* — what other clones run after someone else migrates the schema), `bd init-safety` (explains the flag semantics and the destroy-token format), and `bd where` (report the active beads location).

Three postures worth distinguishing, because they are the whole answer to "the tracker lives in the repo, but which repo?":

- **default** — `.beads/` committed, `AGENTS.md` updated, hooks installed, Dolt data on the git remote under `refs/dolt/data`.
- **`--stealth`** — *"use beads locally without committing files to the main repo"*: sets `no-git-ops: true`, disables hook installation and all git operations. For personal use on a shared project.
- **`--contributor`** — route planning issues to a separate repo so experimental work stays out of PRs ([[beads-repo]]).

Beads also works **without git at all**: `export BEADS_DIR=…` bypasses repo discovery, and *"all core commands work with zero git calls"* — for non-git VCS (Sapling, Jujutsu, Piper), monorepo subdirectories, CI, and ephemeral test databases. That is a sharp contrast with [[seeds-init]], whose entire merge and sync story *is* git (`merge=union` gitattributes); beads' git integration is *"optional"* because Dolt already provides versioning.

Maps to **no canonical SDLC stage** — project bootstrap.

## See Also
- [[beads-setup]] — the richer per-harness integration installer.
- [[beads-doctor]] — health checks and recovery for what this sets up.
- [[beads-repo]] — where `--contributor` routing is configured.
- [[seeds-init]] — the cross-store counterpart, and the opposite bet on git.
