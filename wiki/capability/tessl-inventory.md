---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: ["[[artifact-review-report]]"]
applies: ["[[pattern-supply-chain-scanning]]", "[[pattern-knowledge-compounding]]"]
equivalent_to: ["[[beads-rules]]"]
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl inventory

Scan a source-control organization and index every skill and configuration file across every repository: `tessl inventory import`, plus GitHub App / GitLab token / Bitbucket integrations managed at org level in the web app. Results land as **Context** (what exists, and which repo each item lives in) and **Findings** (issues, ranked by severity).

The pitch is four words — ***"govern what you can see"*** — and it names a real precondition. Before anyone can apply a policy, fork a rubric, or de-duplicate a corpus, they have to know what the organization actually has, and a skill estate accumulates invisibly: copied between repos, forked and drifted, vendored and forgotten. *"Surface duplicates and unmanaged copies."*

This is the layer's answer to a problem the wiki has watched frameworks create. Every framework here encourages writing more skills, and several ([[gstack-skillify]], [[sp-writing-skills]], [[pstack-reflect]], [[ce-compound]]) make skill-creation a first-class lifecycle step under [[stage-learn]]. **Nothing in the process layer manages the resulting sprawl.** [[beads-rules]] is the nearest thing — it audits `.claude/rules/` for contradictions and merges near-duplicates — but it works one repository at a time. Inventory is the same instinct at org scale.

Honest about its own limits, in a way worth preserving: connecting an integration authorizes reading, but provisioning an inventory and starting a scan are *"best-effort and separate from the connection"*, so **a successful connection does not guarantee a scan**. Org-level inventories are gated per organization.

## See Also
- [[tessl-review-security]] — what you run over the estate once you can see it.
- [[tessl-workspace]] — where the inventory and its private index live.
- [[beads-rules]] — the store layer's single-repo counterpart for the same sprawl problem.
- [[pattern-knowledge-compounding]] — the process-layer engine that produces the sprawl this measures.
