---
type: capability
subtype: command
belongs_to: "[[beads]]"
implements: []
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-context-engineering]]"]
equivalent_to: ["[[seeds-onboard]]"]
sources: "gastownhall/beads — docs/CLI_REFERENCE.md + docs/multi-agent + docs/architecture (MIT, 2026)"
raw: ["../../raw/beads/2026-08-31-beads.md"]
updated: 2026-08-31
---

# bd setup

`bd setup <recipe>` — write beads' workflow instructions into the file *a specific harness reads*, and install its hooks. `bd setup --list` enumerates the recipes; `bd onboard` prints a minimal snippet to paste by hand for anything unsupported.

Thirteen built-in recipes: **claude** (hooks and settings), **codex** (skill, `AGENTS.md` guidance, and hooks), **factory** (`AGENTS.md`), plus cursor, copilot, gemini, aider, mux, opencode, junie, windsurf, cody, and kilocode.

**This command is why a store gets an `integrates_with:` edge at all.** A framework `runs_on:` a harness because its skills are written in that harness's format; a store integrates because it must get itself *mentioned* — an agent that does not know `bd` exists will write a markdown TODO list instead, which is precisely the failure the tool was built against. So beads ships a per-harness installer, and the minimal instruction it wants present is four lines:

> This project uses bd (beads) for issue tracking. Run `bd prime` for workflow context. Use `bd ready`, `bd show <id>`, `bd update <id> --claim`, `bd close <id>`. Use `bd remember "insight"` for persistent project memory; do not create MEMORY.md files. **Do not use markdown TODO lists for task tracking.**

The recipe list is also the layer's most concrete evidence of harness-agnosticism — thirteen targets, of which [[claude-code]], [[factory-droid]], and [[opencode]] have pages here and carry the stored edges; the rest stay prose per the support-scope rule.

Maps to **no canonical SDLC stage**. It produces [[artifact-standards]] in the narrow sense that the memory file it writes is where a project's agent-facing conventions live.

## See Also
- [[beads-prime]] — what the installed hook calls at session start.
- [[beads-hooks]] — the git-hook half of the same job.
- [[beads-rules]] — the other command that operates on a harness's guide layer.
- [[seeds-onboard]] — the cross-store counterpart, with three targets instead of thirteen.
