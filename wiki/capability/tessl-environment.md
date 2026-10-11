---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-contract-first]]", "[[pattern-idempotent-operations]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl environment

Named, workspace-scoped bundles of configuration and secrets: `environment create/list/view/update/delete`, loaded from a dotenv file and able to **wire workspace MCP servers into the environment**.

It exists because of what the layer distributes. A [[artifact-capability-bundle|plugin]] can carry MCP servers, and an MCP server usually needs credentials — so the moment a registry ships tools rather than only text, it inherits a secrets-management problem. Environments are where that lands: the credential stays in the workspace rather than in the bundle, and the bundle stays shareable.

The update semantics are strict and the docs flag them: an update **replaces** an environment's values from the supplied file rather than merging, so every value you want to keep has to be present, and rewiring MCP servers replaces the credential set too. That is [[pattern-idempotent-operations]] chosen over convenience, and it is the safer default for a secret store.

Environments also feed the cloud execution surface — [[tessl-launch]] and [[tessl-eval]] can pass secrets into a sandboxed run, which is what makes a cloud eval able to exercise a skill that talks to a real service.

## See Also
- [[tessl-mcp]] — the gateway these credentials configure.
- [[tessl-launch]] — consumes an environment for a sandboxed cloud run.
- [[tessl-workspace]] — the scope environments belong to.
