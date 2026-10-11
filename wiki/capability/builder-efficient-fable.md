---
type: capability
subtype: skill
belongs_to: "[[builder-skills]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-model-tiering]]", "[[pattern-fresh-context-subagents]]", "[[pattern-wave-parallelism]]", "[[pattern-evidence-before-claims]]"]
equivalent_to: ["[[builder-efficient-frontier]]"]
sources: "Builder.io — BuilderIO/skills, MIT (2026)"
raw: ["../../raw/builder-skills/2026-09-26-builder-skills.md"]
updated: 2026-09-26
---
# /efficient-fable

Use **Claude Fable as orchestrator, architect, synthesizer, and final judge**, and send the token-heavy research, coding, testing, and log reduction to cheaper subagents. *"Fable should spend tokens on judgment, not on reading every file, reducing every log, or manually running every browser check."*

Fable keeps five jobs: decomposing ambiguous work into parallel slices, architecture and product tradeoffs, reading conflicting subagent reports, integrating partial implementations, and final review. Delegation is written as **handoff packets**, *"as if the subagent has no useful chat context"*. Each packet names the repo path, objective, in-scope and out-of-scope surfaces, the evidence format to return, verification commands, and stop conditions.

**Vetting is not delegated.** *"Treat subagent reports as leads, not facts. Before using a high-impact finding, opening a PR, or telling the user the work is done, Fable should reopen the important cited files, confirm the relevant line refs or failures, and review the final diff."* The skill includes a performance claim (*"up to 3-5x more cost-efficient and 2-4x faster"* when work parallelizes) and labels it *"workload-dependent estimates, not guarantees."*

Off-stage. One of the two capabilities that anchor [[pattern-model-tiering]].

## See Also
- [[builder-efficient-frontier]] — the model-agnostic generalization.
- [[builder-stay-within-limits]] — the budget pause that pairs with it.
- [[pattern-model-tiering]] — the pattern minted from this pair.
