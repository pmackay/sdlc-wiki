---
type: capability
subtype: command
belongs_to: "[[seeds]]"
implements: []
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: []
sources: "Jaymin West — jayminwest/seeds README + AGENTS.md + SPEC.md (MIT, v0.5.15, 2026)"
raw: ["../../raw/seeds/2026-08-31-seeds.md"]
updated: 2026-08-31
---

# sd onboard

`sd onboard` — write a seeds section into the project's `CLAUDE.md` / `AGENTS.md`, so every future agent session learns the tracker exists without anyone remembering to say so.

It is the *persistent* half of the pair whose ephemeral half is [[seeds-prime]]: prime renders the briefing per session on request, onboard commits it to the memory file the harness auto-loads. The choice of both files is what makes seeds harness-portable without naming harnesses — `CLAUDE.md` for [[claude-code]], `AGENTS.md` for the cross-harness convention that [[opencode]] and others read.

The seeds repo dogfoods the result, and its own `AGENTS.md` shows what a fully-onboarded project looks like: a nine-step loop (prime → find unblocked work → claim → decompose if large → make focused changes → run the gates → pin debt markers → close & sync → record insights) with the `sd` commands inline at each step. That file is also the closest thing seeds has to a written methodology, which is part of why the framework classification holds at all.

Maps to **no canonical SDLC stage** — it configures the agent's environment rather than advancing work. It produces [[artifact-standards]] in the narrow sense that the memory file it edits is where a project's agent-facing conventions live.

## See Also
- [[seeds-prime]] — the per-session counterpart.
- [[seeds-issue-workflow]] — the deeper, skill-shaped version of the same instructions.
- [[claude-code]] · [[opencode]] — the memory-file conventions it targets.
- [[artifact-standards]] — what it writes into.
