---
type: capability
subtype: command
belongs_to: "[[tessl]]"
implements: []
delegates_to: []
produces: []
applies: ["[[pattern-deterministic-gates]]", "[[pattern-project-constitution]]"]
equivalent_to: []
sources: "Tessl docs — CLI v0.108.0 (2026)"
raw: ["../../raw/tessl/2026-09-12-tessl-platform.md"]
updated: 2026-09-12
---

# tessl workspace · org · api-key

The ownership and access boundary: `workspace create/list/delete/archive/unarchive`, `workspace add-member/remove-member/list-members`, `org list/usage`, `api-key create/list/delete`, plus SSO and role administration in the web app.

A **workspace** is the shared private home for a team's context — it holds privately published plugins, controls who can see them, and is where the [[tessl-inventory|inventory]] results and the private index live. It is the middle term of the layer's three nouns: a plugin is *content*, a project is *location*, a workspace is *ownership*.

This is where the layer's governance actually bites, and it is worth being precise about which mechanism does what:

- **RBAC** controls who may create, publish, and view.
- **Install policies** control what may be installed — the mechanism that *blocks*, as distinct from [[tessl-review-security]], which only warns.
- **Publish policies** and **required skills** push a standard outward: an org can mandate that certain skills are present in every workspace.
- A **full audit trail** records it.

*"RBAC, install and publish policies, security scoring, and a full audit trail are first class tools, not bolted on after the fact."* That claim is the layer's enterprise thesis, and it is the reason a registry is a different kind of object from a list of skills — the index is also the enforcement point.

**Required skills are the closest thing in the wiki to a mechanically-gated constitution that is not a document.** [[speckit]]'s [[artifact-constitution]] gates plans through a framework's own analysis step; this pushes a mandated capability set into every workspace from outside the framework entirely. Different layer, same instinct; noted on [[pattern-project-constitution]] rather than treated as evidence for the parked `stage-govern` split, which asks for a *framework* gating *project* principles.

## See Also
- [[tessl-review-security]] — scans and warns; install policy here is what blocks.
- [[tessl-inventory]] — scoped to and stored in the workspace.
- [[tessl-init]] — `tessl project` links a repository to a workspace.
- [[tessl-environment]] — secrets and MCP wiring, scoped the same way.
