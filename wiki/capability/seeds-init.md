---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: []
applies: ["[[pattern-worktree-isolation]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd init

`sd init` — create the `.seeds/` directory in the current project and make it git-native. It writes `config.yaml` (project name, version), the three empty JSONL stores (`issues.jsonl`, `templates.jsonl`, `plans.jsonl`), a `.gitignore` covering `*.lock` files, and — the part that matters — appends the `merge=union` lines to the project's root `.gitattributes`:

```
.seeds/issues.jsonl merge=union
.seeds/templates.jsonl merge=union
.seeds/plans.jsonl merge=union
```

That one-time write is what makes the whole store safe for parallel agents. Union-merging append-only JSONL means two branches that each filed work merge without a conflict, and seeds' dedup-on-read (last occurrence wins) resolves any duplicate ids the union leaves behind — so there is no custom merge driver and no sync step. [[seeds-doctor]] re-checks and backfills all three lines, sourcing the canonical list from `init` rather than hardcoding it.

Maps to **no canonical SDLC stage** — it is project bootstrap. It applies [[pattern-worktree-isolation]] indirectly: the gitattributes are precisely the affordance that lets several agents in several worktrees write one shared store and let git reconcile them.

## See Also
- [[seeds-doctor]] — verifies and repairs what `init` set up.
- [[seeds-onboard]] — the other bootstrap step: telling the *agent* that seeds exists.
- [[seeds-migrate-from-beads]] — populates a freshly-initialized store from a beads export.
- [[seeds]] — the parent framework.
