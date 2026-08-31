---
title: SDLC Agent-Skill Wiki
---

**A comparative map of the toolkits people have built to make AI coding agents follow a software development lifecycle — and a synthesis of what they all turn out to agree on.**

A wave of open-source "agent frameworks" appeared through 2026: GSD, Spec Kit, BMAD, OpenSpec, Superpowers, gstack, Compound Engineering, Agent OS and others. Each ships a bundle of slash-commands, skills, and sub-agents that walk a coding agent from a vague idea to merged code. They use different vocabulary, disagree about ceremony, and are mostly documented only by their own READMEs — so it is genuinely hard to tell whether two of them are doing the same thing under different names.

This wiki reads them side by side. Every framework is decomposed into its individual capabilities, each capability is tagged with the lifecycle stage it performs and the techniques it applies, and matching capabilities across frameworks are linked to one another. What emerges from those links — rather than from anyone's opinion — is a **canonical eight-stage lifecycle** and a set of recurring **patterns** that most frameworks independently converged on.

It currently covers **12 frameworks**, **230 capabilities**, **36 artifacts**, **31 patterns**, **4 agent harnesses**, and **3 execution runtimes**.

## How it is organised

Three layers, from *what the agent does* down to *where it runs*:

- **Process layer** — a **[framework](catalogue.md#framework)** ships **[capabilities](catalogue.md#capability)** (commands, skills, sub-agents). Each capability performs one canonical **[sdlc-stage](catalogue.md#sdlc-stage)**, produces **[artifacts](catalogue.md#artifact)**, and applies **[patterns](catalogue.md#pattern)**.
- **[Harness](catalogue.md#harness) layer** — the agent program itself (Claude Code, Droid, opencode, pi): the loop that loads those skills and executes tool calls. Frameworks *run on* a harness.
- **[Runtime](catalogue.md#runtime) layer** — the substrate deciding *where and how* agents run: sandboxes, parallelism, unattended autonomy, branch→PR. Runtimes *spawn* harnesses.

Two page types are derived rather than authored. **Stage** pages are synthesised purely from the capabilities that link to them — they are evidence summaries, not opinions, and get re-derived on every ingest so the stage names stay neutral rather than borrowing one framework's branding. **[Topic](catalogue.md#topic)** pages are the opposite: hand-written essays that cut across everything else.

The full schema — node types, relationship edges, naming rules, and the discipline for when a new abstraction is allowed to exist — is in **[CONVENTIONS](CONVENTIONS.md)**.

## Ways to use it

**Choosing a framework.** Start at the **[framework catalogue](catalogue.md#framework)**. Each entry states the framework's shape, its signature idea, which stages it covers and which it skips, and how heavy it is. Useful contrasts: [Spec Kit](framework/speckit.md) (gated, maximalist, the reference spec-driven implementation) vs [nano-spec](framework/nano-spec.md) (four tiny files) vs [Superpowers](framework/superpowers.md) (a complete methodology from 14 auto-triggering skills) vs [Agent OS](framework/agent-os.md) (deliberately owns only the front of the lifecycle).

**Borrowing one good idea instead of adopting a whole framework.** Most teams don't want another methodology; they want the two or three moves that actually work. Browse the **[capability catalogue](catalogue.md#capability)** or a **[stage](catalogue.md#sdlc-stage)** page, find the cluster of frameworks solving the same problem, and take the best-shaped version. Cross-framework counterparts are linked on every page.

**Finding the high-confidence practices.** The **[pattern](catalogue.md#pattern)** pages record how many independent frameworks converged on each technique. A pattern shared by eight frameworks that never talked to each other is a much stronger signal than any single project's README — that is the main thing this wiki produces that reading the sources individually cannot.

**Designing your own skill library.** The eight **[stage](catalogue.md#sdlc-stage)** pages are a checklist of what a complete lifecycle has to cover, with every known implementation of each stage listed underneath. Use them to find your gaps — most homegrown setups are missing [review](sdlc-stage/stage-review.md) as distinct from [validate](sdlc-stage/stage-validate.md), or [learn](sdlc-stage/stage-learn.md) entirely.

**Improving the repo the agent works in.** Before adopting any process, check whether your codebase can support one. **[Agent readiness](topic/topic-agent-readiness.md)** covers the two public scoring rubrics for exactly that, and the sibling **[harness engineering](topic/topic-harness-engineering.md)** covers how to steer agents toward your conventions and refine that over time. These two topics are the most directly actionable pages here.

**Picking the substrate.** The **[harness matrix](harness/index.md)** compares agent programs on sub-agents, MCP, hooks, permissions, and model access; the **[runtime matrix](runtime/index.md)** compares isolation, parallelism, autonomy, and steering. Both are decisions people usually make by default rather than deliberately.

**Getting oriented in the field.** Read [CONVENTIONS](CONVENTIONS.md) for the vocabulary, then any two framework pages. The **[visual artifact index](artifact/index.md)** shows how the documents these tools produce flow into one another across a whole lifecycle.

## Provenance

Every article is compiled from captured primary sources — each framework's own documentation and source, archived unmodified before compilation. Pages cite what they were built from and when. The change history, including the reasoning behind every schema decision and stage rename, is in the **[log](log.md)**.

Nothing here is a benchmark: the wiki records what these tools *claim and contain*, not measured outcomes. Star counts and version numbers are as-of their capture date.

---

## The full catalogue

Every article in the wiki, one section per namespace, is listed on a single page: **[Catalogue](catalogue.md)** — [framework](catalogue.md#framework) · [capability](catalogue.md#capability) · [sdlc-stage](catalogue.md#sdlc-stage) · [artifact](catalogue.md#artifact) · [pattern](catalogue.md#pattern) · [harness](catalogue.md#harness) · [runtime](catalogue.md#runtime) · [topic](catalogue.md#topic).
