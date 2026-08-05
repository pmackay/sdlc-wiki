---
type: capability
subtype: command
belongs_to: "[[agent-os]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Agent OS v3.0.0 — inject-standards (2026)"
raw: ["../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Agent OS: inject-standards

`/inject-standards` — **deploy the relevant [[artifact-standards|standards]] into the current context**, on demand. This is the consuming half of Agent OS and the wiki's **purest expression of [[pattern-context-engineering]]** — *right context, right time*, made an explicit, invocable act. Two modes: *auto-suggest* (bare `/inject-standards` analyzes the conversation and recommends from `index.yml`) and *explicit* (`/inject-standards api/response-format` injects a named file). Three steps: **context detection** (are we coding, building a skill, or planning?) → **matching** (reads `index.yml`, matches descriptions against the context, presents 2-5 standards to confirm) → **injection**.

The injection step surfaces a design choice most frameworks leave implicit — the **payload mode**:

- **Conversation mode** loads the full standard content into the window.
- **Skill / Plan mode** offers a choice between **file references** (a pointer that stays current as the standard evolves) and **embedded snapshots** (self-contained, versioned copy).

That reference-vs-embed tradeoff is exactly the [[topic-harness-engineering|guide-layer]] question of *freshness vs self-containment*: a reference tracks the living standard but can drift from what was reviewed; an embed freezes what was agreed but goes stale. Injection also **surfaces relevant Skills** (mentions them) without auto-invoking — reinforcing Agent OS's *Standards (what) vs Skills (how)* split, where standards are **explicitly invoked** and skills auto-detect.

Because it neither authors a lasting artifact nor performs a lifecycle stage — it *loads* the guide layer into a working context — it carries no canonical stage.

## See Also
- [[agent-os-index-standards]] — supplies the `index.yml` this matches against.
- [[agent-os-discover-standards]] — authors the standards this injects.
- [[pattern-context-engineering]] — the pattern this most fully realizes; compare the harness-side `CLAUDE.md`/`AGENTS.md` primitives.
- [[topic-harness-engineering]] — guides (feedforward) and the reference-vs-embed tradeoff.
