---
type: index
sources: "Synthesized from gastownhall/beads + jayminwest/seeds (2026)"
updated: 2026-08-31
---

# Store

*The state layer — the durable work graph or memory corpus that outlives any single agent run.*

The wiki's other three layers are **compute**. A [framework](../catalogue.md#framework) is instructions; a [harness](../harness/index.md) is the loop that executes them; a [runtime](../runtime/index.md) decides where that loop runs. All three are transient — when the run ends they are gone, and so is everything the agent knew. A **store** is state: the layer that survives.

That is not an abstraction the wiki imposed. It is the pitch both members make:

> Coding agents lose their memory every time a session ends. Markdown plans rot, TODO comments scatter, and a crashed agent takes its context with it. […] Work survives the agent; the next session picks up where the last one died. — [[beads]]

A store performs no [SDLC stage](../sdlc-stage/index.md) of its own and connects to the ontology through `integrates_with:` → harness and `enables:` → pattern, plus the `belongs_to:` backlinks from its own command surface. The full schema is in [CONVENTIONS](../CONVENTIONS.md#the-state-layer-stores). **Note on the word:** `store` here means an *agent-facing state store*, not a shop, a Redux store, or a storage engine — beads' own charter is careful that it *"should not become a storage engine"*; it puts data through a storage boundary into Dolt.

## Members

| Store | Subtype | What it is | Surface | Updated |
|---|---|---|---|---|
| [[beads]] | `work` | *"Distributed graph issue tracker for AI agents, powered by Dolt."* Versioned SQL storage, typed dependency edges, knowledge-graph links, a declarative workflow engine, gates, federation, and a first-class memory surface. | ~109 commands · 48 pages | 2026-08-31 |
| [[seeds]] | `work` | *"Git-native issue tracker for AI agent workflows."* Plain JSONL merged by git, plus a schema-validated planning layer the other store deliberately refuses to have. | 37 commands · 37 pages | 2026-08-31 |

Both are `work` stores. The `memory` subtype is declared and unpaged: [[warren]] bundles **mulch** (`.mulch/`, expertise records merged across runs) and **canopy** (a versioned prompt library), and beads ships its own memory surface internally rather than as a separate product. Ingest those as `store` pages if they warrant them.

## The comparison matrix

Two instances, so the shared dimensions live here as a matrix rather than as their own derived-node namespace — the same discipline parked for the [runtime](../runtime/index.md) and [harness](../harness/index.md) layers. Graduate them only if the layer stops fitting a table.

| Concern | [[beads]] | [[seeds]] |
|---|---|---|
| **Storage substrate** | **Dolt** — version-controlled SQL; embedded in-process (default) or an external `dolt sql-server` | **JSONL** — *"the JSONL file IS the database"*; no daemon, no binary |
| **Source of truth** | the Dolt database; `.beads/issues.jsonl` is *"a passive export for viewers and interchange"* | the `.seeds/*.jsonl` files themselves |
| **Concurrency** | single file-locked writer (embedded) or many (server mode) | advisory locks (`O_CREAT\|O_EXCL`) + atomic temp-file rename |
| **Merge model** | Dolt cell-level 3-way merge; content-hash IDs so *"merges never renumber work"* | `merge=union` gitattribute + dedup-on-read (last occurrence wins) |
| **Sync** | native `bd dolt push` / `pull` against `refs/dolt/data` on your existing git remote | `sd sync` commits locally; `git push` is the user's |
| **History / audit** | a Dolt commit per write; `bd history`, `bd diff`, an events journal with actor attribution | *"Git IS the audit trail"* — `git log .seeds/issues.jsonl` |
| **Ready computation** | open, no open blockers, excluding in-progress/blocked/deferred/gated; `--claim` atomic | open with every `blockedBy` closed; `--respect-schedule` honours parked/scheduled keys |
| **Dependency edges** | five typed (`blocks`, `parent-child`, `discovered-from`, `related`, + workflow gating) — only some gate work | one (`blockedBy`/`blocks`); everything stored gates work |
| **Knowledge links** | `relates-to`, `duplicates`, `supersedes`, `replies-to` — meaning without schedulability | none |
| **Hierarchy** | hierarchical IDs (`bd-a3f8.1.1`), epics, swarms | flat ids; plans and convoys provide grouping |
| **Memory surface** | **first-class** — `bd remember` / `recall` / `memories` / `kv`, injected by `bd prime` | **delegated** — soft coupling to mulch; nothing of its own |
| **Context management** | `bd prime` sizes itself to MCP-vs-CLI (~50 vs ~1–2k tokens); semantic compaction decays old closed work | five `--format` modes, `sd prime --compact` |
| **Ephemerality** | **first-class** — `--ephemeral`, wisps, `bd purge`, federation exclusion | none; everything persists |
| **Workflow templating** | `formula` (TOML DAG) → `bd cook` → proto → `bd mol pour` → molecule / wisp | plan templates (schema-validated sections) + convoy templates |
| **Async coordination** | **gates** (human · timer · `gh:run` · `gh:pr`) and a merge slot, both expressed as blocking beads | none |
| **Planning methodology** | **refused by charter** — *"the orchestration layer owns workflow semantics"* | **built in** — `sd plan`: templated, AJV-gated, spawns the children |
| **Stage coverage** | none (deliberate) | [[stage-plan]] (13 capabilities) + a [[stage-learn]] stub |
| **External trackers** | GitHub · GitLab · Jira · Linear · Azure DevOps · Notion, each pull/push/sync | none |
| **Federation / multi-repo** | peer-to-peer federation (incl. GCS/S3 bucket mode), cross-repo deps, role-based routing | none |
| **Human channel** | `bd human` queue + `bd mail` messaging | none |
| **Harness integrations** | 13 `bd setup` recipes (claude · codex · factory · cursor · copilot · gemini · aider · mux · opencode · junie · windsurf · cody · kilocode) | `.claude/commands/` · `.factory/skills/` · `.pi/`; `AGENTS.md` for the rest |
| **MCP** | yes — `beads-mcp` on PyPI, and `bd prime` detects it | no |
| **Works without git** | yes — `BEADS_DIR` + `--stealth`; Dolt is the backend, git integration optional | no — git *is* the merge and sync mechanism |
| **Ops burden** | schema migrations, a version guard, `bd dolt start/stop/killall`, GC | none beyond git |
| **Distribution** | Go binary: Homebrew · npm · PyPI (MCP) · AUR · winget. MIT | npm `@os-eco/seeds-cli`, Bun/TypeScript. MIT |

## What the matrix shows

**They agree on the core model.** Both compute a claimable frontier from a dependency graph and make atomic claiming the coordination protocol between parallel agents. Two tools built independently for the same job converged on *the unblocked frontier as the dispatch primitive* — the strongest signal this layer produces, and the thing an orchestrator like [[warren]] or [[bernstein]] consumes.

**They disagree on storage, explicitly and by design.** Seeds was written to replace beads and its README argues against it by name — the binary database that *"can't diff/merge"*, the export-state tracking, the lock contention. Beads' charter argues the opposite case: *"Dolt provides storage, versioning, sync, merge behavior, concurrency, and crash safety"*, so beads deliberately does not reimplement any of it. Both pages carry the conflict with attribution; neither the wiki nor this table adjudicates it. It is the first head-to-head disagreement between two paged tools here, and it is more useful preserved than resolved.

**They disagree about the layer's own boundary.** Beads' charter forbids encoding *"workflow semantics"* — that belongs to the orchestration layer above. Seeds bakes a planning methodology into the store so that the plan and the queue are one object. That is a genuine open question about how thick this layer should be, and the two answers are visible in the surface size: 109 commands versus 37.

**Three axes only one instance has.** Ephemerality, async gates, and a first-class memory surface are beads-only; a schema-validated plan gate is seeds-only. With two members it is too early to say whether those are the layer's real dimensions or one project's ideas — which is exactly why they are matrix rows and not nodes.

## See Also

- [CONVENTIONS](../CONVENTIONS.md#the-state-layer-stores) — the schema: node type, subtypes, edges, and the ingest procedure.
- [[warren]] — the runtime that consumes a store (dispatching from `.seeds/`) and bundles two `memory`-subtype candidates.
- [[bernstein]] — an orchestrator that built its *own* file-based state (`.sdd/`) instead of adopting a store; the counter-example that shows why the layer is worth naming.
- [[pattern-session-handoff]] · [[pattern-knowledge-compounding]] · [[pattern-context-engineering]] · [[pattern-autonomous-loop]] — the patterns this layer supplies, each carrying a **Persisted by (store)** roster.
- [[topic-harness-engineering]] — the guide layer both stores write into (`bd setup`, `sd onboard`).
