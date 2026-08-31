# SDLC Agent-Skill Wiki

A knowledge base about **software-development-lifecycle agent frameworks** — the toolkits, skills and commands that AI coding agents run (GSD, BMAD, Spec Kit, OpenSpec, Superpowers, Compound Engineering, gstack, Agent OS, nano-spec, and others) — and the lifecycle that emerges when you compare them side by side.

It is not documentation for any one framework. It is a synthesis: every framework's capabilities are compiled into a shared ontology so that the same activity under different branding (GSD's *Discuss*, Matt Pocock's *grilling*, gstack's *office-hours*) resolves to one canonical stage, and so that gaps become visible.

Published at **https://pmackay.github.io/sdlc-wiki**.

## Structure

Two top-level directories, per the skill this vault was built with (see [Provenance](#provenance)):

- **`raw/`** — immutable source material, one directory per framework, files named `YYYY-MM-DD-slug.md` with a `source_urls` / `collected` / `published` header. Never edited after capture. 23 sources across 15 directories.
- **`wiki/`** — compiled articles. Everything here is written by an agent and rewritten freely.

Inside `wiki/`, one level of directories, each mapping to a node type in the ontology:

| Directory | Pages | What it holds |
|---|---:|---|
| `framework/` | 12 | A complete SDLC agent toolkit or methodology |
| `capability/` | 230 | One unit of work a framework exposes — a command, skill, or sub-agent. **The hub**: every process-layer edge originates here |
| `sdlc-stage/` | 9 | The canonical lifecycle stages. **Derived** — a stage page's body is synthesised from the capabilities that `implements:` it |
| `artifact/` | 37 | A concrete output a capability produces (a spec, a plan, a commit) |
| `pattern/` | 31 | A reusable technique a capability applies. Also the seam where the two substrate layers attach |
| `harness/` | 5 | The agent program itself — Claude Code, pi, opencode, Factory Droid |
| `runtime/` | 3 | The execution substrate that spawns harnesses — sandboxes, parallelism, autonomy |
| `topic/` | 2 | Curated cross-cutting overlays (Maps of Content). **Not** ontology nodes — they store no edges |

Page counts are a snapshot (2026-08-31) and drift with every ingest; `wiki/catalogue.md` is always current.

Plus four files at the root of `wiki/`:

- **`CONVENTIONS.md`** — the schema layer. Node types, the nine relationship edges, frontmatter format, naming rules, the ingest workflow, and the discipline for when a new abstraction is allowed to exist. **Read this before any ingest.**
- **`index.md`** — the authored landing page.
- **`catalogue.md`** — the exhaustive per-namespace catalogue (split out of `index.md` in August 2026).
- **`log.md`** — append-only operation log. Every ingest, schema change, stage rename, and structural decision, with reasoning. It is the closest thing to a design history.

### How the pieces connect

Relationships live in each page's YAML frontmatter as `[[wikilinks]]`. A `capability` page carries most of them (`belongs_to`, `implements`, `produces`, `applies`, `delegates_to`, `equivalent_to`); `framework`, `harness` and `runtime` each carry one or two forward edges. Every other view is a **backlink** view — an artifact page's "Produced by" list is a hand-maintained reflection of the `produces:` edges pointing at it.

Two rules matter more than the rest, because breaking them silently corrupts the synthesis:

1. **Stages are derived, and framework-neutral.** A stage exists only where **≥2 frameworks** evidence the activity, and its name must be the most generic term covering every backlink — never one framework's branding. Stages are re-derived on every ingest (rename / split / merge / add / retire). Candidate splits that haven't yet cleared the two-framework bar are parked under a `## Split candidates` heading on the stage page.
2. **Topics never pollute the graph.** A `topic/` page links out to anything but stores no edges, counts as evidence for nothing, and is ignored by stage re-derivation. Deleting every topic page would leave the ontology intact.

## Provenance

This vault was built and is maintained with the **`karpathy-llm-wiki`** skill — [Astro-Han/karpathy-llm-wiki](https://github.com/Astro-Han/karpathy-llm-wiki), after Karpathy's idea that *"the LLM writes and maintains the wiki; the human reads and asks questions."*

- Installed **2026-06-27**, pinned at upstream commit `9e8c4f4` (2026-04-13).
- The wiki was initialised the same day — `wiki/log.md` opens with `## [2026-06-27] init | wiki initialized with SDLC agent-skill ontology`.
- Git history starts later (2026-07-18, "Baseline"): this was an Obsidian vault for three weeks before it was a repository, so early construction is recorded only in `log.md`, not in commits.

**What comes from the skill:** the `raw/` + `wiki/` split with immutable sources; `raw/<topic>/YYYY-MM-DD-slug.md` naming and its metadata header; `wiki/log.md` (headed `# Wiki Log`) and its `## [YYYY-MM-DD] <op> | <title>` entry format; the `# Knowledge Base Index` table of link + summary + Updated; the `sources` / `raw` / `updated` bookkeeping fields on every article; one level of topic directories, no deeper nesting.

**What is local invention**, layered on top:

- The entire ontology — seven node types, nine edges, the derived `sdlc-stage` projection, and the `topic/` overlay — defined in `CONVENTIONS.md`. The skill knows only "topic subdirectories".
- The log vocabulary grew beyond the skill's `ingest` / `query` / `lint` to include `init`, `docs`, `edit`, `schema`, `refactor`, `topic`, `fix`, `build`.
- `index.md` was split into an authored landing page plus `catalogue.md`, deliberately departing from the skill's "index.md is the global index" rule. `CONVENTIONS.md` was updated so future ingests write to the right file.
- Quartz publishing (below), which the skill knows nothing about.

**Known drift from upstream.** The installed `SKILL.md` predates a substantial upstream revision (2026-07-23/24) that added: a *Grounding Invariant* (every load-bearing number, date and quote in `wiki/` must appear verbatim in the linked raw file, verified by `scripts/check_evidence.py`); ingest **triage** with a "No material" stop path; `Status: Disputed` / `Status: Outdated` blocks instead of silently rewriting superseded claims; full-wiki cascade search rather than index-only; and source-fidelity rules. None of that is in force here, and this vault's pages were compiled without it. Upgrading is a real decision, not a routine bump — the newer rules would change how future ingests write against 330+ pages compiled under the older ones.

**Reference templates.** The skill was installed with `"skillPath": "SKILL.md"`, so only that file was fetched and the four `references/*.md` templates it points at were absent. They were restored on 2026-08-31 from the pinned commit (not from upstream HEAD, whose `article-template.md` assumes the Status blocks the installed `SKILL.md` never explains).

## Publishing

`.github/workflows/deploy.yml` builds the site with [Quartz](https://github.com/jackyzha0/quartz) v5 and deploys to GitHub Pages. Deliberately **"B-lean"**: the repo stays pure Markdown and Quartz is fetched at build time, so nothing about the static-site generator leaks into the vault. Every branch builds (validation); only `main` deploys.

One build step has consequences for how you write: **`.github/scripts/inject-titles.py` promotes each page's leading `# ` heading into frontmatter `title:` and removes it from the body**, because Quartz renders the frontmatter title and would otherwise show the filename. So:

- A page's `#` heading **is** its site title and browser-tab text. Write it as a real title, not a slug.
- A page may set `title:` explicitly to override; `index.md` and `catalogue.md` do.
- Known state: ~200 pages still carry a slug-style H1 (`# /gsd-execute-phase`, `# claude-code`). For command pages that is intentional; for others it is a lowercase stand-in. Deliberately not mass-rewritten — see the 2026-08-11 log entries.

## Working in this repo

- **Read `wiki/CONVENTIONS.md` first.** It is the schema, and the ingest workflow at the bottom is the checklist.
- **Write one line per paragraph.** No hard wrapping — the vault was reflowed to single-line paragraphs in July 2026 so Markdown renders correctly in both Obsidian and Quartz.
- **Every `[[wikilink]]` must resolve.** Create stub pages for new link targets during an ingest so nothing dangles.
- **Adding a framework** is a defined sequence: capture the source into `raw/`, create the framework page plus one capability page per command/skill/sub-agent with full frontmatter edges, stub any new artifact/pattern targets, set `equivalent_to:` against capabilities already documented elsewhere (this is what builds the cross-framework clusters), **re-derive the stage set**, then cascade — update affected stage projections, refresh `updated:`, add rows to `catalogue.md`, and append to `log.md`.
- **Log the reasoning, not just the change.** The log's value is that it records *why* a stage was split or a name generalised. Entries are immutable once written, even when later superseded.
- **Obsidian** is the local editing environment; `extended-graph` and `juggl` are configured for graph views coloured by node type. `.obsidian/workspace*.json` and caches are gitignored.

## Reading it

The [landing page](wiki/index.md) suggests routes by intent. The most directly actionable pages are the `topic/` overlays: **agent readiness** (can an agent work in this repo at all?) and **harness engineering** (how do you steer it?) — with a third, on the compounding loop that refines those controls over time, currently in review. For a specific question, the [catalogue](wiki/catalogue.md) lists every page by namespace; the eight [stage](wiki/sdlc-stage/index.md) pages double as a checklist of what a complete lifecycle has to cover, with every known implementation listed underneath.
