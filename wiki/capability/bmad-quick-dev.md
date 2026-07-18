---
type: capability
subtype: skill
belongs_to: "[[bmad]]"
implements: "[[stage-implement]]"
delegates_to: []
produces: ["[[artifact-spec-md]]", "[[artifact-atomic-commit]]"]
applies: ["[[pattern-scale-adaptive-planning]]"]
equivalent_to: []
sources: "bmad-code-org/BMAD-METHOD — bmad-quick-dev / bmad-dev-auto (2026)"
raw: ["../../raw/bmad/2026-07-04-bmad-method-framework.md"]
updated: 2026-07-04
---

# bmad-quick-dev

**`bmad-quick-dev`** — the **Quick Flow** fast path, owned by [[bmad-dev]]: "Intent in, code changes out, with as few human-in-the-loop turns as possible — without sacrificing quality." It bypasses phases 1–3 for small, well-understood work, routing on blast radius: "Small, zero-blast-radius changes can go straight to implementation. Everything else goes through planning." Three human checkpoints (intent, spec, review) → a `spec-*.md` ([[artifact-spec-md]]) plus code.

Quick Flow is the sharpest expression of BMAD's [[pattern-scale-adaptive-planning|scale-adaptive]] principle — the whole four-phase pipeline collapses to a few turns when the work is trivial. Its unattended sibling **`bmad-dev-auto`** runs "one unattended development-loop iteration" (clarify → spec → implement → review → terminal status), resuming from spec status and halting with a `blocked` state for an orchestrator to read.

## See Also
- [[bmad]] — the framework.
- [[bmad-dev-story]] — the full-ceremony implementation path Quick Flow shortcuts.
- [[bmad-spec]] — produces the lightweight SPEC kernel Quick Flow plans against.
- [[stage-implement]] — the canonical stage.
