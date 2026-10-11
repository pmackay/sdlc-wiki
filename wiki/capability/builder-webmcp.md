---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-evidence-before-claims]]"]
equivalent_to: []
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /webmcp

Open a URL in the host's **built-in browser** and complete the request through the page's own **WebMCP** tools (`document.modelContext`) rather than through UI automation. *"The two rules: 1. Open in the host's built-in browser … 2. Call the page's tools. Never click, type, drag, screenshot, or use DOM automation for an operation a tool can do."*

The fast path is short. With no request, open the page and stop. With a request, the budget is *"about three page calls: read the screen, mutate, read back. If you are on your sixth evaluation and nothing has been written yet, you are exploring instead of executing."* The rest of the skill documents host-specific workarounds: evaluators for Claude Code, Cowork, and Codex; a hidden pane throttling tool registration (*"217 tools immediately when fronted … 59 after 28 seconds when hidden"*); and a timed-out evaluator being *"an unread result, not a failed write."*

Off-stage. The transferable idea is **one read, one smallest mutation, one readback**, which is the edit discipline in its simplest form.

## See Also
- [[builder-an]] — the Dispatch-hosted version.
- [[builder-visual-edit]] — the same WebMCP bridge applied to a local app in Design.
