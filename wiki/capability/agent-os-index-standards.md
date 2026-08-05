---
type: capability
subtype: command
belongs_to: "[[agent-os]]"
implements: []
delegates_to: []
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Agent OS v3.0.0 — index-standards (2026)"
raw: ["../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Agent OS: index-standards

`/index-standards` — maintain **`agent-os/standards/index.yml`**, the map from each standard to a one-sentence description that lets [[agent-os-inject-standards]] *match relevant standards without reading every file*. Seven steps: scan `agent-os/standards/` (subfolders by domain; `root` for top-level) → load the existing index → diff (new / deleted / unchanged) → for each new file, read it and propose a one-sentence description (user-confirmed) → auto-remove stale entries → write the index alphabetized (`root` first) → report counts. Run it after hand-creating or deleting standards; [[agent-os-discover-standards]] runs it automatically as its last step.

This is pure **[[pattern-context-engineering|context-engineering]] plumbing**: the index is what makes the guide layer *scale* without blowing the context window. Rather than loading every convention every time (the failure mode of a bloated `CLAUDE.md`), the one-line descriptions let the injector pull only what the current task needs — *"Every word costs tokens."* The matcher, not the standards, is the real innovation: it turns a pile of convention files into a retrievable, token-budgeted resource.

## See Also
- [[agent-os-inject-standards]] — the consumer of `index.yml`; matches its descriptions against the current context.
- [[agent-os-discover-standards]] — the author of standards; calls this as its final step.
- [[artifact-standards]] — the standards corpus this indexes.
- [[topic-harness-engineering]] — why a token-budgeted matcher matters for the guide layer.
