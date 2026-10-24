---
type: index
sources: "Synthesized from Tessl docs (2026); unpaged instances from public documentation — JFrog, Google Cloud, ClawHub, Agensi"
updated: 2026-10-11
---

# Registry

*The supply layer — the versioned index capabilities are discovered in, vouched for, and installed from, before any run begins.*

The wiki's other four layers all describe a **run**: a [framework](../catalogue.md#framework) is the instructions it follows, a [harness](../harness/index.md) is the loop that executes them, a [runtime](../runtime/index.md) decides where that loop runs, and a [store](../store/index.md) is the state it leaves behind. A **registry** describes what happened *before* the run — where the capabilities came from, who scanned and scored them, and what policy allowed to be installed.

This layer appears at the moment capabilities stop being something you write and become something you **acquire**. [[tessl]] states the premise directly:

> **Context as code.** Skills, rules, and docs are versioned, reviewed, and rolled out with the same rigor as code dependencies.

A registry performs no [SDLC stage](../sdlc-stage/index.md) as a layer, and connects to the ontology through `integrates_with:` → harness, `enables:` → pattern, and `distributes:` → framework \| capability, plus the `belongs_to:` backlinks from its own command surface. The full schema is in [CONVENTIONS](../CONVENTIONS.md#the-supply-layer-registries).

## Members

| Registry | Subtype | What it is | Surface | Updated |
|---|---|---|---|---|
| [[tessl]] | `platform` | *"An open platform for managing agentic development across your organization."* Registry and package manager, governance (RBAC, install/publish policy, Snyk scanning), evals, observability, org inventory, and a platform agent. Founded by Snyk's Guy Podjarny; pivoted away from its own framework product to build this. | 101 commands · 20 pages | 2026-09-12 |

One instance paged. The node was minted on one because the **category** is unambiguous even where the wiki's coverage is not — see the queue below.

## The queue

| Instance | Shape | Why it matters |
|---|---|---|
| **JFrog Agent Skills Registry** | `platform`, private-first | The canonical package-registry incumbent entering the space: scanned, signed, approved skills served from a private registry, claiming the **AgentSkills** format and the **OpenClaw registry protocol**. An incumbent arriving is the strongest category signal available. |
| **Google Cloud Skill Registry** | `platform`, private | A hyperscaler shipping a private, low-latency skill repository inside the Gemini Enterprise Agent Platform. |
| **ClawHub** | `index` | Community registry with vector search over skills and gateway plugins — the discovery-only pole, and the evidence that made `index` a subtype rather than an edge case. |
| **Agensi** | `index` | Marketplace for `SKILL.md` skills and MCP servers with curation, security scanning, and a creator revenue split. The commercial-marketplace shape. |

Not a registry: the **AgentSkills format** that JFrog and Tessl both claim is a *standard*, paged in the [contract layer](../standard/index.md) as [[std-agent-skills]]; the agentskills.io client showcase is a list of its adopters, not an install index. **Smithery** is a registry of **MCP servers** — tools rather than capabilities — which is the adjacent-artifact case the [conventions](../CONVENTIONS.md#the-supply-layer-registries) tell you to record rather than blur.

## The boundary test

**An independent product, not a vendor's shelf.** A marketplace shipped by a harness vendor for its own harness — Anthropic's plugin marketplace, `cursor/plugins`, opencode's community registry, Droid's plugin bundles — is a **harness feature**. It stays a row in the [harness matrix](../harness/index.md) and gets no node. A `registry` is a separate product distributing capabilities across harnesses it does not own.

Two consequences worth stating, because both are live cases in this wiki:

- **[[pstack]] ships through `cursor/plugins`, and that does not make `cursor/plugins` a registry.** It is Cursor's shelf for Cursor. The install route stays prose on the framework page.
- **[[bm-skills]] stays a `framework`, and the tension is real.** It is a Claude Code plugin *marketplace* of unrelated utilities whose own page says it is *"deliberately not a full-SDLC framework"* — so it reads like a registry. But it fails the test in both directions: it is single-harness, and it is a GitHub repo of three skills rather than a product that distributes anyone else's work. It is best understood as a **framework whose bundle is unusually loose**, which is the thing the framework node already strains to cover. Re-file it only if it starts carrying third-party skills.

## The synthesis axis

With one member paged, the shared dimensions live here as prose rather than a matrix — the same discipline parked for the [runtime](../runtime/index.md), [harness](../harness/index.md), and [store](../store/index.md) dimensions. The dimensions to fill in as instances arrive:

**unit of distribution** (skill \| plugin \| bundle) · **index visibility** (public \| private \| both) · **versioning & rollback** · **provenance & signing** · **security scanning** · **quality scoring** · **impact measurement (evals)** · **policy & RBAC** · **audit trail** · **estate inventory** · **harness-agnosticism** · **open format vs proprietary** · **self-host vs SaaS**

Public-vs-private is a dimension here and not a subtype, because the platforms are generally both at once: Tessl runs a public registry and private per-team workspaces off the same index. The subtype axis is how much of the supply chain the product owns — a searchable `index` versus a governed `platform`.

## What one instance already shows

**The layer reproduces the review ∥ validate split, independently.** Tessl ships a **review** (is the skill well written? — fast, structural, automatic on publish) and a **scenario eval** (does it work? — run the agent with and without it, score the difference) and is explicit that they answer different questions. That is [[stage-review]] ∥ [[stage-validate]] arrived at from the supply side, by a company with no knowledge of this wiki. Convergence of that kind is the main thing the wiki produces, and finding it in a new layer on the first ingest is a good sign the layer is real.

**Instructions are now an attack surface.** [[pattern-supply-chain-scanning]] is the layer's genuinely new pattern: scanning a capability for prompt injection buried in its text, hardcoded secrets, suspicious download URLs, and hidden or obfuscated content. Every guardrail pattern already here bounds what the agent may *write* ([[pattern-edit-guardrails]]) or *reach* ([[gh-aw]]'s egress firewall). This bounds what it may *read*. Installing a skill from a public index is running someone else's prompt with your agent's permissions, and this is the layer that noticed.

**The framework is coming apart.** The wiki's core claim is that a framework is a bundle of capabilities. A registry makes the capability the independently versioned, installable unit, and four paged frameworks ([[superpowers]], [[addy-agent-skills]], [[compound-engineering]], [[pstack]]) already ship *through* a marketplace rather than as a download. Treat growth in this layer as the leading indicator that `framework` is becoming a distribution convenience rather than a methodology boundary.

**The layer leans toward the factory.** Tessl already ships agent launching, cloud runs, and cron schedules, and says out loud that it takes you *"from scaling skills to building your software factory"*. A supply platform that can also run what it distributes is one product decision away from being a [runtime](../runtime/index.md). Watch the boundary; see the [honest note](tessl.md#the-layer-boundary-honestly) on the Tessl page.

## See Also
- [[tessl]] — the anchor instance.
- [Store layer](../store/index.md) — the nearest neighbour. Both are durable, agent-facing, and off-stage; a store holds what a run produced, a registry holds what a run is provisioned from. Opposite sides of the same session.
- [Harness layer](../harness/index.md) — what registries integrate *with*, and where vendor marketplaces stay as a matrix row.
- [[topic-ai-native-sdlc]] — the org-level governance frame this layer implements commercially.
- [[topic-harness-engineering]] — the guide layer that registries distribute.
- [CONVENTIONS](../CONVENTIONS.md#the-supply-layer-registries) — the schema, the boundary test, and the ingest procedure.
