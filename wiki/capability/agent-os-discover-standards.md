---
type: capability
subtype: command
belongs_to: "[[agent-os]]"
implements: []
delegates_to: []
produces: ["[[artifact-standards]]"]
applies: ["[[pattern-context-engineering]]", "[[pattern-knowledge-compounding]]", "[[pattern-grilling]]"]
equivalent_to: []
sources: "Agent OS v3.0.0 — discover-standards (2026)"
raw: ["../../raw/agent-os/2026-08-05-agent-os.md"]
updated: 2026-08-05
---

# Agent OS: discover-standards

`/discover-standards` — extract a codebase's **tribal knowledge into documented [[artifact-standards|standards]]**, the first move of Agent OS's Discover → Inject → Build → Refine loop. It *"walks you through identifying patterns worth documenting, then creates concise standards files."* Six phases: (1) **focus-area selection** — analyzes the codebase and presents 3-5 major areas (API routes, database, components, auth…) via AskUserQuestion; (2) **pattern analysis** — reads 5-10 representative files and finds patterns that are *unusual, opinionated, tribal, or consistent*; (3) **per-standard development** — asks 1-2 **"why" questions**, drafts, confirms, one standard at a time; (4) writes `agent-os/standards/[folder]/[standard].md`; (5) updates `index.yml` (delegating to [[agent-os-index-standards]] as its final step); (6) offers to continue with another area.

It is the **authoring end of the guide layer** in [[topic-harness-engineering]]: it turns the *"we don't do it that way here"* intuition an agent lacks into an externalized, machine-readable convention. Two design choices set it apart from a naive rules-file dump:

- **Only unconventional patterns.** *"Document only unconventional patterns, not framework defaults"* — it deliberately skips what a good model already knows, keeping standards to the non-derivable kernel. This is [[topic-harness-engineering#How they adapt as models improve|"as models improve, delete the derivable guides"]] as an authoring rule.
- **Rationale capture.** The 1-2 "why" questions per standard mean each convention records *why*, not just *what* — closer to an [[artifact-adr]] than a lint rule. This is a lightweight [[pattern-grilling|interview]].

Because refined standards later `sync-to-profile` and re-inject into future projects, discover-standards seeds a [[pattern-knowledge-compounding|compounding]] loop over *standards themselves* — the steering loop of harness engineering, applied to conventions.

## See Also
- [[agent-os-index-standards]] — the maintenance step discover-standards calls to keep the matcher current.
- [[agent-os-inject-standards]] — the consuming side: deploys these standards into context.
- [[artifact-standards]] — the artifact this produces.
- [[speckit-constitution]] — the *gated, up-front, human-authored* counterpart; discover-standards instead *mines existing code* and produces *advisory, injected* standards (see the `stage-govern` split candidate on [[stage-align]]).
- [[bmad-document-project]] — the brownfield-investigation neighbor (documents architecture/domain for AI context rather than coding standards).
- [[topic-harness-engineering]] — the guide/sensor/steering-loop frame this sits in.
