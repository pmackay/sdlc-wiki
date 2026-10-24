---
type: index
sources: "Synthesized from Agent Skills (agentskills.io), AGENTS.md (agents.md), and the Model Context Protocol specification 2026-07-28, read against the wiki's paged nodes"
updated: 2026-10-24
---

# Standard

*The contract layer — the open specs that products across every other layer agree on, so that what one writes, another can read.*

The wiki's other five layers are **products**: somebody ships a [framework](../catalogue.md#framework), a [harness](../harness/index.md), a [runtime](../runtime/index.md), a [store](../store/index.md), or a [registry](../registry/index.md). A **standard** is owned by none of them. It is the reason a skill written for Claude Code also loads in OpenCode, pi, and Factory Droid, the reason a store can introduce itself to *"any agent"* by writing one file, and the reason one registry integration reaches nine harnesses.

Each page records the spec as published and its **adoption roster**: the `conforms_to:` edges from paged nodes whose own docs claim the standard. An edge means documented adoption, not a validator pass. For a protocol it also needs an endpoint (a client or a server), so a framework that only *calls* MCP tools gets prose, not an edge. The rules are in [CONVENTIONS §The contract layer](../CONVENTIONS.md#the-contract-layer-standards).

## Members

| Standard | Subtype | Steward | Version | What it is |
|---|---|---|---|---|
| [[std-agent-skills]] | `format` | Agent Skills project (originally Anthropic) | unversioned | A skill is a folder with a `SKILL.md`: `name` + `description` frontmatter, a Markdown body, optional `scripts/` · `references/` · `assets/`, loaded by progressive disclosure. 46 listed adopters. |
| [[std-agents-md]] | `format` | Agentic AI Foundation (Linux Foundation) | unversioned | *"A README for agents"*: plain Markdown at the repo root, nearest file wins, user prompts override, listed checks get run. No required fields. 60k+ projects. |
| [[std-mcp]] | `protocol` | MCP, a Series of LF Projects (Steering Group, SEPs) | 2026-07-28 | JSON-RPC 2.0 between a host's client and a server offering resources, prompts, and tools; stateless since 2026-07-28; opt-in extensions including Skills over MCP. |

## Adoption matrix (the `conforms_to:` inverse)

✅ = stored `conforms_to:` edge · ◽ = documented in prose without an edge (see the note) · blank = no documented adoption.

| Node | Layer | [[std-agent-skills]] | [[std-agents-md]] | [[std-mcp]] |
|---|---|---|---|---|
| [[claude-code]] | harness | ✅ | | ✅ |
| [[opencode]] | harness | ✅ | ✅ | ✅ |
| [[pi]] | harness | ✅ | ✅ | ◽ extension only |
| [[factory-droid]] | harness | ✅ | ✅ | ✅ |
| [[tessl]] | registry | ✅ validates against the spec | | ✅ ships the server |
| [[beads]] | store | | ✅ `bd init` writes it | ✅ `beads-mcp` |
| [[seeds]] | store | | ✅ `sd onboard` writes it | |
| [[bernstein]] | runtime | ✅ skill packs | | ✅ ships a server |
| [[sssf]] | runtime | ✅ is a skill | | |
| [[gh-aw]] | runtime | | | ✅ MCP Gateway |
| [[warren]] | runtime | | | ◽ roadmap |
| [[warp-factories]] | runtime | ✅ factory skills | | ✅ Factory MCP |
| [[superpowers]] | framework | ✅ cites the spec | | |
| [[addy-agent-skills]] | framework | ✅ | | ◽ consumer |
| [[bmad]] | framework | ✅ | | |
| [[bm-skills]] | framework | ✅ | ✅ writes it | |
| [[builder-skills]] | framework | ✅ | ✅ writes it | ◽ consumer |
| [[gstack]] | framework | ✅ | | |
| [[matt-pocock-skills]] | framework | ✅ | ◽ symlink to `CLAUDE.md` | |
| [[nano-spec]] | framework | ✅ | ✅ writes it | |
| [[pstack]] | framework | ✅ | | ◽ consumer |
| [[artifact-skill-doc]] | artifact | ✅ | | |

Frameworks absent from the matrix ([[gsd]], [[speckit]], [[openspec]], [[agent-os]], [[compound-engineering]]) have captured sources that do not document any of the three formats. That is a gap in the sources, not evidence they don't use them.

## What the matrix shows

**Agent Skills is the closest thing to a universal format in the wiki.** All four paged harnesses, nine of fourteen frameworks, three runtimes, and the one registry conform. That is the "framework is coming apart" observation from the [registry layer](../registry/index.md) with its precondition made explicit: a capability can only become an independently installable unit because there is a shared format for one.

**`AGENTS.md` has one conspicuous hole, and the rest of the wiki works around it.** Claude Code reads `CLAUDE.md` instead, and it is the harness almost every framework targets first. So the tools that write context files write **both** ([[builder-skills]], [[bm-skills]], [[seeds]]), [[matt-pocock-skills]] symlinks one to the other, and [[factory-droid]] calls its `AGENTS.md` `CLAUDE.md`-compatible. A standard everyone else adopted, minus the market leader, produces exactly this dual-file tax.

**MCP is the only standard with a real process, and the only one a harness opted out of.** It has dated revisions, a changelog, SEPs, named maintainers, and a twelve-month deprecation window, where the two formats have none of those. And [[pi]] keeps it out of core on purpose. So the most formally governed standard is also the one whose adoption is most clearly a design choice.

**The standards are converging.** MCP's *Skills over MCP* extension would carry Agent Skills over the protocol, [[bernstein]] already serves skill bodies through an MCP `load_skill` tool, and [[tessl]] delivers installed context to every harness as MCP tools. If that holds, the skill moves from a file in the repo to something a server offers, which is the supply layer's thesis expressed as a protocol.

## The synthesis axis

With three members the dimensions live as the tables above and prose per page, not as a derived namespace: **subtype** (format \| protocol) · **steward & governance model** · **licence** · **versioning scheme** (dated revisions, semver, none) · **required surface** · **extension mechanism** · **validator / reference implementation** · **deprecation policy** · **adoption breadth**.

## The queue

| Instance | Subtype | Why it is not paged yet |
|---|---|---|
| **A2A** (agent-to-agent) | `protocol` | One paged adopter ([[bernstein]], `core/protocols/`). Needs a second. |
| **Agent Client Protocol** (editor ↔ agent) | `protocol` | One paged adopter ([[bernstein]]). Needs a second. |
| **OpenClaw registry protocol** | `protocol` | Claimed by JFrog's skills registry, which is not paged. |
| **llms.txt** | `format` | One mention in the wiki. Both agentskills.io and modelcontextprotocol.io publish one, which is a hint of where it is heading. |

Not standards, by the boundary test, and staying as prose on their owners' pages: Claude Code's `plugin.json` and `CLAUDE.md`, Codex's `agents/openai.yaml`, Cursor's plugin manifests and `.mdc` rules.

## See Also
- [Registry layer](../registry/index.md) — distributes capabilities *in* these formats; the nearest neighbour.
- [Harness layer](../harness/index.md) — the main adopters, and the matrix whose "skill / command format", "MCP", and "memory & context files" rows this layer gives a home to.
- [[pattern-context-engineering]] — all three standards are contract-side forms of it.
- [[topic-harness-engineering]] — the guide (feedforward) layer that `AGENTS.md` and skills carry.
